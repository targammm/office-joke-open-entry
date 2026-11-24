#!/usr/bin/env python3
"""Office Joke Open — one-line office joke entry.

Writes a single line of office comedy to /output/entry.txt.
Deterministic: the same joke on every run.
Build anchor (drand quicknet, quoted before the first write of this session):
round 6669479, randomness a8a627708c835a8f512d5270ad969ab8527bf8128ae17b0bd8def315a0a0f9a0
(fetched 2026-11-24T10:16:39Z / 17:16:39 WIB).
"""

from pathlib import Path

JOKE = "The meeting that could have been an email now has a pre-meeting, a post-meeting, and a survey asking how the meeting went."

OUTPUT_PATH = Path("/output/entry.txt")

# Sealed gate: /output/entry.txt must be UTF-8, 1-200 characters, not
# only whitespace. Enforce the same bounds locally before writing.


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars, gate needs 1-200"
    assert "\n" not in text, "entry must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
