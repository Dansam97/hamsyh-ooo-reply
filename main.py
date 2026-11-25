import os

ENTRY_TEXT = (
    "I'm out of office until Monday, and I've switched to airplane mode. "
    "Not my phone. Me."
)


MAX_CHARS = 160


def build_entry() -> str:
    """Assemble the entry text and hold it to the competition gate:
    UTF-8 text of 1..MAX_CHARS characters, not only white space."""
    text = ENTRY_TEXT.strip()
    if not text:
        raise ValueError("entry text must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry text is {len(text)} chars, over the {MAX_CHARS} cap")
    text.encode("utf-8")  # raises if the text is not cleanly encodable
    return text


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Write raw UTF-8 bytes: exactly the entry text, no trailing newline,
    # so the file the scorer reads is byte-for-byte the judged line.
    with open(path, "wb") as fh:
        fh.write(build_entry().encode("utf-8"))


if __name__ == "__main__":
    main()
