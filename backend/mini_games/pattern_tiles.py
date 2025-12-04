"""
Pattern Tiles Mini-Game

A memory game where players must memorize and recreate a pattern of blue and white tiles.

Rules:
- 4x4 grid of blue and white tiles shown on TV screen for 10 seconds
- Pattern is then hidden and players get their own blank (all white) grids
- Players have 30 seconds to click tiles to match the pattern
- Click white tile → turns blue
- Click blue tile → turns white
- Players can submit early or wait for timer
- Grids compared to original pattern, accuracy calculated as percentage

Elimination Rules:
- Multiple at-risk players: Only they compete, lowest accuracy eliminated
- Single at-risk vs all others: At-risk eliminated if anyone scores higher
- Ties: Random selection among tied players

Game Flow:
1. Generate random 4x4 pattern
2. Show pattern to all players for 10 seconds (memorization phase)
3. Hide pattern, activate player grids (30-second recreation phase)
4. Players click tiles to match pattern
5. Submit grids (early or on timeout)
6. Calculate accuracy percentages
7. Determine elimination based on scores
"""

from typing import List, Dict, Any
import random
from .base_mini_game import BaseMiniGame, MiniGameResult, MiniGamePhase


class PatternTilesMiniGame(BaseMiniGame):
    """Pattern Tiles memory mini-game."""

    @property
    def name(self) -> str:
        return "Pattern Tiles"

    @property
    def description(self) -> str:
        return (
            "Memorize the pattern shown for 10 seconds, "
            "then recreate it on your grid! "
            "Lowest accuracy = eliminated!"
        )

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
        Set up the Pattern Tiles game.

        Args:
            at_risk_players: Players who answered incorrectly (must participate)
            safe_players: Players who answered correctly (compete if only 1 at-risk)
            total_players: Total living players

        Returns:
            Setup data for frontend
        """
        # Generate random 4x4 pattern (16 tiles)
        pattern = self._generate_pattern()

        # Determine game mode
        if len(at_risk_players) > 1:
            # Multiple at-risk: only they compete
            game_mode = "at_risk_vs_at_risk"
            players_competing = at_risk_players
            observers = safe_players
        else:
            # Single at-risk: competes against everyone
            game_mode = "at_risk_vs_all"
            players_competing = at_risk_players + safe_players
            observers = []

        self.game_state = {
            "pattern": pattern,
            "at_risk_players": at_risk_players,
            "safe_players": safe_players,
            "game_mode": game_mode,
            "players_competing": players_competing,
            "observers": observers,
            "player_submissions": {},  # {player_id: submitted_grid}
            "submitted_players": set(),
            "phase": "memorization"  # memorization -> recreation -> complete
        }

        self.phase = MiniGamePhase.SETUP

        return {
            "pattern": pattern,
            "at_risk_players": at_risk_players,
            "safe_players": safe_players,
            "game_mode": game_mode,
            "players_competing": players_competing,
            "observers": observers,
            "memorization_time": 10,  # seconds
            "recreation_time": 30,  # seconds
            "grid_size": 4,  # 4x4 grid
            "roles": {
                "competitor": {
                    "description": "Memorize the pattern and recreate it!",
                    "action": "submit_grid",
                    "is_at_risk": "varies"
                },
                "observer": {
                    "description": "Watch the memory challenge!",
                    "action": "observe"
                }
            },
            "rules": self._get_rules_description(game_mode, len(at_risk_players))
        }

    def _generate_pattern(self) -> List[List[int]]:
        """
        Generate a random 4x4 pattern of tiles.

        Returns:
            4x4 grid where 1 = blue, 0 = white
        """
        # Generate random pattern (roughly 50/50 blue/white for balance)
        pattern = []
        for _ in range(4):
            row = [random.randint(0, 1) for _ in range(4)]
            pattern.append(row)

        return pattern

    def _get_rules_description(self, game_mode: str, at_risk_count: int) -> Dict[str, Any]:
        """Get rules description based on game mode."""
        if game_mode == "at_risk_vs_at_risk":
            return {
                "title": "🧩 Pattern Tiles",
                "phases": [
                    "Memorize (10s) → Click tiles to match → Submit (30s)"
                ],
                "gameplay": [
                    "Lowest accuracy eliminated!"
                ],
                "elimination": ""
            }
        else:
            return {
                "title": "🧩 Pattern Tiles",
                "phases": [
                    "Memorize (10s) → Click tiles to match → Submit (30s)"
                ],
                "gameplay": [
                    "At-risk must beat everyone!"
                ],
                "elimination": ""
            }

    async def process_player_action(
        self,
        player_id: int,
        action: Dict[str, Any]
    ) -> bool:
        """
        Process a player's action.

        Action formats:
        Start recreation phase:
        {
            "type": "start_recreation"
        }

        Submit grid:
        {
            "type": "submit_grid",
            "grid": [[0,1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1,0]]
        }

        Args:
            player_id: ID of player taking action
            action: The action data

        Returns:
            True if action was valid, False otherwise
        """
        action_type = action.get("type")

        # Handle phase transition from memorization to recreation
        if action_type == "start_recreation":
            if self.game_state["phase"] == "memorization":
                self.game_state["phase"] = "recreation"
                print(f"[PATTERN-TILES DEBUG] Phase transitioned to recreation by player {player_id}")
                return True
            return False

        # Handle grid submission
        if action_type == "submit_grid":
            if self.game_state["phase"] != "recreation":
                print(f"[PATTERN-TILES DEBUG] Rejected submission from player {player_id} - phase is {self.game_state['phase']}")
                return False

            if player_id not in self.game_state["players_competing"]:
                return False  # Only competing players can submit

            # Get submitted grid
            grid = action.get("grid")
            if not self._validate_grid(grid):
                return False

            # Record submission
            self.game_state["player_submissions"][player_id] = grid
            self.game_state["submitted_players"].add(player_id)

            # Store action for notification
            self.player_actions[player_id] = action

            print(f"[PATTERN-TILES DEBUG] Player {player_id} submitted grid: {grid}")
            return True

        return False

    def _validate_grid(self, grid: Any) -> bool:
        """Validate that grid is a proper 4x4 grid of 0s and 1s."""
        if not isinstance(grid, list):
            return False

        if len(grid) != 4:
            return False

        for row in grid:
            if not isinstance(row, list):
                return False
            if len(row) != 4:
                return False
            for cell in row:
                if cell not in [0, 1]:
                    return False

        return True

    def can_resolve(self) -> bool:
        """
        Check if game can be resolved.

        Game resolves when all competing players have submitted.

        Returns:
            True if ready to resolve
        """
        competing_count = len(self.game_state["players_competing"])
        submitted_count = len(self.game_state["submitted_players"])

        return submitted_count >= competing_count

    def resolve(self) -> MiniGameResult:
        """
        Resolve the Pattern Tiles game.

        Calculate accuracy for each player and determine elimination.

        Returns:
            MiniGameResult with elimination data
        """
        pattern = self.game_state["pattern"]
        at_risk_players = self.game_state["at_risk_players"]
        game_mode = self.game_state["game_mode"]
        submissions = self.game_state["player_submissions"]
        players_competing = self.game_state["players_competing"]

        print(f"[PATTERN-TILES DEBUG] Pattern: {pattern}")
        print(f"[PATTERN-TILES DEBUG] At-risk players: {at_risk_players}")
        print(f"[PATTERN-TILES DEBUG] Game mode: {game_mode}")
        print(f"[PATTERN-TILES DEBUG] Players competing: {players_competing}")

        # Players who didn't submit get empty grid (0% accuracy)
        for player_id in players_competing:
            if player_id not in submissions:
                submissions[player_id] = [[0] * 4 for _ in range(4)]
                print(f"[PATTERN-TILES DEBUG] Player {player_id} didn't submit, using default grid")

        # Calculate accuracy for each player
        accuracies = {}
        for player_id, grid in submissions.items():
            accuracy = self._calculate_accuracy(pattern, grid)
            accuracies[player_id] = accuracy
            print(f"[PATTERN-TILES DEBUG] Player {player_id} accuracy: {accuracy:.1f}% - Grid: {grid}")

        # Sort by accuracy (highest first)
        sorted_players = sorted(accuracies.items(), key=lambda x: x[1], reverse=True)
        print(f"[PATTERN-TILES DEBUG] Sorted players (highest first): {sorted_players}")

        # Determine elimination based on game mode
        eliminated_players = []
        survivors = []
        elimination_reason = ""

        if game_mode == "at_risk_vs_at_risk":
            # Multiple at-risk: eliminate lowest scorer
            lowest_accuracy = sorted_players[-1][1]
            highest_accuracy = sorted_players[0][1]
            lowest_scorers = [p for p, acc in sorted_players if acc == lowest_accuracy]

            print(f"[PATTERN-TILES DEBUG] Lowest accuracy: {lowest_accuracy:.1f}%")
            print(f"[PATTERN-TILES DEBUG] Highest accuracy: {highest_accuracy:.1f}%")
            print(f"[PATTERN-TILES DEBUG] Players with lowest accuracy: {lowest_scorers}")

            # If ALL players have the same accuracy, no one is eliminated
            if lowest_accuracy == highest_accuracy:
                eliminated_player = None
                survivors = at_risk_players
                elimination_reason = f"All players tied at {lowest_accuracy:.1f}% - everyone survives!"
                print(f"[PATTERN-TILES DEBUG] ALL PLAYERS TIED - no elimination")
            else:
                # Random selection if tie for lowest
                eliminated_player = random.choice(lowest_scorers)
                survivors = [p for p in at_risk_players if p != eliminated_player]
                elimination_reason = f"Lowest accuracy: {lowest_accuracy:.1f}%"
                print(f"[PATTERN-TILES DEBUG] ELIMINATING player: {eliminated_player}")
                print(f"[PATTERN-TILES DEBUG] Survivors: {survivors}")

        else:
            # Single at-risk vs all: at-risk must not have anyone score higher
            at_risk_player = at_risk_players[0]
            at_risk_accuracy = accuracies.get(at_risk_player, 0.0)

            print(f"[PATTERN-TILES DEBUG] At-risk player: {at_risk_player} with accuracy: {at_risk_accuracy:.1f}%")

            # Check if anyone scored higher
            higher_scorers = [p for p, acc in accuracies.items()
                            if p != at_risk_player and acc > at_risk_accuracy]

            print(f"[PATTERN-TILES DEBUG] Players who scored higher: {higher_scorers}")

            if higher_scorers:
                # At-risk player eliminated
                eliminated_player = at_risk_player
                survivors = []
                highest_accuracy = max(accuracies[p] for p in higher_scorers)
                elimination_reason = (
                    f"At-risk player scored {at_risk_accuracy:.1f}%, "
                    f"but others scored higher ({highest_accuracy:.1f}%)"
                )
                print(f"[PATTERN-TILES DEBUG] ELIMINATING at-risk player: {eliminated_player}")
            else:
                # At-risk player survived
                eliminated_player = None
                survivors = at_risk_players
                elimination_reason = f"At-risk player scored highest: {at_risk_accuracy:.1f}%!"
                print(f"[PATTERN-TILES DEBUG] At-risk player SURVIVES")

        self.phase = MiniGamePhase.RESULTS

        result_data = {
            "accuracies": accuracies,
            "pattern": pattern,
            "game_mode": game_mode,
            "elimination_reason": elimination_reason,
            "sorted_results": [
                {
                    "player_id": player_id,
                    "accuracy": accuracy,
                    "rank": idx + 1
                }
                for idx, (player_id, accuracy) in enumerate(sorted_players)
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

    def _calculate_accuracy(self, pattern: List[List[int]], grid: List[List[int]]) -> float:
        """
        Calculate accuracy percentage between pattern and player's grid.

        Args:
            pattern: The original pattern (4x4)
            grid: Player's submitted grid (4x4)

        Returns:
            Accuracy percentage (0.0 to 100.0)
        """
        correct_tiles = 0
        total_tiles = 16  # 4x4 grid

        for i in range(4):
            for j in range(4):
                if pattern[i][j] == grid[i][j]:
                    correct_tiles += 1

        accuracy = (correct_tiles / total_tiles) * 100.0
        return accuracy

    def handle_timeout(self) -> MiniGameResult:
        """
        Handle timeout scenario.

        Players who didn't submit get empty grid (0% accuracy).

        Returns:
            MiniGameResult after handling timeout
        """
        # Mark as complete
        self.game_state["phase"] = "complete"

        # Players who didn't submit get default grid (all white)
        for player_id in self.game_state["players_competing"]:
            if player_id not in self.game_state["player_submissions"]:
                self.game_state["player_submissions"][player_id] = [[0] * 4 for _ in range(4)]

        # Resolve with current submissions
        return self.resolve()

    def get_timeout_seconds(self) -> int:
        """
        Get timeout for Pattern Tiles game.

        Returns:
            40 seconds total (10s memorization + 30s recreation)
        """
        return 40  # Total time: 10s memorization + 30s recreation
