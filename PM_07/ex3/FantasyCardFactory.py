from typing import Any, Optional, Dict, List, Union
from ex0.Card import CardError
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import DeckError
from ex3.CardFactory import CardFactory
import random


class FantasyCardFactory(CardFactory):
    """
    Concrete factory for creating fantasy-themed cards.

    Supports creation of creatures (dragons, goblins),
    spells (fire, ice, lightning), and magical artifacts
    (rings, staffs, crystals).
    """

    def __init__(self) -> None:
        """
        Initializes available card types and mapping by category.
        """

        self.creature_types: List[str] = ["Fire Dragon", "Goblin Warrior",
                                          "Shaman Ork"]
        self.spell_types: List[str] = ["Fireball", "Ice Shard",
                                       "Lightning Bolt"]
        self.artifact_types: List[str] = ["Mana Ring", "Mystic Staff",
                                          "Crystal Orb"]

        self.supported_types: Dict[str, List[str]] = {
            "creatures": self.creature_types,
            "spells": self.spell_types,
            "artifacts": self.artifact_types
        }

    def create_creature(
            self, name_or_power: Optional[Union[str, int]] = None
            ) -> CreatureCard:
        """
        Creates a fantasy creature card with randomized stats.
        """

        name: str = name_or_power if isinstance(
            name_or_power, str) else random.choice(self.creature_types)

        cost: int = name_or_power if isinstance(
            name_or_power, int) else random.randint(1, 5)

        attack: int = random.randint(1, 8)
        health: int = random.randint(3, 12)

        rarities: List[str] = ["Common", "Uncommon", "Rare", "Epic",
                               "Legendary"]
        rarity: str = random.choice(rarities)

        try:
            return CreatureCard(name, cost, rarity, attack, health)
        except CardError as error:
            raise error

    def create_spell(
            self, name_or_power: Optional[Union[str, int]] = None
            ) -> SpellCard:
        """
        Creates a fantasy-themed spell card.
        """

        name: str = str(name_or_power) if isinstance(
            name_or_power, str) else random.choice(self.spell_types)

        cost: int = name_or_power if isinstance(
            name_or_power, int) else random.randint(1, 5)

        rarities: List[str] = ["Common", "Uncommon",
                               "Rare", "Epic", "Legendary"]
        rarity: str = random.choice(rarities)

        effect: str = random.choice(["damage", "heal", "buff", "debuff"])

        try:
            return SpellCard(name, cost, rarity, effect)
        except CardError as error:
            raise error

    def create_artifact(
            self, name_or_power: Optional[Union[str, int]] = None
            ) -> ArtifactCard:
        """
        Creates a fantasy-themed artifact card.
        """

        name: str = str(name_or_power) if isinstance(
            name_or_power, str) else random.choice(self.artifact_types)

        cost: int = name_or_power if isinstance(
            name_or_power, int) else random.randint(1, 5)

        rarities: List[str] = ["Common", "Uncommon",
                               "Rare", "Epic", "Legendary"]
        rarity: str = random.choice(rarities)

        durability: int = random.randint(1, 5)
        effect: str = random.choice(["+1 mana per turn", "+2 attack",
                                     "heal 3 HP", "draw 1 card"])
        try:
            return ArtifactCard(name, cost, rarity, durability, effect)
        except CardError as error:
            raise error

    def create_themed_deck(self, size: int) -> Dict[str, List[Any]]:
        """
        Generates a deck with a mix of creatures, spells, and artifacts.
        """

        deck: Dict[str, List[Any]] = {"creatures": [], "spells": [],
                                      "artifacts": []}

        try:
            for _ in range(size):
                card_type: str = random.choice(
                    ["creature", "spell", "artifact"])
                if card_type == "creature":
                    deck["creatures"].append(self.create_creature())
                elif card_type == "spell":
                    deck["spells"].append(self.create_spell())
                elif card_type == "artifact":
                    deck["artifacts"].append(self.create_artifact())
        except DeckError as error:
            raise error

        return deck

    def get_supported_types(self) -> Dict[str, type]:
        """
        Returns the classes of cards supported by this factory.
        """

        return self.supported_types
