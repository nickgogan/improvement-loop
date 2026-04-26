---
title: "Fix Data and Schema Before Automating"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "fix-data-schema-before-automating"
extraction_date: "2026-04-19"
last_change_session: 44
last_change_sl: "session-44-codifier-extraction-run"
identification_report: "2026-04-19-identification-report-4.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "workflow automation design where agents read from or write to structured data stores"
    - "agentic coding systems operating on knowledge bases, CRM records, or any structured data"
    - "agent deployment gates where schema validation is a prerequisite"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "high — automation built on unvalidated data requires full halt, data audit, schema definition, and restart; accumulated dirty records may require manual remediation"
  auditability: "high — machine-readable schemas and validation run results are directly inspectable; compliance is verifiable before automation begins"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Pattern is partially adopted via _schema.yaml in this project; not yet enforced as a gate before agent workflow automation."
contract:
  preconditions: "A workflow automation is being designed that reads or writes data. The data stores are known. A schema authoring mechanism is available."
  invariants: "No automation runs against data that has not passed schema validation. Schemas are versioned and stored alongside the automation. Conflict resolution strategies are documented before the first run."
  governance: "Owner: MetaSystem / Claude Build system. _schema.yaml modifications require Nick's authorization. Applies at workflow design gate and every schema change event."
  recovery: "If automation running against unvalidated data: halt immediately, run full validation, resolve violations, obtain sign-off before restarting."
tags:
  - "extracted-artifact"
  - "rule"
---

# Fix Data and Schema Before Automating

**Source:** [[fix-data-schema-before-automating]]
**Form:** rule
**Extraction date:** 2026-04-19

## Condition

Before any workflow automation is designed, built, or deployed that will read from or write to any data store.

## Action

The following MUST be completed and validated before automation begins:
1. **Single source of truth:** Identify and designate exactly one authoritative location for each data entity.
2. **Explicit schema:** Define schemas for all data the agent will read or write. Schemas must be machine-readable and versioned.
3. **Validation rules:** Build and run validation against the schema on existing data before automation operates on it.
4. **Conflict resolution strategy:** Decide explicitly how conflicts are resolved — do not leave to runtime improvisation.

Automation MUST NOT proceed on data that has not passed schema validation.

## Boundary

Enforced at workflow design gate, before any implementation work begins. Revalidated when the schema changes or when a new data source is added.

## Enforcement

- A machine-readable schema file must exist and be versioned before implementation starts.
- A validation pass must be run against current data; results documented.
- Conflict resolution strategy must be written down (not assumed).
- Anti-pattern flag: Any automation designed before a schema file exists is non-compliant.
- Anti-pattern flag: Treating schema validation as a post-deployment task is non-compliant.
- Reference: MetaSystem's own `_schema.yaml` is the canonical in-project example.

## Rationale

The $14K voice agent failure case study: no schemas specified, records scattered across systems, funnel measurement impossible despite the system being "up and functioning." Schema-first design is the prerequisite that makes agent work sustainable. Day 1 vs. Day 30 degradation compounds when schema violations are never caught at source.

## Contract

### Preconditions
A workflow automation is being designed that reads or writes data. The data stores are known. A schema authoring mechanism is available.

### Invariants
No automation runs against data that has not passed schema validation. Schemas are versioned and stored alongside the automation. Conflict resolution strategies are documented before the first run.

### Governance
Owner: MetaSystem / Claude Build system. _schema.yaml modifications require Nick's authorization. Applies at workflow design gate and every schema change event.

### Recovery
If automation running against unvalidated data: halt immediately, run full validation, resolve violations, obtain sign-off before restarting.
