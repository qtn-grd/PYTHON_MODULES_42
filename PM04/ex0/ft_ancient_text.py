#!/usr/bin/env python3

from typing import TextIO


def ancient_text() -> None:
    """Reads 'ancient_fragment.txt' file and displays its content
    as part of the cyber archive recovery process.

    If the file does not exist, an error message is displayed."""

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print("Accessing Storage Vault: ancient_fragment.txt")

    try:
        file: TextIO = open("ancient_fragment.txt", "r")
    except FileNotFoundError as error:
        raise FileNotFoundError(
            "Storage vault not found. Run data generator first."
            ) from error
    except OSError as error:
        raise OSError(
            "Could not access the storage vault due to system error."
            ) from error

    print("Connection established...")

    content: str = file.read()

    print()
    print("RECOVERED DATA:")
    print(content)

    file.close()

    print()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":

    try:
        ancient_text()
    except Exception as error:
        print(f"ERROR: {error}")
