from ex0.Card import Card, CardError
from typing import Union


class CreatureCard(Card):
    """
    Concrete implementation of a Creature card.

    Attributes:
        attack (int): Attack value of the creature.
        health (int): Health points of the creature.
    """

    def __init__(
            self, name: str, cost: int, rarity: str, attack: int, health: int
            ) -> None:
        """
        Initialize a CreatureCard with specific attributes.

        Args:
            name (str): Name of the creature.
            cost (int): Mana cost to play the creature.
            rarity (str): Rarity of the creature.
            attack (int): Attack points of the creature.
            health (int): Health points of the creature.

        Raises:
            ValueError: If attack or health are not positive integers.
        """

        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack <= 0:
            raise CardError("Attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise CardError("Health must be a positive integer")

        self._attack: int = attack
        self._health: int = health

    def get_card_info(self) -> dict[str, Union[str, int]]:
        """
        Return full information for the creature card,
        including type, attack, and health.

        Returns:
            dict[str, Union[str, int]: Dictionary containing card info.
        """

        info = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self._attack
        info["health"] = self._health

        return info

    def play(self, game_state: dict) -> dict:
        """
        Simulate playing the creature card.

        Args:
            game_state (dict): Current state of the game
            (not modified in this exercise).

        Returns:
            dict: Information about the play action.
        """

        return {
            "card_played": self._name,
            "mana_used": self._cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: "CreatureCard") -> dict:
        """
        Simulate attacking another creature.

        Args:
            target (CreatureCard): Target creature to attack.

        Returns:
            dict: Information about the combat action.
        """

        return {
            "attacker": self._name,
            "target": target._name,
            "damage_dealt": self._attack,
            "combat_resolved": True
        }
