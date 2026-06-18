---
title: "Ralph Wiggum Execution Pattern"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "ralph-wiggum-execution-pattern"
extraction_date: "2026-05-25"
last_change_session: 94
last_change_sl: "session-94-codifier-extract-non-pattern-artifacts"
identification_report: "2026-05-24-identification-report-2.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "Complex individual work items that cannot be completed in a single agent pass — database schema migrations, multi-file refactors, multi-step configurations, research-to-implementation pipelines"
    - "Any agent workflow where context accumulation across iterations would push the model into degraded-performance territory (typically above 100k tokens for large models)"
    - "Teams building autonomous coding agents that need a structured iteration primitive with externalized state and deterministic termination"
    - "Orchestration pipelines where a single work item must be driven to completion without human intervention between passes, but with a human-reviewable audit trail"
  platform_coupling: "specific:claude-code"
  autonomy: "autonomous-only"
  stage: "build"
  reversibility: "low — the loop writes to the file system and modifies source code across iterations; each completed task changes the working directory state; reversing requires a clean git checkout before the loop started"
  auditability: "High when plan.md and the iteration log are retained — each iteration's task selection, implementation, and pass/fail result are independently verifiable; low when only the final implementation is kept"
  evidence_strength: "Strong"
  adoption:
    status: "Partially Adopted"
    notes: "Confirmed as a key orchestration pattern in Anthropic's published scientific computing workflow, where it drove a cosmological Boltzmann solver reimplementation over multiple days to sub-percent accuracy. Multiple practitioner sources corroborate the bash claude -p implementation over the in-session plugin variant."
contract:
  preconditions: "spec.md is complete and unambiguous before the loop starts. plan.md exists with a discrete, ordered task list. The working directory is in a clean, known-good state. Pass/fail criteria are runnable from the shell without manual intervention. The execution environment supports spawning headless claude -p invocations."
  invariants: "Each iteration is a fresh headless invocation — no context inherited from prior iterations. State is externalized to spec.md, plan.md, and the file system. The loop terminates: either all tasks pass or the max iteration cap is reached. plan.md is updated after each iteration. Pass/fail criteria are not modified between iterations."
  governance: "Owner: the caller who defines spec.md, plan.md, and the pass/fail criteria. The spec and plan are caller-owned — the looping agent fills in task completions but does not rewrite acceptance criteria. The iteration log is the primary audit artifact."
  recovery: "Max iterations reached without completing: surface iteration log, current state, remaining tasks; escalate to human. Spec discovered incorrect mid-loop: halt, correct spec, restart from beginning. Headless invocation fails: record failure, retry once, escalate on second failure."
tags:
  - "extracted-artifact"
  - "skill"
---

# Ralph Wiggum Execution Pattern

**Source:** [[ralph-wiggum-execution-pattern]]
**Form:** skill
**Extraction date:** 2026-05-25

A depth-first execution skill for complex individual work items. Runs a bash loop that maintains a `plan.md` file tracking progress across iterations. Each iteration starts with a fresh context window via headless `claude -p`, executes a single pass, then tests against pass/fail criteria before looping. The loop continues until the item passes verification or a maximum iteration count is hit.

## Inputs

- **Spec file (`spec.md`):** A complete, self-contained specification of the work item — requirements, acceptance criteria, scope boundaries, and definition of done. Must be detailed enough that an agent reading it cold can produce meaningful work.
- **Implementation plan (`plan.md`):** A checklist of discrete tasks derived from the spec. Each task is a unit of work completable in a single agent pass.
- **Pass/fail criteria:** Explicit, testable conditions that determine whether an iteration's output passes. Typically unit test results, but may include linting, type checks, or integration smoke tests.
- **Max iteration count:** An integer cap on bash loop iterations. Prevents runaway execution. Recommended starting value: 10, tuned to task complexity.
- **Working directory / repo context:** The file system state the agent operates on. Must be clean and consistent at loop start.

## Outputs

