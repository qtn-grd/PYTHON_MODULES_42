from typing import List
from ex4.TournamentPlatform import TournamentPlatform, TournamentPlatformError
from ex4.TournamentCard import TournamentCard, TournamentCardError
import sys


def main() -> None:
    """
    Demonstrates the DataDeck Tournament Platform.

    Steps performed:
    1. Initializes the tournament platform.
    2. Creates and registers tournament cards with the platform.
    3. Displays card information including interfaces, rating, and record.
    4. Simulates a tournament match between two cards and shows the results.
    5. Generates and displays the leaderboard sorted by rating.
    6. Generates a platform report summarizing total cards, matches played,
       average rating, and platform status.
    7. Handles errors gracefully to prevent crashes during card registration,
       match simulation, leaderboard generation, and report creation.

    Output:
        Printed tournament progress, match results, leaderboard, and
        platform report to the console.
    """

    print()
    print("=== DataDeck Tournament Platform ===")
    print()

    platform = TournamentPlatform()

    print("Registering Tournament Cards...")
    print()

    try:
        card1 = TournamentCard("Fire Dragon", 5, "Epic", 50, 1200)
        card2 = TournamentCard("Ice Wizard", 4, "Rare", 30, 1150)
    except (TypeError, TournamentCardError) as error:
        print(f"Error creating cards: {error}", file=sys.stderr)
        return

    try:
        id1: str = platform.register_card(card1)
        id2: str = platform.register_card(card2)

        ids: List[str] = [id1, id2]

        for id in ids:
            card = platform.cards.get(id)

            if card is None:
                continue

            parents = [
                base.__name__ for base in card.__class__.__bases__
            ]
            parents_str = ", ".join(parents)

            print(f"{card._name} (ID: {id}):")
            print(f"- Interfaces: [{parents_str}]")
            print(f"- Rating: {card.rating}")
            print(f"- Record: {card.wins}-{card.losses}")
            print()

    except TournamentPlatformError as error:
        print(f"Error registering cards: {error}", file=sys.stderr)
        return

    print("Creating tournament match...")

    try:
        result = platform.create_match(id1, id2)

        if "draw" in result:
            print(
                f"Match result: Draw between "
                f"{result['card1']} and {result['card2']}"
            )
            print(
                f"Ratings: {result['card1_rating']} - "
                f"{result['card2_rating']}"
            )
        else:
            print(
                "Match result: "
                f"{{'winner': '{result['winner']}', "
                f"'loser': '{result['loser']}', "
                f"'winner_rating': {result['winner_rating']}, "
                f"'loser_rating': {result['loser_rating']}}}"
            )

    except (TypeError, TournamentPlatformError) as error:
        print(f"Error during match: {error}", file=sys.stderr)
        return

    print()
    print("Tournament Leaderboard:")

    try:
        leaderboard = platform.get_leaderboard()

        for position, card in enumerate(leaderboard, start=1):
            print(
                f"{position}. {card._name} - Rating: {card.rating} "
                f"({card.wins}-{card.losses})"
            )
    except TournamentPlatformError as error:
        print(f"Error generating leaderboard: {error}", file=sys.stderr)

    print()
    print("Platform Report:")

    try:
        report = platform.generate_tournament_report()
        print(report)
    except Exception as error:
        print(f"Error generating tournament report: {error}", file=sys.stderr)
        report = {"total_cards": 0, "matches_played": 0, "avg_rating": 0,
                  "platform_status": "error"}

    print()
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
