---
title: "Read and Update memory.md on Agent Startup"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "memorymd-cross-session-preference-persistence"
identification_report: "session-persistence-and-memory.harvest-queue.md::memorymd-cross-session-preference-persistence::rule::agent-must-read-and-update-memory-md-on-startup"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
deployed: false
deployed_to: null
context:
  applies_to:
    - "persistent role-based agents used across multiple sessions"
    - "agent harnesses that lack built-in cross-session memory"
    - "long-running agent deployments where users repeat corrections without a persistence layer"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — remove the system-prompt clause and the memory file; no migration cost"
  auditability: "high when the memory file is committed to a visible location and session logs capture read/write events; medium when the file is local-only"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Production-tested by practitioners running persistent role agents; no formal MetaSystem deployment at extraction time."
contract:
  preconditions: "A persistent role-based agent runs across multiple sessions on a harness with no built-in cross-session memory. A plain-markdown memory file is provisioned alongside the primary system-prompt file. The agent has read/write access to the memory file. The system-prompt file contains an explicit clause naming the memory file and instructing read-on-startup plus update-on-correction."
  invariants: "Every session begins with a full read of the memory file before any task action. Every user correction, stated preference, or durable learned fact during the session is written to the memory file before the agent moves on. The user can see and reject any write. The memory file remains within a size budget that does not itself cause context bloat (best-practice cap of roughly 200 lines for the primary context file)."
  governance: "Owner: Whoever maintains the agent's system-prompt file (e.g., CLAUDE.md author, agent definition author). The read/update directive must be embedded explicitly in that file rather than delegated to model judgment. The user retains veto power over any addition — entries are user-visible and editable. Periodic pruning of stale or unreferenced entries is the user's responsibility (or a scheduled maintenance task) to prevent unbounded growth."
  recovery: "If startup-read is skipped, the user surfaces the omission and the agent reads before continuing. If a correction is absorbed silently without write, the user prompts an explicit write and verifies the entry. If hallucinated or incorrect content lands in the memory file, the user edits or deletes it directly — false memories compound otherwise. If the file grows beyond the size budget, prune unreferenced entries or split into structured sections."
tags:
  - "extracted-artifact"
  - "rule"
---

# Read and Update memory.md on Agent Startup

**Source:** [[memorymd-cross-session-preference-persistence]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

A persistent role-based agent runs across multiple sessions on a harness whose default behavior provides no cross-session memory (each session starts fresh with no recall of prior corrections, preferences, or learned facts). A plain-markdown memory file (e.g., `memory.md`) is provisioned alongside the agent's primary system-prompt file as the user-visible persistence surface.

## Action

**Required:** At session start, the agent reads the memory file in full before taking any task action. During the session, when the user makes a correction, states a preference, or supplies a learned fact the agent should retain, the agent immediately writes the new entry into the relevant section of the memory file. The agent surfaces what it wrote so the user can verify.

**Forbidden:** Beginning task work in a fresh session without first reading the memory file. Deferring memory-file updates to end-of-session (corrections may be forgotten or lost on context truncation). Writing to the memory file silently — the user must be able to see and reject any addition. Using the memory file as a dumping ground for transcript-level chatter; entries are scoped to durable preferences, corrections, and facts.

## Boundary

Enforced at two boundaries: (1) **Session start** — the read happens before the first task action of the session. (2) **Each correction/preference event** during the session — the write happens immediately after the user-stated correction, before the agent moves on. The directive lives in the agent's primary system-prompt file (e.g., `CLAUDE.md`, `agents.md`, system prompt) so that every session begins with the read-instruction in context.

## Enforcement

- **Mechanism:** A short, explicit clause in the agent's system-prompt file instructs both the read-on-startup and the update-on-correction behaviors. The clause names the memory file by path.
- **Check (deterministic):** `(memory_file_read_before_first_action == true) AND (corrections_written_to_memory_file_during_session == true)`. Reviewable from session logs.
- **Violation response:** If the agent skips startup-read, the user surfaces the omission and the agent reads before continuing. If the agent silently absorbs a correction without persisting, the user prompts an explicit write. Repeated lapses indicate the system-prompt clause is too weak — strengthen the directive.

## Rationale

Default agent harnesses provide no cross-session memory, so users repeat the same corrections endlessly. A user-visible markdown memory file gives compounding improvement: corrections persist, preferences accumulate, role-specific knowledge survives session boundaries — without depending on opaque cloud-managed memory systems users cannot inspect. Production-tested. The transparent file is also fully user-controllable (unlike opaque vendor memory features), which preserves user agency over what the agent remembers.

## Contract

### Preconditions
A persistent role-based agent runs across multiple sessions on a harness with no built-in cross-session memory. A plain-markdown memory file is provisioned alongside the primary system-prompt file. The agent has read/write access to the memory file. The system-prompt file contains an explicit clause naming the memory file and instructing read-on-startup plus update-on-correction.

### Invariants
Every session begins with a full read of the memory file before any task action. Every user correction, stated preference, or durable learned fact during the session is written to the memory file before the agent moves on. The user can see and reject any write. The memory file remains within a size budget that does not itself cause context bloat (best-practice cap of roughly 200 lines for the primary context file).

### Governance
Owner: Whoever maintains the agent's system-prompt file (e.g., CLAUDE.md author, agent definition author). The read/update directive must be embedded explicitly in that file rather than delegated to model judgment. The user retains veto power over any addition — entries are user-visible and editable. Periodic pruning of stale or unreferenced entries is the user's responsibility (or a scheduled maintenance task) to prevent unbounded growth.

### Recovery
If startup-read is skipped, the user surfaces the omission and the agent reads before continuing. If a correction is absorbed silently without write, the user prompts an explicit write and verifies the entry. If hallucinated or incorrect content lands in the memory file, the user edits or deletes it directly — false memories compound otherwise. If the file grows beyond the size budget, prune unreferenced entries or split into structured sections.
