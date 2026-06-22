#!/usr/bin/env python3
"""Run git's whitespace check while allowing Markdown hard breaks."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


TRAILING_WHITESPACE = re.compile(r"^(.*):(\d+): trailing whitespace\.$")


def is_markdown_hard_break(diagnostic: str, added_line: str) -> bool:
    match = TRAILING_WHITESPACE.match(diagnostic)
    if not match or Path(match.group(1)).suffix.lower() not in {".md", ".markdown"}:
        return False

    if not added_line.startswith("+"):
        return False

    content = added_line[1:]
    return (
        content.endswith("  ")
        and not content.endswith("   ")
        and bool(content[:-2].strip())
    )


def main() -> int:
    result = subprocess.run(
        ["git", "diff", "--check"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    lines = result.stdout.splitlines()
    errors: list[str] = []
    index = 0

    while index < len(lines):
        diagnostic = lines[index]
        added_line = lines[index + 1] if index + 1 < len(lines) else ""
        if is_markdown_hard_break(diagnostic, added_line):
            index += 2
            continue

        errors.append(diagnostic)
        index += 1

    if errors:
        print("\n".join(errors))
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
