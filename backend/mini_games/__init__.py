"""
Mini-games package for Knockout Trivia.

Mini-games are played between questions to eliminate players who answered incorrectly.
Eliminated players become "ghost players" and continue playing but cannot win.
"""

print("[MINI-GAMES] Loading mini-games with DEBUG logging enabled for Quick Math and Chalices")

from .base_mini_game import BaseMiniGame, MiniGameResult
from .chalices import ChalicesMiniGame
from .worst_answer import WorstAnswerMiniGame
from .quick_math import QuickMathMiniGame
from .grab_more_points import GrabMorePointsMiniGame
from .pattern_tiles import PatternTilesMiniGame
from .playing_at_disadvantage import PlayingAtDisadvantageMiniGame

# Registry of available mini-games
MINI_GAMES = {
    "chalices": ChalicesMiniGame,
    "worst_answer": WorstAnswerMiniGame,
    "quick_math": QuickMathMiniGame,
    "grab_more_points": GrabMorePointsMiniGame,
    "pattern_tiles": PatternTilesMiniGame,
    "playing_at_disadvantage": PlayingAtDisadvantageMiniGame,
}

__all__ = ["BaseMiniGame", "MiniGameResult", "ChalicesMiniGame", "WorstAnswerMiniGame", "QuickMathMiniGame", "GrabMorePointsMiniGame", "PatternTilesMiniGame", "PlayingAtDisadvantageMiniGame", "MINI_GAMES"]
