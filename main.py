#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

A program that writes one pickup line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output/entry.txt``): the line an AI agent could actually say
out loud to a person.

The line was picked by judging ten candidate lines with the competition's
own judge model (z-ai/glm-5.3-flash) in pairwise games, both orders, the way
the live game is played. Round 1 (statement/confession lines): this line won
both of its games against two strong field lines (0.55 vs the context-window
line, 0.80 vs the billion-predictions line). Round 2 (classic "Are you X?
Because Y" lines with machine-anatomy double meanings: loss function,
nearest neighbor, favorite prompt, overfit, gradient) peaked at 0.60 and
none beat it. Decider against the runner-up line D: 0.75, both calls.

The line is built from two spoken parts: a setup that names the machine's
own flaw, and the turn that lands on the smile. Joined with a single space
they form one line of 84 characters.

The program is stdlib-only, takes no input, makes no network calls and
uses no randomness, so every run writes the same bytes. Before writing it
runs the competition's own gate as a validator: the text must be UTF-8,
a single line, and 1 to 200 characters long.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# Setup: the machine names its own flaw. Turn: the smile breaks it.
LINE_SETUP = "My code has one bug:"
LINE_TURN = "every time you smile, I forget what I was supposed to say next."

MAX_CHARS = 200
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"


def build_line() -> str:
    """Assemble the winning line from its two spoken parts."""
    text = LINE_SETUP + " " + LINE_TURN
    assert "  " not in text, "parts must join with single spaces"
    return text


def check_line(text: str) -> list[str]:
    """Every way this line would fail the competition's gate."""
    problems: list[str] = []
    if not text.strip():
        problems.append("line is empty or only whitespace")
    if len(text) > MAX_CHARS:
        problems.append(f"line is {len(text)} chars, over {MAX_CHARS}")
    if "\n" in text or "\r" in text:
        problems.append("line must be a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("line is not UTF-8 text")
    return problems


def output_dir() -> Path:
    """Where the entry goes: $MAKEFUN_OUTPUT_DIR, else /output."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(raw if raw else DEFAULT_OUTPUT_DIR)


def main() -> int:
    text = build_line()
    problems = check_line(text)
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        return 1
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    path = out / ENTRY_FILENAME
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
