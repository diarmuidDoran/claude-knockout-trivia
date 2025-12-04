"""
Worst Answer Mini-Game

At-risk players (who answered incorrectly) are shown an opinion question and must
submit what they think is the WORST answer to that question.

All players (safe, at-risk, and ghosts) then vote on which answer is the worst.
The player whose answer gets the most votes is eliminated.

Players cannot vote for their own answer.

Rules:
- Random opinion question selected
- At-risk players submit worst answers (max 30 characters, alphanumeric + spaces)
- All players vote on the worst answer
- Player with most votes is eliminated
- Ties: random selection among tied players
- If player doesn't submit, they get auto-answer and likely eliminated
"""

from typing import List, Dict, Any
import random
import re
from .base_mini_game import BaseMiniGame, MiniGameResult, MiniGamePhase
from .opinion_questions import get_random_question


class WorstAnswerMiniGame(BaseMiniGame):
    """Worst Answer voting mini-game."""

    @property
    def name(self) -> str:
        return "Worst Answer"

    @property
    def description(self) -> str:
        return ("At-risk players submit worst answers to an opinion question. "
                "Everyone votes on the worst answer. Most votes = eliminated!")

    @property
    def min_players(self) -> int:
        return 2  # Need at least 2 at-risk players for voting to work

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
        Set up the Worst Answer game.

        Args:
            at_risk_players: Players who answered incorrectly (must submit answers)
            safe_players: Players who answered correctly (vote only)
            total_players: Total living players

        Returns:
            Setup data for frontend

        Raises:
            ValueError: If there are not enough players (need 2+ at-risk AND 1+ voter)
        """
        # Validate player counts - need at least 2 at-risk players AND at least 1 voter
        if len(at_risk_players) < 2:
            raise ValueError(f"Worst Answer requires at least 2 at-risk players, got {len(at_risk_players)}")

        # Need at least one voter (safe or ghost players will vote)
        # Note: Ghost players can vote too, so we check total_players - at_risk_players
        num_voters = total_players - len(at_risk_players)
        if num_voters < 1:
            raise ValueError(f"Worst Answer requires at least 1 voter (safe or ghost player), got {num_voters}")

        # Select random opinion question
        question = get_random_question()

        self.game_state = {
            "at_risk_players": at_risk_players,
            "safe_players": safe_players,
            "question": question,
            "submitted_answers": {},  # player_id -> answer_text
            "votes": {},  # voter_id -> voted_for_player_id
            "phase": "submission"  # submission -> voting -> complete
        }

        self.phase = MiniGamePhase.SETUP

        return {
            "question": question,
            "at_risk_players": at_risk_players,
            "safe_players": safe_players,
            "roles": {
                "at_risk": {
                    "description": "Submit what you think is the WORST answer to this question!",
                    "action": "submit_answer",
                    "max_length": 30
                },
                "safe": {
                    "description": "Wait for answers, then vote on the worst one!",
                    "action": "wait_then_vote"
                },
                "ghost": {
                    "description": "Wait for answers, then vote on the worst one!",
                    "action": "vote"
                }
            }
        }

    async def process_player_action(
        self,
        player_id: int,
        action: Dict[str, Any]
    ) -> bool:
        """
        Process a player's action (submitting answer or voting).

        Action format for Answer Submission:
        {
            "type": "submit_answer",
            "answer": "Happy Birthday"  # Max 30 chars, sanitized
        }

        Action format for Voting:
        {
            "type": "vote",
            "voted_for": 123  # Player ID being voted for
        }

        Args:
            player_id: ID of player taking action
            action: The action data

        Returns:
            True if action was valid, False otherwise
        """
        action_type = action.get("type")

        # Player submitting their worst answer
        if action_type == "submit_answer":
            if player_id not in self.game_state["at_risk_players"]:
                return False  # Only at-risk players can submit

            if self.game_state["phase"] != "submission":
                return False  # Not in submission phase

            answer = action.get("answer", "").strip()

            # Sanitize and validate answer
            if not self._is_valid_answer(answer):
                return False

            self.game_state["submitted_answers"][player_id] = answer
            self.player_actions[player_id] = action

            # Check if all at-risk players have submitted
            if len(self.game_state["submitted_answers"]) == len(self.game_state["at_risk_players"]):
                self.game_state["phase"] = "voting"

            return True

        # Player voting on worst answer
        elif action_type == "vote":
            if self.game_state["phase"] != "voting":
                return False  # Not in voting phase

            voted_for = action.get("voted_for")
            if not isinstance(voted_for, int):
                return False

            # Validate vote
            if voted_for not in self.game_state["submitted_answers"]:
                return False  # Can't vote for player who didn't submit

            if voted_for == player_id:
                return False  # Can't vote for yourself

            self.game_state["votes"][player_id] = voted_for
            self.player_actions[player_id] = action
            return True

        return False

    def _is_valid_answer(self, answer: str) -> bool:
        """
        Validate submitted answer for security and length.

        Rules:
        - Max 30 characters
        - Only letters, numbers, spaces, and basic punctuation
        - No special characters that could be code injection

        Args:
            answer: The answer to validate

        Returns:
            True if valid, False otherwise
        """
        if not answer or len(answer) > 30:
            return False

        # Allow only alphanumeric, spaces, and basic punctuation (.,!?'-)
        # This prevents code injection and special characters
        pattern = r'^[a-zA-Z0-9\s.,!?\'-]+$'
        return bool(re.match(pattern, answer))

    def can_resolve(self) -> bool:
        """
        Check if game can be resolved.

        For voting phase: All players (safe + at-risk + potentially ghosts) should vote.
        But we can resolve when we have enough votes to determine a winner.

        Returns:
            True if ready to resolve
        """
        # Need all at-risk players to submit first
        if self.game_state["phase"] == "submission":
            return len(self.game_state["submitted_answers"]) == len(self.game_state["at_risk_players"])

        # For voting, we need at least majority of players to vote
        # (being lenient to keep game moving)
        if self.game_state["phase"] == "voting":
            total_voters = len(self.game_state["at_risk_players"]) + len(self.game_state["safe_players"])
            votes_needed = max(1, total_voters // 2)  # At least half
            return len(self.game_state["votes"]) >= votes_needed

        return False

    def resolve(self) -> MiniGameResult:
        """
        Resolve the Worst Answer game.

        Count votes and eliminate the player with the most votes.
        Ties are broken randomly.

        Returns:
            MiniGameResult with elimination data
        """
        # Count votes for each player
        vote_counts = {}
        for player_id in self.game_state["submitted_answers"].keys():
            vote_counts[player_id] = 0

        for voted_for in self.game_state["votes"].values():
            vote_counts[voted_for] = vote_counts.get(voted_for, 0) + 1

        # Find player(s) with most votes
        if vote_counts:
            max_votes = max(vote_counts.values())
            worst_players = [p for p, v in vote_counts.items() if v == max_votes]

            # Random selection if tie
            eliminated_player = random.choice(worst_players)
        else:
            # No votes cast, eliminate random at-risk player
            eliminated_player = random.choice(self.game_state["at_risk_players"])

        # Survivors are all other at-risk players
        survivors = [p for p in self.game_state["at_risk_players"] if p != eliminated_player]

        self.phase = MiniGamePhase.RESULTS

        return MiniGameResult(
            eliminated_player_ids=[eliminated_player],
            survivors=survivors,
            game_data={
                "question": self.game_state["question"],
                "submitted_answers": self.game_state["submitted_answers"],
                "votes": self.game_state["votes"],
                "vote_counts": vote_counts,
                "eliminated_player": eliminated_player,
                "elimination_reason": f"Received {vote_counts.get(eliminated_player, 0)} votes for worst answer"
            },
            success=True
        )

    def handle_timeout(self) -> MiniGameResult:
        """
        Handle timeout scenario.

        Submission phase timeout:
        - Players who didn't submit get auto-answer "..."
        - Proceed to voting

        Voting phase timeout:
        - Players who didn't vote: their vote doesn't count
        - Resolve with current votes

        Returns:
            MiniGameResult after handling timeout
        """
        if self.game_state["phase"] == "submission":
            # Give auto-answers to players who didn't submit
            for player_id in self.game_state["at_risk_players"]:
                if player_id not in self.game_state["submitted_answers"]:
                    self.game_state["submitted_answers"][player_id] = "..."

            # Move to voting phase
            self.game_state["phase"] = "voting"

            # If only 1 at-risk player, auto-eliminate them
            if len(self.game_state["at_risk_players"]) == 1:
                eliminated = self.game_state["at_risk_players"][0]
                return MiniGameResult(
                    eliminated_player_ids=[eliminated],
                    survivors=[],
                    game_data={
                        "question": self.game_state["question"],
                        "submitted_answers": self.game_state["submitted_answers"],
                        "timeout": True,
                        "reason": "Only one at-risk player"
                    },
                    success=True
                )

            # Give more time for voting (shouldn't happen immediately)
            return MiniGameResult(
                eliminated_player_ids=[],
                survivors=[],
                game_data={"waiting_for": "votes"},
                success=False,
                error_message="Timeout in submission, proceeding to voting"
            )

        elif self.game_state["phase"] == "voting":
            # Resolve with current votes
            return self.resolve()

        return self.resolve()

    def get_timeout_seconds(self) -> int:
        """
        Get timeout for Worst Answer game.

        Submission phase: 30 seconds
        Voting phase: 30 seconds
        Total: 60 seconds max

        Returns:
            Timeout in seconds
        """
        if self.game_state.get("phase") == "submission":
            return 30
        elif self.game_state.get("phase") == "voting":
            return 30
        return 30  # Default
