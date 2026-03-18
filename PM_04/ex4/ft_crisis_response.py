#!/usr/bin/env python3

import sys


def crisis_manager(filename: str) -> None:
    """Attempt to open and read a file while handling access-related
    errors gracefully using secure crisis protocols."""

    try:
        with open(filename, "r") as archive:
            content: str = archive.read()
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
            print("SUCCESS: Archive recovered - Knowledge preserved for "
                  "humanity")
            print(content)
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...",
              file=sys.stderr)
        print("RESPONSE: Archive not found in storage matrix",
              file=sys.stderr)
        print("STATUS: Crisis handled, system stable",
              file=sys.stderr)

    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...",
              file=sys.stderr)
        print("RESPONSE: Security protocols deny access",
              file=sys.stderr)
        print("STATUS: Crisis handled, security maintained",
              file=sys.stderr)

    except OSError:
        print("RESPONSE: Unidentified anomaly detected",
              file=sys.stderr)
        print("STATUS: Emergency protocols activated. Music on",
              file=sys.stderr)
        print()
        print("\t~ It's the end of the world as we know it... ~",
              file=sys.stderr)


def crisis_response() -> None:
    """Simulate multiple archive access scenarios to validate
    crisis response handling."""

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()

    crisis_manager("lost_archive.txt")
    print()

    crisis_manager("classified_vault.txt")
    print()

    crisis_manager(".")
    print()

    crisis_manager("standard_archive.txt")
    print()

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_response()
