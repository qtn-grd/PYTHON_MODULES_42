from typing import Optional
import sys


GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def access_archive() -> Optional[str]:
    """Read and display archive content."""

    try:

        file_name = sys.argv[1]

        print(f"Accessing file '{YELLOW}{file_name}{RESET}'")
        print()

        file_one = open(file_name, "r")

        print("---")
        print()
        brut_data = file_one.read()
        print(brut_data)
        print("---")

        file_one.close()

        print()
        print(f"File '{GREEN}{file_name}{RESET}' closed.")

    except IndexError:
        print(f"Usage: {sys.argv[0]} {YELLOW}<file>{RESET}")
        return None

    except (FileNotFoundError, PermissionError) as error:
        print("Error opening file "
              f"'{YELLOW}{file_name}{RESET}': {RED}{error}{RESET}")
        return None

    except OSError as error:
        print("Error opening file "
              f"'{YELLOW}{file_name}{RESET}': {RED}{error}{RESET}")
        return None

    return brut_data


def generate_archive(brut_data: str) -> None:
    """Transform and optionally save archive data."""

    print("Transform data:")
    print()

    transformed_lines = []

    for line in brut_data.split("\n"):
        transformed_lines.append(line + "#")

    transformed_data = "\n".join(transformed_lines)

    print()
    print("---")
    print()
    print(transformed_data)
    print("---")
    print()

    try:
        new_name = input("Enter new file name (or empty): ")

        if new_name == "":
            print(f"{YELLOW}Not saving data.{RESET}")
        else:
            new_file = open(new_name, "w")
            new_file.write(transformed_data)
            new_file.close()
            print()
            print(f"Saving data to '{YELLOW}{new_name}'{RESET}")
            print(f"{GREEN}Data saved {RESET}in file "
                  f"'{YELLOW}{new_name}{RESET}'.")

    except PermissionError as error:
        print("Error saving data "
              f"'{YELLOW}{new_name}{RESET}': {RED}{error}{RESET}")
        print(f"{YELLOW}Not saving data.{RESET}")
        return

    except OSError as error:
        print("Error saving data "
              f"'{YELLOW}{new_name}{RESET}': {RED}{error}{RESET}")
        print(f"{YELLOW}Not saving data.{RESET}")
        return


def main() -> None:
    """Run the archive recovery workflow."""

    print("=== Cyber Archives Recovery & Preservation ===")
    print()

    brut_data = access_archive()

    print()
    if brut_data:
        generate_archive(brut_data)


if __name__ == "__main__":
    main()
