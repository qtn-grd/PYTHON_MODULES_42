from ex0.Card import Card, CardError
from typing import Union


class SpellCard(Card):
    """
    Represents an instant-use spell card with a specific effect type.

    Attributes:
        name (str): Name of the card.
        cost (int): Mana cost to play the card.
        rarity (str): Rarity level of the card.
        effect_type (str): Type of spell effect, one of
        "damage", "heal", "buff", "debuff".
    """

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        """
        Initializes a SpellCard instance.

        Args:
            name (str): Name of the spell.
            cost (int): Mana cost to play the spell.
            rarity (str): Rarity of the spell.
            effect_type (str): Type of spell effect.
        """
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def resolve_effect(self, targets: list) -> dict:
        """
        Resolves the effect of the spell on the given targets.

        Args:
            targets (list): List of targets affected by the spell.

        Returns:
            dict: Dictionary describing the effect applied.

        Raises:
            ValueError: If the effect_type is unknown.
        """
        if self.effect_type == "damage":
            result: dict[str, Union[str, int]] = {
                "effect_type": "damage",
                "targets": targets,
                "damage_done": 2
            }
            return result
        elif self.effect_type == "heal":
            result: dict[str, Union[str, int]] = {
                "effect_type": "heal",
                "targets": targets,
                "healing_done": 2
            }
            return result
        elif self.effect_type == "buff":
            result: dict[str, Union[str, int]] = {
                "effect_type": "buff",
                "targets": targets,
                "buff_applied": "+2 attack"
            }
            return result
        elif self.effect_type == "debuff":
            result: dict[str, Union[str, int]] = {
                "effect_type": "debuff",
                "targets": targets,
                "debuff_applied": "-2 attack"
            }
            return result
        else:
            raise CardError(f"Unknown effect_type: {self.effect_type}")

    def play(self, game_state: dict) -> dict:
        """
        Plays the spell, resolves its effect, and returns the action
        description.

        Args:
            game_state (dict): The current state of the game.

        Returns:
            dict: Dictionary describing the action of playing the card.
        """
        effect_result = self.resolve_effect(targets=[])
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_result
        }
