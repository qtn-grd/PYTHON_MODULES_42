from typing import Any
from collections.abc import Callable
import functools
import operator
import sys


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce a list of spell powers using a specified operation.

    Supported operations: 'add', 'multiply', 'max', 'min'.
    Returns 0 if the spell list is empty.
    Raises ValueError if the operation is unknown.
    """

    if not spells:
        return 0
    operations_dict = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
        }
    if operation not in operations_dict:
        raise ValueError(f"Unknown operation: {operation}")
    return functools.reduce(operations_dict[operation], spells)


def test_spell_reducer() -> None:
    """Test spell reduction with various operations and edge cases."""

    print("=" * 42)
    print("*", " " * 6, "Testing spell reducer...", " " * 6, "*")
    print("=" * 42)
    print()

    spell_powers = [41, 16, 12, 44, 21, 47]
    operations = ['add', 'multiply', 'max', 'min']

    labels = {
        "add": "Sum",
        "multiply": "Product",
        "max": "Max",
        "min": "Min"
    }

    print("Testing valid data...")
    print()

    for op in operations:
        try:
            print(f"{labels[op]}: {spell_reducer(spell_powers, op)}")
            print()
        except ValueError:
            print("Operation impossible")

    print()
    print("Testing empty data...")
    print()

    try:
        print(f"Empty: {spell_reducer([], 'add')}")
        print()
    except ValueError:
        print("Operation impossible")

    print()
    print("Testing invalid data...")
    print()

    try:
        print(spell_reducer(spell_powers, 'unknown'))
        print()
    except ValueError:
        print("Operation impossible")

    print()


def partial_enchanter(base_enchantment: Callable[
        [int, str, str], str]) -> dict[str, Callable[[str], str]]:
    """Create predefined elemental enchantments using partial application."""

    fire = functools.partial(base_enchantment, 50, "Fire")
    earth = functools.partial(base_enchantment, 50, "Earth")
    wind = functools.partial(base_enchantment, 50, "Wind")
    enchantment_dict = {"fire": fire, "earth": earth, "wind": wind}
    return enchantment_dict


def test_partial_enchanter() -> None:
    """Test partial enchantment factory with valid and invalid keys."""

    print("=" * 42)
    print("*", " " * 4, "Testing partial enchanter...", " " * 4, "*")
    print("=" * 42)
    print()

    def base_enchantment(power: int, element: str, target: str) -> str:
        """Apply an elemental enchantment to a target with a given power."""

        return f"{element} enchantment with power {power} on {target}"

    result = partial_enchanter(base_enchantment)

    print("Testing valid data...")
    print()

    try:
        print(result["fire"]("Dragon"))
        print(result["earth"]("Golem"))
        print(result["wind"]("Evaluator"))
        print()
    except KeyError as error:
        print(f"Invalid key: {error}")

    print()
    print("Testing invalid data...")
    print()

    try:
        print(result["water"]("Melon"))
    except KeyError as error:
        print(f"Error: {error} is not a valid key")

    print()


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Compute Fibonacci numbers with memoization.

    Raises:
        ValueError: if n is not a non-negative integer.
    """

    if not isinstance(n, int):
        raise ValueError(f"{n} is not an int")
    if n < 0:
        raise ValueError("Only positive int are valuable")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (memoized_fibonacci(n - 2) + memoized_fibonacci(n - 1))


def test_memoized_fibonacci() -> None:
    """Test Fibonacci computation and cache behavior."""

    print("=" * 42)
    print("*", " " * 4, "Testing memoized fibonacci...", " " * 3, "*")
    print("=" * 42)
    print()

    good_values = [0, 1, 10, 15]
    bad_values = ["", "error"]

    print("Testing good values...")
    print()
    for good_val in good_values:
        try:
            print(f"Fib({good_val}): {memoized_fibonacci(good_val)}")
        except ValueError as error:
            print(f"ValueError:  value '{good_val}' {error}")

    print()
    print("Cache info:", memoized_fibonacci.cache_info())
    print()

    print()
    print("Testing bad values...")
    print()

    for bad_val in bad_values:
        try:
            print(f"Fib({bad_val}): {memoized_fibonacci(bad_val)}")
        except ValueError as error:
            print(f"ValueError:  value '{bad_val}' {error}")

    print()
    print("Cache info:", memoized_fibonacci.cache_info())
    print()


def spell_dispatcher() -> Callable[[Any], str]:
    """Create a dispatcher that adapts behavior based on input type."""

    @functools.singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatcher.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatcher.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatcher


def test_spell_dispatcher() -> None:
    """Test dispatcher with multiple data types."""

    print("=" * 42)
    print("*", " " * 5, "Testing spell dispatcher...", " " * 4, "*")
    print("=" * 42)
    print()

    dispatch = spell_dispatcher()

    good_datas = [42, "fireball", [1, 2, 3], []]
    bad_datas = [{"no": "signal"}, None, 4.2]

    print("Testing valid datas...")
    print()

    for data in good_datas:
        print(dispatch(data))

    print()
    print()

    print("Testing invalid datas...")
    print()

    for data in bad_datas:
        print(dispatch(data))

    print()


def main() -> None:
    """Run all tests for exercise 3."""

    print()

    print()
    try:
        test_spell_reducer()
        print()
    except Exception as error:
        print(f"Error in test_spell_reducer: {error}", file=sys.stderr)
        sys.exit()

    print()
    try:
        test_partial_enchanter()
        print()
    except Exception as error:
        print(f"Error in test_partial_enchanter: {error}", file=sys.stderr)
        sys.exit()

    print()
    try:
        test_memoized_fibonacci()
        print()
    except Exception as error:
        print(f"Error in test_memoized_fibonacci: {error}", file=sys.stderr)
        sys.exit()

    print()
    try:
        test_spell_dispatcher()
        print()
    except Exception as error:
        print(f"Error in test_spell_dispatcher: {error}", file=sys.stderr)
        sys.exit()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
