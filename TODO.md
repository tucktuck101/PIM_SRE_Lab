# Phase 0 – Documentation Guardrails and Authoring System
---

## [01] – `.markdownlint.yaml`
**Status:** Ready to review
**Goal:** Create baseline Markdown formatting rules for the repo.  
**Acceptance Criteria:**  
- `markdownlint` or `markdownlint-cli` runs with no errors on `README.md` or any sample doc.  
- Rules include: MD013 line length = 120, MD041 first-line heading required, ATX headings enforced, fenced code language required.  
- MD033 (inline HTML) disabled; all other rules enabled or justified inline.  
**References:** `docs/Vison_and_Scope.md`, `docs/02_Glossary.md`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:**  
 **Note for GPT-Codex** Configure exceptions for Mermaid and tables if needed.

---

## [02] – `.vale.ini`
**Status:** Ready to review
**Goal:** Add prose linting config for style and clarity.  
**Acceptance Criteria:**  
- `vale docs/` returns no fatal errors.  
- `StylesPath = .vale` and at least `write-good` style enabled at **warn** level.  
- Custom dictionary only if referenced in `.vale.ini`.  
**References:** `docs/` tree  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:**  
- Bootstrap `.vale/` folder (empty or with seed rules if referenced).

---

## [03] – `/docs/03_Style_Guide.md`
**Status:** Ready to review
**Goal:** Define canonical writing rules for all documents.  
**Acceptance Criteria:**  
- Specifies tone, units (SI with space), date format (ISO-8601), code fence language tags, link style, front matter keys, section order per doc type.  
- Includes filename regex reference and how headings are structured.  
- Contains examples and “do/don’t” pairs.  
**References:** BR/FR/NFR docs under `docs/Requirements/`  
**Blocked by:** [01], [02]  
**Parent Task:** N/A  
**Child Tasks:**  
- Add table mapping **doc types → required H2 sections**.

---

## [04] – `/docs/03a_Naming_And_Filenames.md`
**Status:** Ready to review
**Goal:** Publish filename regex + examples.  
**Acceptance Criteria:**  
- Presents regex: `^\d{2}_[A-Z][A-Za-z0-9]*(?:_[A-Z][A-Za-z0-9]*)*\.md$` and POSIX ERE equivalent.  
- Shows 5 valid and 5 invalid examples with brief reasons.  
- States where deviations are allowed (if any).  
**References:** [03]  
**Blocked by:** [03]  
**Parent Task:** N/A  
**Child Tasks:**  
- Cross-link to `Id_Registry.md`.

---

## [05] – `/docs/02_Glossary.md`
**Status:** Ready to review
**Goal:** Provide alphabetized one-line definitions with cross-links.  
**Acceptance Criteria:**  
- Alphabetized; internal links resolve; no duplicate terms.  
- Entries align with existing `docs/02_Glossary.md` content or supersede it; note deprecation of old file.  
**References:** `docs/02_Glossary.md` (source), BR/FR/NFR  
**Blocked by:** [03]  
**Parent Task:** N/A  
**Child Tasks:**  
- Add “Terms to add later” section with placeholders.

---

## [06] – `/docs/04_GPT5_Working_Agreement.md`
**Status:** Ready to review
**Goal:** Define operating rules for GPT-5 in this repo.  
**Acceptance Criteria:**  
- Lists allowed/protected paths, “PR only” rule for risky edits, ADR requirement for breaking changes.  
- Specifies output contract: PR body sections (summary, diff highlights, test plan).  
- Refusal rules when validators fail.  
**References:** [14] guardrails, [15] CODEOWNERS  
**Blocked by:** [03], [04]  
**Parent Task:** N/A  
**Child Tasks:**  
- Add example PR checklist snippet.

---

## [07] – `/docs/35_Templates_Index.md`
**Status:** Ready to review
**Goal:** Index all templates with purpose and links.  
**Acceptance Criteria:**  
- Table with columns **Name | Path | Purpose | Required?** with working relative links.  
- Includes `00_Design_Doc_Template`, `01_ADR_Template`, `02_RFC_Template`, `03_Runbook_Template`.  
**References:** [08], [09], [10], [11]  
**Blocked by:** [08], [09] (can stub), [10], [11]  
**Parent Task:** N/A  
**Child Tasks:**  
- Add section “How to choose a template”.

