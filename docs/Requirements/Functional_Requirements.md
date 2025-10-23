---
title: Functional Requirements
doc_type: policy
status: draft
version: 0.1.0
owners:
  - product@pim-sre.lab
last_updated: 2024-05-18
tags:
  - requirements
  - functional
---

## Functional Requirements (FRD)

**Frame:** Flat list. Each FR includes explicit traceability to Business
Requirements via `BR Refs:`. Style = **MUST + expected defaults**
(portfolio-grade).

---

### BR-01 — Realistic national-scale workload simulation

**FR-01.1** The system SHALL generate Mockaroo-based seed datasets for
patients, providers, facilities, encounters, diagnoses, procedures,
medications, and claims.  
*BR Refs:* BR-01, BR-02

**FR-01.2** The load generator SHALL simulate three user profiles (patient,
clinician, admin) with configurable arrival rates, concurrency, and
think-time.  
*BR Refs:* BR-01, BR-11

**FR-01.3** The system SHALL provide role-specific operation mixes (read %
vs write %, heavy-read for patients, mixed for clinicians, admin-heavy
maintenance).  
*BR Refs:* BR-01

**FR-01.4** The system SHALL support traffic shape presets (e.g., weekday
clinic peak, night lull, end-of-month billing burst).  
*BR Refs:* BR-01

**FR-01.5** The system SHOULD expose a single YAML profile to define dataset
size, shard counts, and traffic patterns.  
*BR Refs:* BR-01

---

### BR-02 — Safe operation without real PHI

**FR-02.1** All seed data MUST be synthetic, pseudonymized, and non-reversible to
real individuals.  
*BR Refs:* BR-02

**FR-02.2** The platform SHALL block ingestion of external identifiers beyond the
defined synthetic schema.  
*BR Refs:* BR-02

**FR-02.3** Exports and logs SHALL exclude sensitive fields or present them in
masked form per allowlist.  
*BR Refs:* BR-02, BR-06

**FR-02.4** The system SHALL provide redaction for audit/event payloads where
fields are not required for troubleshooting.  
*BR Refs:* BR-02, BR-07

---

### BR-03 — Horizontal scalability without redesign

**FR-03.1** The APIs SHALL be stateless and horizontally scalable via HPA.  
*BR Refs:* BR-03

**FR-03.2** The database layer SHALL scale via sharding and SQL Server AG
read replicas without schema change.  
*BR Refs:* BR-03, BR-04

**FR-03.3** The system SHALL externalize configuration (replica counts,
shard count, listener DSNs) via environment or Helm values.  
*BR Refs:* BR-03

**FR-03.4** The system SHALL maintain idempotent writes to tolerate retries
under scale.  
*BR Refs:* BR-03

---

### BR-04 — Shard-based routing and locality

**FR-04.1** The router SHALL deterministically route requests by `patient_id` to the correct shard  
                        listener.
*BR Refs:* BR-04

**FR-04.2** The router SHALL support shard map updates without downtime (hot reload or versioned config).  
*BR Refs:* BR-04

**FR-04.3** Read requests SHOULD prefer read-only replicas; write requests MUST target the primary.  
*BR Refs:* BR-04, BR-05

**FR-04.4** The system SHALL expose a health endpoint that verifies shard reachability and listener status.  
*BR Refs:* BR-04

---

### BR-05 — Failure resilience

**FR-05.1** The platform SHALL continue serving traffic during arbitrary pod kill of any single API pod.  
*BR Refs:* BR-05

**FR-05.2** The data tier SHALL continue serving reads during primary failover and recover write capability  
                        automatically.
*BR Refs:* BR-05

**FR-05.3** The system SHALL retry transient DB errors with exponential backoff and timeouts.  
*BR Refs:* BR-05

**FR-05.4** An SRE-operated chaos interface SHALL support injections: pod kill, network delay, DB failover,  
                        replica drain.
*BR Refs:* BR-05, BR-11

**FR-05.5** The platform SHALL publish failover events to observability for incident correlation.  
*BR Refs:* BR-05, BR-06

---

### BR-06 — Full observability (MELTP)

**FR-06.1** Each request SHALL emit a trace with unique `trace_id` propagated across edge-api, core-api,  
                        and DB spans.
*BR Refs:* BR-06

