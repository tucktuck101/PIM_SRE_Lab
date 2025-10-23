# API_Surface Applicable Requirements

This note summarizes the business, functional, and non-functional requirements that constrain or inform the API surface. Refer to it when designing endpoints, payloads, authentication, and operational guarantees.

## Business Requirements
- **BR-01** through **BR-16** — All business drivers shape the API surface: realistic workloads, safe synthetic data, scalability, observability, resilience, auditability, role boundaries, GitOps reproducibility, chaos readiness, operator learning, debugging, event consistency, failure visibility, and narratability.

## Functional Requirements (API-Focused Highlights)
- FR-01.x to FR-16.x & cross-cutting FR-X, FR-17.x, FR-18.x — Focus on requirements discussing APIs, request/response patterns, telemetry, auditing, roles, and narrative. This includes FR-03.x (stateless APIs), FR-06.x (observability), FR-07.x (auditing), FR-08.x (authorization/session context), FR-09.x (GitOps), FR-10.x (SLIs/SLO readiness), FR-11.x (chaos impacts), FR-13.x (drill-down debugging), FR-14.x (event consistency), FR-15.x (failure evidence), FR-16.x (journey documentation), FR-X.x (cross-cutting defaults), FR-17.x (retention), FR-18.x (guarded operations).

## Non-Functional Requirements (API-Focused Highlights)
- NFR-01 through NFR-37 — Pay attention to availability, latency, security, observability, deployment, storage, backup/restore, efficiency, chaos guardrails, and self-documenting observability. These requirements determine API SLO targets, authentication flows, monitoring, documentation, and resilience expectations.
