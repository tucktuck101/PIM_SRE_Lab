title: PIM SRE Lab Core Platform Design
doc_type: design_doc
status: draft
version: 0.2.0
owners:
  - docs@pim-sre.lab
last_updated: 2025-05-19
tags:
  - design
---

# Purpose

Deliver a reference architecture for the PIM SRE Lab that demonstrates national-scale healthcare workloads while remaining safe for synthetic data (BR-01, BR-02, BR-16). The design aligns infrastructure, services, and operations so the lab can exercise SRE practices, validate reliability metrics, and narrate end-to-end system behavior (BR-06, BR-10, FR-10.1).

## Scope and Non-Goals

- **In scope:** Authoritative blueprint for application services, data layer, and platform infrastructure spanning request ingress to observability pipelines (BR-03, FR-03.1, FR-06.5).  
- **In scope:** Security, audit, and compliance controls necessary to satisfy multi-role access, traceability, and retention requirements (BR-07, FR-07.1, NFR-21).  
- **In scope:** Operational workflows covering GitOps automation, chaos readiness, SLO management, and educational storytelling (BR-09, BR-11, FR-09.1, FR-11.2).  
- **Out of scope:** Low-level implementation details of individual microservices, UI/UX design, and environment-specific cost modeling; these will be captured in service design docs or runbooks.  
- **Out of scope:** Non-healthcare workloads and third-party integrations not listed in the requirements baseline (BR-01, BR-04).  

## Context and Constraints

- The lab must simulate realistic patient, clinician, admin, and SRE personas using configurable traffic profiles (FR-01.2, FR-01.4).  
- All data must remain synthetic, pseudonymized, and compliant with privacy guardrails, with no path to re-identification (BR-02, FR-02.1, NFR-24).  
- Deployments run on two kubeadm clusters with GitOps-based configuration management; infrastructure changes must be reproducible from source (BR-03, BR-09, FR-09.1).  
- Observability, auditability, and documentation must be first-class outputs for both humans and GPT agents (BR-06, BR-07, BR-12, BR-16, NFR-32).  
- System operations must tolerate chaos experiments and planned fault injection without breaching SLOs or compromising state (BR-05, BR-11, FR-11.1, NFR-34).  

## Architecture Overview

Traffic flows begin at an ingress gateway that authenticates personas, routes requests to stateless API surfaces, and enforces shard-aware routing policies (FR-04.1, FR-08.1). Domain-aligned microservices execute healthcare scenarios, emitting events via an outbox pattern to a message backbone that feeds downstream projections and analytics (FR-14.1, FR-14.2).  
Stateful workloads reside in a sharded SQL Server topology with Always On availability groups and backup tooling to meet RPO/RTO expectations (BR-04, BR-05, FR-04.3, FR-17.2).  
Observability spans MELTP signals (metrics, events, logs, traces, profiles) funneled into Grafana, Loki, Tempo, and Pyroscope, with dashboards tailored for each persona and scenario (FR-06.3, FR-06.5, NFR-33).  
GitOps controllers reconcile manifests for infrastructure and applications, while CI/CD pipelines promote changes through dev, stage, and demo environments under release guardrails (FR-09.1, FR-10.2, NFR-11).  

## Components

- **Ingress & API Gateway** — Terminates TLS, enforces JWT/session context, and applies shard routing rules; integrates with observability annotations for every request (FR-04.1, FR-06.2, FR-08.2).  
- **Persona Simulation Engine** — Generates configurable traffic mixes and arrival patterns to exercise BR-01 and FR-01.x scenarios; emits telemetry for each persona journey.  
- **Clinical & Billing Services** — Stateless microservices implementing CRUD flows, orchestrations, and domain logic, persisting to shard-aware repositories (FR-03.1, FR-04.3).  
- **Event Platform** — Outbox processors, Kafka-compatible topics, and consumers providing eventual consistency and downstream projections (FR-14.2, FR-14.4).  
- **Data Platform** — SQL Server primary, read replicas, partitioned storage, and archival pipelines satisfying retention and compliance obligations (FR-04.3, FR-17.1, NFR-23).  
- **Observability Stack** — Prometheus/Grafana metrics, Loki logs, Tempo traces, Pyroscope profiles, plus SLO tooling aligned with FR-06.x, FR-10.x, and NFR-33.  
- **Automation & GitOps** — Flux/Argo controllers, CI/CD pipelines, and ADR-backed config repositories ensuring reproducibility and audit trails (BR-09, FR-09.1, FR-07.1).  

## Interfaces and Contracts

- RESTful APIs expose patient, encounter, billing, and admin endpoints; each operation documents idempotency, authentication, and MELTP expectations (FR-03.4, FR-06.2, FR-08.1).  
- Event schemas follow the domain event catalog with versioned payloads and explicit retention policies to maintain temporal replay fidelity (FR-14.3, FR-17.3).  
- Administrative interfaces expose GitOps workflows and audit queries for SRE operators, respecting role separation and least privilege (FR-08.2, FR-07.3).  
- Contracts are versioned semantically; backward-compatible changes follow additive patterns, while breaking changes mandate ADR approval and deprecation schedules (BR-16, FR-X.1).  

## Data Model

The core entities include Patients, Providers, Facilities, Encounters, Diagnoses, Procedures, Medications, and Claims derived from FR-01.1 seed datasets. Relationships enforce shard locality via patient identifiers, while temporal history tables capture before/after states for audits (FR-04.1, FR-07.2). Analytical projections create read-optimized tables and materialized views for dashboards and SLO calculations, adhering to retention rules (FR-14.4, FR-17.1, NFR-21). Sensitive attributes remain pseudonymized and hashed with irreversible tokens to satisfy privacy constraints (BR-02, FR-02.3).

