---
title: Templates Index
doc_type: policy
status: draft
version: 0.1.0
owners:
  - docs@pim-sre.lab
last_updated: 2024-05-18
tags:
  - templates
  - documentation
---

# Templates Index

## Purpose

Provide a single directory for all sanctioned documentation templates
used within the PIM SRE Lab, including their intent and adoption
requirements.

## Available Templates

| Name | Path | Purpose | Required? |
| --- | --- | --- | --- |
| 00_Design_Doc_Template | [docs/templates/00_Design_Doc_Template.md](templates/00_Design_Doc_Template.md) | Design proposals covering<br>architecture, risks, and rollout. | Yes |
| 01_ADR_Template | [docs/templates/01_ADR_Template.md](templates/01_ADR_Template.md) | Decision record capturing<br>context, choice, and consequences. | Yes |
| 02_RFC_Template | [docs/templates/02_RFC_Template.md](templates/02_RFC_Template.md) | Cross-team proposal requiring<br>review and consensus. | Yes |
| 03_Runbook_Template | [docs/templates/03_Runbook_Template.md](templates/03_Runbook_Template.md) | Operational playbook for incident<br>response and recovery. | Yes |

> Templates marked as “Yes” under **Required?** must be used whenever a
> document of that type is created or significantly revised. Stub files
> will be added as the respective templates are authored.

## How to Choose a Template

1. Determine the document type (e.g., design, decision record, RFC, runbook).
2. Locate the matching template in the table above.
3. Copy the template into your working branch without renaming the original template file.
4. Fill in required sections, retaining front matter keys and canonical heading order.
5. Update `Id_Registry.md` with your new document ID and link to the source template.

## Governance

- Templates are protected assets; modifications require maintainer approval
  and, when structural, an ADR referencing the change.
- When a template is updated, notify the documentation maintainers and
  include the change in the PR “Diff Highlights.”
- Deprecated templates must remain available until replacement documents are
  fully adopted and linked from this index.

---

Last reviewed: 2024-05-18.
