#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Writes one original one-line joke about office life to /output/entry.txt.
The joke is a single line, well under 200 characters.
"""

import os

JOKE = (
    "I asked IT for a second monitor; they sent a mirror and a sticky note "
    "saying, 'Reflect on your productivity.'"
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
