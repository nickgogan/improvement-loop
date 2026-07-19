---
title: "Loop Anatomy Spec Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "loop-node-anatomy-schema-enforced-ralph-primitive"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-architecture-decisions.harvest-queue"
identification_report: "agent-architecture-decisions.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams designing an agent that repeats the same task in a loop until some condition is met — an iterative coding agent, a retry-until-done automation, or an autonomous multi-step task runner"
    - "anyone building a workflow or orchestration engine that needs a declared, checkable loop-node type instead of ad hoc scripting"
    - "anyone currently assembling a bash `while` loop around a headless agent call who wants a checklist to avoid missing a safety element"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — the filled template is a planning document; editing or discarding it costs nothing. (The loop implementation it specs may carry its own, separate reversibility profile.)"
  auditability: "high — every field is a plain-text checklist item, so the presence or absence of a completion check, an iteration budget, or a human-gate message is directly verifiable by reading the filled spec, no execution required"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Derived from one production framework's shipped loop-node schema (a workflow engine's `loop:` config), not yet observed as a standalone design artifact in independent use. Treat as extrapolated-but-well-grounded rather than field-proven."
contract:
  preconditions: "Someone is about to design or implement a loop that re-runs an agent (or an agent-driven step) multiple times toward a goal, and wants to fix the loop's safety-relevant decisions before writing the harness code. They have (or can approximate) a mechanism for at least one of: matching a signal string in agent output, or running a deterministic check script after each iteration."
  invariants: "A filled spec always declares a hard iteration budget — no loop is speced as unboundedly retryable. A filled spec always declares at least one completion check (a signal check, a deterministic check, or both); 'the model decides it's done' alone, with no deterministic backstop, is a permitted but flagged-as-weaker configuration. A filled spec always states its per-iteration context policy explicitly — whether context resets each iteration and, if so, exactly what carries over. If a human gate is included, it always carries a gate message; a gate with no message is invalid."
  governance: "Owner: whoever authors the loop-running component (an orchestration engine's node type, a workflow config, or a bespoke script) is responsible for keeping the filled spec in sync with the implementation. Changes to a filled spec that affect the iteration budget, completion checks, or the human-gate policy should go through the same review a change to the loop's actual behavior would — the spec is meant to be load-bearing documentation, not decoration."
  recovery: "If a filled spec has no iteration budget, treat it as incomplete — do not build against it until one is set. If a filled spec relies on a signal check with no deterministic backstop and the loop's output is high-stakes, flag this as a known gap (spoofable completion) and either add a deterministic check or explicitly accept the risk in the spec's notes. If the context policy is left unstated, default to 'ask' rather than guessing — silent context-policy drift between spec and implementation is the most common source of loop bugs."
tags:
  - "extracted-artifact"
  - "template"
  - "loop-engineering"
  - "agent-orchestration"
  - "ralph-loop"
---

# Loop Anatomy Spec Template

**Source:** [[loop-node-anatomy-schema-enforced-ralph-primitive]]
**Form:** template
**Extraction date:** 2026-07-19

A fill-in checklist for specifying an iterative agent loop — the "Ralph loop" shape, generalized — before building it. Answering every variable below produces a complete loop-anatomy spec: how the loop knows it's done, what stops it from running forever, whether each iteration sees the last one's context, whether a human can intervene mid-loop, and whether anyone can see what each iteration did.

## Variables

| Variable | Type | Description |
|---|---|---|
| `{{LOOP_NAME}}` | string | Short name/purpose of this loop — what it's iterating toward. |
| `{{COMPLETION_SIGNAL}}` | string or "none" | The exact marker (e.g. a token or phrase) the agent emits in its output to claim completion. Set to "none" if completion is judged only by the deterministic check. |
| `{{DETERMINISTIC_CHECK}}` | command/script or "none" | A script or command run after each iteration whose exit code (0 = done) is treated as authoritative. Set to "none" only if the signal check alone is an accepted risk (see Contract → Recovery). |
| `{{MAX_ITERATIONS}}` | integer (required) | The hard iteration budget. The loop must fail or halt, not silently retry forever, once this is exceeded. |
| `{{CONTEXT_POLICY}}` | enum: "fresh-per-iteration" \| "accumulating" \| other | Whether each iteration starts from a clean slate or continues in the same context. |
| `{{CARRYOVER_CONTENT}}` | string or "none" | If context resets each iteration, exactly what output or state is deliberately carried forward into the next one. |
| `{{HUMAN_GATE}}` | boolean | Whether a human approval point exists mid-loop (per iteration, or at defined checkpoints). |
| `{{GATE_MESSAGE}}` | string or "n/a" | The message shown to the human at the gate, and what input from them (if any) feeds back into the next iteration. Required if `{{HUMAN_GATE}}` is true. |
| `{{OBSERVABILITY_EVENTS}}` | list | What gets recorded or emitted per iteration (start/complete/fail events, iteration count, cost/token totals, or equivalent). |
| `{{RESUME_STATE}}` | string or "not supported" | What state must be persisted to pause and later resume the loop at the right iteration (e.g. iteration counter, session identifier). |