**FR-06.2** Structured logs SHALL include `trace_id`, `span_id`, `request_id`, `user_id` (if present), and  
                        role.
*BR Refs:* BR-06

**FR-06.3** Metrics SHALL include RED (rate, errors, duration) per endpoint and shard; DB metrics SHALL  
                        include waits and replica role.
*BR Refs:* BR-06

**FR-06.4** Profiles (CPU/mem) SHALL be captured for APIs under load with symbolized stack frames.  
*BR Refs:* BR-06

**FR-06.5** No code path SHALL execute without at least one MELTP signal produced (“no orphan telemetry”).  
*BR Refs:* BR-06

---

### BR-07 — Auditable accountability

**FR-07.1** Every write operation SHALL produce an `AUDIT_EVENT` containing actor, role, action, object  
                        type/id, before/after JSON, and timestamps.
*BR Refs:* BR-07

**FR-07.2** Core tables (Patient, Appointment, Encounter, Medication Order, Claim, Claim Line) SHALL be  
                        system-versioned (temporal).
*BR Refs:* BR-07

**FR-07.3** Audit and temporal history SHALL be queryable by `request_id` and `user_id`.  
*BR Refs:* BR-07

**FR-07.4** The system SHALL reject write requests missing `user_id` and `request_id` in session context.  
*BR Refs:* BR-07

---

### BR-08 — Multi-role security boundaries

**FR-08.1** The platform SHALL implement three application roles: `patient`, `clinician`, `admin`, and a  
                        dedicated operator role: `sre`.
*BR Refs:* BR-08

**FR-08.2** Row-Level Security (RLS) SHALL enforce patient-only visibility for `patient` role and facility-  
                        scoped visibility for `clinician`.
*BR Refs:* BR-08

**FR-08.3** `admin` role SHALL have application-level CRUD and user admin via app procedures only. The  
                        `sre` role SHALL have full read/write and ops via secured procedures.
*BR Refs:* BR-08, BR-07

**FR-08.4** Session context SHALL be set from JWT at connection open and refreshed per request.  
*BR Refs:* BR-08

---

### BR-09 — GitOps reproducibility

**FR-09.1** All manifests, schema migrations, and configs SHALL live in Git with versioned environments.  
*BR Refs:* BR-09

**FR-09.2** One command (or Argo CD sync) SHALL recreate a working environment end-to-end.  
*BR Refs:* BR-09

**FR-09.3** Database migrations SHALL be idempotent and forward-only with rollback scripts when feasible.  
*BR Refs:* BR-09

**FR-09.4** Seed and demo data generation SHALL be deterministic via pinned seeds and versions.  
*BR Refs:* BR-09, BR-01

---

### BR-10 — SLO-ready signals

**FR-10.1** The system SHALL expose golden signals for availability, latency (p50/p95/p99), and error rate  
                        for each API and for each shard.
*BR Refs:* BR-10

**FR-10.2** The system SHALL emit SLO-window rollups and error-budget burn rates.  
*BR Refs:* BR-10

**FR-10.3** Alert rules SHOULD reference SLOs and trigger at fast and slow burn thresholds.  
*BR Refs:* BR-10

---

### BR-11 — Controlled chaos & failure injection

**FR-11.1** An SRE-only chaos interface SHALL allow scheduled or ad-hoc injections: pod kill, node taint,  
                        DB failover, latency/jitter.
*BR Refs:* BR-11

**FR-11.2** Chaos runs SHALL annotate Grafana/Tempo to correlate experiments with observed impact.  
*BR Refs:* BR-11, BR-06

**FR-11.3** Chaos operations SHALL be authorization-gated to `sre` and logged in audit.  
*BR Refs:* BR-11, BR-07, BR-08

---

### BR-12 — Measurable operator learning & assessment

**FR-12.1** The platform SHALL provide guided scenarios (tickets) that require using traces/logs to resolve  
                        performance or correctness issues.
*BR Refs:* BR-12, BR-06

**FR-12.2** A reviewer mode SHALL expose checklists and expected signals for scenario completion.  
*BR Refs:* BR-12

**FR-12.3** The system SHALL export anonymized performance-of-operator metrics (e.g., time-to-hypothesis,  
                        time-to-fix) for assessment.
*BR Refs:* BR-12

---

### BR-13 — Observability-driven debugging

