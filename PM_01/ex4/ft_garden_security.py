RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"


class Plant:
    """Represents a plant with a name, height (in cm), and age (in days)."""

    def __init__(self, name: str, height: float, age: int) -> None:
        """Initialize a Plant instance."""

        self._name = name.capitalize()
        self._height = height
        self._age = age

    def show(self) -> str:
        """Return a formatted description of the plant."""

        return (f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def get_height(self) -> float:
        """Get the current height."""

        return self._height

    def get_age(self) -> int:
        """Get the current age."""

        return self._age

    def set_height(self, new_height: float) -> None:
        """Safely update the plant height."""

        if new_height >= 0.0:
            self._height = new_height
            print(f"{GREEN}Height updated: {self.get_height()}cm{RESET}")
        else:
            print(f"{self._name}: {RED}Error, height can't be negative{RESET}")
            print(f"Height update rejected{RESET}")

    def set_age(self, new_age: int) -> None:
        """Safely update the plant age."""

        if new_age >= 0:
            self._age = new_age
            print(f"{GREEN}Age updated: {self.get_age()} days{RESET}")
        else:
            print(f"{self._name}: {RED}Error, age can't be negative{RESET}")
            print("Age update rejected")


def main() -> None:
    """Run a demonstration of the plant security system."""

    print("=== Garden Security System ===")
    print()

    rose = Plant("rose", 15.0, 10)
    print("Plant created:", rose.show())
    print()

    rose.set_height(25.0)
    rose.set_age(30)

    print()

    rose.set_height(-25.0)
    print()
    rose.set_age(-30)

    print()

    print("Current state:", rose.show())


if __name__ == "__main__":
    main()
