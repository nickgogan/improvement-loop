---
title: "Append-Only Run Log — No-Edit, No-Delete Invariant"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "append-only-run-log-as-working-memory"
extraction_date: "2026-07-13"
last_change_session: 146
last_change_report: "session-persistence-and-memory.harvest-queue"
identification_report: "session-persistence-and-memory.harvest-queue.md::append-only-run-log-as-working-memory::rule::append-only-no-edit-delete-log-invariant"
deployed: false
deployed_to: null
context:
  applies_to:
    - "long-running agent workflows that must survive context compaction or session interruption without losing run state"
    - "orchestrators resuming multi-task execution where re-dispatching already-completed work is the expensive failure"
    - "agent harness designers choosing a working-memory primitive for durable per-run state"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "low — adopting the log is additive, but migrating off it to mutable state files changes resume semantics and forfeits the run's decision history"
  auditability: "high — append-only growth is mechanically checkable (version-control diffs show only additions); the absence of edit/delete operations is verifiable from the logging tool's interface"
  evidence_strength: "Medium"
  adoption:
    status: "Partially Adopted"
    notes: "Two open-source agent frameworks converged on this independently: one ships an append-only run-log tool as the shared working-memory primitive across its whole skill suite; the other added a durable progress ledger after its most expensive observed failure — controllers re-dispatching entire completed task sequences after context compaction."
contract:
  preconditions: "A long-running agent workflow has one designated per-run log file used as working memory. The writer can append atomically (temp file + fsync + rename or equivalent). A resume protocol exists (or is being defined) that reads the log on session restart."
  invariants: "The logging interface exposes append operations only — no edit or delete operation exists on the run log; the discipline is enforced by the tool's shape, not by prose. Entries are chronological and every write is atomic. Lifecycle state (completion, kills, overrides) is recorded as event entries in the stream, never as a mutable status field. During the run the writer is blind: each write echoes the resulting state back to the caller, and the log is not re-read mid-run. On resume, the log tail (plus version-control history) outranks the agent's conversational recollection."
  governance: "Owner: the harness or tool layer that mediates run-log writes. Adding an edit or delete capability to the log tool is a deliberate design decision requiring review — it breaks the invariant the whole pattern rests on. The resume-reads-the-tail trust rule must be stated in the resume procedure itself, since it is the one prose-enforced leg of the discipline."
  recovery: "Wrong entry → append a correcting event; never rewrite history. Interrupted write → atomic write protocol leaves the file at the prior valid state; resume from the last valid entry. Resume that trusted conversational memory and diverged from the log → stop, re-read the tail, reconcile against the log before continuing. Log bloat degrading resume-read cost → snapshot or rotate at run boundaries only, never within a run."
tags:
  - "extracted-artifact"
  - "rule"
  - "append-only"
  - "working-memory"
  - "context-engineering"
  - "session-resume"
---

# Append-Only Run Log — No-Edit, No-Delete Invariant

**Source:** [[append-only-run-log-as-working-memory]]
**Form:** rule
**Extraction date:** 2026-07-13

## Condition

A long-running agent workflow maintains a per-run log file as its durable working memory — decisions, assumptions, overrides, task completions, and terminal events written as they happen. The run must survive context compaction, interruption, or hand-off, and on resume the workflow must reconstruct where it actually is rather than where the agent remembers being.

Scope of application: **session-scoped run logs and progress ledgers** — the working-memory layer. Governance audit logs (accountability records with storage-layer immutability and regulatory retention) are a different object governed by their own immutability rule; long-term memory stores (lesson stores, changelogs) are downstream promotion targets, not run logs.

## Action

**Required:**
- The run log is **append-only chronological**. The writing tool or procedure exposes no edit and no delete operation — the discipline is enforced by the tool's shape, not by instructions.
- Writes are **atomic** (temp file + fsync + rename, or an equivalent all-or-nothing write).
- Lifecycle state is recorded as **event entries in the stream** — completion, kill, and override are appended events, not a mutable status field. A resume learns the state by reading the last entries, the same way it learns everything else.
- During the run, writes are **blind**: each write echoes the resulting state back to the caller (e.g., one JSON line), so the writer never re-reads its own history mid-run. The file is read only on resume.
- On resume, the **log outranks recollection**: the log tail and version-control history — not the agent's conversational memory — determine what has been done and where execution continues.

