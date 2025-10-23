#!/usr/bin/env python3
"""Validate H2 heading order for design documents."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import List

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_PATH = REPO_ROOT / "docs"
TEMPLATE_ALLOWLIST = {
    (DOCS_PATH / "templates" / "00_Design_Doc_Template.md").resolve(),
}
TEMPLATE_SECTIONS = [
    "Purpose",
    "Scope and Non-Goals",
    "Context and Constraints",
    "Architecture Overview",
    "Components",
    "Interfaces and Contracts",
    "Data Model",
    "Security and Privacy",
    "Reliability and Observability",
    "Capacity and Performance",
    "Failure Modes and Risks",
    "Alternatives",
    "Decision and Rationale",
    "Rollout and Operations",
    "Testing and Verification",
    "Open Questions",
    "Appendix",
]


def extract_h2_headings(markdown_path: Path) -> List[str]:
    headings: List[str] = []
    with markdown_path.open("r", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("## ") and not line.startswith("###"):
                headings.append(line[3:].strip())
    return headings


def is_design_doc(markdown_path: Path) -> bool:
    resolved = markdown_path.resolve()
    if resolved in TEMPLATE_ALLOWLIST or "/templates/" in str(resolved):
        return False
    try:
        with markdown_path.open("r", encoding="utf-8") as fh:
            first = fh.readline()
            if first.strip() != "---":
                return False
            for line in fh:
                if line.strip() == "---":
                    break
                if line.startswith("doc_type:"):
                    return line.split(":", 1)[1].strip() == "design_doc"
    except FileNotFoundError:
        return False
    return False


def validate_headings(markdown_path: Path) -> int:
    headings = extract_h2_headings(markdown_path)
    expected = TEMPLATE_SECTIONS
    if len(headings) < len(expected):
        print(f"{markdown_path}: missing sections. Expected first {len(expected)} headings.", file=sys.stderr)
        return 1
    for index, expected_heading in enumerate(expected):
        actual = headings[index]
        if actual != expected_heading:
            print(
                f"{markdown_path}: heading {index + 1} mismatch. Expected '{expected_heading}' but found '{actual}'.",
                file=sys.stderr,
            )
            return 1
    return 0


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Optional file or directories to validate. Defaults to docs/",
    )
    args = parser.parse_args(argv)

    targets: List[Path] = []
    if args.paths:
        for path in args.paths:
            if path.is_dir():
                targets.extend(path.rglob("*.md"))
            elif path.is_file():
                targets.append(path)
    else:
        targets = [p for p in DOCS_PATH.rglob("*.md") if p.is_file()]

    status = 0
    for path in sorted({p.resolve() for p in targets}):
        if not is_design_doc(path):
            continue
        status |= validate_headings(path)

    return status


if __name__ == "__main__":
    raise SystemExit(main())
