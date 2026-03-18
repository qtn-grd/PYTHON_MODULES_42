#!/usr/bin/env python3


def check_temperature(temp_str: str) -> int:
    """Check if temperature is valid"""

    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number")

    if temp < 0:
        raise ValueError(f"{temp} is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp} is too hot for plants (max 40°C)")
    return temp


def test_temperature_input() -> None:
    """Test valid and invalid temperature inputs"""

    print("=== Garden Temperature Checker ===")

    tests = ["25", "abc", "100", "-50"]

    for value in tests:
        print()
        print(f"Testing temperature: {value}")
        try:
            temp = check_temperature(value)
            print(f"Temperature {temp}°C is perfect for plants!")
        except ValueError as error:
            print(f"Error: {error}")

    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
