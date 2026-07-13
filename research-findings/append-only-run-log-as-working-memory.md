---
name: "Append-Only Run Log as Durable Working Memory (Memlog / Progress Ledger)"
summary: |-
  Plain English: give every long-running agent workflow one append-only log file it
  writes decisions and completions into as they happen — never edited, never re-read
  mid-session, trusted over the agent's own recollection on resume. Two watched repos
  converged on this independently. BMAD v6.10.0 ships `memlog.py` as the shared
  working-memory primitive across its whole skill suite, with three designed
  invariants: append-only chronological (no edit/delete subcommand exists), write-only/
  blind (every call echoes state back as one JSON line so the caller never re-reads its
  own history mid-run; the file is read only on resume), and no lifecycle status field
  (completion is an `event` entry — "a resume learns the state by reading the last
  entries, the same way it learns everything else"); writes are atomic
  temp+fsync+rename. Superpowers v6.x independently added a durable progress ledger
  (`.superpowers/sdd/progress.md`, one appended line per completed task with commit
  range) after "the single most expensive failure observed": controllers re-dispatching
  entire completed task sequences after compaction; on resume the ledger and `git log`
  explicitly outrank conversation memory.
implementation_notes: |-
  Direct input to IB-172 (layered memory architecture) and the engine's
  PROGRESS/HISTORY session-ops spine. The memlog invariants are the designed version of
  what the engine approximates by convention: append-only truth, artifacts derived from
  it, state learned by reading the tail on resume. The blind-write discipline (JSON
  echo instead of mid-run re-reads) and the no-status-field rule are the two moves
  worth evaluating for the engine's layered-memory design; the Superpowers ledger shows
  the same primitive is what compaction recovery needs.
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "append-only-lesson-store-owning-surface-identity.md"
    rel: "same-problem"
  - file: "workflow-state-vs-conversation-state.md"
    rel: "same-problem"
  - file: "phase-queue-state-file-as-orchestrator-memory.md"
    rel: "same-problem"
  - file: "cross-session-learnings-jsonl.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "context-engineering"
  - "working-memory"
  - "append-only"
  - "cross-repo-convergence"
---

# Append-Only Run Log as Durable Working Memory (Memlog / Progress Ledger)

## What It Is

A single append-only file per run that is the workflow's working memory, with the
BMAD implementation defining the invariant set:

1. **Append-only chronological.** `memlog.py` has no edit or delete subcommand — the
   discipline is enforced by the tool's shape, not by prose. Writes are atomic
   (temp file + fsync + rename).
2. **Write-only / blind during the session.** Every `memlog.py` call echoes the
   resulting state as one JSON line, so the writing agent never re-reads its own
   history mid-run; the file is read only on resume.
3. **No lifecycle status field.** Completion, kills, and overrides are `event` entries
   in the stream. A resume learns state by reading the last entries — no mutable
   frontmatter to drift out of sync with the log.

Every BMAD flagship workflow logs each decision, assumption, override, and terminal
event as it happens; the finalize sequence starts with a "memlog audit" walking the log
with the user. Superpowers' progress ledger is the same primitive scoped to task
completion: one appended line per finished task (commit range + review status), with an
explicit trust rule — after compaction, the ledger and `git log`, not the agent's
recollection, determine where execution resumes.

## Why It Matters

Long agent runs die two deaths: context compaction (state evaporates) and state
mutation (the artifact and the history disagree). The append-only run log answers both
with one mechanism — and the two repos arrived at it from opposite directions, BMAD
for decision auditability and order-independent artifact derivation, Superpowers for
compaction recovery after its most expensive observed failure. The convergence is the
signal: durable, append-only, resume-by-reading-the-tail working memory is what
unattended and long-attended runs both end up needing.

## Why People Are Using It

BMAD standardized memlog across its entire flagship skill suite in v6.9.0 (replacing
per-skill decision logs); Superpowers added the ledger in its v6.0.0 SDD rewrite after
production failure evidence. Sources: Observed in
[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) v6.10.0 — see
[[bmad-method-analysis]] — and [superpowers](https://github.com/obra/superpowers)
v6.1.1 — see [[superpowers-analysis]].

## Potential Alternatives

- **Mutable state files** (STATE.md, status frontmatter) — simpler reads, but state and
  history can disagree, and concurrent/interrupted writes corrupt silently.
- **Conversation memory + compaction summaries** — zero infrastructure; exactly the
  thing both repos found untrustworthy.
- **Database-backed session stores** — stronger queries, heavier dependency; loses the
  git-diffable plain-text property.

## Potential Improvements

- Layer promotion: run logs are session-scoped; a promotion path into durable stores
  (lesson stores, changelogs) would connect working memory to long-term memory.
- Log-schema conventions (entry types like BMAD's `crack`/`kill`/`lock`) portable
  across systems.

## Potential Failure Modes

- **Log bloat on long runs** — append-only never shrinks; very long sessions pay
  growing resume-read cost.
- **Blind-write drift** — if the JSON echo is ignored, the agent's mental state and the
  log can diverge until resume exposes it.
- **Trust rule erosion** — the pattern only works if resume *actually* reads the tail
  instead of trusting residual conversation memory; that discipline is prose-enforced.
