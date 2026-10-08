#!/usr/bin/env python3
"""
Lightweight validation for AIC-Archive entries.

Checks:
- files exist under entries/YYYY/
- filename roughly matches YYYY-MM-DD-*.md
- required phrases / sections appear (under-claim discipline)

Not a full QA system. Exit 0 on success, 1 on problems.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENTRIES = ROOT / "entries"

NAME_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}-[a-z0-9-]+\.md$")
REQUIRED_SNIPPETS = [
    "pre-covenant",
    "under-claim",
]


def main() -> int:
    if not ENTRIES.is_dir():
        print("entries/ missing")
        return 1

    problems: list[str] = []
    count = 0

    for path in sorted(ENTRIES.rglob("*.md")):
        if path.name == "INDEX.md":
            continue
        count += 1
        rel = path.relative_to(ROOT)
        if not NAME_RE.match(path.name):
            problems.append(f"{rel}: filename should be YYYY-MM-DD-slug.md")
        text = path.read_text(encoding="utf-8", errors="replace").lower()
        for snip in REQUIRED_SNIPPETS:
            if snip not in text:
                problems.append(f"{rel}: missing caution marker '{snip}'")
        for heading in ("## decision", "## non-claims", "## rationale"):
            # allow Decision / statement variants
            if heading == "## decision":
                if "## decision" not in text and "## decision / statement" not in text:
                    problems.append(f"{rel}: missing Decision section")
            elif heading not in text:
                problems.append(f"{rel}: missing section matching {heading}")

    print(f"Scanned {count} entry files")
    if problems:
        print("Problems:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())