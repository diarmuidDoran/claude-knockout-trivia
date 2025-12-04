import json
import asyncio
from typing import Dict, Any
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from ..models.database import SessionLocal
from ..models.models import Room, Player, Question, QuestionOption, Answer, GameState, PlayerSession
from ..websockets.manager import ConnectionManager
from .mini_game_manager import MiniGameManager
from .haunting_race_service import HauntingRaceService

class GameService:
    def __init__(self, connection_manager: ConnectionManager):
        self.connection_manager = connection_manager
        self.mini_game_manager = MiniGameManager()  # Mini-game manager
        self.haunting_race_service = HauntingRaceService(connection_manager)  # Haunting race service
        self.active_games: Dict[str, Dict] = {}  # room_code -> game_state
        self.active_haunting_races: Dict[str, bool] = {}  # room_code -> is_active
        # Track who has answered for each question: {room_code: {question_id: set(player_ids)}}
        self.answered_players: Dict[str, Dict[int, set]] = {}
        # Track used questions per room to avoid duplicates: {room_code: set(question_ids)}
        self.used_questions: Dict[str, set] = {}
        # Track if results have been shown for a question: {room_code: {question_id: bool}}
        self.results_shown: Dict[str, Dict[int, bool]] = {}
        # Track which players have acknowledged receiving results: {room_code: {question_id: set(player_ids)}}
        self.results_acknowledged: Dict[str, Dict[int, set]] = {}
        # Track each player's current question: {room_code: {player_id: question_id}}
        # Track mini-game timeout tasks to allow cancellation: {room_code: asyncio.Task}
        self.mini_game_timeout_tasks: Dict[str, asyncio.Task] = {}
        self.player_question_state: Dict[str, Dict[int, int]] = {}
        
    async def handle_websocket_message(self, room_code: str, player_id: str, message: str):
        try:
            data = json.loads(message)
            message_type = data.get("type")

            if message_type == "ping":
                await self.connection_manager.send_personal_message(
                    {"type": "pong", "timestamp": datetime.utcnow().isoformat()},
                    room_code,
                    player_id
                )
            elif message_type == "player_ready":
                await self.handle_player_ready(room_code, player_id)
            elif message_type == "player_answered":
                await self.handle_player_answered(room_code, player_id, data)
            elif message_type == "results_received":
                await self.handle_results_acknowledged(room_code, player_id, data)
            elif message_type == "request_sync":
                await self.handle_sync_request(room_code, player_id)
            elif message_type == "mini_game_action":
                await self.handle_mini_game_action(room_code, player_id, data)

        except json.JSONDecodeError:
            await self.connection_manager.send_personal_message(
                {"type": "error", "message": "Invalid JSON"},
                room_code,
                player_id
            )
    
    async def handle_player_disconnect(self, room_code: str, player_id: str):
        # Ignore TV disconnects
        if player_id == 'tv' or player_id == 'null':
            return

        db = SessionLocal()
        try:
            # Update player connection status
            try:
                player_id_int = int(player_id)
                player = db.query(Player).filter(Player.id == player_id_int).first()
                if player:
                    player.is_connected = False
                    db.commit()

                    # Notify other players
                    await self.connection_manager.broadcast_to_room(
                        room_code,
                        {
                            "type": "player_disconnected",
                            "player_id": player_id,
                            "player_name": player.name,
                            "timestamp": datetime.utcnow().isoformat()
                        }
                    )
            except ValueError:
                # Invalid player_id (not an integer), ignore
                pass
        finally:
            db.close()
    
    async def start_game(self, room_code: str):
        db = SessionLocal()
        try:
            room = db.query(Room).filter(Room.code == room_code).first()
            if not room:
                return

            room.game_state = GameState.ACTIVE
            db.commit()

            # Initialize game state
            self.active_games[room_code] = {
                "current_question": 0,
                "questions_answered": 0,
                "total_questions": 10,  # Configurable
                "players_ready": set()
            }

            # Initialize used questions tracker for this room
            self.used_questions[room_code] = set()

            # Broadcast game_started BEFORE sending first question
            # This ensures clients receive events in correct order: game_started -> new_question
            await self.connection_manager.broadcast_to_room(
                room_code,
                {
                    "type": "game_started",
                    "room_code": room_code,
                    "message": "Game is starting!"
                }
            )

            # Small delay to ensure game_started is processed first
            await asyncio.sleep(0.1)

            # Start first question
            await self.next_question(room_code, is_first=True)

        finally:
            db.close()
    
    async def next_question(self, room_code: str, is_first: bool = False):
        print(f"[DEBUG] next_question called for room {room_code}, is_first={is_first}")
        db = SessionLocal()
        try:
            room = db.query(Room).filter(Room.code == room_code).first()
            if not room:
                print(f"[ERROR] Room {room_code} not found in next_question")
                return

            # Check if game is still active
            if room_code not in self.active_games:
                print(f"[ERROR] Room {room_code} not in active_games - game state may be corrupted")
                return

            # Get used questions for this room
            used_ids = self.used_questions.get(room_code, set())

            # Get available questions (excluding used ones)
            import random
            query = db.query(Question).filter(
                Question.is_active == True,
                ~Question.id.in_(used_ids) if used_ids else True
            )

            # For first question, only get easy or medium difficulty
            if is_first:
                query = query.filter(Question.difficulty.in_(['easy', 'medium']))

            all_questions = query.all()
            print(f"[DEBUG] Room {room_code}: Found {len(all_questions)} available questions (used: {len(used_ids)})")

            if not all_questions:
                # No more unused questions, end the game
                print(f"[DEBUG] Room {room_code}: No more questions available, ending game")
                await self.end_game(room_code)
                return

            # Pick a random question from available ones
            question = random.choice(all_questions)
            print(f"[DEBUG] Room {room_code}: Selected question {question.id} - {question.question_text[:50]}...")

            # Mark this question as used
            if room_code not in self.used_questions:
                self.used_questions[room_code] = set()
            self.used_questions[room_code].add(question.id)

            # Update room with current question
            room.current_question_id = question.id
            db.commit()

            # Get question options
            options = db.query(QuestionOption).filter(
                QuestionOption.question_id == question.id
            ).order_by(QuestionOption.option_order).all()

            # Shuffle options randomly so correct answer isn't always in same position
            options_list = list(options)
            random.shuffle(options_list)

            # Get all players in this room to include disabled positions
            players = db.query(Player).filter(Player.room_id == room.id).all()
            disabled_positions = {
                player.id: player.disabled_answer_position
                for player in players
                if player.disabled_answer_position is not None
            }

            # Generate start time RIGHT BEFORE broadcasting (minimize any delay)
            start_time = datetime.utcnow()

            # Broadcast question to all players IMMEDIATELY with the fresh start_time
            # Do this BEFORE database commit to minimize latency
            await self.connection_manager.broadcast_to_room(
                room_code,
                {
                    "type": "new_question",
                    "question": {
                        "id": question.id,
                        "text": question.question_text,
                        "category": question.category,
                        "time_limit": question.time_limit,
                        "options": [
                            {
                                "id": option.id,
                                "text": option.option_text,
                                "order": idx + 1  # New shuffled order (1-4)
                            }
                            for idx, option in enumerate(options_list)
                        ]
                    },
                    "start_time": start_time.isoformat(),
                    "disabled_positions": disabled_positions  # Include disabled positions for Playing at a Disadvantage
                }
            )

            # Now update room with start time in database (for session restoration)
            room.question_start_time = start_time
            db.commit()

            # Wait 0.5 seconds to ensure all devices receive the question before timer starts
            await asyncio.sleep(0.5)

            # Broadcast start_timer event to begin countdown on all devices simultaneously
            await self.connection_manager.broadcast_to_room(
                room_code,
                {
                    "type": "start_timer",
                    "question_id": question.id,
                    "time_limit": question.time_limit,
                    "timestamp": datetime.utcnow().isoformat()
                }
            )

            # Schedule question timeout - add 0.5 seconds to account for the delay
            asyncio.create_task(
                self.question_timeout(room_code, question.id, question.time_limit + 0.5)
            )
            
        finally:
            db.close()
    
    async def question_timeout(self, room_code: str, question_id: int, timeout_seconds: int):
        await asyncio.sleep(timeout_seconds)

        db = SessionLocal()
        try:
            room = db.query(Room).filter(Room.code == room_code).first()
            if not room or room.current_question_id != question_id:
                return  # Question has already changed or room doesn't exist

            # Check if results have already been shown (all players answered)
            if room_code in self.answered_players:
                if question_id in self.answered_players[room_code]:
                    # Get player count
                    all_players = db.query(Player).filter(
                        Player.room_id == room.id,
                        Player.is_connected == True
                    ).all()

                    # If all players answered, results already shown
                    if len(self.answered_players[room_code][question_id]) >= len(all_players):
                        return

            # Time's up - show results for whoever answered
            await self.show_question_results(room_code, question_id)

        finally:
            db.close()
    
    async def handle_player_answered(self, room_code: str, player_id: str, data: Dict[str, Any]):
        """Track that a player has answered and check if all players have answered"""
        db = SessionLocal()
        try:
            room = db.query(Room).filter(Room.code == room_code).first()
            if not room or not room.current_question_id:
                return

            question_id = room.current_question_id

            # Initialize tracking for this room/question if needed
            if room_code not in self.answered_players:
                self.answered_players[room_code] = {}
            if question_id not in self.answered_players[room_code]:
                self.answered_players[room_code][question_id] = set()

            # Add this player to the answered set
            self.answered_players[room_code][question_id].add(int(player_id))

            # Broadcast to other players that someone answered
            await self.connection_manager.broadcast_to_room(
                room_code,
                {
                    "type": "player_answered",
                    "player_id": player_id,
                    "timestamp": datetime.utcnow().isoformat()
                },
                exclude_player=player_id
            )

            # Check if all players (living + ghosts) have answered
            all_players = db.query(Player).filter(
                Player.room_id == room.id,
                Player.is_connected == True
            ).all()

            total_players = len(all_players)
            answered_count = len(self.answered_players[room_code][question_id])

            print(f"[GAME] Question {question_id}: {answered_count}/{total_players} players answered (living + ghosts)")

            # If all players (living + ghosts) have answered, trigger results immediately
            if answered_count >= total_players:
                print(f"[GAME] All players answered! Showing results early...")
                await self.show_question_results(room_code, question_id)

        finally:
            db.close()

    async def handle_results_acknowledged(self, room_code: str, player_id: str, data: Dict[str, Any]):
        """Handle when a player acknowledges receiving results"""
        question_id = data.get("question_id")
        if not question_id:
            return

        print(f"[SYNC] Player {player_id} acknowledged results for question {question_id} in room {room_code}")

        # Initialize tracking for this room/question if needed
        if room_code not in self.results_acknowledged:
            self.results_acknowledged[room_code] = {}
        if question_id not in self.results_acknowledged[room_code]:
            self.results_acknowledged[room_code][question_id] = set()

        # Add this player to the acknowledged set
        try:
            self.results_acknowledged[room_code][question_id].add(int(player_id))
        except ValueError:
            # Invalid player_id, ignore
            pass

    async def handle_sync_request(self, room_code: str, player_id: str):
        """Handle when a player requests sync for current question"""
        print(f"[SYNC] Player {player_id} requesting sync for room {room_code}")

        db = SessionLocal()
        try:
            room = db.query(Room).filter(Room.code == room_code).first()
            if not room or not room.current_question_id:
                print(f"[SYNC] No active question for room {room_code}")
                return

            question_id = room.current_question_id
            question = db.query(Question).filter(Question.id == question_id).first()
            if not question:
                return

            # Get question options
            options = db.query(QuestionOption).filter(
                QuestionOption.question_id == question_id
            ).order_by(QuestionOption.option_order).all()

            # Shuffle options randomly so correct answer isn't always in same position
            options_list = list(options)
            random.shuffle(options_list)

            # Get all players in this room to include disabled positions
            players = db.query(Player).filter(Player.room_id == room.id).all()
            disabled_positions = {
                player.id: player.disabled_answer_position
                for player in players
                if player.disabled_answer_position is not None
            }

            # Calculate remaining time
            time_elapsed = 0
            if room.question_start_time:
                time_elapsed = (datetime.utcnow() - room.question_start_time).total_seconds()

            remaining_time = max(0, question.time_limit - time_elapsed)

            print(f"[SYNC] Sending question {question_id} to player {player_id}, {remaining_time}s remaining")

            # Send the current question to this specific player
            await self.connection_manager.send_personal_message(
                {
                    "type": "new_question",
                    "question": {
                        "id": question.id,
                        "text": question.question_text,
                        "category": question.category,
                        "time_limit": int(remaining_time),
                        "options": [
                            {
                                "id": option.id,
                                "text": option.option_text,
                                "order": idx + 1  # New shuffled order (1-4)
                            }
                            for idx, option in enumerate(options_list)
                        ]
                    },
                    "start_time": room.question_start_time.isoformat() if room.question_start_time else datetime.utcnow().isoformat(),
                    "disabled_positions": disabled_positions,  # Include disabled positions for Playing at a Disadvantage
                    "is_sync": True  # Flag to indicate this is a sync message
                },
                room_code,
                player_id
            )

        finally:
            db.close()

    async def show_question_results(self, room_code: str, question_id: int):
        """Show results for a question and schedule next question"""
        print(f"[DEBUG] show_question_results called for room {room_code}, question {question_id}")

        # Check if results have already been shown for this question
        if room_code in self.results_shown:
            if question_id in self.results_shown[room_code] and self.results_shown[room_code][question_id]:
                print(f"[DEBUG] Results already shown for room {room_code}, question {question_id} - skipping")
                return

        # Mark that we're showing results for this question
        if room_code not in self.results_shown:
            self.results_shown[room_code] = {}
        self.results_shown[room_code][question_id] = True

        db = SessionLocal()
        try:
            # Get question and correct answer
            question = db.query(Question).filter(Question.id == question_id).first()
            correct_option = db.query(QuestionOption).filter(
                QuestionOption.question_id == question_id,
                QuestionOption.is_correct == True
            ).first()

            # Get all answers for this question
            answers = db.query(Answer).join(Player).filter(
                Answer.question_id == question_id
            ).all()

            # Get updated player scores
            room = db.query(Room).filter(Room.code == room_code).first()
            players = db.query(Player).filter(
                Player.room_id == room.id
            ).order_by(Player.total_score.desc()).all()

            # Get all living (non-ghost) players in the room
            living_players = db.query(Player).filter(
                Player.room_id == room.id,
                Player.is_ghost == False
            ).all()
            living_player_ids = {p.id for p in living_players}

            # Separate correct and incorrect answers
            # - incorrect_players: Only living players who got it wrong (at-risk)
            # - correct_players: Living + ghost players who got it right (safe players for mini-games)
            correct_players = []
            incorrect_players = []
            answered_player_ids = set()

            for answer in answers:
                if not answer.player.is_ghost:
                    # Track living players who answered
                    answered_player_ids.add(answer.player_id)
                    if answer.selected_option_id == correct_option.id if correct_option else False:
                        correct_players.append(answer.player_id)
                    else:
                        incorrect_players.append(answer.player_id)
                else:
                    # Ghosts who answered correctly can be safe players in mini-games
                    if answer.selected_option_id == correct_option.id if correct_option else False:
                        correct_players.append(answer.player_id)

            # Living players who didn't answer are also at-risk (incorrect)
            for player_id in living_player_ids:
                if player_id not in answered_player_ids:
                    incorrect_players.append(player_id)
                    print(f"[DEBUG] Room {room_code}: Player {player_id} didn't answer - marked as at-risk")

            # Debug logging for correct/incorrect determination
            print(f"[DEBUG] Room {room_code}: Question {question_id} results:")
            print(f"[DEBUG] - Correct option ID: {correct_option.id if correct_option else 'None'}")
            print(f"[DEBUG] - Total answers received: {len(answers)}")
            print(f"[DEBUG] - Living players: {living_player_ids}")
            print(f"[DEBUG] - Correct players: {correct_players}")
            print(f"[DEBUG] - Incorrect players: {incorrect_players}")
            for answer in answers:
                print(f"[DEBUG] - Player {answer.player_id} answered option {answer.selected_option_id}, is_ghost={answer.player.is_ghost}")

            # Broadcast results
            await self.connection_manager.broadcast_to_room(
                room_code,
                {
                    "type": "question_results",
                    "question_id": question_id,
                    "correct_answer": {
                        "id": correct_option.id,
                        "text": correct_option.option_text
                    } if correct_option else None,
                    "results": [
                        {
                            "player_id": answer.player_id,
                            "player_name": answer.player.name,
                            "selected_option_id": answer.selected_option_id,
                            "points_earned": answer.points_earned,
                            "response_time": answer.response_time,
                            "is_correct": answer.selected_option_id == correct_option.id if correct_option else False,
                            "is_ghost": answer.player.is_ghost
                        }
                        for answer in answers
                    ],
                    "leaderboard": [
                        {
                            "player_id": player.id,
                            "name": player.name,
                            "total_score": player.total_score,
                            "is_ghost": player.is_ghost
                        }
                        for player in players
                    ]
                }
            )

            # Update game state
            if room_code in self.active_games:
                self.active_games[room_code]["questions_answered"] += 1

                questions_answered = self.active_games[room_code]["questions_answered"]
                total_questions = self.active_games[room_code]["total_questions"]
                print(f"[DEBUG] Room {room_code}: Completed question {questions_answered}/{total_questions}")

                # Wait 3 seconds to show results
                await asyncio.sleep(3)

                # Check if game should end
                if questions_answered >= total_questions:
                    print(f"[DEBUG] Room {room_code}: All trivia questions completed")
                    await asyncio.sleep(2)  # Show final results for 2 more seconds

                    # Check if multiple living players remain - convert extras to ghosts for haunting race
                    db = SessionLocal()
                    try:
                        room = db.query(Room).filter(Room.code == room_code).first()
                        living_players = db.query(Player).filter(
                            Player.room_id == room.id,
                            Player.is_ghost == False,
                            Player.is_connected == True
                        ).order_by(Player.total_score.desc()).all()

                        if len(living_players) > 1:
                            # Multiple living players - highest scorer becomes unicorn, rest become ghosts
                            print(f"[GAME] {len(living_players)} living players remain. Converting lower scorers to ghosts...")

                            unicorn = living_players[0]  # Highest scorer
                            ghosts_to_convert = living_players[1:]  # Everyone else

                            # Convert lower scorers to ghosts
                            for player in ghosts_to_convert:
                                player.is_ghost = True
                                print(f"[GAME] Converting {player.name} (ID: {player.id}, Score: {player.total_score}) to ghost")

                            db.commit()

                            # Broadcast conversion message
                            await self.connection_manager.broadcast_to_room(
                                room_code,
                                {
                                    "type": "multiple_survivors",
                                    "message": f"{unicorn.name} has the highest score and becomes the Unicorn! All other players become ghosts.",
                                    "unicorn": {
                                        "player_id": unicorn.id,
                                        "name": unicorn.name,
                                        "score": unicorn.total_score
                                    },
                                    "converted_ghosts": [
                                        {
                                            "player_id": p.id,
                                            "name": p.name,
                                            "score": p.total_score
                                        }
                                        for p in ghosts_to_convert
                                    ]
                                }
                            )

                            await asyncio.sleep(4)  # Show conversion message

                            # Now check if haunting race should trigger
                            should_trigger_haunting_race = await self.check_haunting_race_trigger(room_code)
                            is_already_active = self.active_haunting_races.get(room_code, False)

                            if should_trigger_haunting_race and not is_already_active:
                                print(f"[GAME] ✓ Triggering haunting race after converting survivors")
                                await self.start_haunting_race(room_code)
                                return  # Don't end the game

                    except Exception as e:
                        print(f"[ERROR] Room {room_code}: Failed to convert survivors: {e}")
                        import traceback
                        traceback.print_exc()
                    finally:
                        db.close()

                    # If we get here, end the game normally
                    try:
                        await self.end_game(room_code)
                    except Exception as e:
                        print(f"[ERROR] Room {room_code}: Failed to end game: {e}")
                        import traceback
                        traceback.print_exc()
                else:
                    # Start mini-game if there are incorrect players
                    if incorrect_players:
                        print(f"[DEBUG] Room {room_code}: Starting mini-game with {len(incorrect_players)} at-risk players: {incorrect_players}")
                        print(f"[DEBUG] Room {room_code}: Safe players: {correct_players}")
                        try:
                            await self.start_mini_game(room_code, incorrect_players, correct_players)
                        except Exception as e:
                            print(f"[ERROR] Room {room_code}: Failed to start mini-game: {e}")
                            import traceback
                            traceback.print_exc()
                            # Fall back to next question
                            await asyncio.sleep(2)
                            await self.next_question(room_code)
                    else:
                        print(f"[DEBUG] Room {room_code}: Everyone answered correctly, proceeding to next question")
                        await asyncio.sleep(2)
                        try:
                            await self.next_question(room_code)
                        except Exception as e:
                            print(f"[ERROR] Room {room_code}: Failed to proceed to next question: {e}")
                            import traceback
                            traceback.print_exc()
                            # Try to end the game gracefully
                            try:
                                await self.end_game(room_code)
                            except:
                                pass

        finally:
            db.close()
    
    async def wait_for_results_acknowledgment(self, room_code: str, question_id: int, room_id: int, timeout: int = 2):
        """Wait for all players to acknowledge receiving results, with timeout"""
        print(f"[SYNC] Waiting for players to acknowledge results for question {question_id}")

        db = SessionLocal()
        try:
            # Get all connected players
            players = db.query(Player).filter(
                Player.room_id == room_id,
                Player.is_connected == True
            ).all()

            total_players = len(players)
            if total_players == 0:
                return

            # Wait up to timeout seconds for acknowledgments
            start_time = asyncio.get_event_loop().time()
            check_interval = 0.2  # Check every 200ms

            while (asyncio.get_event_loop().time() - start_time) < timeout:
                # Count how many players have acknowledged
                acknowledged_count = 0
                if room_code in self.results_acknowledged:
                    if question_id in self.results_acknowledged[room_code]:
                        acknowledged_count = len(self.results_acknowledged[room_code][question_id])

                print(f"[SYNC] {acknowledged_count}/{total_players} players acknowledged results for question {question_id}")

                # If all players acknowledged, proceed immediately
                if acknowledged_count >= total_players:
                    print(f"[SYNC] All players acknowledged, proceeding")
                    return

                # Wait a bit before checking again
                await asyncio.sleep(check_interval)

            # Timeout reached
            acknowledged_count = 0
            if room_code in self.results_acknowledged:
                if question_id in self.results_acknowledged[room_code]:
                    acknowledged_count = len(self.results_acknowledged[room_code][question_id])

            print(f"[SYNC] Timeout reached, {acknowledged_count}/{total_players} players acknowledged")

        finally:
            db.close()

    async def handle_player_ready(self, room_code: str, player_id: str):
        if room_code not in self.active_games:
            return

        self.active_games[room_code]["players_ready"].add(player_id)

        # Check if all players are ready
        connected_players = self.connection_manager.get_room_players(room_code)
        if len(self.active_games[room_code]["players_ready"]) >= len(connected_players):
            await self.start_next_phase(room_code)
    
    async def start_next_phase(self, room_code: str):
        # Start next question or end game logic
        await self.next_question(room_code)

    async def check_haunting_race_trigger(self, room_code: str) -> bool:
        """
        Check if haunting race should be triggered.

        Conditions:
        - Exactly 1 living player (is_ghost == False)
        - 2 or more ghost players (is_ghost == True)

        Returns:
            True if haunting race should start, False otherwise
        """
        db = SessionLocal()
        try:
            room = db.query(Room).filter(Room.code == room_code).first()
            if not room:
                return False

            # Count living players
            living_players = db.query(Player).filter(
                Player.room_id == room.id,
                Player.is_ghost == False,
                Player.is_connected == True
            ).all()

            # Count ghost players
            ghost_players = db.query(Player).filter(
                Player.room_id == room.id,
                Player.is_ghost == True,
                Player.is_connected == True
            ).all()

            living_count = len(living_players)
            ghost_count = len(ghost_players)

            should_trigger = living_count == 1 and ghost_count >= 1

            print(f"[HAUNTING-RACE] Check trigger - Living: {living_count}, Ghosts: {ghost_count}, Trigger: {should_trigger}")

            return should_trigger
        finally:
            db.close()

    async def start_haunting_race(self, room_code: str):
        """Start the haunting race endgame."""
        print(f"[HAUNTING-RACE] Starting haunting race for room {room_code}")

        # Mark as active to prevent duplicate starts
        self.active_haunting_races[room_code] = True

        db = SessionLocal()
        try:
            room = db.query(Room).filter(Room.code == room_code).first()
            if not room:
                print(f"[HAUNTING-RACE] Error: Room {room_code} not found")
                return

            # Mark room as haunting race active
            room.is_haunting_race_active = True
            db.commit()

            # Get all players with their data
            players = db.query(Player).filter(
                Player.room_id == room.id,
                Player.is_connected == True
            ).all()

            # Convert to dict format for service
            player_data = [
                {
                    "id": p.id,
                    "name": p.name,
                    "total_score": p.total_score,
                    "is_ghost": p.is_ghost
                }
                for p in players
            ]

            # Setup the race
            race_setup = self.haunting_race_service.setup_race(room_code, player_data)

            # Broadcast race start to all players
            await self.connection_manager.broadcast_haunting_race_start(
                room_code,
                {
                    "unicorn_id": race_setup["unicorn_player"]["id"],
                    "ghost_ids": [g["id"] for g in race_setup["ghost_players"]],
                    "initial_positions": {
                        race_setup["unicorn_player"]["id"]: race_setup["unicorn_player"]["starting_position"],
                        **{g["id"]: g["starting_position"] for g in race_setup["ghost_players"]}
                    },
                    "players": player_data,
                    "total_columns": race_setup["total_columns"],
                    "time_limit": race_setup["time_limit"]
                }
            )

            print(f"[HAUNTING-RACE] Race started, waiting 3 seconds before first question")
            await asyncio.sleep(3)

            # Start the race questions loop
            await self.haunting_race_question_loop(room_code)

        except Exception as e:
            print(f"[HAUNTING-RACE] Error starting race: {e}")
            import traceback
            traceback.print_exc()
        finally:
            db.close()

    async def haunting_race_question_loop(self, room_code: str):
        """Run the haunting race question loop until someone wins."""
        print(f"[HAUNTING-RACE] Starting question loop for room {room_code}")

        while self.active_haunting_races.get(room_code, False):
            try:
                # Get next question
                question_data = self.haunting_race_service.get_next_question()

                if not question_data:
                    print(f"[HAUNTING-RACE] No more questions available!")
                    break

                # Send question to all players (with role-based filtering)
                db = SessionLocal()
                try:
                    room = db.query(Room).filter(Room.code == room_code).first()
                    players = db.query(Player).filter(
                        Player.room_id == room.id,
                        Player.is_connected == True
                    ).all()

                    unicorn_id = self.haunting_race_service.game_state["unicorn_id"]

                    for player in players:
                        is_unicorn = (player.id == unicorn_id)
                        await self.connection_manager.send_haunting_race_player_question(
                            room_code,
                            player.id,
                            question_data,
                            is_unicorn
                        )
                finally:
                    db.close()

                # Wait for all players to answer or timeout (20 seconds + 2 second grace period)
                max_wait_time = 22  # 20s timer + 2s grace period
                start_time = asyncio.get_event_loop().time()

                while True:
                    elapsed = asyncio.get_event_loop().time() - start_time

                    # Check if all players have answered
                    if self.haunting_race_service.can_resolve_question():
                        all_player_ids = [self.haunting_race_service.game_state["unicorn_id"]] + self.haunting_race_service.game_state["ghost_ids"]
                        all_answered = all(pid in self.haunting_race_service.game_state["player_answers"] for pid in all_player_ids)

                        if all_answered:
                            print(f"[HAUNTING-RACE] All players answered! Resolving early after {elapsed:.1f}s")
                            break

                    # Check if time is up
                    if elapsed >= max_wait_time:
                        print(f"[HAUNTING-RACE] Time limit reached ({max_wait_time}s)")
                        break

                    # Wait a bit before checking again
                    await asyncio.sleep(0.5)

                # Resolve question
                results = self.haunting_race_service.resolve_question()

                # Broadcast results
                await self.connection_manager.broadcast_haunting_race_results(
                    room_code,
                    results
                )

                # Check for unicorn swap
                if results.get("unicorn_swap"):
                    await self.connection_manager.broadcast_haunting_race_unicorn_swap(
                        room_code,
                        results["unicorn_swap"]
                    )

                # Update positions
                await self.connection_manager.broadcast_haunting_race_positions(
                    room_code,
                    results["positions"],
                    results.get("movements")
                )

                # Check for winner
                if results.get("winner"):
                    await self.connection_manager.broadcast_haunting_race_end(
                        room_code,
                        {
                            "winner_id": results["winner"]["player_id"],
                            "winner_name": results["winner"]["player_name"],
                            "final_positions": results["positions"]
                        }
                    )

                    # End the haunting race
                    self.active_haunting_races[room_code] = False

                    # End the game with haunting race winner
                    await self.end_game(room_code, haunting_race_winner_id=results["winner"]["player_id"])
                    break

                # Wait 6 seconds before next question (shows results to players)
                await asyncio.sleep(6)

            except Exception as e:
                print(f"[HAUNTING-RACE] Error in question loop: {e}")
                import traceback
                traceback.print_exc()
                break

    async def end_game(self, room_code: str, haunting_race_winner_id: int = None):
        db = SessionLocal()
        try:
            room = db.query(Room).filter(Room.code == room_code).first()
            if room:
                room.game_state = GameState.FINISHED
                room.current_question_id = None
                db.commit()

                # Get all players
                all_players = db.query(Player).filter(
                    Player.room_id == room.id
                ).all()

                # If haunting race winner provided, they are the winner
                if haunting_race_winner_id:
                    winner = db.query(Player).filter(Player.id == haunting_race_winner_id).first()

                    # Build leaderboard: winner first, then others by score
                    players = []
                    other_players = [p for p in all_players if p.id != haunting_race_winner_id]
                    other_players.sort(key=lambda p: p.total_score, reverse=True)

                    players = [winner] + other_players
                else:
                    # Normal game: winner is last living player or highest score among living
                    winner = db.query(Player).filter(
                        Player.room_id == room.id,
                        Player.is_ghost == False  # Must be living
                    ).order_by(
                        Player.total_score.desc()
                    ).first()

                    # Get final leaderboard (living players first, then ghosts)
                    players = db.query(Player).filter(
                        Player.room_id == room.id
                    ).order_by(
                        Player.is_ghost.asc(),  # Living players first
                        Player.total_score.desc()
                    ).all()

                # Save high scores for all players
                from app.models.models import HighScore, Answer
                for player in players:
                    # Calculate stats for this player
                    answers = db.query(Answer).filter(Answer.player_id == player.id).all()
                    questions_answered = len(answers)
                    correct_answers = sum(1 for answer in answers
                                         if answer.points_earned > 0)

                    # Create high score entry
                    high_score = HighScore(
                        player_name=player.name,
                        score=player.total_score,
                        questions_answered=questions_answered,
                        correct_answers=correct_answers,
                        room_code=room_code,
                        is_ghost=player.is_ghost  # Track if they were a ghost
                    )
                    db.add(high_score)

                db.commit()

                # Keep only top 5 high scores - delete lower scores
                all_high_scores = db.query(HighScore).order_by(HighScore.score.desc()).all()
                if len(all_high_scores) > 5:
                    # Get IDs of scores to keep (top 5)
                    top_5_ids = [score.id for score in all_high_scores[:5]]
                    # Delete everything else
                    db.query(HighScore).filter(~HighScore.id.in_(top_5_ids)).delete(synchronize_session=False)
                    db.commit()

                # Don't delete player sessions here - they should persist until room is deleted
                # This allows players to reconnect and see the game over screen

                # Broadcast game end
                await self.connection_manager.broadcast_to_room(
                    room_code,
                    {
                        "type": "game_ended",
                        "winner": {
                            "player_id": winner.id,
                            "player_name": winner.name,
                            "total_score": winner.total_score
                        } if winner else None,
                        "final_leaderboard": [
                            {
                                "rank": idx + 1,
                                "player_id": player.id,
                                "player_name": player.name,
                                "total_score": player.total_score,
                                "is_ghost": player.is_ghost
                            }
                            for idx, player in enumerate(players)
                        ]
                    }
                )

            # Clean up game state
            if room_code in self.active_games:
                del self.active_games[room_code]

            # Clean up used questions tracker
            if room_code in self.used_questions:
                del self.used_questions[room_code]

            # Clean up answered players tracker
            if room_code in self.answered_players:
                del self.answered_players[room_code]

            # Clean up results shown tracker
            if room_code in self.results_shown:
                del self.results_shown[room_code]

            # Clean up results acknowledged tracker
            if room_code in self.results_acknowledged:
                del self.results_acknowledged[room_code]

            # Clean up player question state tracker
            if room_code in self.player_question_state:
                del self.player_question_state[room_code]

        finally:
            db.close()

    async def start_mini_game(self, room_code: str, at_risk_players: list, safe_players: list):
        """Start a mini-game for elimination"""
        db = SessionLocal()
        try:
            # Count total living players
            total_living = len(at_risk_players) + len(safe_players)

            print(f"[MINI-GAME] Room {room_code}: Starting mini-game selection")
            print(f"[MINI-GAME] - At-risk players: {at_risk_players}")
            print(f"[MINI-GAME] - Safe players: {safe_players}")
            print(f"[MINI-GAME] - Total living: {total_living}")

            # Start mini-game (random selection)
            mini_game_data = self.mini_game_manager.start_mini_game(
                room_code=room_code,
                at_risk_players=at_risk_players,
                safe_players=safe_players,
                total_players=total_living
            )

            print(f"[MINI-GAME] Room {room_code}: Selected game: {mini_game_data.get('game_name', 'Unknown')}")

            # Broadcast to all players
            await self.connection_manager.broadcast_to_room(room_code, mini_game_data)

            # Get timeout from mini-game
            mini_game = self.mini_game_manager.get_active_mini_game(room_code)
            if mini_game:
                # Cancel any existing timeout task from previous mini-game
                if room_code in self.mini_game_timeout_tasks:
                    old_task = self.mini_game_timeout_tasks[room_code]
                    if not old_task.done():
                        print(f"[MINI-GAME] Room {room_code}: Canceling previous timeout task")
                        old_task.cancel()

                timeout = mini_game.get_timeout_seconds()
                print(f"[MINI-GAME] Room {room_code}: Starting timeout timer for {timeout} seconds")

                # Start timeout timer and store the task reference
                task = asyncio.create_task(self.check_mini_game_timeout(room_code, timeout))
                self.mini_game_timeout_tasks[room_code] = task

        finally:
            db.close()

    async def handle_mini_game_action(self, room_code: str, player_id: str, data: Dict[str, Any]):
        """Handle a player's action in the mini-game"""
        try:
            player_id_int = int(player_id)
        except ValueError:
            return

        action = data.get("action")
        if not action:
            return

        # Process action
        success = await self.mini_game_manager.process_player_action(
            room_code,
            player_id_int,
            action
        )

        if not success:
            await self.connection_manager.send_personal_message(
                {
                    "type": "error",
                    "message": "Invalid mini-game action"
                },
                room_code,
                player_id
            )
            return

        # Check if this action generated a new question (Quick Math)
        mini_game = self.mini_game_manager.get_active_mini_game(room_code)
        if mini_game and player_id_int in mini_game.player_actions:
            player_action_data = mini_game.player_actions[player_id_int]
            if player_action_data.get("type") == "new_question":
                # Send question directly to the requesting player
                await self.connection_manager.send_personal_message(
                    {
                        "type": "mini_game_question",
                        "player_id": player_id_int,
                        "question": player_action_data["question"]
                    },
                    room_code,
                    player_id
                )
                return

        # Check if Worst Answer game phase changed to voting
        mini_game = self.mini_game_manager.get_active_mini_game(room_code)
        if mini_game and mini_game.name == "Worst Answer":
            game_state = mini_game.game_state
            if game_state.get("phase") == "voting" and action.get("type") == "submit_answer":
                # Broadcast phase change with submitted answers for voting
                submitted_answers = game_state.get("submitted_answers", {})
                print(f"[WORST-ANSWER DEBUG] Broadcasting phase change to voting with answers: {submitted_answers}")
                await self.connection_manager.broadcast_to_room(
                    room_code,
                    {
                        "type": "mini_game_phase_change",
                        "game_name": "Worst Answer",
                        "phase": "voting",
                        "question": game_state.get("question", ""),
                        "submitted_answers": submitted_answers,
                        "at_risk_players": game_state.get("at_risk_players", []),
                        "safe_players": game_state.get("safe_players", [])
                    }
                )
                print(f"[WORST-ANSWER DEBUG] Phase changed to voting, broadcast sent with {len(submitted_answers)} answers")

        # Notify room that player acted - include action for live score updates
        await self.connection_manager.broadcast_to_room(
            room_code,
            {
                "type": "mini_game_player_action",
                "player_id": player_id_int,
                "action": action,  # Include action for live score updates on TV
                "action_received": True
            }
        )

        # Check if ready to resolve
        if self.mini_game_manager.can_resolve(room_code):
            await self.resolve_mini_game(room_code)

    async def resolve_mini_game(self, room_code: str):
        """Resolve the mini-game and eliminate players"""
        # Cancel timeout task if it's still running (game resolved early)
        if room_code in self.mini_game_timeout_tasks:
            task = self.mini_game_timeout_tasks[room_code]
            if not task.done():
                print(f"[MINI-GAME] Room {room_code}: Canceling timeout task (game resolved early)")
                task.cancel()
            del self.mini_game_timeout_tasks[room_code]

        db = SessionLocal()
        try:
            # Resolve mini-game
            result = self.mini_game_manager.resolve_mini_game(
                room_code,
                db,
                force=False
            )

            if not result.success:
                await self.connection_manager.broadcast_to_room(
                    room_code,
                    {
                        "type": "error",
                        "message": result.error_message or "Mini-game failed"
                    }
                )
                return

            # Get player names for eliminated players
            eliminated_players = db.query(Player).filter(
                Player.id.in_(result.eliminated_player_ids)
            ).all()

            # Get game name from active mini-game
            mini_game = self.mini_game_manager.get_active_mini_game(room_code)
            game_name = mini_game.name if mini_game else "Mini-Game"

            # Broadcast results
            await self.connection_manager.broadcast_to_room(
                room_code,
                {
                    "type": "mini_game_results",
                    "game_name": game_name,
                    "eliminated": [
                        {
                            "player_id": p.id,
                            "player_name": p.name
                        }
                        for p in eliminated_players
                    ],
                    "survivors": result.survivors,
                    "game_data": result.game_data
                }
            )

            # Wait for players to see results
            await asyncio.sleep(5)

            # Check if game should end (only 1 or 0 living players) or trigger haunting race
            room = db.query(Room).filter(Room.code == room_code).first()
            living_count = db.query(Player).filter(
                Player.room_id == room.id,
                Player.is_ghost == False,
                Player.is_connected == True
            ).count()

            if living_count <= 1:
                print(f"[GAME] Living count <= 1 in room {room_code}. Checking for haunting race trigger...")

                # Check if haunting race should be triggered
                should_trigger_haunting_race = await self.check_haunting_race_trigger(room_code)
                is_already_active = self.active_haunting_races.get(room_code, False)

                print(f"[GAME] Haunting race check: should_trigger={should_trigger_haunting_race}, already_active={is_already_active}")

                if should_trigger_haunting_race and not is_already_active:
                    print(f"[GAME] ✓ Triggering haunting race for room {room_code}")
                    await self.start_haunting_race(room_code)
                else:
                    if is_already_active:
                        print(f"[GAME] Haunting race already active for room {room_code}, skipping")
                    else:
                        print(f"[GAME] Conditions not met for haunting race. Ending game for room {room_code}")
                    await self.end_game(room_code)
            else:
                # Continue to next question
                await self.next_question(room_code)

        finally:
            db.close()

    async def check_mini_game_timeout(self, room_code: str, timeout: int):
        """Check for mini-game timeout and force resolution"""
        print(f"[MINI-GAME TIMEOUT] Room {room_code}: Timeout task started, will wait {timeout} seconds")

        # Wait for timeout
        await asyncio.sleep(timeout)

        print(f"[MINI-GAME TIMEOUT] Room {room_code}: {timeout} seconds elapsed, checking if game needs resolution")

        # Check if still active and not resolved
        if not self.mini_game_manager.can_resolve(room_code):
            print(f"[MINI-GAME TIMEOUT] Room {room_code}: Game not resolved yet, forcing timeout resolution")
            db = SessionLocal()
            try:
                # Force resolution with timeout
                result = self.mini_game_manager.resolve_mini_game(
                    room_code,
                    db,
                    force=True  # Handle timeout
                )

                # Broadcast timeout message
                await self.connection_manager.broadcast_to_room(
                    room_code,
                    {
                        "type": "mini_game_timeout",
                        "message": "Time's up! Resolving mini-game..."
                    }
                )

                # Then show results
                if result.success:
                    eliminated_players = db.query(Player).filter(
                        Player.id.in_(result.eliminated_player_ids)
                    ).all()

                    # Get game name from active mini-game
                    mini_game = self.mini_game_manager.get_active_mini_game(room_code)
                    game_name = mini_game.name if mini_game else "Mini-Game"

                    await self.connection_manager.broadcast_to_room(
                        room_code,
                        {
                            "type": "mini_game_results",
                            "game_name": game_name,
                            "eliminated": [
                                {
                                    "player_id": p.id,
                                    "player_name": p.name
                                }
                                for p in eliminated_players
                            ],
                            "survivors": result.survivors,
                            "game_data": result.game_data,
                            "timeout": True
                        }
                    )

                    await asyncio.sleep(5)

                    # Continue game or trigger haunting race
                    room = db.query(Room).filter(Room.code == room_code).first()
                    living_count = db.query(Player).filter(
                        Player.room_id == room.id,
                        Player.is_ghost == False
                    ).count()

                    if living_count <= 1:
                        print(f"[GAME-TIMEOUT] Living count <= 1 in room {room_code}. Checking for haunting race trigger...")

                        # Check if haunting race should be triggered
                        should_trigger_haunting_race = await self.check_haunting_race_trigger(room_code)
                        is_already_active = self.active_haunting_races.get(room_code, False)

                        print(f"[GAME-TIMEOUT] Haunting race check: should_trigger={should_trigger_haunting_race}, already_active={is_already_active}")

                        if should_trigger_haunting_race and not is_already_active:
                            print(f"[GAME-TIMEOUT] ✓ Triggering haunting race for room {room_code}")
                            await self.start_haunting_race(room_code)
                        else:
                            if is_already_active:
                                print(f"[GAME-TIMEOUT] Haunting race already active for room {room_code}, skipping")
                            else:
                                print(f"[GAME-TIMEOUT] Conditions not met for haunting race. Ending game for room {room_code}")
                            await self.end_game(room_code)
                    else:
                        await self.next_question(room_code)

            finally:
                db.close()
        else:
            print(f"[MINI-GAME TIMEOUT] Room {room_code}: Game already resolved, timeout task exiting")

        # Clean up task reference
        if room_code in self.mini_game_timeout_tasks:
            del self.mini_game_timeout_tasks[room_code]