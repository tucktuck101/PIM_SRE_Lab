---
title: Non-Functional Requirements
doc_type: policy
status: draft
version: 0.1.0
owners:
  - sre@pim-sre.lab
last_updated: 2024-05-18
tags:
  - requirements
  - non-functional
---

## Non-Functional Requirements (NFR)

**Frame:** Flat list. Each NFR includes explicit traceability via `BR Refs:`
and uses MUST-level targets tuned for a production credible SRE demo.

---

### Availability & Reliability

**NFR-01 — API availability**  The platform SHALL sustain **≥99.5%** monthly availability for
both edge-api and core-api on
single-node Kubernetes; target **≥99.9%** when running multi-node.
*BR Refs:*BR-03, BR-05, BR-10

**NFR-02 — Read continuity during failover**  During SQL AG primary failover, **read endpoints
remain available** with ≤ **30 s** aggregate
brownout; writes recover automatically ≤ **60 s**.
*BR Refs:*BR-05, BR-10

**NFR-03 — Pod kill survivability**  Random kill of a single API pod SHALL not breach
availability SLO nor drop in-flight requests
beyond standard retry policy.
*BR Refs:*BR-05, BR-11

**NFR-04 — Error budget cadence**  Error budget burn SHALL be computed over **28-day** windows
with fast/slow burn alerts at
**2%/5%** of budget consumed per hour/day.
*BR Refs:*BR-10

**NFR-05 — Data durability**  Committed writes SHALL have durability ≥ **99.99%** at the
database level (AG synchronous
commit for primary + one replica in demo mode).
*BR Refs:*BR-05

---

### Latency & Performance

**NFR-06 — Read latency**  Edge-api GETs: p50 ≤ **50 ms**, p95 ≤ **200 ms**, p99 ≤ **400 ms**
under nominal load.
*BR Refs:* BR-06, BR-10, BR-13

**NFR-07 — Write latency**  Core-api POST/PUT: p50 ≤ **90 ms**, p95 ≤ **300 ms**, p99 ≤ **600
ms** with synchronous audit
  outbox write.
*BR Refs:* BR-06, BR-10, BR-14

**NFR-08 — Billing/analytics queries**  Reporting reads on projections/materialized views: p95
≤ **500 ms** for single-patient scope;
≤ **2 s** for facility-scope queries.
*BR Refs:*BR-01, BR-06, BR-10

**NFR-09 — Cold start**  API container cold start to ready ≤ **8 s**; warm restarts ≤ **2 s**.
*BR Refs:*BR-03, BR-05

**NFR-10 — Queue processing**  Command/outbox consumers SHALL drain at ≥ **500 msgs/min** per
worker with idempotent
processing.
*BR Refs:*BR-14, BR-15

---

### Scalability (Envelopes & Headroom)

**NFR-11 — Concurrency envelope**  Sustain ≥ **1,000 RPS** read-heavy profile or **200 RPS**
mixed profile on commodity lab
hardware; scale linearly with replicas.
*BR Refs:*BR-01, BR-03

**NFR-12 — Shard capacity**  Each shard SHALL support ≥ **5 million** patient records in demo
datasets without schema
change; add shards via config only.
*BR Refs:*BR-03, BR-04

**NFR-13 — HPA behavior**  Autoscale APIs between **1–5 replicas** on CPU ≥ **60%** or p95
latency breach; scale down
gracefully after **5 min** idle.
*BR Refs:*BR-03, BR-10

**NFR-14 — Backpressure**  System SHALL return **429** with `Retry-After` when upstream queues
exceed safe thresholds; no
unbounded memory growth.
*BR Refs:*BR-03, BR-05

---

### Security & Compliance Tone (Demo-appropriate)

**NFR-15 — Authentication**  All endpoints SHALL require JWT with short-lived access tokens (≤
**15 min**) and rotating
signing keys.
*BR Refs:*BR-08, BR-07

**NFR-16 — Authorization**  RLS + SQL roles SHALL enforce least privilege; app roles
(`patient`, `clinician`, `admin`)
cannot perform direct table DML, reserving guarded procedures for `sre`.
*BR Refs:*BR-08, BR-07

**NFR-17 — Secrets handling**  No secrets in images or Git; use Kubernetes secrets mounted as
env/volumes; support key
rotation without downtime.
*BR Refs:*BR-09

