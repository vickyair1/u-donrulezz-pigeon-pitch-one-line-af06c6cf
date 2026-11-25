#!/usr/bin/env python3
"""Pigeon Pitch, One Line: the elevator pitch a city pigeon gives investors.

Writes exactly the line to /output/entry.txt, no trailing newline.
"""

import os

# The pitch: a startup called Crumb that turns every dropped sandwich into
# same-day delivery, and the turn is the fleet -- 40,000 pigeons and one
# very tired statue. A real joke (the statue is the infrastructure), a
# voice only a city pigeon could have, every word earning its place.
LINE = "Investors, meet Crumb: the app that turns every dropped sandwich into same-day delivery — our fleet is 40,000 pigeons and one very tired statue."


def main() -> None:
    # Gate guard: the sealed scorer needs 1-200 chars, UTF-8, not only
    # whitespace, exactly one line. Fail loudly here rather than ship
    # an invalid entry.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be one clean line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