---

## [08] – `/docs/templates/00_Design_Doc_Template.md`
**Status:** Ready to review
**Goal:** Ship the standard design skeleton.  
**Acceptance Criteria:**  
- Fixed H2 order: Purpose; Scope and Non-Goals; Context and Constraints; Architecture Overview; Components; Interfaces and Contracts; Data Model; Security and Privacy; Reliability and Observability; Capacity and Performance; Failure Modes and Risks; Alternatives; Decision and Rationale; Rollout and Operations; Testing and Verification; Open Questions; Appendix.  
- Front matter fields present: title, doc_type, status, version, owners, last_updated, tags.  
**References:** [03], [18] schema  
**Blocked by:** [03]  
**Parent Task:** N/A  
**Child Tasks:**  
- Provide inline guidance bullets under each H2.

---

## [09] – `/docs/templates/01_ADR_Template.md`
**Status:** Ready to review
**Goal:** Establish decision record format.  
**Acceptance Criteria:**  
- Fields: ADR ID, Status, Context, Decision, Consequences, Rejected Options, Links.  
- Concise “Decision” line ≤ 200 chars.  
**References:** [13] Id Registry  
**Blocked by:** [13] (can stub)  
**Parent Task:** N/A  
**Child Tasks:**  
- Include example ADR header.

---

## [10] – `/docs/templates/02_RFC_Template.md`
**Status:** Ready to review
**Goal:** Define proposal format and lifecycle.  
**Acceptance Criteria:**  
- Lifecycle states: proposed | accepted | rejected | deprecated.  
- Sections: Motivation, Design, Alternatives, Rollout Plan, Success Criteria, Risks.  
**References:** [03]  
**Blocked by:** [03]  
**Parent Task:** N/A  
**Child Tasks:**  
- Add “When to write an RFC vs ADR” note.

---

## [11] – `/docs/templates/03_Runbook_Template.md`
**Status:** Ready to review
**Goal:** Provide standard ops response template.  
**Acceptance Criteria:**  
- Includes SLOs, alerts, dashboards, diagnostics, mitigation steps, communication, rollback, verification.  
- Checklist format with copy-paste-ready sections.  
**References:** NFRs (Availability, Latency), Observability Plan (later)  
**Blocked by:** [07]  
**Parent Task:** N/A  
**Child Tasks:**  
- Include sample placeholders for URLs.

---

## [12] – `/docs/Docs_Index.md`
**Status:** Ready to review
**Goal:** Single navigation index of all docs.  
**Acceptance Criteria:**  
- Groups by category (Requirements, Architecture, Data, Security, Ops, Templates).  
- All links valid; “Last updated” column reads from front matter if present; otherwise shows N/A.  
**References:** Entire `docs/` tree  
**Blocked by:** [03], [07], [08]–[11]  
**Parent Task:** N/A  
**Child Tasks:**  
- Add “Start here” pointers for new readers and GPT-5.

---

## [13] – `/docs/Id_Registry.md`
**Status:** Ready to review
**Goal:** Reserve canonical ID ranges and patterns.  
**Acceptance Criteria:**  
- Patterns: `BR-\d{3}`, `FR-\d{3}`, `NFR-\d{3}`, `ADR-\d{3}`.  
- Reserve 001–009 for bootstrap; include examples and allocation rules.  
**References:** Existing BR/FR/NFR files in `docs/Requirements/`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:**  
- Add “How to request an ID” steps.

---

## [14] – `.gpt/guardrails.yaml`
**Status:** Ready to review
**Goal:** Machine-enforced policy for GPT-5 edits.  
**Acceptance Criteria:**  
- Filename regex matches from [04].  
- `front_matter_required: true` with `$schema` pointing to `/tools/frontmatter.schema.json`.  
- Protected paths list includes `Docs_Index.md`, `Id_Registry.md`, `02_Glossary.md`; changes require `approved-adr` label.  
**References:** [06], [03], [04], [18]  
**Blocked by:** [06], [18]  
**Parent Task:** N/A  
**Child Tasks:**  
- Add deny-list for deleting docs.