- **Completed implementation:** Code, configuration, migrations, or other artifacts that satisfy the spec's acceptance criteria.
- **Updated `plan.md`:** All tasks marked `[x]` with per-task completion notes. Serves as the audit trail.
- **Iteration log:** A record of how many iterations ran, which task was addressed each iteration, and whether pass/fail criteria were met at each step.
- **Final status:** Pass (all criteria met) or max-iterations-reached (criteria not fully met; remaining tasks surfaced for human review).

## Steps

1. **Validate the spec and plan before starting.** Read `spec.md` in full. Verify that every task in `plan.md` maps to a requirement in `spec.md`. If the spec is ambiguous or incomplete, halt and surface the gaps — errors in the spec cascade across all iterations.

2. **Initialize the loop.** Set iteration counter `i = 1`. Verify the working directory is in a clean, known-good state. Write the initial `plan.md` (all tasks unchecked) if it does not already exist.

3. **Start iteration `i`: read context fresh.** Launch a headless Claude invocation (`claude -p`) targeting the current iteration step. The prompt instructs the agent to: (a) read `spec.md` and `plan.md` in full; (b) identify the highest-leverage unchecked task; (c) implement that task; (d) write an unbiased unit test and verify it passes; (e) mark the task `[x]` in `plan.md`.

4. **Run verification.** After the headless invocation returns, execute the full pass/fail criteria from outside the agent context. Record the result in the iteration log.

5. **Check completion condition.** If all tasks in `plan.md` are marked `[x]` AND all pass/fail criteria pass → terminate loop, emit final implementation and iteration log, status: complete.

6. **Check max iterations.** If `i = max iterations` and completion condition is not met → terminate loop, emit current state, remaining unchecked tasks, and iteration log, status: max-iterations-reached. Escalate to human review.

7. **Increment counter and loop.** Set `i = i + 1`. Return to step 3 with a fresh invocation. Do not carry context from the previous iteration.

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Bad spec cascades errors | Every iteration produces non-converging work | Validate spec in step 1; invest in spec quality proportional to task complexity |
| Model-written tests biased toward passing | Tests confirm agent output rather than spec requirements | Write acceptance tests from the spec before starting the loop; treat agent-written tests as supplementary |
| In-session plugin causes context rot | Context accumulates within a single session | Always use bash `claude -p` implementation, not the in-session plugin variant |
| Plan granularity mismatch | Tasks too large for one pass, or too small for meaningful progress | Size tasks to be completable in a single focused invocation |
| Parallel runs not token-efficient | Multiple concurrent loops multiply token cost | Prioritize work items; do not treat Ralph as a parallelization primitive |
| Max iteration cap too low | Complex tasks consistently hit the limit | Tune max iterations to 2x the task count in plan.md |

## Contract

### Preconditions
`spec.md` is complete and unambiguous before the loop starts. `plan.md` exists (or is created in step 2) with a discrete, ordered task list. The working directory is in a clean, known-good state — no uncommitted partial work. Pass/fail criteria (tests, lint, etc.) are runnable from the shell without manual intervention. The execution environment supports spawning headless `claude -p` invocations.

### Invariants
Each iteration is a fresh headless invocation — no context is inherited from prior iterations. State is externalized exclusively to `spec.md`, `plan.md`, and the file system; the context window carries no inter-iteration memory. The loop terminates: either all tasks pass and criteria are met, or the max iteration cap is reached. `plan.md` is updated after each iteration — it is always an accurate reflection of what has been completed. Pass/fail criteria are not modified between iterations within a single run.

### Governance
Owner: the caller (human or orchestrating agent) who defines `spec.md`, `plan.md`, and the pass/fail criteria. The spec and plan are caller-owned — the looping agent fills in task completions but does not rewrite acceptance criteria or redefine done. The iteration log is the primary audit artifact; it must be retained alongside the final implementation.

### Recovery
If the loop hits max iterations without completing: surface the iteration log, the current implementation state, and the list of remaining unchecked tasks; do not treat a partial completion as equivalent to a full pass; escalate to human review. If the spec is discovered to be incorrect mid-loop: halt; correct the spec; restart the loop from the beginning — do not continue from mid-loop state against a changed spec. If a headless invocation fails (timeout, error): record the failure in the iteration log; do not silently skip the iteration; retry once before treating it as a failure and escalating.
