from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
import random
import string
import secrets
from datetime import datetime, timedelta

from ..models.database import get_db
from ..models.models import Room, Player, PlayerSession, GameState
from ..websockets.manager import connection_manager

router = APIRouter()

class CreateRoomRequest(BaseModel):
    host_name: str

class JoinRoomRequest(BaseModel):
    player_name: str
    room_code: str

class RoomResponse(BaseModel):
    id: int
    code: str
    host_name: str
    player_count: int
    max_players: int
    is_active: bool
    game_state: str

class PlayerResponse(BaseModel):
    id: int
    name: str
    total_score: int
    is_connected: bool
    is_vip: bool
    is_ghost: bool

def generate_room_code() -> str:
    """Generate a 4-character room code like 'RGHB'"""
    return ''.join(random.choices(string.ascii_uppercase, k=4))

def generate_session_token() -> str:
    """Generate a secure session token"""
    return secrets.token_urlsafe(32)

def create_player_session(db: Session, player_id: int, room_id: int) -> str:
    """Create a session token for a player that expires in 2 hours"""
    # Clean up any existing sessions for this player
    db.query(PlayerSession).filter(PlayerSession.player_id == player_id).delete()

    # Generate new session token
    token = generate_session_token()
    expires_at = datetime.utcnow() + timedelta(hours=2)

    # Create session
    session = PlayerSession(
        player_id=player_id,
        room_id=room_id,
        session_token=token,
        expires_at=expires_at
    )
    db.add(session)
    db.commit()

    return token

@router.post("/create", response_model=dict)
async def create_room(request: CreateRoomRequest, db: Session = Depends(get_db)):
    # Generate unique room code
    while True:
        room_code = generate_room_code()
        existing_room = db.query(Room).filter(Room.code == room_code, Room.is_active == True).first()
        if not existing_room:
            break
    
    # Create new room
    room = Room(
        code=room_code,
        host_name=request.host_name,
        max_players=10
    )
    db.add(room)
    db.commit()
    db.refresh(room)

    # Don't create a host player - first real player to join will be VIP
    # This prevents TV_HOST from appearing in the player list

    return {
        "id": room.id,
        "code": room.code,
        "room_code": room.code,  # Also include room_code for frontend compatibility
        "host_name": room.host_name,
        "host_player_id": None,  # No host player created
        "max_players": room.max_players,
        "is_active": room.is_active,
        "game_state": room.game_state.value,
        "players": []  # Empty players list at start
    }

@router.post("/join", response_model=dict)
async def join_room(join_request: JoinRoomRequest, request: Request, db: Session = Depends(get_db)):
    # Find room
    room = db.query(Room).filter(
        Room.code == join_request.room_code.upper(),
        Room.is_active == True
    ).first()

    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    # Check if game has already started
    if room.game_state != GameState.WAITING:
        raise HTTPException(status_code=400, detail="Game has already started. Cannot join in progress.")

    # Check if room is full
    current_players = db.query(Player).filter(Player.room_id == room.id).count()
    if current_players >= room.max_players:
        raise HTTPException(status_code=400, detail="Room is full")

    # Check if player name is already taken in this room
    existing_player = db.query(Player).filter(
        Player.room_id == room.id,
        Player.name == join_request.player_name
    ).first()

    if existing_player:
        raise HTTPException(status_code=400, detail="Player name already taken in this room")

    # Check if this is the first player (should be VIP)
    is_first_player = current_players == 0

    # Create player
    player = Player(
        name=join_request.player_name,
        room_id=room.id,
        is_vip=is_first_player
    )
    db.add(player)
    db.commit()
    db.refresh(player)

    # Create session token for this player
    session_token = create_player_session(db, player.id, room.id)

    # Get all players in the room
    all_players = db.query(Player).filter(Player.room_id == room.id).all()

    # Broadcast player joined event via WebSocket
    if hasattr(request.app.state, 'connection_manager'):
        connection_manager = request.app.state.connection_manager
        import asyncio
        asyncio.create_task(connection_manager.broadcast_to_room(
            room.code,
            {
                "type": "player_joined",
                "player": {
                    "id": player.id,
                    "name": player.name,
                    "is_vip": player.is_vip,
                    "total_score": player.total_score,
                    "is_connected": player.is_connected
                },
                "players": [{
                    "id": p.id,
                    "name": p.name,
                    "is_vip": p.is_vip,
                    "total_score": p.total_score,
                    "is_connected": p.is_connected
                } for p in all_players]
            }
        ))

    return {
        "player_id": player.id,
        "room_code": room.code,
        "is_vip": player.is_vip,
        "session_token": session_token,  # Include session token for reconnection
        "player": {
            "id": player.id,
            "name": player.name,
            "is_vip": player.is_vip,
            "total_score": player.total_score,
            "is_connected": player.is_connected
        },
        "message": f"Successfully joined room {room.code}",
        "players": [{
            "id": p.id,
            "name": p.name,
            "is_vip": p.is_vip,
            "total_score": p.total_score,
            "is_connected": p.is_connected
        } for p in all_players]
    }

