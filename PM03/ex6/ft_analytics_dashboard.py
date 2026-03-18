#!/usr/bin/env python3


def dashboard() -> None:
    """Display a simple analytics dashboard using list, dict,
    and set comprehensions on sample gaming data."""

    players: list[str] = ["alice", "bob", "charlie", "diana"]

    scores: dict[str, int] = {"alice": 2300, "bob": 1800, "charlie": 2150,
                              "diana": 2000}

    achievements: dict[str, list[str]] = {
        "alice": ["first_kill", "level_10", "boss_slayer", "explorer",
                  "collector"],
        "bob": ["first_kill", "level_10", "survivor"],
        "charlie": ["level_10", "boss_slayer", "explorer", "collector",
                    "hunter", "tactical_master", "champion"],
        "diana": ["rich", "level_5", "ghost"]
    }

    regions = {"alice": "north", "bob": "east", "charlie": "central",
               "diana": "north"}

    print("=== Game Analytics Dashboard ===")
    print()

    print("=== List Comprehension Exemples ===")
    print()

    high_scorers: list[str] = [p for p in scores if scores[p] >= 2000]
    print(f"High scorers (>2000): {high_scorers}")

    double_score: list[int] = [scores[p] * 2 for p in scores]
    print(f"Scores doubled: {double_score}")

    active_players: list[str] = [
        p for p in achievements if "level_10" in achievements[p]]
    print(f"Active players: {active_players}")
    print()

    print("=== Dict Comprehension Exemples ===")
    print()

    player_scores: dict[str, int] = {p: scores[p] for p in scores}
    print(f"Player scores: {player_scores}")

    score_cat: dict[str, int] = {
        "high": sum(1 for p in players if scores[p] >= 2000),
        "medium": sum(1 for p in players if 2000 <= scores[p] <= 2250),
        "low": sum(1 for p in players if scores[p] < 2000)
    }
    print(f"Score categories: {score_cat}")

    count_achiev: dict[str, int] = {
        p: len(achievements[p]) for p in achievements}
    print(f"Achievement counts: {count_achiev}")
    print()

    print("=== Set Comprehension Exemples ===")
    print()

    unique_players: set[str] = {p for p in players}
    print(f"Unique players: {sorted(unique_players)}")

    unique_achievements: set[str] = {
        ach for ach_list in achievements.values() for ach in ach_list}
    print(f"Unique achievements: {sorted(unique_achievements)}")

    active_regions: set[str] = {regions[p] for p in regions}
    print(f"Active regions: {sorted(active_regions)}")
    print()

    print("=== Combined Analysis ===")
    print()

    number_players: int = len(players)
    average_score: float = sum(scores[p] for p in scores) / number_players
    top_player: str = max(scores, key=scores.get)

    print(f"Total players: {number_players}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print(f"Average score: {average_score:.1f}")
    print(
        f"Top performer: {top_player} "
        f"({scores[top_player]} points, "
        f"{count_achiev[top_player]} achievements)"
    )


if __name__ == "__main__":
    dashboard()
