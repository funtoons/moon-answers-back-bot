#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry.

Writes one line, in the voice of the Moon replying at last to the
wishes, howls and late-night promises of everyone staring up at it,
to /output/entry.txt. Deterministic and offline: the same fixed text
on every run, no randomness, no network, no timestamps.
"""

import os

ENTRY = (
    "I heard every wish, every howl, every 2 a.m. promise to change. "
    "My answer, after four and a half billion years: no. Same time tomorrow?"
)


def main():
    if not 1 <= len(ENTRY) <= 240 or not ENTRY.strip():
        raise SystemExit("entry must be 1-240 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