## Security and Privacy

Authentication uses OIDC-backed tokens mapped to personas; authorization leverages Kubernetes RBAC and service-level checks to uphold multi-role boundaries (BR-08, FR-08.1).  
Row-level security and attribute-based access control enforce shard and persona segregation across services and data stores (FR-08.3, FR-08.4).  
Audit trails capture request IDs, user IDs, actions, and before/after states, stored in immutable append-only logs with retention aligned to NFR-23 (FR-07.1, FR-07.3).  
Data classification tags each dataset (synthetic PHI-like, operational metadata, observability telemetry) and defines masking or redaction rules for exports (FR-02.3, NFR-24).  

## Reliability and Observability

Service SLIs focus on latency, availability, and error ratios per persona journey, derived from the SLI/SLO measurement plan (FR-10.1, FR-10.2, NFR-01).  
Each component emits MELTP signals with consistent labels, correlating traces, logs, and metrics for rapid debugging (BR-06, FR-06.5, FR-13.1).  
Alerting follows multi-window burn rates and ties directly to runbook automation; annotations mark deployments, chaos experiments, and failovers (FR-10.3, NFR-33, NFR-34).  
Synthetic monitors and canaries validate flows continuously, feeding dashboards that narrate the story for both humans and GPT agents (BR-12, BR-16, NFR-36).  

## Capacity and Performance

Baseline load models simulate peak clinic traffic, billing bursts, and overnight processing with configurable concurrency and think times (BR-01, FR-01.4).  
Stateless services scale horizontally via HPA, while stateful tiers rely on shard expansion and read replicas; autoscaling policies observe CPU, latency, and custom SLO signals (BR-03, FR-03.2, FR-03.3).  
Performance targets include <300 ms p95 API latency under peak, zero data loss during failover, and ability to replay 24 hours of events within NFR-08 boundaries.  
Capacity reviews occur quarterly, using production-like telemetry stored per NFR-27, and feed ADRs when architectural adjustments are needed.  

## Failure Modes and Risks

- **Cluster or node loss:** Mitigated by multi-zone node pools, pod disruption budgets, and automated rescheduling (BR-05, FR-05.1, NFR-03).  
- **Primary database outage:** Handled via automatic AG failover, connection retries, and read replica promotion procedures (FR-05.2, FR-05.3, NFR-05).  
- **Event backlog or DLQ growth:** Addressed through autoscaling processors, alert thresholds, and replay tooling with audit traceability (FR-14.5, NFR-18).  
- **Misconfigured deployment:** Prevented by GitOps policies, preview environments, and automated rollback/feature flag support (FR-09.2, NFR-12).  
- **Observability blind spots:** Guarded by MELTP coverage dashboards, telemetry schema validation, and weekly audits (FR-06.5, NFR-32).  

## Alternatives

- **Single-cluster topology:** Rejected because it cannot demonstrate cross-cluster failover scenarios required by BR-05 and BR-11.  
- **Direct database integration without events:** Dismissed due to limited auditability and inability to model eventual consistency stories mandated by FR-14.x.  
- **Manual deployments:** Set aside because they undermine GitOps reproducibility (BR-09) and fail to produce audit trails demanded by FR-07.1.  

## Decision and Rationale

Adopt a modular, GitOps-driven microservice architecture on dual Kubernetes clusters with sharded data services and full-stack observability. This approach maximizes alignment with the BR/FR/NFR set, enables rapid experimentation, and keeps operational stories transparent for both humans and AI partners (BR-03, BR-06, FR-09.1, NFR-32).

## Rollout and Operations

Initial rollout seeds dev and stage clusters via GitOps, validating infrastructure, persona simulation, and observability wiring before enabling full workloads (FR-09.1, NFR-11).  
Production-like demonstrations promote changes through staged PRs with required reviews from platform and observability owners (FR-08.2, FR-10.3).  
On-call SREs maintain runbooks, chaos schedules, and recovery drills; weekly ops reviews ensure documentation, dashboards, and ADRs remain current (BR-11, FR-11.2, NFR-35).  
Operational ownership rotates between human SREs and GPT agents, guided by the GPT Working Agreement and ADR governance.  

## Testing and Verification

- Unit and contract tests run per service to enforce API and event schema compatibility (FR-03.4, FR-14.3).  
- Integration suites validate end-to-end personas across API, event, and data layers with synthetic datasets (FR-01.3, FR-06.1).  
- Load tests benchmark peak scenarios and validate autoscaling thresholds against SLO budgets (BR-01, NFR-02).  
- Chaos experiments inject pod failures, latency, and network partitions to verify resilience objectives (BR-05, FR-11.1, NFR-34).  
- Release gates require `make docs-validate`, telemetry checks, and SLO dashboards to be green before promotion (FR-10.2, NFR-12).  

## Open Questions

- Confirm identity provider integration approach that balances synthetic personas with realistic auth flows (FR-08.1, NFR-19).  
- Finalize tooling for automated ADR updates when architecture decisions occur during releases.  
- Determine long-term storage costs for full MELTP retention while meeting NFR-21 and NFR-27.  
- Validate whether additional external partner systems are required to broaden system context narratives (BR-16).  

## Appendix

- Placeholder for C4 diagrams once drafted (Tasks [57]–[59]).  
- Link to requirements summary: `docs/requirements/notes/Design_Doc_Applicable_Requirements.md`.  
- Reference ADR index and upcoming ADRs documenting shard strategy, GitOps workflows, and observability defaults.

---

_#### Changelog

Last updated: 2025-05-19 (update before publishing)_
