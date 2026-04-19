---
notion_id: 32b1e08b-9b34-815a-b4f8-e0a1c99f6600
name: 'Orchestrated Execution: One Task Per Sub-Agent with Wiring Verification'
summary: Assign exactly one implementation task per sub-agent to maximize output quality, with the orchestrator as the single source of truth, and explicitly verify after each wave that sub-agent outputs
  are wired into the main application (not left as isolated islands).
implementation_notes: null
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- these-3-frameworks-make-claude-code-unstoppable.md
- anthropic-multi-agent-research-system.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-09'
related_findings:
- file: task-contract-pattern-schema-first-agent.md
  rel: enables
- file: planner-executor-deterministic-guardrails.md
  rel: same-problem
- file: archon-yaml-defined-harness-workflows.md
  rel: same-problem
pipeline_status: "raw"
consumed_by: []
---
# Orchestrated Execution: One Task Per Sub-Agent with Wiring Verification

## What It Is
Giving one focused task to one sub-agent produces dramatically better output than having one agent handle many tasks — the sub-agent's fresh context is entirely dedicated to a single problem. The orchestrator maintains the build plan and tracks progress without its own context being burdened by implementation details (those are offloaded to sub-agents). After each wave of sub-agents completes, the developer verifies that each sub-agent's implementation was actually wired into the main application — a critical step because sub-agents frequently complete their building task but fail to integrate their output with the rest of the codebase, leaving 'islands' of unreachable code. The orchestrator's plan and context are the two sources of truth, not any individual sub-agent's session.

## Why It Matters
Isolated code islands are the most common failure pattern in sub-agent orchestration. Without explicit wiring verification after each wave, integration failures accumulate silently and produce a codebase that builds but does not function end-to-end.

## Why People Are Using It
Faster iteration than human-in-loop sequential coding. The ability to build and throw away implementations for learning (since rebuilding with sub-agents takes a fraction of the original time).

## Potential Alternatives
Sequential single-agent implementation with /handoff between phases. Ralph loops for tasks that are fully specced upfront.

## Potential Improvements
Automated wiring tests that verify each new module is reachable from the application's entry point. CI/CD integration that runs connectivity checks after each sub-agent wave.

## Potential Failure Modes
Without human monitoring during sub-agent waves, wiring failures are discovered only after multiple waves have compounded the problem. Sub-agents writing conflicting implementations of shared interfaces.
