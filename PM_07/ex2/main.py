from ex0.Card import Card, CardError
from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
import sys
from typing import Any


def main() -> None:
    """
    Demonstrates the Ability Layer for Exercise 2.
    Creates an EliteCard, lists all its capabilities from
    multiple inherited interfaces, executes a combat phase,
    then executes a magic phase
    with spell casting and mana channeling.
    """

    print()
    print("=== DataDeck Ability System ===")
    print()

    capabilities: dict[str, list[str]] = {}

    for cls in [Card, Combatable, Magical]:
        methods = [
            name for name, value in cls.__dict__.items()
            if callable(value) and not name.startswith("__")
        ]
        capabilities[cls.__name__] = methods

    print("EliteCard capabilities:")
    for parent, method_list in capabilities.items():
        print(f"- {parent}: {method_list}")

    print()

    try:
        arcane_warrior: EliteCard = EliteCard(
            "Arcane Warrior", 10, "Epic", 5, 10, 8
        )
        print(f"Playing: {arcane_warrior._name} "
              f"({type(arcane_warrior).__name__}):")
    except (CardError, TypeError) as error:
        print(f"Error creating elite card: {error}", file=sys.stderr)
        return

    try:
        enemy: CreatureCard = CreatureCard("Enemy", 2, "Common", 5, 5)
    except (CardError, TypeError) as error:
        print(f"Error creating creature card: {error}", file=sys.stderr)
        return

    print()

    print("Combat phase:")

    try:
        att_result: dict[str, Any] = arcane_warrior.attack(enemy)
        def_result: dict[str, Any] = arcane_warrior.defend(enemy._attack)

        print(f"Attack result: {att_result}")
        print(f"Defense result: {def_result}")
    except (NameError, TypeError) as error:
        print(f"Error: {error}", file=sys.stderr)

    print()

    print("Magic phase:")

    targets: list[str] = ["Enemy1", "Enemy2"]

    spell_result: dict[str, Any] = arcane_warrior.cast_spell(
        "Fireball", targets)
    print(f"Spell cast: {spell_result}")

    try:
        spring_mana: int = 3
        mana_result: dict[str, Any] = arcane_warrior.channel_mana(spring_mana)
        print(f"Mana channel: {mana_result}")
    except TypeError as error:
        print(f"Error: {error}", file=sys.stderr)

    print()
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
