import sys


def sacred_scroll() -> None:
    """Demonstrates the Sacred Scroll (__init__.py) functionality
    in the Alchemy package."""

    print()
    print("=== Sacred Scroll Mastery ===")
    print()

    print("Testing direct module access:")

    import alchemy.elements

    try:
        print("alchemy.elements.create_fire():",
              alchemy.elements.create_fire())
        print("alchemy.elements.create_water():",
              alchemy.elements.create_water())
        print("alchemy.elements.create_earth():",
              alchemy.elements.create_earth())
        print("alchemy.elements.create_air():",
              alchemy.elements.create_air())
    except AttributeError as error:
        print(f"Error: {error}", file=sys.stderr)

    print()
    print("Testing package-level access (controlled by __init__.py):")

    import alchemy

    try:
        print("alchemy.create_fire():", alchemy.create_fire())
    except AttributeError:
        print("alchemy.create_fire(): AttributeError - not exposed",
              file=sys.stderr)

    try:
        print("alchemy.create_water():", alchemy.create_water())
    except AttributeError:
        print("alchemy.create_water(): AttributeError - not exposed",
              file=sys.stderr)

    try:
        print("alchemy.create_earth():", alchemy.create_earth())
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed",
              file=sys.stderr)

    try:
        print("alchemy.create_air():", alchemy.create_air())
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed",
              file=sys.stderr)

    print()
    print("Package metadata:")

    try:
        print("Version:", alchemy.__version__)
        print("Author:", alchemy.__author__)
    except AttributeError as error:
        print(f"AttributeError: {error}", file=sys.stderr)


if __name__ == "__main__":
    sacred_scroll()
