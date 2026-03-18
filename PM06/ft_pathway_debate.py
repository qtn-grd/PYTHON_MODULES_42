import sys


def pathway_debate() -> None:
    """Demonstrates absolute vs relative imports in the Alchemy package."""

    print()
    print("=== Pathway Debate Mastery ===")
    print()

    print("Testing Absolute Imports (from basic.py):")

    from alchemy.transmutation import lead_to_gold, stone_to_gem

    try:
        print("lead_to_gold():", lead_to_gold())
        print("stone_to_gem():", stone_to_gem())
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)

    print()
    print("Testing Relative Imports (from advanced.py):")

    from alchemy.transmutation.advanced import (
        philosophers_stone, elixir_of_life
    )

    try:
        print("philosophers_stone():", philosophers_stone())
        print("elixir_of_life():", elixir_of_life())
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)

    print()
    print("Testing Package Access:")

    import alchemy.transmutation

    try:
        print("alchemy.transmutation.lead_to_gold():",
              alchemy.transmutation.lead_to_gold())
        print(
            "alchemy.transmutation.philosophers_stone():",
            alchemy.transmutation.philosophers_stone(),
        )
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)

    print()
    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    pathway_debate()
