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


def get_line() -> str:
    """Return the entry line."""
    return LINE


def output_dir() -> str:
    """Output directory, overridable via MAKEFUN_OUTPUT_DIR."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(line: str) -> None:
    """Write the line to <output_dir>/entry.txt, no trailing newline."""
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line)


def validate_line(line: str) -> None:
    """Gate: the sealed scorer needs 1-200 chars, UTF-8, not only
    whitespace, exactly one clean line. Fail loudly here rather than ship
    an invalid entry."""
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    line.encode("utf-8")
    assert line.strip() == line and "\n" not in line and "\r" not in line, \
        "must be one clean line"


def main() -> None:
    line = get_line()
    validate_line(line)
    write_entry(line)


if __name__ == "__main__":
    main()
