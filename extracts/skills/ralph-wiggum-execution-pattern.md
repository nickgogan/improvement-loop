---
title: "Ralph Wiggum Execution Pattern"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "ralph-wiggum-execution-pattern"
extraction_date: "2026-05-25"
last_change_session: 146
last_change_report: "2026-07-13-source-drift"
identification_report: "2026-05-24-identification-report-2.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "Complex individual work items that cannot be completed in a single agent pass — database schema migrations, multi-file refactors, multi-step configurations, research-to-implementation pipelines"
    - "Any agent workflow where context accumulation across iterations would push the model into degraded-performance territory (empirically ~100k tokens for large frontier models)"
    - "Teams building autonomous coding agents that need a structured iteration primitive with externalized state and deterministic termination — whether hand-rolled in a shell loop or declared as a workflow-engine node"
    - "Orchestration pipelines where a single work item must be driven to completion without human intervention between passes, but with a human-reviewable audit trail (spec, plan, per-iteration log)"
  platform_coupling: "agnostic"
  autonomy: "autonomous-only"
  stage: "build"
  reversibility: "low — the loop writes to the file system and modifies source code across iterations; each completed task changes the working directory state; reversing requires a clean git checkout captured before the loop started"
  auditability: "High when the spec, plan, and per-iteration log are retained — each iteration's task selection, implementation, and pass/fail result are independently verifiable; a schema-enforced loop node additionally emits per-iteration events/metrics. Low when only the final implementation is kept"
  evidence_strength: "Strong"
  adoption:
    status: "Partially Adopted"
    notes: "Production-tested across five independent orgs: Anthropic (drove a cosmological Boltzmann solver reimplementation over multiple days to sub-percent accuracy; framed as scaffolding against 'agentic laziness'), the AI Automators / practitioner corpus (headless per-task implementation), a headless orchestrator harness (breadth-plus-depth pairing), and Archon v0.5.0 — which promotes the loop from a shell idiom to a schema-enforced workflow-engine primitive and ships it as a default PRD-to-PR workflow. The pattern crossed from prompt idiom to a checkable engine primitive; the reference shell implementation (headless `claude -p` per pass) and the declarative loop-node implementation are two faces of the same shape."
contract:
  preconditions: "spec.md is complete and unambiguous before the loop starts. plan.md exists with a discrete, ordered task list. The working directory is in a clean, known-good state. Pass/fail criteria are runnable from the shell (or a deterministic completion check) without manual intervention. A per-iteration fresh-context mechanism is available — a headless invocation, or a workflow engine that resets the session and bridges the prior iteration's cleaned output forward. A maximum-iteration budget is set before the loop runs."
  invariants: "Each iteration runs in fresh context — no unbounded context inherited from prior iterations; at most the prior iteration's cleaned output is bridged forward. State is externalized to spec.md, plan.md, and the file system. The loop terminates: either the completion condition is met (all tasks pass, or a deterministic completion check succeeds) or the max-iteration cap is reached. plan.md is updated after each iteration. Pass/fail criteria are not modified between iterations within a run."
  governance: "Owner: the caller who defines spec.md, plan.md, the pass/fail criteria, and the max-iteration budget. The spec and plan are caller-owned — the looping agent fills in task completions but does not rewrite acceptance criteria. The per-iteration log (or the engine's iteration events/metrics) is the primary audit artifact. Where the loop is declared as a workflow-engine node, the loop config (completion signal, deterministic completion check, iteration cap, fresh-context flag, optional per-iteration human gate) is validated at load time."
  recovery: "Max iterations reached without completing: surface the iteration log, current state, and remaining tasks; escalate to human — do not treat partial completion as a full pass. Spec discovered incorrect mid-loop: halt, correct the spec, restart from the beginning. Fresh-context invocation fails: record the failure, retry once, escalate on the second failure. Non-converging loop (marginal changes, never a clean pass): treat as an under-specified spec or ambiguous completion check; halt and tighten before resuming."
tags:
  - "extracted-artifact"
  - "skill"
---

