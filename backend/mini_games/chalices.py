"""
Chalices Mini-Game

Players who answered correctly (and are NOT ghosts) are "Poisoners" - they choose which chalices to poison.
Players who answered incorrectly are "Testers" - they choose which chalice to drink.
If a Tester drinks from a poisoned chalice, they are eliminated.
If they drink from a safe chalice, they survive.

Rules:
- Number of chalices = max(number of players, 3)
- Only SAFE (non-ghost) players can poison chalices
- Each Tester independently chooses which chalice to drink
- Testers are eliminated if they drink poison
- Choices are locked on click (no submit button needed)
- Game resolves when all players have made their choice
"""

from typing import List, Dict, Any, Set
import random
from .base_mini_game import BaseMiniGame, MiniGameResult, MiniGamePhase


class ChalicesMiniGame(BaseMiniGame):
    """Chalices poisoning mini-game."""

    @property
    def name(self) -> str:
        return "Chalices"

    @property
    def description(self) -> str:
        return ("Safe players poison chalices. At-risk players drink. "
                "Drink from a poisoned chalice and you're eliminated!")

    @property
    def min_players(self) -> int:
        return 1  # Can work with just 1 tester

    @property
    def max_eliminates(self) -> int:
        return -1  # Can eliminate all testers if they all drink poison

    def setup(
        self,
        at_risk_players: List[int],
        safe_players: List[int],
        total_players: int
    ) -> Dict[str, Any]:
        """
        Set up the Chalices game.

        Args:
            at_risk_players: Testers (answered wrong) - must choose chalice to drink
            safe_players: Poisoners (answered correctly, non-ghost) - can poison chalices
            total_players: Total living players

        Returns:
            Setup data for frontend
        """
        # Determine number of chalices (minimum 3)
        num_chalices = max(total_players, 3)

        self.game_state = {
            "at_risk_players": at_risk_players,  # Testers (must drink)
            "safe_players": safe_players,  # Poisoners (only non-ghosts can poison)
            "num_chalices": num_chalices,
            "poisoned_chalices": set(),  # Will be set by poisoners
            "tester_choices": {},  # tester_id -> chalice_number (locked on click)
            "poisoner_choices": {}  # poisoner_id -> chalice_number (single selection, locked on click)
        }

        self.phase = MiniGamePhase.SETUP

        return {
            "num_chalices": num_chalices,
            "testers": at_risk_players,
            "poisoners": safe_players,
            "at_risk_players": at_risk_players,
            "safe_players": safe_players,
            "roles": {
                "at_risk": {
                    "description": "You're at risk! Click a chalice to drink from it. Choose wisely!",
                    "action": "choose_chalice"
                },
                "safe": {
                    "description": "You're safe! Click a chalice to poison it.",
                    "action": "poison_chalice"
                },
                "ghost": {
                    "description": "You're a ghost. Watch the game unfold!",
                    "action": "observe"
                }
            }
        }

    async def process_player_action(
        self,
        player_id: int,
        action: Dict[str, Any]
    ) -> bool:
        """
        Process a player's action (choosing chalice to drink or poison).
        Choices are LOCKED on click - no changing once submitted.

        Action format for Testers (at-risk):
        {
            "type": "choose_chalice",
            "chalice": 1  # Chalice number (0-indexed)
        }

        Action format for Poisoners (safe, non-ghost):
        {
            "type": "poison_chalice",
            "chalice": 1  # Single chalice number to poison (0-indexed)
        }

        Args:
            player_id: ID of player taking action
            action: The action data

        Returns:
            True if action was valid, False otherwise
        """
        action_type = action.get("type")

        # Tester choosing a chalice to drink
        if action_type == "choose_chalice":
            if player_id not in self.game_state["at_risk_players"]:
                return False  # Not a tester

            # Check if already made a choice (locked)
            if player_id in self.game_state["tester_choices"]:
                return False  # Already locked in

            chalice = action.get("chalice")
            print(f"[CHALICES DEBUG] Tester {player_id} choosing chalice: {chalice} (type: {type(chalice)})")
            if not isinstance(chalice, int) or chalice < 0 or chalice >= self.game_state["num_chalices"]:
                print(f"[CHALICES DEBUG] Invalid chalice number: {chalice}")
                return False  # Invalid chalice number

            # Lock in the choice
            self.game_state["tester_choices"][player_id] = chalice
            self.player_actions[player_id] = action
            print(f"[CHALICES DEBUG] Tester {player_id} locked in chalice {chalice}")
            return True

        # Poisoner choosing which chalice to poison (single selection)
        elif action_type == "poison_chalice":
            if player_id not in self.game_state["safe_players"]:
                return False  # Not a poisoner (or is a ghost)

            # Check if already made a choice (locked)
            if player_id in self.game_state["poisoner_choices"]:
                return False  # Already locked in

            chalice = action.get("chalice")
            print(f"[CHALICES DEBUG] Poisoner {player_id} choosing chalice: {chalice} (type: {type(chalice)})")
            if not isinstance(chalice, int) or chalice < 0 or chalice >= self.game_state["num_chalices"]:
                print(f"[CHALICES DEBUG] Invalid chalice number: {chalice}")
                return False  # Invalid chalice number

            # Lock in the poisoner's choice
            self.game_state["poisoner_choices"][player_id] = chalice
            self.player_actions[player_id] = action
            print(f"[CHALICES DEBUG] Poisoner {player_id} locked in chalice {chalice}")
            return True

        return False

    def can_resolve(self) -> bool:
        """
        Check if all players have made their choice.
        Game resolves when ALL testers AND ALL poisoners have clicked.

        Returns:
            True if all players have locked in their choice
        """
        testers = self.game_state["at_risk_players"]
        poisoners = self.game_state["safe_players"]

        print(f"[CHALICES DEBUG] ===== CAN_RESOLVE CHECK =====")
        print(f"[CHALICES DEBUG] Testers (at-risk): {testers}")
        print(f"[CHALICES DEBUG] Poisoners (safe): {poisoners}")
        print(f"[CHALICES DEBUG] Tester choices made: {self.game_state['tester_choices']}")
        print(f"[CHALICES DEBUG] Poisoner choices made: {self.game_state['poisoner_choices']}")

        # All testers must have chosen a chalice to drink
        testers_acted = all(t in self.game_state["tester_choices"] for t in testers)
        print(f"[CHALICES DEBUG] All testers acted: {testers_acted} ({len(self.game_state['tester_choices'])}/{len(testers)})")

        # All poisoners must have chosen a chalice to poison (or no poisoners exist)
        poisoners_acted = (len(poisoners) == 0 or
                          all(p in self.game_state["poisoner_choices"] for p in poisoners))
        print(f"[CHALICES DEBUG] All poisoners acted: {poisoners_acted} ({len(self.game_state['poisoner_choices'])}/{len(poisoners)})")

        can_resolve = testers_acted and poisoners_acted
        print(f"[CHALICES DEBUG] Can resolve: {can_resolve}")

        return can_resolve

    def resolve(self) -> MiniGameResult:
        """
        Resolve the Chalices game.

        Each poisoner poisons ONE chalice (their choice).
        A chalice is poisoned if ANY poisoner chose it.
        Testers who drank from poisoned chalices are eliminated.

        Returns:
            MiniGameResult with eliminations and game data
        """
        print(f"[CHALICES DEBUG] ===== RESOLVING CHALICES =====")
        # Determine which chalices are poisoned
        # Each poisoner's choice poisons that chalice
        poisoner_choices = self.game_state["poisoner_choices"]
        num_chalices = self.game_state["num_chalices"]

        print(f"[CHALICES DEBUG] Poisoner choices: {poisoner_choices}")
        print(f"[CHALICES DEBUG] Tester choices: {self.game_state['tester_choices']}")

        # All chalices chosen by poisoners are poisoned
        poisoned = set(poisoner_choices.values())
        print(f"[CHALICES DEBUG] Poisoned chalices set: {poisoned}")

        # If no poisoners exist (all players got trivia wrong), randomly poison one chalice
        if len(poisoned) == 0 and len(self.game_state["at_risk_players"]) > 0:
            random_poison = random.randint(0, num_chalices - 1)
            poisoned.add(random_poison)
            print(f"[CHALICES DEBUG] No poisoners - randomly poisoned chalice {random_poison}")

        self.game_state["poisoned_chalices"] = poisoned

        # Determine eliminations
        eliminated = []
        survivors = []
        tester_results = {}  # tester_id -> {chalice, poisoned, eliminated}

        for tester_id, chalice_chosen in self.game_state["tester_choices"].items():
            is_poisoned = chalice_chosen in poisoned
            print(f"[CHALICES DEBUG] Tester {tester_id}: chose chalice {chalice_chosen} (type: {type(chalice_chosen)}), poisoned chalices: {poisoned}, is_poisoned: {is_poisoned}")

            tester_results[tester_id] = {
                "chalice": chalice_chosen,
                "poisoned": is_poisoned,
                "eliminated": is_poisoned
            }

            if is_poisoned:
                eliminated.append(tester_id)
                print(f"[CHALICES DEBUG] Tester {tester_id} ELIMINATED - drank from poisoned chalice {chalice_chosen}")
            else:
                survivors.append(tester_id)
                print(f"[CHALICES DEBUG] Tester {tester_id} SURVIVED - drank from safe chalice {chalice_chosen}")

        self.phase = MiniGamePhase.RESULTS

        return MiniGameResult(
            eliminated_player_ids=eliminated,
            survivors=survivors,
            game_data={
                "num_chalices": num_chalices,
                "poisoned_chalices": list(poisoned),
                "tester_choices": self.game_state["tester_choices"],
                "tester_results": tester_results,
                "poisoner_choices": poisoner_choices,
                "chalice_poison_counts": self._get_poison_counts()
            },
            success=True
        )

    def _get_poison_counts(self) -> Dict[int, int]:
        """Get count of how many poisoners chose each chalice."""
        poison_counts = {}
        for chalice in self.game_state["poisoner_choices"].values():
            poison_counts[chalice] = poison_counts.get(chalice, 0) + 1
        return poison_counts

    def handle_timeout(self) -> MiniGameResult:
        """
        Handle timeout scenario.

        - Testers who didn't choose: randomly assigned a chalice
        - Poisoners who didn't choose: randomly assigned a chalice to poison

        Returns:
            MiniGameResult after handling timeout
        """
        testers = self.game_state["at_risk_players"]
        poisoners = self.game_state["safe_players"]
        num_chalices = self.game_state["num_chalices"]

        # Assign random chalices to testers who didn't choose
        for tester_id in testers:
            if tester_id not in self.game_state["tester_choices"]:
                random_chalice = random.randint(0, num_chalices - 1)
                self.game_state["tester_choices"][tester_id] = random_chalice

        # Assign random chalices to poisoners who didn't choose
        for poisoner_id in poisoners:
            if poisoner_id not in self.game_state["poisoner_choices"]:
                random_chalice = random.randint(0, num_chalices - 1)
                self.game_state["poisoner_choices"][poisoner_id] = random_chalice

        # Now resolve normally
        return self.resolve()

    def get_timeout_seconds(self) -> int:
        """Chalices game gets 30 seconds for players to decide."""
        return 30
