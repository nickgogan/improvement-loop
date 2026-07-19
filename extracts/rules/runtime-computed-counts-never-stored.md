---
title: "Runtime-Computed Counts, Never Stored"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "deterministic-store-checker-runtime-threshold-flags"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "verifying-agent-output.harvest-queue"
identification_report: "verifying-agent-output.harvest-queue.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "markdown-native or free-text stores (memory files, backlog logs, lesson stores) that track counts, thresholds, or readiness flags"
    - "validation scripts or checkers that enforce schema conformance on operational data files"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "low — once stored counts have accumulated with baked-in values, removing them requires a migration pass to strip the values and confirm the checker re-derives the same numbers at runtime"
  auditability: "high — the checker's exit code and flag output are deterministic and inspectable; schema violations name the exact offending line"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "A markdown-native or similarly free-text store tracks entries with counters, thresholds, or readiness flags (e.g., occurrence counts, promotion thresholds, eval-readiness counts), and a companion checker script exists, or is being designed, to validate the store's schema."
  invariants: "Counts, thresholds, and readiness flags are never persisted as literal values inside the store files themselves — they are recomputed by the checker on every run and reported as flag output. Store entries follow a documented, regex-anchored grammar; the checker validates every entry against it and names the specific malformed line on violation. The checker exposes distinct exit codes for valid, violated, and not-yet-initialized states."
  governance: "Owner: whoever authors the store's schema doc and the checker script. Schema and checker co-evolve through the same gated-change path — the schema doc is normative prose, the checker is its executable enforcement; on disagreement, the script is fixed to match the documented schema, not silently patched around it."
  recovery: "If a stored count or threshold value is found inside a store file (schema drift), treat it as a violation — remove the stored value and confirm the checker still derives the same number at runtime. If the checker's regex rejects a legitimate new entry shape, that is a schema gap, not a data error — fix it via a gated schema-and-checker amendment, never by manually bypassing validation."
tags:
  - "extracted-artifact"
  - "rule"
  - "deterministic-validation"
  - "no-stored-counts"
---

# Runtime-Computed Counts, Never Stored

**Source:** [[deterministic-store-checker-runtime-threshold-flags]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A markdown-native (or otherwise free-text) memory or operational store — a lesson log, backlog, capture buffer, or similar — needs counts, thresholds, or readiness flags (e.g., "this item has occurred N times," "this item is ready for the next stage") to drive downstream action, and a checker script exists or is being designed to keep that store schema-conformant.

## Action

**Required:** Compute counts, thresholds, and readiness flags at runtime, on every check, from the store's actual entries. Report them as informational flag output from the checker rather than as data fields inside the store file. Give the store entries a documented, regex-anchored grammar and validate every entry against it on every run, naming the specific malformed line when validation fails. Distinguish valid / violated / not-yet-initialized states with distinct exit codes.

**Forbidden:** Writing a count, threshold-met flag, or readiness marker as a literal stored value inside the store file itself. Treating the checker's regex grammar as fixed once written — when the documented schema and the script disagree, fix the script to match the schema, not the other way around, and do so through a gated amendment that updates both together.

## Boundary

Enforced at the checker script itself (the deterministic arbiter of the store) and at the point the store is written to — ideally the agent or process runs the checker before ending any turn that wrote to the store, so validation is never a deferred judgment call.

## Enforcement

- **Mechanism:** A compiled regex or equivalent pattern per required field/header shape; a malformed line is named in the checker's error output, not just flagged generically.
- **Check (deterministic):** `(entry conforms to documented grammar) AND (no literal count/threshold/readiness field is present in the stored entry)`. Any branch false → violation.
- **Violation response:** a stored literal count/flag is schema drift — strip it and confirm the checker re-derives the same value at runtime; a regex rejection on a legitimate new entry shape is a schema gap — file a gated schema-and-checker amendment rather than bypassing the check.

## Rationale

A free-text store drifts from its schema within days without something other than an LLM enforcing conformance. Making the checker the deterministic arbiter turns "what needs attention" into a computed output instead of a manually maintained number, which eliminates a whole class of stale-count drift: a stored count can silently fall out of sync with the entries it's supposed to summarize, but a runtime-computed count cannot. This mirrors a broader no-hardcoded-counts discipline: any number that could go stale should be derived, not written down.

## Failure Modes

- **Regex brittleness against legitimate new shapes.** A checker's grammar can reject entries that are valid but not yet anticipated — without a cheap, gated amendment path, the checker becomes a reason to stop capturing data rather than a guardrail.
- **Dead flags.** Informational flags nobody reads are dead code; wire them into whatever surface actually gets checked (a status command, a dashboard, a session-start read), not just into a log nobody opens.
- **Shape, not truth.** A checker validates that an entry is well-formed, not that its content is accurate or traceable — an untraceable or wrong entry in valid format still passes. Truth-checking is a separate procedural discipline layered on top.

## Contract

### Preconditions
A markdown-native or similarly free-text store tracks entries with counters, thresholds, or readiness flags (e.g., occurrence counts, promotion thresholds, eval-readiness counts), and a companion checker script exists, or is being designed, to validate the store's schema.

### Invariants
Counts, thresholds, and readiness flags are never persisted as literal values inside the store files themselves — they are recomputed by the checker on every run and reported as flag output. Store entries follow a documented, regex-anchored grammar; the checker validates every entry against it and names the specific malformed line on violation. The checker exposes distinct exit codes for valid, violated, and not-yet-initialized states.

### Governance
Owner: whoever authors the store's schema doc and the checker script. Schema and checker co-evolve through the same gated-change path — the schema doc is normative prose, the checker is its executable enforcement; on disagreement, the script is fixed to match the documented schema, not silently patched around it.

### Recovery
If a stored count or threshold value is found inside a store file (schema drift), treat it as a violation — remove the stored value and confirm the checker still derives the same number at runtime. If the checker's regex rejects a legitimate new entry shape, that is a schema gap, not a data error — fix it via a gated schema-and-checker amendment, never by manually bypassing validation.
