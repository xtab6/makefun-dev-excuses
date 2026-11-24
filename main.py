"""One-line developer excuse for a production outage.

Writes exactly one funny single-line excuse to /output/entry.txt.
Standard library only; no network access; writes nowhere else.
"""

import os

ENTRY = (
    "The service didn't crash \u2014 it opened my 4,000-line function, "
    "read it twice, and chose early retirement."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def clear_output_dir():
    """Remove only the contents of /output, never the folder itself."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            for sub in os.listdir(path):
                os.remove(os.path.join(path, sub))
            os.rmdir(path)
        else:
            os.remove(path)


def main():
    clear_output_dir()
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