# Ralph Wiggum Execution Pattern

**Source:** [[ralph-wiggum-execution-pattern]]
**Form:** skill
**Extraction date:** 2026-05-25

A depth-first execution skill for complex individual work items. It drives one hard item to completion through repeated **fresh-context** passes: each iteration reads the spec and a progress-tracking `plan.md`, executes a single pass, then tests against pass/fail criteria before looping. The loop continues until the item passes verification or a maximum iteration count is hit. State lives in the spec, plan, and file system — never in an accumulating context window — so even multi-day projects run at full model intelligence throughout, well below the ~100k-token "dumb zone" where reasoning degrades.

The pattern exists in two interchangeable forms, and this skill covers both:

- **Reference shell implementation** — a bash loop spawning a headless agent (`claude -p`) per pass. This is the correct implementation; the in-session plugin variant runs inside one session and causes context rot.
- **Schema-enforced engine primitive** — a declarative `loop:` workflow-engine node (Archon v0.5.0) whose config schema encodes the full loop anatomy: a signal-string completion condition (`until`) plus a deterministic shell completion check (`until_bash`), a **required** iteration budget (`max_iterations`), per-iteration session reset (`fresh_context: true`) with the prior iteration's cleaned output bridged forward (`$LOOP_PREV_OUTPUT`), optional per-iteration human gates, and iteration-level events/metrics. Load-time schema validation hardens the same invariants the shell form enforces by convention. Archon ships this as its default PRD-to-PR workflow.

**Ralph and PIV are sibling loop variants.** The plan→implement→verify (PIV) loop drives long-running autonomous implementation through the same core moves — iterated fresh-context passes with per-pass verification and externalized state — but differs in loop topology: Ralph iterates *one item to convergence*, while PIV stages plan→implement→verify *once per unit* of work. Choose Ralph when a single hard item needs repeated passes to converge; choose PIV when work decomposes into units each needing one plan/implement/verify cycle. Both are the same anti-context-rot primitive under different iteration shapes.

## Inputs

- **Spec file (`spec.md`):** A complete, self-contained specification — requirements, acceptance criteria, scope boundaries, definition of done. Detailed enough that an agent reading it cold produces meaningful work.
- **Implementation plan (`plan.md`):** A checklist of discrete tasks derived from the spec. Each task is completable in a single agent pass.
- **Pass/fail criteria:** Explicit, testable conditions determining whether an iteration passes — unit tests, lint, type checks, integration smoke tests, or a deterministic completion check runnable from the shell.
- **Max iteration count:** An integer cap on loop iterations. In the schema-enforced form this is a *required* field, not optional. Prevents runaway execution. Starting value ~10, tuned to ~2x the task count.
- **Fresh-context mechanism:** Headless invocation (`claude -p`) or an engine loop node with `fresh_context: true`. Optionally a bridge (`$LOOP_PREV_OUTPUT`) carrying the prior iteration's cleaned output — nothing more.
- **Working directory / repo context:** The file-system state the agent operates on. Clean and consistent at loop start.

## Outputs

- **Completed implementation:** Code, configuration, migrations, or other artifacts satisfying the spec's acceptance criteria.
- **Updated `plan.md`:** All tasks marked `[x]` with per-task completion notes — the audit trail.
- **Iteration log / engine metrics:** How many iterations ran, which task each addressed, and the pass/fail result at each step. A schema-enforced loop node emits these as first-class iteration events/metrics.
- **Final status:** Pass (all criteria met) or max-iterations-reached (surfaced for human review).

## Steps

1. **Validate the spec and plan before starting.** Read `spec.md` in full. Verify every `plan.md` task maps to a spec requirement. If the spec is ambiguous or incomplete, halt and surface the gaps — errors in the spec cascade across all iterations.

2. **Initialize the loop.** Set iteration counter `i = 1`. Verify the working directory is clean. Write the initial `plan.md` (all tasks unchecked) if absent. Set the max-iteration budget and the completion condition (a signal string and/or a deterministic completion check).

