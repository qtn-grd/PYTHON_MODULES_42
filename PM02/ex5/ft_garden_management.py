#!/usr/bin/env python3


class GardenError(Exception):
    """Base exceptions for garden-related errors."""


class PlantError(GardenError):
    """Exceptions for plant-related errors."""


class WaterError(GardenError):
    """Exceptions for water-related errors."""


class Plant:
    """A basic plant object."""
    def __init__(self, name: str, water: int, sunlight: int) -> None:
        """Initialize the plant."""
        self.name = name
        self.water = water
        self.sunlight = sunlight


class GardenManager:
    """Garden management system."""

    def __init__(self) -> None:
        """Create an empty garden with empty tank."""
        self.plants: list[Plant] = []
        self.tank: int = 0

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        if not plant.name:
            raise PlantError("Plant name cannot be empty!")
        else:
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")

    def check_tank(self) -> None:
        """Check water quantity."""
        if self.tank < len(self.plants):
            raise GardenError("Not enough water in tank")

    def water_plants(self) -> None:
        """Water all plants."""
        self.check_tank()
        print("Opening watering system")
        try:
            for plant in self.plants:
                plant.water += 1
                self.tank -= 1
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plants_health(self) -> None:
        """Check plants attributes"""

        for plant in self.plants:
            try:
                if plant.water < 1:
                    raise WaterError(f"Water level {plant.water} "
                                     f"is too low (min 1)")
                if plant.water > 10:
                    raise WaterError(f"Water level {plant.water} "
                                     f"is too high (max 10)")
                if plant.sunlight < 2:
                    raise PlantError(f"Sunlight hours {plant.sunlight} "
                                     f"is too low (min 2)")
                if plant.sunlight > 12:
                    raise PlantError(f"Sunlight hours {plant.sunlight} "
                                     f"is too high (max 12)")
                print(f"{plant.name}: healthy "
                      f"(water: {plant.water}, sun: {plant.sunlight})")
            except GardenError as error:
                print(f"Error checking {plant.name}: {error}")


def test_garden_management() -> None:
    """Check GardenManager efficiency."""

    print("=== Garden Management System ===")
    print()

    garden = GardenManager()
    garden.tank = 3

    print("Adding plants to garden...")

    plants = [
        Plant("tomato", 4, 8),
        Plant("lettuce", 14, 5),
        Plant("", 5, 5)
    ]

    for plant in plants:
        try:
            garden.add_plant(plant)
        except PlantError as error:
            print(f"Error adding plant: {error}")

    print()

    print("Watering plants...")
    try:
        garden.water_plants()
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print()

    print("Checking plant health...")
    garden.check_plants_health()

    print()
    print("Testing error recovery...")
    try:
        garden.water_plants()
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print("System recovered and continuing...")

    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
