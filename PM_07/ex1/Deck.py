from ex0.Card import Card
import random
from typing import Dict


class DeckError(Exception):
    """Raised when an invalid operation is performed on a deck."""
    pass


class Deck:
    """
    Represents a deck of cards that can hold any type of Card.

    Attributes:
        cards (list[Card]): List of cards in the deck.
    """

    def __init__(self):
        """
        Initializes an empty deck.
        """

        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        """
        Adds a card to the deck.

        Args:
            card (Card): Card to add.
        """

        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """
        Removes the first card with the given name from the deck.

        Args:
            card_name (str): Name of the card to remove.

        Returns:
            bool: True if a card was removed, False otherwise.
        """

        for element, card in enumerate(self.cards):
            if card._name == card_name:
                self.cards.pop(element)
                return True
        return False

    def shuffle(self) -> None:
        """
        Shuffles the deck in place.
        """

        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """
        Draws the top card from the deck.

        Returns:
            Card: The card drawn.

        Raises:
            DeckError: If the deck is empty.
        """

        if not self.cards:
            raise DeckError("Cannot draw from an empty deck")

        return self.cards.pop()

    def get_deck_stats(self) -> Dict[str, float]:
        """
        Returns statistics about the deck.

        Returns:
            dict: Dictionary containing:
                - total_cards (int): Total number of cards in the deck.
                - creatures (int): Number of CreatureCard instances.
                - spells (int): Number of SpellCard instances.
                - artifacts (int): Number of ArtifactCard instances.
                - avg_cost (float): Average mana cost of cards (1 decimal).
        """

        total_cards: int = len(self.cards)

        total_creatures: int = sum(1 for creature in self.cards if
                                   type(creature).__name__ == "CreatureCard")
        total_spells: int = sum(1 for spell in self.cards if
                                type(spell).__name__ == "SpellCard")
        total_artifacts: int = sum(1 for artifact in self.cards if
                                   type(artifact).__name__ == "ArtifactCard")
        avg_cost: float = 0

        if total_cards:
            avg_cost = round(
                sum(card._cost for card in self.cards) / total_cards, 1)

        return {
            "total_cards": total_cards,
            "creatures": total_creatures,
            "spells": total_spells,
            "artifacts": total_artifacts,
            "avg_cost": avg_cost
        }
