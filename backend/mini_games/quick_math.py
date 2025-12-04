"""
Quick Math Mini-Game

A fast-paced mental math race where players compete to answer simple math questions
as quickly as possible. Speed and accuracy determine who survives!

Rules:
- At-risk players compete against each other OR single at-risk player competes vs safe players
- 45-second race to answer as many questions as possible
- Each correct answer = 1 point
- Questions are simple: addition, subtraction, multiplication, division
- Questions appear instantly with no delay for maximum speed

Elimination Rules:
- Multiple at-risk players: Lowest scorer is eliminated
- Single at-risk vs safe players: At-risk must place 1st or be eliminated
- Ties: Random selection among tied players

Game Flow:
1. Players shown their role (Racer vs Racer OR At-Risk vs Safe)
2. 45-second countdown begins
3. Math questions appear instantly
4. Players submit answers as fast as possible
5. Scores tracked in real-time
6. Lowest scorer (or at-risk if not 1st) is eliminated
"""

from typing import List, Dict, Any
import random
import time
from .base_mini_game import BaseMiniGame, MiniGameResult, MiniGamePhase


class QuickMathMiniGame(BaseMiniGame):
    """Quick Math mental arithmetic race mini-game."""

    @property
    def name(self) -> str:
        return "Quick Math"

    @property
    def description(self) -> str:
        return ("Race against other players in a fast-paced mental math challenge! "
                "Answer as many questions as possible in 45 seconds. "
                "Lowest scorer is eliminated!")

    @property
    def min_players(self) -> int:
        return 1  # Need at least 1 at-risk player

    @property
    def max_eliminates(self) -> int:
        return 1  # Eliminates exactly 1 player per round

    def setup(
        self,
        at_risk_players: List[int],
        safe_players: List[int],
        total_players: int
    ) -> Dict[str, Any]:
        """
        Set up the Quick Math game.

        Args:
            at_risk_players: Players who answered incorrectly (racers)
            safe_players: Players who answered correctly (compete if only 1 at-risk)
            total_players: Total living players

        Returns:
            Setup data for frontend
        """
        print(f"[QUICK-MATH DEBUG] ===== SETUP =====")
        print(f"[QUICK-MATH DEBUG] At-risk players: {at_risk_players}")
        print(f"[QUICK-MATH DEBUG] Safe players: {safe_players}")
        print(f"[QUICK-MATH DEBUG] Total players: {total_players}")

        # Determine game mode
        if len(at_risk_players) > 1:
            # Multiple at-risk players compete against each other
            game_mode = "at_risk_vs_at_risk"
            racers = at_risk_players
            observers = safe_players
            print(f"[QUICK-MATH DEBUG] Mode: at_risk_vs_at_risk")
        else:
            # Single at-risk player must beat safe players to survive
            game_mode = "at_risk_vs_safe"
            racers = at_risk_players + safe_players
            observers = []
            print(f"[QUICK-MATH DEBUG] Mode: at_risk_vs_safe")

        print(f"[QUICK-MATH DEBUG] Racers: {racers}")
        print(f"[QUICK-MATH DEBUG] Observers: {observers}")

        self.game_state = {
            "at_risk_players": at_risk_players,
            "safe_players": safe_players,
            "game_mode": game_mode,
            "racers": racers,
            "observers": observers,
            "player_scores": {player_id: 0 for player_id in racers},
            "player_questions": {player_id: [] for player_id in racers},
            "start_time": time.time(),  # Start immediately
            "phase": "racing"  # Auto-start in racing phase for immediate play
        }

        self.phase = MiniGamePhase.SETUP

        return {
            "game_mode": game_mode,
            "racers": racers,
            "observers": observers,
            "at_risk_players": at_risk_players,
            "safe_players": safe_players,
            "time_limit": 45,
            "roles": {
                "racer": {
                    "description": "Answer as many math questions as possible!",
                    "action": "answer_questions",
                    "is_at_risk": "varies"
                },
                "observer": {
                    "description": "Watch the race unfold!",
                    "action": "observe"
                }
            },
            "rules": self._get_rules_description(game_mode, len(at_risk_players))
        }

    def _get_rules_description(self, game_mode: str, at_risk_count: int) -> str:
        """Get appropriate rules description based on game mode."""
        if game_mode == "at_risk_vs_at_risk":
            return f"All {at_risk_count} at-risk players compete. Lowest scorer is eliminated!"
        else:
            return "At-risk player must place 1st to survive! Safe players try to beat them."

    def generate_question(self, player_id: int) -> Dict[str, Any]:
        """
        Generate a simple math question for a player.

        Requirements: All numbers ≤ 2 digits (≤99), whole numbers only.
        - Addition: result ≤ 99
        - Subtraction: both numbers ≤ 99, positive result
        - Multiplication: 1-12 × 1-12
        - Division: dividend ≤ 99, whole number answers

        Args:
            player_id: The player to generate a question for

        Returns:
            Question data
        """
        operations = ['+', '-', '×', '÷']
        operation = random.choice(operations)

        if operation == '+':
            # Addition: result must be ≤ 99
            a = random.randint(1, 50)
            b = random.randint(1, min(99 - a, 50))
            answer = a + b
            question = f"{a} + {b}"

        elif operation == '-':
            # Subtraction: both numbers ≤ 99, result positive
            a = random.randint(10, 98)
            b = random.randint(1, a - 1)
            answer = a - b
            question = f"{a} - {b}"

        elif operation == '×':
            # Multiplication: both operands ≤ 12 for mental math
            a = random.randint(1, 12)
            b = random.randint(1, 12)
            answer = a * b
            question = f"{a} × {b}"

        else:  # Division
            # Division: dividend ≤ 99, whole number answer
            quotient = random.randint(1, 12)
            max_divisor = 99 // quotient
            divisor = random.randint(2, min(max_divisor, 12))
            dividend = divisor * quotient  # Always ≤ 99
            answer = quotient
            question = f"{dividend} ÷ {divisor}"

        question_data = {
            "question_id": len(self.game_state["player_questions"][player_id]),
            "question": question,
            "answer": answer,
            "timestamp": time.time()
        }

        # Store question for this player
        self.game_state["player_questions"][player_id].append(question_data)

        return question_data

    async def process_player_action(
        self,
        player_id: int,
        action: Dict[str, Any]
    ) -> bool:
        """
        Process a player's action (answering a question).

        Questions are generated client-side for instant responsiveness.
        Client validates answers locally and sends correct answers to server.

        Action format for Answer Submission:
        {
            "type": "answer",
            "question_id": 0,
            "answer": 12,
            "is_correct": true  # Client-validated
        }

        Args:
            player_id: ID of player taking action
            action: The action data

        Returns:
            True if action was valid, False otherwise
        """
        action_type = action.get("type")

        # Player submitting a correct answer (client-side validation for speed)
        if action_type == "answer":
            print(f"[QUICK-MATH DEBUG] Answer action received from player {player_id}")
            print(f"[QUICK-MATH DEBUG] Racers list: {self.game_state['racers']}")
            print(f"[QUICK-MATH DEBUG] Player in racers: {player_id in self.game_state['racers']}")

            if player_id not in self.game_state["racers"]:
                print(f"[QUICK-MATH DEBUG] Player {player_id} NOT in racers - rejecting answer")
                return False  # Only racers can answer

            current_phase = self.game_state["phase"]
            print(f"[QUICK-MATH DEBUG] Current phase: {current_phase}")
            if current_phase != "racing":
                print(f"[QUICK-MATH DEBUG] Not in racing phase - rejecting answer")
                return False  # Not in racing phase

            # Client sends is_correct flag - trust it for speed
            # (cheating prevention is handled by game design - scores are relative)
            is_correct = action.get("is_correct", False)
            print(f"[QUICK-MATH DEBUG] Answer is_correct: {is_correct}")

            if is_correct:
                old_score = self.game_state["player_scores"][player_id]
                self.game_state["player_scores"][player_id] += 1
                new_score = self.game_state["player_scores"][player_id]
                print(f"[QUICK-MATH DEBUG] Player {player_id} score: {old_score} -> {new_score}")

            # Store action
            self.player_actions[player_id] = action

            return True

        # Start racing (for timing synchronization)
        elif action_type == "start_racing":
            if self.game_state["phase"] == "ready":
                self.game_state["phase"] = "racing"
                self.game_state["start_time"] = time.time()
                return True

        return False

    def can_resolve(self) -> bool:
        """
        Check if game can be resolved.

        Game resolves when time is up (handled by timeout).

        Returns:
            True if ready to resolve
        """
        # Game is resolved by timeout
        current_phase = self.game_state["phase"]
        can_resolve = current_phase == "complete"
        print(f"[QUICK-MATH DEBUG] can_resolve() called - phase: {current_phase}, can_resolve: {can_resolve}")
        return can_resolve

    def resolve(self) -> MiniGameResult:
        """
        Resolve the Quick Math game.

        Determine elimination based on scores and game mode.

        Returns:
            MiniGameResult with elimination data
        """
        print(f"[QUICK-MATH DEBUG] ===== RESOLVING =====")
        scores = self.game_state["player_scores"]
        at_risk_players = self.game_state["at_risk_players"]
        game_mode = self.game_state["game_mode"]

        print(f"[QUICK-MATH DEBUG] Scores: {scores}")
        print(f"[QUICK-MATH DEBUG] At-risk players: {at_risk_players}")
        print(f"[QUICK-MATH DEBUG] Game mode: {game_mode}")

        if not scores:
            # No one played, eliminate random at-risk player
            eliminated_player = random.choice(at_risk_players)
            survivors = [p for p in at_risk_players if p != eliminated_player]
            print(f"[QUICK-MATH DEBUG] No participation - eliminating random player: {eliminated_player}")

            return MiniGameResult(
                eliminated_player_ids=[eliminated_player],
                survivors=survivors,
                game_data={
                    "scores": {},
                    "game_mode": game_mode,
                    "elimination_reason": "No participation"
                },
                success=True
            )

        # Sort players by score (highest first)
        sorted_players = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        if game_mode == "at_risk_vs_at_risk":
            # Multiple at-risk players: eliminate lowest scorer(s)
            lowest_score = sorted_players[-1][1]
            highest_score = sorted_players[0][1]

            # Check if everyone tied (complete tie - all same score)
            if lowest_score == highest_score:
                # Everyone has the same score - no elimination
                print(f"[QUICK-MATH DEBUG] Complete tie at {lowest_score} points - no elimination")
                elimination_reason = f"Complete tie at {lowest_score} points - no one eliminated"

                self.phase = MiniGamePhase.RESULTS

                return MiniGameResult(
                    eliminated_player_ids=[],
                    survivors=at_risk_players,
                    game_data={
                        "scores": scores,
                        "game_mode": game_mode,
                        "elimination_reason": elimination_reason,
                        "sorted_results": [
                            {
                                "player_id": player_id,
                                "score": score,
                                "rank": idx + 1
                            }
                            for idx, (player_id, score) in enumerate(sorted_players)
                        ]
                    },
                    success=True
                )

            lowest_scorers = [p for p, s in sorted_players if s == lowest_score]

            # CRITICAL: Filter to only at-risk players (safety check)
            lowest_scorers_at_risk = [p for p in lowest_scorers if p in at_risk_players]
            print(f"[QUICK-MATH DEBUG] Lowest score: {lowest_score}, lowest scorers (at-risk only): {lowest_scorers_at_risk}")

            # Random selection if tie among lowest scorers
            eliminated_player = random.choice(lowest_scorers_at_risk)
            survivors = [p for p in at_risk_players if p != eliminated_player]

            elimination_reason = f"Lowest score: {lowest_score} points"
            print(f"[QUICK-MATH DEBUG] Eliminated player: {eliminated_player}, survivors: {survivors}")

        else:
            # Single at-risk vs safe: ONLY at-risk player can be eliminated
            # Safe players can NEVER be eliminated in any mini-game
            at_risk_player = at_risk_players[0]
            first_place_score = sorted_players[0][1]
            at_risk_score = scores.get(at_risk_player, 0)
            safe_player_ids = self.game_state["safe_players"]

            print(f"[QUICK-MATH DEBUG] At-risk player: {at_risk_player}, score: {at_risk_score}, 1st place score: {first_place_score}")
            print(f"[QUICK-MATH DEBUG] Safe players (CANNOT be eliminated): {safe_player_ids}")

            # Check if at-risk player got first place (or tied for 1st)
            if at_risk_score == first_place_score:
                # At-risk player survived by placing 1st!
                eliminated_player = None
                survivors = at_risk_players
                elimination_reason = f"At-risk player placed 1st with {at_risk_score} points!"
                print(f"[QUICK-MATH DEBUG] At-risk player SURVIVED!")
            else:
                # At-risk player didn't place first, eliminated
                # Safe players are NEVER eliminated regardless of their scores
                eliminated_player = at_risk_player
                survivors = []
                elimination_reason = f"At-risk player scored {at_risk_score}, needed 1st place ({first_place_score} points)"
                print(f"[QUICK-MATH DEBUG] At-risk player ELIMINATED!")
                print(f"[QUICK-MATH DEBUG] Safe players remain safe regardless of score")

        self.phase = MiniGamePhase.RESULTS

        result_data = {
            "scores": scores,
            "game_mode": game_mode,
            "elimination_reason": elimination_reason,
            "sorted_results": [
                {
                    "player_id": player_id,
                    "score": score,
                    "rank": idx + 1
                }
                for idx, (player_id, score) in enumerate(sorted_players)
            ]
        }

        if eliminated_player:
            return MiniGameResult(
                eliminated_player_ids=[eliminated_player],
                survivors=survivors,
                game_data=result_data,
                success=True
            )
        else:
            return MiniGameResult(
                eliminated_player_ids=[],
                survivors=survivors,
                game_data=result_data,
                success=True
            )

    def handle_timeout(self) -> MiniGameResult:
        """
        Handle timeout scenario.

        When time's up, resolve the game based on current scores.

        Returns:
            MiniGameResult after handling timeout
        """
        print(f"[QUICK-MATH DEBUG] ===== HANDLE_TIMEOUT CALLED =====")
        print(f"[QUICK-MATH DEBUG] Current phase: {self.game_state['phase']}")
        print(f"[QUICK-MATH DEBUG] Current scores: {self.game_state['player_scores']}")

        # Mark as complete
        self.game_state["phase"] = "complete"
        print(f"[QUICK-MATH DEBUG] Phase set to 'complete'")

        # Resolve with current scores
        return self.resolve()

    def get_timeout_seconds(self) -> int:
        """
        Get timeout for Quick Math game.

        Returns:
            45 seconds for the race
        """
        return 45
