---
title: "Workflow State vs. Conversation State Separation"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "workflow-state-vs-conversation-state"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "An agent system performs multi-step operations that produce side effects (file writes, API calls, state mutations). At least one operation is not naturally idempotent."
  invariants: "Workflow state and conversation state are stored and managed independently. Workflow state includes explicit step tracking and side-effect records. Retry of a crashed operation consults workflow state to skip completed side effects."
  governance: "Workflow state schemas are versioned. State transitions are validated against a defined state machine -- impossible transitions are rejected. Workflow state is never derived solely from conversation replay."
  recovery: "On crash, read the last persisted workflow checkpoint, identify completed side effects, and resume from the next incomplete step. If workflow state is corrupted or missing, fall back to a safe default (re-plan from scratch) rather than replaying the conversation."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Workflow State vs. Conversation State Separation

**Source:** [[workflow-state-vs-conversation-state]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agent systems that rely solely on conversation state (the chat transcript) for tracking progress conflate "what was said" with "what was done." When a crash occurs mid-operation, retrying from the conversation replays side effects -- duplicate API calls, double file writes, repeated mutations. The conversation transcript records intent and discussion but does not reliably indicate which steps completed, which side effects occurred, or whether the current state is consistent. Long-running multi-step operations are especially vulnerable because the window for crashes grows with execution time.

## Forces

- **Simplicity vs. safety:** Conversation-only state is simpler to implement (no additional persistence layer), but any crash during a multi-step operation risks duplicated or inconsistent side effects.
- **Conversation fidelity vs. operation tracking:** The conversation captures rich context about reasoning and decisions, but it is a poor data structure for tracking step completion and side-effect status.
- **Checkpoint frequency vs. overhead:** Persisting workflow state at every micro-step adds overhead; persisting too infrequently leaves gaps where crashes can cause inconsistency.
- **State complexity vs. task complexity:** Simple tasks (single-step, no side effects) do not need workflow state separation. The pattern adds overhead that is only justified when operations have side effects or span multiple steps.
- **Sync burden vs. divergence risk:** Maintaining two separate state representations (conversation and workflow) creates a risk that they diverge, but a single representation cannot serve both purposes.

## Solution

Separate agent state into two independently managed layers:

**Conversation state** tracks what was said -- the chat transcript, reasoning, user inputs, and agent responses. It is append-only and serves as an audit log and context source for the LLM.

**Workflow state** tracks what step the agent is on, what side effects have occurred, and whether the current position is retry-safe. It uses explicit, enumerated states:

- `planned` -- steps defined but not started
- `awaiting_approval` -- human gate before execution
- `executing` -- active side effects in progress
- `waiting_on_external` -- blocked on external system response
- `completed` -- step finished, side effects recorded
- `failed` -- step failed, failure reason recorded

Implementation requirements:

1. **Persist workflow state frequently.** Checkpoint after each state transition, not just at task boundaries. Use a persistent store that survives process crashes (file, database, not in-memory only).

2. **Record side effects explicitly.** When a step produces a side effect (file written, API called, resource created), record it in workflow state immediately. On retry, consult the side-effect record to determine what can be skipped.

3. **Design for idempotent retry.** Each step should be resumable from its last checkpoint without re-executing completed side effects. The combination of explicit state tracking and side-effect recording makes this possible without requiring every individual operation to be natively idempotent.

4. **Validate state transitions.** Define the legal state machine (which transitions are valid) and reject impossible transitions. This catches bugs where the workflow jumps to an inconsistent state.

5. **Never derive workflow state from conversation replay.** The conversation may be ambiguous, truncated, or misleading about what actually completed. Workflow state is the authoritative record of progress.

## Consequences

**Positive:**
- Crash recovery is safe and deterministic -- resume from the last checkpoint without re-executing side effects
- Operations become retry-safe by design, not by accident or by requiring every operation to be individually idempotent
- Clear separation enables independent optimization: conversation state for LLM context, workflow state for operational reliability
- Explicit state machine makes debugging straightforward -- the current state and valid transitions are inspectable

**Negative:**
- Added complexity for simple tasks that have no side effects and no crash risk
- Two state representations must be kept in sync -- divergence creates confusion about actual progress
- Checkpoint persistence adds latency to each state transition
- State machine design requires upfront analysis of all possible steps and transitions, which may be premature for exploratory tasks

## Known Uses

- Anthropic's production Claude Code system, where explicit workflow states (planned, awaiting_approval, executing, waiting_on_external) are persisted frequently to enable crash recovery
- MetaSystem's milestone-gated development loop (DD-61) has implicit workflow states that could be made explicit and persistent for crash resilience
- Durable workflow engines (Temporal, AWS Step Functions) implement this pattern at the infrastructure level for distributed systems
- Event sourcing patterns in traditional software architecture achieve similar goals by recording state transitions as an append-only log

## Contract

### Preconditions
An agent system performs multi-step operations that produce side effects (file writes, API calls, state mutations, resource creation). At least one operation is not naturally idempotent. The system experiences or could experience mid-operation interruptions (crashes, token exhaustion, timeouts).

### Invariants
Workflow state and conversation state are stored and managed independently -- neither is derived from the other. Workflow state includes explicit step tracking with enumerated states and a side-effect record for each completed step. Retry of a crashed operation consults workflow state to determine completed side effects before resuming. State transitions are validated against the defined state machine; impossible transitions are rejected, not silently accepted.

### Governance
Workflow state schemas are versioned alongside the system configuration. New steps or state transitions require updating the state machine definition before implementation. Workflow state is the authoritative record of progress -- conversation state is supplementary context, not a source of truth for what completed. State machine definitions are reviewed when new operation types are added.

### Recovery
On crash: read the last persisted workflow checkpoint, identify completed side effects from the record, and resume execution from the next incomplete step. Do not replay the conversation to infer progress. If workflow state is corrupted or missing, fall back to a safe default (re-plan from scratch with human confirmation) rather than guessing at progress. If workflow and conversation state are discovered to have diverged, workflow state is authoritative for operational decisions; flag the divergence for investigation.