**Forbidden:** Edit or delete subcommands on the run-log tool. Mutable status fields or frontmatter that can drift out of sync with the event stream. Re-reading the log mid-run as a substitute for the write echo. Resuming from conversational memory when a run log exists. Rewriting an entry to "fix" it — corrections are appended events.

## Boundary

Enforced at the logging tool's interface (what operations exist) and at the resume protocol (what is read first). Applies from the first entry of a run until the run's terminal event; the file persists after the run as the run's durable record. Out of scope: governance audit logs, always-loaded memory files, and derived artifacts rendered *from* the log.

## Enforcement

- **Mechanism:** Tool shape — the log writer implements append only. Version control provides the secondary check: diffs of the run log must show additions only.
- **Check (deterministic):** `(log_tool_has_edit_op == false) AND (log_tool_has_delete_op == false) AND (every_diff_is_append_only == true) AND (no_mutable_status_field_in_log == true)`. Any branch false → violation.
- **Violation response:**
  - *Edit/delete capability found on the tool:* remove it or gate it behind explicit design review; treat any log written while it existed as suspect for divergence.
  - *Non-append diff detected:* restore the overwritten history from version control; append a correcting event describing the divergence.
  - *Resume ignored the log:* halt; re-read the tail; reconcile the agent's plan against the logged state before any further dispatch.
- **Prose-enforced residue:** the resume-reads-the-tail trust rule cannot be enforced by tool shape — it must be stated in the resume procedure and checked in review.

## Rationale

Long agent runs die two deaths: context compaction (state evaporates) and state mutation (the artifact and the history disagree). One mechanism answers both — an append-only stream that is the single source of run truth, read from the tail on resume. Two independent production systems converged on this from opposite directions: one for decision auditability and order-independent artifact derivation, the other for compaction recovery after controllers re-dispatched entire completed task sequences. The convergence is the signal: durable, append-only, resume-by-reading-the-tail working memory is what unattended and long-attended runs both end up needing.

Enforcing the invariant through tool shape rather than prose is the load-bearing move: a tool with no edit subcommand cannot be talked into editing.

## Failure Modes

- **Log bloat on long runs.** Append-only never shrinks; very long sessions pay growing resume-read cost. Mitigation: rotate or snapshot at run boundaries only; keep entries structured and terse.
- **Blind-write drift.** If the write echo is ignored, the agent's mental state and the log diverge until resume exposes it. Mitigation: treat the echo as the authoritative state acknowledgment.
- **Trust-rule erosion.** The pattern only works if resume actually reads the tail instead of trusting residual conversation memory — and that leg is prose-enforced. Mitigation: make "read the log tail" the first step of the written resume procedure.

## Contract

### Preconditions
A long-running agent workflow has one designated per-run log file used as working memory. The writer can append atomically (temp file + fsync + rename or equivalent). A resume protocol exists (or is being defined) that reads the log on session restart.

### Invariants
The logging interface exposes append operations only — no edit or delete operation exists on the run log; the discipline is enforced by the tool's shape, not by prose. Entries are chronological and every write is atomic. Lifecycle state (completion, kills, overrides) is recorded as event entries in the stream, never as a mutable status field. During the run the writer is blind: each write echoes the resulting state back to the caller, and the log is not re-read mid-run. On resume, the log tail (plus version-control history) outranks the agent's conversational recollection.

### Governance
Owner: the harness or tool layer that mediates run-log writes. Adding an edit or delete capability to the log tool is a deliberate design decision requiring review — it breaks the invariant the whole pattern rests on. The resume-reads-the-tail trust rule must be stated in the resume procedure itself, since it is the one prose-enforced leg of the discipline.

### Recovery
Wrong entry → append a correcting event; never rewrite history. Interrupted write → atomic write protocol leaves the file at the prior valid state; resume from the last valid entry. Resume that trusted conversational memory and diverged from the log → stop, re-read the tail, reconcile against the log before continuing. Log bloat degrading resume-read cost → snapshot or rotate at run boundaries only, never within a run.
