RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def input_temperature(temp_str: str) -> int:
    """Convert a string representing a temperature into an integer."""

    return int(temp_str)


def test_temperature() -> None:
    """Test the input_temperature function with valid and invalid inputs."""

    print("=== Garden Temperature ===")
    print()

    tests = ["25", "abc"]

    for test in tests:

        print(f"Input data is '{YELLOW}{test}{RESET}'")

        try:
            result = input_temperature(test)
            print(f"{GREEN}Temperature is now {result}°C{RESET}")
            print()

        except ValueError as error:
            print(f"{RED}Caught input_temperature error: {error}{RESET}")

    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
