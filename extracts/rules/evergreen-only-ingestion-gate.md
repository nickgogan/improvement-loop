---
title: "Evergreen-Only Ingestion Gate — Access, Don't Copy, Volatile Data"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "evergreen-vs-volatile-ingestion-rule"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "structuring-agent-context.harvest-queue"
identification_report: "structuring-agent-context.harvest-queue.md::evergreen-vs-volatile-ingestion-rule::rule::evergreen-only-ingestion-gate"
deployed: false
deployed_to: null
context:
  applies_to:
    - "curated knowledge bases, second-brain systems, or agent memory stores deciding what to ingest"
    - "designers of ingestion pipelines or skills that write into a durable knowledge store"
    - "any system that maintains both a durable curated corpus and one or more live systems of record it could copy data from"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "medium — un-ingesting a wrongly-copied volatile item requires locating and removing it and verifying nothing downstream depends on the stale copy; changing the ingestion policy going forward is a one-line gate edit"
  auditability: "high — every ingestion decision can be checked against the stated test ('would this still be good to have in a year'); an ingestion path can log its evergreen/volatile classification as an explicit, inspectable decision"
  evidence_strength: "Medium"
  adoption:
    status: "Partially Adopted"
    notes: "Practitioner-run in production for a live business second-brain system. Partially adopted in at least one curated-knowledge-base deployment that keeps its curated corpus local and separate from a live operational system, reaching the latter via an access pointer rather than a copy."
contract:
  preconditions: "A curated, durable knowledge store (second brain, agent memory corpus, curated KB) exists or is being designed, alongside one or more live systems of record (chat threads, email, ticketing, customer records, or similar) that could be copied into it. An ingestion decision point exists — a moment where a candidate item is about to be written into the curated store."
  invariants: "Every candidate item is classified evergreen or volatile before ingestion, using the test: 'in a year, will it still be good to have this in the curated store?' Evergreen items — locked-in decisions, durable priorities, holistic context — are ingested as copies. Volatile items — live threads, live records, anything that changes on a short cycle — are never copied into the curated store; the store instead gets an access pointer or tool-level connection to the live system of record."
  governance: "Owner: whoever designs or operates the ingestion path (skill, agent, or manual curation process) feeding the knowledge store. The evergreen/volatile classification applies at every ingestion decision, not only at initial design. Any future automated or scheduled ingestion (e.g., an always-on ingestion job) must implement the same gate rather than bypass it for convenience."
  recovery: "If volatile data is found already copied into the curated store: remove the copy, replace it with an access pointer to the system of record, and audit for anything downstream that depended on the stale copy. If an evergreen judgment later proves wrong (a 'durable' decision gets superseded): do not silently edit or delete the record — append the supersession to a decisions log so the correction itself is durable and auditable. If access tooling to a system of record is missing or breaks: the curated store will appear to have a gap where that volatile category should be — treat this as an access-layer defect to fix, not a reason to copy the data in as a workaround."
tags:
  - "extracted-artifact"
  - "rule"
  - "knowledge-architecture"
  - "context-engineering"
  - "ingestion"
---

# Evergreen-Only Ingestion Gate — Access, Don't Copy, Volatile Data

**Source:** [[evergreen-vs-volatile-ingestion-rule]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A candidate item is about to be written into a curated, durable knowledge store, and a live system of record exists (or could exist) as the item's origin.

## Action

**Required:** Apply the ingestion-time test — "in a year, will it be good to have this memory in here?" — before writing. Ingest only items that pass (evergreen: durable decisions, priorities, holistic context). For items that fail (volatile: live threads, emails, live records, anything that changes on a short cycle), do not copy the data — instead give the store access to the live system of record.

**Forbidden:** Ingesting volatile data as a copy "just in case," even temporarily, without an explicit expiry or refresh mechanism. Treating a copy of live data as equivalent to a live access pointer.

## Boundary

Enforced at every ingestion decision point: manual curation, an ingestion skill, or any automated or scheduled ingestion process.

## Enforcement

- **Mechanism:** Apply the evergreen test to each candidate item before it is written.
- **Check (deterministic-enough):** `passes_evergreen_test(item) == true` → ingest as a copy. `== false` → do not copy; verify or provision an access pointer to the item's system of record instead.
- **Violation response:** A volatile copy found in the curated store is removed and replaced with an access pointer; a stale evergreen judgment is corrected via an appended supersession, never a silent edit.

## Rationale

An over-ingested curated store accumulates stale copies of data that changes faster than the store is curated — those copies compete with (and eventually contradict) the live truth, impose a recurring deletion/maintenance tax, and degrade retrieval quality by diluting genuinely durable knowledge with noise. The rule bounds the curated corpus to what curation actually buys: durable, low-churn knowledge. Volatile truth stays exactly one tool-call away in its own system of record instead of drifting out of sync inside a copy nobody remembers to refresh. Framed the other direction, this is also what keeps ingestion a deliberate, controllable act rather than an always-on autonomous process — the classification decision is the point where a human or a policy stays in the loop.

## Failure Modes

- **Wrong evergreen judgment at ingestion time.** A decision classified as durable gets superseded later. Mitigation: don't silently rot the old entry — maintain a decisions log that appends supersessions so the correction itself is auditable.
- **Under-ingestion from broken access tooling.** If the connection to a system of record is missing or breaks, the curated store simply doesn't know the volatile half exists — this looks like a knowledge gap but is actually an access-layer defect, and the fix is restoring access, not copying the data in.
- **Drift toward convenience copying.** Under time pressure, it is easier to paste a volatile snippet into the curated store than to wire up proper access — this defeats the rule's purpose and reintroduces the maintenance tax the gate exists to avoid.

## Contract

### Preconditions
A curated, durable knowledge store (second brain, agent memory corpus, curated KB) exists or is being designed, alongside one or more live systems of record (chat threads, email, ticketing, customer records, or similar) that could be copied into it. An ingestion decision point exists — a moment where a candidate item is about to be written into the curated store.

### Invariants
Every candidate item is classified evergreen or volatile before ingestion, using the test: "in a year, will it still be good to have this in the curated store?" Evergreen items — locked-in decisions, durable priorities, holistic context — are ingested as copies. Volatile items — live threads, live records, anything that changes on a short cycle — are never copied into the curated store; the store instead gets an access pointer or tool-level connection to the live system of record.

### Governance
Owner: whoever designs or operates the ingestion path (skill, agent, or manual curation process) feeding the knowledge store. The evergreen/volatile classification applies at every ingestion decision, not only at initial design. Any future automated or scheduled ingestion (e.g., an always-on ingestion job) must implement the same gate rather than bypass it for convenience.

### Recovery
If volatile data is found already copied into the curated store: remove the copy, replace it with an access pointer to the system of record, and audit for anything downstream that depended on the stale copy. If an evergreen judgment later proves wrong (a "durable" decision gets superseded): do not silently edit or delete the record — append the supersession to a decisions log so the correction itself is durable and auditable. If access tooling to a system of record is missing or breaks: the curated store will appear to have a gap where that volatile category should be — treat this as an access-layer defect to fix, not a reason to copy the data in as a workaround.
