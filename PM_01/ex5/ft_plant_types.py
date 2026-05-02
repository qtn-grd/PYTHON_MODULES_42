YELLOW = "\033[33m"
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

    def grow(self, growing: float) -> None:
        """Increase the plant's height."""

        self._height += growing

    def grow_older(self, aging: int) -> None:
        """Increase the plant's age."""

        self._age += aging


class Flower(Plant):
    """Represents a flower with a color and blooming state."""
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            color: str,
            bloomed: bool
    ) -> None:
        """Initialize a Flower instance."""

        super().__init__(name, height, age)
        self._color = color
        self._bloomed = bloomed

    def make_bloom(self) -> None:
        """Active flower blooming."""

        self._bloomed = True

    def bloom_status(self) -> str:
        """Return the blooming status of the flower."""

        if self._bloomed:
            return (f"{self._name} is blooming beautifully!")
        else:
            return (f"{self._name} has not bloomed yet")


class Tree(Plant):
    """Represents a tree with a trunk diameter."""

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            diameter: float,
    ) -> None:
        """Initialize a Tree instance."""

        super().__init__(name, height, age)
        self._diameter = diameter

    def shade(self) -> str:
        """Return a description of the shade produced by the tree."""

        return (f"Tree {self._name} now produces a shade of "
                f"{self._height}cm long and {self._diameter}cm wide")


class Vegetable(Plant):
    """Represents a vegetable with a harvest season and nutritional value."""

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            season: str,
            nutrit: int
    ) -> None:
        """Initialize a Vegetable instance."""

        super().__init__(name, height, age)
        self._season = season.capitalize()
        self._nutrit = nutrit

    def grow_older(self, aging: int) -> None:
        """Increase age and nutritional value."""

        super().grow_older(aging)
        self._nutrit += aging


def flower_test() -> None:
    """Test Flower behavior and display output."""

    print("=== Flower")
    print()

    rose = Flower("rose", 15.0, 10, "red", False)
    print(rose.show())
    print(f" Color: {rose._color}")
    print(f" {rose.bloom_status()}")

    print()
    print(f"{YELLOW}[asking the rose to bloom]{RESET}")
    print()

    rose.make_bloom()
    print(rose.show())
    print(f" Color: {rose._color}")
    print(f" {rose.bloom_status()}")


def tree_test() -> None:
    """Test Tree behavior and display output."""

    print("=== Tree")
    print()

    oak = Tree("oak", 200.0, 365, 5.0)
    print(oak.show())
    print(f" Trunk diameter: {oak._diameter}cm")

    print()
    print(f"{YELLOW}[asking the oak to produce shade]{RESET}")
    print()

    print(f" {oak.shade()}")


def vegetable_test() -> None:
    """Test Vegetable behavior and display output."""

    print("=== Vegetable")
    print()

    tomato = Vegetable("tomato", 5.0, 10, "april", 0)
    print(tomato.show())
    print(f" Harvest season: {tomato._season}")
    print(f" Nutritional value: {tomato._nutrit}")

    print()
    print(f"{YELLOW}[make tomato grow and age for 20 days]{RESET}")
    print()

    tomato.grow(42)
    tomato.grow_older(20)
    print(tomato.show())
    print(f" Harvest season: {tomato._season}")
    print(f" Nutritional value: {tomato._nutrit}")


def main():
    """Run all plant type demonstrations."""

    print("=== Garden Plant Types ===")
    print()

    print()
    flower_test()
    print()

    print()
    tree_test()
    print()

    print()
    vegetable_test()
    print()


if __name__ == "__main__":
    main()
