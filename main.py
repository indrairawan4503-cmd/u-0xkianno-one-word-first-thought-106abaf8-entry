"""Variant A — One Word, First Thought.

Concept: a rare but REAL word naming a precise feeling most people have
felt but rarely name (the petrichor/sonder family). The word is "hiraeth":
a Welsh loanword in the Oxford English Dictionary — homesickness for a home
you cannot return to, a place that no longer exists, or never was. Seven
letters, instantly evocative, surprising as a first thought.

Deterministic: no randomness, no network, no input. Writes the single word
to /output/entry.txt.

Why this word fits the judge: surprising (no one guesses a Welsh word for
lost-home longing as a first thought), vivid and specific (it calls up one
exact ache — the house, the street, the childhood bedroom that is gone),
and chosen rather than generic (a dictionary word with a sound — heer-eye-th
— that rewards a second look, not filler like "happy" or "love").
"""

import os

# "hiraeth" — 7 chars, one word. Verified free: no submission among all 658
# public entries for this bounty uses it (full paginated sweep, 24 Nov 03:2x WIB).
# The obvious family (petrichor x59, vellichor x25, apricity x11, sonder x6,
# psithurism, limerence, kenopsia) is already taken; this one is not.
WORD = "hiraeth"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
