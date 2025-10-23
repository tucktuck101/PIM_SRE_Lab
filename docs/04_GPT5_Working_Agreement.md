---
title: GPT-5 Working Agreement
doc_type: policy
status: draft
version: 0.1.0
owners:
  - docs@pim-sre.lab
last_updated: 2024-05-18
tags:
  - governance
  - automation
---

# GPT-5 Working Agreement

## Purpose

Define the operating guardrails for GPT-5 contributions within the PIM SRE Lab so automated assistance remains
auditable, reversible, and aligned with maintainer expectations.

## Scope

Applies to any GPT-5 initiated or assisted change to documentation, tooling,
or configuration stored in this repository. The agreement binds both
autonomous runs and human-in-the-loop sessions that rely on GPT-5 output.

## Requirements

### Allowed and Protected Paths

- Allowed for direct edits: `docs/**`, `tools/**`, `.github/`,
  `.markdownlint.yaml`, `.vale/**`, `Makefile`, and project scripts assigned
  to GPT-5.
- Protected (read-only without prior approval): production manifests,
  Terraform, secrets, credentials, and any path listed in `Id_Registry.md` as
  maintainer-controlled.
- Protected documents (`docs/02_Glossary.md`, `docs/03_Style_Guide.md`,
  `docs/03a_Naming_And_Filenames.md`, `docs/35_Templates_Index.md` once
  created) require explicit maintainer confirmation before modification.

### Change Control

- Risky edits (schema changes, validators, or tooling under `tools/`) must
  be proposed via pull request; no direct pushes.
- Breaking documentation structures or unpublished templates mandates an
  Architecture Decision Record (`docs/templates/01_ADR_Template.md`) linked
  in the PR.
- GPT-5 must refuse to proceed if required validators (`markdownlint`,
  `vale`, front matter schema, link checks, or heading order) fail locally.

### Output Contract

All GPT-5-authored pull requests must include the following PR body sections:

1. Summary — concise explanation of scope and intent.
2. Diff Highlights — bullet list of the most critical or high-risk changes.
3. Test Plan — commands executed (or rationale if tests are not applicable), including validator runs.

### Example PR Checklist

```text
- [ ] Summary, Diff Highlights, and Test Plan completed
- [ ] Front matter validated (`make docs-frontmatter`)
- [ ] Markdown, link, and style linters pass (`make docs-validate`)
- [ ] References and cross-links verified
- [ ] ADR linked when change alters governance or templates
```

## Compliance

- Run `make docs-validate` before requesting review; attach command output to
  the PR body.
- Preserve change history by referencing related ADRs, RFCs, or issues when
  submitting updates.
- Refuse to apply changes if requested operations would violate protected
  path rules or bypass reviewer sign-off.

## Exceptions

- Emergency fixes to resolve failing CI may be applied after maintainer
  approval with a follow-up PR documenting clean-up.
- Minor formatting corrections inside protected documents are allowed only
  when explicitly instructed by a maintainer in writing and must be limited
  to the described scope.

## References

- [Documentation Style Guide](03_Style_Guide.md)
- [Naming and Filenames Policy](03a_Naming_And_Filenames.md)
- [PIM SRE Glossary](02_Glossary.md)
- [Design Doc Template](templates/00_Design_Doc_Template.md) *(pending)*
- [ADR Template](templates/01_ADR_Template.md) *(pending)*

---

Last reviewed: 2024-05-18.
