---
term: agentic-systems
type: concept
variants: []
target_system:
  - "improvement-loop"
created: "2026-04-22"
updated: "2026-04-22"
author: "claude"
stage: "draft"
tags:
  - "librarian-concept"
  - "agentic-systems"
  - "multi-agent"
  - "orchestration"
aliases:
  - "Agentic system"
  - "Multi-agent system"
  - "Agent orchestration"
  - "Agent topology"
---

# Agentic Systems

## Short definition

An **agentic system** is a topology of multiple agents plus shared state — orchestrators, sub-agents, workers, reviewers — coordinating over a task that no single agent handles end-to-end. The term names the *system level*, not the agent level: an agentic system has multiple agent roles, message/state channels between them, and usually an orchestration mechanism (DAG, BSP, supervisor, queue).

Single referent. No variants. The specific topologies (single-agent vs multi-agent; DAG vs BSP; supervisor vs swarm; orchestrator-worker vs orchestrated-competition) are *design choices within* the agentic-system concept, not variants of it. Those choices route through `decide` (planned) or `design` operations, not through variant selection here.

## Not to be confused with

| Not agentic system | What it is instead |
|---|---|
| **Agent** | A single unit within an agentic system. One agent is not an agentic system. See `agent.md`. |
| **Harness** | The runtime substrate. Multiple agents in one harness is a *harness configuration*, not necessarily an agentic system — the system exists when the agents *coordinate*. See `harness.md`. |
| **Workflow** | A procedural composition of steps. A workflow can be single-agent (one agent runs the whole workflow) — that's *not* an agentic system. G3b §Contract distinguishes workflow mechanics from multi-agent mechanics. |
| **Second brain** | A shared knowledge surface. Multiple agents sharing a brain is a *memory topology*, which an agentic system may have, but shared memory alone is not the system. See `second-brain.md`. |

## Why this is a concept, not a dimension

Like `harness.md`, agentic-systems is a *consumer lens* that cross-cuts multiple dimensions — any real question about an agentic system touches architecture (G3), workflow (G3b), context (G2a/G2b), tool design (G5), safety (G6), memory (G7), and governance (G9) at once. Scan-topic framing would partition-overlap existing dimensions. Consumer-query framing is the right place: this file points into the aspects already scanned.

## Architecture baseline — single-agent is the default

G3 `agent-architecture-decisions.md` §Key Concepts and §Procedure §Step 2 carry load-bearing invariants the Librarian must surface whenever agentic-system design is in scope:

1. **Single agent is the default (L > D).** Information loss across agent boundaries typically exceeds context degradation within a single agent. Multi-agent swarms degrade sequential tasks by 39–70% (G3 §Key Concepts §1; `legitimate-multi-agent-domains-taxonomy`).
2. **45% saturation threshold.** Below ~45% baseline single-agent performance, invest in making the single agent better before adding agents (G3 §Key Concepts §2).
3. **Decompose by task characteristics, not roles.** Role-mirroring (engineer / QA / PM) is specialization theater. Decomposition criteria are parallelizability, information-flow dependencies, error sensitivity (G3 §Key Concepts §3).

The Librarian should not produce agentic-system designs without these three invariants in scope — they're the default rubric against which any multi-agent proposal fires.

## Composition

Substrate pointers for the core Librarian operations on agentic systems.

