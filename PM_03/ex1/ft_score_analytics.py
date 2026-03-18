#!/usr/bin/env python3

import sys


def score_cruncher() -> None:
    """Compare scores found in command-line arguments."""
    print("=== Player Score Analytics ===")
    arguments: list[str] = sys.argv[1:]

    if not arguments:
        print()
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
        return

    else:
        scores: list[int] = []
        negatives: int = 0
        for arg in arguments:
            try:
                score = int(arg)
                if score < 0:
                    negatives += 1
                scores.append(score)
            except ValueError:
                print()
                print(f"Error: '{arg}' is not a valid integer.")
                return

        print()
        print(f"Scores processed: {scores}")

        if negatives == 1:
            print()
            print(f"WARNING: {negatives} score is negative!")
        elif negatives > 1:
            print()
            print(f"WARNING: {negatives} scores are negative!")

        players: int = len(scores)
        total: int = sum(scores)
        highest: int = max(scores)
        lowest: int = min(scores)
        average: float = total / players

        print()
        print(f"Total players: {players}")
        print(f"Total score: {total}")
        print(f"Average score: {average:.2f}")
        print(f"High score: {highest}")
        print(f"Low score: {lowest}")
        print(f"Score range: {highest - lowest}")


if __name__ == "__main__":
    score_cruncher()
