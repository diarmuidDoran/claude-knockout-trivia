"""
Base class for all mini-games in Knockout Trivia.

Mini-games are elimination games played between trivia questions.
Players who answered the previous question incorrectly are at risk of elimination.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Set
from dataclasses import dataclass
from enum import Enum


class MiniGamePhase(Enum):
    """Phases of mini-game execution."""
    INTRODUCTION = "introduction"  # Show rules/setup
    SETUP = "setup"  # Initialize game state
    PLAYER_ACTION = "player_action"  # Players make choices
    RESOLUTION = "resolution"  # Determine outcomes
    RESULTS = "results"  # Show who was eliminated
    COMPLETE = "complete"  # Mini-game finished


@dataclass
class MiniGameResult:
    """Result of a mini-game execution."""
    eliminated_player_ids: List[int]  # Players eliminated in this mini-game
    survivors: List[int]  # Players who survived
    game_data: Dict[str, Any]  # Game-specific data for frontend display
    success: bool = True
    error_message: str = None


class BaseMiniGame(ABC):
    """
    Abstract base class for mini-games.

    All mini-games must:
    1. Accept a list of players who got the last question wrong (at-risk players)
    2. Accept a list of players who got the last question right (safe players)
    3. Determine which at-risk players are eliminated
    4. Return results including eliminated players and game state
    """

    def __init__(self, room_code: str):
        """
        Initialize mini-game.

        Args:
            room_code: The room code this mini-game is running in
        """
        self.room_code = room_code
        self.phase = MiniGamePhase.INTRODUCTION
        self.game_state: Dict[str, Any] = {}
        self.player_actions: Dict[int, Any] = {}  # player_id -> action

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique name for this mini-game."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Short description of the mini-game rules."""
        pass

    @property
    @abstractmethod
    def min_players(self) -> int:
        """Minimum number of at-risk players required to run this game."""
        pass

    @property
    @abstractmethod
    def max_eliminates(self) -> int:
        """
        Maximum number of players this game can eliminate.
        Return -1 for no limit (can eliminate all at-risk players).
        """
        pass

    @abstractmethod
    def setup(
        self,
        at_risk_players: List[int],
        safe_players: List[int],
        total_players: int
    ) -> Dict[str, Any]:
        """
        Set up the mini-game with players.

        Args:
            at_risk_players: Player IDs who answered incorrectly (potential elimination)
            safe_players: Player IDs who answered correctly (helpers/safe)
            total_players: Total number of living players in the room

        Returns:
            Dict containing setup data to send to frontend
        """
        pass

    @abstractmethod
    async def process_player_action(
        self,
        player_id: int,
        action: Dict[str, Any]
    ) -> bool:
        """
        Process an action from a player.

        Args:
            player_id: ID of player taking action
            action: The action data (game-specific)

        Returns:
            True if action was valid and processed, False otherwise
        """
        pass

    @abstractmethod
    def can_resolve(self) -> bool:
        """
        Check if all required player actions have been received.

        Returns:
            True if ready to resolve, False if waiting for more actions
        """
        pass

    @abstractmethod
    def resolve(self) -> MiniGameResult:
        """
        Resolve the mini-game and determine eliminations.

        Returns:
            MiniGameResult with eliminated players and game data
        """
        pass

    def get_timeout_seconds(self) -> int:
        """
        Get the timeout in seconds for player actions.
        Default is 30 seconds, can be overridden.

        Returns:
            Timeout in seconds
        """
        return 30

    def get_introduction_data(self) -> Dict[str, Any]:
        """
        Get data for the introduction phase.

        Returns:
            Dict with name, description, and any intro-specific data
        """
        return {
            "name": self.name,
            "description": self.description,
            "timeout": self.get_timeout_seconds()
        }

    def handle_timeout(self) -> MiniGameResult:
        """
        Handle case where players don't respond in time.
        Default behavior: eliminate all at-risk players who didn't act.
        Can be overridden for different timeout behavior.

        Returns:
            MiniGameResult with timeout eliminations
        """
        at_risk = self.game_state.get("at_risk_players", [])
        acted_players = set(self.player_actions.keys())

        # Eliminate players who didn't act
        eliminated = [p for p in at_risk if p not in acted_players]
        survivors = [p for p in at_risk if p in acted_players]

        return MiniGameResult(
            eliminated_player_ids=eliminated,
            survivors=survivors,
            game_data={
                "reason": "timeout",
                "message": "Players who didn't act in time were eliminated"
            },
            success=True
        )

    def reset(self):
        """Reset the mini-game state for a new round."""
        self.phase = MiniGamePhase.INTRODUCTION
        self.game_state = {}
        self.player_actions = {}
