from abc import ABC, abstractmethod
from typing import Any


class GameStrategy(ABC):
    """
    Abstract base class defining the interface for all game strategies.

    A strategy determines how a turn is executed, including which cards
    are played and how targets are selected.
    """

    @abstractmethod
    def execute_turn(
        self, hand: list[Any], battlefield: list[Any]) -> dict[
            str, Any]:

        """
        Executes a game turn based on the current hand and battlefield.

        Args:
            hand (list[Any]): Cards available to play.
            battlefield (list[Any]): Cards already in play.

        Returns:
            dict[str, Any]: Summary of actions taken during the turn.
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """
        Returns the name of the strategy.

        Returns:
            str: Strategy name.
        """
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        """
        Determines the order of target priority.

        Args:
            available_targets (list[Any]): Possible targets.

        Returns:
            list[Any]: Ordered targets based on priority.
        """
        pass
