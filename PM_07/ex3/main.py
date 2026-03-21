from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from typing import Any, Union
import sys


def main() -> None:

    print()
    print("=== DataDeck Game Engine ===")
    print()
    print("Configuring Fantasy Card Game...")

    factory: FantasyCardFactory = FantasyCardFactory()
    strategy: AggressiveStrategy = AggressiveStrategy()

    engine: GameEngine = GameEngine()

    try:
        engine.configure_engine(factory, strategy)
    except (AttributeError, TypeError) as error:
        print(f"Failed to configure engine: {error}", file=sys.stderr)
        return

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")

    print(f"Available types: {factory.supported_types}")
    print()
    print("Simulating aggressive turn...")

    try:
        result: dict[str, Any] = engine.simulate_turn()
    except Exception as error:
        print(f"Error during turn simulation: {error}", file=sys.stderr)
        return

    hand_display: list[Any] = []

    card: Union[Card, CreatureCard, SpellCard, ArtifactCard]
    for card in engine.hand:
        try:
            cost: int = getattr(card, "_cost")
            name: str = getattr(card, "_name")
            hand_display.append(f"{name} ({cost})")
        except AttributeError:
            hand_display.append("Unknown Card")

    hand_display_str: str = ", ".join(hand_display)
    print(f"Hand: [{hand_display_str}]")

    print()
    print("Turn execution:")

    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {result}")
    print()

    print("Game Report:")
    print(engine.get_engine_status())
    print()

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
