#!/usr/bin/env python3

from typing import TextIO


def archive_creation() -> None:
    """Creates 'new_discovery.txt' and writes three archival entries
    into it while displaying the preservation process."""

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()

    print("Initializing new storage unit: new_discovery.txt")

    file: TextIO

    try:
        file = open("new_discovery.txt", "w")
    except PermissionError as error:
        raise PermissionError(
            "Insufficient permissions to create storage unit."
            ) from error
    except OSError as error:
        raise OSError(
            "Storage unit initialization failed."
            ) from error

    print("Storage unit created successfully...")
    print()

    print("Inscribing preservation data...")

    text: list[str] = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
        ]

    for line in text:
        file.write(line + "\n")
        print(line)

    file.close()
    print()
    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":

    try:
        archive_creation()
    except Exception as error:
        print(f"ERROR: {error}")
