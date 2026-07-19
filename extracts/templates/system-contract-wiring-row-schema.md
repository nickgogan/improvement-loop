---
title: "System-Contract Wiring-Row Schema"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "machine-readable-system-contract-with-wiring-rows"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "building-agentic-systems.harvest-queue"
identification_report: "building-agentic-systems.harvest-queue.md::machine-readable-system-contract-with-wiring-rows::template::system-contract-wiring-row-schema"
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams packaging a multi-file agentic system for install onto a different host or harness"
    - "specification authors who need a machine-checkable statement of what a target platform must provide versus what can degrade gracefully"
    - "system designers building a portability contract that stays honest under incomplete target-platform support"
    - "auditors who need a mechanical way to check whether a documented install contract still matches the live wired files"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — a document/schema convention; dropping the wiring-row format reverts to prose install notes with no migration cost"
  auditability: "high — tier, capability IDs, and invariant are structured per-row fields, so row completeness and invariant-per-row presence are mechanically checkable; pairing the schema with a file-hash manifest over the wired files gives an automatable drift check between the documented contract and the live install"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Documented as a design-gate decision in one production agentic system's install canon; not yet adopted elsewhere."
contract:
  preconditions: "An installable multi-file agentic system exists whose harness-integration concerns can be individually named (entry points, rule injection, memory scopes, registries, invocation context, and similar). Each concern's owner can state whether the system can function at all without it."
  invariants: "Every wiring row states exactly five fields: tier (required|optional), capabilities (IDs drawn from a controlled, shared vocabulary — not free text per row), purpose, degradation, and invariant. A `required` row names the minimum satisfier and carries no degradation path. An `optional` row always names a fallback — typically a prose description of manual/weaker handling — that still preserves the row's invariant; the degradation is the worst-case guarantee, not an escape hatch that lets the invariant lapse. If a companion human-readable document exists, it is generated from the rows, never hand-edited independently — the rows are the single source of truth."
  governance: "Owned by whoever authors the target system's install or adaptation canon. Rows are added or changed only through the process that owns the schema — not ad hoc per-install edits. When a row's real-world satisfier changes (harness migration, a capability added or removed), the row is updated at the source, and any derived prose or downstream copies are regenerated rather than patched independently."
  recovery: "If a required row has no satisfier on the target platform, the install is blocked — do not silently substitute a degraded path for a required row. If an optional row's degradation path is invoked, record which degradation applied so the gap stays auditable instead of silent. If a drift check (e.g. a hash manifest over the wired files) shows the live install has diverged from the documented rows, treat the documentation as stale and regenerate it before trusting it for any decision. If two rows are found to protect the same invariant, merge them rather than letting both drift independently."
tags:
  - "extracted-artifact"
  - "template"
  - "system-contract"
  - "portability"
  - "capability-vocabulary"
---

# System-Contract Wiring-Row Schema

**Source:** [[machine-readable-system-contract-with-wiring-rows]]
**Form:** template
**Extraction date:** 2026-07-19

A fillable five-field row schema for the "wiring" section of a machine-readable system contract — the part of an installable agentic system's self-description that states, per harness-integration concern, what the target platform must supply and what happens when it can't. Each row is small enough to read in one glance and complete enough to gate an install: a target that fails a `required` row cannot run the system at all; a target that only partially satisfies an `optional` row still preserves the row's invariant via its named degradation path. The schema is meant to be instantiated once per harness-integration concern (entry point, rule injection, memory store, registry, and so on) and assembled into one contract document or file per system.

## Variables

| Variable | Type | Description |
|----------|------|-------------|
| `{{CONCERN_NAME}}` | identifier | Short stable name for the harness-integration concern this row covers (e.g. `always-on-entry`, `path-scoped-rules`, `scoped-memory-store`). |
| `{{TIER}}` | enum: `required` \| `optional` | `required` = do not install without a satisfier; check this before paying any adaptation cost. `optional` = install and record the degradation. |
| `{{CAPABILITIES}}` | list of IDs | One or more capability IDs drawn from a controlled, shared vocabulary (e.g. `always-on-instruction-injection`, `path-scoped-rule-injection`, `scoped-memory-store`, `human-approval-channel`). Not free text — the vocabulary is what lets rows compare across systems. |
| `{{PURPOSE}}` | string | One sentence: what this concern is for, in plain language. |
| `{{DEGRADATION}}` | string | The fallback if the target platform cannot natively satisfy the capabilities — almost always a named prose or manual substitute. For `required` rows, this is typically "none — no acceptable degradation exists" (the row blocks install instead). |
| `{{INVARIANT}}` | string (testable) | The property that must survive *any* adaptation, however the target platform ends up satisfying the row. Phrased so it can be checked, not just asserted. |

