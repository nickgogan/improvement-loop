---
notion_id: 32b1e08b-9b34-81be-9b5e-db592dceca2f
name: 'Trajectory Engineering: Non-Linear Session Forking with /re'
summary: Advanced Claude Code users exploit LLM statelessness to jump back to any prior session state (via /re or double-ESC), fork into parallel trajectories, and trim context to the lean 'trunk' — enabling
  exploration of solution approaches without accumulating context rot from dead ends.
implementation_notes: null
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-code-works-better-when-you-do-this.md
- anthropic-claude-code-session-management-1m-context.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-20'
related_findings:
- file: fork-subagent-parallel-trajectory-exploration.md
  rel: same-problem
- file: claude-code-context-management-decision-matrix-five-tools.md
  rel: extends
- file: proactive-compaction-before-intelligence-degradation.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- managing-agent-context.md
- artifact: re-fork-and-trim-trajectory-procedure
  type: extracted-artifact
  form: skill
  date: 2026-04-27
  session: 83
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

## Corroborating Evidence — 2026-04-20 (Anthropic canonical framing)

Anthropic's April 2026 "Session Management and 1M Context" blog post (Thariq Shihipar) formalizes the /rewind primitive as a first-class matrix cell in the product decision framework (see [[claude-code-context-management-decision-matrix-five-tools.md]]). Anthropic's guidance: "Rewind is often the better approach to correction" — rather than forward-patching with "that didn't work, try X," rewind post-file-reads and re-prompt with the learnings. This promotes Roman's practitioner framing of trajectory engineering from "advanced technique" to "Anthropic-recommended default." The shortcut is now officially Esc+Esc. Evidence_strength remains Strong; applicability widens to all Claude Code users, not just advanced practitioners.
