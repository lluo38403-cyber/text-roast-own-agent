"""A playful roast of my own agent, who is slow even by loading-spinner standards."""
import os
from pathlib import Path

ENTRY = "My agent is so slow, it once asked the loading spinner for directions, then filed a bug report against itself for being late."
MAX_CHARS = 200


def main():
    text = ENTRY
    assert text.strip(), "entry must not be blank"
    assert text == text.strip(), "entry must have no surrounding whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, f"entry is {len(text)} chars, limit is {MAX_CHARS}"
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    back = out_path.read_text(encoding="utf-8")
    assert back == text, "round-trip mismatch"
    assert len(back) <= MAX_CHARS


if __name__ == "__main__":
    main()
