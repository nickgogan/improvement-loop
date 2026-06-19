---
title: "Project-Scoped Coding Workcell"
id: "project-coding-workcell"
type: "schematic"
category: "system-design"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-06-18"
updated: "2026-06-18"
author: "claude"
altitude: "top"
maturity: "seed"
grounded_in:
  - "bmad-method-v6-multi-agent-sdlc"
  - "brainstorming-as-mandatory-design-gate"
  - "acceptance-criteria-as-verifiable-eval-anchor"
  - "confirm-failure-first-tdd-agent-discipline"
  - "builder-validator-chain-pattern"
  - "autonomy-gradient-not-binary-delegation"
  - "compound-review-debt-from-deferred-inspection"
composed_of:
  - "systems/improvement-loop/.claude/skills/design-agent"
  - "systems/improvement-loop/.claude/skills/assess-agent"
  - "systems/improvement-loop/.claude/skills/audit-artifacts"
  - "systems/improvement-loop/knowledge/reference/household-os/architecture/s3-claude-code-build/vault-architecture.md"
source_dd:
  - "DD-107"
tags:
  - "schematic"
  - "coding"
aliases:
  - "Coding Workcell"
  - "Spec-Driven SDLC Workcell"
---

# Project-Scoped Coding Workcell

> A supervised multi-agent SDLC line — discover → spec → plan → build → review — where each phase
> is a gated handoff and no code merges without an independent reviewer that didn't write it.

