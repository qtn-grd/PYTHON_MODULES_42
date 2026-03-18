from ex0.Card import CardError
from ex0.CreatureCard import CreatureCard
import sys


def main() -> None:
    """
    Demonstration script for Exercise 0: Card Foundation.

    Creates CreatureCard instances, displays their information,
    tests if they are playable with different mana amounts,
    simulates playing a card, and simulates a combat action.
    """

    print()
    print("=== DataDeck Card Foundation ===")
    print()

    print("Testing Abstract Base Class Design:")
    print()

    try:
        fire_dragon: CreatureCard = CreatureCard(
            "Fire Dragon", 5, "Legendary", 7, 5
            )
    except (CardError, TypeError) as error:
        print(f"Error creating creature card: {error}", file=sys.stderr)
        return

    print("CreatureCard Info:")

    print(fire_dragon.get_card_info())
    print()

    available_mana: int = 6

    print(f"Playing {fire_dragon.name} with {available_mana} mana available:")
    print(f"Playable: {fire_dragon.is_playable(available_mana)}")

    if fire_dragon.is_playable(available_mana):
        print(f"Play result: {fire_dragon.play({})}")

    print()

    try:
        goblin_warrior: CreatureCard = CreatureCard(
            "Goblin Warrior", 2, "Common", 3, 2
        )
    except (CardError, TypeError) as error:
        print(f"Error creating creature card: {error}", file=sys.stderr)
        return

    print(f"{fire_dragon.name} attacks {goblin_warrior.name}:")
    print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")
    print()

    available_mana = 3

    print(f"Testing insufficient mana ({available_mana} available):")
    print(f"Playable: {fire_dragon.is_playable(available_mana)}")
    if fire_dragon.is_playable(available_mana):
        print(f"Play result: {fire_dragon.play({})}")

    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
