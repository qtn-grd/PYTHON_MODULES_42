from typing import Dict, Any
from ex0.Card import Card, CardError
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCardError(Exception):
    """Custom exception for TournamentCard errors."""
    pass


class TournamentCard(Card, Combatable, Rankable):
    """
    A card that can participate in a tournament.
    Combines combat abilities and ranking system.

    Attributes:
        _attack (int): Attack value of the card.
        wins (int): Number of wins recorded.
        losses (int): Number of losses recorded.
        rating (int): Current rating of the card.
    """

    def __init__(
            self, name: str,
            cost: int, rarity: str,
            attack: int, rating: int
            ) -> None:
        """
        Initializes a TournamentCard with combat and ranking attributes.

        Args:
            name (str): Name of the card.
            cost (int): Mana or resource cost to play the card.
            rarity (str): Card rarity classification.
            attack (int): Combat attack value.
            rating (int): Initial tournament rating.

        Raises:
            TournamentCardError: If parent Card initialization fails.
        """

        try:
            super().__init__(name, cost, rarity)
        except CardError as error:
            raise TournamentCardError(str(error))

        self._attack: int = attack
        self.wins: int = 0
        self.losses: int = 0
        self.rating: int = rating

    def attack(self, target: Any) -> Dict[str, Any]:
        """
        Performs an attack on a target card.

        Args:
            target (Any): Target card object to attack. Must have '_name'
            attribute.

        Returns:
            Dict[str, Any]: Dictionary containing attacker name,
            target name, and damage dealt.

        Raises:
            TournamentCardError: If attacker or target is missing required
            attributes.
        """

        try:
            if not hasattr(self, "_attack"):
                raise TournamentCardError("Attacker has no attack value")

            if not hasattr(target, "_name"):
                raise TournamentCardError("Target has no name")

            damage: int = self._attack
            target_name: str = target._name

            return {
                "attacker": self._name,
                "target": target_name,
                "damage": damage
            }

        except TournamentCardError as error:
            raise error

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Plays the card in a game context.

        Args:
            game_state (Dict[str, Any]): Current game state (not used here).

        Returns:
            Dict[str, Any]: Dictionary with card played name and cost.
        """

        return {
            "card_played": self._name,
            "cost": self._cost
        }

    def calculate_rating(self) -> int:
        """
        Returns the current tournament rating of the card.

        Returns:
            int: Current rating value.
        """

        return self.rating

    def update_wins(self, wins: int) -> None:
        """
        Updates the number of wins and increases rating accordingly.

        Args:
            wins (int): Number of wins to add.
        """

        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        """
        Updates the number of losses and decreases rating accordingly.

        Args:
            losses (int): Number of losses to add.
        """

        self.losses += losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> Dict[str, int]:
        """
        Returns ranking information.

        Returns:
            Dict[str, int]: Dictionary with 'rating', 'wins', and 'losses'.
        """

        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def defend(self, incoming_damage: int) -> dict:
        """
        Reduces health when receiving damage.

        Args:
            incoming_damage (int): Amount of damage to apply.

        Returns:
            dict: Dictionary with defender name, damage taken,
            and remaining health.
        """

        self.health -= incoming_damage

        return {
            "defender": self._name,
            "damage_taken": incoming_damage,
            "remaining_health": self.health
        }

    def get_combat_stats(self) -> dict:
        """
        Returns the card's combat statistics.

        Returns:
            dict: Dictionary with 'attack' and current 'health' values.
        """

        return {
            "attack": self._attack,
            "health": self.health
        }

    def get_tournament_stats(self) -> Dict[str, int]:
        """
        Returns the card's tournament statistics.

        Returns:
            Dict[str, int]: Dictionary containing rating, wins, and losses.
        """

        return self.get_rank_info()