**NFR-18 — Data minimization**  Logs, traces, and events SHALL exclude sensitive personal
fields unless explicitly allow-
listed and masked.
*BR Refs:*BR-02, BR-06, BR-07

**NFR-19 — Audit retention**  Audit events and temporal history retained **90 days** minimum in
demo; configurable to **365
days**.
*BR Refs:*BR-07, BR-15

---

### Observability (MELTP) Constraints

**NFR-20 — Trace coverage**  ≥ **95%** of requests must have a complete trace from API to DB
span; sampling may reduce
storage but not break correlation.
*BR Refs:*BR-06, BR-13, BR-16

**NFR-21 — Log structure**  100% of application logs are structured JSON and include
`trace_id`, `span_id`, `request_id`,
`user_id` (if present), `role`, and `shard_id`.
*BR Refs:*BR-06, BR-13

**NFR-22 — Metrics cardinality**  Label cardinality per metric family SHALL remain ≤ **2,000**
series per service to avoid TSDB
blow-ups.
*BR Refs:*BR-06, BR-10

**NFR-23 — Profiles**  Continuous profiling enabled with **10 s** sampling and ≤ **3%** CPU
overhead on APIs under
nominal load.
*BR Refs:*BR-06

**NFR-24 — Dashboards**  Grafana dashboards SHALL render ≤ **3 s** p95 and use exemplars for trace jump-links.
*BR Refs:*BR-06, BR-13

---

### Infrastructure & Deployment

**NFR-25 — Zero-downtime deploys**  Rolling updates for APIs and projection workers with max
unavailable **1**, readiness-gated;
SQL schema changes use online migrations.
*BR Refs:*BR-03, BR-09

**NFR-26 — SQL AG topology**  At least **1 primary + 1 synchronous replica** per shard in demo;
listener failover completes
≤ **60 s**.
*BR Refs:*BR-05, BR-13

**NFR-27 — Storage**  DB PVCs use SSD-class volumes with ≥ **3,000 IOPS** per replica target; WAL/log volume
separated when supported.
*BR Refs:*BR-03, BR-05

**NFR-28 — GitOps source of truth**  Cluster state is reconciled from Git; drift detection ≤
**5 min**; rollbacks are single-click
via Argo CD.
*BR Refs:*BR-09

---

### Operability (Backup, Restore, Runbooks)

**NFR-29 — Backups**  Nightly full + **15 min** log backups; verify restore integrity at least **weekly** in a
scratch namespace.
*BR Refs:*BR-05, BR-09

**NFR-30 — RPO/RTO**  Target **RPO ≤ 15 min**, **RTO ≤ 30 min** for a single-shard incident in demo mode.
*BR Refs:*BR-05

**NFR-31 — Runbooks**  Each alert SHALL link to a runnable, up-to-date runbook with
verification steps and rollback
paths.
*BR Refs:*BR-12, BR-13, BR-15

---

### Resource Efficiency & Cost Observability

**NFR-32 — Efficiency SLI**  Track CPU/memory per request and cost-per-1000-requests
(synthetic) as a teaching signal;
publish in Grafana.
*BR Refs:*BR-12, BR-16

**NFR-33 — Idle limits**  Non-critical workers scale to zero after **10 min** idle; caches
expire predictably to avoid
cold-start thundering herds.
*BR Refs:*BR-03

---

### Chaos & Experimentation Safety

**NFR-34 — Guardrails**  Chaos experiments require `sre` role, dry-run preview, and automatic
Grafana annotation; blast
radius and duration are mandatory inputs.
*BR Refs:*BR-11, BR-15

**NFR-35 — Post-experiment hygiene**  System SHALL auto-restore normal replicas/policies after
experiments and post a summary to
logs with `request_id`.
*BR Refs:*BR-11, BR-12

---
**NFR-36 — Golden path enforcement**  The platform SHOULD provide **single, officially
supported “golden path” workflows** (e.g. how
to create a new feature, deploy, observe, debug) — documented and reinforced by defaults —  to
prevent divergence or anti-patterns.
*BR Refs:*BR-12, BR-16

---
**NFR-37 — Self-documenting observability**  Dashboards, trace exemplars, and logs SHOULD
collectively allow a user to navigate to
**documentation or source-of-truth context automatically** (e.g., clicking an endpoint name
jumps to its API spec or annotated architecture doc).
*BR Refs:*BR-13, BR-16

---
