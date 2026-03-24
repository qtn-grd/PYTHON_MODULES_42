import sys
import os
import site


def outside_construct() -> None:
    """
    Display information and instructions when running outside
    a virtual environment.
    """

    print()
    print("MATRIX STATUS: You're still plugged in")
    print()

    print("Current Python:", sys.executable)
    print("Virtual Environment: None detected")

    print()

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")

    print()

    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate    # On Windows")

    print()

    print("Then run this program again.")


def inside_construct() -> None:
    """
    Display environment details when running inside a virtual environment.
    """

    packages_path = site.getsitepackages()
    env_name = os.path.basename(sys.prefix)

    print()
    print("MATRIX STATUS: Welcome to the construct")
    print()

    print("Current Python:", sys.executable)
    print("Virtual Environment:", env_name)
    print("Environment Path:", sys.prefix)

    print()

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")

    print()

    print("Package installation path:")

    for path in packages_path:
        print(path)


def is_venv() -> bool:
    """
    Determine whether the current Python interpreter is running
    inside a virtual environment.
    """

    return sys.prefix != sys.base_prefix


def main() -> None:
    """
    Entry point of the program. Determines environment and displays
    appropriate information.
    """

    if is_venv():
        inside_construct()
    else:
        outside_construct()


if __name__ == "__main__":
    main()
