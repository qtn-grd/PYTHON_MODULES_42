#!/usr/bin/env python3


class Plant:
    """A basic plant object that can grow."""
    def __init__(self, name: str, height: int) -> None:
        """Initialize the plant with a name and a height."""
        self.name = name
        self.height = height

    def grow(self, y: int) -> None:
        """Increase the plant height by y."""
        self.height += y

    def get_info(self) -> None:
        """Display the plant information."""
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """A colored plant that can grow and display blooming information."""
    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize the plant and set its flower color."""
        super().__init__(name, height)
        self.color = color

    def get_info(self) -> None:
        """Display the flowering plant information."""
        print(f"- {self.name}: {self.height}cm, "
              f"{self.color} flowers(blooming)")


class PrizeFlower(FloweringPlant):
    """A flowering plant that also has prize points."""
    def __init__(self, name: str, height: int, color: str, score: int) -> None:
        """Initialize the prize flower with a score value."""
        super().__init__(name, height, color)
        self.score = score

    def get_info(self) -> None:
        """Display the prize flower information."""
        print(f"- {self.name}: {self.height}cm, "
              f"{self.color} flowers(blooming), "
              f"Prize points: {self.score}")


class Garden:
    """A garden that can store multiple plants and manage their growth."""
    def __init__(self, player: str) -> None:
        """Create an empty garden for a given player."""
        self.player = player
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.player}'s Garden")

    def grow_all(self, y: int) -> None:
        """Grow all plants in the garden by y."""
        print(f"{self.player} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(y)
            print(f"---> {plant.name} grew {y}cm")

    def report(self) -> None:
        """Display a report of all plants in the garden."""
        print(f"=== {self.player}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.get_info()


class GardenManager:
    """A manager that can handle multiple gardens and compute analytics."""
    def __init__(self) -> None:
        """Create an empty list of gardens."""
        self.gardens: list[Garden] = []

    def add_garden(self, garden: Garden) -> None:
        """Add a garden to the manager."""
        self.gardens.append(garden)

    def report_gardens(self) -> None:
        """Display reports and statistics for all managed gardens."""
        for garden in self.gardens:
            print()
            garden.report()
            print()
            self.show_garden_stats(garden)
            print()
            height = GardenManager.GardenStats.total_growth(garden)
            print(f"Height validation test: "
                  f"{GardenManager.is_valid_height(height)}")
            print()

    def show_garden_stats(self, garden: Garden) -> None:
        """Display statistics for a single garden."""
        count = self.GardenStats.count_plants(garden)
        growth = self.GardenStats.total_growth(garden)
        regular, flowering, prize = self.GardenStats.type_list(garden)
        print(f"Plants added: {count}, Total growth: {growth} cm")
        print(f"Plants types: {regular} regular, "
              f"{flowering} flowering, {prize} prize flowers")

    def compute_garden_score(self, garden: Garden) -> int:
        """Compute and return the score of a garden."""
        score = 0
        for plant in garden.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.score
        return score

    def show_garden_scores(self) -> None:
        """Display the score of each garden."""
        print("  ------------- ")
        print("| Garden scores |")
        print("  ------------- \n")
        for garden in self.gardens:
            score = self.compute_garden_score(garden)
            print(f"- {garden.player}: {score}")

    def is_valid_height(height: int) -> bool:
        """Return True if the given height value is valid."""
        return height >= 0
    is_valid_height = staticmethod(is_valid_height)

    def create_garden_network(cls):
        """Create and return a manager pre-filled with sample gardens."""
        manager = cls()

        alice = Garden("Alice")
        alice.add_plant(Plant("Oak Tree", 100))
        alice.add_plant(FloweringPlant("Rose", 25, "red"))
        alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
        print()
        bob = Garden("Bob")
        bob.add_plant(Plant("Pine Tree", 80))
        bob.add_plant(FloweringPlant("Tulip", 30, "pink"))
        manager.add_garden(alice)
        manager.add_garden(bob)
        return manager
    create_garden_network = classmethod(create_garden_network)

    class GardenStats:
        """A helper class providing statistics for gardens."""
        def count_plants(garden) -> int:
            """Return the number of plants in the given garden."""
            return len(garden.plants)
        count_plants = staticmethod(count_plants)

        def total_growth(garden) -> int:
            """Return the total height of all plants in the given garden."""
            height = 0
            for plant in garden.plants:
                height += plant.height
            return height
        total_growth = staticmethod(total_growth)

        def type_list(garden) -> tuple[int, int, int]:
            """Return counts of regular, flowering, and prize flowers."""
            regular = flowering = prize = 0
            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize
        type_list = staticmethod(type_list)


if __name__ == "__main__":

    print("=== Garden Management System Demo ===")
    print()
    manager = GardenManager.create_garden_network()
    print()
    for garden in manager.gardens:
        garden.grow_all(1)
        print()
    manager.report_gardens()
    print()
    manager.show_garden_scores()
    print()
    print(f"Total gardens managed: {len(manager.gardens)}")
