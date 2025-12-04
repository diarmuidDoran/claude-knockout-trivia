"""
Grab More Points Mini-Game

A prisoner's dilemma game where at-risk players must decide whether to grab extra points.
The twist: if anyone grabs points, those who don't become ghost players!

Rules:
- At-risk players can grab 0-1000 bonus points
- Points are ALWAYS added to player's score (regardless of outcome)
- If NO ONE takes points: NO ONE becomes a ghost player (all survive)
- If SOME take points: Players who DIDN'T take points become ghost players
- If ALL take points: Everyone becomes a ghost player

Elimination Rules:
- 0 players grab points → 0 eliminations (all survive)
- Some players grab points → Eliminate those who took 0 points
- All players grab points → Everyone eliminated

Game Flow:
1. At-risk players shown rules and point entry form
2. Players enter amount (0-1000) and submit
3. 30-second timer for submissions
4. Resolution based on who grabbed points
5. Points added to scores, eliminations applied
"""

from typing import List, Dict, Any
from .base_mini_game import BaseMiniGame, MiniGameResult, MiniGamePhase


class GrabMorePointsMiniGame(BaseMiniGame):
    """Grab More Points prisoner's dilemma mini-game."""

    @property
    def name(self) -> str:
        return "Grab More Points"

    @property
    def description(self) -> str:
        return (
            "Grab bonus points (0-1000)! But beware: "
            "If anyone takes points, those who don't become ghosts! "
            "If everyone takes points, everyone becomes a ghost!"
        )

    @property
    def min_players(self) -> int:
        return 2  # Need at least 2 for the dilemma to work

    @property
    def max_eliminates(self) -> int:
        return 999  # Can eliminate all at-risk players

    def setup(
        self,
        at_risk_players: List[int],
        safe_players: List[int],
        total_players: int
    ) -> Dict[str, Any]:
        """
        Set up the Grab More Points game.

        Args:
            at_risk_players: Players who answered incorrectly (the decision makers)
            safe_players: Players who answered correctly (observers)
            total_players: Total living players

        Returns:
            Setup data for frontend
        """
        self.game_state = {
            "at_risk_players": at_risk_players,
            "safe_players": safe_players,
            "player_submissions": {},  # {player_id: points_grabbed}
            "submitted_players": set(),  # Track who has submitted
            "phase": "submission"
        }

        self.phase = MiniGamePhase.SETUP

        return {
            "at_risk_players": at_risk_players,
            "safe_players": safe_players,
            "observers": safe_players,
            "max_points": 1000,
            "time_limit": 30,
            "roles": {
                "decision_maker": {
                    "description": "Decide how many points to grab (0-1000)",
                    "action": "submit_points",
                    "is_at_risk": True
                },
                "observer": {
                    "description": "Watch and wait to see what happens!",
                    "action": "observe"
                }
            },
            "rules": self._get_rules_text()
        }

    def _get_rules_text(self) -> Dict[str, str]:
        """Get the rules text for display."""
        return {
            "title": "⚠️ Grab More Points - Choose Wisely! ⚠️",
            "main_rules": [
                "You can grab 0-1000 bonus points",
                "Points are ALWAYS added to your score",
                "BUT... there's a catch!"
            ],
            "outcomes": [
                "✅ If NO ONE takes points → Everyone survives!",
                "⚠️ If SOME take points → Those who didn't become ghosts!",
                "❌ If ALL take points → Everyone becomes a ghost!"
            ],
            "strategy": "Trust your fellow players... or don't?"
        }

    async def process_player_action(
        self,
        player_id: int,
        action: Dict[str, Any]
    ) -> bool:
        """
        Process a player's point submission.

        Action format:
        {
            "type": "submit_points",
            "points": 0-1000
        }

        Args:
            player_id: ID of player taking action
            action: The action data

        Returns:
            True if action was valid, False otherwise
        """
        if self.game_state["phase"] != "submission":
            return False

        if player_id not in self.game_state["at_risk_players"]:
            return False  # Only at-risk players can submit

        action_type = action.get("type")
        if action_type != "submit_points":
            return False

        # Get points value
        points = action.get("points", 0)

        # Validate points (must be integer between 0-1000)
        try:
            points = int(points)
            if points < 0 or points > 1000:
                return False
        except (ValueError, TypeError):
            return False

        # Record submission
        self.game_state["player_submissions"][player_id] = points
        self.game_state["submitted_players"].add(player_id)

        # Store action for notification
        self.player_actions[player_id] = action

        return True

    def can_resolve(self) -> bool:
        """
        Check if game can be resolved.

        Game resolves when all at-risk players have submitted.

        Returns:
            True if ready to resolve
        """
        at_risk_count = len(self.game_state["at_risk_players"])
        submitted_count = len(self.game_state["submitted_players"])

        return submitted_count >= at_risk_count

    def resolve(self) -> MiniGameResult:
        """
        Resolve the Grab More Points game.

        Determine eliminations based on prisoner's dilemma logic.

        Returns:
            MiniGameResult with elimination data
        """
        at_risk_players = self.game_state["at_risk_players"]
        submissions = self.game_state["player_submissions"]

        # Players who didn't submit get 0 points
        for player_id in at_risk_players:
            if player_id not in submissions:
                submissions[player_id] = 0

        # Count how many grabbed points (> 0)
        grabbers = [p for p, pts in submissions.items() if pts > 0]
        non_grabbers = [p for p, pts in submissions.items() if pts == 0]

        num_grabbers = len(grabbers)
        num_total = len(at_risk_players)

        # Determine eliminations based on rules
        eliminated_players = []
        survivors = []
        elimination_reason = ""

        if num_grabbers == 0:
            # NO ONE took points → Everyone survives!
            eliminated_players = []
            survivors = at_risk_players
            elimination_reason = "No one took points - Everyone survives!"

        elif num_grabbers == num_total:
            # EVERYONE took points → Everyone eliminated!
            eliminated_players = at_risk_players
            survivors = []
            elimination_reason = "Everyone took points - Everyone becomes a ghost!"

        else:
            # SOME took points → Eliminate those who DIDN'T take points
            eliminated_players = non_grabbers
            survivors = grabbers
            elimination_reason = (
                f"{num_grabbers} player(s) took points - "
                f"Those who didn't take points become ghosts!"
            )

        self.phase = MiniGamePhase.RESULTS

        result_data = {
            "submissions": submissions,
            "grabbers": grabbers,
            "non_grabbers": non_grabbers,
            "elimination_reason": elimination_reason,
            "scenario": self._determine_scenario(num_grabbers, num_total),
            "player_details": [
                {
                    "player_id": player_id,
                    "points_grabbed": submissions.get(player_id, 0),
                    "took_points": submissions.get(player_id, 0) > 0,
                    "eliminated": player_id in eliminated_players
                }
                for player_id in at_risk_players
            ]
        }

        return MiniGameResult(
            eliminated_player_ids=eliminated_players,
            survivors=survivors,
            game_data=result_data,
            success=True
        )

    def _determine_scenario(self, num_grabbers: int, num_total: int) -> str:
        """Determine which scenario occurred."""
        if num_grabbers == 0:
            return "no_one_grabbed"
        elif num_grabbers == num_total:
            return "everyone_grabbed"
        else:
            return "some_grabbed"

    def handle_timeout(self) -> MiniGameResult:
        """
        Handle timeout scenario.

        Players who didn't submit are treated as taking 0 points.

        Returns:
            MiniGameResult after handling timeout
        """
        # Mark as complete
        self.game_state["phase"] = "complete"

        # Players who didn't submit get 0 points (auto-filled)
        for player_id in self.game_state["at_risk_players"]:
            if player_id not in self.game_state["player_submissions"]:
                self.game_state["player_submissions"][player_id] = 0

        # Resolve with current submissions
        return self.resolve()

    def get_timeout_seconds(self) -> int:
        """
        Get timeout for Grab More Points game.

        Returns:
            30 seconds for decision making
        """
        return 30

    def get_points_to_award(self) -> Dict[int, int]:
        """
        Get points to award to each player (regardless of elimination).

        Returns:
            Dictionary mapping player_id to points to add to their score
        """
        return self.game_state.get("player_submissions", {})
