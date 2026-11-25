#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun program/v1.

Writes a single line, in the voice of the Moon answering at last,
to /output/entry.txt. Deterministic: the same line on every run.
"""

import os

ENTRY = (
    "You wished, you howled, you promised you'd change at 2 a.m. \u2014 "
    "four billion years of it. Tonight I finally answer: no. "
    "Ask the sun. He's younger, and he still believes in you."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 240, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
