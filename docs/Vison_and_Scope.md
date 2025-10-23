---
title: Vision and Scope
doc_type: policy
status: draft
version: 0.2.0
owners:
  - product@pim-sre.lab
  - sre@pim-sre.lab
last_updated: 2024-05-18
tags:
  - vision
  - scope
---

### Vision & Scope — Final Draft v2

**Purpose**  
Create a high-value, production-credible demo lab environment that SREs can use to **prove real technical competence** — not theory — through a system that demonstrates **reliability engineering, sharded database architecture, and full-fidelity observability** under load.

---

### Audience
- **SREs** — junior to senior — demonstrating or sharpening production engineering skill  
- **Engineers learning the Grafana MELTP stack** as an end-to-end observability platform  
- **Recruiters and hiring managers** evaluating portfolio depth and readiness for real ops environments  

This is explicitly *not* a bootcamp toy or slide-ware — it must be believable as a real internal platform.

---

### Scope (In)
- U.S.-style national **health data spine** model  
- Core entities only: **patients, providers, facilities, encounters, diagnoses, procedures, medications, billing**  
- All seed data is **Mockaroo-generated, pseudonymized, HIPAA-safe**  
- **CQRS + per-patient sharding** — `patient_id` drives routing, tenancy, and locality  
- **Cluster A** (Kaladesh server): App + SQL Server Always On AG + synthetic load  
- **Cluster B** (MacBook): **full Grafana MELTP observability stack** (metrics/events/logs/traces/profiles)  
- Observability is **non-optional** — every execution path emits trace-linked telemetry  
- Zero rewrite required to expand to **multi-region or multi-cluster**  

---

### Explicitly Out of Scope (anti-scope-creep guardrail)
- **No real PHI** — never touches real patient/customer data  
- **No rich Web UI / EHR-style frontend** — API-only by design  
- **No HL7/FHIR interoperability** — simulated data only  
- **No third-party billing, insurance clearinghouses, payer logic**  
- **No async patient messaging or multi-party workflow systems**  
- **No cloud services dependency** — must run fully self-hosted  

---

### Success Criteria (measurable, SRE-appropriate)
- System **survives arbitrary pod kill** on single-node Kubernetes without data loss  
- All **writes are auditable to user_id + request_id**, and reconstructable from event history  
- **Trace → Log → Metric correlation is provable in Grafana** within one click from Tempo to Loki to Mimir  
- **Shard routing works deterministically** — traffic distribution visible in observability without logs  
- **All execution is reproducible** from Git, including full teardown and redeploy in <30m  
- **Load generator can simulate failure pressure** while system maintains defined SLOs  
