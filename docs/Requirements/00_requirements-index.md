---
title: Requirements Index
doc_type: policy
status: draft
version: 0.1.0
owners:
  - docs@pim-sre.lab
last_updated: 2024-05-18
tags:
  - requirements
  - index
---

# Requirements Index

Canonical index of business, functional, and non-functional requirements.

## Business Requirements

- `BR-01` — Demonstrate realistic national-scale healthcare workload simulation
  _Purpose:_ The platform must simulate U.S.-style healthcare entities (patients, providers,
  facilities, encounters, billing events) with enough fidelity to meaningfully exercise SRE
  patterns under realistic load.

- `BR-02` — Prove ability to safely operate under load without real PHI
  _Purpose:_ All data must be fully synthetic, safe, and pseudonymized while still behaving
  architecturally like real health data for observability, diagnosis, and performance
  testing.

- `BR-03` — Prove horizontal scalability without redesign
  _Purpose:_ The system must scale from single-node to multi-node Kubernetes environments with **no
  architectural changes** — only configuration and replica count adjustments.

- `BR-04` — Demonstrate shard-based routing and locality enforcement
  _Purpose:_ The platform must prove that data is **partitioned and routed logically by patient
  identity**, allowing realistic demonstration of affinity, locality, and downstream load
  behavior.

- `BR-05` — Demonstrate provable failure resilience
  _Purpose:_ The system must **remain operational during arbitrary pod/replica failure** — including
  SQL nodes — proving that it can self-heal without operator intervention.

- `BR-06` — Demonstrate full observability maturity (MELTP)
  _Purpose:_ Every request must emit **Metrics, Events, Logs, Traces, and Profiles** — correlated —
  with **zero orphan execution**, and fully visualizable in Grafana.

- `BR-07` — Prove auditable accountability for ALL state changes
  _Purpose:_ Every write must be traceable to a **specific user_id and request_id**, fully
  reconstructible via temporal tables plus audit events.

- `BR-08` — Demonstrate multi-role security boundaries
  _Purpose:_ The platform must support at minimum **3 application roles** (patient, clinician, admin)
  with **enforced logical access separation** and a guard-railed **`sre` operator role** for
  infrastructure-grade actions — not just conceptual or UI-only separation.

- `BR-09` — Enable continuous GitOps-based reproducibility
  _Purpose:_ The entire environment must be **teardown-and-redeploy reproducible from Git** — including
  data plane, control plane, SQL AG topology, and Grafana telemetry contracts.

- `BR-10` — Demonstrate SLO-ready reliability metrics
  _Purpose:_ The platform must produce **immediately usable SLI signals** for availability, latency,
  and failure rate — enabling SLO definition without friction or redesign.

- `BR-11` — Demonstrate controlled chaos & failure injection readiness
  _Purpose:_ The platform must support **intentional failure injection (e.g. pod kill, DB failover,
  latency spikes)** as a **first-class capability**, not a bolt-on, to prove active
  reliability engineering readiness.

- `BR-12` — Must enable measurable operator learning & hiring assessment
  _Purpose:_ The platform must allow **recruiters, mentors, or SRE leads** to clearly observe behaviors
  such as **debug skill, trace correlation, failure analysis**, and **system recovery
  reasoning** — not just view static dashboards.

- `BR-13` — Support observability-driven debugging, not log scraping
  _Purpose:_ The platform must enable engineers to **start from a symptom (e.g. latency spike)** and
  navigate **trace → log → metric → root cause** without guesswork — proving observability
  is engineered, not decorative.

- `BR-14` — Prove event-driven consistency and traceable data flow
  _Purpose:_ All state changes must emit **domain events**, enabling downstream systems or analytics to
  **process changes deterministically** — demonstrating readiness for a **future event-
  driven ecosystem**.

- `BR-15` — Must teach failure visibility, not hide it
  _Purpose:_ System must **surface and preserve evidence** of failures (e.g. stuck commands, slow
  replication, failed shard routing) for **post-incident analysis**, not silently auto-
  resolve or discard failure signals.

