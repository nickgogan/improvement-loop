---
name: 'Archon: YAML-Defined Harness Workflow DAGs'
summary: Archon is an open-source harness builder that encodes software development workflows as YAML-defined DAGs of nodes. Each node is either an agentic prompt sent to a coding agent session or a deterministic
  command. Supports parallel execution, node-level model selection, human approval gates, and skill/MCP injection per node.
implementation_notes: 'The hybrid deterministic+agentic node approach and per-node model selection are the key patterns. Evidence: Stripe Minion ships 1,300 AI PRs/week using similar harness; PR acceptance
  rate jumps from 6.7% (raw) to ~70% (harnessed).'
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- archon-open-source-harness-builder.md
related_findings:
- file: bmad-method-v6-multi-agent-sdlc.md
  rel: same-problem
- file: durable-workflow-engine-for-agent-systems.md
  rel: same-problem
- file: gsd-get-shit-done-plugin.md
  rel: same-problem
- file: multi-framework-orchestration-power-stack.md
  rel: same-problem
- file: orchestrated-competition-n-sub-agents-solve-same.md
  rel: same-problem
- file: orchestrated-execution-one-task-per-sub-agent-wit.md
  rel: same-problem
- file: phase-task-hierarchical-plan-decomposition.md
  rel: same-problem
- file: planner-executor-deterministic-guardrails.md
  rel: same-problem
- file: specialized-harness-engineering-deterministic-rail.md
  rel: same-problem
- file: superpowers-plugin-spec-driven-sub-agent-orchestra.md
  rel: same-problem
- file: bmad-v6-builder-custom-agent-workflow-creation.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-19'
pipeline_status: synthesized
consumed_by:
- agent-workflow-and-execution.md
---

## What It Is
Archon (open-source, by the creator of the previous Archon AI command center) sits above coding agents and orchestrates multiple sessions into repeatable workflows. Workflows are YAML files defining a DAG of nodes. Node types: (1) Agentic — a prompt sent into a Claude Code or Codex session. (2) Deterministic — a bash command or script that always runs the same way. (3) Human gate — pauses for approval. Key features: per-node model selection (Haiku for classification, Sonnet for implementation, Opus for planning), separate context windows per node (preventing context rot), parallel workflow execution (6+ simultaneous issue fixes demonstrated), web UI for monitoring, and a skill for invoking workflows from within Claude Code. Ships with default workflows: fix GitHub issue, create PRD, PR review, Ralph loop, adversarial dev. Supporting evidence: 40% of Claude Code's codebase is harness code. Stripe Minion ships 1,300 AI-only PRs/week via harness. Raw AI PR acceptance: 6.7%; harnessed: ~70%.

## Why It Matters
Harness engineering represents the third evolution: prompt engineering → context engineering → harness engineering. Single-agent prompting has a ceiling. Harnesses break through by chaining multiple focused sessions with deterministic validation between them.

## Why People Are Using It
Practitioners report going from "AI shepherding" (manually kicking off skills/commands in sequence) to "define once, run forever" workflows. The parallel execution capability (fixing 6 GitHub issues simultaneously) is a multiplier.

## Potential Alternatives
- GSD (Get Shit Done) plugin — phase-based orchestration, more opinionated
- BMAD Method — multi-agent SDLC framework
- Custom harness scripts (shell scripts chaining Claude Code sessions)
- Anthropic's agent teams (native, but experimental and expensive)

## Potential Improvements
- Visual workflow builder (N8N-like interface — explicitly on the Archon roadmap)
- Cross-workflow state sharing for dependent tasks
- Auto-workflow generation from git history patterns

## Potential Failure Modes
- Token cost amplification — each node is a full session, complex workflows burn many tokens
- Workflow rigidity — YAML-defined steps may not adapt well to unexpected intermediate states
- Model mismatch — using Haiku for a node that needs Sonnet-level reasoning silently degrades output
