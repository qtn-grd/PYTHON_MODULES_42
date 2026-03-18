#!/usr/bin/env python3


def water_plants(plants: list[str]) -> None:
    """Run a list and check if all elements are correct."""

    print("Opening watering system")
    success = 0

    try:
        for plant in plants:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            else:
                print(f"Watering {plant}")
                success += 1

    except ValueError as error:
        print(f"Error: {error}")

    finally:
        print("Closing watering system (cleanup)")
        if success == len(plants):
            print("Watering completed successfully!")


def test_watering_system() -> None:
    """Test two lists, one with a missing element."""

    print("=== Garden Watering System ===")
    print()

    print("Testing normal watering...")
    good_list = ["tomato", "lettuce", "carrots"]
    water_plants(good_list)
    print()

    print("Testing with error...")
    wrong_list = ["tomato", None, "carrots"]
    water_plants(wrong_list)
    print()

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