@router.get("/{room_code}", response_model=RoomResponse)
async def get_room(room_code: str, db: Session = Depends(get_db)):
    room = db.query(Room).filter(
        Room.code == room_code.upper(),
        Room.is_active == True
    ).first()
    
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    
    player_count = db.query(Player).filter(Player.room_id == room.id).count()
    
    return RoomResponse(
        id=room.id,
        code=room.code,
        host_name=room.host_name,
        player_count=player_count,
        max_players=room.max_players,
        is_active=room.is_active,
        game_state=room.game_state.value
    )

@router.get("/{room_code}/players", response_model=List[PlayerResponse])
async def get_room_players(room_code: str, db: Session = Depends(get_db)):
    room = db.query(Room).filter(
        Room.code == room_code.upper(),
        Room.is_active == True
    ).first()
    
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    
    players = db.query(Player).filter(Player.room_id == room.id).all()
    
    return [
        PlayerResponse(
            id=player.id,
            name=player.name,
            total_score=player.total_score,
            is_connected=player.is_connected,
            is_vip=player.is_vip,
            is_ghost=player.is_ghost
        )
        for player in players
    ]

@router.delete("/{room_code}")
async def close_room(room_code: str, db: Session = Depends(get_db)):
    room = db.query(Room).filter(
        Room.code == room_code.upper(),
        Room.is_active == True
    ).first()

    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    # Broadcast room_terminated to all connected clients BEFORE deleting
    await connection_manager.broadcast_to_room(
        room_code.upper(),
        {
            "type": "room_terminated",
            "message": "The room has been closed by the host."
        }
    )

    # Get all players in this room
    players = db.query(Player).filter(Player.room_id == room.id).all()
    player_ids = [p.id for p in players]

    # Delete all player sessions for this room
    db.query(PlayerSession).filter(PlayerSession.room_id == room.id).delete(synchronize_session=False)

    # Delete all answers for these players (if any exist)
    if player_ids:
        from ..models.models import Answer
        db.query(Answer).filter(
            Answer.player_id.in_(player_ids)
        ).delete(synchronize_session=False)

    # Delete all players in the room
    db.query(Player).filter(Player.room_id == room.id).delete(synchronize_session=False)

    # Delete the room itself
    db.delete(room)
    db.commit()

    return {"message": f"Room {room_code} has been deleted"}

class RestoreSessionRequest(BaseModel):
    session_token: str

