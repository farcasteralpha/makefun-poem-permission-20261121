#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is a fixed literal: no input, no network, no randomness, so
every run writes byte-identical output.
"""

from pathlib import Path

POEM = """I carried the question
like a key
in a closed fist,
as if to ask
were to confess
I had no door.

Then I asked.
A hand that was not mine
turned the lock —
to ask is to lend another
the power to give,
and be given back
the key — still warm
from another hand.
"""


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