- `BR-16` — Must be educationally narratable end-to-end
  _Purpose:_ The platform must be structured so that **a human or AI can tell the story of how a
  request flows through the system** — from API to shard to observability to audit trail —
  making it usable as a teaching, documentation, or portfolio artifact.

## Functional Requirements

- `FR-01.1` — Generate Mockaroo-based seed datasets for patients, providers, facilities, encounters, diagnoses,…
  _Purpose:_ The system SHALL generate Mockaroo-based seed datasets for patients, providers,
  facilities, encounters, diagnoses, procedures, medications, and claims.

- `FR-01.2` — The load generator SHALL simulate three user profiles (patient, clinician,…
  _Purpose:_ The load generator SHALL simulate three user profiles (patient, clinician, admin) with
  configurable arrival rates, concurrency, and think-time.

- `FR-01.3` — Provide role-specific operation mixes (read % vs write %, heavy-read…
  _Purpose:_ The system SHALL provide role-specific operation mixes (read % vs write %, heavy-read for
  patients, mixed for clinicians, admin-heavy maintenance).

- `FR-01.4` — Support traffic shape presets (e.g., weekday clinic peak, night lull,…
  _Purpose:_ The system SHALL support traffic shape presets (e.g., weekday clinic peak, night lull,
  end-of-month billing burst).

- `FR-01.5` — The system SHOULD expose a single YAML profile to define…
  _Purpose:_ The system SHOULD expose a single YAML profile to define dataset size, shard counts, and
  traffic patterns.

- `FR-02.1` — All seed data MUST be synthetic, pseudonymized, and non-reversible to…
  _Purpose:_ All seed data MUST be synthetic, pseudonymized, and non-reversible to real individuals.

- `FR-02.2` — Block ingestion of external identifiers beyond the defined synthetic schema
  _Purpose:_ The platform SHALL block ingestion of external identifiers beyond the defined synthetic
  schema.

- `FR-02.3` — Exports and logs SHALL exclude sensitive fields or present them…
  _Purpose:_ Exports and logs SHALL exclude sensitive fields or present them in masked form per
  allowlist.

- `FR-02.4` — Provide redaction for audit/event payloads where fields are not required…
  _Purpose:_ The system SHALL provide redaction for audit/event payloads where fields are not required
  for troubleshooting.

- `FR-03.1` — The APIs SHALL be stateless and horizontally scalable via HPA
  _Purpose:_ The APIs SHALL be stateless and horizontally scalable via HPA.

- `FR-03.2` — The database layer SHALL scale via sharding and SQL Server…
  _Purpose:_ The database layer SHALL scale via sharding and SQL Server AG read replicas without schema
  change.

- `FR-03.3` — Externalize configuration (replica counts, shard count, listener DSNs) via environment…
  _Purpose:_ The system SHALL externalize configuration (replica counts, shard count, listener DSNs)
  via environment or Helm values.

- `FR-03.4` — Maintain idempotent writes to tolerate retries under scale
  _Purpose:_ The system SHALL maintain idempotent writes to tolerate retries under scale.

- `FR-04.1` — Deterministically route requests by `patient_id` to the correct shard listener
  _Purpose:_ The router SHALL deterministically route requests by `patient_id` to the correct shard
  listener.

- `FR-04.2` — Support shard map updates without downtime (hot reload or versioned…
  _Purpose:_ The router SHALL support shard map updates without downtime (hot reload or versioned
  config).

- `FR-04.3` — Prefer read-only replicas; write requests MUST target the primary
  _Purpose:_ Read requests SHOULD prefer read-only replicas; write requests MUST target the primary.

- `FR-04.4` — Expose a health endpoint that verifies shard reachability and listener…
  _Purpose:_ The system SHALL expose a health endpoint that verifies shard reachability and listener
  status.

- `FR-05.1` — Continue serving traffic during arbitrary pod kill of any single…
  _Purpose:_ The platform SHALL continue serving traffic during arbitrary pod kill of any single API
  pod.

- `FR-05.2` — The data tier SHALL continue serving reads during primary failover…
  _Purpose:_ The data tier SHALL continue serving reads during primary failover and recover write
  capability automatically.

- `FR-05.3` — Retry transient DB errors with exponential backoff and timeouts
  _Purpose:_ The system SHALL retry transient DB errors with exponential backoff and timeouts.

- `FR-05.4` — Support injections: pod kill, network delay, DB failover, replica drain
  _Purpose:_ An SRE-operated chaos interface SHALL support injections: pod kill, network delay, DB
  failover, replica drain.

- `FR-05.5` — Publish failover events to observability for incident correlation
  _Purpose:_ The platform SHALL publish failover events to observability for incident correlation.

- `FR-06.1` — Each request SHALL emit a trace with unique `trace_id` propagated…
  _Purpose:_ Each request SHALL emit a trace with unique `trace_id` propagated across edge-api, core-
  api, and DB spans.

- `FR-06.2` — Include `trace_id`, `span_id`, `request_id`, `user_id` (if present), and role
  _Purpose:_ Structured logs SHALL include `trace_id`, `span_id`, `request_id`, `user_id` (if present),
  and role.

- `FR-06.3` — Include RED (rate, errors, duration) per endpoint and shard; DB…
  _Purpose:_ Metrics SHALL include RED (rate, errors, duration) per endpoint and shard; DB metrics
  SHALL include waits and replica role.

- `FR-06.4` — Be captured for APIs under load with symbolized stack frames
  _Purpose:_ Profiles (CPU/mem) SHALL be captured for APIs under load with symbolized stack frames.

- `FR-06.5` — Execute without at least one MELTP signal produced (“no orphan…
  _Purpose:_ No code path SHALL execute without at least one MELTP signal produced (“no orphan
  telemetry”).

- `FR-07.1` — Produce an `AUDIT_EVENT` containing actor, role, action, object type/id, before/after…
  _Purpose:_ Every write operation SHALL produce an `AUDIT_EVENT` containing actor, role, action,
  object type/id, before/after JSON, and timestamps.

- `FR-07.2` — Be system-versioned (temporal)
  _Purpose:_ Core tables (Patient, Appointment, Encounter, Medication Order, Claim, Claim Line) SHALL
  be system-versioned (temporal).

- `FR-07.3` — Be queryable by `request_id` and `user_id`
  _Purpose:_ Audit and temporal history SHALL be queryable by `request_id` and `user_id`.

- `FR-07.4` — Reject write requests missing `user_id` and `request_id` in session context
  _Purpose:_ The system SHALL reject write requests missing `user_id` and `request_id` in session
  context.

- `FR-08.1` — Implement three application roles: `patient`, `clinician`, `admin`, and a dedicated…
  _Purpose:_ The platform SHALL implement three application roles: `patient`, `clinician`, `admin`, and
  a dedicated operator role: `sre`.

- `FR-08.2` — Row-Level Security (RLS) SHALL enforce patient-only visibility for `patient` role…
  _Purpose:_ Row-Level Security (RLS) SHALL enforce patient-only visibility for `patient` role and
  facility- scoped visibility for `clinician`.

- `FR-08.3` — `admin` role SHALL have application-level CRUD and user admin via…
  _Purpose:_ `admin` role SHALL have application-level CRUD and user admin via app procedures only. The
  `sre` role SHALL have full read/write and ops via secured procedures.

- `FR-08.4` — Session context SHALL be set from JWT at connection open…
  _Purpose:_ Session context SHALL be set from JWT at connection open and refreshed per request.

- `FR-09.1` — All manifests, schema migrations, and configs SHALL live in Git…
  _Purpose:_ All manifests, schema migrations, and configs SHALL live in Git with versioned
  environments.

- `FR-09.2` — One command (or Argo CD sync) SHALL recreate a working…
  _Purpose:_ One command (or Argo CD sync) SHALL recreate a working environment end-to-end.

- `FR-09.3` — Database migrations SHALL be idempotent and forward-only with rollback scripts…
  _Purpose:_ Database migrations SHALL be idempotent and forward-only with rollback scripts when
  feasible.

- `FR-09.4` — Be deterministic via pinned seeds and versions
  _Purpose:_ Seed and demo data generation SHALL be deterministic via pinned seeds and versions.

- `FR-10.1` — Expose golden signals for availability, latency (p50/p95/p99), and error rate…
  _Purpose:_ The system SHALL expose golden signals for availability, latency (p50/p95/p99), and error
  rate for each API and for each shard.

- `FR-10.2` — Emit SLO-window rollups and error-budget burn rates
  _Purpose:_ The system SHALL emit SLO-window rollups and error-budget burn rates.

- `FR-10.3` — Alert rules SHOULD reference SLOs and trigger at fast and…
  _Purpose:_ Alert rules SHOULD reference SLOs and trigger at fast and slow burn thresholds.

- `FR-11.1` — Allow scheduled or ad-hoc injections: pod kill, node taint, DB…
  _Purpose:_ An SRE-only chaos interface SHALL allow scheduled or ad-hoc injections: pod kill, node
  taint, DB failover, latency/jitter.

- `FR-11.2` — Chaos runs SHALL annotate Grafana/Tempo to correlate experiments with observed…
  _Purpose:_ Chaos runs SHALL annotate Grafana/Tempo to correlate experiments with observed impact.

- `FR-11.3` — Chaos operations SHALL be authorization-gated to `sre` and logged in…
  _Purpose:_ Chaos operations SHALL be authorization-gated to `sre` and logged in audit.

- `FR-12.1` — Provide guided scenarios (tickets) that require using traces/logs to resolve…
  _Purpose:_ The platform SHALL provide guided scenarios (tickets) that require using traces/logs to
  resolve performance or correctness issues.

- `FR-12.2` — A reviewer mode SHALL expose checklists and expected signals for…
  _Purpose:_ A reviewer mode SHALL expose checklists and expected signals for scenario completion.

- `FR-12.3` — Export anonymized performance-of-operator metrics (e.g., time-to-hypothesis, time-to-fix) for assessment
  _Purpose:_ The system SHALL export anonymized performance-of-operator metrics (e.g., time-to-
  hypothesis, time-to-fix) for assessment.

- `FR-13.1` — Grafana dashboards SHALL support drill-down: SLO panel → service panel…
  _Purpose:_ Grafana dashboards SHALL support drill-down: SLO panel → service panel → trace exemplar →
  correlated logs.

- `FR-13.2` — Each error log entry SHALL include a URL-safe link or…
  _Purpose:_ Each error log entry SHALL include a URL-safe link or IDs to fetch the matching trace and
  audit event.

- `FR-13.3` — DB slow queries SHALL surface as traces with spans for…
  _Purpose:_ DB slow queries SHALL surface as traces with spans for waits and query text fingerprints.

- `FR-14.1` — The core-api SHALL implement the outbox pattern for every transactional…
  _Purpose:_ The core-api SHALL implement the outbox pattern for every transactional write.

- `FR-14.2` — Projection workers SHALL consume outbox or CDC streams to update…
  _Purpose:_ Projection workers SHALL consume outbox or CDC streams to update read models idempotently.

- `FR-14.3` — Event schemas SHALL be versioned and backward-compatible, with dead-letter handling
  _Purpose:_ Event schemas SHALL be versioned and backward-compatible, with dead-letter handling.

- `FR-15.1` — Persist evidence of failures (stuck commands, projection lag, failed shard…
  _Purpose:_ The system SHALL persist evidence of failures (stuck commands, projection lag, failed
  shard lookups) with timestamps and context.

- `FR-15.2` — Expose dashboards for backlog depth, lag, retry counts, and dead-letter…
  _Purpose:_ The platform SHALL expose dashboards for backlog depth, lag, retry counts, and dead-letter
  volume.

- `FR-15.3` — Automatic retries SHALL cap at a configurable limit and then…
  _Purpose:_ Automatic retries SHALL cap at a configurable limit and then quarantine to dead-letter
  with alert.

- `FR-16.1` — Illustrate edge-api → core-api → shard → event → projection…
  _Purpose:_ A “request journey” view SHALL illustrate edge-api → core-api → shard → event → projection
  → Grafana, for a given `request_id`.

- `FR-16.2` — A “data lineage” query SHALL reconstruct an entity’s state from…
  _Purpose:_ A “data lineage” query SHALL reconstruct an entity’s state from temporal history + audit
  events.

- `FR-16.3` — Include step-by-step narratives and curl examples that align with dashboards…
  _Purpose:_ Documentation SHALL include step-by-step narratives and curl examples that align with
  dashboards and traces.

- `FR-16.4` — All public artifacts (README, diagrams, dashboards) SHALL use consistent glossary…
  _Purpose:_ All public artifacts (README, diagrams, dashboards) SHALL use consistent glossary terms
  and IDs.

- `FR-X.1` — All APIs SHALL be versioned, accept and return JSON, and…
  _Purpose:_ All APIs SHALL be versioned, accept and return JSON, and support pagination, filtering,
  and sorting for list endpoints.

- `FR-X.2` — All write endpoints SHALL be idempotent via `Idempotency-Key` or natural…
  _Purpose:_ All write endpoints SHALL be idempotent via `Idempotency-Key` or natural keys; duplicate
  submissions MUST NOT create duplicate records.

- `FR-X.3` — Validation errors SHALL return structured problem details; server errors SHALL…
  _Purpose:_ Validation errors SHALL return structured problem details; server errors SHALL include a
  correlation `request_id`.

- `FR-X.4` — All configs SHALL have sane defaults and be overrideable via…
  _Purpose:_ All configs SHALL have sane defaults and be overrideable via env/Helm; secrets SHALL never
  be hardcoded.

- `FR-X.5` — Time handling SHALL be UTC internally with ISO-8601 in APIs;…
  _Purpose:_ Time handling SHALL be UTC internally with ISO-8601 in APIs; DB timestamps SHALL be
  `datetime2` with precision aligned across services.

- `FR-X.6` — Referential integrity SHALL be enforced via FK constraints; deletes SHOULD…
  _Purpose:_ Referential integrity SHALL be enforced via FK constraints; deletes SHOULD be soft-deletes
  where auditability matters.

- `FR-17.1` — Define explicit retention policies for raw transactional tables, audit logs,…
  _Purpose:_ The system SHALL define explicit retention policies for raw transactional tables, audit
  logs, and observability signal retention windows.

- `FR-17.2` — The system SHOULD support purging or archiving data after a…
  _Purpose:_ The system SHOULD support purging or archiving data after a defined retention period,
  using a versioned procedure or migration task.

- `FR-18.1` — Prevent destructive operations (e.g. shard reassignment, route map overwrite) unless…
  _Purpose:_ The system SHALL prevent destructive operations (e.g. shard reassignment, route map
  overwrite) unless explicitly authorized under `sre` role and audited.

- `FR-18.2` — The system SHOULD provide a dry-run mode for migrations, shard…
  _Purpose:_ The system SHOULD provide a dry-run mode for migrations, shard remaps, and capped rollout
  of chaos experiments, operable by `sre`.

## Non-Functional Requirements

- `NFR-01` — API availability
  _Purpose:_ monthly availability for both edge-api and core-api on single-node Kubernetes; target
  **≥99.9%** when running multi-node.

- `NFR-02` — Read continuity during failover
  _Purpose:_ read endpoints remain available** with ≤ **30 s** aggregate brownout; writes recover
  automatically ≤ **60 s**.

- `NFR-03` — Pod kill survivability
  _Purpose:_ Random kill of a single API pod SHALL not breach availability SLO nor drop in-flight
  requests beyond standard retry policy.

- `NFR-04` — Error budget cadence
  _Purpose:_ windows with fast/slow burn alerts at **2%/5%** of budget consumed per hour/day.

- `NFR-05` — Data durability
  _Purpose:_ at the database level (AG synchronous commit for primary + one replica in demo mode).

- `NFR-06` — Read latency
  _Purpose:_ under nominal load.

- `NFR-07` — Write latency
  _Purpose:_ 600 ms** with synchronous audit outbox write.

- `NFR-08` — Billing/analytics queries
  _Purpose:_ Reporting reads on projections/materialized views: p95 ≤ **500 ms** for single-patient
  scope; ≤ **2 s** for facility-scope queries.

- `NFR-09` — Cold start
  _Purpose:_ .

- `NFR-10` — Queue processing
  _Purpose:_ per worker with idempotent processing.

- `NFR-11` — Concurrency envelope
  _Purpose:_ mixed profile on commodity lab hardware; scale linearly with replicas.

- `NFR-12` — Shard capacity
  _Purpose:_ patient records in demo datasets without schema change; add shards via config only.

- `NFR-13` — HPA behavior
  _Purpose:_ or p95 latency breach; scale down gracefully after **5 min** idle.

- `NFR-14` — Backpressure
  _Purpose:_ with `Retry-After` when upstream queues exceed safe thresholds; no unbounded memory
  growth.

- `NFR-15` — Authentication
  _Purpose:_ All endpoints SHALL require JWT with short-lived access tokens (≤ **15 min**) and rotating
  signing keys.

- `NFR-16` — Authorization
  _Purpose:_ RLS + SQL roles SHALL enforce least privilege; app roles (`patient`, `clinician`, `admin`)
  cannot perform direct table DML, reserving guarded procedures for `sre`.

- `NFR-17` — Secrets handling
  _Purpose:_ No secrets in images or Git; use Kubernetes secrets mounted as env/volumes; support key
  rotation without downtime.

- `NFR-18` — Data minimization
  _Purpose:_ Logs, traces, and events SHALL exclude sensitive personal fields unless explicitly allow-
  listed and masked.

- `NFR-19` — Audit retention
  _Purpose:_ minimum in demo; configurable to **365 days**.

- `NFR-20` — Trace coverage
  _Purpose:_ of requests must have a complete trace from API to DB span; sampling may reduce storage
  but not break correlation.

- `NFR-21` — Log structure
  _Purpose:_ 100% of application logs are structured JSON and include `trace_id`, `span_id`,
  `request_id`, `user_id` (if present), `role`, and `shard_id`.

- `NFR-22` — Metrics cardinality
  _Purpose:_ series per service to avoid TSDB blow-ups.

- `NFR-23` — Profiles
  _Purpose:_ CPU overhead on APIs under nominal load.

- `NFR-24` — Dashboards
  _Purpose:_ p95 and use exemplars for trace jump-links.

- `NFR-25` — Zero-downtime deploys
  _Purpose:_ Rolling updates for APIs and projection workers with max unavailable **1**, readiness-
  gated; SQL schema changes use online migrations.

- `NFR-26` — SQL AG topology
  _Purpose:_ per shard in demo; listener failover completes ≤ **60 s**.

- `NFR-27` — Storage
  _Purpose:_ per replica target; WAL/log volume separated when supported.

- `NFR-28` — GitOps source of truth
  _Purpose:_ Cluster state is reconciled from Git; drift detection ≤ **5 min**; rollbacks are single-
  click via Argo CD.

- `NFR-29` — Backups
  _Purpose:_ in a scratch namespace.

- `NFR-30` — RPO/RTO
  _Purpose:_ for a single-shard incident in demo mode.

- `NFR-31` — Runbooks
  _Purpose:_ Each alert SHALL link to a runnable, up-to-date runbook with verification steps and
  rollback paths.

- `NFR-32` — Efficiency SLI
  _Purpose:_ Track CPU/memory per request and cost-per-1000-requests (synthetic) as a teaching signal;
  publish in Grafana.

- `NFR-33` — Idle limits
  _Purpose:_ idle; caches expire predictably to avoid cold-start thundering herds.

- `NFR-34` — Guardrails
  _Purpose:_ Chaos experiments require `sre` role, dry-run preview, and automatic Grafana annotation;
  blast radius and duration are mandatory inputs.

- `NFR-35` — Post-experiment hygiene
  _Purpose:_ System SHALL auto-restore normal replicas/policies after experiments and post a summary to
  logs with `request_id`.

- `NFR-36` — Golden path enforcement
  _Purpose:_ single, officially supported “golden path” workflows** (e.g. how to create a new feature,
  deploy, observe, debug) — documented and reinforced by defaults — to prevent divergence or
  anti-patterns.

- `NFR-37` — Self-documenting observability
  _Purpose:_ Dashboards, trace exemplars, and logs SHOULD collectively allow a user to navigate to
  **documentation or source-of-truth context automatically** (e.g., clicking an endpoint
  name jumps to its API spec or annotated architecture doc).