**FR-13.1** Grafana dashboards SHALL support drill-down: SLO panel → service panel → trace exemplar →  
                        correlated logs.
*BR Refs:* BR-13, BR-06

**FR-13.2** Each error log entry SHALL include a URL-safe link or IDs to fetch the matching trace and audit  
                        event.
*BR Refs:* BR-13, BR-07

**FR-13.3** DB slow queries SHALL surface as traces with spans for waits and query text fingerprints.  
*BR Refs:* BR-13

---

### BR-14 — Event-driven consistency & traceable data flow

**FR-14.1** The core-api SHALL implement the outbox pattern for every transactional write.  
*BR Refs:* BR-14, BR-07

**FR-14.2** Projection workers SHALL consume outbox or CDC streams to update read models idempotently.  
*BR Refs:* BR-14

**FR-14.3** Event schemas SHALL be versioned and backward-compatible, with dead-letter handling.  
*BR Refs:* BR-14

---

### BR-15 — Failure visibility preserved

**FR-15.1** The system SHALL persist evidence of failures (stuck commands, projection lag, failed shard  
                        lookups) with timestamps and context.
*BR Refs:* BR-15

**FR-15.2** The platform SHALL expose dashboards for backlog depth, lag, retry counts, and dead-letter  
                        volume.
*BR Refs:* BR-15, BR-06

**FR-15.3** Automatic retries SHALL cap at a configurable limit and then quarantine to dead-letter with  
                        alert.
*BR Refs:* BR-15

---

### BR-16 — Educationally narratable end-to-end

**FR-16.1** A “request journey” view SHALL illustrate edge-api → core-api → shard → event → projection →  
                        Grafana, for a given `request_id`.
*BR Refs:* BR-16, BR-06

**FR-16.2** A “data lineage” query SHALL reconstruct an entity’s state from temporal history + audit  
                        events.
*BR Refs:* BR-16, BR-07

**FR-16.3** Documentation SHALL include step-by-step narratives and curl examples that align with  
                        dashboards and traces.
*BR Refs:* BR-16

**FR-16.4** All public artifacts (README, diagrams, dashboards) SHALL use consistent glossary terms and  
                        IDs.
*BR Refs:* BR-16

---

### Cross-cutting expected defaults (applied wherever relevant)

**FR-X.1** All APIs SHALL be versioned, accept and return JSON, and support pagination, filtering, and  
                      sorting for list endpoints.
*BR Refs:* BR-01, BR-03, BR-10

**FR-X.2** All write endpoints SHALL be idempotent via `Idempotency-Key` or natural keys; duplicate  
                      submissions MUST NOT create duplicate records.
*BR Refs:* BR-03, BR-05, BR-07

**FR-X.3** Validation errors SHALL return structured problem details; server errors SHALL include a  
                      correlation `request_id`.
*BR Refs:* BR-06, BR-13

**FR-X.4** All configs SHALL have sane defaults and be overrideable via env/Helm; secrets SHALL never be  
                      hardcoded.
*BR Refs:* BR-03, BR-09

**FR-X.5** Time handling SHALL be UTC internally with ISO-8601 in APIs; DB timestamps SHALL be `datetime2`  
                      with precision aligned across services.
*BR Refs:* BR-09, BR-10

**FR-X.6** Referential integrity SHALL be enforced via FK constraints; deletes SHOULD be soft-deletes  
                      where auditability matters.
*BR Refs:* BR-07, BR-14

---

### Data Lifecycle & Retention

**FR-17.1** The system SHALL define explicit retention policies for raw transactional tables, audit logs,  
                        and observability signal retention windows.
*BR Refs:* BR-07, BR-09, BR-15

**FR-17.2** The system SHOULD support purging or archiving data after a defined retention period, using a  
                        versioned procedure or migration task.
*BR Refs:* BR-07, BR-09

---

**FR-18.1** The system SHALL prevent destructive operations (e.g. shard reassignment, route map overwrite)  
                        unless explicitly authorized under `sre` role and audited.
*BR Refs:* BR-07, BR-08, BR-11

**FR-18.2** The system SHOULD provide a dry-run mode for migrations, shard remaps, and capped rollout of  
                        chaos experiments, operable by `sre`.
*BR Refs:* BR-11, BR-16
