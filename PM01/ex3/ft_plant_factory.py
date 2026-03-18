#!/usr/bin/env python3


class Plant:
    """A plant object that can grow and age over time."""

    def __init__(self, name: str, height: int, days_old: int) -> None:
        """Initialize the plant with a name, height, and age in days."""
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


class Factory:
    """A factory class responsible for creating and storing plant objects."""

    def __init__(self) -> None:
        """Create an empty garden to store plants."""
        self.garden: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        self.garden.append(plant)


if __name__ == "__main__":

    print("=== Plant Factory Output ===")
    addnew = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 20)
    ]

    factory = Factory()
    garden = factory.garden

    for name, height, days in addnew:
        factory.add_plant(Plant(name, height, days))

    for plant in garden:
        print(f"Created: {plant.name} ({plant.height}cm, "
              f"{plant.old} days)")

    print()
    print(f"Total plants created: {len(garden)}")
