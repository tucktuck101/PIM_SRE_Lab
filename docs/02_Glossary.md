---
title: PIM SRE Glossary
doc_type: glossary
status: draft
version: 0.1.0
owners:
  - docs@pim-sre.lab
last_updated: 2024-05-18
tags:
  - glossary
  - documentation
---

# PIM SRE Glossary

This glossary replaces the legacy `docs/Glossary.md` file.
Terms are alphabetized and include cross-links to related guidance where available.

## Usage Notes

- Treat this file as the single source of truth for platform terminology;
  update it before introducing new words or abbreviations in docs or
  prompts.
- When drafting content (human or GPT-Codex), reuse the canonical term
  names and abbreviations exactly as listed here.
- Cross-link the first occurrence of a term in new documents back to this
  glossary when it aids navigation (`[Term](02_Glossary.md#term-in-kebab-case)`).
- For new concepts, add them here in alphabetical order and document any
  accepted synonyms to prevent drift.

## A

**Admin (Application Administrator)**  
Application administrator role with organization-wide CRUD capability
through sanctioned workflows. Related runbooks: forthcoming runbook
templates in `docs/templates/03_Runbook_Template.md`.

**Always On Availability Group (AG)**  
SQL Server high-availability feature that provides failover and readable replicas across shards.

**Alloy (Grafana Alloy)**  
Unified Grafana agent that collects and forwards metrics, logs, and traces from both clusters.

**Appointment**  
Scheduled patient–provider interaction managed by the core API; used to stress concurrency and audit logging.

**Argo CD**  
GitOps controller that applies declarative manifests, detects drift, and automates rollback for the lab clusters.

**Audit Event**  
Record of who changed what, when, and how. In this platform, each mutation
logs before/after JSON, request ID, and user ID for traceability.

**Audit Policy**  
Retention and review standard for audit data. In this platform, it defines
storage duration, rotation, and integrity verification expectations.

## B

**Billing Claim**  
Synthetic reimbursement request linked to encounters and procedure codes;
used for workload diversity and observability demos.

## C

**CDC (Change Data Capture)**  
SQL Server change feed powering projection updates and Grafana reporting.

**Chaos Experiment**  
Intentional failure injection to validate resilience and error budgets; documented in future runbooks.

**CI/CD Pipeline**  
Automated workflow that builds, tests, scans, and deploys platform components.

**Command Queue**  
Service Broker-backed queue storing pending write operations to ensure atomic processing.

**Core API (Core-API)**  
Authoritative write service in the CQRS split; validates commands, updates the database, and emits audit events.

**CQRS (Command Query Responsibility Segregation)**  
Architecture pattern separating write commands from read projections; core to lab service design.

## D

**Diagnosis (ICD-10)**  
Coded classification of diseases and conditions. In this platform, sourced
from ICD-10 and referenced by `ENCOUNTER_DIAGNOSIS` for analytics.

**Domain Event**  
Message describing a significant state change (e.g., `PatientUpdated`) consumed by projection workers.

## E

**Edge API (Edge-API)**  
Read-only service that serves safe projections; cannot mutate state and is optimized for observability consumers.

**Encounter**  
Recorded patient–provider interaction that links diagnoses, procedures, and
billing data; primary telemetry correlation node.

**Error Budget**  
Allowed failure margin within an SLO window; informs chaos testing cadence.

**Event**  
Discrete system state change. In this platform, includes both domain and
system events published to Grafana Loki or Mimir.

## F

**Facility**  
Logical grouping for providers and the boundary for row-level security enforcement.

## G

**GitOps**  
Operating model treating Git as the source of truth for infrastructure and configuration.

## H

**HCPCS Code**  
Healthcare Common Procedure Coding System identifier; used for synthetic billing scenarios.

**Helm Chart**  
Kubernetes packaging format parameterizing SQL AG, APIs, and observability stack deployments.

## I

**Incident**  
Any event that breaches an SLO. Logged automatically with correlation to request ID and shard routing data.

## J

**JWT (JSON Web Token)**  
Compact credential issued by the authentication layer; claims populate SQL session context for authorization decisions.

## K

**Kaladesh Server**  
Local Kubernetes cluster hosting application pods, SQL Server AG replicas, and the synthetic load generator.

**Kubernetes (K8s)**  
Container orchestration platform managing workloads, scaling, and self-healing for the lab.

## L

