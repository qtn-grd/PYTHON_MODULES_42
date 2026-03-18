from abc import ABC, abstractmethod
from typing import Union
from enum import Enum


class CardError(Exception):
    """Raised when an invalid card is created or used."""
    pass


class Rarity(Enum):
    """
    Represents card rarity levels.
    """
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    """
    Abstract base class representing a generic card in DataDeck.

    Attributes:
        name (str): The name of the card.
        cost (int): The mana cost to play the card.
        rarity (str): The rarity of the card (Common, Rare, Epic, Legendary).
    """

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """
        Initialize a Card with name, cost, and rarity.

        Args:
            name (str): Name of the card.
            cost (int): Mana cost to play the card.
            rarity (str): Rarity of the card.
        """

        self.name: str = name
        if not isinstance(cost, int) or cost < 0:
            raise CardError(f"Invalid cost for card {name}: {cost}")

        self.cost: int = cost

        try:
            rarity_enum = Rarity(rarity)
        except ValueError:
            raise CardError("Invalid rarity value")

        self.rarity: str = rarity_enum

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """
        Abstract method to play the card.

        Args:
            game_state (dict): Current state of the game.

        Returns:
            dict: Information about the action performed.
        """
        pass

    def get_card_info(self) -> dict[str, Union[str, int]]:
        """
        Returns basic information about the card.

        Returns:
            dict[str, str | int]: Dictionary containing 'name', 'cost',
            and 'rarity'.
        """

        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """
        Check if the card can be played with the given mana.

        Args:
            available_mana (int): Mana currently available to the player.

        Returns:
            bool: True if available_mana >= cost, False otherwise.
        """

        return available_mana >= self.cost
