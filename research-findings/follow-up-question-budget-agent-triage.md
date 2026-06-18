---
name: Follow-Up Question Budget in Agent Triage
summary: Hard limit of 2 follow-up questions per triage response. Each question must be high-value (would change label assignment, owner routing, or reproduction confidence if answered). Prevents over-questioning
  by requiring each question to pass a value test before being asked.
implementation_notes: null
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources: []
related_findings:
- file: agent-proof-of-work-ui-trust-building.md
  rel: same-problem
- file: agent-clarification-over-assumption-pattern.md
  rel: same-problem
proposals: null
date_discovered: '2026-05-24'
last_updated: '2026-05-24'
pipeline_status: raw
---

# Follow-Up Question Budget in Agent Triage

## Pattern

When an AI agent triages issues (or any information-gathering task), enforce a hard limit on follow-up questions:

**Budget:** At most 2 follow-up questions per response.

**Quality gate per question:**
- Must be "high-value" — answering it would meaningfully change the label assignment, owner routing, or reproduction confidence
- Cannot be inferred from existing evidence (check first, then ask)
- Cannot bundle multiple sub-questions into a single bullet
- If more than 2 unknowns exist, prioritize the two most likely to unblock triage

**Before asking, check:**
- Issue body, comments, attachments, logs, labels, and repository context
- Existing documentation and feature set (maybe it's already supported)
- Visual evidence (screenshots, recordings) for information that can be inferred

## Why It Matters

Without a budget, AI agents default to asking many questions (feels thorough, costs nothing to the agent). But each question costs the reporter time and attention, often leading to "question fatigue" where reporters abandon issues. A budget forces the agent to prioritize information gathering — exactly what a skilled human triage engineer would do.

The "high-value" test also prevents low-information questions that don't actually change the outcome regardless of the answer.

## How It Could Fail

- 2 may be too few for genuinely complex/ambiguous issues
- The "high-value" test is subjective — agents may miscalculate what's high-value
- May miss critical context that a third question would have revealed
- Reporters may still feel interrogated even with 2 questions

## Evidence

Warp (warpdotdev/warp) — `triage-issue-local` skill with explicit "Ask at most 2 follow-up questions" rule and high-value criteria. Production-tested across thousands of issue triage operations visible at build.warp.dev.
