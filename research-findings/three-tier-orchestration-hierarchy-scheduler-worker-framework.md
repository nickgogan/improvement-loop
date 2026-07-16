---
name: 'Three-Tier Orchestration Hierarchy: Scheduler, Worker, Framework'
summary: 'A layered orchestration architecture with three distinct tiers: (1) a scheduler/loop tier that manages the phase queue and dispatch logic, (2) a worker tier of headless sessions that each execute
  one phase with a fresh context, and (3) a framework tier where specific tools (Superpowers for TDD, gstack for decisions) run inside each worker. Each tier has a different context scope and lifetime,
  creating strict isolation between dispatch logic, execution work, and framework-specific behavior.'
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- gstack-gsd-superpowers-orchestrator-headless.md
related_findings:
- file: orchestrator-headless-dispatch-context-isolation.md
  rel: extends
- file: five-layer-recursive-ai-loop-architecture.md
  rel: same-problem
- file: skill-phase-pipeline-shared-session-orchestrator.md
  rel: contradicts
- file: teach-orchestrator-to-delegate-pattern.md
  rel: extends
- file: execution-topology-as-runtime-selection.md
  rel: same-problem
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
tags:
- session-95-reextract
---

# Three-Tier Orchestration Hierarchy: Scheduler, Worker, Framework

## What It Is

A layered architecture for autonomous multi-phase builds with three distinct tiers, each with different context scope, lifetime, and responsibilities:

### Tier 1: Scheduler (Build Loop / Route Loop)
- **Scope:** Phase queue and dispatch logic only
- **Lifetime:** Entire project duration (hours to overnight)
- **Context load:** <10% -- only reads state file, dispatches, ingests summaries
- **Responsibility:** "What's next?" -- read state file, find next incomplete phase, dispatch it, wait, mark complete, loop

### Tier 2: Worker (Headless Sessions)
- **Scope:** One phase of execution
- **Lifetime:** Minutes to hours per phase
- **Context load:** Full fresh context per phase -- can use up to 50% without concern
- **Responsibility:** "Do this phase" -- receive phase prompt, execute it using whatever tools/skills are needed, produce summary, exit

### Tier 3: Framework (Superpowers, gstack, etc.)
- **Scope:** Specific execution concerns within a phase
- **Lifetime:** Invoked and completed within a single worker session
- **Context load:** Shares the worker's context budget
- **Responsibility:** "How to do this step" -- Superpowers provides TDD discipline, gstack provides role-based decision-making

The three tiers map to different concerns:
- Tier 1 = **What** (which phase, which order)
- Tier 2 = **Do** (execute this one phase)
- Tier 3 = **How** (with what methodology)

The critical design constraint: information flows DOWN (scheduler tells worker what to do, worker invokes framework) but only SUMMARIES flow UP (framework results feed into worker output, worker summary feeds into scheduler state). This asymmetric information flow is what keeps the upper tiers lean.

## Why It Matters

Most orchestration patterns operate at only two levels (orchestrator + worker, or orchestrator + framework). The three-tier model separates concerns that are commonly conflated:

- **Scheduler vs Worker separation** prevents the scheduler from accumulating execution context. This is the core insight from the headless dispatch pattern -- but the three-tier model makes it architecturally explicit.
- **Worker vs Framework separation** means the worker can use different frameworks for different phases. Phase 1 might use gstack for planning, Phase 2 might use Superpowers for TDD, Phase 3 might use raw Claude Code. The worker session is framework-agnostic; frameworks are pluggable.

For MetaSystem, this maps to a potential architecture for `/gsd-autonomous`: Tier 1 is the GSD skill orchestrator, Tier 2 is headless session per phase, Tier 3 is the specific discuss/plan/execute skills invoked within each session. Currently GSD runs all tiers in a single session, which works but accumulates context.

## Why People Are Using It

Demonstrated in the composite GStack + GSD + Superpowers workflow (Eric Tech). The three tiers were visible in the live demo: the orchestrator session (Tier 1) dispatched headless sessions (Tier 2) that invoked Superpowers and gstack (Tier 3). The 16-phase overnight completion with <10% orchestrator context is the empirical evidence that the tier separation works.

## Potential Improvements

- Formalize the tier boundaries as contracts: what information can flow up/down at each boundary, in what format
- Allow Tier 1 to dynamically adjust the phase queue based on Tier 2 summaries (e.g., insert a remediation phase if a prior phase partially failed)
- Enable Tier 3 framework selection per phase (the scheduler declares which framework each worker should use, not the worker)
- Add a fourth tier for human oversight that monitors Tier 1 and can pause/redirect without entering the execution context

## Potential Failure Modes

- **Tier boundary leakage.** If a worker session starts performing scheduling logic (deciding what to execute next) or the scheduler starts doing execution work (reading code, making design decisions), the context isolation breaks down.
- **Over-layering.** Three tiers add latency and complexity. For simple 2-3 phase projects, the overhead of maintaining three tiers likely exceeds the benefit.
- **Framework incompatibility.** Not all frameworks compose well within a headless worker session. A framework that expects interactive human input (brainstorm approval) cannot run in an unattended headless session without adaptation.
- **Debug complexity.** When something goes wrong, the developer must trace across three tiers to find the root cause. Tier 1 logs show dispatches, Tier 2 logs show execution, Tier 3 logs show framework behavior -- correlating across tiers requires tooling.
