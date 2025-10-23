---
title: ID Registry
doc_type: policy
status: draft
version: 0.1.0
owners:
  - docs@pim-sre.lab
last_updated: 2024-05-18
tags:
  - governance
  - identifiers
---

# ID Registry

Canonical registry for scoped document and artifact identifiers used across
the PIM SRE Lab. This registry prevents collisions, documents reserved
ranges, and links each ID family to its owning templates or requirement
sets.

## Identifier Families

| ID Family | Pattern | Description | Reserved Range | Allocation Notes |
| --- | --- | --- | --- | --- |
| Business Requirements | `BR-\d{3}` | Business requirement statements that frame project scope. | `BR-001`–`BR-009` | Assign sequentially starting at `BR-010`.<br>Reference `docs/Requirements/Business_Requirements.md`. |
| Functional Requirements | `FR-\d{3}` | Functional capabilities required by the system. | `FR-001`–`FR-009` | Assign sequentially starting at `FR-010`.<br>Link to `docs/Requirements/Functional_Requirements.md`. |
| Non-Functional Requirements | `NFR-\d{3}` | Reliability, performance, and compliance requirements. | `NFR-001`–`NFR-009` | Assign sequentially starting at `NFR-010`.<br>Link to `docs/Requirements/Non_functional_requirements.md`. |
| Architecture Decision Records | `ADR-\d{3}` | Decisions documented using the ADR template. | `ADR-001`–`ADR-009` | Assign sequentially starting at `ADR-010`.<br>Use `docs/templates/01_ADR_Template.md`. |

## Allocation Rules

- IDs are immutable once assigned; do not reuse retired IDs.
- Maintain ascending order with zero-padded three-digit numbers.
- Document the allocation in the source file (requirements doc, ADR) and
  update this registry in the same pull request.
- Reserve IDs `001`–`009` in each family for foundational bootstrap decisions
  and early adoption testing.

## How to Request an ID

1. Determine the appropriate family (BR, FR, NFR, ADR) based on the document
   type.
2. Check this registry to find the next available number (≥ `010` unless
   otherwise authorized).
3. Add the new entry to this table in numeric order, including description
   and link to the target document.
4. Update the corresponding document (e.g., requirement, ADR) with the
   assigned ID in its front matter or heading.
5. Submit both updates in the same PR. If the change affects a protected
   document, follow the [GPT-5 Working Agreement](04_GPT5_Working_Agreement.md)
   for approval steps.

---

Last reviewed: 2024-05-18.
