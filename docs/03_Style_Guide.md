---
title: PIM SRE Documentation Style Guide
doc_type: style_guide
status: draft
version: 0.1.0
owners:
  - docs@pim-sre.lab
last_updated: 2024-05-18
tags:
  - documentation
  - style
---

## Purpose

Define the shared writing and formatting rules for the PIM SRE Lab
documentation set so that humans and automation produce consistent,
reviewer-friendly content.

## Tone and Voice

- Use direct, action-oriented language; prefer active voice and present tense.
- Default to inclusive, gender-neutral phrasing.
- For warnings and guardrails, lead with the risk, then the mitigation.
- Remove fluff—assume the reader is an experienced engineer with limited time.

**Do:** “Verify the shard routing hash before enabling traffic.”  
**Don’t:** “It might be a good idea to check the shard routing hash just in case.”

## Units, Numbers, and Dates

- Follow SI units with a space between the value and unit (e.g., `250 ms`,
  `5 GB`, `20 °C`).
- Spell out numbers below ten unless paired with a unit (`three services`,
  `7 pods`).
- Express dates in ISO-8601 format (`YYYY-MM-DD`), and include timezone
  offsets when times matter (`2024-05-18T13:00:00Z`).

## File Names and Headings

- All new Markdown files must satisfy
  `^\d{2}_[A-Z][A-Za-z0-9]*(?:_[A-Z][A-Za-z0-9]*)*\.md$`.
- POSIX ERE equivalent: `^[0-9]{2}_[A-Z][A-Za-z0-9]*(?:_[A-Z][A-Za-z0-9]*)*\.md$`.
- Use ATX (`#`) headings throughout; only one H1 per file that matches the
  title case of the front matter `title`.
- Increment heading levels sequentially—never skip levels.
- Keep headings ≤ 120 characters to align with markdownlint rules.

**Do:** `## Failure Modes and Risks`  
**Don’t:** `### FAILURE MODES!`

## Front Matter

Every managed document must begin with YAML front matter containing:

- `title` — Title-cased string that matches the H1.
- `doc_type` — One of: `style_guide`, `design_doc`, `adr`, `rfc`, `runbook`,
  `glossary`, `policy`.
- `status` — `draft`, `in_review`, or `published`.
- `version` — Semantic version string (`MAJOR.MINOR.PATCH`).
- `owners` — YAML list of contact emails or team handles.
- `last_updated` — `YYYY-MM-DD`.
- `tags` — YAML list of short, lowercase keywords.

## Code Blocks and Examples

- Wrap code and shell snippets in fenced code blocks with an explicit
  language tag (` ```sh `, ` ```sql `, etc.).
- Prefer realistic, copy-paste-ready examples.
- Annotate inline commands with preceding prose that explains when and why
  to run them.

```sh
make docs-validate
```

## Links and Cross-References

- Use relative paths for intra-repo links (e.g.,
  `[Design Template](templates/00_Design_Doc_Template.md)`).
- Reference anchors with lowercase-hyphenated fragments
  (`#failure-modes-and-risks`).
- Avoid bare URLs; wrap links in descriptive text.
- Cross-link related documents the first time they are mentioned.

## Tables and Lists

- Format tables with header separators and align text for readability.
- Use unordered lists for parallel items; ordered lists only when sequence
  matters.
- Keep list items under 120 characters; break into multiple lines with a
  hanging indent if needed.

## Doc Type Containers

Use the following required H2 sections for each doc type. Optional sections
are listed in parentheses.

| Doc Type   | Required H2 Sections                                                                                                                        | Purpose                                                     | Required? |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | --------- |
| design_doc | Purpose; Scope and Non-Goals; Context and Constraints; Architecture Overview; Components; Interfaces and Contracts; Data Model; Security and Privacy; Reliability and Observability; Capacity and Performance; Failure Modes and Risks; Alternatives; Decision and Rationale; Rollout and Operations; Testing and Verification; Open Questions; Appendix | Standardize design proposals and reviews                   | Yes       |
| adr        | Context; Decision; Consequences; Rejected Options; Links                                                                                    | Capture architectural decisions                             | Yes       |
| rfc        | Summary; Motivation; Proposal; Compatibility; Security; Observability; Rollout Plan; Open Questions; Alternatives; Appendix                 | Govern broader-scope change proposals                       | Yes       |
| runbook    | Overview; Preconditions; Validation; Step-by-Step; Rollback; Contacts; Signals and Metrics; Related Documents                               | Guide on-call responders through routine or emergency work  | Yes       |
| glossary   | Introduction; Terms; Terms to Add Later                                                                                                     | Maintain shared vocabulary                                  | Yes       |
| policy     | Purpose; Scope; Requirements; Compliance; Exceptions; References                                                                             | Define enforceable standards                                | Yes       |

## Visuals and Diagrams

- Use Mermaid fenced blocks with explicit `mermaid` tag; describe the
  diagram purpose before the block.
- Provide alternative text that summarizes the visual outcome.
- For figures sourced externally, retain local copies and cite the source
  beneath the figure.

## Validation Workflow

- Run `markdownlint` before submitting any PR that touches Markdown.
- Run `vale docs/` and fix warnings unless waived in writing.
- If front matter changes, run the front matter validator once staged.
- Document waivers inline with a short justification and owner approval
  reference.

## Change History

- Maintain a changelog entry in the relevant document or linked ADR when
  substantive updates occur.
- For published documents, increment `version` and update `last_updated`;
  describe the change in the PR body.

---

Last reviewed: 2024-05-18.