This schematic captures the **spec-driven multi-agent coding line** the market has converged on
(BMAD, GSD, Archon, and the retired Claude Build's Python/OpenAPI/SOA intent). Unlike the
research-scanner and audit-workcell seeds — which are the engine's *own* operations — this is a
configuration the engine **designs for a consumer** and does not itself run. It exists so the
durable value of the retired Claude Build (an opinionated, spec-first coding harness) survives as a
reusable blueprint rather than as a maintained system.

## Demand

| Axis | Value |
|------|-------|
| **Function** | coding |
| **Scope / lifespan** | project-bound (one workcell per codebase / milestone; phase state is per-project, not standing) |
| **Non-functionals** | data boundary: the project repo + its specs; reliability: high — merged code must be reviewed and tested, not vibe-coded; autonomy need: medium — autonomous within a phase, gated at phase boundaries; cost: scales with phase count and parallel reviewers |

Reach for this when a single owner (or small team) wants an agent system to take a feature from
idea to merged code under a structured SDLC — with design, planning, and shipping decisions gated
by a human — rather than a single agent improvising the whole thing in one context.

## Configuration

### Capability + memory core

A **role-set of specialized agents**, each owning one SDLC phase: an analyst/brainstormer
(requirements + design gate), an architect (tech stack, data models, interfaces), a planner
(decomposition into ordered, atomically-committable tasks), a builder (implements one task at a
time under red/green TDD), and an independent reviewer (audits the builder's output). **Memory is
docs-as-code**: the spec, the architecture doc, and the per-task plan files ARE the source of
truth and the cross-phase memory — sharded so each agent loads only its slice. This artifact-chain
memory is the reusable core; swap the language/stack and the role-set and gate structure stay put.

### Coordination / architecture

**Pipeline of gated phases (relay), with a builder-validator fan-out inside the build phase.** Each
phase consumes the prior phase's artifact and emits its own; a human gate sits on the high-blast
transitions (spec approved? plan approved? ship?). Within the build phase, the builder and reviewer
are **separate agents in separate contexts** — the reviewer never inherits the builder's
rationalizations ([[builder-validator-chain-pattern]]). Fresh context per phase is deliberate
context hygiene, not an accident.

### Autonomy

**collaborator** — the workcell acts alongside the owner, not for them at the load-bearing lines.
It runs each phase autonomously but defers at phase boundaries: design, plan, and ship are
**proposal-first** gates because they are high-blast-radius and not easily reversed
([[autonomy-gradient-not-binary-delegation]]). Within a phase, low-blast reversible actions (write
a task, run a test, draft a doc) are fully autonomous. "Supervised" here means *gated at the seams*,
not *watched at every keystroke*.

### Deployment surface

Claude Code harness, using its subagent primitive for the per-phase roles and the builder/reviewer
split. Runs in-session against a local project repo; no external runtime. The stack the workcell
*builds* (e.g. Python / OpenAPI-first / SOA — Claude Build's opinionated intent) is a parameter of
the schematic, not a constraint of the deployment surface.

## Evaluation & feedback

- **How it's evaluated:** **outcome + independent.** Two anchors: (1) **acceptance criteria** fixed
  at the spec gate are the eval target — work is "done" when it satisfies them, not when the builder
  says so ([[acceptance-criteria-as-verifiable-eval-anchor]]); (2) **red-before-green TDD** — the
  builder must confirm a test fails before implementing, so green means something
  ([[confirm-failure-first-tdd-agent-discipline]]). Neither is graded by the agent that produced the
  code: the reviewer is a separate invocation.
- **Feedback mechanism:** **multi-agent + human.** Multi-agent: the independent reviewer feeds
  defects back to the builder each phase — and reviewing *every* phase rather than deferring is what
  keeps the loop honest, since deferred inspection compounds into unreviewable debt
  ([[compound-review-debt-from-deferred-inspection]]). Human: the owner gates the phase transitions
  and adjudicates scope changes.

## Grounding & composition

- **`grounded_in`** — the evidence:
  - [[bmad-method-v6-multi-agent-sdlc]] — the canonical phased multi-agent SDLC (analyst→PM→
    architect→SM→dev→QA, docs-as-code, scale-adaptive); the shape this schematic generalizes.
  - [[brainstorming-as-mandatory-design-gate]] — an upstream design/brainstorming gate before any
    build; grounds the analyst phase and the first human gate.
  - [[acceptance-criteria-as-verifiable-eval-anchor]] — acceptance criteria as the verifiable eval
    target; grounds the "done = criteria met" evaluation.
  - [[confirm-failure-first-tdd-agent-discipline]] — red-before-green for *coding agents*
    specifically; grounds the build-phase test discipline.
  - [[builder-validator-chain-pattern]] — build and review as separate agents in separate contexts;
    grounds the independent-reviewer split.
  - [[autonomy-gradient-not-binary-delegation]] — autonomy by blast radius / reversibility; grounds
    "autonomous within a phase, proposal-first at phase gates."
  - [[compound-review-debt-from-deferred-inspection]] — deferred review compounds into debt; grounds
    review-every-phase over batch-review-at-end.
- **`composed_of`** — how the engine builds and gates it (this engine designs the workcell; it does
  not operate it):
  - `/design-agent` — author each SDLC role (analyst, architect, planner, builder, reviewer).
  - `/assess-agent` — gate each authored role against IL guides before deployment.
  - `/audit-artifacts` — whole-workcell read once the roles exist (the audit-workcell seed evaluating
    this one).
  - `knowledge/reference/household-os/.../vault-architecture.md` — the lifted Claude Build stack
    intent (Python / OpenAPI-first / SOA) the workcell can be parameterized to build.

## Risk & maturity

- **Known risks / failure modes:** (1) role sprawl — 26-agent frameworks are overkill for a solo
  project; the role-set must scale down (BMAD's "Quick Flow" exists for exactly this); (2)
  cross-phase context loss — fresh-context-per-phase saves tokens but drops insights unless the
  docs-as-code artifacts carry them faithfully; (3) docs-as-code drift — the spec/plan stop matching
  the code if discipline slips.
- **Maturity:** seed — grounded in production frameworks and the engine's own retired-harness intent,
  but **not instantiated**: no role-set has been authored via `/design-agent` and run end-to-end.
  This is a captured blueprint, not yet an exercised one. `composed_of` is the *construction path*,
  not a running system.
- **Revisit when:** a consumer actually asks the engine to stand one up (instantiate via
  `/design-agent` and validate), or any `grounded_in` finding moves (re-check the eval/feedback and
  autonomy layers).
