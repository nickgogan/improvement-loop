---
name: "Execution Topology as Runtime Human Selection"
summary: "The framework offers the human a choice point between execution topologies — sub-agent-per-task (fresh context, human review between tasks) vs inline batch (same session, checkpoints) — at runtime rather than hardcoding one approach. The topology is a configurable parameter, not an architectural constant. This lets the same plan execute via different strategies depending on project shape, risk tolerance, and human availability."
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P2
applicability:
  - "S3 (Claude Code Build)"
sources:
  - "claude-code-plus-superpowers-tutorial.md"
related_findings:
  - file: "superpowers-plugin-spec-driven-sub-agent-orchestra.md"
    rel: "extends"
  - file: "sub-agent-context-isolation-for-parallel-complex.md"
    rel: "same-problem"
  - file: "orchestrator-headless-dispatch-context-isolation.md"
    rel: "same-problem"
  - file: "autonomy-gradient-not-binary-delegation.md"
    rel: "extends"
  - file: "foreground-vs-background-subagent-permission-models.md"
    rel: "same-problem"
adopted_in: []
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - "agent-architecture-decisions.md"
tags:
  - "session-95-reextract"
---

# Execution Topology as Runtime Human Selection

## What It Is

A harness design pattern where the execution topology (how tasks are dispatched and reviewed) is a runtime parameter selected by the human, not an architectural constant baked into the framework. The same implementation plan can be executed via different strategies depending on the situation.

In the observed Superpowers workflow (Eric Tech tutorial, BookZero.ai), after the plan was generated with 11 tasks, the framework offered two options:

**Option 1: Sub-Agent-Driven (recommended)**
- Dispatch a fresh sub-agent per task
- Each sub-agent gets a clean context window with only the task spec
- Human can review between tasks
- Best for: complex tasks where context isolation matters, tasks where the human wants checkpoint review

**Option 2: Inline Batch Execution**
- Execute all tasks within the current session
- Batch execution with checkpoints
- Faster iteration, no sub-agent overhead
- Best for: simpler tasks, when the human trusts the plan, when context from previous tasks helps the next

The human selects the option, and the same plan file is consumed by different execution engines. The plan artifact is topology-agnostic — it does not encode how it will be executed, only what needs to be done.

## Why It Matters

Most frameworks hardcode their execution topology. GSD always resets context per phase. Superpowers historically always dispatched sub-agents. Custom scripts use whatever the author chose. This creates a mismatch when the project shape does not match the framework's assumptions.

The runtime selection pattern solves this by decoupling the plan from its execution strategy. A 3-task plan for a well-understood feature might run inline (fast, low overhead). A 15-task plan for a novel feature might run via sub-agents (isolated, reviewed). Same framework, same plan format, different execution.

This maps to a broader principle: **the plan artifact should be execution-topology-agnostic.** A well-designed plan specifies WHAT (tasks, acceptance criteria, test expectations) but not HOW the execution engine dispatches them. The topology is an orthogonal concern.

For MetaSystem: this is directly relevant to how GSD skills could evolve. Currently `/gsd-execute-phase` uses a fixed wave-based parallelization. If the plan format were topology-agnostic, the same PLAN.md could be consumed by a sub-agent executor, an inline executor, or a parallel wave executor depending on the phase's complexity and the user's preference.

## Why People Are Using It

Demonstrated in Superpowers' execute-plan skill (Eric Tech tutorial). The framework explicitly presented both options with descriptions of when each is appropriate. The recommendation was sub-agent-driven for the 11-task plan, citing fresh context and review between tasks.

The autonomy-gradient finding captures the broader principle that delegation level should be selectable rather than fixed. This finding is a concrete instantiation of that principle applied specifically to execution topology.

## Potential Improvements

- Auto-recommendation based on plan complexity: if <5 tasks and estimated low risk, suggest inline; if >10 tasks or high-risk changes, suggest sub-agent
- Hybrid execution: some tasks inline, some via sub-agent, based on per-task risk assessment
- Topology preview: before executing, show the human what the execution graph will look like under each option (estimated token cost, expected review points, estimated time)
- Post-execution topology feedback: after completion, report whether the selected topology was appropriate (e.g., "sub-agent mode used 4x more tokens than inline would have, but caught 2 cross-task issues that inline would have missed")

## Potential Failure Modes

- **Selection paralysis.** Adding a choice point where none existed adds cognitive load. For most users, the recommendation should be the default with a single confirmation, not an explained tradeoff.
- **Plan assumes topology.** If the plan contains topology-specific instructions ("dispatch this to a sub-agent," "checkpoint after step 3"), it is no longer topology-agnostic and the selection becomes partially illusory.
- **Inline execution inherits context rot.** Choosing inline for a large plan defeats the context-isolation benefit. The framework should warn when inline is selected for plans that will likely exceed context thresholds.
- **Sub-agent overhead for trivial plans.** Dispatching 11 fresh sub-agents for 11 one-line config changes wastes tokens and time. The topology recommendation should account for per-task complexity, not just task count.
