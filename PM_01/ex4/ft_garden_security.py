#!/usr/bin/env python3


class SecurePlant:
    """A secured plant object that can grow and age with validation checks."""

    def __init__(self, name: str, height: int, days_old: int) -> None:
        """Initialize the plant with protected attributes."""
        self._name = name
        self._height = height
        self._old = days_old
        print(f"Plant created: {self._name}")

    def set_height(self, x: int) -> None:
        """Set the plant height with validation."""
        if x < 0:
            print(f"Invalid operation attempted: height {x}cm [REJECTED]\n"
                  f"Security: negative height rejected")
        else:
            self._height = x
            print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, y: int) -> None:
        """Set the plant age with validation."""
        if y < 0:
            print(f"Invalid operation attempted: age {y}days [REJECTED]\n"
                  f"Security: negative age rejected")
        else:
            self._old = y
            print(f"Age updated: {self._old} days [OK]")

    def get_height(self) -> int:
        """Return the current height of the plant."""
        return self._height

    def get_age(self) -> int:
        """Return the current age of the plant."""
        return self._old

    def get_info(self) -> None:
        """Display the current information of the plant."""
        print(f"Current plant: {self._name} ({self.get_height()}cm, "
              f"{self.get_age()} days)")


if __name__ == "__main__":

    print("=== Garden Security System ===")
    plant1 = SecurePlant("Rose", 1, 1)
    plant1.set_height(25)
    plant1.set_age(30)
    print()
    plant1.set_height(-5)
    print()
    plant1.get_info()
