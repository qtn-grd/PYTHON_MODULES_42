#!/usr/bin/env python3


class Plant:
    """A simple object representing a plant that can grow and age."""

    def __init__(self, name: str, height: int, days_old: int) -> None:
        """Initialize the plant with a name, height, and age."""
        self.name = name
        self.height = height
        self.old = days_old

    def age(self, x: int) -> None:
        """Increase the plant's age by a given number of days."""
        self.old += x

    def grow(self, y: int) -> None:
        """Increase the plant's height by a given amount."""
        self.height += y

    def get_info(self) -> None:
        """Display the current information of the plant."""
        print(f"{self.name}: {self.height}cm, {self.old} days old")


rose = Plant("Rose", 25, 30)
time = 6

if __name__ == "__main__":

    print("=== Day 1 ===")
    rose.get_info()
    rose.age(time)
    rose.grow(time)
    print("=== Day", 1 + time, "===")
    rose.get_info()
    print(f"Growth this week: +{time} cm")
