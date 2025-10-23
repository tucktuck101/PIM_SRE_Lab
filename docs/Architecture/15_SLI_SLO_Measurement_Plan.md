---
title: TODO — Replace with SLI/SLO Measurement Plan Title
doc_type: sli_slo_measurement_plan
status: draft
version: 0.1.0
owners:
  - TODO@example.com
last_updated: YYYY-MM-DD
tags:
  - slo
  - observability
---

# Measurement Plan Overview

> Summarize the services or user journeys this plan covers and the business
> outcomes it protects. Reference driving requirements or commitments.

## Target Services and Dependencies

| Service / Journey | Description | Dependencies | Notes |
| --- | --- | --- | --- |
| TODO | Summarize scope | List critical dependencies | Ownership, SLAs |

## SLO Objectives

| SLO ID | Description | Target | Measurement Window | Error Budget |
| --- | --- | --- | --- | --- |
| SLO-001 | Describe the SLO | e.g., 99.9% | e.g., 30 days | Compute % allowance |

> Add rows for each SLO, tying them to BR/FR/NFR IDs where relevant.

## SLIs and Measurement

| SLI | Definition / Formula | Data Source | Collection Method |
| --- | --- | --- | --- |
| TODO | e.g., Good requests / Total requests | e.g., Prometheus | Describe pipeline/calculation |

## Alerting and Burn Rate Policies

> Document alert thresholds, burn rate monitors, paging policies, and who
> responds. Reference runbooks or on-call rotations.

## Reporting and Review Cadence

> Explain how SLO compliance is reported (dashboards, weekly reviews,
> postmortems), including responsible teams.

## Tooling and Automation

> List tooling, automation, or scripts supporting SLI/SLO measurement (e.g.,
> service-level objective tooling, data pipelines, synthetic checks).

## Risks and Open Questions

> Capture risks (missing telemetry, data quality, tooling gaps) and open
> questions. Assign owners and due dates.

## References

> Link to supporting documents: requirements, observability dictionary,
> runbooks, dashboards, ADRs, etc.

---

#### Notes

Last updated: YYYY-MM-DD (update before publishing)
