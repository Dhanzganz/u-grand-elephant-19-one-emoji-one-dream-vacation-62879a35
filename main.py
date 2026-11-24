#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — entry program.

Writes a single emoji to /output/entry.txt: the desert island,
the dream vacation in one glyph — faraway, warm, and instantly
readable as a postcard from the trip of a lifetime.
"""
import os

EMOJI = "\U0001F3DD\uFE0F"  # desert island
# Why this one: it names the dream vacation outright (faraway island +
# beach), it is a postcard at a glance, it points at one particular
# dream rather than any holiday, and it reads instantly on any screen.

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)
    print(EMOJI)

if __name__ == "__main__":
    main()
