# Domain_Model_UML Applicable Requirements

This note captures the business, functional, and non-functional requirements that the domain model (UML) must honor. Use it while defining entities, relationships, aggregates, value objects, and invariants.

## Business Requirements
- **BR-01** through **BR-16** — All business drivers listed in the requirements catalog define entity responsibilities, data sensitivity, audit needs, event flow, observability, and educational narrative expectations.

## Functional Requirements (Entity & Domain Modeling Highlights)
- Key FRs from the requirements catalog that affect domain modeling, data lineage, auditing, observability, event consistency, and educational narrative. In particular: FR-01.x (data generation), FR-02.x (schema/data handling), FR-03.x (stateless APIs/sharding), FR-04.x (routing/locality), FR-05.x (resilience), FR-06.x (observability), FR-07.x (audit/temporal), FR-08.x (roles/authorization), FR-09.x (GitOps), FR-10.x (SLIs), FR-11.x (chaos), FR-14.x (event consistency), FR-15.x (failure evidence), FR-16.x (request journey/data lineage), FR-X.x (cross-cutting defaults), FR-17.x (retention), FR-18.x (controlled operations).

## Non-Functional Requirements (Entity Responsibilities & Operations)
- Relevant NFRs spanning availability, latency, security, observability, DR, operational readiness, and compliance (NFR-01 through NFR-37). These govern entity lifecycle, consistency, testing, backup, audit, and documentation expectations.
