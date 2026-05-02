RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def garden_operations(operation_number: int) -> None:
    """Perform different operations that may raise various exceptions.
    Each operation number triggers a specific error:"""

    if operation_number == 0:
        int("abc")

    elif operation_number == 1:
        42 / 0

    elif operation_number == 2:
        open("/non/existent/file")

    elif operation_number == 3:
        "abc" + 42

    else:
        return f"{GREEN}Operation completed successfully{RESET}"


def test_error_types() -> None:
    """Test and demonstrate handling of different exception types."""

    for test in range(0, 5):

        print()
        print(f"Testing operation {YELLOW}{test}{RESET}...")

        try:
            result = garden_operations(test)
            if result:
                print(result)

        except ValueError as error:
            print(f"Caught ValueError: {RED}{error}{RESET}")

        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {RED}{error}{RESET}")

        except (FileNotFoundError, TypeError) as error:
            print(f"Caught FileNotFoundError: {RED}{error}{RESET}")


def main() -> None:
    """Entry point of the program."""

    print("=== Garden Error Types Demo ===")

    test_error_types()

    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    main()