## Body

```yaml
wiring:
  - concern: "{{CONCERN_NAME}}"
    tier: "{{TIER}}"                # required | optional
    capabilities:
      - "{{CAPABILITIES[0]}}"
      # - "{{CAPABILITIES[1]}}"     # add one line per capability ID
    purpose: "{{PURPOSE}}"
    degradation: "{{DEGRADATION}}"  # required rows: "none — no acceptable degradation"
    invariant: "{{INVARIANT}}"

  # Repeat one block per harness-integration concern.
```

## Usage

Enumerate every harness-integration concern the system actually depends on before filling any row — an incomplete concern list is a worse failure than an imperfect row, because a missing row means a silent, undeclared assumption at install time. For each concern: set the tier first (this determines whether a degradation entry is even meaningful), pick capability IDs from the shared vocabulary rather than inventing new free-text labels per row, and write the invariant last, phrased so a reviewer — human or automated — could check it against the actual target platform. If a prose companion document exists alongside the row set, generate it from the rows; never let the two diverge by hand-editing the prose separately.

Two independent parties read the same row set for different purposes: a system deciding whether to trust and adopt another (does the offered system's contract fit what I can host?) and an installer computing whether a specific target host can run this system (which rows are satisfied, which degrade, which block). Keep both purposes in mind — the schema does not distinguish reader intent, only what's true about the concern.

## Variation Axis

- **Vocabulary granularity.** A coarse capability vocabulary (few, broad IDs) is easy to satisfy-check but blurs real differences between platforms; an over-detailed vocabulary invites classification debates about which ID a given platform feature actually maps to. Calibrate toward the smallest vocabulary that still lets required rows fail unambiguously.
- **Degradation depth.** Some rows degrade once (native → prose); others may have a staged fallback chain (native → partial-native → prose). The schema as written assumes one degradation step; systems with staged fallbacks either flatten to the worst-case single step or extend the row with an ordered list — document the choice explicitly if extending.
- **Drift-detection pairing.** A row set with no accompanying integrity check (e.g., a hash manifest over the files each row references) can silently go stale as the real install evolves. Pairing the schema with any mechanical drift check meaningfully raises its trustworthiness; using it as an unaudited static document lowers it.

## Contract

### Preconditions
An installable multi-file agentic system exists whose harness-integration concerns can be individually named (entry points, rule injection, memory scopes, registries, invocation context, and similar). Each concern's owner can state whether the system can function at all without it.

### Invariants
Every wiring row states exactly five fields: tier (required|optional), capabilities (IDs drawn from a controlled, shared vocabulary — not free text per row), purpose, degradation, and invariant. A `required` row names the minimum satisfier and carries no degradation path. An `optional` row always names a fallback — typically a prose description of manual/weaker handling — that still preserves the row's invariant; the degradation is the worst-case guarantee, not an escape hatch that lets the invariant lapse. If a companion human-readable document exists, it is generated from the rows, never hand-edited independently — the rows are the single source of truth.

### Governance
Owned by whoever authors the target system's install or adaptation canon. Rows are added or changed only through the process that owns the schema — not ad hoc per-install edits. When a row's real-world satisfier changes (harness migration, a capability added or removed), the row is updated at the source, and any derived prose or downstream copies are regenerated rather than patched independently.

### Recovery
If a required row has no satisfier on the target platform, the install is blocked — do not silently substitute a degraded path for a required row. If an optional row's degradation path is invoked, record which degradation applied so the gap stays auditable instead of silent. If a drift check (e.g. a hash manifest over the wired files) shows the live install has diverged from the documented rows, treat the documentation as stale and regenerate it before trusting it for any decision. If two rows are found to protect the same invariant, merge them rather than letting both drift independently.