---

## [15] – `/CODEOWNERS`
**Status:** Ready to review
**Goal:** Enforce review gates for sensitive areas.  
**Acceptance Criteria:**  
- Owners assigned for `*`, `/docs/**`, `/.gpt/**`, `/tools/**`.  
- Protected docs owned by primary maintainer.  
**References:** [14]  
**Blocked by:** [14]  
**Parent Task:** N/A  
**Child Tasks:**  
- Add backup owner if primary unavailable.

---

## [16] – `.github/PULL_REQUEST_TEMPLATE.md`
**Status:** Ready to review
**Goal:** Standard PR checklist for docs.  
**Acceptance Criteria:**  
- Checkboxes: front matter valid, links valid, headings order valid, IDs registered, style/lint passing.  
- Fields: Linked Issue/ADR, Affected IDs, Evidence (screens/mermaid URLs), Rollback Plan or N/A.  
**References:** [03], [18], [19], [20], [21], [22]  
**Blocked by:** [18]–[22]  
**Parent Task:** N/A  
**Child Tasks:**  
- Include “What changed and why” 3-bullet prompt.

---

## [17] – `.github/ISSUE_TEMPLATE/doc_task.yml`
**Status:** Ready to review
**Goal:** Structure incoming doc tasks.  
**Acceptance Criteria:**  
- Required fields: scope, target file path, sources/refs, acceptance criteria.  
- Dropdown for `doc_type` aligned with template types.  
- Auto-suggest filename matching regex from [04].  
**References:** [03], [07], [08]–[11]  
**Blocked by:** [07], [08]–[11]  
**Parent Task:** N/A  
**Child Tasks:**  
- Include “Blocked by” multi-select.

---

## [18] – `/tools/frontmatter.schema.json`
**Status:** Ready to review
**Goal:** JSON Schema to validate doc front matter.  
**Acceptance Criteria:**  
- Requires: `title`, `doc_type`, `status`, `version`, `owners`, `last_updated`, `tags`.  
- Patterns: SemVer for version, `YYYY-MM-DD` for dates, enum for `doc_type`.  
- `$id` and `$schema` present; validates with `jsonschema`.  
**References:** [03], [08]  
**Blocked by:** [03], [08]  
**Parent Task:** N/A  
**Child Tasks:**  
- Add examples folder with valid/invalid front matter.

---

## [19] – `/tools/validate_frontmatter.py`
**Status:** Ready to review
**Goal:** CLI validator for front matter against schema.  
**Acceptance Criteria:**  
- Scans `docs/**/*.md`; returns non-zero on invalid/missing fields.  
- Outputs file path and specific field errors.  
- No network access; pure local validation.  
**References:** [18]  
**Blocked by:** [18]  
**Parent Task:** N/A  
**Child Tasks:**  
- Add `requirements.txt` or use `pipx` in CI.

---

## [20] – `/tools/validate_links.sh`
**Status:** Ready to review
**Goal:** Detect broken Markdown links.  
**Acceptance Criteria:**  
- Non-zero exit on any unresolved local path.  
- Ignores `#` anchor-only links.  
- Works on macOS/Linux POSIX sh.  
**References:** `docs/Docs_Index.md`, `docs/`  
**Blocked by:** [12]  
**Parent Task:** N/A  
**Child Tasks:**  
- Optionally use `markdown-link-check` if installed; fall back to grep+test.

---

## [21] – `/tools/check_headings_order.py`
**Status:** Ready to review
**Goal:** Enforce required H2 order for design docs.  
**Acceptance Criteria:**  
- Reads H2s and compares against template from [08].  
- Fails fast with the first offending heading and expected sequence.  
**References:** [08]  
**Blocked by:** [08]  
**Parent Task:** N/A  
**Child Tasks:**  
- Add allow-list for non-design docs.

---

