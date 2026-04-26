---
title: "File Read Deduplication (18% Duplicate Reads, 2.6% Fleet Savings)"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "file-read-deduplication-pattern"
extraction_date: "2026-04-19"
last_change_session: 44
last_change_sl: "session-44-codifier-extraction-run"
identification_report: "2026-04-19-identification-report-4.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agentic coding systems with file-read-heavy workflows"
    - "custom agent harnesses where file read tool calls are interceptable"
    - "long-session agent workflows reading large reference or configuration files repeatedly"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — deduplication layer is additive infrastructure; removing it reverts to full re-reads with no data loss"
  auditability: "medium — stub responses are logged and distinguishable from full reads; session read history is inspectable in harness state"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Pattern is implemented in Claude Code's production infrastructure; not yet adopted in custom harness context as of extraction date."
contract:
  preconditions: "Session-scoped read history is initialized at session start. The execution environment provides filesystem mtime. File read tool call is interceptable."
  invariants: "Read history is strictly session-scoped. mtime comparison is always against the live filesystem. Every full read updates the history entry. Stub response is unambiguous."
  governance: "Owner: Infrastructure layer of the agent harness. Modification to deduplication thresholds or stub format requires a logged configuration change."
  recovery: "If read history unavailable: proceed without deduplication for that session, log the failure. If mtime unavailable: default to full re-read for that file."
tags:
  - "extracted-artifact"
  - "rule"
---

# File Read Deduplication

**Source:** [[file-read-deduplication-pattern]]
**Form:** rule
**Extraction date:** 2026-04-19

## Condition

An agent requests a file read operation for a file that has already been read during the current session.

## Action

**Required:** Before executing a full file read, check whether the file has changed since the last read in this session. If the file is unchanged, return a one-line stub confirming no change instead of re-reading the full file content.

**Forbidden:** Re-reading a file in full when the session has a cached read and no modification has occurred.

## Boundary

Enforced at the file-read tool call layer — before the read operation is dispatched. Applies within a single agent session. Does not persist across session boundaries.

## Enforcement

- **Mechanism:** Session-scoped read history: a map of `{file_path → last_read_timestamp}` maintained in session state.
- **Check:** On each file read request, look up `file_path` in read history. If found, compare file modification time (mtime) to `last_read_timestamp`. If `mtime ≤ last_read_timestamp`: return stub. If `mtime > last_read_timestamp`: execute full read, update history entry.
- **Stub format:** `[DEDUP] {file_path} unchanged since {last_read_timestamp}. No re-read performed.`
- **History update:** On every full read, record `{file_path → current_timestamp}` in session read history.
- **Scope:** Per session. Read history is cleared at session end.

## Rationale

Production metrics from Claude Code show 18% of all file reads within a session are duplicates of files already read with no intervening modification. At fleet scale this represents 2.6% of all token costs. The pattern is validated at production scale.

## Failure Modes

- **Stale cache from external modification:** Mitigated by always comparing against filesystem mtime, not a fixed TTL.
- **False savings on small files:** For files under ~500 tokens, deduplication overhead may exceed savings. Apply only above a minimum size threshold.
- **Read history implementation complexity:** Custom harnesses must implement and maintain session-scoped read history.

## Contract

### Preconditions
Session-scoped read history is initialized at session start. The execution environment provides filesystem mtime. File read tool call is interceptable.

### Invariants
Read history is strictly session-scoped. mtime comparison is always against the live filesystem. Every full read updates the history entry. Stub response is unambiguous.

### Governance
Owner: Infrastructure layer of the agent harness. Modification to deduplication thresholds or stub format requires a logged configuration change.

### Recovery
If read history unavailable: proceed without deduplication for that session, log the failure. If mtime unavailable: default to full re-read for that file.
