#!/usr/bin/env python3


class Plant:
    """A simple object representing a plant that can grow and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant with a name, height, and age."""
        self.name = name
        self.height = height
        self.age = age


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)
garden = [rose, sunflower, cactus]

if __name__ == "__main__":

    print("=== Garden Plant Registry ===")
    for plant in garden:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
