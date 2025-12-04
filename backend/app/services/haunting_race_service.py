"""
Haunting Race Service

Endgame mode triggered when only 1 living player remains vs 2+ ghost players.
The unicorn player (living) must race to the end (column 20) while ghosts chase.

Game Mechanics:
- 20-column race track
- Unicorn starts at column 4-8 based on score lead
- Ghosts start at column 1, positioned by score difference
- 40 seconds per question
- True/False statements (Unicorn sees 2, Ghosts see 3)
- +1 space for each correct selection (true=select, false=don't select)
- Ghost catches unicorn = swap roles + pushback
- First to reach column 20 as unicorn wins
"""

import random
import time
from typing import List, Dict, Any, Tuple, Optional
from sqlalchemy.orm import Session
from ..models.models import HauntingRaceQuestion, HauntingRaceStatement, Player
from ..models.database import SessionLocal


class HauntingRaceService:
    """Service for managing the Haunting Race endgame."""

    TOTAL_COLUMNS = 20
    MIN_UNICORN_START = 4
    MAX_UNICORN_START = 8
    POINTS_PER_SPACE = 500  # 500 points difference = 1 space back
    TIME_LIMIT = 20  # seconds per question

    def __init__(self, connection_manager):
        self.connection_manager = connection_manager
        self.game_state = {}
        self.used_question_ids = set()

    def can_trigger_haunting_race(self, players: List[Dict]) -> bool:
        """
        Check if haunting race should be triggered.

        Args:
            players: List of player dicts with is_ghost and other data

        Returns:
            True if exactly 1 living player and 2+ ghosts
        """
        living_players = [p for p in players if not p.get("is_ghost", False)]
        ghost_players = [p for p in players if p.get("is_ghost", False)]

        can_trigger = len(living_players) == 1 and len(ghost_players) >= 2
        print(f"[HAUNTING-RACE] Can trigger: {can_trigger} (Living: {len(living_players)}, Ghosts: {len(ghost_players)})")
        return can_trigger

    def setup_race(self, room_code: str, players: List[Dict]) -> Dict[str, Any]:
        """
        Setup the haunting race with starting positions.

        Args:
            room_code: The game room code
            players: List of player dicts with id, name, score, is_ghost

        Returns:
            Setup data for frontend
        """
        print(f"[HAUNTING-RACE] ===== SETTING UP RACE =====")
        print(f"[HAUNTING-RACE] Room: {room_code}")
        print(f"[HAUNTING-RACE] Players: {players}")

        # Identify unicorn and ghosts
        unicorn_player = None
        ghost_players = []

        for player in players:
            if not player.get("is_ghost", False):
                unicorn_player = player
            else:
                ghost_players.append(player)

        if not unicorn_player or len(ghost_players) < 1:
            raise ValueError("Invalid player configuration for haunting race")

        print(f"[HAUNTING-RACE] Unicorn: {unicorn_player['name']} (Score: {unicorn_player['total_score']})")
        print(f"[HAUNTING-RACE] Ghosts: {[(g['name'], g['total_score']) for g in ghost_players]}")

        # Calculate starting positions
        starting_positions = self._calculate_starting_positions(unicorn_player, ghost_players)

        # Initialize game state
        self.game_state = {
            "room_code": room_code,
            "unicorn_id": unicorn_player["id"],
            "ghost_ids": [g["id"] for g in ghost_players],
            "positions": starting_positions,  # player_id -> column (1-20)
            "question_number": 0,
            "player_answers": {},  # player_id -> {statements_selected: [], response_time: float}
            "current_question_id": None,
            "phase": "setup",  # setup, question, results, complete
            "question_start_time": None,
        }

        print(f"[HAUNTING-RACE] Starting positions: {starting_positions}")

        return {
            "race_id": room_code,
            "unicorn_player": {
                "id": unicorn_player["id"],
                "name": unicorn_player["name"],
                "starting_position": starting_positions[unicorn_player["id"]]
            },
            "ghost_players": [
                {
                    "id": g["id"],
                    "name": g["name"],
                    "starting_position": starting_positions[g["id"]]
                }
                for g in ghost_players
            ],
            "total_columns": self.TOTAL_COLUMNS,
            "time_limit": self.TIME_LIMIT,
            "rules": {
                "unicorn_sees": 2,  # statements
                "ghosts_see": 3,  # statements
                "winning_column": self.TOTAL_COLUMNS
            }
        }

    def _calculate_starting_positions(self, unicorn: Dict, ghosts: List[Dict]) -> Dict[int, int]:
        """
        Calculate starting positions based on score differences.

        Rules:
        - Ghosts start at column 1-4 (based on scores relative to lowest ghost)
        - Unicorn ALWAYS has a MINIMUM 4-space lead over the closest ghost
        - Additional score-based bonus on top of minimum lead
        - Unicorn can go beyond column 8 if needed to maintain 4-space lead

        Args:
            unicorn: The unicorn player dict
            ghosts: List of ghost player dicts

        Returns:
            Dict mapping player_id -> starting_column (1-20)
        """
        unicorn_score = unicorn["total_score"]
        positions = {}

        # Find lowest scoring ghost
        ghost_scores = sorted([g["total_score"] for g in ghosts])
        lowest_ghost_score = ghost_scores[0]

        # Position ghosts FIRST (columns 1-4)
        # Lowest scoring ghost at column 1
        # Others positioned between 2-4 based on their score relative to lowest
        for ghost in ghosts:
            ghost_score = ghost["total_score"]
            score_diff_from_lowest = ghost_score - lowest_ghost_score

            if score_diff_from_lowest == 0:
                # Lowest scoring ghost(s)
                ghost_position = 1
            else:
                # Position between 2-4 based on score
                # Every 500 points above lowest = +1 column (max column 4)
                additional_spaces = min(score_diff_from_lowest // self.POINTS_PER_SPACE, 3)
                ghost_position = 1 + additional_spaces

            positions[ghost["id"]] = ghost_position
            print(f"[HAUNTING-RACE] Ghost {ghost['name']}: {ghost_score} pts → Column {ghost_position}")

        # Find the closest (highest column) ghost position
        max_ghost_position = max(positions[g["id"]] for g in ghosts)
        print(f"[HAUNTING-RACE] Closest ghost at column: {max_ghost_position}")

        # Calculate unicorn position with MINIMUM 4-space lead guarantee
        # Start with minimum position (4 spaces ahead of closest ghost)
        minimum_unicorn_position = max_ghost_position + 4

        # Calculate score-based bonus
        score_lead = unicorn_score - lowest_ghost_score
        score_bonus_spaces = score_lead // self.POINTS_PER_SPACE

        # Unicorn position = minimum lead + score bonus (HARD CAP at column 8)
        # MAX_UNICORN_START = 8 is the absolute maximum starting position
        unicorn_position = min(minimum_unicorn_position + score_bonus_spaces, self.MAX_UNICORN_START)

        # Ensure we never go below the minimum 4-space lead
        unicorn_position = max(unicorn_position, minimum_unicorn_position)

        # Final validation: unicorn position must be <= 8
        unicorn_position = min(unicorn_position, self.MAX_UNICORN_START)

        positions[unicorn["id"]] = unicorn_position

        print(f"[HAUNTING-RACE] Unicorn score: {unicorn_score}, Lead over lowest: {score_lead} pts")
        print(f"[HAUNTING-RACE] Unicorn position: Column {unicorn_position} (Lead over closest ghost: {unicorn_position - max_ghost_position} spaces, Max allowed: {self.MAX_UNICORN_START})")

        return positions

    def get_next_question(self) -> Dict[str, Any]:
        """
        Get the next haunting race question.

        Returns:
            Question data with statements
        """
        db = SessionLocal()
        try:
            # Get random unused question
            query = db.query(HauntingRaceQuestion).filter(
                HauntingRaceQuestion.is_active == True
            )

            if self.used_question_ids:
                query = query.filter(HauntingRaceQuestion.id.notin_(self.used_question_ids))

            questions = query.all()

            if not questions:
                # Reset used questions if we've exhausted the pool
                self.used_question_ids.clear()
                questions = query.all()

            if not questions:
                raise ValueError("No haunting race questions available")

            question = random.choice(questions)
            self.used_question_ids.add(question.id)

            # Increment question number
            self.game_state["question_number"] += 1
            self.game_state["current_question_id"] = question.id
            self.game_state["phase"] = "question"
            self.game_state["question_start_time"] = time.time()
            self.game_state["player_answers"] = {}  # Reset answers

            print(f"[HAUNTING-RACE] Question #{self.game_state['question_number']}: {question.question_text}")

            # Format statements
            statements = []
            for stmt in sorted(question.statements, key=lambda s: s.statement_order):
                statements.append({
                    "id": stmt.id,
                    "text": stmt.statement_text,
                    "order": stmt.statement_order,
                    "is_ghost_only": stmt.is_ghost_only
                })

            return {
                "question_id": question.id,
                "question_number": self.game_state["question_number"],
                "question_text": question.question_text,
                "category": question.category,
                "time_limit": self.TIME_LIMIT,
                "statements": statements,
                "is_first_question": self.game_state["question_number"] == 1
            }
        finally:
            db.close()

    def submit_answer(self, player_id: int, selected_statement_ids: List[int], response_time: float) -> bool:
        """
        Submit a player's answer (selected true statements).

        Args:
            player_id: The player's ID
            selected_statement_ids: List of statement IDs the player believes are TRUE
            response_time: Time taken to answer in seconds

        Returns:
            True if answer was accepted, False otherwise
        """
        if self.game_state["phase"] != "question":
            print(f"[HAUNTING-RACE] Answer rejected - not in question phase")
            return False

        if player_id in self.game_state["player_answers"]:
            print(f"[HAUNTING-RACE] Answer rejected - player {player_id} already answered")
            return False

        self.game_state["player_answers"][player_id] = {
            "selected_statement_ids": selected_statement_ids,
            "response_time": response_time,
            "timestamp": time.time()
        }

        print(f"[HAUNTING-RACE] Player {player_id} answered: selected {len(selected_statement_ids)} statements")
        return True

    def can_resolve_question(self) -> bool:
        """Check if all players have answered or time is up."""
        if self.game_state["phase"] != "question":
            return False

        all_player_ids = [self.game_state["unicorn_id"]] + self.game_state["ghost_ids"]
        all_answered = all(pid in self.game_state["player_answers"] for pid in all_player_ids)

        # Check timeout
        elapsed = time.time() - self.game_state["question_start_time"]
        timed_out = elapsed >= self.TIME_LIMIT

        return all_answered or timed_out

    def resolve_question(self) -> Dict[str, Any]:
        """
        Resolve the current question and update positions.

        Returns:
            Results including movements and unicorn swaps
        """
        print(f"[HAUNTING-RACE] ===== RESOLVING QUESTION =====")

        db = SessionLocal()
        try:
            question_id = self.game_state["current_question_id"]
            question = db.query(HauntingRaceQuestion).filter(HauntingRaceQuestion.id == question_id).first()

            # Get correct answers (statement IDs that are TRUE)
            correct_true_ids = set(s.id for s in question.statements if s.is_true)
            correct_false_ids = set(s.id for s in question.statements if not s.is_true)

            print(f"[HAUNTING-RACE] Correct TRUE statements: {correct_true_ids}")
            print(f"[HAUNTING-RACE] Correct FALSE statements: {correct_false_ids}")

            # Calculate movement for each player
            movements = {}
            player_results = {}

            for player_id in [self.game_state["unicorn_id"]] + self.game_state["ghost_ids"]:
                if player_id not in self.game_state["player_answers"]:
                    # No answer = no movement
                    movements[player_id] = 0
                    player_results[player_id] = {"spaces_moved": 0, "reason": "No answer"}
                    print(f"[HAUNTING-RACE] Player {player_id}: No answer → 0 spaces")
                    continue

                answer = self.game_state["player_answers"][player_id]
                selected_ids = set(answer["selected_statement_ids"])

                # Determine which statements this player can see
                is_unicorn = player_id == self.game_state["unicorn_id"]
                if is_unicorn:
                    # Unicorn only sees non-ghost-only statements (first 2)
                    visible_stmt_ids = set(s.id for s in question.statements if not s.is_ghost_only)
                else:
                    # Ghosts see all 3 statements
                    visible_stmt_ids = set(s.id for s in question.statements)

                # Calculate points:
                # +1 for each TRUE statement they selected (if it's truly TRUE)
                # +1 for each FALSE statement they didn't select (if it's truly FALSE)

                correct_true_selections = selected_ids & correct_true_ids & visible_stmt_ids
                # False statements they correctly didn't select
                visible_false_ids = correct_false_ids & visible_stmt_ids
                correct_false_non_selections = visible_false_ids - selected_ids

                spaces_moved = len(correct_true_selections) + len(correct_false_non_selections)

                movements[player_id] = spaces_moved
                player_results[player_id] = {
                    "spaces_moved": spaces_moved,
                    "correct_true": len(correct_true_selections),
                    "correct_false": len(correct_false_non_selections),
                    "response_time": answer["response_time"]
                }

                print(f"[HAUNTING-RACE] Player {player_id}: +{spaces_moved} spaces")

            # Move unicorn FIRST and check for win
            unicorn_id = self.game_state["unicorn_id"]
            swap_result = None  # Initialize to None

            if unicorn_id in movements:
                old_position = self.game_state["positions"][unicorn_id]
                new_position = min(old_position + movements[unicorn_id], self.TOTAL_COLUMNS)
                self.game_state["positions"][unicorn_id] = new_position
                print(f"[HAUNTING-RACE] Unicorn {unicorn_id} moved from {old_position} to {new_position}")

            # Check win condition BEFORE moving ghosts
            unicorn_position = self.game_state["positions"][unicorn_id]
            game_won = unicorn_position >= self.TOTAL_COLUMNS

            if game_won:
                self.game_state["phase"] = "complete"
                print(f"[HAUNTING-RACE] GAME WON by unicorn player {unicorn_id}!")
            else:
                # Unicorn didn't win, now move ghosts
                for player_id in self.game_state["ghost_ids"]:
                    if player_id in movements:
                        old_position = self.game_state["positions"][player_id]
                        new_position = min(old_position + movements[player_id], self.TOTAL_COLUMNS)
                        self.game_state["positions"][player_id] = new_position
                        print(f"[HAUNTING-RACE] Ghost {player_id} moved from {old_position} to {new_position}")

                # Check for unicorn swaps (ghosts catching unicorn)
                swap_result = self._check_unicorn_swap(movements)

                self.game_state["phase"] = "results"

            # Format statements with answers for results display
            statements_with_answers = []
            for stmt in sorted(question.statements, key=lambda s: s.statement_order):
                statements_with_answers.append({
                    "id": stmt.id,
                    "text": stmt.statement_text,
                    "is_true": stmt.is_true,
                    "is_ghost_only": stmt.is_ghost_only,
                    "order": stmt.statement_order
                })

            # Get winner information if game is won
            winner_info = None
            if game_won:
                winner_player = db.query(Player).filter(Player.id == self.game_state["unicorn_id"]).first()
                if winner_player:
                    winner_info = {
                        "player_id": winner_player.id,
                        "player_name": winner_player.name
                    }

            return {
                "question_id": question_id,
                "question_text": question.question_text,
                "statements": statements_with_answers,
                "player_results": player_results,
                "movements": movements,
                "positions": self.game_state["positions"].copy(),
                "unicorn_swap": swap_result,
                "game_won": game_won,
                "winner": winner_info
            }
        finally:
            db.close()

    def _check_unicorn_swap(self, movements: Dict[int, int]) -> Optional[Dict[str, Any]]:
        """
        Check if the leader changed - leader should always be the unicorn.

        The player at the highest position is always the unicorn.
        If a ghost overtakes the unicorn, they swap roles.

        Args:
            movements: player_id -> spaces_moved this turn

        Returns:
            Swap result dict or None
        """
        current_unicorn_id = self.game_state["unicorn_id"]
        all_player_ids = [current_unicorn_id] + self.game_state["ghost_ids"]

        # Find the highest position (leader)
        max_position = max(self.game_state["positions"][pid] for pid in all_player_ids)

        # Find all players at the highest position (could be tied)
        leaders = [
            pid for pid in all_player_ids
            if self.game_state["positions"][pid] == max_position
        ]

        print(f"[HAUNTING-RACE] Position check - Max position: {max_position}, Leaders: {leaders}")

        # If current unicorn is the only leader, no swap needed
        if len(leaders) == 1 and leaders[0] == current_unicorn_id:
            print(f"[HAUNTING-RACE] Unicorn {current_unicorn_id} maintains lead")
            return None

        # If ghost(s) caught or overtook the unicorn, swap occurs
        # Find all ghosts at the lead position
        ghost_leaders = [pid for pid in leaders if pid in self.game_state["ghost_ids"]]

        if not ghost_leaders:
            # This shouldn't happen, but safeguard
            return None

        # If multiple ghosts tied for lead, pick the fastest
        if len(ghost_leaders) > 1:
            # Sort by response time (fastest first)
            ghost_leaders_data = [
                (gid, self.game_state["player_answers"].get(gid, {}).get("response_time", 999))
                for gid in ghost_leaders
            ]
            ghost_leaders_data.sort(key=lambda x: x[1])
            new_unicorn_id = ghost_leaders_data[0][0]
            fastest_time = ghost_leaders_data[0][1]

            print(f"[HAUNTING-RACE] Multiple ghost leaders - fastest: {new_unicorn_id} ({fastest_time}s)")
        else:
            new_unicorn_id = ghost_leaders[0]

        print(f"[HAUNTING-RACE] Ghost {new_unicorn_id} caught/overtook unicorn {current_unicorn_id}! SWAPPING ROLES")

        # Perform swap
        old_unicorn_id = current_unicorn_id
        self.game_state["unicorn_id"] = new_unicorn_id
        self.game_state["ghost_ids"].remove(new_unicorn_id)
        self.game_state["ghost_ids"].append(old_unicorn_id)

        # Push old unicorn back 1 space (minimum position 1)
        old_position = self.game_state["positions"][old_unicorn_id]
        new_position = max(1, old_position - 1)
        self.game_state["positions"][old_unicorn_id] = new_position

        print(f"[HAUNTING-RACE] Swap complete: Unicorn is now {new_unicorn_id}, {old_unicorn_id} pushed back from {old_position} to {new_position}")

        return {
            "old_unicorn_id": old_unicorn_id,
            "new_unicorn_id": new_unicorn_id,
            "ghost_ids": self.game_state["ghost_ids"].copy(),
            "new_positions": self.game_state["positions"].copy(),
            "reason": "overtake",
            "position": max_position
        }

    def get_game_state(self) -> Dict[str, Any]:
        """Get current game state for frontend."""
        return {
            "unicorn_id": self.game_state["unicorn_id"],
            "ghost_ids": self.game_state["ghost_ids"],
            "positions": self.game_state["positions"].copy(),
            "question_number": self.game_state["question_number"],
            "phase": self.game_state["phase"]
        }
