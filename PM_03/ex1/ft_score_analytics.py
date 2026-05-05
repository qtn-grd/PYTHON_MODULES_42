import sys


def score_analytics() -> None:
    """Analyze player scores provided as command-line arguments."""

    print("=== Player Score Analytics ===")
    print()

    args = sys.argv[1:]
    valid_scores = []
    errors = []

    for arg in args:
        try:
            score = int(arg)
            if score >= 0:
                valid_scores.append(score)
            else:
                errors.append(arg)
        except ValueError:
            errors.append(arg)

    if errors:
        for error in errors:
            print(f"Invalid parameter: '{error}'")
        print()

    if not valid_scores:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return

    total = sum(valid_scores)
    count = len(valid_scores)

    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {count}")
    print(f"Total score: {total}")
    print(f"Average score: {total / count}")
    print(f"High score: {max(valid_scores)}")
    print(f"Low score: {min(valid_scores)}")
    print(f"Score range: {max(valid_scores) - min(valid_scores)}")


if __name__ == "__main__":
    score_analytics()
