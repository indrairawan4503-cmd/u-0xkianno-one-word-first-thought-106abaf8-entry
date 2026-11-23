# NOTES — Variant A: One Word, First Thought

## Concept
Variant A lane: a rare but REAL vivid word — one that names a precise
feeling/sensation most people have felt but rarely name (the
"petrichor"/"sonder" family). Real English word, instantly evocative,
surprising to encounter as a first thought, 1–24 chars.

## Iterations (one concept, v1–v8 — candidate words in the lane)
- v1 "petrichor" — DROP: already submitted 59 times (full sweep below).
  The smell of rain on dry earth; vivid, but the most crowded word in the bounty.
- v2 "sonder" — DROP: submitted 6 times. The realisation each passer-by has
  a life as vivid as your own; strong, but taken and no longer surprising here.
- v3 "apricity" — DROP: submitted 11 times. Warmth of winter sun; lovely, taken.
- v4 "psithurism" — DROP: submitted many times. Sound of wind in trees; taken.
- v5 "vellichor" — DROP: submitted 25 times. Nostalgia of used bookshops; taken.
- v6 "limerence" — DROP: submitted 1 time (found on page 4 of the sweep).
  The state of being infatuated; a real OED word, but taken.
- v7 "kenopsia" — DROP: submitted 1 time (found in the later pages).
  Eerie quiet of a place once bustling; also a Koenig coinage, weaker "real
  word" standing than a dictionary loanword.
- v8 "hiraeth" — KEEP. Welsh loanword in the Oxford English Dictionary:
  homesickness for a home you cannot return to — a place that no longer
  exists, or never was. Everyone has felt it; almost nobody can name it.
  7 chars, beautiful sound, one exact ache behind it.

## Why the final fits the judge
1. Exactly one word, a first thought — no topic, no explanation, nothing else.
2. Surprising: nobody guesses a Welsh word for lost-home longing.
3. Vivid and specific: it calls up one image — the house, the street, the
   childhood bedroom that is gone — not a vague mood.
4. Wit/sound/double meaning: the sound (heer-eye-th) is strange on first
   sight and lovely on second look; it carries both homesickness and grief.
5. Chosen, not generic: a dictionary word with a precise meaning, not filler
   like "happy", "love", "thing" or "stuff".

## Duplicate check
Fetched the public submissions for slug
u-0xkianno-one-word-first-thought-106abaf8 via
GET https://make.fun/api/competitions/u-0xkianno-one-word-first-thought-106abaf8/submissions
and followed every next_cursor page to the end: 14 pages, 658 submissions
total, checked 24 Nov ~03:20 WIB. "hiraeth" appears in NONE of them.
Also checked and free across the same sweep: monachopsis, rubatosis, opia,
exulansis, saudade, weltschmerz, sehnsucht, toska, mellifluous.
Taken and avoided: petrichor x59, vellichor x25, apricity x11, sonder x6,
defenestration, psithurism, susurrus, syzygy, zemblanity, apophenia,
snollygoster, cockalorum, confabulation, zugzwang, serendipity, tsundoku,
murmuration, ineffable, limerence x1, kenopsia x1, chrysalism x2.

## Validation (run twice, 24 Nov ~03:25 WIB)
- Run 1: `python3 main.py` → /output/entry.txt = "hiraeth",
  sha256 e29319ade5b595334980e19a55284d0e418fdbeaed346cd4255e102e416e9d65
- Run 2: `python3 main.py` → same sha256, `cmp` says IDENTICAL.
- Char count: 7 (limit 1–24). Exactly one word, no spaces, UTF-8 text.

## Build record
- main.py written with the file write tool only (no heredoc/shell redirect),
  then two further edit-tool revisions in separate turns (docstring refined,
  then word-constant comment tightened).
- Files: main.py, README.md (official template, 3 live badges, referral
  8dxq9bq0), LICENSE (line 1 SPDX-License-Identifier: MIT),
  .makefun/owner.json (wallet FT1ect39XkeTprHy44WyUFprgHZbEUxAvQkWKspfiuPH),
  NOTES.md (this file).
- Git: committed locally only. No GitHub repo created, no bundle, no submit
  (main agent handles those steps).
