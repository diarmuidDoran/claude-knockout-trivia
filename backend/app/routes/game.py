from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
import asyncio

from ..models.database import get_db
from ..models.models import Room, Player, Question, QuestionOption, Answer, GameState

router = APIRouter()

class QuestionResponse(BaseModel):
    id: int
    question_text: str
    category: str
    time_limit: int
    options: List[dict]

class SubmitAnswerRequest(BaseModel):
    player_id: int
    question_id: int
    selected_option_id: int
    response_time: float

class HauntingRaceAnswerRequest(BaseModel):
    room_code: str
    player_id: int
    question_id: int
    selected_statement_ids: List[int]
    response_time: float

# IMPORTANT: Haunting race route must come BEFORE generic /{room_code}/submit-answer
# to avoid FastAPI matching "haunting-race" as a room_code parameter
@router.post("/haunting-race/submit-answer")
async def submit_haunting_race_answer(
    answer_request: HauntingRaceAnswerRequest,
    request: Request,
    db: Session = Depends(get_db)
):
    """Submit answer for haunting race question"""
    room = db.query(Room).filter(
        Room.code == answer_request.room_code.upper(),
        Room.is_active == True
    ).first()

    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    # Validate player exists and is in room
    player = db.query(Player).filter(
        Player.id == answer_request.player_id,
        Player.room_id == room.id
    ).first()

    if not player:
        raise HTTPException(status_code=404, detail="Player not found in room")

    # Submit answer to haunting race service
    if hasattr(request.app.state, 'game_service'):
        game_service = request.app.state.game_service
        haunting_race_service = game_service.haunting_race_service

        try:
            # Submit the player's answer
            success = haunting_race_service.submit_answer(
                player_id=answer_request.player_id,
                selected_statement_ids=answer_request.selected_statement_ids,
                response_time=answer_request.response_time
            )

            if not success:
                raise HTTPException(status_code=400, detail="Answer not accepted - question phase ended")

            return {
                "message": "Answer submitted",
                "player_id": answer_request.player_id,
                "statements_selected": len(answer_request.selected_statement_ids)
            }
        except HTTPException:
            # Re-raise HTTP exceptions as-is
            raise
        except Exception as e:
            print(f"[HAUNTING-RACE API] Error submitting answer: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    else:
        raise HTTPException(status_code=500, detail="Game service not available")

@router.get("/{room_code}/current-question", response_model=Optional[QuestionResponse])
async def get_current_question(room_code: str, db: Session = Depends(get_db)):
    room = db.query(Room).filter(
        Room.code == room_code.upper(),
        Room.is_active == True
    ).first()
    
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    
    if not room.current_question_id:
        return None
    
    question = db.query(Question).filter(Question.id == room.current_question_id).first()
    if not question:
        return None
    
    options = db.query(QuestionOption).filter(
        QuestionOption.question_id == question.id
    ).order_by(QuestionOption.option_order).all()
    
    return QuestionResponse(
        id=question.id,
        question_text=question.question_text,
        category=question.category,
        time_limit=question.time_limit,
        options=[
            {
                "id": option.id,
                "text": option.option_text,
                "order": option.option_order
            }
            for option in options
        ]
    )

@router.post("/{room_code}/submit-answer")
async def submit_answer(
    room_code: str, 
    request: SubmitAnswerRequest, 
    db: Session = Depends(get_db)
):
    # Verify room exists
    room = db.query(Room).filter(
        Room.code == room_code.upper(),
        Room.is_active == True
    ).first()
    
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    
    # Verify player exists and is in this room
    player = db.query(Player).filter(
        Player.id == request.player_id,
        Player.room_id == room.id
    ).first()
    
    if not player:
        raise HTTPException(status_code=404, detail="Player not found in this room")
    
    # Check if player has already answered this question
    existing_answer = db.query(Answer).filter(
        Answer.player_id == request.player_id,
        Answer.question_id == request.question_id
    ).first()
    
    if existing_answer:
        raise HTTPException(status_code=400, detail="Player has already answered this question")
    
    # Get the question and selected option
    question = db.query(Question).filter(Question.id == request.question_id).first()
    selected_option = db.query(QuestionOption).filter(
        QuestionOption.id == request.selected_option_id
    ).first()
    
    if not question or not selected_option:
        raise HTTPException(status_code=404, detail="Question or option not found")
    
    # Calculate points based on correctness and response time
    points_earned = 0
    if selected_option.is_correct:
        # Points calculation: Base points (1000) minus time penalty
        # Faster answers get more points, up to 30 seconds
        max_points = 1000
        time_penalty = min(request.response_time, 30) * 20  # 20 points per second
        points_earned = max(100, max_points - int(time_penalty))  # Minimum 100 points
    
    # Create answer record
    answer = Answer(
        player_id=request.player_id,
        question_id=request.question_id,
        selected_option_id=request.selected_option_id,
        response_time=request.response_time,
        points_earned=points_earned
    )
    
    # Update player's total score
    player.total_score += points_earned
    
    db.add(answer)
    db.commit()
    
    return {
        "correct": selected_option.is_correct,
        "points_earned": points_earned,
        "total_score": player.total_score,
        "response_time": request.response_time
    }

@router.get("/{room_code}/leaderboard")
async def get_leaderboard(room_code: str, db: Session = Depends(get_db)):
    room = db.query(Room).filter(
        Room.code == room_code.upper(),
        Room.is_active == True
    ).first()
    
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    
    players = db.query(Player).filter(
        Player.room_id == room.id
    ).order_by(Player.total_score.desc()).all()
    
    return [
        {
            "rank": idx + 1,
            "player_id": player.id,
            "name": player.name,
            "total_score": player.total_score,
            "is_connected": player.is_connected
        }
        for idx, player in enumerate(players)
    ]

class StartGameRequest(BaseModel):
    room_code: str
    player_id: int

@router.post("/start")
async def start_game(start_request: StartGameRequest, request: Request, db: Session = Depends(get_db)):
    room = db.query(Room).filter(
        Room.code == start_request.room_code.upper(),
        Room.is_active == True
    ).first()

    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    # Validate that the player is VIP
    player = db.query(Player).filter(
        Player.id == start_request.player_id,
        Player.room_id == room.id
    ).first()
    
    if not player:
        raise HTTPException(status_code=404, detail="Player not found in room")
    
    if not player.is_vip:
        raise HTTPException(status_code=403, detail="Only VIP players can start the game")

    if room.game_state != GameState.WAITING:
        raise HTTPException(status_code=400, detail="Game is not in waiting state")
    
    # Check if there are enough players
    player_count = db.query(Player).filter(Player.room_id == room.id).count()
    if player_count < 1:  # Allow starting with 1 player for testing
        raise HTTPException(status_code=400, detail="Need at least 1 player to start")
    
    # Update room state
    room.game_state = GameState.STARTING
    db.commit()

    # Start game via game service - it will broadcast game_started THEN send first question
    # to ensure proper ordering (avoids race condition where question arrives before game_started)
    if hasattr(request.app.state, 'game_service'):
        game_service = request.app.state.game_service
        asyncio.create_task(game_service.start_game(room.code))

    return {"message": "Game is starting", "room_code": start_request.room_code}

class RematchRequest(BaseModel):
    room_code: str
    player_id: int

@router.post("/rematch")
async def rematch_game(rematch_request: RematchRequest, request: Request, db: Session = Depends(get_db)):
    """Start a rematch - reset scores and start a new game with the same players"""
    room = db.query(Room).filter(
        Room.code == rematch_request.room_code.upper(),
        Room.is_active == True
    ).first()

    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    # Validate that the player is VIP
    player = db.query(Player).filter(
        Player.id == rematch_request.player_id,
        Player.room_id == room.id
    ).first()

    if not player:
        raise HTTPException(status_code=404, detail="Player not found in room")

    if not player.is_vip:
        raise HTTPException(status_code=403, detail="Only VIP players can start a rematch")

    # Reset all player scores to 0 and revive ghost players
    players = db.query(Player).filter(Player.room_id == room.id).all()
    for p in players:
        p.total_score = 0
        p.is_ghost = False  # Revive all ghost players for rematch
        p.disabled_answer_position = None  # Clear disadvantage from previous game

    # Delete all answers from the previous game
    db.query(Answer).filter(
        Answer.player_id.in_([p.id for p in players])
    ).delete(synchronize_session=False)

    # Reset room state
    room.game_state = GameState.WAITING
    room.current_question_id = None
    room.question_start_time = None
    room.is_haunting_race_active = False  # Clear haunting race state
    db.commit()

    # Broadcast rematch event via WebSocket
    if hasattr(request.app.state, 'connection_manager'):
        connection_manager = request.app.state.connection_manager
        await connection_manager.broadcast_to_room(
            room.code,
            {
                "type": "rematch_started",
                "room_code": room.code,
                "message": "Starting rematch - all scores reset!"
            }
        )

    # Wait a moment for clients to process the rematch event
    await asyncio.sleep(1)

    # Actually start the game with game_service
    if hasattr(request.app.state, 'game_service'):
        game_service = request.app.state.game_service
        # Clear haunting race state
        if room.code in game_service.active_haunting_races:
            del game_service.active_haunting_races[room.code]
        if room.code in game_service.haunting_race_service.game_state:
            game_service.haunting_race_service.game_state = {}
        asyncio.create_task(game_service.start_game(room.code))

    return {"message": "Rematch started", "room_code": rematch_request.room_code}

class FinishGameRequest(BaseModel):
    room_code: str
    player_id: int

@router.post("/finish")
async def finish_game(finish_request: FinishGameRequest, request: Request, db: Session = Depends(get_db)):
    """Finish the game - delete room and players, return all to home screen"""
    room = db.query(Room).filter(
        Room.code == finish_request.room_code.upper(),
        Room.is_active == True
    ).first()

    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    # Validate that the player is VIP
    player = db.query(Player).filter(
        Player.id == finish_request.player_id,
        Player.room_id == room.id
    ).first()

    if not player:
        raise HTTPException(status_code=404, detail="Player not found in room")

    if not player.is_vip:
        raise HTTPException(status_code=403, detail="Only VIP players can finish the game")

    # Broadcast finish event via WebSocket before cleanup
    if hasattr(request.app.state, 'connection_manager'):
        connection_manager = request.app.state.connection_manager
        await connection_manager.broadcast_to_room(
            room.code,
            {
                "type": "game_finished",
                "room_code": room.code,
                "message": "Game has been finished by VIP"
            }
        )

    # Wait a moment for the message to be delivered
    await asyncio.sleep(0.5)

    # Get all players in this room
    players = db.query(Player).filter(Player.room_id == room.id).all()
    player_ids = [p.id for p in players]

    # Delete all player sessions for this room
    from ..models.models import PlayerSession
    db.query(PlayerSession).filter(PlayerSession.room_id == room.id).delete(synchronize_session=False)

    # Delete all answers for these players (HighScores are preserved as they're not FK-linked)
    db.query(Answer).filter(
        Answer.player_id.in_(player_ids)
    ).delete(synchronize_session=False)

    # Delete all players in the room
    db.query(Player).filter(Player.room_id == room.id).delete(synchronize_session=False)

    # Delete the room itself
    db.delete(room)
    db.commit()

    return {"message": "Game finished", "room_code": finish_request.room_code}

class TimerExpiredRequest(BaseModel):
    question_id: int

@router.post("/{room_code}/timer-expired")
async def timer_expired(
    room_code: str,
    timer_request: TimerExpiredRequest,
    request: Request,
    db: Session = Depends(get_db)
):
    """Handle timer expiration - broadcast instant timeout notification to all players"""
    room = db.query(Room).filter(
        Room.code == room_code.upper(),
        Room.is_active == True
    ).first()

    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    # Broadcast timer expired event to all players
    if hasattr(request.app.state, 'connection_manager'):
        connection_manager = request.app.state.connection_manager
        await connection_manager.broadcast_to_room(
            room.code,
            {
                "type": "timer_expired",
                "question_id": timer_request.question_id,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

    return {"message": "Timer expired notification sent"}