| Aspect | Tier 1 (guides, default) | Tier 2 (patterns / findings) | Tier 3 (watched-libraries) |
|---|---|---|---|
| Single-agent vs multi-agent decision | G3 §Key Concepts §1–3, §Procedure §Step 2 (decision tree), §Pitfalls | `legitimate-multi-agent-domains-taxonomy`, `autonomy-gradient-not-binary-delegation` | — |
| Legitimate multi-agent domains | G3 §Procedure §Step 2, §Templates (Agent Architecture Decision) | `legitimate-multi-agent-domains-taxonomy` (research / debugging / synthesis / monitoring are the four) | — |
| Orchestration mechanics (DAG, BSP, supervisor) | G3 §Key Concepts, §Procedure | `dag-vs-bsp-two-graph-based-orchestration-models`, `effort-scaling-rules-embedded-in-orchestrator`, `issue-based-agent-orchestration-replacing-markdown-plans`, `multi-framework-orchestration-power-stack` | — |
| Model-tier routing (orchestrator vs subagent model selection) | G3.I4 / G8.I4 (task-based model selection, merged invariant) | `model-tier-routing-expensive-orchestrator-cheap-s` | Anthropic model-comparison docs |
| Workflow execution across agents | G3b `agent-workflow-and-execution.md` §Contract, §Procedure, §Pitfalls | `deep-plan-multi-agent-exploration-pattern`, `orchestrated-competition-n-sub-agents-solve-same` | — |
| Multi-agent memory topology | G7 §Part 1 (tiered memory) + `memory.md` concept | `agent-memory-architecture-multi-agent-layered`, `multi-agent-proportional-content-summarization` | — |
| HITL governance across agents | G9 `agent-governance-and-trust.md` §Contract, §Section 1 (autonomy tiers), §Section 4 (governance infrastructure) | Patterns on HITL gating, trust promotion, audit trails | — |
| System-level framing | — | `five-pillar-agentic-os-framework`, `agentic-speculation-four-characteristics-data-system-redesign`, `agentic-infrastructure-pilot-to-production`, `bmad-method-v6-multi-agent-sdlc` | — |

## Librarian read rule

**Default (Tier 1).** Start with G3 §Key Concepts §1–3 unconditionally — the "single-agent is default" triad is load-bearing for any agentic-system query. Then route by aspect: decomposition → G3 §Procedure §Step 2; workflow mechanics → G3b; safety across agents → G6 + G9; memory across agents → G7 + `memory.md`.

**Escalate to Tier 2 when:**
- Consumer is designing a new multi-agent topology — surface `legitimate-multi-agent-domains-taxonomy` *before* any design step runs (it's a precondition check: does the consumer's task fit a legitimate domain?).
- Consumer is comparing orchestration mechanics (DAG vs BSP) — `dag-vs-bsp-two-graph-based-orchestration-models` carries the tradeoff directly.
- Consumer asks about cost / latency tradeoffs in multi-agent — `model-tier-routing-expensive-orchestrator-cheap-s` is canonical.

**Escalate to Tier 3 when:**
- Consumer is comparing their design against a canonical framework (BMad, LangGraph, CrewAI, Autogen) — Tier 3 for the reference repo.

**Do not:**
- Produce a multi-agent design without first surfacing the "single-agent is default" invariants. Consumer should see the default *before* the alternative.
- Conflate "agents using tools" (single-agent system) with "multiple agents coordinating" (agentic system). The distinction is load-bearing.
- Assume role-mirroring decomposition is valid. G3 §Key Concept 3 rules it out; patterns agree.

## Provenance surfacing

Tier-1 citations: `<guide>.md#<anchor>` with line-range appendix until the section manifest lands. Tier-2 citations: finding file path + slug. Tier-3 citations: `watched-lib/<path>:<line-range>`. When the Librarian surfaces the single-agent-default invariants, cite *both* G3 and the corroborating pattern(s) — these are load-bearing enough that one citation is thin.

## Cross-references

- Related concepts: `agent.md` (the unit), `harness.md` (the runtime), `memory.md` (shared state tier), `second-brain.md` (shared knowledge tier).
- Related operations: `audit.md`, `design.md`, `coverage.md` (UC-8.2 "which guides discuss multi-agent orchestration"), `decide.md` (planned — single vs multi-agent is canonical decide query).
- Use-case registry (UC-3.6 audit agentic-system; UC-8.2 coverage multi-agent orchestration): `operations/references/librarian/use-case-registry.md`.
- Governing DDs: DD-78 (Contract triple-role), DD-82 (IL 4-agent architecture — the IL itself is an agentic system).
