from abc import ABC, abstractmethod
from typing import Any, Union, Optional
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class CardFactory(ABC):
    """
    Abstract factory interface for creating different types of cards.

    Concrete factories must implement methods to create creatures,
    spells, artifacts, and themed decks.
    """

    @abstractmethod
    def create_creature(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> CreatureCard:

        """
        Creates a creature card.

        Args:
            name_or_power (str | int | None):
            Optional parameter to customize the card.

        Returns:
            Card: A creature card instance.
        """
        pass

    @abstractmethod
    def create_spell(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Card:

        """
        Creates a spell card.

        Args:
            name_or_power (str | int | None):
            Optional parameter to customize the card.

        Returns:
            Card: A spell card instance.
        """
        pass

    @abstractmethod
    def create_artifact(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Card:

        """
        Creates an artifact card.

        Args:
            name_or_power (str | int | None):
            Optional parameter to customize the card.

        Returns:
            Card: An artifact card instance.
        """
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict[str, Any]:
        """
        Creates a themed deck of cards.

        Args:
            size (int): Number of cards in the deck.

        Returns:
            dict[str, Any]: Representation of the created deck.
        """
        pass

    @abstractmethod
    def get_supported_types(self) -> dict[str, Any]:
        """
        Returns the types of cards supported by the factory.

        Returns:
            dict[str, Any]: Supported card categories and examples.
        """
        pass
