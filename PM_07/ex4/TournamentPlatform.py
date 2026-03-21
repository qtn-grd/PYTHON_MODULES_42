from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatformError(Exception):
    """Custom exception for TournamentPlatform-related errors."""
    pass


class TournamentPlatform:
    """
    Manages tournament cards, matches, and leaderboard.

    Attributes:
        cards (Dict[str, TournamentCard]): Registered tournament cards
        keyed by unique ID.
        matches_played (int): Total number of matches played
        on the platform.
    """

    def __init__(self) -> None:
        """
        Initializes an empty tournament platform with no cards
        or matches played.
        """

        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        """
        Registers a TournamentCard and generates a unique ID for it.

        Args:
            card (TournamentCard): Card to register.

        Returns:
            str: Unique ID assigned to the card.

        Raises:
            TournamentPlatformError: If the card is not a TournamentCard
                                     or if the generated ID already exists.
        """

        if not isinstance(card, TournamentCard):
            raise TournamentPlatformError("Invalid card type")

        words = card._name.lower().split()
        temp_id: str = words[-1] if words else "card"
        final_id: str = f"{temp_id}_{len(self.cards)+1:03}"

        if final_id in self.cards:
            raise TournamentPlatformError("Card ID already exists")

        self.cards[final_id] = card

        return final_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """
        Simulates a match between two registered cards.

        Args:
            card1_id (str): ID of the first card.
            card2_id (str): ID of the second card.

        Returns:
            dict: Match outcome with winner/loser IDs and updated ratings.
                  If a draw occurs, contains 'draw':
                  True and both card ratings.

        Raises:
            TournamentPlatformError: If either card is not found
            or missing attack value.
        """

        if card1_id not in self.cards or card2_id not in self.cards:
            raise TournamentPlatformError("Card not found")

        first_card: TournamentCard = self.cards[card1_id]
        second_card: TournamentCard = self.cards[card2_id]

        try:
            if not hasattr(first_card, "_attack") or not hasattr(
                    second_card, "_attack"):
                raise TournamentPlatformError("Missing attack attribute")

            attack1 = first_card._attack
            attack2 = second_card._attack

            self.matches_played += 1

            if attack1 > attack2:
                first_card.update_wins(1)
                second_card.update_losses(1)

                return {
                    "winner": card1_id,
                    "loser": card2_id,
                    "winner_rating": first_card.calculate_rating(),
                    "loser_rating": second_card.calculate_rating()
                }

            elif attack2 > attack1:
                second_card.update_wins(1)
                first_card.update_losses(1)

                return {
                    "winner": card2_id,
                    "loser": card1_id,
                    "winner_rating": second_card.calculate_rating(),
                    "loser_rating": first_card.calculate_rating()
                }

            else:
                return {
                    "draw": True,
                    "card1": card1_id,
                    "card2": card2_id,
                    "card1_rating": first_card.calculate_rating(),
                    "card2_rating": second_card.calculate_rating()
                }

        except Exception as error:
            raise TournamentPlatformError(f"Match error: {error}")

    def get_leaderboard(self) -> List[TournamentCard]:
        """
        Returns all registered cards sorted by rating in descending order.

        Returns:
            List[TournamentCard]: Cards sorted from highest to lowest rating.
        """

        cards_list: List[TournamentCard] = list(self.cards.values())

        for i in range(len(cards_list)):
            for j in range(i + 1, len(cards_list)):
                if cards_list[j].rating > cards_list[i].rating:
                    cards_list[i], cards_list[j] = cards_list[j], cards_list[i]

        return cards_list

    def generate_tournament_report(self) -> dict:
        """
        Generates a summary report of the tournament platform.

        Returns:
            dict: Contains total cards, matches played, average rating,
            and platform status.
        """

        avg_rating: int

        if not self.cards:
            avg_rating = 0
        else:
            sum_rating = sum(
                card.rating for card in self.cards.values())
            avg_rating = sum_rating // len(self.cards)

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
