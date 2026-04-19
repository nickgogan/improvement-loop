---
notion_id: 32b1e08b-9b34-81e3-bcd3-d927b2ea3775
name: Concierge Agent Architecture (Slack + Notion + Claude Code)
summary: 'A three-layer orchestration model: Slack handles user intake (Front Desk), Notion Custom Agents handle lightweight operations (triage, Q&A), and Claude Code handles heavyweight execution (Build
  Specs). Messaging bots are kept narrowly scoped to intake -- not triage.'
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
proposer_priority: null
applicability:
- S2 (Notion Operations)
adopted_in:
- S2 (Notion Operations)
sources:
- notion-custom-agents-the-best-new-ai-for-all.md
proposals: []
date_discovered: '2026-03-15'
last_updated: '2026-04-07'
pipeline_status: "raw"
consumed_by: []
---
# Concierge Agent Architecture (Slack + Notion + Claude Code)

## What It Is
The Concierge architecture assigns each platform a bounded role: Slack (Front Desk) captures user intent and routes it; Notion Custom Agents handle structured, lightweight operations like triage and Q&A; Claude Code handles complex, long-horizon execution like generating Build Specs. PEA cadences (Daily Pulse, Weekly Family Meeting) manage human-in-the-loop review.

## Why It Matters
Scope creep in the intake bot is the most common failure in multi-agent orchestration -- when the Slack bot tries to do triage, it becomes brittle and hard to maintain. Keeping each layer narrowly scoped makes the system easier to debug, extend, and hand off.

## Why People Are Using It
Community validation includes a reference implementation of an 11-agent Notion system running at approximately $114/month. The community has converged on separating messaging bots from operational agents.

## Potential Improvements
Adding intent routing at the intake layer -- classifying the incoming request before it reaches Notion or Claude Code -- would reduce misrouting and allow more precise escalation paths.

## Potential Failure Modes
The most cited failure mode is the Slack bot expanding beyond intake into triage logic, creating a fragile, over-coupled system.