@router.post("/restore-session", response_model=dict)
async def restore_session(restore_request: RestoreSessionRequest, request: Request, db: Session = Depends(get_db)):
    """Restore a player's session using their session token"""
    # Find active session
    session = db.query(PlayerSession).filter(
        PlayerSession.session_token == restore_request.session_token
    ).first()

    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    # Check if session is expired
    if session.expires_at < datetime.utcnow():
        db.delete(session)
        db.commit()
        raise HTTPException(status_code=401, detail="Session expired")

    # Get player and room
    player = db.query(Player).filter(Player.id == session.player_id).first()
    room = db.query(Room).filter(Room.id == session.room_id).first()

    if not player or not room:
        db.delete(session)
        db.commit()
        raise HTTPException(status_code=404, detail="Player or room not found")

    # Check if room is still active
    if not room.is_active:
        db.delete(session)
        db.commit()
        raise HTTPException(status_code=400, detail="Room is no longer active")

    # Update player connection status
    player.is_connected = True
    db.commit()

    # Get all players in the room
    all_players = db.query(Player).filter(Player.room_id == room.id).all()

    # Get current question if game is active
    current_question = None
    if room.current_question_id:
        from ..models.models import Question, QuestionOption
        question = db.query(Question).filter(Question.id == room.current_question_id).first()
        if question:
            options = db.query(QuestionOption).filter(
                QuestionOption.question_id == question.id
            ).order_by(QuestionOption.option_order).all()

            current_question = {
                "id": question.id,
                "text": question.question_text,
                "category": question.category,
                "time_limit": question.time_limit,
                "options": [
                    {
                        "id": option.id,
                        "text": option.option_text,
                        "order": option.option_order
                    }
                    for option in options
                ],
                "start_time": room.question_start_time.isoformat() if room.question_start_time else None
            }

    # Get haunting race state if active
    haunting_race_state = None
    if room.is_haunting_race_active and hasattr(request.app.state, 'game_service'):
        game_service = request.app.state.game_service
        haunting_race_service = game_service.haunting_race_service

        if haunting_race_service and haunting_race_service.game_state:
            # Get basic game state
            race_state = haunting_race_service.get_game_state()

            # Get current question if in question phase
            current_race_question = None
            if race_state.get("phase") == "question" and haunting_race_service.game_state.get("current_question_id"):
                from ..models.models import HauntingRaceQuestion, HauntingRaceStatement
                question_id = haunting_race_service.game_state["current_question_id"]
                question = db.query(HauntingRaceQuestion).filter(HauntingRaceQuestion.id == question_id).first()

                if question:
                    # Filter statements based on player role
                    is_unicorn = (player.id == race_state["unicorn_id"])
                    statements = []
                    for stmt in sorted(question.statements, key=lambda s: s.statement_order):
                        # Unicorn doesn't see ghost-only statements
                        if is_unicorn and stmt.is_ghost_only:
                            continue
                        statements.append({
                            "id": stmt.id,
                            "text": stmt.statement_text,
                            "is_ghost_only": stmt.is_ghost_only,
                            "order": stmt.statement_order
                        })

                    current_race_question = {
                        "question_id": question.id,
                        "question_text": question.question_text,
                        "category": question.category,
                        "statements": statements,
                        "question_number": race_state["question_number"]
                    }

            # Get player list for race
            all_race_player_ids = [race_state["unicorn_id"]] + race_state["ghost_ids"]
            race_players = []
            for pid in all_race_player_ids:
                p = db.query(Player).filter(Player.id == pid).first()
                if p:
                    race_players.append({
                        "id": p.id,
                        "name": p.name,
                        "total_score": p.total_score
                    })

            haunting_race_state = {
                "unicorn_id": race_state["unicorn_id"],
                "ghost_ids": race_state["ghost_ids"],
                "initial_positions": race_state["positions"],
                "positions": race_state["positions"],
                "phase": race_state["phase"],
                "question_number": race_state["question_number"],
                "current_question": current_race_question,
                "players": race_players
            }

    return {
        "player_id": player.id,
        "room_code": room.code,
        "is_vip": player.is_vip,
        "session_token": restore_request.session_token,
        "player": {
            "id": player.id,
            "name": player.name,
            "is_vip": player.is_vip,
            "total_score": player.total_score,
            "is_connected": player.is_connected,
            "is_ghost": player.is_ghost
        },
        "room": {
            "code": room.code,
            "game_state": room.game_state.value,
            "current_question": current_question,
            "is_haunting_race_active": room.is_haunting_race_active
        },
        "players": [{
            "id": p.id,
            "name": p.name,
            "is_vip": p.is_vip,
            "total_score": p.total_score,
            "is_connected": p.is_connected,
            "is_ghost": p.is_ghost
        } for p in all_players],
        "haunting_race_state": haunting_race_state,
        "message": "Session restored successfully"
    }