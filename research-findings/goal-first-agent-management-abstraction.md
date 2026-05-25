---
name: Goal-First Agent Management Abstraction
summary: Instead of managing terminal sessions or IDE windows, manage business goals. The system determines what sessions to spin up, how many agents, and what planning depth is required. 'Start from the
  top and work downwards.'
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- stop-using-claude-code-in-terminal.md
- agentic-os-five-pillars-claude-code.md
proposals: null
date_discovered: '2026-04-07'
last_updated: "2026-05-25"
related_findings:
- file: agent-architecture-layer-impermanence.md
  rel: same-problem
- file: tiered-interaction-model-quick-ask-vs-supervisor.md
  rel: extends
pipeline_status: raw
consumed_by: []
---

# Goal-First Agent Management Abstraction

## What It Is
An orchestration philosophy that abstracts one layer higher than current tooling. Instead of starting from terminal sessions, IDE windows, or code files and layering project management on top, the system starts from business goals and determines what sessions to spin up, how many agents to allocate, and what planning depth each task requires. Documented by Simon Scrapes as a custom build. Includes a last-two-messages summary view that shows only the tail of agent conversations, an output gallery for visual artifacts, and memory continuity across sessions.

## Why It Matters
Current tools (tmux, Desktop App, Vibe Kanban, Paperclip) all start from the session/code layer and bolt PM on top. This inverts the relationship -- the goal defines the execution plan, not the other way around. Reduces cognitive overhead for the human operator who should be thinking about outcomes, not infrastructure.

## Why People Are Using It
The approach includes iterative turn-based kanban (Your Turn / Claude's Turn), task complexity tiering (Quick / Campaign / Deep Build), multi-client context isolation, and visual skills management. These features address real friction points in multi-agent development workflows where context switching between goals and sessions is the primary bottleneck.

## Potential Improvements
MetaSystem's existing skill and workflow architecture could benefit from a goal-first entry point that determines execution strategy before spinning up agents or sessions.

## Potential Failure Modes
Over-abstraction that hides important implementation details from the user. When the system decides session count and agent allocation autonomously, the human loses visibility into execution mechanics. Debugging becomes harder when you cannot see what the system decided to do and why.
