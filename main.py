"""Write one short relaxing text for the make.fun AI judge to /output/entry.txt.

Pure standard library, deterministic: the same text on every run.
The text is a small, unhurried scene -- a lighthouse keeper at dawn --
written to slow the reader down and leave a steady image behind.
"""

import os

TEXT = (
    "The lighthouse keeper never hurries the dawn. He trims the wick, "
    "sets the kettle on, and watches the grey water turn to glass. "
    "The lamp is already lit; it only has to be kept. Small, steady, "
    "and enough to find the shore by."
)


def main():
    # Self-check the gate before writing: 1-280 characters, not only whitespace.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text must be 1-280 non-whitespace characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
