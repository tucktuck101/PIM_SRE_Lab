#!/usr/bin/env python3
"""Validate Markdown front matter against the repository schema."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "tools" / "frontmatter.schema.json"
DOCS_PATH = REPO_ROOT / "docs"


def load_schema() -> Dict[str, Any]:
    with SCHEMA_PATH.open("r", encoding="utf-8") as fh:
        return json.load(fh)

def parse_simple_yaml(lines: List[str]) -> Dict[str, Any]:
    """Parse a limited subset of YAML used in front matter."""
    data: Dict[str, Any] = {}
    current_key: str | None = None
    for raw in lines:
        line = raw.rstrip("\n")
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("- "):
            if not current_key or not isinstance(data.get(current_key), list):
                raise ValueError(f"unexpected list item: {line}")
            data[current_key].append(stripped[2:].strip())
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if not key:
                raise ValueError(f"invalid key line: {line}")
            if value:
                data[key] = value
                current_key = None
            else:
                data[key] = []
                current_key = key
            continue
        raise ValueError(f"unsupported front matter line: {line}")
    return data

def validate_against_schema(front_matter: Dict[str, Any], schema: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    required = schema.get("required", [])
    for field in required:
        if field not in front_matter:
            errors.append(f"<root>: missing required field '{field}'")
    properties = schema.get("properties", {})
    for key in front_matter:
        if key not in properties:
            errors.append(f"{key}: unexpected property")
    for key, prop_schema in properties.items():
        if key not in front_matter:
            continue
        value = front_matter[key]
        errors.extend(check_property(value, prop_schema, key))
    return errors


def check_property(value: Any, prop_schema: Dict[str, Any], path: str) -> List[str]:
    errors: List[str] = []
    expected_type = prop_schema.get("type")
    if expected_type == "string":
        if not isinstance(value, str):
            errors.append(f"{path}: expected string")
            return errors
        enum_values = prop_schema.get("enum")
        if enum_values and value not in enum_values:
            errors.append(f"{path}: value '{value}' not in {enum_values}")
        pattern = prop_schema.get("pattern")
        if pattern and not re.fullmatch(pattern, value):
            errors.append(f"{path}: value '{value}' does not match pattern {pattern}")
    elif expected_type == "array":
        if not isinstance(value, list):
            errors.append(f"{path}: expected array")
            return errors
        min_items = prop_schema.get("minItems")
        if min_items and len(value) < min_items:
            errors.append(f"{path}: must contain at least {min_items} items")
        item_schema = prop_schema.get("items", {})
        item_type = item_schema.get("type")
        enum_values = item_schema.get("enum")
        pattern = item_schema.get("pattern")
        for idx, item in enumerate(value):
            item_path = f"{path}[{idx}]"
            if item_type == "string" and not isinstance(item, str):
                errors.append(f"{item_path}: expected string")
                continue
            if enum_values and item not in enum_values:
                errors.append(f"{item_path}: value '{item}' not in {enum_values}")
            if pattern and isinstance(item, str) and not re.fullmatch(pattern, item):
                errors.append(f"{item_path}: value '{item}' does not match pattern {pattern}")
        enum_values = prop_schema.get("enum")
        if enum_values and value not in enum_values:
            errors.append(f"{path}: value not in allowed set {enum_values}")
    else:
        # For property types not explicitly handled, rely on presence of value only.
        pass
    return errors

def extract_front_matter(markdown_path: Path) -> Tuple[Dict[str, Any], int]:
    """Return front matter dict and body start line (1-based)."""
    with markdown_path.open("r", encoding="utf-8") as fh:
        lines = fh.readlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing front matter fence")
    front_lines: List[str] = []
    for idx, line in enumerate(lines[1:], start=2):
        if line.strip() == "---":
            body_start = idx + 1
            break
        front_lines.append(line)
    else:
        raise ValueError("unterminated front matter block")
    data = parse_simple_yaml(front_lines)
    return data, body_start


def validate_file(schema: Dict[str, Any], markdown_path: Path) -> List[str]:
    errors: List[str] = []
    try:
        front_matter, _ = extract_front_matter(markdown_path)
    except ValueError as exc:
        errors.append(f"{markdown_path}: {exc}")
        return errors

    for message in validate_against_schema(front_matter, schema):
        errors.append(f"{markdown_path}: {message}")
    return errors


def collect_markdown_files() -> List[Path]:
    return [p for p in DOCS_PATH.rglob("*.md") if p.is_file()]


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Optional file or directory paths to validate (defaults to docs/)",
    )
    args = parser.parse_args(argv)

    schema = load_schema()

    targets: List[Path] = []
    if args.paths:
        for path in args.paths:
            if path.is_dir():
                targets.extend(path.rglob("*.md"))
            elif path.is_file():
                targets.append(path)
    else:
        targets = collect_markdown_files()

    targets = sorted({p.resolve() for p in targets if p.suffix == ".md"})

    all_errors: List[str] = []
    for markdown_path in targets:
        if DOCS_PATH not in markdown_path.parents and markdown_path.parent != DOCS_PATH:
            # Skip files outside docs/ unless explicitly provided
            continue
        all_errors.extend(validate_file(schema, markdown_path))

    if all_errors:
        for err in all_errors:
            print(err, file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
