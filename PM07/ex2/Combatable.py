from abc import ABC, abstractmethod
from typing import Any


class Combatable(ABC):
    """
    Abstract interface defining combat capabilities for cards.

    Classes implementing this interface must provide methods
    for attacking, defending, and retrieving combat statistics.
    """

    @abstractmethod
    def attack(self, target: Any) -> dict:
        """
        Performs an attack against a target.

        Args:
            target: The entity being attacked.

        Returns:
            dict: Result of the attack action.
        """
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """
        Handles incoming damage from an attack.

        Args:
            incoming_damage (int): Amount of damage received.

        Returns:
            dict: Result of the defense action.
        """
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """
        Returns combat-related statistics for the entity.

        Returns:
            dict: Combat statistics such as attack or health.
        """
        pass
