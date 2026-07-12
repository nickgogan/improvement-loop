---
name: Orchestrator-Delegates-to-Headless-Sessions for Context Isolation
summary: A thin orchestrator session dispatches each phase as a separate claude -p headless subprocess. Each headless session gets a fresh context window, executes one phase, reports a summary, and exits.
  The orchestrator never accumulates work context — only coordination state — staying at <10% context utilization after 100+ headless sessions. Demonstrated on a 16-phase project completed overnight autonomously.
implementation_notes: MetaSystem already uses subagent isolation (DD-82 agent-as-directory pattern). This finding adds the specific mechanism of process-level isolation via claude -p for context management
  — each phase runs in a fresh process, not just a fresh agent context within the same process. The phase-queue state file format is the key design artifact.
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- gstack-gsd-superpowers-orchestrator-headless.md
proposals: null
date_discovered: '2026-05-24'
last_updated: '2026-07-12'
related_findings:
- file: claude-p-headless-mode-as-openclaw-replacement.md
  rel: extends
- file: sub-agent-context-isolation-for-parallel-complex.md
  rel: same-problem
- file: teach-orchestrator-to-delegate-pattern.md
  rel: extends
- file: distribution-as-floor-raising-one-click-skill-buttons.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- defending-agent-context.md
- skills/build-loop-skill-autonomous-phase-driver.md
tags:
- context-engineering
- orchestration
- claude-code
---

# Orchestrator-Delegates-to-Headless-Sessions for Context Isolation

## What It Is

An orchestration pattern where a thin orchestrator session maintains a phase-queue state file and dispatches each phase as a separate `claude -p` headless subprocess. Each headless session gets a fresh context window, executes one phase against the full codebase, reports a summary, and exits cleanly. The orchestrator reads completion status and dispatches the next incomplete phase.

## Why It Matters

Context rot is the primary failure mode for long-running autonomous workflows. This pattern solves it at the process level: the orchestrator never accumulates work context, only coordination state. After delegating 100+ sessions, it stays under 10% context utilization. Each headless session independently has the full context budget for its phase.

## How It Could Fail

Phase prompts must be self-contained — the headless session has no access to the orchestrator's conversation history. Complex inter-phase dependencies require explicit state passing through files. The pattern trades context isolation for handoff overhead.
