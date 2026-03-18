import sys


def circular_curse() -> None:
    """Demonstrates safe handling of circular import issues
    in the Alchemy package."""

    print()
    print("=== Circular Curse Breaking ===")
    print()

    print("Testing ingredient validation:")

    from alchemy.grimoire import validate_ingredients

    try:
        print('validate_ingredients("fire air"):',
              validate_ingredients("fire air"))
        print('validate_ingredients("dragon scales"):',
              validate_ingredients("dragon scales"))
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)

    print()
    print("Testing spell recording with validation:")

    from alchemy.grimoire import record_spell

    try:
        print('record_spell("Fireball", "fire air"):',
              record_spell("Fireball", "fire air"))
        print('record_spell("Dark Magic", "shadow"):',
              record_spell("Dark Magic", "shadow"))
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)

    print()
    print("Testing late import technique:")

    try:
        print('record_spell("Lightning", "air"):',
              record_spell("Lightning", "air"))
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)

    print()
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    circular_curse()
