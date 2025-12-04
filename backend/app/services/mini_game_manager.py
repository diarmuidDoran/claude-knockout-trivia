"""
Mini-Game Manager Service

Handles mini-game lifecycle:
1. Select appropriate mini-game based on player count
2. Set up mini-game with correct players
3. Process player actions
4. Resolve mini-game and determine eliminations
5. Update player statuses (ghost players)
"""

import random
from typing import Dict, List, Any, Optional
from datetime import datetime
from sqlalchemy.orm import Session

from ..models.models import Player
from mini_games import MINI_GAMES, BaseMiniGame, MiniGameResult


class MiniGameManager:
    """Manages mini-game execution and player elimination."""

    def __init__(self):
        """Initialize mini-game manager."""
        self.active_mini_games: Dict[str, BaseMiniGame] = {}  # room_code -> mini_game instance
        self.mini_game_timers: Dict[str, datetime] = {}  # room_code -> start_time

    def select_mini_game(
        self,
        at_risk_count: int,
        safe_count: int,
        available_games: Optional[List[str]] = None
    ) -> Optional[BaseMiniGame]:
        """
        Select an appropriate mini-game based on player counts.

        Args:
            at_risk_count: Number of players who answered incorrectly
            safe_count: Number of players who answered correctly
            available_games: Optional list of game names to choose from
                           If None, all games are considered

        Returns:
            Instantiated mini-game or None if no suitable game found
        """
        if at_risk_count == 0:
            return None  # No one to eliminate

        # Filter games that can handle this player count
        suitable_games = []

        games_to_check = available_games or list(MINI_GAMES.keys())

        for game_name in games_to_check:
            game_class = MINI_GAMES.get(game_name)
            if not game_class:
                continue

            # Create temporary instance to check requirements
            temp_game = game_class("")
            if temp_game.min_players <= at_risk_count:
                suitable_games.append(game_name)

        if not suitable_games:
            return None

        # Randomly select from suitable games
        selected_name = random.choice(suitable_games)
        return MINI_GAMES[selected_name]

    def start_mini_game(
        self,
        room_code: str,
        at_risk_players: List[int],
        safe_players: List[int],
        total_players: int,
        game_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Start a mini-game for a room.

        Args:
            room_code: Room code
            at_risk_players: Player IDs who answered incorrectly
            safe_players: Player IDs who answered correctly
            total_players: Total number of living (non-ghost) players
            game_name: Specific game to use, or None for random selection

        Returns:
            Dict with mini-game setup data for frontend
        """
        # Select mini-game
        if game_name:
            game_class = MINI_GAMES.get(game_name)
            if not game_class:
                raise ValueError(f"Unknown mini-game: {game_name}")
            mini_game = game_class(room_code)
        else:
            game_class = self.select_mini_game(
                len(at_risk_players),
                len(safe_players)
            )
            if not game_class:
                # No suitable mini-game, eliminate all at-risk players by default
                return self._default_elimination(room_code, at_risk_players, safe_players)

            mini_game = game_class(room_code)

        # Set up the mini-game
        setup_data = mini_game.setup(at_risk_players, safe_players, total_players)

        # Store active mini-game
        self.active_mini_games[room_code] = mini_game
        self.mini_game_timers[room_code] = datetime.utcnow()

        return {
            "type": "mini_game_start",
            "game_name": mini_game.name,
            "description": mini_game.description,
            "timeout": mini_game.get_timeout_seconds(),
            "setup": setup_data,
            "introduction": mini_game.get_introduction_data()
        }

    async def process_player_action(
        self,
        room_code: str,
        player_id: int,
        action: Dict[str, Any]
    ) -> bool:
        """
        Process a player's action in the active mini-game.

        Args:
            room_code: Room code
            player_id: Player ID
            action: Action data

        Returns:
            True if action was processed, False if invalid
        """
        mini_game = self.active_mini_games.get(room_code)
        if not mini_game:
            return False

        return await mini_game.process_player_action(player_id, action)

    def can_resolve(self, room_code: str) -> bool:
        """
        Check if mini-game can be resolved (all players have acted).

        Args:
            room_code: Room code

        Returns:
            True if ready to resolve
        """
        mini_game = self.active_mini_games.get(room_code)
        if not mini_game:
            return False

        return mini_game.can_resolve()

    def resolve_mini_game(
        self,
        room_code: str,
        db: Session,
        force: bool = False
    ) -> MiniGameResult:
        """
        Resolve the active mini-game and update player statuses.

        Args:
            room_code: Room code
            db: Database session
            force: If True, force resolution even if not all players acted (timeout)

        Returns:
            MiniGameResult with elimination data
        """
        mini_game = self.active_mini_games.get(room_code)
        if not mini_game:
            return MiniGameResult(
                eliminated_player_ids=[],
                survivors=[],
                game_data={},
                success=False,
                error_message="No active mini-game"
            )

        # Resolve or handle timeout
        if force and not mini_game.can_resolve():
            result = mini_game.handle_timeout()
        else:
            result = mini_game.resolve()

        # Award points if mini-game supports it (e.g., Grab More Points)
        if hasattr(mini_game, 'get_points_to_award'):
            points_to_award = mini_game.get_points_to_award()
            for player_id, points in points_to_award.items():
                if points > 0:
                    player = db.query(Player).filter(Player.id == player_id).first()
                    if player:
                        player.total_score += points
                        print(f"[MINI-GAME] Awarded {points} points to player {player_id}")

        # Update database: mark eliminated players as ghosts
        for player_id in result.eliminated_player_ids:
            player = db.query(Player).filter(Player.id == player_id).first()
            if player:
                player.is_ghost = True
                player.eliminated_at = datetime.utcnow()

        # Handle Playing at a Disadvantage: Update disabled positions
        if result.game_data and 'disabled_positions' in result.game_data:
            disabled_positions = result.game_data['disabled_positions']
            for player_id, position in disabled_positions.items():
                player = db.query(Player).filter(Player.id == player_id).first()
                if player:
                    player.disabled_answer_position = position
                    print(f"[MINI-GAME] Player {player_id} disabled position {position}")

        db.commit()

        # Clean up
        del self.active_mini_games[room_code]
        if room_code in self.mini_game_timers:
            del self.mini_game_timers[room_code]

        return result

    def check_timeout(self, room_code: str) -> bool:
        """
        Check if mini-game has timed out.

        Args:
            room_code: Room code

        Returns:
            True if timed out
        """
        mini_game = self.active_mini_games.get(room_code)
        start_time = self.mini_game_timers.get(room_code)

        if not mini_game or not start_time:
            return False

        elapsed = (datetime.utcnow() - start_time).total_seconds()
        return elapsed >= mini_game.get_timeout_seconds()

    def get_active_mini_game(self, room_code: str) -> Optional[BaseMiniGame]:
        """Get the active mini-game for a room."""
        return self.active_mini_games.get(room_code)

    def _default_elimination(
        self,
        room_code: str,
        at_risk_players: List[int],
        safe_players: List[int]
    ) -> Dict[str, Any]:
        """
        Default elimination when no mini-game is available.
        Simply eliminates all at-risk players.

        Args:
            room_code: Room code
            at_risk_players: Players to eliminate
            safe_players: Players who are safe

        Returns:
            Setup data for default elimination
        """
        return {
            "type": "mini_game_start",
            "game_name": "Instant Elimination",
            "description": "Players who answered incorrectly are eliminated!",
            "timeout": 5,  # Short timeout, just for display
            "setup": {
                "eliminated": at_risk_players,
                "survivors": safe_players
            },
            "introduction": {
                "name": "Instant Elimination",
                "description": "All players who answered incorrectly are eliminated.",
                "timeout": 5
            }
        }

    def cleanup_room(self, room_code: str):
        """Clean up mini-game data for a room."""
        if room_code in self.active_mini_games:
            del self.active_mini_games[room_code]
        if room_code in self.mini_game_timers:
            del self.mini_game_timers[room_code]
