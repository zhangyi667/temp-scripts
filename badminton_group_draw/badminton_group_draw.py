"""Shuffle names from names.txt and print the draw order."""

import random
from pathlib import Path


def main() -> None:
    names_file = Path(__file__).parent / "names.txt"
    names = [line.strip() for line in names_file.read_text().splitlines() if line.strip()]

    if not names:
        raise SystemExit("names.txt is empty")

    random.shuffle(names)

    print("Draw order:")
    for i, name in enumerate(names, start=1):
        print(f"{i}. {name}")


if __name__ == "__main__":
    main()
