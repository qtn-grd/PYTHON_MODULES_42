#!/usr/bin/env python3

import sys


def check_key(bag: dict[str, int], item: str) -> None:
    """Check if a specific item exists in the inventory and print result."""
    found = False

    for key, value in bag.items():
        if key == item and value > 0:
            found = True
    if found:
        print(f"Sample lookup - '{item}' is in inventory :-)")
        print("You can have it!")
    else:
        print(f"Sample lookup - '{item}' is not in inventory :-(")
        print("Go back exploring!")


def dictionary_resume(bag: dict[str, int]) -> None:
    """Print the keys and values of the inventory dictionary."""

    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys: ", end="")
    first = True
    for key in bag.keys():
        if not first:
            print(", ", end="")
        print(key, end="")
        first = False
    print()

    print("Dictionary values: ", end="")
    first = True
    for value in bag.values():
        if not first:
            print(", ", end="")
        print(value, end="")
        first = False
    print()


def evaluate_bag(bag: dict[str, int]) -> None:
    """Categorize items and display recommendations."""

    moderate_bag: dict[str, int] = dict()
    scarce_bag: dict[str, int] = dict()
    restock_bag: dict[str, int] = dict()

    moderate: int = 5

    for item, qty in bag.items():
        if qty >= moderate:
            moderate_bag.update({item: qty})
        else:
            scarce_bag.update({item: qty})
        if qty == 1 or qty == 0:
            restock_bag.update({item: qty})

    print("=== Item Categories ===")

    print(f"Moderate: {moderate_bag}")
    print(f"Scarce: {scarce_bag}")
    print()

    print("=== Management Suggestions ===")
    print(f"Restock needed: {list(restock_bag)}")
    print()


def study_bag(bag: dict[str, int]) -> None:
    """Display total items, unique types, sorted inventory,
    and abundance statistics."""

    unique_types = 0
    total_items = 0
    for item, qty in bag.items():
        if qty < 0:
            raise ValueError(f"Inventory contains negative quantity for "
                             f"item '{item}'")
        unique_types += 1
        total_items += qty

    print(f"Total items in inventory: {total_items}")
    if total_items <= 0:
        raise ValueError("Inventory total items <= 0")

    print(f"Unique item types: {unique_types}")
    print()

    print("=== Current Inventory ===")

    copy_bag: dict[str, int] = dict(bag)

    while len(copy_bag) > 0:

        max_qty = -1
        max_item = ""
        for item, qty in copy_bag.items():
            if qty > max_qty:
                max_qty = qty
                max_item = item

        percent = (max_qty / total_items) * 100

        if max_qty == 1:
            print(f"{max_item}: {max_qty} unit ({percent:.1f}%)")
        else:
            print(f"{max_item}: {max_qty} units ({percent:.1f}%)")

        copy_bag.pop(max_item)

    max_qty: int = -1
    min_qty: int | None = None
    most_abundant: str = ""
    least_abundant: str = ""

    for item, qty in bag.items():

        if qty > max_qty:
            max_qty = qty
            most_abundant = item
        if min_qty is None or qty < min_qty:
            min_qty = qty
            least_abundant = item

    print()
    print("=== Inventory Statistics ===")

    if max_qty > 1:
        print(f"Most abundant: {most_abundant} ({max_qty} units)")
    else:
        print(f"Most abundant: {most_abundant} ({max_qty} unit)")
    if min_qty > 1:
        print(f"Least abundant: {least_abundant} ({min_qty} units)")
    else:
        print(f"Least abundant: {least_abundant} ({min_qty} unit)")

    print()


def parse_arguments(arguments: list[str]) -> dict[str, int]:
    """Parse command-line arguments into an inventory dictionary."""

    bag: dict[str, int] = dict()

    for arg in arguments:
        separator = 0
        for charac in arg:
            if charac == ':':
                separator += 1
        if separator != 1:
            raise ValueError(f"Invalid argument format: '{arg}'")

    for arg in arguments:
        key_str: str = ""
        value_str: str = ""
        separator = False

        for charac in arg:
            if charac == ':':
                separator = True
                continue
            if not separator:
                key_str += charac
            else:
                value_str += charac

        try:
            value_int = int(value_str)
        except ValueError:
            raise ValueError(f"Invalid quantity of item: '{arg}'")

        if value_int < 0:
            raise ValueError(f"Negative quantity not allowed for "
                             f"item '{key_str}'")

        bag.update({key_str: value_int})

    return bag


def inventory_system() -> None:
    """Entry point of the inventory system."""

    print("=== Inventory System Analysis ===")
    print()
    arguments: list[str] = sys.argv[1:]

    if not arguments:
        print("Error: No items found... continue exploring!")
        return

    try:
        bag = parse_arguments(arguments)
    except ValueError as error:
        print(f"Error parsing inventory : {error}!")
        return

    print("Inventory successfully parsed!")
    print()

    try:
        study_bag(bag)
    except ValueError:
        print("Error: No items found... continue exploring!")
        return

    evaluate_bag(bag)

    dictionary_resume(bag)

    print()
    print("=== Item Recuperation ===")
    print("What are you looking for ?")
    print()
    looking_for: str = input()
    print()
    check_key(bag, looking_for)


if __name__ == "__main__":
    inventory_system()
