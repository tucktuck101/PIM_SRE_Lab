---
title: Naming and Filenames Policy
doc_type: policy
status: draft
version: 0.1.0
owners:
  - docs@pim-sre.lab
last_updated: 2024-05-18
tags:
  - naming
  - documentation
---

# Naming and Filenames Policy

## Purpose

Document the canonical filename patterns for PIM SRE Lab markdown artifacts
and provide quick-reference examples that align with the [Documentation Style
Guide](03_Style_Guide.md).

## Required Filename Pattern

All governed Markdown files must satisfy the following PCRE pattern:

```regex
^\d{2}_[A-Z][A-Za-z0-9]*(?:_[A-Z][A-Za-z0-9]*)*\.md$
```

POSIX ERE equivalent:

```regex
^[0-9]{2}_[A-Z][A-Za-z0-9]*(?:_[A-Z][A-Za-z0-9]*)*\.md$
```

Key rules:

- Two-digit numeric prefix (`00`–`99`) that enforces ordering.
- Words are TitleCase segments separated by underscores.
- Only ASCII letters and digits are allowed; no spaces or hyphens.
- File extension must be `.md`.

## Valid Examples

- `00_Design_Doc_Template.md` — Template identifier with ordering prefix.
- `03_Style_Guide.md` — Matches current style guide document.
- `12_Runbook_Template.md` — Uses TitleCase segments and numeric prefix.
- `21_Check_Headings_Order.md` — Verb-noun phrase normalized to TitleCase segments.
- `35_Templates_Index.md` — Index document with two segments after the prefix.

## Invalid Examples

- `3_style_guide.md` — Prefix must be two digits; segments must be TitleCase.
- `07-style-guide.md` — Hyphen separators are not allowed.
- `08_StyleGuide.MD` — Extension must be lowercase `.md`.
- `09_Style Guide.md` — Spaces are not allowed in filenames.
- `11_Style_Guide!.md` — Special characters (`!`) are disallowed.

## Allowed Deviations

- Legacy files outside the managed docs program retain their existing names until migrated into compliance.
- Auto-generated files (e.g., API reference stubs) must be approved via
  [Id_Registry.md](Id_Registry.md) before using alternate patterns.

Waivers must include the owning team, justification, expected remediation
date, and a link to the approved registry entry.

## Registration

All new filenames must be registered in `Id_Registry.md` with their numeric
prefix and purpose before merging. Coordinate updates through the
documentation governance process described in the style guide to avoid
collisions.

---

Last reviewed: 2024-05-18.
