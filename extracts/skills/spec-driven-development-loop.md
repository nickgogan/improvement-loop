---
title: "Spec-Driven Development Loop"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "specification-as-governance-fourth-enforcement-philosophy"
identification_report: "agent-governance-and-trust.harvest-queue.md::specification-as-governance-fourth-enforcement-philosophy::skill::spec-driven-development-loop"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agentic development workflows where a written specification governs implementation work and the agent is expected to keep the two aligned across multiple edits"
    - "governance-by-spec systems that treat written specifications as the source of truth for architectural decisions, behavioral contracts, or conformance tests"
    - "specification-driven coding agents that implement TODO-tracked work items against a checked-in spec file rather than against ad-hoc instructions"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — the skill is a procedural pattern; removing it from a workflow leaves spec and code in their last-reconciled state and requires no migration"
  auditability: "high when each loop iteration writes a reconciliation entry (commit message, TODO checkbox transition, or change-log line) tying spec edits and code edits to the same change; medium when reconciliation is recorded only in the agent's working notes; low when reconciliation is implicit"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Practitioner-observed in n8n's spec-driven development Claude Code skill (`.claude/specs/`). No widespread published adoption pattern beyond this and adjacent conformance-suite implementations (LangGraph)."
contract:
  preconditions: "A specification file exists at a known location (e.g., `.claude/specs/<feature>.md`) and is treated by project policy as the source of truth for the feature being implemented. The spec contains either trackable work items (TODO checkboxes, numbered requirements, conformance assertions) or a structure from which such items can be derived. The implementation surface (code paths, modules, tests) referenced by the spec is identified before invocation. The caller has authority to edit both the spec and the code."
  invariants: "The loop terminates only when spec and code agree on every tracked work item — each item is either implemented (code conforms; checkbox checked) or explicitly skipped (annotated in the spec with rationale; struck through). The spec is the source of truth: when spec and code disagree, exactly one of them is updated in the same iteration to restore agreement; the other side is never silently mutated. No iteration ends with a tracked item in an indeterminate state (neither resolved nor explicitly deferred). The spec file, after the loop completes, accurately reflects the code that exists."
  governance: "Owner: the policy that declares the spec the source of truth — the project convention file, the skill or workflow that enforces spec-driven development, or the change-management policy. The loop does not invent work items; items are added or modified only by deliberate spec edits, not as a side effect of implementation. Reconciliation events (a TODO transitioning to checked, a strikethrough being added, a spec sentence being rewritten to match new code) are the primary audit artifact and must be visible in the change record. If the skill operates in a regulated or load-bearing context, the final spec-and-code state must be reviewable by a human before deployment."
  recovery: "If implementation reveals that the spec is wrong (the spec describes behavior that cannot or should not be built): halt the loop on that item; update the spec in place with the corrected requirement; record the spec edit explicitly before resuming code work. If a tracked item cannot be implemented in the current cycle (out of scope, blocked, deliberately deferred): strike it through in the spec with a brief annotation (`~~item~~ — deferred: <reason>`); do not silently leave it unchecked. If the loop discovers drift accumulated from prior cycles (existing code does not match existing spec sentences): treat each disagreement as a reconciliation item — choose which side is authoritative for that item, update the other, then proceed. If the spec file is missing, malformed, or has no trackable items: halt before generating any code; surface the precondition failure to the caller."
tags:
  - "extracted-artifact"
  - "skill"
  - "spec-driven-development"
  - "governance"
  - "bidirectional-sync"
  - "specification-as-governance"
---

# Spec-Driven Development Loop

**Source:** [[specification-as-governance-fourth-enforcement-philosophy]]
**Form:** skill
**Extraction date:** 2026-04-27

Companion rule: [[spec-and-code-reconcile-bidirectionally]] — the invariant this skill operationalizes.

## Inputs

