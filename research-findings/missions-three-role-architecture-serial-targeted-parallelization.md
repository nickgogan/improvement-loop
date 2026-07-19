---
name: 'Missions — Three-Role Architecture (Orchestrator/Workers/Validators) with Serial-Targeted-Parallelization'
summary: |-
  Factory's production multi-day agent system, composing four of five communication
  patterns (see five-pattern-multi-agent-communication-taxonomy.md) into three fixed
  roles: orchestrator (scopes the goal, produces a plan plus a validation contract),
  workers (clean context per feature, commit via git, hand off clean to the next worker),
  validators (verify behavior, not just code shape). Key execution claim: naive N-way
  parallelism was tried and rejected — agents "conflict, step on each other's changes,
  duplicate work, make inconsistent architectural decisions." Missions instead runs
  features serially (one worker or validator active at a time) with parallelization
  targeted only at read-only operations. Production numbers: 16-day longest mission (30
  believed achievable), 60% of time/tokens on implementation, ~50% of final LOC as tests
  at ~90% coverage, team economics moving from ~10 to ~30 concurrent workstreams per 5
  engineers. Orchestration logic lives in ~700 lines of prompts and skills, not a
  hardcoded state machine — a deliberate bitter-lesson-resistant design choice.
implementation_notes: |-
  Not a near-term IL adoption target (the engine doesn't run multi-day autonomous
  missions), but the serial-with-targeted-parallelization prescription is directly
  checkable against any future IL parallel-subagent design — before proposing N-way
  fan-out for a new skill, check whether the task is read-only/independent (parallelize)
  or interdependent (serialize), per this finding and
  legitimate-multi-agent-domains-taxonomy.md.
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- Improvement Loop
- General
adopted_in: []
sources:
- multi-agent-architecture-that-actually-ships.md
related_findings:
- file: five-pattern-multi-agent-communication-taxonomy.md
  rel: enabled-by
- file: harness-engineering-third-evolution.md
  rel: same-problem
- file: specialized-harness-engineering-deterministic-rail.md
  rel: same-problem
- file: l-d-hypothesis-information-loss-across-agent-bound.md
  rel: same-problem
- file: legitimate-multi-agent-domains-taxonomy.md
  rel: same-problem
- file: dark-factory-ai-only-codebase-management.md
  rel: same-problem
- file: pre-code-validation-contracts-dual-blind-validators.md
  rel: enables
- file: structured-handoff-schema-self-healing-multi-agent-missions.md
  rel: enables
proposals: null
date_discovered: '2026-07-18'
last_updated: '2026-07-18'
pipeline_status: "synthesized"
consumed_by:
  - "agent-architecture-decisions.md"
---

## What It Is

A named production system ("Missions," Factory) combining four of the five taxonomy
patterns (five-pattern-multi-agent-communication-taxonomy.md) into a workflow that runs
for hours to days on one described goal. Three fixed roles: **orchestrator** (scopes the
goal through conversation, produces a plan with features and milestones plus a
validation contract — see pre-code-validation-contracts-dual-blind-validators.md);
**workers** (each gets a clean context per feature — "no accumulated baggage, no
degraded attention" — implements, commits via git, hands off to the next worker on a
clean slate); **validators** (verify behavior, not just code shape — see the companion
finding for detail). The key execution-strategy claim: naive N-way parallelism (10 agents
running concurrently) was tried and rejected — agents "conflict, step on each other's
changes, duplicate work, make inconsistent architectural decisions," and coordination
overhead ate the speed gain while still burning tokens. Missions instead runs **features
serially** (exactly one worker or validator active at any point) with **targeted internal
parallelization** limited to read-only operations (searching the codebase, researching
APIs, running parallel code-review passes within a validator) — slower on paper, but the
error-rate drop compounds favorably over multi-day runs. Production numbers: 60% of
wall-clock time and 60% of tokens spent on implementation; final codebases run roughly
50% tests by line count at roughly 90% coverage; the longest completed mission ran 16
days, with 30 days believed achievable; team economics reported as moving from roughly 10
concurrent workstreams to roughly 30, for the same 5-engineer team. A stated design
commitment for durability against model churn: orchestration logic (how to decompose
features, handle failures, alter execution strategy) lives almost entirely in about 700
lines of prompts and skills, not a hardcoded state machine — deliberately structured so
each new model generation improves the system rather than obsoleting the harness around
it (the "bitter lesson" named explicitly).

## Why It Matters

This is independent, cross-vendor corroboration of the KB's L>D hypothesis and
legitimate-multi-agent-domains-taxonomy.md from a production system built without
apparent reference to that framing — Factory re-derived "naive parallelism fails on
interdependent work" empirically and landed on the same prescription (serialize the
sequential/context-dependent parts, parallelize only the genuinely independent,
lossy-tolerant parts: search, research, read-only review). It also supplies a concrete
answer to a design question the KB's harness-engineering findings raise but don't
resolve: how do you keep a harness from being obsoleted by the next model release. "Put
the intelligence in the model, the discipline in prompts/skills, keep the hardcoded layer
thin and deterministic" is a specific, testable answer, not just an aspiration.

## Why People Are Using It

Production account with quantified adoption inside Factory's enterprise customer base
(prototyping overnight, running large refactors/migrations, codebase modernization) — the
numbers above are presented as measured outcomes, not projections, though they come from
a single vendor with an obvious incentive to present its own product favorably.

## Potential Alternatives

- **Naive N-way parallel agent fleets:** the alternative explicitly tried and rejected by
  this same team; the KB's L>D and legitimate-multi-agent-domains-taxonomy.md findings
  predict exactly this failure mode for implementation-type work.
- **Single long-running agent session with context compaction** (the OpenAI/Codex
  approach described in harness-engineering-third-evolution.md's update) rather than
  role-decomposed multi-agent: trades clean-context-per-worker for continuity — a
  different bet on where reliability comes from.

## Potential Improvements

- The talk closes with its own open questions worth tracking: further parallelizing
  Missions' own workload, and orchestrating multiple Missions into higher-order
  workflows — both unresolved as of this source.
- A cost/latency breakdown of the read-only-parallelization carve-out (search, research,
  parallel code review) would clarify how much of the serial system's slowness that
  carve-out actually recovers.

## Potential Failure Modes

- **Unaudited vendor numbers:** the 16-day/30-day and workstream-economics figures are
  self-reported from a single production system, not independently audited — treat as a
  strong existence proof, not a benchmark others should expect to replicate without the
  same validation-contract and handoff-schema infrastructure underneath it.
- **Lost accumulated context:** clean-context-per-worker trades away exactly the kind of
  accumulated task-specific learning a longer-running single session builds up — for
  tasks where that accumulated context matters more than freshness, this architecture may
  underperform a simpler approach.
- **Prompt-encoded orchestration is still a maintenance surface:** the "~700 lines of
  prompts and skills, thin deterministic layer" design is a bet, not a guarantee —
  bitter-lesson-resistance doesn't prevent 700 lines of prompt-encoded logic from rotting
  or drifting the way any other large prompt can.
