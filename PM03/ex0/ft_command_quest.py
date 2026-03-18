#!/usr/bin/env python3

import sys


def command_quest() -> None:
    """Display information about command-line arguments."""

    print("=== Command Quest ===")
    arguments: list[str] = sys.argv[1:]

    if not arguments:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        count: int = 1
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(arguments)}")
        for arg in arguments:
            print(f"Argument {count}: {arg}")
            count += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    command_quest()