- **Spec file path:** A path to a checked-in specification file (e.g., `.claude/specs/<feature>.md`) that the project treats as the source of truth for the feature in scope. The spec must contain trackable work items: TODO checkboxes (`- [ ]`/`- [x]`), numbered requirements, conformance assertions, or an equivalent structure from which the agent can derive a discrete item list.
- **Implementation surface:** The code paths, modules, or tests that the spec governs. Either declared in the spec itself (preferred) or supplied by the caller. The agent must know where to read and where to write.
- **Reconciliation marker convention:** How the loop will record per-item progress in the spec — TODO checkbox toggles, strikethrough+annotation for deferred items, change-log entries, or commit-message references. The convention should already be project policy; the skill follows it, does not invent it.
- **Optional — change-record destination:** A file or location where reconciliation events are written for audit (e.g., commit messages, a `CHANGELOG.md` entry, a session log). If omitted, reconciliation is recorded only in the spec file itself.
- **Optional — max iterations:** A cap on the number of read-implement-verify-reconcile cycles before the skill halts and surfaces remaining work. Recommended default: one cycle per remaining unresolved item, plus a safety cap (e.g., 10) to prevent runaway loops on pathological specs.

## Procedure

1. **Read the spec.** Open the spec file. Enumerate the tracked work items in document order. For each item, record its current state: `unchecked` (work to do), `checked` (claimed complete), `struck-through` (deliberately skipped), `ambiguous` (cannot determine state — surface as a precondition failure). The enumerated list is the loop's working state — call it `items`.

2. **Verify current alignment.** For each `checked` and `struck-through` item, sanity-check the implementation surface: does the code reflect the claim? If a `checked` item has no corresponding code (or vice versa), record a `drift` entry against that item. Drift entries are reconciled before proceeding to new work — the loop does not build on top of unresolved disagreement between spec and code.

3. **Pick the next unresolved item.** From `items`, select the first entry whose state is `unchecked` or has a `drift` entry. If no such item exists → loop is complete; jump to step 7.

4. **Implement (or update the spec).** For an `unchecked` item with no drift: write the code that makes the item true. For a drift entry: decide which side is authoritative (the spec sentence or the existing code), and update the other to match. If implementation reveals the spec is wrong (item cannot or should not be built as written): edit the spec sentence in place to reflect the corrected requirement; record the spec edit explicitly before continuing. If the item is genuinely out of scope or deferred: strike it through with an annotation (`~~item~~ — deferred: <reason>`) — do not leave it `unchecked`.

5. **Verify alignment for this item.** Re-read the spec sentence and the code that should now satisfy it. Confirm: spec says X, code does X. If they disagree, return to step 4 for this item before advancing — do not move on with disagreement live.

6. **Reconcile in the spec.** Toggle the item's marker per the project convention (checkbox to `[x]`, strikethrough applied, or equivalent). If a change-record destination was supplied, write the reconciliation event there as well (e.g., commit message, change-log line). Return to step 3.

7. **Final pass — completeness check.** Re-enumerate `items` from the spec. Confirm: every item is in a terminal state (`checked` or `struck-through`); no item is `unchecked`; no item has an open drift entry. If any item fails this check, the loop did not complete — surface the failing items as the loop's output and halt without claiming completion.

8. **Emit final state.** The loop's outputs are: the updated spec file (now reflecting the implemented + deferred state), the implementation changes made, and the reconciliation log (per-item: what was done, what was deferred, what drift was resolved). The final spec is the loop's primary artifact.

## Outputs

- **Updated spec file:** The spec, edited in place, with every tracked item in a terminal state — checked, struck-through with annotation, or rewritten to reflect a corrected requirement. The spec at exit is what the spec at entry would have been if it had matched the code from the start.
- **Implementation changes:** The code edits made during the loop. Each change ties to a specific spec item via the reconciliation marker (commit message, change-log line, or in-line spec reference).
- **Reconciliation log:** A per-item record of: starting state, action taken (implement / update-spec / strike-through), ending state, and any drift resolved. This log is the audit artifact for the loop run; it must exist whether the loop completed or halted incomplete.
- **Completion verdict:** Either "loop complete — all items terminal" or "loop halted — items remaining: [list]" with the reason for each remaining item.

## Boundary

**In scope:**
- Reconciling spec and code on a feature whose spec already exists and is the source of truth.
- Resolving drift between an existing spec sentence and existing code (which side wins is decided per item).
- Marking items as deferred with explicit annotation when the work is out of scope for the current cycle.
- Updating the spec when implementation reveals the spec was wrong, before continuing with the work.

**Out of scope:**
- Authoring a new spec from scratch — the loop reads an existing spec; spec authorship is a separate workflow.
- Adjudicating governance disputes about whether the spec should be the source of truth in this project — that policy is a precondition, not a loop output.
- Editing code that is not governed by the spec (e.g., refactors, unrelated improvements) — the loop's surface is what the spec covers.
- Long-horizon planning across multiple specs — the loop runs against a single spec at a time.

