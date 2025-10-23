#!/usr/bin/env sh
set -eu

ROOT_DIR=$(dirname "$0")/..
ROOT_DIR=$(cd "$ROOT_DIR" && pwd)
TARGET_DIR="$ROOT_DIR/docs"
STATUS=0

find "$TARGET_DIR" -name '*.md' | while IFS= read -r file; do
  dir=$(dirname "$file")
  # Extract markdown links excluding anchors only
  grep -oE '\[[^\]]+\]\([^#)]+\)' "$file" | while IFS= read -r match; do
    path=$(printf '%s' "$match" | sed -E 's/^\[[^\]]+\]\(([^)]+)\)$/\1/')
    # Ignore absolute URLs (http/https) and mailto
    case "$path" in
      http://*|https://*|mailto:*)
        continue
        ;;
    esac
    # Resolve relative paths
    if [ "${path#../}" != "$path" ]; then
      target=$(cd "$dir" && cd "${path%/*}" 2>/dev/null && pwd)/$(basename "$path")
    else
      target="$dir/$path"
    fi
    if [ ! -f "$target" ]; then
      printf '%s: broken link -> %s\n' "$file" "$path" >&2
      STATUS=1
    fi
  done
  # Check reference-style links
  awk '/^\[[^\]]+\]: /{print $2}' "$file" | while IFS= read -r ref; do
    case "$ref" in
      http://*|https://*|mailto:*)
        continue
        ;;
      \#*)
        continue
        ;;
    esac
    if [ -z "$ref" ]; then
      continue
    fi
    target="$dir/$ref"
    if [ ! -f "$target" ]; then
      printf '%s: broken reference link -> %s\n' "$file" "$ref" >&2
      STATUS=1
    fi
  done
done

exit "$STATUS"
