#!/usr/bin/env python3


def garden_operations(case: int) -> None:
    """List different invalid operations"""

    if case == 1:
        int("abc")

    elif case == 2:
        42 / 0

    elif case == 3:
        open("missing.txt")

    elif case == 4:
        missing = {}
        print(missing['missing_plant'])


def test_error_types() -> None:
    """Force testing invalid operations"""

    print("=== Garden Error Types Demo ===")

    print()
    print("Testing ValueError...")
    try:
        garden_operations(1)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print()
    print("Testing ZeroDivisionError...")
    try:
        garden_operations(2)
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")

    print()
    print("Testing FileNotFoundError...")
    try:
        garden_operations(3)
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print()
    print("Testing KeyError...")
    try:
        garden_operations(4)
    except KeyError as error:
        print(f"Caught KeyError: {error}")

    print()
    print("Testing multiple errors together...")
    try:
        garden_operations(1)
        garden_operations(2)
        garden_operations(3)
        garden_operations(4)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
