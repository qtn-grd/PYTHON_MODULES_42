from abc import ABC, abstractmethod
from typing import Dict


class Rankable(ABC):
    """
    Interface for ranking and tournament statistics.
    """

    @abstractmethod
    def calculate_rating(self) -> int:
        """
        Calculates and returns the current rating.
        """
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """
        Updates the number of wins.
        """
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """
        Updates the number of losses.
        """
        pass

    @abstractmethod
    def get_rank_info(self) -> Dict[str, int]:
        """
        Returns ranking information.
        """
        pass
