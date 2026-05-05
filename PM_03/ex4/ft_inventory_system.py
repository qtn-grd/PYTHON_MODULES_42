import sys


def get_inventory(args: list[str]) -> dict[str, int]:
    """Parse command-line arguments into an inventory dictionary.
    Each argument must follow the format 'item:quantity'.
    Invalid parameters and duplicates are reported and discarded."""

    inventory = {}

    for arg in args:

        try:
            adding = True

            arg_key, arg_value = arg.split(":")

            arg_key = arg_key.strip().lower()
            arg_value = arg_value.strip()
            if arg_key in inventory:
                print(f"Redundant item '{arg_key}' - discarding")
                adding = False
                continue

        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            adding = False
            continue

        try:
            int_value = int(arg_value)
            if int_value == 0:
                raise ValueError("nul value - rejected")
            if int_value < 0:
                raise ValueError("negative value - rejected")
        except ValueError as error:
            print(f"Quantity error for '{arg_key}': {error}")
            adding = False

        if adding:
            inventory[arg_key] = int_value

    print()
    print(f"Got inventory: {inventory}")
    print()

    return inventory


def study_inventory(inventory: dict[str, int]) -> None:
    """Analyze and display information about the inventory."""

    item_list = list(inventory.keys())

    print(f"Item list: {item_list}")

    total_quantity = sum(inventory.values())

    print(f"Total quantity of the {len(item_list)} items: {total_quantity}")
    print()

    most_abundant = ""
    least_abundant = ""
    max_quantity = 1
    min_quantity = 1
    first_item = True

    for item_name, item_quantity in inventory.items():
        print(f"Item {item_name} represents "
              f"{round((item_quantity/total_quantity)*100, 1)}%")

        if first_item:
            most_abundant = item_name
            least_abundant = item_name
            max_quantity = item_quantity
            min_quantity = item_quantity
            first_item = False
        else:
            if item_quantity < min_quantity:
                least_abundant = item_name
                min_quantity = item_quantity

        if item_quantity > max_quantity:
            most_abundant = item_name
            max_quantity = item_quantity

    print()
    print("Item most abundant: "
          f"{most_abundant} with quantity {max_quantity}")
    print("Item least abundant: "
          f"{least_abundant} with quantity {min_quantity}")


def main():
    """Entry point of the inventory system program."""

    print("=== Inventory System Analysis ===")
    print()

    inventory = get_inventory(sys.argv[1:])

    if inventory:
        study_inventory(inventory)
    else:
        print("Inventory is empty!")

    inventory.update({"magic_item": 1})

    print()
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
