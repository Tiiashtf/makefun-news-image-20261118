#!/usr/bin/env python3
"""Entry point for the make.fun news-image-20261118 bounty.

The program ships a pre-composed newspaper front page (entry.png, 1024x1024)
summing up Wednesday 18 November 2026's world news and copies it, byte for
byte, to $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).

Stdlib only. No network, no randomness: two runs produce identical output.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.png")
    # MAKEFUN_OUTPUT_DIR names a directory in the harness; tolerate a file path.
    dest = out_dir if out_dir.endswith(".png") else os.path.join(out_dir, "entry.png")
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    shutil.copyfile(SOURCE, dest)
    if os.path.getsize(dest) != os.path.getsize(SOURCE):
        print(f"error: copied {dest} is truncated", file=sys.stderr)
        return 1
    print(f"wrote {dest}")


if __name__ == "__main__":
    sys.exit(main())
