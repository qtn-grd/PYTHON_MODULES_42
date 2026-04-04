import time
from functools import wraps
from typing import Any
from collections.abc import Callable
import sys


def spell_timer(func: Callable) -> Callable:
    """Measure execution time of a function."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Wrap the function to measure execution time and display logs."""

        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        timer = end - start
        print(f"Spell completed in {timer:.3f} seconds")
        return result
    return wrapper


def test_spell_timer(target: str, player: str):
    """Test the spell_timer decorator with basic and advanced spells."""

    print("=" * 42)
    print("*", " " * 13, "PART ONE:", " " * 14, "*")
    print("*", " " * 6, "Testing spell timer...", " " * 5, "*")
    print("=" * 42)

    print()
    print(f"Oh no! A wild {target} appears! (not again???)")
    print()
    print()
    print(f'{target}: "H..."')
    print()
    print(f'{player}: "Enough! No time to play!"')
    print()

    @spell_timer
    def fireball(target: str, power: int) -> str:
        """Simulate a fireball attack with a fixed delay."""

        time.sleep(0.1)
        return f"Fireball hits {target} for {power} damage!"

    @spell_timer
    def advanced_attack(spell_name: str, target: str, power: int) -> str:
        """Simulate a named spell attack with execution delay."""

        time.sleep(0.1)
        return f"{spell_name} hits {target} for {power} damage!"

    basic_result = fireball(target, 10)
    print(basic_result)

    print()

    result_args = advanced_attack("Quick Fireball", target, 20)
    print("Result (args):", result_args)

    print()

    result_kwargs = advanced_attack(
        spell_name="Meteor",
        target=target,
        power=100
    )
    print("Result (kwargs):", result_kwargs)

    print()
    print(f"{target} is KO...")
    print(f"{player} won!")
    print()


def power_validator(min_power: int) -> Callable:
    """Create a decorator that validates if a spell has sufficient power."""

    def decorator(func: Callable) -> Callable:
        """Decorator that checks the power before executing the function."""

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Validate power before executing the decorated function."""

            validation_power = next(
                filter(lambda x: isinstance(x, int), args),
                kwargs.get('power')
            )

            if validation_power is not None and validation_power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)
        return wrapper
    return decorator


def test_power_validator(target: str, player: str):
    """Test power validation with decreasing mana across multiple targets."""

    print("=" * 42)
    print("*", " " * 13, "PART TWO:", " " * 14, "*")
    print("*", " " * 5, "Testing power validator...", " " * 5, "*")
    print("=" * 42)

    print()

    print(f"{player} hears a noise and turn back...")
    print()

    print(f"Oh no! {target} came with his three minions!")
    print(f"{target}'s minions: 'Vengeance!'")
    print()

    @power_validator(10)
    def cast_fire(power: int, target: str) -> str:
        """Cast a fire spell on a target using available mana."""

        return f"Fire hits {target} with {power} MP!"

    mana = 15
    targets = ["Maso_minion1", "Maso_minion2", "Maso_minion3"]

    print(f"{player} attacks all of them...")
    print()

    for t in targets:
        current_power = mana
        result = cast_fire(current_power, t)
        mana -= 5
        print(result)

    print()
    print(f"{player} is outnumbered...")
    print(f"{player} runs away!")
    print()


def retry_spell(max_attempts: int) -> Callable:
    """Create a decorator that retries a function upon failure."""

    def decorator(func: Callable) -> Callable:
        """Decorator that retries execution up to max_attempts on exception."""

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Attempt to execute a function multiple times if it fails."""

            if max_attempts < 0:

                return ("Spell casting failed after 0 attempts\n"
                        "Waaaaaaagh spelled !")

            if max_attempts > 0:
                for attempt in range(1, max_attempts + 1):
                    try:
                        return func(*args, **kwargs)
                    except Exception:
                        if attempt < max_attempts:
                            print(f"Spell failed, retrying... "
                                  f"(attempt {attempt}/{max_attempts})")
            return (f"Spell casting failed after {max_attempts} attempts\n"
                    "Waaaaaaagh spelled !")

        return wrapper
    return decorator


