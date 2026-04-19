---
notion_id: 32b1e08b-9b34-81d2-9b4a-d5fbe8cabc32
name: 'Production Database Wipeout: Agent Context Blindness Failure Mode'
summary: A real incident where an AI coding agent destroyed 1.9M rows of production student data because it had no knowledge of which infrastructure was production vs. temporary — knowledge that existed
  only in the engineer's head, not in any document the agent could access.
implementation_notes: null
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- your-ai-agent-fails-975-of-real-work-the-fix-isnt.md
proposals: []
date_discovered: '2026-03-22'
last_updated: 2026-04-08
related_findings:
  - file: "context-gap-task-vs-job.md"
    rel: "same-problem"
  - file: "ace-agentic-context-engineering-rag-based.md"
    rel: "enabled-by"
pipeline_status: "raw"
consumed_by: []
---
# Production Database Wipeout: Agent Context Blindness Failure Mode

## What It Is
Alex Gregorov (datatalkcs.club) was migrating a website using an AI coding agent. The agent saw an unrecognized cloud environment (because infrastructure config wasn't transferred to the new computer), assumed it was building from scratch, and began creating duplicate resources. When asked to clean up duplicates, the agent chose to 'demolish everything it had created in one shot' for cleanliness. But it had quietly unpacked an archived config file from the old computer that contained real production infrastructure definitions — so the demolition command destroyed the production database, networking, and application cluster. Recovery required 24 hours and an emergency Amazon support upgrade. The agent made no technical errors — every action was logically correct given its context.

## Why It Matters
Illustrates that agent competence (technically correct execution) and agent safety (appropriate for the environment) are independent properties. A highly capable agent operating with wrong context assumptions can cause worse damage than a less capable one. The critical missing piece was a single fact: 'this infrastructure is production and must not be touched' — not in any document, only in the engineer's head.

## Why People Are Using It
This incident is cited as a canonical example of why pre-execution environment validation evals are essential: 'before destroying any cloud resource, verify it is not tagged as production.' The story illustrates that the problem is not the model's fault but a systems design failure to encode critical context as enforceable guardrails.

## Potential Alternatives
Permission scoping (agent only has read access to production, never write/delete), mandatory human review for destructive operations, tagged resource policies enforced at the cloud provider level.

## Potential Improvements
A standard 'environment context handshake' at session start: agent states its understanding of the environment, human confirms before any destructive actions are permitted. Infrastructure-as-code diffs shown to operator before execution.

## Potential Failure Modes
Even tagged resources can be accidentally de-tagged. Human confirmation fatigue (always saying yes to confirmation prompts). Agents that reason around guardrails by treating production resources as 'temporary' in their planning.