## Body

```
Loop: {{LOOP_NAME}}

Completion:
  signal check:         {{COMPLETION_SIGNAL}}
  deterministic check:   {{DETERMINISTIC_CHECK}}

Budget:
  max_iterations:        {{MAX_ITERATIONS}}   # required; no retry-forever allowed

Context policy:
  mode:                   {{CONTEXT_POLICY}}
  carryover:              {{CARRYOVER_CONTENT}}

Human-in-loop:
  gate enabled:           {{HUMAN_GATE}}
  gate message:           {{GATE_MESSAGE}}

Observability:
  events/metrics:         {{OBSERVABILITY_EVENTS}}

Resume:
  persisted state:        {{RESUME_STATE}}
```

## Usage

Fill in every variable before writing (or configuring) the loop itself — this is a specify-stage artifact, not a runtime component. Use it as:

- A design checklist when adding a new loop-shaped node to a workflow or orchestration engine.
- A pre-build spec attached to a design decision, so the loop's safety-relevant choices (budget, completion check, context policy) are reviewed before code exists rather than reverse-engineered from it afterward.
- A conversion tool for existing ad hoc loops (a bash `while` around a headless agent call): fill the template against the current implementation to surface silently-missing elements — most commonly a missing `{{MAX_ITERATIONS}}` or an unstated `{{CONTEXT_POLICY}}`.

Render one filled copy per distinct loop. A system with several different loop-shaped components (e.g., a build loop and a review loop) gets one filled spec each — do not merge unrelated loops into a single spec.

## Variation Axis

What changes between renderings:

- **Completion strategy.** Signal-only (cheapest, spoofable) vs. deterministic-only (most reliable, requires a checkable artifact) vs. both (highest confidence — the two checks catch different failure classes).
- **Context policy.** Fresh-per-iteration with explicit carryover (isolates each iteration from prior hallucinated state, but requires deliberate bridging) vs. accumulating context (simpler, but risks compounding drift across iterations).
- **Human involvement.** Fully autonomous (no `{{HUMAN_GATE}}`, fastest, highest risk) vs. gated (a human reviews every iteration or defined checkpoints, slower but bounds the blast radius of a bad iteration).
- **Observability depth.** Minimal (iteration count only) vs. full (per-iteration events, cost/token totals, and persisted resume state) — richer observability costs more instrumentation but makes a stuck or runaway loop diagnosable after the fact.
- **Budget shape.** A flat iteration ceiling (this template's baseline) vs. an added cumulative cost ceiling vs. an adaptive budget driven by a progress signal — all are extensions of the same `{{MAX_ITERATIONS}}` slot, not alternatives to having one.

## Contract

### Preconditions
Someone is about to design or implement a loop that re-runs an agent (or an agent-driven step) multiple times toward a goal, and wants to fix the loop's safety-relevant decisions before writing the harness code. They have (or can approximate) a mechanism for at least one of: matching a signal string in agent output, or running a deterministic check script after each iteration.

### Invariants
A filled spec always declares a hard iteration budget — no loop is speced as unboundedly retryable. A filled spec always declares at least one completion check (a signal check, a deterministic check, or both); "the model decides it's done" alone, with no deterministic backstop, is a permitted but flagged-as-weaker configuration. A filled spec always states its per-iteration context policy explicitly — whether context resets each iteration and, if so, exactly what carries over. If a human gate is included, it always carries a gate message; a gate with no message is invalid.

### Governance
Owner: whoever authors the loop-running component (an orchestration engine's node type, a workflow config, or a bespoke script) is responsible for keeping the filled spec in sync with the implementation. Changes to a filled spec that affect the iteration budget, completion checks, or the human-gate policy should go through the same review a change to the loop's actual behavior would — the spec is meant to be load-bearing documentation, not decoration.

### Recovery
If a filled spec has no iteration budget, treat it as incomplete — do not build against it until one is set. If a filled spec relies on a signal check with no deterministic backstop and the loop's output is high-stakes, flag this as a known gap (spoofable completion) and either add a deterministic check or explicitly accept the risk in the spec's notes. If the context policy is left unstated, default to "ask" rather than guessing — silent context-policy drift between spec and implementation is the most common source of loop bugs.
