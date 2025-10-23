---
title: Documentation Index
doc_type: policy
status: draft
version: 0.1.0
owners:
  - docs@pim-sre.lab
last_updated: 2024-05-18
tags:
  - navigation
  - documentation
---

# Documentation Index

Central index for all current documentation. Last updated values are sourced
from front matter when present; files without front matter display `N/A`.

## Requirements

| Document | Path | Description | Last Updated |
| --- | --- | --- | --- |
| Business Requirements | [docs/Requirements/Business_Requirements.md](Requirements/Business_Requirements.md) | Business objectives and success criteria for the lab. | N/A |
| Functional Requirements | [docs/Requirements/Functional_Requirements.md](Requirements/Functional_Requirements.md) | Functional capabilities required across services. | N/A |
| Non-Functional Requirements | [docs/Requirements/Non_functional_requirements.md](Requirements/Non_functional_requirements.md) | Reliability, performance, and compliance expectations. | N/A |
| Requirements Index | [docs/Requirements/00_requirements-index.md](Requirements/00_requirements-index.md) | Canonical list of BR/FR/NFR with stable IDs and owners. | N/A |
| Traceability Matrix | [docs/Requirements/01_traceability-matrix.md](Requirements/01_traceability-matrix.md) | Mapping of each requirement to design docs, tests, SLOs, and telemetry. | N/A |

## Architecture — Core System Design

| Document | Path | Description | Last Updated |
| --- | --- | --- | --- |
| Vision and Scope | [docs/Vison_and_Scope.md](Vison_and_Scope.md) | High-level product vision, scope boundaries, and success metrics. | N/A |
| C4: System Context (L1) | [docs/Architecture/01_c4-l1-system-context.md](Architecture/01_c4-l1-system-context.md) | Actors, trust boundaries, and external interactions. | N/A |
| C4: Containers (L2) | [docs/Architecture/02_c4-l2-containers.md](Architecture/02_c4-l2-containers.md) | Deployable services, data stores, and network paths per cluster. | N/A |
| C4: Components (L3) | [docs/Architecture/03_c4-l3-components.md](Architecture/03_c4-l3-components.md) | Internal components and data/control flow per service. | N/A |
| Runtime Sequence Catalog | [docs/Architecture/05_runtime-sequence-catalog.md](Architecture/05_runtime-sequence-catalog.md) | Key runtime flows: booking, encounter, billing, failover. | N/A |
| Domain Context Map | [docs/Architecture/10_domain-context-map.md](Architecture/10_domain-context-map.md) | Bounded contexts and upstream/downstream relationships. | N/A |
| Domain Model (UML) | [docs/Architecture/11_domain-model-uml.md](Architecture/11_domain-model-uml.md) | Logical domain entities and relations, pre-SQL. | N/A |
| API Surface | [docs/Architecture/17_api-surface.md](Architecture/17_api-surface.md) | Public/internal APIs, versioning, idempotency, and error contracts. | N/A |

## Architecture — Infrastructure & Reliability

| Document | Path | Description | Last Updated |
| --- | --- | --- | --- |
| Infrastructure Architecture | [docs/Architecture/infrastructure-architecture.md](Architecture/infrastructure-architecture.md) | End-to-end infra for two kubeadm clusters and inter-cluster networking. | N/A |
| Kubernetes Topology | [docs/Architecture/40_k8s-topology.md](Architecture/40_k8s-topology.md) | Namespaces, ingress, services, node pools, and autoscaling. | N/A |
| Storage Topology | [docs/Architecture/13_storage-topology.md](Architecture/13_storage-topology.md) | Datastores, replicas, shard/partition keys, and backups. | N/A |
| Availability & DR Topology | [docs/Architecture/30_availability-dr-topology.md](Architecture/30_availability-dr-topology.md) | HA layout, RPO/RTO targets, and failover drills. | N/A |
| Release Strategy | [docs/Architecture/41_release-strategy.md](Architecture/41_release-strategy.md) | CI/CD branching, promotion, rollback, and provenance. | N/A |

## Architecture — Events & Data Movement

| Document | Path | Description | Last Updated |
| --- | --- | --- | --- |
| Event Architecture | [docs/Architecture/14_event-architecture.md](Architecture/14_event-architecture.md) | Outbox, topics/queues, schemas, retention, retries, and DLQ. | N/A |

## Architecture — Observability

| Document | Path | Description | Last Updated |
| --- | --- | --- | --- |
| Observability Signal Dictionary | [docs/Architecture/50_observability-signal-dictionary.md](Architecture/50_observability-signal-dictionary.md) | Metrics, logs, traces per component with naming and cardinality rules. | N/A |
| SLI/SLO Measurement Plan | [docs/Architecture/51_sli-slo-measurement-plan.md](Architecture/51_sli-slo-measurement-plan.md) | SLIs, targets, windows, burn alerts, and runbooks. | N/A |

## Data

| Document | Path | Description | Last Updated |
| --- | --- | --- | --- |
| PIM SRE Glossary | [docs/02_Glossary.md](02_Glossary.md) | Canonical terminology and abbreviations for the platform. | 2024-05-18 |
| Database ERD (Mermaid) | [Database_erd_mermaid.md](../Database_erd_mermaid.md) | Entity relationship diagram for core data model. | N/A |

## Security

| Document | Path | Description | Last Updated |
| --- | --- | --- | --- |
| Naming and Filenames Policy | [docs/03a_Naming_And_Filenames.md](03a_Naming_And_Filenames.md) | Enforced filename conventions and deviation process. | 2024-05-18 |

## Ops

| Document | Path | Description | Last Updated |
| --- | --- | --- | --- |
| GPT-5 Working Agreement | [docs/04_GPT5_Working_Agreement.md](04_GPT5_Working_Agreement.md) | Guardrails and PR expectations for GPT-assisted changes. | 2024-05-18 |

## Templates

| Document | Path | Description | Last Updated |
| --- | --- | --- | --- |
| Templates Index | [docs/35_Templates_Index.md](35_Templates_Index.md) | Overview of available templates and governance rules. | 2024-05-18 |
| Design Doc Template | [docs/templates/00_Design_Doc_Template.md](templates/00_Design_Doc_Template.md) | Required structure for architecture and design proposals. | 2024-05-18 |
| ADR Template | [docs/templates/01_ADR_Template.md](templates/01_ADR_Template.md) | Standard format for architectural decision records. | 2024-05-18 |
| RFC Template | [docs/templates/02_RFC_Template.md](templates/02_RFC_Template.md) | Proposal template for changes needing cross-team review. | 2024-05-18 |
| Runbook Template | [docs/templates/03_Runbook_Template.md](templates/03_Runbook_Template.md) | Operational response playbook skeleton for on-call teams. | 2024-05-18 |

---

Last reviewed: 2025-10-23.
