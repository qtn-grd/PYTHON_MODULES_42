from typing import Any
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """
    A strategy focused on aggressive play.

    Plays low-cost cards quickly and prioritizes dealing damage
    to enemy targets.
    """

    def execute_turn(
            self, hand: list[Any], battlefield: list[Any]
    ) -> dict[str, Any]:
        """
        Executes an aggressive turn by playing cards and attacking directly.

        Args:
            hand (list[Any]): Cards available to play.
            battlefield (list[Any]): Cards already in play.

        Returns:
            dict[str, Any]: Summary of the turn.
        """
        cards_played: list[str] = []
        mana_used: int = 0
        damage_dealt: int = 0

        for card in hand:
            if hasattr(card, "_cost") and card._cost <= 5:
                cards_played.append(card._name)
                mana_used += card._cost

                if hasattr(card, "_attack"):
                    damage_dealt += card._attack
                elif hasattr(card, "effect") and card._effect == "damage":
                    damage_dealt += card.cost

        targets = self.prioritize_targets(battlefield)
        if not targets:
            targets = ["Enemy Player"]

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        """
        Returns the name of the strategy.
        """
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        """
        Selects creature targets with low health first.

        Args:
            available_targets (list[Any]): Cards in play that may be attacked.

        Returns:
            list[Any]: Ordered list of prioritized targets.
        """
        creatures: list[Any] = [
            targ for targ in available_targets if hasattr(targ, "_health")]
        weak_creatures: list[Any] = [
            creat for creat in creatures if creat._health < 5]

        return weak_creatures if weak_creatures else creatures
