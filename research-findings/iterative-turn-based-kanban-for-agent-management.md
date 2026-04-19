---
name: "Iterative Turn-Based Kanban for Agent Management"
summary: "A kanban variant with two columns -- Your Turn and Claude's Turn -- reflecting the iterative, non-sequential nature of agent conversations. Tasks bounce between columns as feedback loops iterate, replacing the traditional linear kanban (Not Started -> In Progress -> Review -> Done)."
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: "P3 (Monitor)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "stop-using-claude-code-in-terminal.md"
date_discovered: "2026-04-07"
last_updated: "2026-04-07"
pipeline_status: "raw"
consumed_by: []
---

## What It Is

A kanban board design specifically adapted for human-agent collaboration workflows. Instead of the traditional linear kanban flow (Not Started -> In Progress -> Review -> Done), the board has two primary columns: "Your Turn" (items awaiting human review/feedback) and "Claude's Turn" (items the agent is actively working on). Tasks move back and forth between columns as the iterative feedback loop progresses. Documented by Simon Scrapes as part of a custom command center.

The key insight is that agent workflows are fundamentally iterative, not sequential. A task may bounce between human and agent three or four times before completion. Traditional kanban boards with linear stage progression misrepresent this interaction pattern and create false expectations about workflow linearity.

## Why It Matters

Current agent management tools (tmux, Vibe Kanban, Claude Desktop) all assume either linear progression or a single conversation thread. Neither captures the reality of managing multiple concurrent iterative loops. The turn-based model gives the human operator a single glance view of "what needs my attention now" across all active tasks -- reducing the cognitive overhead of context-switching between terminal windows.

## Why People Are Using It

The pattern addresses the specific bottleneck of managing five or more concurrent agent sessions. The "Your Turn" column acts as a prioritized inbox of agent outputs awaiting review, while "Claude's Turn" represents delegated work the human can ignore until it returns. This maps to how experienced practitioners actually work with agents -- short bursts of feedback followed by delegation.

## Potential Improvements

Could be combined with priority scoring to surface the most important items in "Your Turn" first. Time-in-column metrics could identify tasks that are stuck in feedback loops. Integration with Claude Code's session management could auto-populate columns based on active sessions.

## Potential Failure Modes

Risk of tasks accumulating in "Your Turn" faster than the human can review them -- the same review bottleneck problem identified in the Review Pipeline Bottleneck finding. The iterative model could also mask tasks that should be rejected outright rather than iterated upon endlessly.
