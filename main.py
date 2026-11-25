#!/usr/bin/env python3
"""Write the Famous Last Words epitaph entry to /output/entry.txt.

Stdlib only. The output directory defaults to /output and can be
overridden with the OUTPUT_DIR environment variable (used for local
verification).
"""

import os
from pathlib import Path

ENTRY = (
    "Doctor, you said I'd live to a hundred. I'm 34, you're holding "
    "the wrong chart, and my wife just married the man in bed 12 "
    "while I was still warm."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
