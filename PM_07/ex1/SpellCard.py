from ex0.Card import Card, CardError


class SpellCardError(CardError):
    """Raised when an invalid spell is used."""
    pass


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

        self._effect_type = effect_type

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
            "card_played": self._name,
            "mana_used": self._cost,
            "effect": f"{effect_result['effect_type']}"
            }

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

        return {
            "effect_type": self._effect_type,
            "targets": targets
        }
