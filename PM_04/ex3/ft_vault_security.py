#!/usr/bin/env python3

import sys


def vault_security() -> None:
    """Perform secure archive extraction and preservation using
    context managers to guarantee automatic file sealing."""

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print()

    print()
    print("SECURE EXTRACTION:")

    try:
        with open("classified_data.txt", "r") as data_one:
            content_one: str = data_one.read()
            print(content_one)
    except FileNotFoundError as error:
        raise FileNotFoundError(
            "Missing file. Add classified_data.txt to repository."
        ) from error
    except OSError as error:
        raise OSError(
            "Failed to access file."
        ) from error

    print()

    print("SECURE PRESERVATION:")

    try:
        with open("new_security.txt", "w") as vault:
            vault.write("[CLASSIFIED] New security protocols archived")
    except PermissionError as error:
        raise PermissionError(
            "Unauthorized procedure. Cannot write to new_security.txt."
        ) from error
    except OSError as error:
        raise OSError(
            "Failed to access file."
        ) from error

    try:
        with open("new_security.txt", "r") as data_two:
            content_two: str = data_two.read()
            print(content_two)
    except FileNotFoundError as error:
        raise FileNotFoundError(
            "Missing file. Add new_security.txt to repository."
        ) from error
    except OSError as error:
        raise OSError(
            "Failed to access file."
        ) from error

    print()

    print("Vault automatically sealed upon completion")

    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    try:
        vault_security()
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
