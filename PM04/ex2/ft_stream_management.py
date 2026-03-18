#!/usr/bin/env python3

import sys


# def stream_management_alternate() -> None:
#     """Manages the three sacred streams: input, stdout, stderr."""

#     print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
#     print()

#     print("Input Stream active. Enter archivist ID: ", end="", flush=True)
#     archivist_id: str = sys.stdin.readline().rstrip("\n")

#     print("Input Stream active. Enter status report: ", end="", flush=True)
#     status_report: str = sys.stdin.readline().rstrip("\n")

#     print()
#     print("[STANDARD] Archive status from "
#           f"{archivist_id}: {status_report}", file=sys.stdout)
#     print("[ALERT] System diagnostic: Communication channels "
#           "verified", file=sys.stderr)
#     print("[STANDARD] Data transmission complete", file=sys.stdout)

#     print()
#     print("Three-channel communication test successful.")


def stream_management() -> None:
    """Manages the three sacred streams: input, stdout, stderr."""

    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()

    archivist_id: str = input("Input Stream active. Enter archivist ID: ")
    status_report: str = input("Input Stream active. Enter status report: ")

    print()
    print("[STANDARD] Archive status from "
          f"{archivist_id}: {status_report}", file=sys.stdout)
    print("[ALERT] System diagnostic: Communication channels "
          "verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)

    print()
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    stream_management()