3. **Start iteration `i`: read context fresh.** Launch a fresh-context pass. The agent: (a) reads `spec.md` and `plan.md` in full (plus the bridged prior-iteration output, if any); (b) picks the highest-leverage unchecked task; (c) implements it; (d) writes an unbiased unit test and verifies it passes; (e) marks the task `[x]` in `plan.md`.

4. **Run verification.** After the pass returns, execute the full pass/fail criteria (or the deterministic completion check) from outside the agent context. Record the result.

5. **Check completion condition.** If all tasks are `[x]` AND all pass/fail criteria pass (or the completion check succeeds) → terminate, emit final implementation and log, status: complete.

6. **Check max iterations.** If `i = max_iterations` and completion is not met → terminate, emit current state, remaining tasks, and log, status: max-iterations-reached. Escalate to human review.

7. **Increment and loop.** Set `i = i + 1`. Return to step 3 with a fresh context. Carry no accumulated context from the previous iteration — at most the bridged cleaned output.

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Bad spec cascades errors | Every iteration produces non-converging work | Validate spec in step 1; invest in spec quality proportional to task complexity |
| Model-written tests biased toward passing | Tests confirm agent output rather than spec requirements | Write acceptance tests from the spec before starting; treat agent-written tests as supplementary |
| In-session plugin causes context rot | Context accumulates within a single session | Use the headless `claude -p` form or a `fresh_context: true` loop node — never the in-session plugin |
| No iteration cap set | Runaway loop, unbounded cost | Set `max_iterations` before the loop runs; the schema-enforced form makes this a required field |
| Plan granularity mismatch | Tasks too large for one pass, or too small for progress | Size tasks to a single focused invocation |
| Parallel runs not token-efficient | Multiple concurrent loops multiply token cost super-linearly | Prioritize items; do not treat Ralph as a parallelization primitive |
| Max iteration cap too low | Complex tasks consistently hit the limit | Tune max iterations to ~2x the task count in plan.md |

## Contract

### Preconditions
`spec.md` is complete and unambiguous before the loop starts. `plan.md` exists (or is created in step 2) with a discrete, ordered task list. The working directory is clean — no uncommitted partial work. Pass/fail criteria (tests, lint, or a deterministic completion check) are runnable from the shell without manual intervention. A fresh-context mechanism is available (headless `claude -p`, or a workflow engine that resets the session per iteration and optionally bridges the prior iteration's cleaned output). A maximum-iteration budget is set before the loop runs.

### Invariants
Each iteration runs in fresh context — no unbounded context is inherited from prior iterations; at most the prior iteration's cleaned output is bridged forward. State is externalized exclusively to `spec.md`, `plan.md`, and the file system; the context window carries no unbounded inter-iteration memory. The loop terminates: either the completion condition is met (all tasks pass / deterministic check succeeds) or the max-iteration cap is reached. `plan.md` is updated after each iteration and always reflects what has been completed. Pass/fail criteria are not modified between iterations within a run.

### Governance
Owner: the caller (human or orchestrating agent) who defines `spec.md`, `plan.md`, the pass/fail criteria, and the max-iteration budget. The spec and plan are caller-owned — the looping agent fills in task completions but does not rewrite acceptance criteria or redefine done. The per-iteration log (or the engine's iteration events/metrics) is the primary audit artifact and must be retained alongside the final implementation. Where the loop is declared as a workflow-engine node, its config (completion signal, deterministic check, iteration cap, fresh-context flag, optional per-iteration human gate) is validated at load time.

### Recovery
If the loop hits max iterations without completing: surface the iteration log, current implementation state, and remaining unchecked tasks; do not treat partial completion as a full pass; escalate to human review. If the spec is discovered incorrect mid-loop: halt; correct the spec; restart from the beginning — do not continue from a mid-loop state against a changed spec. If a fresh-context invocation fails (timeout, error): record the failure; do not silently skip the iteration; retry once before escalating. If the loop makes only marginal changes without converging: treat it as an under-specified spec or ambiguous completion check; halt and tighten before resuming.
