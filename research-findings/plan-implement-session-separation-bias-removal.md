---
name: Plan-Implement Session Separation for Bias Removal
summary: 'A specific harness engineering principle: planning and implementation must occur in different coding agent sessions with a fresh context window boundary between them. The planning node writes
  to an artifact directory; the implementation node reads from it in a clean session. This prevents ''planning bias'' — where the implementation session is unconsciously influenced by the planning conversation''s
  reasoning path rather than the plan artifact itself.'
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- archon-open-source-harness-builder.md
related_findings:
- file: new-chat-per-agent-step-context-hygiene.md
  rel: extends
- file: orchestrator-headless-dispatch-context-isolation.md
  rel: same-problem
- file: boris-chernys-explore-plan-implement-commit-workf.md
  rel: extends
- file: planner-executor-deterministic-guardrails.md
  rel: extends
- file: war-game-plan-format-for-executor-handoff.md
  rel: same-problem
- file: planning-thread-vs-execution-thread-subagent-fleets.md
  rel: extended-by
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-07-12'
pipeline_status: classified
consumed_by: []
tags:
- session-95-reextract
---

## What It Is

Cole Medin states explicitly: "You always want to do your planning and implementation in different coding sessions to remove bias." In Archon's workflow system, each node can be configured as either `continue` (extend the prior node's session) or `fresh` (new session). The plan-to-implement boundary should always use `fresh`.

The mechanism: the planning node writes its output to an `artifact_dir` — a file-based handoff. The implementation node starts with a fresh context window and reads only the artifact, not the planning conversation. This means the implementation agent receives the plan as a specification, without the exploratory reasoning, false starts, or hedging that occurred during planning.

This is a specific application of the more general "new-chat-per-agent-step" discipline, but with a named rationale: **planning bias**. When implementation occurs in the same session as planning, the agent tends to follow the planning conversation's reasoning path rather than treating the plan artifact as an independent specification. The fresh session forces the implementation agent to interpret the plan on its own terms.

## Why It Matters

Planning bias is a subtle failure mode. The agent appears to follow the plan, but its implementation choices are shaped by the planning conversation's exploration rather than the plan's stated requirements. This manifests as:
- Implementing alternatives that were discussed and rejected during planning
- Carrying forward assumptions that were questioned but not resolved
- Over-engineering areas that received disproportionate planning attention

A clean context boundary ensures the implementation agent sees the plan as a reader, not as a participant in its creation. This is the same principle that makes code review by a different developer more effective than self-review.

## Why People Are Using It

Cole Medin cites this as a core Archon design principle. The Archon workflow system's `continue`/`fresh` parameter per node makes this trivial to enforce. The fix-GitHub-issue workflow uses fresh sessions between classification, investigation, implementation, and validation nodes.

## Potential Improvements

- Plan quality validation before passing to implementation — a deterministic node that checks the plan artifact against a schema
- Bidirectional bias detection — also check whether the implementation node's output was influenced by information not in the plan artifact
- Summary extraction from the planning session that captures key decisions and rejected alternatives as metadata alongside the plan

## Potential Failure Modes

- The plan artifact itself may be incomplete or ambiguous, and the implementation agent has no conversation context to disambiguate
- Fresh sessions increase total token cost (each session re-reads project context)
- Overly rigid separation for small tasks where plan-and-implement in one session is more efficient
