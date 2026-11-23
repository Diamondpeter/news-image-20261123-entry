#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261123.

Writes the news-network image held in this repository to /output/entry.png.
Standard library only, no network, deterministic: a plain file copy, so
both runs write identical bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    """Copy the held news-network image to the output path.

    Refuses a file that is not a whole PNG or is over the 1 MiB gate
    limit, so a broken held image fails loudly here instead of at the
    gate.
    """
    if not os.path.isfile(SOURCE):
        print("entry.png missing beside main.py", file=sys.stderr)
        raise SystemExit(1)
    with open(SOURCE, "rb") as fh:
        magic = fh.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG", file=sys.stderr)
        raise SystemExit(1)
    size = os.path.getsize(SOURCE)
    if size > 1048576:
        print("entry.png is %d bytes, over the 1 MiB limit" % size,
              file=sys.stderr)
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    print("wrote %s (%d bytes)" % (dest, size))


if __name__ == "__main__":
    main()