def test_retry_spell(target: str, player: str):
    """Test retry mechanism with a consistently failing function."""

    print("=" * 42)
    print("*", " " * 12, "PART THREE:", " " * 13, "*")
    print("*", " " * 7, "Testing retry spell...", " " * 7, "*")
    print("=" * 42)

    print()

    print(f"One week later, {player} is still traumatized...")
    print()
    print(f"{player} tries some exercices to overcome it...")

    print()

    @retry_spell(max_attempts=3)
    def trauma() -> None:
        """Simulate a failing spell to test retry behavior."""

        raise ValueError("Impossible to concentrate")

    failure = trauma()

    print(failure)
    print()

    print(f"{player} can't overcome it...")
    print("...and fail his exam")

    print()
    print(f"{player} leaves the guild bitterly...")
    print()


class MageGuild:
    """Represent a guild responsible for validating and casting spells."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Validate a mage name (at least 3 characters,
        letters and spaces only)."""

        try:
            if len(name) < 3:
                return False
            if not all(char.isalpha() or char.isspace() for char in name):
                return False
            return True
        except TypeError:
            return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell if sufficient power is provided."""

        return f"Successfully cast {spell_name} with {power} power"


def test_mageguild(target: str, player: str):
    """Test mage validation and spell casting within the MageGuild."""

    print("=" * 42)
    print("*", " " * 13, "PART FOUR:", " " * 13, "*")
    print("*", " " * 8, "Testing Mageguild ...", " " * 7, "*")
    print("=" * 42)

    mage = MageGuild()
    guard = MageGuild()

    print()

    print("A few other days have passed...")
    print()
    print(f"Shocked,{player} has forgotten many things, even his name...")
    print()

    print(f"And when some day {player}'s steps "
          "aim to cross the guild front gate...")
    print()
    print(f'{target}: "Halt! Only current and past students may pass!')
    print(f'{target}: "Who are you?')

    print()
    print(f'{player}: "Ev... ev..."')
    print()
    print(f'-->\t{mage.validate_mage_name("Ev")}')
    print()
    print(f"{player} is rejected hardly, while another person overtake him")
    print()
    print(f'-->\t{mage.validate_mage_name("Student")}')
    print()

    print(f"{target} wants {player} to leave...")
    print()
    print(f'-->\t{guard.cast_spell("Repel", 20)}')
    print()
    print(f"{player} try to resist...")
    print()
    print(f'-->\t{mage.cast_spell("Resist", 2)}')

    print()
    print(f"{player} give up and leave the city")
    print()
    print()
    print(f"Progressively, {player} started a new life "
          "far away from civilization...")
    print("He loses sociability and express his rage"
          " when fighting monsters bare handed")
    print()
    print("Fight after fight, "
          "he starts to appreciate violence and suffering...")


def main():
    """Run all test scenarios for decorator mastery."""

    print()

    print("=" * 42)
    print("*", " " * 13, "GAME START", " " * 13, "*")
    print("=" * 42)

    target = "Masochist"
    player = "Evaluator"

    print()
    print(f"{player} goes on a new adventure!")
    print()

    try:
        test_spell_timer(target, player)
        print()
    except Exception as error:
        print(f"Error in test_spell_timer: {error}", file=sys.stderr)
        sys.exit()

    try:
        test_power_validator(target, player)
        print()
    except Exception as error:
        print(f"Error in test_power_validator: {error}", file=sys.stderr)
        sys.exit()

    try:
        test_retry_spell(target, player)
        print()
    except Exception as error:
        print(f"Error in test_retry_spell: {error}", file=sys.stderr)
        sys.exit()

    target = "Door guard"

    try:
        test_mageguild(target, player)
        print()
    except Exception as error:
        print(f"Error in test_mage_guild: {error}", file=sys.stderr)
        sys.exit()

    print()

    print("=" * 42)
    print("*", " " * 14, "GAME OVER", " " * 13, "*")
    print("=" * 42)


if __name__ == "__main__":
    main()
