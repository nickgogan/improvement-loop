---
name: 'Claude Code Framework Taxonomy: gstack Thinks, GSD Stabilizes, Superpowers Executes'
summary: 'Three popular Claude Code orchestration frameworks are not interchangeable — each solves a different primary problem. gstack (23+ specialist slash commands) enforces role-separated thinking via specialist chaining. GSD (Get Shit Done) enforces context stability by running each phase in a fresh Claude instance with explicit artifact handoff. Superpowers (14 interconnected skills, 7-phase TDD workflow) enforces execution discipline via a mega-orchestrator. The failure mode follows from the architecture: Superpowers'' one-big-brain orchestrator hits context limits on long sessions; GSD''s fresh-session-per-phase pays explicit-handoff tax; gstack''s chain rigidity resists ad-hoc work. They stack cleanly rather than compete.'
implementation_notes: MetaSystem's IL pipeline resembles GSD's "fresh context per phase" topology — agents write findings, later agents read findings, no shared context. This finding is useful as prior art when refining IL's agent handoff protocol or evaluating whether to adopt a specific gstack/Superpowers primitive.
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- pulumi-blog-claude-code-orchestration-frameworks.md
- medium-ewan-mak-superpowers-gsd-gstack.md
related_findings:
- file: multi-framework-orchestration-power-stack.md
  rel: same-problem
- file: gstack-specialist-role-architecture.md
  rel: extends
- file: specialized-harness-engineering-deterministic-rail.md
  rel: same-problem
- file: planning-session-bias-separate-context-windows.md
  rel: enables
- file: gsd-stall-detection-revision-loop-escalation.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-23'
last_updated: '2026-04-23'
pipeline_status: raw
consumed_by: []
---

# Claude Code Framework Taxonomy: gstack Thinks, GSD Stabilizes, Superpowers Executes

## What It Is

Three popular Claude Code orchestration frameworks solve three different primary problems:

- **gstack (Garry Tan's 23+ specialist slash commands)** — "cognitive gearing": force the LLM into distinct named roles (CEO, Eng Manager, Designer, Reviewer, QA, Release Engineer). Each role's output becomes the next role's input. The bet: role-separation reduces context-switching tax and produces higher-quality output than a single generalist turn.
- **GSD (Get Shit Done, @gsd-build)** — fresh Claude per phase. Each phase gets a clean 200K context window. The output of Phase 1 becomes the input to Phase 2; nothing carries over except what is explicitly passed forward. The bet: context stability (not role specialization) is the binding constraint, so wipe and hand off.
- **Superpowers (Jesse Vincent's 14 interconnected skills)** — one mega-orchestrator running a 7-phase TDD workflow (brainstorm → spec → plan → failing-tests → implement-via-subagents → review → finalize). The bet: execution discipline (explicit TDD loop, enforced subagent fan-out for implementation) dominates — so let one brain coordinate the whole job.

The one-line framing from practitioner analyses: **"gstack thinks, GSD stabilizes, Superpowers executes."**

## Why It Matters for Us

Plain English: when teams hit problems with a Claude Code framework, the problem is usually with the wrong framework for the task — not with agents in general. A team doing exploratory product work picks Superpowers (over-engineered for the stage) and gets stuck; a team doing long-horizon structured delivery picks gstack (under-engineered for context hygiene) and drifts. Knowing *which constraint each framework solves* lets you pick the right one, or (more often) stack them: use gstack for specialist thinking inside phases, use GSD to isolate phases from each other, import Superpowers primitives (TDD loop, subagent fan-out) when executing the phase.

For IL: our pipeline is structurally GSD-shaped (phase-per-agent, artifact handoff). Knowing this helps us borrow specific gstack/Superpowers primitives without accidentally inheriting their failure modes.

## Why People Are Using It

Pulumi, Medium practitioners, MindStudio, and DEV Community writers have all published cross-framework comparisons in 2026. No single framework is winning; teams increasingly stack them. The DEV Community post "A Claude Code Skills Stack" explicitly advocates combining all three with role boundaries.

## Potential Alternatives

- Native Claude Code without any framework (default for small jobs)
- BMAD v6 module marketplace (module-based rather than role/phase based)
- Custom per-team harnesses (MetaSystem's own IL is one example)

## Potential Improvements

- A selection rubric that maps project shape (duration, scope, novelty) to the right framework choice
- Compositional guidance: which primitives of each framework are safe to adopt without the rest

## Potential Failure Modes

- **Superpowers — orchestrator context exhaustion**: one big brain coordinating everything works well until the big brain fills up; marathon sessions with dozens of files hit the ceiling
- **GSD — explicit-handoff tax**: every phase boundary requires writing and reading artifacts; expensive for small tasks
- **gstack — chain rigidity**: the role pipeline resists ad-hoc work; free-form exploration doesn't fit the chain
- **Cargo-culting the stack**: teams adopt all three without understanding the constraints each solves, paying all three taxes at once
