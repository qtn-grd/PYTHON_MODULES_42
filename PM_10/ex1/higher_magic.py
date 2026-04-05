import sys
from typing import List
from collections.abc import Callable


def enough_mana(target: str, power: int) -> bool:
    """Check if there is enough mana to cast a spell."""
    return power >= 10


def hug(target: str, power: int) -> str:
    """A... questionable healing spell."""
    return f"hugs {target} for {power} HP"


def freezing(target: str, power: int) -> str:
    """Ice damage spell."""
    return f"Inflicts {power} ice damage to {target}!"


def fireball(target: str, power: int) -> str:
    """Fire damage spell."""
    return f"Fireball hits {target} for {power} HP"


def thunder(target: str, power: int) -> str:
    """Lightning damage spell."""
    return f"Thunder hits {target} for {power} HP"


def storm(target: str, power: int) -> str:
    """Wind damage spell."""
    return f"Wind hits {target} for {power} HP"


def aqua(target: str, power: int) -> str:
    """Water damage spell."""
    return f"Water hits {target} for {power} HP"


def heal(target: str, power: int) -> str:
    """Healing spell."""
    return f"Heal restores {target} for {power} HP"


def spell_combiner(
        spell1: Callable,
        spell2: Callable) -> Callable:
    """Combine two spells into one that returns both results."""

    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined


def power_amplifier(base_spell: Callable,
                    multiplier: int) -> Callable:
    """Amplify a spell's power by a multiplier."""

    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(
        condition: Callable,
        spell: Callable) -> Callable:
    """Cast a spell only if a condition is met."""

    def casted(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return casted


def spell_sequence(
        spells: List[Callable]) -> Callable:
    """Execute a sequence of spells."""

    def chained(target: str, power: int) -> List[str]:
        return [spell(target, power) for spell in spells]

    return chained


def test_spell_combiner(target: str, player: str) -> None:
    """Test combining two spells."""

    print("=" * 42)
    print("*", " " * 13, "PART ONE:", " " * 14, "*")
    print("*", " " * 6, "Testing spell combiner...", " " * 5, "*")
    print("=" * 42)

    print()
    print(f"Oh no! A wild {target} appears!")
    print()
    print(f'{target}: "Hit me..."')
    print()
    print(f"{player} prepares a fireball...")
    print(fireball(target, 10))
    print()
    print(f"{target} is still here!")
    print()
    print(f'{target}: "Hit me... Love me..."')
    print()
    print(f"{player} is combining spells...")

    combined = spell_combiner(fireball, heal)
    result = combined(target, 10)

    print(f"{player} casts combined spells!")
    print()
    print(f"{result[0]}, {result[1]}")
    print()
    print(f"{target} is KO...")
    print(f"{player} won!")
    print()


def test_power_amplifier(target: str, player: str) -> None:
    """Test power amplification."""

    print("=" * 42)
    print("*", " " * 13, "PART TWO:", " " * 14, "*")
    print("*", " " * 5, "Testing power amplifier...", " " * 5, "*")
    print("=" * 42)

    print()
    print(f"{target} is back! (surprise!)")
    print()
    print(f'{target}: "Hit me..."')
    print()
    print(f"{player} prepares a fireball...")
    print(fireball(target, 10))
    print()
    print(f'{target}: "More... I need more..."')
    print()
    print(f"{player} prepares a powerful attack...")

    mega_fireball = power_amplifier(fireball, 3)
    print(f"{player} prepares a mega fireball!")
    print()
    print(f"Mega{mega_fireball(target, 10)}")
    print()
    print(f"{target} is KO...")
    print(f"{player} won!")
    print()


def test_conditional_cast(target: str, player: str) -> None:
    """Test conditional spell casting."""

    print("=" * 42)
    print("*", " " * 13, "PART THREE:", " " * 12, "*")
    print("*", " " * 5, "Testing conditional cast...", " " * 4, "*")
    print("=" * 42)

    print()
    print(f"{target} is back! (yes... again...)")
    print()
    print(f'{target}: "Wanna play... more..."')
    print()
    print(f"{player} aims {target}...")

    mana = 5
    result = conditional_caster(enough_mana, freezing)

    print(f"...but {player} is tired!")
    print()
    print(result(target, mana))
    print()

    mana *= 2

    print(f"{player} concentrates and casts again...")
    print(result(target, mana))
    print()
    print(f"{target} is KO...")
    print(f"{player} won!")
    print()


def test_spell_sequence(target: str, player: str) -> None:
    """Test executing a sequence of spells."""

    print("=" * 42)
    print("*", " " * 13, "PART FOUR:", " " * 13, "*")
    print("*", " " * 6, "Testing spell sequence...", " " * 5, "*")
    print("=" * 42)

    print()
    print(f"{target} refuses to die. (sadly...)")
    print(f"{player} loses patience...")
    print()

    spells = [fireball, thunder, storm, aqua]
    sequence = spell_sequence(spells)

    results = sequence(target, 10)

    for res in results:
        print(f"--> {res}")

    print()
    print(heal(target, 40))

    print()
    print(f"{target} is happy!")
    print(target, hug(player, -100))
    print()
    print(f"{player} is KO...")
    print(f"{target} won!")
    print()


def main() -> None:
    """Run all spell tests."""

    print()

    print("=" * 42)
    print("*", " " * 13, "GAME START", " " * 13, "*")
    print("=" * 42)

    target = "Masochist"
    player = "Evaluator"

    print()
    print(f"{player} goes on an adventure!")
    print()

    try:
        test_spell_combiner(target, player)
    except Exception as error:
        print(f"Error in test_spell_combiner: {error}", file=sys.stderr)
        sys.exit()

    try:
        test_power_amplifier(target, player)
    except Exception as error:
        print(f"Error in test_power_amplifier: {error}", file=sys.stderr)
        sys.exit()

    try:
        test_conditional_cast(target, player)
    except Exception as error:
        print(f"Error in test_conditional_cast: {error}", file=sys.stderr)
        sys.exit()

    try:
        test_spell_sequence(target, player)
    except Exception as error:
        print(f"Error in test_spell_sequence: {error}", file=sys.stderr)
        sys.exit()

    print("=" * 42)
    print("*", " " * 14, "GAME OVER", " " * 13, "*")
    print("=" * 42)


if __name__ == "__main__":
    main()
