---
name: "Loop-Node Anatomy — Schema-Enforced Ralph Loop as an Engine Primitive"
summary: |-
  Plain English: if you're going to run an agent in a loop, the loop itself needs a
  complete, checkable spec — not a prompt idiom. Archon v0.5.0 ships the most complete
  production loop-anatomy schema in the watched set: a `loop:` node whose config covers
  every element of a safe agent loop — completion signal (`until:` string matched in AI
  output), deterministic check (`until_bash:` script, exit 0 = done), hard budget
  (`max_iterations`, required; `retry` explicitly rejected on loop nodes), context
  policy (`fresh_context: true` per-iteration session reset with `$LOOP_PREV_OUTPUT`
  bridging the prior iteration's cleaned output across), per-iteration human gates
  (`interactive: true` + `gate_message`, feedback injected via `$LOOP_USER_INPUT`),
  observability (`loop_iteration_started/completed/failed` events, `loopIterations` in
  run metrics), and pause/resume semantics (iteration counter + session id persisted).
  Maps directly onto the 11.A Loop Engineering init → iterate → evaluate → exit framing.
implementation_notes: |-
  If the engine ever designs a loop skill or Ralph-style autonomous session harness,
  this is the reference checklist of loop-config elements: signal AND deterministic
  completion checks, a required iteration budget, an explicit per-iteration context
  policy, an optional per-iteration human gate, and iteration-level observability.
  Schema-level rejection of retry-on-loop ("the loop manages its own iteration") is a
  design invariant worth carrying over.
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "ralph-wiggum-execution-pattern.md"
    rel: "extends"
  - file: "stop-rules-as-execution-boundaries.md"
    rel: "extends"
  - file: "archon-yaml-defined-harness-workflows.md"
    rel: "extends"
  - file: "incremental-one-feature-per-session-pattern.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "orchestration"
  - "loop-engineering"
  - "ralph-loop"
  - "archon"
---

# Loop-Node Anatomy — Schema-Enforced Ralph Loop as an Engine Primitive

## What It Is

Archon v0.5.0 promotes the Ralph loop from a prompt/bash idiom to a first-class, schema-enforced workflow-engine primitive. A `loop:` node's configuration is a complete loop-anatomy spec:

| Element | Mechanism |
|---------|-----------|
| Completion signal | `until:` string matched in AI output (e.g. `<promise>COMPLETE</promise>`) |
| Deterministic check | `until_bash:` optional script run after each iteration; exit 0 = complete |
| Budget | `max_iterations` (required); exceeding it fails the node; `retry` is explicitly rejected on loop nodes by schema validation |
| Context policy | `fresh_context: true` starts a new session per iteration; `$LOOP_PREV_OUTPUT` bridges the previous iteration's cleaned output into the fresh session |
| Human-in-loop | `interactive: true` + `gate_message` pauses every iteration for `/workflow approve`; `$LOOP_USER_INPUT` carries the human's feedback into the resumed iteration |
| Observability | `loop_iteration_started/completed/failed` events; `loopIterations` plus summed token/cost totals in run metrics; `interactive_loop` pause type distinct from one-shot `approval` |
| Resume semantics | A paused loop persists its iteration counter and session id; resume continues at iteration N+1 |

Schema enforcement (Zod `superRefine`) rejects invalid combinations at load time — e.g. retry-on-loop, or `interactive` without `gate_message`. Key files: `packages/workflows/src/schemas/loop.ts`, `dag-executor.ts`, `event-emitter.ts`.

## Why It Matters

Ralph-style loops are usually assembled ad hoc — a bash `while` around a headless agent call, a magic completion string, and hope. Each ad-hoc assembly re-decides (or forgets) the same questions: how does the loop know it's done, what stops it from running forever, does each iteration see the last one's context, can a human intervene mid-loop, and can anyone see what iteration N did. Archon's loop node answers all of them in one declarative config, and makes the dangerous omissions (no budget) unrepresentable. It is the most complete production loop-anatomy spec observed in the watched-library set, and it maps one-to-one onto the KB's 11.A Loop Engineering framing (init → iterate → evaluate → exit).

Two details are independently valuable: (1) pairing a *signal-string* check with an optional *deterministic bash* check acknowledges that "the model says it's done" and "the tests pass" are different facts; (2) `fresh_context` + `$LOOP_PREV_OUTPUT` codifies the fresh-context-with-explicit-carryover policy that Ralph practitioners converged on informally.

## Why People Are Using It

Observed in [Archon](https://github.com/coleam00/archon) v0.5.0 — see [[archon-analysis]] for structural details. The loop node is exercised by shipped default workflows: `archon-ralph-dag.yaml` (28k, a full PRD-driven fresh-context implementation loop), `archon-piv-loop.yaml`, and `archon-test-loop-dag.yaml` (a minimal loop exemplar). Loop progress is surfaced in the run-monitoring console UI rather than being opaque.

## Potential Alternatives

Ad-hoc bash loops around headless agent invocations (the original Ralph idiom); harness-level stop hooks; durable workflow engines (Temporal-style) where iteration is a workflow-level retry concern rather than a declared node type.

## Potential Improvements

Loop-level cost budgets (`maxBudgetUsd` exists per node; a per-loop cumulative ceiling is the natural extension). Adaptive iteration budgets based on progress signals. Divergence detection (iteration N output similarity to N-1) as an additional exit trigger.

## Potential Failure Modes

Signal-string matching is spoofable — a model can emit the completion token without the work being done (mitigated by `until_bash` but only when authors use it). `$LOOP_PREV_OUTPUT` bridging reintroduces cross-iteration contamination if the "cleaned" output carries hallucinated state. Interactive loops turn a human into a per-iteration blocker — the gate that makes the loop safe also caps its autonomy.
