#!/usr/bin/env python3
"""Midnight Fridge Roast — writes one roast line to /output/entry.txt.

The bounty gate: /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only white space, a single line. validate() mirrors
that gate so a bad entry can never be written by accident, and main()
reads the file back to prove the bytes on disk are exactly the line.
"""

import os

ENTRY = "At midnight the fridge locks and says 'go to bed' \u2014 it has a healthier sleep schedule than I do."


def validate(text):
    """Mirror the bounty gate: 1-200 chars, not only whitespace, one line."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main():
    if not validate(ENTRY):
        raise SystemExit("entry fails the bounty gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and prove the bytes on disk are exactly the entry.
    with open("/output/entry.txt", "rb") as f:
        on_disk = f.read()
    if on_disk != ENTRY.encode("utf-8"):
        raise SystemExit("read-back mismatch: entry.txt is not the entry")


if __name__ == "__main__":
    main()
