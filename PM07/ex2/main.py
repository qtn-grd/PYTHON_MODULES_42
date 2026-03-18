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
        methods = [met for met in dir(cls)
                   if callable(getattr(cls, met)) and not met.startswith("__")]
        capabilities[cls.__name__] = methods

    print("EliteCard capabilities:")
    for parent, method_list in capabilities.items():
        print(f"- {parent}: {method_list}")

    print()

    try:
        arcane_warrior: EliteCard = EliteCard(
            "Arcane Warrior", 10, "Epic", 5, 10, 8
        )
    except (CardError, TypeError) as error:
        print(f"Error creating elite card: {error}", file=sys.stderr)
        return

    try:
        enemy: CreatureCard = CreatureCard("Enemy", 2, "Common", 5, 5)
    except (CardError, TypeError) as error:
        print(f"Error creating creature card: {error}", file=sys.stderr)
        return

    print(f"Playing: {arcane_warrior.name} ({type(arcane_warrior).__name__}):")
    print()

    print("Combat phase:")

    att_result: dict[str, Any] = arcane_warrior.attack(enemy)
    def_result: dict[str, Any] = arcane_warrior.defend(enemy.attack)

    print(f"Attack result: {att_result}")
    print(f"Defense result: {def_result}")

    print()

    print("Magic phase:")

    targets: list[str] = ["Enemy1", "Enemy2"]

    spell_result: dict[str, Any] = arcane_warrior.cast_spell(
        "Fireball", targets)
    print(f"Spell cast: {spell_result}")

    mana_result: dict[str, Any] = arcane_warrior.channel_mana(3)
    print(f"Mana channel: {mana_result}")

    print()
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
