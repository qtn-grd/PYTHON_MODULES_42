#!/usr/bin/env python3


def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int
) -> str:
    """Check plant health values and raise errors if invalid."""

    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")

    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")

    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         f"is too high (max 12)")

    return (f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """Raise and catch different errors"""

    print("=== Garden Plant Health Checker ===")
    print()

    print("Testing good values...")
    try:
        test_ok = check_plant_health("tomato", 5, 5)
        print(test_ok)
    except ValueError as error:
        print(f"Error: {error}")
    print()

    print("Testing empty plant name...")
    try:
        test_missing_name = check_plant_health("", 5, 5)
        print(test_missing_name)
    except ValueError as error:
        print(f"Error: {error}")
    print()

    print("Testing bad water level...")
    try:
        test_flood = check_plant_health("tomato", 15, 5)
        print(test_flood)
    except ValueError as error:
        print(f"Error: {error}")
    print()

    print("Testing bad sunlight hours...")
    try:
        test_darkness = check_plant_health("tomato", 5, 0)
        print(test_darkness)
    except ValueError as error:
        print(f"Error: {error}")
    print()

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
