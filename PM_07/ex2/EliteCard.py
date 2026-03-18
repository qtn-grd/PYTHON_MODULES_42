from ex0.Card import Card, CardError
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Any, Union, List, Dict


class EliteCard(Card, Combatable, Magical):
    """
    Represents a powerful card combining combat and magical abilities.

    This class demonstrates multiple inheritance by implementing the
    Card base class together with the Combatable and Magical interfaces.
    Elite cards can attack, defend, and cast spells while existing as
    playable cards within the game system.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        mana: int
    ) -> None:
        """
        Initializes an elite card with combat and magic attributes.

        Args:
            name (str): Name of the card.
            cost (int): Mana cost required to play the card.
            rarity (str): Rarity classification of the card.
            attack (int): Attack value used in combat.
            health (int): Health points of the card.
            mana (int): Available mana for casting spells.

        Raises:
            CardError: If any attribute has an invalid value.
        """
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack <= 0:
            raise CardError("Attack must be a positive integer")

        if not isinstance(health, int) or health <= 0:
            raise CardError("Health must be a positive integer")

        if not isinstance(mana, int) or mana < 0:
            raise CardError("Mana must be a non-negative integer")

        self._attack: int = attack
        self.health: int = health
        self.mana: int = mana

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Plays the elite card onto the battlefield.

        Args:
            game_state (Dict[str, Any]): Current state of the game.

        Returns:
            Dict[str, Any]: Result of the play action.
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card summoned to battlefield"
        }

    def attack(self, target: Any) -> Dict[str, Any]:
        """
        Performs an attack against a target.

        Args:
            target (Any): Target of the attack.

        Returns:
            Dict[str, Any]: Result of the attack action.
        """
        target_name = getattr(target, "name", "unknown")
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self._attack,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """
        Reduces health when receiving damage.

        Args:
            incoming_damage (int): Damage received from an attack.

        Returns:
            Dict[str, Any]: Resulting defense state.
        """
        blocked: int = 3
        damage_taken: int = max(0, incoming_damage - blocked)
        self.health -= damage_taken
        still_alive: bool = self.health > 0

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": blocked,
            "still_alive": still_alive
        }

    def get_combat_stats(self) -> Dict[str, int]:
        """
        Returns combat-related statistics.

        Returns:
            Dict[str, int]: Attack and health values.
        """
        return {
            "attack": self._attack,
            "health": self.health
        }

    def cast_spell(
        self,
        spell_name: str,
        targets: List[Any]
    ) -> Dict[str, Any]:
        """
        Casts a spell using the card's mana.

        Args:
            spell_name (str): Name of the spell being cast.
            targets (List[Any]): List of spell targets.

        Raises:
            CardError: If the card has insufficient mana.

        Returns:
            Dict[str, Any]: Result of the spell cast.
        """
        mana_cost: int = len(targets) * 2
        if self.mana < mana_cost:
            raise CardError("Not enough mana to cast spell")
        self.mana -= mana_cost

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": [getattr(t, "name", t) for t in targets],
            "mana_used": mana_cost
        }

    def channel_mana(self, amount: int) -> Dict[str, Union[int, str]]:
        """
        Adds mana to the card.

        Args:
            amount (int): Amount of mana to channel.

        Raises:
            CardError: If the amount is negative.

        Returns:
            Dict[str, Union[int, str]]: Updated mana information.
        """
        if amount < 0:
            raise CardError("Mana amount must be positive")

        self.mana += amount

        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> Dict[str, int]:
        """
        Returns magic-related statistics.

        Returns:
            Dict[str, int]: Current mana value.
        """
        return {
            "mana": self.mana
        }