## [22] – `/Makefile`
**Status:** Ready to review
**Goal:** Single entrypoint for all validations.  
**Acceptance Criteria:**  
- Targets: `docs-frontmatter`, `docs-markdown`, `docs-links`, `docs-style`, `docs-validate`.  
- `docs-validate` depends on all other targets and fails on first error.  
- Works on macOS and Linux.  
**References:** [19], [20], [21]  
**Blocked by:** [19], [20], [21]  
**Parent Task:** N/A  
**Child Tasks:**  
- Add `help` target listing commands.

---

## [23] – `.github/workflows/docs-validate.yml`
**Status:** Ready to review
**Goal:** CI gate to enforce documentation quality.  
**Acceptance Criteria:**  
- Runs on PRs affecting `docs/**` or `*.md`.  
- Installs `markdownlint-cli`, `vale`, `jsonschema` (via pip), and optional `markdown-link-check`.  
- Executes `make docs-validate`.  
- Posts summary to `$GITHUB_STEP_SUMMARY`. Blocks merge on failure.  
**References:** [22]  
**Blocked by:** [22]  
**Parent Task:** N/A  
**Child Tasks:**  
- Add matrix for macOS and Ubuntu if desired.

---

## Notes
- After Phase 0 completes, create `SPEC.md` (navigation assistant for GPT-5 and humans) to explain how to route queries to the correct document.  
- Existing repo state:  
  - `Database_erd_mermaid.md`  
  - `docs/02_Glossary.md`  
  - `docs/Requirements/{Business_Requirements.md, Functional_Requirements.md, Non_functional_requirements.md}`  
  - `docs/Vison_and_Scope.md` (typo retained until naming conventions are enforced in Phase 0).

---

## [24] – `docs/02_Glossary.md`
**Status:** Ready to review
**Goal:** Resolve markdownlint violations in the glossary.  
**Acceptance Criteria:**  
- `markdownlint docs/02_Glossary.md` reports no MD013, MD022, MD025, or MD032 findings.  
- `make docs-markdown` completes without errors for this file.  
**References:** `docs/03_Style_Guide.md`, `.markdownlint.yaml`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:** N/A

---

## [25] – `docs/03_Style_Guide.md`
**Status:** Ready to review
**Goal:** Bring the style guide into compliance with markdownlint rules.  
**Acceptance Criteria:**  
- `markdownlint docs/03_Style_Guide.md` reports no MD013, MD022, MD025, or MD032 findings.  
- `make docs-markdown` completes without errors for this file.  
**References:** `.markdownlint.yaml`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:** N/A

---

## [26] – `docs/03a_Naming_And_Filenames.md`
**Status:** Ready to review
**Goal:** Fix lint issues in the naming policy document.  
**Acceptance Criteria:**  
- `markdownlint docs/03a_Naming_And_Filenames.md` reports no MD013, MD022, MD025, MD032, or MD040 findings.  
- `make docs-markdown` completes without errors for this file.  
**References:** `.markdownlint.yaml`, `docs/03_Style_Guide.md`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:** N/A

---

## [27] – `docs/04_GPT5_Working_Agreement.md`
**Status:** Ready to review
**Goal:** Align the GPT-5 agreement with markdownlint rules.  
**Acceptance Criteria:**  
- `markdownlint docs/04_GPT5_Working_Agreement.md` reports no MD013, MD022, MD025, MD031, MD032, or MD040 findings.  
- `make docs-markdown` completes without errors for this file.  
**References:** `.markdownlint.yaml`, `docs/03_Style_Guide.md`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:** N/A

---

## [28] – `docs/35_Templates_Index.md`
**Status:** Ready to review
**Goal:** Resolve markdownlint findings in the templates index.  
**Acceptance Criteria:**  
- `markdownlint docs/35_Templates_Index.md` reports no MD013, MD022, MD025, or MD032 findings.  
- `make docs-markdown` completes without errors for this file.  
**References:** `.markdownlint.yaml`, `docs/03_Style_Guide.md`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:** N/A

---

## [29] – `docs/Docs_Index.md`
**Status:** Ready to review
**Goal:** Clear markdownlint issues on the documentation index.  
**Acceptance Criteria:**  
- `markdownlint docs/Docs_Index.md` reports no MD013 or MD025 findings.  
- `make docs-markdown` completes without errors for this file.  
**References:** `.markdownlint.yaml`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:** N/A

---

