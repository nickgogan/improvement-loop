---
notion_id: 32b1e08b-9b34-81be-9b5e-db592dceca2f
name: 'Trajectory Engineering: Non-Linear Session Forking with /re'
summary: Advanced Claude Code users exploit LLM statelessness to jump back to any prior session state (via /re or double-ESC), fork into parallel trajectories, and trim context to the lean 'trunk' — enabling
  exploration of solution approaches without accumulating context rot from dead ends.
implementation_notes: null
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-code-works-better-when-you-do-this.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: fork-subagent-parallel-trajectory-exploration.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Trajectory Engineering: Non-Linear Session Forking with /re

## What It Is
In Claude Code, pressing double-ESC (or using /re) activates a time-travel feature that returns to any prior point in the current session. Trajectory engineers use this not just to retry failed attempts, but proactively: (1) after a bug fix, they trim out the bug-fixing context (now irrelevant) by rewinding to before the bug was spotted, providing a brief summary of what happened and how it was fixed, then continuing from that clean state; (2) when exploring architectural options, they fork from a common starting point, run each option down its trajectory, compare results, and keep the best; (3) they intentionally keep sessions lean by trimming branches back to the trunk after each exploration. The 'tree' metaphor: trunk = stable reusable context (repo info, current plan), branches = explorations that should be trimmed once evaluated.

## Why It Matters
Context accumulated during problem-solving (debugging attempts, failed approaches, exploratory tangents) is dead weight that degrades future responses. By treating sessions as a directed tree rather than a linear chat, practitioners eliminate this dead weight while retaining all learnings in a compact form. This fundamentally changes the quality ceiling achievable with coding agents.

## Why People Are Using It
Roman reports using /re multiple times per session as a standard workflow. The three-tier framework (90/9/1 split) positions this as the differentiating practice of top-tier AI coders. The technique requires no external tools — just Claude Code's built-in /re command.

## Potential Alternatives
Creating a new session for each new approach (loses common trunk context). Using handoff documents (lossy, requires writing). Compact command (worse than either, as argued in Video 3).

## Potential Improvements
Visualizing the session tree structure (not just a linear history) would make trajectory engineering more intuitive. Automatic trunk detection (identify which parts of context are stable reusable vs. ephemeral exploration) could automate the trimming decision.

## Potential Failure Modes
Without clear mental tagging of trunk vs. branch content, practitioners may trim context that was actually load-bearing. Time-travel is limited to the current session — it cannot restore context from a previous session.
