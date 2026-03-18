#!/usr/bin/env python3


class Plant:
    """A plant object that can grow and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant with a name, height, and age."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        """Display the current information of the plant."""
        print(f"Current plant: {self.name} ({self.height}cm, "
              f"{self.age} days)")


class Flower(Plant):
    """A flowering plant that can grow, age, and bloom."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize the flower with a color attribute."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Make the flower bloom beautifully."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """A plant that can grow, age, and provide shade."""

    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            trunk_diameter: int
    ) -> None:
        """Initialize the tree with a trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Generate shade based on the trunk diameter."""
        print(f"{self.name} provides {self.trunk_diameter * 1.56} "
              f"square meters of shade")


class Vegetable(Plant):
    """A seasonal plant that can grow, age, and provide nutrition."""

    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutritional_value: str
    ) -> None:
        """Initialize the vegetable with harvest season and nutrition data."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutrition(self) -> None:
        """Display the nutritional value of the vegetable."""
        print(f"{self.name} is rich in {self.nutritional_value}")


rose = Flower("Rose", 25, 30, "red")
mimosa = Flower("Mimosa", 20, 27, "yellow")

oak = Tree("Oak", 500, 1825, 50)
fir_tree = Tree("Fir tree", 400, 670, 32)

tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
carrot = Vegetable("Carrot", 70, 50, "autumn", "vitamin A")


if __name__ == "__main__":

    print("=== Garden Plant Type ===")
    print()

    print(f"{rose.name} ({rose.__class__.__name__}): {rose.height}cm, "
          f"{rose.age} days, {rose.color} color")
    rose.bloom()
    print()

    print(f"{mimosa.name} ({mimosa.__class__.__name__}): {mimosa.height}cm, "
          f"{mimosa.age} days, {mimosa.color} color")
    mimosa.bloom()
    print()

    print(f"{oak.name} ({oak.__class__.__name__}): {oak.height}cm, "
          f"{oak.age} days, {oak.trunk_diameter}cm diameter")
    oak.produce_shade()
    print()

    print(f"{fir_tree.name} ({fir_tree.__class__.__name__}): "
          f"{fir_tree.height}cm, {fir_tree.age} days, "
          f"{fir_tree.trunk_diameter}cm diameter")
    fir_tree.produce_shade()
    print()

    print(f"{tomato.name} ({tomato.__class__.__name__}): {tomato.height}cm, "
          f"{tomato.age} days, {tomato.harvest_season} harvest")
    tomato.get_nutrition()
    print()

    print(f"{carrot.name} ({carrot.__class__.__name__}): {carrot.height}cm, "
          f"{carrot.age} days, {carrot.harvest_season} harvest")
    carrot.get_nutrition()
