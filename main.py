#!/usr/bin/env python3
"""make.fun entry: One Line, Best Line.

Writes one line as UTF-8 text to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Standard library only; runs offline.
"""
import os

LINE = "My therapist says hearing voices is completely normal for a ventriloquist, so she billed the dummy as a second patient \u2014 apparently he is the one in denial."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
