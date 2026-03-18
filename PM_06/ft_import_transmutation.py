import sys


def import_transmutation() -> None:
    """Demonstrates four different import styles in the Alchemy package."""

    print()
    print("=== Import Transmutation Mastery ===")
    print()

    print("Method 1 - Full module import:")

    import alchemy.elements

    try:
        print("alchemy.elements.create_fire():",
              alchemy.elements.create_fire())
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)

    print()
    print("Method 2 - Specific function import:")

    from alchemy.elements import create_water

    try:
        print("create_water():", create_water())
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)

    print()
    print("Method 3 - Aliased import:")

    from alchemy.potions import healing_potion as heal

    try:
        print("heal():", heal())
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)

    print()
    print("Method 4 - Multiple imports:")

    from alchemy.elements import create_earth as earth, create_fire as fire
    from alchemy.potions import strength_potion as strength

    try:
        print("create_earth():", earth())
        print("create_fire():", fire())
        print("strength_potion():", strength())
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)

    print()
    print("All import transmutation methods mastered")


if __name__ == "__main__":
    import_transmutation()
