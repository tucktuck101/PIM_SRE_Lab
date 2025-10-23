---
title: Documentation Navigation Specification
doc_type: navigation
status: draft
version: 0.1.0
owners:
  - docs@pim-sre.lab
last_updated: 2024-05-18
tags:
  - navigation
  - docs
---

# Documentation Navigation Specification

## Purpose
Provide a single routing guide so GPT-5 agents and human maintainers can quickly determine which document, template, or tool applies to any incoming request or repository change.

## How to Use This Spec
- Start with the **Routing Matrix** to map the question to the appropriate document family.
- Consult the **Decision Checklist** to confirm prerequisites (naming, IDs, front matter, validations).
- Follow the **Escalation Paths** when existing documentation is insufficient or out of date.

## Routing Matrix

| Query Type | Primary Destination | Backup / Related Docs | Notes |
| --- | --- | --- | --- |
| High-level product vision or scope | `docs/Vison_and_Scope.md` | `docs/Requirements/Business_Requirements.md` | Use when clarifying objectives, stakeholders, or success metrics. |
| Business requirement updates | `docs/Requirements/Business_Requirements.md` | `docs/Id_Registry.md` | Allocate new `BR-###` IDs and update registry. |
| Functional capability changes | `docs/Requirements/Functional_Requirements.md` | `docs/templates/01_ADR_Template.md` | Use ADR if implementation changes architecture. |
| Non-functional/SLO updates | `docs/Requirements/Non_functional_requirements.md` | `docs/templates/02_RFC_Template.md`, `docs/04_GPT5_Working_Agreement.md` | Ensure SLO/SLI impacts are captured in RFC checklist. |
| Terminology or definitions | `docs/02_Glossary.md` | `docs/03a_Naming_And_Filenames.md` | Update glossary and cross-link the first usage in other docs. |
| Authoring guidance or style | `docs/03_Style_Guide.md` | `docs/03a_Naming_And_Filenames.md`, `.markdownlint.yaml` | Confirm tone, heading order, and formatting before drafting. |
| Naming or filename questions | `docs/03a_Naming_And_Filenames.md` | `.gpt/guardrails.yaml` | Ensure new files match regex and ID registry entries exist. |
| Template selection | `docs/35_Templates_Index.md` | `docs/templates/*.md` | Copy templates without renaming originals; register IDs in `docs/Id_Registry.md`. |
| GPT automation policy | `docs/04_GPT5_Working_Agreement.md` | `.gpt/guardrails.yaml`, `CODEOWNERS` | Verify protected paths and refusal rules. |
| Validation tooling | `Makefile` | `tools/validate_frontmatter.py`, `tools/validate_links.sh`, `tools/check_headings_order.py` | Run `make docs-validate` before submitting PRs. |
| CI status or workflow changes | `.github/workflows/docs-validate.yml` | `Makefile`, `tools/requirements.txt` | Ensure workflow mirrors local validation commands. |

## Decision Checklist
1. **Filename & ID**
   - New Markdown files follow `^\d{2}_[A-Z][A-Za-z0-9]*(?:_[A-Z][A-Za-z0-9]*)*\.md$`.
   - IDs allocated via `docs/Id_Registry.md` with reservation of 001–009 per family.
2. **Front Matter**
   - Include required fields (`title`, `doc_type`, `status`, `version`, `owners`, `last_updated`, `tags`) per `tools/frontmatter.schema.json`.
   - Validate with `make docs-frontmatter`.
3. **Content Standards**
   - Follow tone, headings, and examples defined in `docs/03_Style_Guide.md`.
   - For design docs ensure H2 order matches `docs/templates/00_Design_Doc_Template.md`; verify with `make docs-headings`.
4. **Validation**
   - Run `make docs-validate`; review summary in CI (`docs-validate` workflow) before requesting review.
5. **Governance**
   - Changes to protected documents require maintainer approval (see `.gpt/guardrails.yaml` and `CODEOWNERS`).

## Escalation Paths
- **Missing Content**: Draft new sections using the appropriate template and open a PR labeled `docs` plus any relevant IDs. Reference this spec in the PR description to confirm routing.
- **Conflicting Guidance**: File an ADR (using `docs/templates/01_ADR_Template.md`) describing the discrepancy and link the affected docs.
- **Tooling Issues**: Update or open issues for scripts under `tools/` and ensure Makefile targets remain in sync. CI failures should reference the `docs-validate` workflow run.

## Update Process
- Keep `last_updated` current whenever this spec changes.
- Coordinate modifications with documentation maintainers listed in front matter.
- For large structural changes, pair an ADR that records the decision to adjust navigation rules.

---

Last reviewed: 2024-05-18.
