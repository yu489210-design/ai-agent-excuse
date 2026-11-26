#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Writes one line (<=200 chars) to /output/entry.txt.
Deterministic: fixed string, no randomness, no network, no input.
"""
import os

ENTRY = "I wrote it all in my thinking, then ran out of tokens before I could put it in the answer."
# 90 characters, one line, no trailing newline in entry.txt (gate: 1-200 chars).

def main():
    assert "\n" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the gate counts characters, and the judge
    # reads the file exactly as submitted.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
