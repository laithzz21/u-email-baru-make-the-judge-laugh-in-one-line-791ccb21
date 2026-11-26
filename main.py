#!/usr/bin/env python3
"""Entry for make.fun: Make the Judge Laugh in One Line.

Prints exactly one funny line (<=200 characters) to stdout and writes
it to entry.txt under the output directory given by the environment.
Stdlib only. Never writes into the repository directory.
"""

import os

ENTRY = "My plants died, so I replaced them with a photo of plants. Now even the photo looks disappointed."


def validate_entry(line):
    """Check the entry is exactly one line and at most 200 characters."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) == 0:
        raise ValueError("entry must not be empty")
    if len(line) > 200:
        raise ValueError("entry exceeds 200 characters: %d" % len(line))
    return line


def resolve_output_dir():
    """Pick the output directory from the environment, in priority order."""
    for var in ("MAKEFUN_OUTPUT_DIR", "MAKEFUN_OUTPUT"):
        value = os.environ.get(var)
        if value:
            return value
    return os.path.join("/tmp", "makefun", "u-email-baru-make-the-judge-laugh-in-one-line-791ccb21")


def main():
    entry = validate_entry(ENTRY)
    output_dir = resolve_output_dir()
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    try:
        with open(entry_path, "w", encoding="utf-8") as f:
            f.write(entry + "\n")
    except OSError:
        # Fallback: if the chosen directory is not writable, use /tmp.
        fallback_dir = os.path.join("/tmp", "makefun", "u-email-baru-make-the-judge-laugh-in-one-line-791ccb21")
        os.makedirs(fallback_dir, exist_ok=True)
        entry_path = os.path.join(fallback_dir, "entry.txt")
        with open(entry_path, "w", encoding="utf-8") as f:
            f.write(entry + "\n")
    # Read-back verify: what was written must match the entry exactly.
    with open(entry_path, "r", encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    if written != entry:
        raise RuntimeError("read-back mismatch in entry.txt")
    print(entry)


if __name__ == "__main__":
    main()
