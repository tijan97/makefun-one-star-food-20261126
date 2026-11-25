#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single-sentence alien-tourist one-star review of planet Earth
that still lands a genuine compliment about the food.
"""

import os
import sys

SENTENCE = (
    "One star: the gravity is broken, the weather has no settings menu, "
    "and the locals keep telling me to 'have a nice day,' but the tacos "
    "are so good I would invade this planet again just for the salsa."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    sentence = SENTENCE.strip()
    if not sentence:
        print("error: empty sentence", file=sys.stderr)
        return 1
    if len(sentence) > 200:
        print(
            f"error: sentence is {len(sentence)} chars, over the 200 limit",
            file=sys.stderr,
        )
        return 1
    if sentence.count(".") != 1 or not sentence.endswith("."):
        print("error: entry must be exactly one sentence", file=sys.stderr)
        return 1
    if any(p in sentence[:-1] for p in ".!?"):
        print("error: entry must be exactly one sentence", file=sys.stderr)
        return 1
    if "\n" in sentence or "\r" in sentence:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "sentence.txt"), "w", encoding="utf-8") as f:
        f.write(sentence + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
