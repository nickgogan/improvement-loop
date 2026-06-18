---
name: "Minimal Agent Harness Skeleton (Three Primitives)"
summary: "A production-grade agent harness reduces to three essential primitives: a loop (model decides, tool runs, result returns, repeat), a tool registry (descriptions for model selection, execution layer for doing), and a memory system (session state + compaction). This skeleton is implementable in a few hundred lines. Hooks, skills, sub-agents, and context loading are additive layers — valuable but not structurally necessary for the core loop to function."
implementation_notes: null
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Already Adopted"
priority: "Not Flagged"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in:
  - "S3 (Claude Code Build)"
sources:
  - "claude-code-architecture-under-the-hood.md"
related_findings:
  - file: "claude-code-12-agent-primitives.md"
    rel: "same-problem"
  - file: "framework-abstraction-tax-for-agents.md"
    rel: "extends"
  - file: "harness-simplification-as-models-improve.md"
    rel: "extends"
  - file: "sdk-vs-framework-decision-for-agent-building.md"
    rel: "same-problem"
  - file: "agent-architecture-layer-impermanence.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
tags:
  - "session-95-reextract"
---

# Minimal Agent Harness Skeleton (Three Primitives)

## What It Is

An observation from the Claude Code clean room reconstruction that a functional agent harness reduces to three structural primitives:

1. **Loop** — The model decides what to do. A tool runs. The result comes back. The model decides the next step. Repeat until done. This is the minimum viable agent — replacing hardcoded logic with model-driven decisions at each step.

2. **Tool registry** — Each tool has a description (so the model knows when to use it) and an execution function (so the system can actually do it). The model handles thinking; the tool layer handles doing. The model never directly touches the file system or runs commands — it makes a request, the tool executes, results come back.

3. **Memory system** — Session state that persists across loop iterations. When conversation history gets too long, a compaction step summarizes what happened and replaces the full history with that summary. Without this, agents fail on tasks spanning more than a few dozen steps.

The claim: "A loop, a tool registry, a memory system, a few hundred lines of Python gets you a working skeleton." The 24-hour TypeScript → Python → Rust clean room rewrite validates this — the architecture reproduced quickly because the core is simple.

**Additive layers** (not structurally necessary for the loop, but present in production):
- **Hooks** — Pre/post tool middleware for safety and observability
- **Context loading** — CLAUDE.md and skills loaded before the first loop iteration
- **Sub-agents** — Parallel delegation via the agent tool

## Why It Matters

This finding complements the "12 agent primitives" and "80% infrastructure" findings by answering the inverse question: what is the **minimum** viable harness? The 12-primitives finding shows what production scale requires. This finding shows what a functional skeleton requires. The gap between them is the additive infrastructure that scales the system but is not part of the core loop.

For harness builders, this establishes a build order:
1. Get the three-primitive skeleton working first
2. Add hooks when you need safety/observability
3. Add context loading when sessions need project awareness
4. Add sub-agents when tasks exceed single-thread complexity

This build order matters because it prevents the framework abstraction tax — teams that start with a heavy framework often don't understand which parts are load-bearing vs. which are optional infrastructure.

## Why People Are Using It

The speed of the clean room rewrite (24 hours, TS → Python → Rust) is the primary evidence. Engineers used AI tools to accelerate the port, but the architecture itself was simple enough that understanding and reimplementing it was tractable in a day. The analyst's framing — "the architecture is not that complicated once you see it laid out" — directly supports the three-primitive characterization.

This also aligns with Anthropic's own recommendation that "the most successful implementations weren't using complex frameworks" but "simple, composable patterns" (framework-abstraction-tax finding). The three primitives are those composable patterns at their most reduced.

## Potential Improvements

- Codify the additive layer build order as a "harness maturity ladder" — each rung adds one layer (hooks → context → sub-agents) with clear criteria for when to add the next.
- Define the minimum interface contract for each primitive (loop needs X, registry needs Y, memory needs Z) so different implementations can be swapped cleanly.

## Potential Failure Modes

- **Under-engineering** — The three-primitive skeleton works for demos and personal tools but fails in production without the additive layers. Teams may mistake the skeleton for the full architecture.
- **Premature simplification** — Removing hooks or context loading to "keep it simple" when the use case actually requires them. The skeleton is a starting point, not a ceiling.
- **Model-dependency** — The claim that "a few hundred lines gets you a working skeleton" depends on the model being capable enough to drive the loop effectively. Weaker models need more harness scaffolding (the harness-simplification finding documents this co-evolution).
