from typing import Any
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
import random


class EngineError(Exception):
    """Raised when the game engine is used without proper configuration."""
    pass


class GameEngine:
    """
    Core orchestrator for the DataDeck game.

    Handles card creation using a concrete CardFactory and executes game
    turns using a specified GameStrategy. Tracks state including hand,
    battlefield, number of turns simulated,
    total damage dealt, and total cards created.
    """

    def __init__(self) -> None:
        """
        Initializes a new, empty GameEngine instance.

        Attributes:
            factory (CardFactory | None): The card factory used to create
            cards.
            strategy (GameStrategy | None): The strategy for executing turns.
            hand (list[Any]): Current cards in the player's hand.
            battlefield (list[Any]): Cards currently in play on the
            battlefield.
            turns_simulated (int): Number of turns simulated by the engine.
            total_damage (int): Total damage dealt across all turns.
            cards_created (int): Total number of cards created by the factory.
        """

        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None

        self.hand: list[Any] = []
        self.battlefield: list[Any] = []

        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy
    ) -> None:
        """
        Configures the engine with a card factory and a game strategy.

        Resets engine state including hand, battlefield, turn counter,
        total damage, and cards created.

        Args:
            factory (CardFactory): Concrete factory used to create cards.
            strategy (GameStrategy): Strategy used to play turns.
        """

        self.factory = factory
        self.strategy = strategy

        self.hand = []
        self.battlefield = []

        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def simulate_turn(self) -> dict[str, Any]:
        """
        Simulates a single game turn.

        - Generates a hand of 3 cards chosen randomly from creature, spell,
          or artifact types using the configured CardFactory.
        - Executes the turn using the configured GameStrategy.
        - Updates total damage, cards created, and turns simulated.

        Returns:
            dict[str, Any]: Summary of actions taken during the turn,
            as returned by the strategy's `execute_turn` method.

        Raises:
            EngineError: If the engine is not configured with a factory
            and strategy before simulation.
        """

        if self.factory is None or self.strategy is None:
            raise EngineError("Engine not configured")

        self.hand = []

        deck_size: int = 3

        try:
            for _ in range(deck_size):
                card_type: str = random.choice(
                    ["creature", "spell", "artifact"])

                if card_type == "artifact":
                    card = self.factory.create_artifact()
                elif card_type == "spell":
                    card = self.factory.create_spell()
                else:
                    card = self.factory.create_creature()

                self.hand.append(card)
                self.cards_created += 1

            result = self.strategy.execute_turn(self.hand, self.battlefield)
        except Exception as error:
            raise EngineError(f"Failed during turn simulation: {error}")

        self.turns_simulated += 1
        damage: int = result.get("damage_dealt", 0)
        self.total_damage += damage

        return result

    def get_engine_status(self) -> dict[str, Any]:
        """
        Retrieves the current status of the game engine.

        Returns:
            dict[str, Any]: Engine status including:
                - turns_simulated (int): Number of simulated turns.
                - strategy_used (str | None): Name of the strategy in use.
                - total_damage (int): Cumulative damage dealt.
                - cards_created (int): Total number of cards created.
        """

        strategy_name: str | None = None

        if self.strategy is not None:
            strategy_name = self.strategy.get_strategy_name()

        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
