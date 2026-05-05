import sys


def command_quest() -> None:
    """Display command-line arguments passed to the script."""

    print("=== Command Quest ===")
    print()

    args = sys.argv

    print(f"Program name: {args[0]}")

    if len(args) == 1:
        print("No arguments provided!")
    else:
        listing = args[1:]
        print(f"Arguments received: {len(listing)}")
        for position, arg in enumerate(listing, start=1):
            print(f"Argument {position}: {arg}")
            position += 1

    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    command_quest()
