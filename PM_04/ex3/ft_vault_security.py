from typing import Optional


def secure_archive(
        file_name: str,
        mode: str,
        to_write: Optional[str] = None
) -> tuple[bool, str]:
    """Safely read from or write to a file."""

    if mode not in ["r", "w"]:
        return (False, "Invalid file mode.")

    if mode == "w" and to_write is None:
        return (False, "Missing content to write.")

    try:
        with open(file_name, mode) as my_file:
            if mode == "w":
                my_file.write(to_write)
                return (True, "Content successfully written to file.")
            else:
                return (True, my_file.read())

    except OSError as error:
        return (False, str(error))


def main() -> None:
    """Run archive security tests."""

    print("=== Cyber Archives Security ===")
    print()

    print("Using 'secure_archive' with wrong mode:")
    print(secure_archive("mode_error.txt", "a"))
    print()

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("foo.txt", "r"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("forbidden.txt", "r"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("regular.txt", "r"))
    print()

    to_write = ("[FRAGMENT 001] Digital preservation protocols "
                "established 2087\n"
                "[FRAGMENT 002] Knowledge must survive "
                "the entropy wars\n"
                "[FRAGMENT 003] Every byte saved "
                "is a victory against oblivion\n")

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "w", to_write))
    print()


if __name__ == "__main__":
    main()
