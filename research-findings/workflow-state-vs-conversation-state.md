---
name: Workflow State vs. Conversation State Separation
summary: Explicit separation of conversation state (what was said) from workflow state (what step the agent is on and what side effects have occurred), enabling retry-safe crash recovery with explicit states
  like planned → awaiting_approval → executing → waiting_on_external.
implementation_notes: MetaSystem's milestone-gated development loop (DD-61) has implicit workflow states. Making these explicit and persistent would enable crash-resilient execution.
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropics-2-5-billion-leak-12-critical-pieces.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-07-13'
related_findings:
- file: session-as-append-only-event-log.md
  rel: extended-by
- file: planner-executor-deterministic-guardrails.md
  rel: same-problem
- file: durable-workflow-engine-for-agent-systems.md
  rel: enabled-by
- file: system-event-logging-actions-not-words.md
  rel: same-problem
- file: agent-state-machine-with-witness-monitoring.md
  rel: same-problem
- file: append-only-run-log-as-working-memory.md
  rel: same-problem
- file: spec-frontmatter-state-machine-unattended-dev-loop.md
  rel: extended-by
pipeline_status: synthesized
consumed_by:
- agent-workflow-and-execution.md
- session-persistence-and-memory.md
---
# Workflow State vs. Conversation State Separation

## What It Is
Conversation state = "what was said" (chat transcript). Workflow state = "what step am I on, what side effects have occurred, is this retry-safe?" Claude Code defines explicit states: planned → awaiting_approval → executing → waiting_on_external. Checkpoints persisted frequently; designed to avoid duplication and destruction on crash/retry.

## Why It Matters
Without this separation, retrying after a crash re-executes side effects (duplicate API calls, double writes). Workflow state makes operations idempotent and retry-safe.

## Why People Are Using It
Anthropic's production Claude Code. Foundation for reliable long-running multi-step operations.

## Potential Alternatives
Conversation-only state (simpler but not retry-safe). Database-backed state machines. Event sourcing patterns.

## Potential Improvements
Visual workflow state inspection for debugging. Automatic rollback on crash detection. State machine validation to prevent impossible transitions.

## Potential Failure Modes
State tracking overhead for simple operations. State desync between workflow and conversation. Over-engineering for tasks that don't have side effects.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[workflow-state-vs-conversation-state.md]] in `extracts/patterns/`
