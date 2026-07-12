---
name: 'Deterministic Store Checker with Runtime-Computed Threshold Flags'
summary: 'A small script is the deterministic arbiter of a markdown memory store: it regex-validates every entry against the documented schema and emits informational threshold flags (lesson at promotion threshold, skill at eval-readiness) computed at runtime. Counts are never stored in the files themselves — they are recomputed on every check, eliminating a whole class of drift. Exit codes distinguish valid, violated, and not-yet-initialized.'
implementation_notes: 'How this could apply to the MetaSystem engine — Phase 2 of its restructure program will size a second-brain-for-operations against this store model; IB-172 (layered memory architecture) is the related backlog item. This is Nick''s standing no-hardcoded-counts rule made executable: the checker is where counts live. The engine''s pre-commit frontmatter hook is the same species; a store checker would extend it to operational memory.'
category: Evaluation
evidence_strength: Medium (practitioner-documented, single production system with live store evidence)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-ops-self-improve.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: raw
consumed_by: []
tags:
- deterministic-validation
- schema-check
- threshold-flags
- no-stored-counts
---

# Deterministic Store Checker with Runtime-Computed Threshold Flags

## Why It Matters

A markdown-native memory store is only trustworthy if something other than an LLM enforces its schema — free-text capture drifts within days otherwise (CareerBuddy accumulated 9 silent schema violations in its first live capture sessions). A ~170-line script makes conformance binary and makes "what needs attention" a computed output rather than a maintained number. The agent runs it before ending any turn that wrote to the store; validation stops being a judgment call.

## What It Is

CareerBuddy's `store_check.py` validates the three schema-bearing store files (`lessons.md`, `eval-candidates.md`, `proposal-log.md`) against the authoritative schema doc and emits two informational flag types:

- `PROMOTE:` — an open lesson whose Occurrences count meets the threshold (N=2 normal, 1 high).
- `EVAL-READY:` — a skill section with ≥15 usable real phrasings (router-mediated entries excluded), ready for eval-set authoring.

Exit codes: `0` = schema valid (flags are informational), `1` = violations, `2` = store not initialized — "not an error for a fresh store, but distinct."

## How It Works

- **Regex-anchored entry grammar.** Headers (`## L-<seq> · date · severity · status`, `## P-<seq> · date · L-<seq> · applied|declined`) and required body fields each have a compiled pattern; a malformed line is named in the error output. Sequence numbers are checked monotonic and duplicate-free.
- **Doc rules over script.** The schema doc states: "if this document and the script disagree, fix the script (this document rules)" — the prose schema is canonical, the script is its enforcement.
- **Counts are runtime-only.** The readiness count is computed per run and reported in the flag output; the store files never carry counters. When router-mediated entries had to be excluded from readiness (L-17/P-13), the fix was a marker prefix (`routed:`) plus a regex — the checker "reports them separately at runtime — never store counts in this file."
- **Checker and schema co-evolve through the same gate.** Live capture produced entry shapes the schema rejected (annotation parentheticals, hybrid verdicts — L-7); the fix was a gated proposal (P-5) editing schema doc + regex together, taking the live store from FAIL(9) to PASS(0). Growth-bound rules (date-list dedup, P-15) landed the same way.
- **Scoped tolerance.** The freeform `improve-backlog.md` is explicitly exempt — the checker validates what has a schema and ignores what deliberately doesn't.

## How It Could Fail

- Regex grammars are brittle against legitimate new annotation needs — CareerBuddy needed two schema amendments in five days; without a cheap gated amendment path the checker becomes a reason to stop capturing.
- Informational flags that nobody reads are dead code; CareerBuddy wires them into the skill's `status` mode so every store read surfaces them.
- A checker validates shape, not truth — an untraceable or wrong lesson in valid format passes; the evidence-trace rule is enforced by procedure, not by the script.