## [30] – `docs/Id_Registry.md`
**Status:** Ready to review
**Goal:** Fix lint violations in the ID registry.  
**Acceptance Criteria:**  
- `markdownlint docs/Id_Registry.md` reports no MD013, MD022, MD025, or MD032 findings.  
- `make docs-markdown` completes without errors for this file.  
**References:** `.markdownlint.yaml`, `docs/03_Style_Guide.md`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:** N/A

---

## [31] – `docs/Requirements/Business_Requirements.md`
**Status:** Ready to review
**Goal:** Resolve markdownlint spacing/length issues in the business requirements.  
**Acceptance Criteria:**  
- `markdownlint docs/Requirements/Business_Requirements.md` reports no MD013 or MD022 findings.  
- `make docs-markdown` completes without errors for this file.  
**References:** `.markdownlint.yaml`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:** N/A

---

## [32] – `docs/Requirements/Functional_Requirements.md`
**Status:** Ready to review
**Goal:** Align functional requirements with markdownlint rules.  
**Acceptance Criteria:**  
- `markdownlint docs/Requirements/Functional_Requirements.md` reports no MD003, MD013, or MD022 findings.  
- `make docs-markdown` completes without errors for this file.  
**References:** `.markdownlint.yaml`, `docs/03_Style_Guide.md`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:** N/A

---

## [33] – `docs/Requirements/Non_functional_requirements.md`
**Status:** Ready to review
**Goal:** Clear lint issues in the non-functional requirements.  
**Acceptance Criteria:**  
- `markdownlint docs/Requirements/Non_functional_requirements.md` reports no MD003, MD013, or MD022 findings.  
- `make docs-markdown` completes without errors for this file.  
**References:** `.markdownlint.yaml`, `docs/03_Style_Guide.md`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:** N/A

---

## [34] – `docs/Vison_and_Scope.md`
**Status:** Pending
**Goal:** Address markdownlint findings in the vision and scope document.  
**Acceptance Criteria:**  
- `markdownlint docs/Vison_and_Scope.md` reports no MD013, MD022, or MD032 findings.  
- `make docs-markdown` completes without errors for this file.  
**References:** `.markdownlint.yaml`, `docs/03_Style_Guide.md`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:** N/A

---

## [35] – `docs/templates/00_Design_Doc_Template.md`
**Status:** Pending
**Goal:** Ensure the design doc template satisfies markdownlint rules.  
**Acceptance Criteria:**  
- `markdownlint docs/templates/00_Design_Doc_Template.md` reports no MD022, MD025, or MD036 findings.  
- `make docs-markdown` completes without errors for this file.  
**References:** `.markdownlint.yaml`, `docs/03_Style_Guide.md`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:** N/A

---

## [36] – `docs/templates/01_ADR_Template.md`
**Status:** Pending
**Goal:** Resolve lint violations in the ADR template.  
**Acceptance Criteria:**  
- `markdownlint docs/templates/01_ADR_Template.md` reports no MD013, MD022, MD025, or MD036 findings.  
- `make docs-markdown` completes without errors for this file.  
**References:** `.markdownlint.yaml`, `docs/03_Style_Guide.md`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:** N/A

---

## [37] – `docs/templates/02_RFC_Template.md`
**Status:** Pending
**Goal:** Bring the RFC template into compliance with markdownlint rules.  
**Acceptance Criteria:**  
- `markdownlint docs/templates/02_RFC_Template.md` reports no MD022, MD025, MD032, or MD036 findings.  
- `make docs-markdown` completes without errors for this file.  
**References:** `.markdownlint.yaml`, `docs/03_Style_Guide.md`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:** N/A

---

## [38] – `docs/templates/03_Runbook_Template.md`
**Status:** Pending
**Goal:** Fix markdownlint issues in the runbook template.  
**Acceptance Criteria:**  
- `markdownlint docs/templates/03_Runbook_Template.md` reports no MD022, MD025, or MD036 findings.  
- `make docs-markdown` completes without errors for this file.  
**References:** `.markdownlint.yaml`, `docs/03_Style_Guide.md`  
**Blocked by:** None  
**Parent Task:** N/A  
**Child Tasks:** N/A
