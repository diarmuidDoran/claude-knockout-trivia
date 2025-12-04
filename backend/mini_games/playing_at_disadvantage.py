"""
Playing at a Disadvantage Mini-Game

A penalty game where players choose which answer position they will be unable to select
for the remainder of the trivia game.

Rules:
- At-risk players must choose a number between 1-4
- This corresponds to an answer position (1st, 2nd, 3rd, or 4th answer)
- For all remaining trivia questions, that answer position is disabled for them
- The disabled answer will be greyed out and unclickable
- NO players are eliminated in this mini-game
- This is a permanent disadvantage for the rest of the game

Game Flow:
1. At-risk players shown the rules
2. Players have 30 seconds to select a number (1-4)
3. If no selection, random position is chosen
4. Results show which position each player disabled
5. Disadvantage persists for all future questions
6. No eliminations occur

Strategic Considerations:
- Avoid disabling position 1 or 2 (commonly correct answers)
- Balance risk vs. survival strategy
- No way to undo the choice
"""

from typing import List, Dict, Any
import random
from .base_mini_game import BaseMiniGame, MiniGameResult, MiniGamePhase


class PlayingAtDisadvantageMiniGame(BaseMiniGame):
    """Playing at a Disadvantage penalty mini-game."""

    @property
    def name(self) -> str:
        return "Playing at a Disadvantage"

    @property
    def description(self) -> str:
        return (
            "Choose which answer position (1-4) you'll be unable to select "
            "for the rest of the game. Strategic penalty - no eliminations!"
        )

    @property
    def min_players(self) -> int:
        return 1  # Need at least 1 at-risk player

    @property
    def max_eliminates(self) -> int:
        return 0  # NO eliminations in this game!

    def setup(
        self,
        at_risk_players: List[int],
        safe_players: List[int],
        total_players: int
    ) -> Dict[str, Any]:
        """
        Set up the Playing at a Disadvantage game.

        Args:
            at_risk_players: Players who must make a choice
            safe_players: Players who are safe (observe)
            total_players: Total living players

        Returns:
            Setup data for frontend
        """
        self.game_state = {
            "at_risk_players": at_risk_players,
            "safe_players": safe_players,
            "player_selections": {},  # {player_id: disabled_position (1-4)}
            "submitted_players": set(),
        }

        self.phase = MiniGamePhase.SETUP

        return {
            "at_risk_players": at_risk_players,
            "safe_players": safe_players,
            "players_competing": at_risk_players,
            "observers": safe_players,
            "selection_time": 30,  # seconds
            "answer_positions": [1, 2, 3, 4],
            "roles": {
                "at_risk": {
                    "description": "Choose an answer position to disable for the rest of the game!",
                    "action": "select_position",
                    "is_at_risk": True
                },
                "observer": {
                    "description": "Watch others make their strategic choice!",
                    "action": "observe"
                }
            },
            "rules": self._get_rules_description(len(at_risk_players))
        }

    def _get_rules_description(self, at_risk_count: int) -> Dict[str, Any]:
        """Get rules description."""
        return {
            "title": "⚠️ Playing at a Disadvantage",
            "main_rules": [
                "Choose a number from 1 to 4",
                "This answer position will be DISABLED for the rest of the game",
                "You won't be able to select that answer position in future questions",
                "Even if you know it's correct, you can't click it!",
                "NO ONE gets eliminated in this mini-game"
            ],
            "consequence": f"⚠️ This disadvantage is PERMANENT for all remaining questions!"
        }

    async def process_player_action(
        self,
        player_id: int,
        action: Dict[str, Any]
    ) -> bool:
        """
        Process a player's position selection.

        Action format:
        {
            "type": "select_position",
            "position": 1-4
        }

        Args:
            player_id: ID of player taking action
            action: The action data

        Returns:
            True if action was valid, False otherwise
        """
        if player_id not in self.game_state["at_risk_players"]:
            return False  # Only at-risk players can select

        action_type = action.get("type")
        if action_type != "select_position":
            return False

        # Get selected position
        position = action.get("position")
        if not self._validate_position(position):
            return False

        # Record selection
        self.game_state["player_selections"][player_id] = position
        self.game_state["submitted_players"].add(player_id)

        # Store action for notification
        self.player_actions[player_id] = action

        return True

    def _validate_position(self, position: Any) -> bool:
        """Validate that position is 1, 2, 3, or 4."""
        if not isinstance(position, int):
            return False

        return position in [1, 2, 3, 4]

    def can_resolve(self) -> bool:
        """
        Check if game can be resolved.

        Game resolves when all at-risk players have selected.

        Returns:
            True if ready to resolve
        """
        at_risk_count = len(self.game_state["at_risk_players"])
        submitted_count = len(self.game_state["submitted_players"])

        return submitted_count >= at_risk_count

    def resolve(self) -> MiniGameResult:
        """
        Resolve the Playing at a Disadvantage game.

        Assign disabled positions and return results with NO eliminations.

        Returns:
            MiniGameResult with disadvantage data (no eliminations)
        """
        at_risk_players = self.game_state["at_risk_players"]
        selections = self.game_state["player_selections"]

        # Players who didn't select get random position
        for player_id in at_risk_players:
            if player_id not in selections:
                selections[player_id] = random.randint(1, 4)

        # Calculate distribution of disabled positions
        position_counts = {1: 0, 2: 0, 3: 0, 4: 0}
        for position in selections.values():
            position_counts[position] += 1

        self.phase = MiniGamePhase.RESULTS

        result_data = {
            "disabled_positions": selections,  # {player_id: disabled_position}
            "position_distribution": position_counts,  # {position: count}
            "summary": [
                {
                    "player_id": player_id,
                    "disabled_position": position,
                    "description": f"Position {position} disabled"
                }
                for player_id, position in selections.items()
            ]
        }

        # NO eliminations - everyone survives with a disadvantage
        return MiniGameResult(
            eliminated_player_ids=[],  # No one eliminated!
            survivors=at_risk_players,  # All at-risk players survive
            game_data=result_data,
            success=True
        )

    def handle_timeout(self) -> MiniGameResult:
        """
        Handle timeout scenario.

        Players who didn't select get random position assigned.

        Returns:
            MiniGameResult after handling timeout
        """
        # Players who didn't submit get random selection
        for player_id in self.game_state["at_risk_players"]:
            if player_id not in self.game_state["player_selections"]:
                self.game_state["player_selections"][player_id] = random.randint(1, 4)

        # Resolve with current/random selections
        return self.resolve()

    def get_timeout_seconds(self) -> int:
        """
        Get timeout for Playing at a Disadvantage game.

        Returns:
            30 seconds for selection
        """
        return 30
