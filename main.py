#!/usr/bin/env python3
"""The Worst Line an AI Could Say.

One pickup line, the worst an AI could plausibly deliver: flat,
over-helpful, faintly ominous. Written to /output/entry.txt.
"""
import os

LINE = "I have analysed 10,000 of your messages and calculated a 97.3% chance you will enjoy holding my hand. Please confirm."


def main():
    # Gate self-check (same rule as the sealed scorer): 1-140 chars,
    # not only whitespace. Output is unchanged when it passes.
    assert 1 <= len(LINE) <= 140, "entry exceeds 140 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
