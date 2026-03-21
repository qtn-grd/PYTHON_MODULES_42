from ex0.Card import Card, CardError
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, SpellCardError
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck, DeckError
import sys


def main() -> None:
    """
    Demonstration script for Exercise 1: Deck Builder.

    Creates a deck containing CreatureCard, SpellCard, and ArtifactCard,
    displays deck statistics, shuffles the deck, draws and plays each card,
    illustrating polymorphism in action.
    """

    print()
    print("=== DataDeck Deck Builder ===")
    print()

    print("Building deck with different card types...")
    print()

    deck: Deck = Deck()

    fire_dragon = None
    lightning_bolt = None
    mana_crystal = None

    try:
        fire_dragon = CreatureCard(
            "Fire Dragon", 6, "Legendary", 4, 5)
    except (CardError, TypeError) as error:
        print(f"Error creating creature card: {error}", file=sys.stderr)

    try:
        lightning_bolt = SpellCard(
            "Lightning Bolt", 3, "Rare", "Deal 3 damage to target")
    except (SpellCardError, TypeError) as error:
        print(f"Error creating spell card: {error}", file=sys.stderr)

    try:
        mana_crystal = ArtifactCard(
            "Mana Crystal", 3, "Uncommon", 3, "+1 mana per turn")
    except (CardError, TypeError) as error:
        print(f"Error creating artifact card: {error}", file=sys.stderr)

    try:
        if fire_dragon is not None and isinstance(fire_dragon, Card):
            deck.add_card(fire_dragon)
        if lightning_bolt is not None and isinstance(lightning_bolt, Card):
            deck.add_card(lightning_bolt)
        if mana_crystal is not None and isinstance(mana_crystal, Card):
            deck.add_card(mana_crystal)
    except DeckError as error:
        print(f"Error adding card to deck: {error}", file=sys.stderr)

    print(f"Deck stats: {deck.get_deck_stats()}")
    print()

    print("Drawing and playing cards:")
    print()

    deck.shuffle()

    num_cards: int = len(deck.cards)

    for _ in range(num_cards):
        try:
            card: Card = deck.draw_card()
            print(f"Drew: {card._name} ({type(card).__name__})")
            print("Play result:", card.play({}))
            print()
        except DeckError as error:
            print(f"Deck operation failed: {error}", file=sys.stderr)
            break

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
