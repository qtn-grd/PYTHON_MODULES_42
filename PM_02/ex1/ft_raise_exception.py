RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def input_temperature(temp_str: str) -> int:
    """Convert a string to an integer temperature and validate its range."""

    result = int(temp_str)

    if result < 0:
        raise ValueError(f"{result}°C is too cold for plants (min 0°C)")
    elif result > 40:
        raise ValueError(f"{result}°C is too hot for plants (max 40°C)")

    return result


def test_temperature() -> None:
    """Test the input_temperature function with various inputs."""

    print("=== Garden Temperature Checker ===")
    print()

    tests = ["25", "abc", "100", "-50"]

    for test in tests:

        print(f"Input data is '{YELLOW}{test}{RESET}'")

        try:
            result = input_temperature(test)
            print(f"{GREEN}Temperature is now {result}°C{RESET}")
            print()

        except ValueError as error:
            print(f"Caught input_temperature error: {RED}{error}{RESET}")
            print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
