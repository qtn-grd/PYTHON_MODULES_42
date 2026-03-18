#!/usr/bin/env python3


class GardenError(Exception):
    """Base exceptions for garden-related errors."""


class PlantError(GardenError):
    """Exceptions for plant-related errors."""


class WaterError(GardenError):
    """Exceptions for water-related errors."""


class Plant:
    """A plant object that can grow and age."""

    def __init__(self, name: str, health: int, water: int) -> None:
        """Initialize the plant with a name, health, and water."""
        self.name = name
        self.health = health
        self.water = water

    @classmethod
    def let_choose_value(cls) -> "Plant":
        """Let user define plant values."""

        try:
            health = int(input("Define tomato's health : "))
            water = int(input("Define tomato's water: "))
        except ValueError:
            print()
            raise GardenError("health and water must be numbers!\n\n"
                              "Please try again :-)\n")
        return cls("tomato", health, water)


def check_health(plant: Plant) -> None:
    """Check if the plant is in a good health."""
    if plant.health <= 0:
        raise PlantError(f"The {plant.name} plant is wilting!")
    if plant.health > 100:
        raise PlantError("Health value out of range")


def check_water(plant: Plant) -> None:
    """Check if the plant has enough water."""
    if plant.water <= 0:
        raise WaterError("Not enough water in the tank!")
    if plant.water > 100:
        raise WaterError("Too much water in the tank!")


def test_error_types(plant: Plant) -> None:
    """Force testing invalid operations"""

    print("=== Custom Garden Error Demo ===")
    print()

    print("Testing PlantError...")
    try:
        check_health(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print()

    print("Testing WaterError...")
    try:
        check_water(plant)
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print()

    print("Testing catching all garden errors...")
    try:
        check_health(plant)
    except GardenError as error:
        print(f"Caught a garden error: {error}")
    try:
        check_water(plant)
    except GardenError as error:
        print(f"Caught a garden error: {error}")
    print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    print()
    try:
        tomato = Plant.let_choose_value()
        print()
        test_error_types(tomato)
    except GardenError as error:
        print()
        print(f"Error: {error}")
