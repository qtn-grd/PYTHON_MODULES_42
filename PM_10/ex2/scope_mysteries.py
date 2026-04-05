from collections.abc import Callable
from typing import Any
import sys


def mage_counter() -> Callable:
    """Create a counter that increments each time it is called."""
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def test_mage_counter() -> None:
    """Test independent counters."""

    print("=" * 42)
    print("*", " " * 6, "Testing mage counter...", " " * 7, "*")
    print("=" * 42)

    print()

    player = "Evaluator"

    print(f"{player} wants to play hide and seek...")
    print()

    counter_a = mage_counter()
    counter_b = mage_counter()

    calling_a = 2
    calling_b = 1

    for _ in range(1, calling_a + 1):
        print(f"counter_a call {_}: {counter_a()}")
    for _ in range(1, calling_b + 1):
        print(f"counter_b call {_}: {counter_b()}")
    print()


def spell_accumulator(initial_power: int) -> Callable:
    """Accumulate power over multiple calls."""

    def accumulator(power_addition: int) -> int:
        nonlocal initial_power
        initial_power += power_addition
        return initial_power

    return accumulator


def test_spell_accumulator() -> None:
    """Test power accumulation."""

    print("=" * 42)
    print("*", " " * 4, "Testing spell accumulator...", " " * 4, "*")
    print("=" * 42)

    print()

    player = "Evaluator"

    print(f"{player} feels power growing...")
    print()

    base = 100
    accum = spell_accumulator(base)

    print(f"Base {base}, add 20: {accum(20)}")
    print(f"Base {base}, add 30: {accum(30)}")
    print()


def enchantment_factory(enchantment_type: str) -> Callable:
    """Create an enchantment function based on type."""

    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"

    return enchant


def test_enchantment_factory() -> None:
    """Test enchantment creation."""

    print("=" * 42)
    print("*", " " * 3, "Testing enchantment factory...", " " * 3, "*")
    print("=" * 42)

    player = "Evaluator"

    print()

    print(f"{player} commands blacksmith for a new set of equipment...")

    enchantment_types = ['Dark', 'Flowing', 'Flaming', 'Frozen']
    items_to_enchant = ['Amulet', 'Sword', 'Shield', 'Staff']

    for item in items_to_enchant:
        print()
        for enchantment in enchantment_types:
            result = enchantment_factory(enchantment)
            print(result(item))


def memory_vault() -> dict[str, Callable]:
    """Create a storage system with independent memory."""

    vault_storage: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault_storage[key] = value

    def recall(key: str) -> Any:
        return vault_storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def test_memory_vault() -> None:
    """Test independent memory vaults."""

    print("=" * 42)
    print("*", " " * 7, "Testing memory vault...", " " * 6, "*")
    print("=" * 42)

    print()

    thief = "Thief"
    player = "Evaluator"

    vault1 = memory_vault()
    vault2 = memory_vault()

    print(f"{player} stores his possessions in vault1 and vault2...")

    vault1["store"]("potion", "Elixir of Life")
    vault1["store"]("spell", "Fireball")
    vault2["store"]("potion", "Ice Brew")
    vault2["store"]("shield", "Wind Barrier")

    print()

    print(f"{thief} tries to recall secrets from vault1!")
    print()
    print("potion:", vault1["recall"]("potion"))
    print("spell:", vault1["recall"]("spell"))
    print("shield:", vault1["recall"]("shield"))

    print()
    print(f"{thief} tries to recall secrets from vault2!")
    print()
    print("potion:", vault2["recall"]("potion"))
    print("spell:", vault2["recall"]("spell"))
    print("shield:", vault2["recall"]("shield"))


def main() -> None:
    """Run all closure tests."""

    print()

    try:
        test_mage_counter()
        print()
    except Exception as error:
        print(f"Error in test_mage_counter: {error}", file=sys.stderr)
        sys.exit()

    try:
        test_spell_accumulator()
        print()
    except Exception as error:
        print(f"Error in test_spell_accumulator: {error}", file=sys.stderr)
        sys.exit()

    try:
        test_enchantment_factory()
        print()
    except Exception as error:
        print(f"Error in test_enchantment_factory: {error}", file=sys.stderr)
        sys.exit()

    try:
        test_memory_vault()
        print()
    except Exception as error:
        print(f"Error in test_memory_vault: {error}", file=sys.stderr)
        sys.exit()


if __name__ == "__main__":
    main()
