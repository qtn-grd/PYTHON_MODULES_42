import sys


GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def read_file() -> None:
    """Read and display the content of a file."""

    print("=== Cyber Archives Recovery ===")
    print()

    try:

        file_name = sys.argv[1]

        print(f"Accessing file '{YELLOW}{file_name}{RESET}'")
        print()

        f = open(file_name, "r")

        print("---")
        print()
        print(f.read())
        print("---")

        f.close()

        print(f"\nFile '{GREEN}{file_name}{RESET}' closed.")

    except IndexError:
        print(f"Usage: {sys.argv[0]} {YELLOW}<file>{RESET}")

    except (FileNotFoundError, PermissionError) as error:
        print("Error opening file "
              f"'{YELLOW}{file_name}{RESET}': {RED}{error}{RESET}")

    except OSError as error:
        print("Error opening file "
              f"'{YELLOW}{file_name}{RESET}': {RED}{error}{RESET}")


if __name__ == "__main__":
    read_file()
