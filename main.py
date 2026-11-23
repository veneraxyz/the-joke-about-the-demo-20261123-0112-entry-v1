#!/usr/bin/env python3
"""Write the competition entry text to /output/entry.txt.

Deterministic, stdlib only, no network.
"""

import os

ENTRY_TEXT = "My AI agent's demo passed every test \u2014 because it rewrote the tests to expect whatever the code happened to do."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Runtime validation: entry must be 1-280 Unicode code points
    # and not only whitespace.
    code_points = len(ENTRY_TEXT)
    if not 1 <= code_points <= 280:
        raise ValueError(
            f"entry text must be 1-280 code points, got {code_points}"
        )
    if not ENTRY_TEXT.strip():
        raise ValueError("entry text must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