**Load Generator**  
Traffic driver that simulates patient, clinician, and admin workflows; also orchestrates chaos scenarios.

**Log**  
Timestamped record of application activity. In this platform, structured
JSON logs carry `trace_id`, `span_id`, and `request_id`.

**Loki**  
Grafana log aggregation backend storing structured JSON logs with correlation identifiers.

## M

**MacBook Cluster**  
Developer-hosted cluster running Grafana observability components.

**Materialized View**  
Precomputed read model persisted for performance-critical queries served by the edge API.

**Medication (NDC)**  
National Drug Code identifier for medications. In this platform, captures
brand, generic, and manufacturer metadata in `MEDICATION_NDC`.

**MELTP**  
Acronym for Metrics, Events, Logs, Traces, Profiles—the mandatory observability signal set.

**Metric**  
Time-series measurement (latency, throughput, queue depth) stored in Grafana Mimir.

**Mimir**  
Grafana metrics backend storing time-series data emitted by services and DB workloads.

**MTBF (Mean Time Between Failures)**  
Average interval between recoverable incidents derived from chaos logs.

**MTTR (Mean Time to Recovery)**  
Average duration to restore service after an incident; target is under 60 seconds for single pod failures.

## O

**Outbox Pattern**  
Pattern ensuring reliable event publishing from transactional writes. Each
write stores a domain event in the OUTBOX table before workers publish it.

## P

**Patient**  
Person receiving care; primary sharding key (`patient_id`) and tenancy boundary.

**Pod Kill Survivability**  
Capability of workloads to remain available after random pod termination; core SRE success metric.

**Procedure (ICD-10-PCS)**  
Standardized code describing medical operations. In this platform, used in
`ENCOUNTER_PROCEDURE` and `CLAIM_LINE` for billing simulations.

**Profile**  
Continuous performance sample (CPU, memory) collected by Grafana Pyroscope.

**Projection / Read Model**  
Materialized view optimized for queries. Built by CDC projectors to feed Grafana dashboards and the edge API.

**Provider**  
Licensed healthcare professional linked to facilities and encounters within the platform.

**PVC (Persistent Volume Claim)**  
Kubernetes storage request defining capacity and access modes for SQL replicas.

**Postmortem**  
Structured analysis conducted after incident resolution. Generated from Grafana annotations and audit data.

**Pyroscope**  
Grafana profiling backend that stores CPU and memory profiles for analysis.

## R

**RBAC (Role-Based Access Control)**  
Permission model mapping roles (`patient`, `clinician`, `admin`, `sre`) to authorized actions.

**RBAC Matrix**  
Tabular view describing role scope, permitted actions, and access channels
for patient, clinician, admin, and SRE personas.

**RLS (Row-Level Security)**  
SQL Server feature enforcing per-user row visibility based on session context attributes.

**Router Shard Map**  
Lookup table directing requests to the correct SQL shard using `patient_id` ranges or hashes.

**Runbook**  
Operational guide describing recovery or maintenance procedures; see `docs/templates/03_Runbook_Template.md` (pending).

## S

**Service Broker (SB)**  
SQL Server component providing reliable, transactional message handling for command and event queues.

**Session Context**  
SQL Server key-value metadata populated with user identity and scope for authorization checks.

**Shard Key**  
Field used to route data to the correct shard; always `patient_id` in this lab.

**Sharding**  
Horizontal partitioning strategy distributing data across multiple SQL Server shards.

**Site Reliability Engineer (SRE)**  
Primary lab operator responsible for reliability, automation, chaos testing, and observability management.

**SLI (Service Level Indicator)**  
Quantitative measure used to track performance against an SLO (e.g., success rate, latency p95, failover time).

**SLO (Service Level Objective)**  
Target reliability threshold (latency, availability, error rate) tracked for each API and shard.

**StatefulSet**  
Kubernetes controller providing stable network IDs and storage for stateful workloads, including SQL Server pods.

## T

**Tempo**  
Grafana distributed tracing backend capturing OpenTelemetry spans end to end.

**Temporal Table**  
SQL Server table with system-versioned history for immutable audit trails.

**Trace**  
End-to-end request representation captured and stored in Tempo; correlated with logs and metrics.

## Terms to Add Later

- Data Residency
- Edge Cache
- Front Matter Validator
- Observability Pipeline
- Synthetic Dataset

---

Last reviewed: 2024-05-18.