## Failure Modes

- **Spec drift not detected at the start.** If step 2 (verify current alignment) is skipped or rushed, the loop builds on a foundation where existing `checked` items don't actually match the code. Subsequent reconciliations layer onto a corrupted base. Mitigation: step 2 is non-optional; treat any `checked` item with no implementation evidence as a drift entry and resolve it before new work.

- **Spec edits made silently during implementation.** The agent updates the spec to match what was easier to build, without recording the edit as a deliberate spec change. This converts the spec from "source of truth" to "rationalization log." Mitigation: every spec edit during the loop must be recorded as an explicit reconciliation event in the log, with rationale ("spec sentence X corrected because behavior Y is unbuildable as originally specified"). Implicit spec mutation is treated as a contract violation.

- **Items left in `unchecked` state at exit.** The loop terminates with work items neither implemented nor explicitly deferred. The spec then misrepresents the project's actual state. Mitigation: step 7 is the gate — every item must be in a terminal state; an `unchecked` item at exit means the loop halted, not completed, and the verdict must say so.

- **Strikethrough used as a hiding mechanism.** Items struck through without a real annotation become invisible to future review. The deferred-item pile grows indefinitely. Mitigation: every strikethrough requires an annotation explaining why; the reconciliation log carries the annotation forward; periodic review of struck-through items is a separate maintenance discipline (out of this skill's scope, but the annotation makes that review possible).

- **Reconciliation between iterations skipped.** The loop advances to the next item before confirming the current item's spec edit and code edit agree (step 5 short-circuited). Drift is created within the loop itself. Mitigation: step 5 must complete before step 6; if a verification fails, the loop returns to step 4 for the same item, not the next.

- **Loop oscillation on contradictory items.** Two items in the spec contradict each other; implementing one forces the other to fail; reconciling that one breaks the first. Mitigation: detect oscillation (same item alternating between `checked` and drift across iterations); halt; surface the contradicting items to the caller; do not continue looping.

- **Max iterations reached with items remaining.** A pathological spec with many items, deep drift, or genuine ambiguity exhausts the cap before completion. Mitigation: emit the partial reconciliation log and the remaining-items list; report "halted — items remaining" rather than a false-pass; the next loop run starts from the partial state.

## Contract

### Preconditions
A specification file exists at a known location (e.g., `.claude/specs/<feature>.md`) and is treated by project policy as the source of truth for the feature being implemented. The spec contains either trackable work items (TODO checkboxes, numbered requirements, conformance assertions) or a structure from which such items can be derived. The implementation surface (code paths, modules, tests) referenced by the spec is identified before invocation. The caller has authority to edit both the spec and the code.

### Invariants
The loop terminates only when spec and code agree on every tracked work item — each item is either implemented (code conforms; checkbox checked) or explicitly skipped (annotated in the spec with rationale; struck through). The spec is the source of truth: when spec and code disagree, exactly one of them is updated in the same iteration to restore agreement; the other side is never silently mutated. No iteration ends with a tracked item in an indeterminate state (neither resolved nor explicitly deferred). The spec file, after the loop completes, accurately reflects the code that exists.

### Governance
Owner: the policy that declares the spec the source of truth — the project convention file, the skill or workflow that enforces spec-driven development, or the change-management policy. The loop does not invent work items; items are added or modified only by deliberate spec edits, not as a side effect of implementation. Reconciliation events (a TODO transitioning to checked, a strikethrough being added, a spec sentence being rewritten to match new code) are the primary audit artifact and must be visible in the change record. If the skill operates in a regulated or load-bearing context, the final spec-and-code state must be reviewable by a human before deployment.

### Recovery
If implementation reveals that the spec is wrong (the spec describes behavior that cannot or should not be built): halt the loop on that item; update the spec in place with the corrected requirement; record the spec edit explicitly before resuming code work. If a tracked item cannot be implemented in the current cycle (out of scope, blocked, deliberately deferred): strike it through in the spec with a brief annotation (`~~item~~ — deferred: <reason>`); do not silently leave it unchecked. If the loop discovers drift accumulated from prior cycles (existing code does not match existing spec sentences): treat each disagreement as a reconciliation item — choose which side is authoritative for that item, update the other, then proceed. If the spec file is missing, malformed, or has no trackable items: halt before generating any code; surface the precondition failure to the caller.
