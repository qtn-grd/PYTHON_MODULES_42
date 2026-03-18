from abc import ABC, abstractmethod
from typing import Any


class Magical(ABC):
    """
    Abstract interface defining magical abilities for cards.

    Classes implementing this interface must provide methods
    for casting spells, channeling mana, and retrieving
    magic-related statistics.
    """

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list[Any]) -> dict:
        """
        Casts a spell affecting one or more targets.

        Args:
            spell_name (str): Name of the spell being cast.
            targets (list[Any]): Entities affected by the spell.

        Returns:
            dict: Result of the spell casting.
        """
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """
        Channels mana to increase magical power.

        Args:
            amount (int): Amount of mana to channel.

        Returns:
            dict: Result of the mana channeling action.
        """
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """
        Returns magic-related statistics for the entity.

        Returns:
            dict: Magical statistics such as mana or spell power.
        """
        pass
