YELLOW = "\033[33m"
RESET = "\033[0m"


class Plant:
    """Represents a plant with a name, height (in cm), and age (in days)."""

    def __init__(self, name: str, height: float, age: int) -> None:
        """Initialize a Plant instance."""

        self._name = name.capitalize()
        self._height = height
        self._age = age
        self._stats = Plant.PlantStats()

    class PlantStats:
        """Tracks usage statistics for a Plant instance."""

        def __init__(self) -> None:
            """Initialize all counters to zero."""

            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0
            self._shade_calls = 0

        def display(self) -> str:
            """Return a formatted string of plant statistics."""

            return (f"{self._grow_calls} grow, {self._age_calls} age, "
                    f"{self._show_calls} show")

        def increment_shade(self) -> None:
            """Increment shade generation count"""

            self._shade_calls += 1

        def display_with_shade(self) -> str:
            """Return statistics including shade usage."""

            return (f"{self._grow_calls} grow, {self._age_calls} age, "
                    f"{self._show_calls} show, {self._shade_calls} shade")

    def show(self) -> str:
        """Return a formatted description of the plant."""

        self._stats._show_calls += 1
        return (f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self, growing: float) -> None:
        """Increase the plant's height."""

        self._stats._grow_calls += 1
        self._height += growing

    def grow_older(self, aging: int) -> None:
        """Increase the plant's age."""

        self._stats._age_calls += 1
        self._age += aging

    @staticmethod
    def check_aging(number: int) -> bool:
        """Check if a given age exceeds one year."""

        return number >= 365

    @classmethod
    def create_plant(cls):
        """Create a default plant with unknown characteristics."""

        return cls("unknown plant", 0.0, 0)


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
        """Simulate shade production and update statistics."""

        self._stats.increment_shade()
        return (f"Tree {self._name} now produces a shade of "
                f"{self._height}cm long and {self._diameter}cm wide")


class Seed(Flower):
    """Represents a flower that can produce seeds after blooming."""

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            color: str,
            bloomed: bool
    ) -> None:
        """Initialize a Flower instance."""

        super().__init__(name, height, age, color, bloomed)

    def seeds_quantity(self) -> int:
        """Determine seed count according if flower already bloomed."""

        if not self._bloomed:
            return 0
        return 42

    def show(self) -> str:
        """Return plant info including seed count."""

        return (f"{super().show()}\nSeeds: {self.seeds_quantity()}")


def checking_values() -> None:

    print("=== Check year-old ===")
    print()
    print("Is 30 days more than a year? ->", Plant.check_aging(30))
    print("Is 400 days more than a year? ->", Plant.check_aging(400))


def flower_test() -> None:

    print("=== Flower")
    print()

    rose = Flower("rose", 15.0, 10, "red", False)

    print(rose.show())
    print(f" Color: {rose._color}")
    print(f" {rose.bloom_status()}")
    print()

    print(f"{YELLOW}[statistics for {rose._name}]{RESET}")
    print()
    print(f"Stats: {rose._stats.display()}")
    print()

    print(f"{YELLOW}[asking the rose to grow and bloom]{RESET}")
    print()

    rose.grow(8)
    rose.make_bloom()

    print(rose.show())
    print(f" Color: {rose._color}")
    print(f" {rose.bloom_status()}")
    print()

    print(f"{YELLOW}[statistics for {rose._name}]{RESET}")
    print()
    print(f"Stats: {rose._stats.display()}")


def tree_test() -> None:

    print("=== Tree")
    print()
    oak = Tree("oak", 200.0, 365, 5.0)

    print(oak.show())
    print(f" Trunk diameter: {oak._diameter}cm")
    print()

    print(f"{YELLOW}[statistics for {oak._name}]{RESET}")
    print()
    print(f"Stats: {oak._stats.display_with_shade()}")
    print()

    print(f"{YELLOW}[asking the oak to produce shade]{RESET}")
    print()

    print(f"{oak.shade()}")
    print()

    print(f"{YELLOW}[statistics for {oak._name}]{RESET}")
    print()
    print(f"Stats: {oak._stats.display_with_shade()}")


def seed_test() -> None:

    print("=== Seed")
    print()

    sunflower = Seed("sunflower", 80.0, 45, "yellow", False)

    print(sunflower.show())
    print(f" Color: {sunflower._color}")
    print(f" {sunflower.bloom_status()}")
    print(f"Stats: {sunflower._stats.display()}")
    print()

    print(f"{YELLOW}[make sunflower grow, age and bloom]{RESET}")
    print()

    sunflower.grow(30)
    sunflower.grow_older(20)
    sunflower.make_bloom()

    print(sunflower.show())
    print(f" Color: {sunflower._color}")
    print(f" {sunflower.bloom_status()}")
    print(f" Seeds: {sunflower.seeds_quantity()}")
    print()

    print(f"{YELLOW}[statistics for {sunflower._name}]{RESET}")
    print()
    print(f"Stats: {sunflower._stats.display()}")


def anonymous_test() -> None:

    print("=== Anonymous")
    print()

    unknown = Plant.create_plant()
    print(unknown.show())
    print()

    print(f"{YELLOW}[statistics for {unknown._name}]{RESET}")
    print()
    print(f"Stats: {unknown._stats.display()}")


def main() -> None:

    print("=== Garden statistics ===")
    print()

    print()
    checking_values()
    print()

    print()
    flower_test()
    print()

    print()
    tree_test()
    print()

    print()
    seed_test()
    print()

    print()
    anonymous_test()
    print()


if __name__ == "__main__":
    main()
