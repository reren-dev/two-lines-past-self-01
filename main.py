#!/usr/bin/env python3
"""Two Lines to Your Past Self.

Writes exactly two lines to /output/entry.txt: a warning to the writer's
past self about one specific moment, and one sentence on why it mattered.
"""

import os

LINE_ONE = "Don't delete Grandma's voicemail about the soup she left in your fridge - save it."
LINE_TWO = "Three years from now it will be the only recording of her voice you own, and you will play it every time you forget what home sounds like."

ENTRY = LINE_ONE + "\n" + LINE_TWO + "\n"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY, end="")


if __name__ == "__main__":
    main()
