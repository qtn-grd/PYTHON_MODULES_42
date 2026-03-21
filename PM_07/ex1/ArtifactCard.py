from ex0.Card import Card, CardError


class ArtifactCard(Card):
    """
    Represents a permanent artifact card with durability
    and a persistent effect.

    Attributes:
        name (str): Name of the artifact.
        cost (int): Mana cost to play the artifact.
        rarity (str): Rarity level of the artifact.
        durability (int): Number of turns the artifact can remain active.
        effect (str): Description of the artifact's permanent ability.
    """

    def __init__(self, name: str, cost: int,
                 rarity: str, durability: int, effect: str):
        """
        Initializes an ArtifactCard instance.

        Args:
            name (str): Name of the artifact.
            cost (int): Mana cost to play the artifact.
            rarity (str): Rarity of the artifact.
            durability (int): Number of turns the artifact remains active.
            effect (str): Description of the permanent effect.

        Raises:
            ValueError: If durability is not a positive integer.
        """

        super().__init__(name, cost, rarity)

        if not isinstance(durability, int) or durability <= 0:
            raise CardError("Durability must be a positive integer")

        self._durability = durability

        self._effect = effect

    def play(self, game_state: dict) -> dict:
        """
        Plays the artifact, returning a dictionary describing the action.

        Args:
            game_state (dict): The current state of the game.

        Returns:
            dict: Description of the card played and its effect.
        """

        return {
            "card_played": self._name,
            "mana_used": self._cost,
            "effect": f"Permanent: {self._effect}"
        }

    def activate_ability(self) -> dict:
        """
        Activates the artifact's durable ability.

        Returns:
            dict: Description of the artifact effect
            and its remaining durability.
        """

        return {
            "artifact": self._name,
            "effect_active": self._effect,
            "durability_remaining": self._durability
        }
