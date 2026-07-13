---
title: "Lessons — append-only operational lesson store"
type: "resource"
target_system:
  - "improvement-loop"
created: "2026-07-13"
---

# Lessons

Append-only lesson store (IB-176; design:
`project-management/design-notes/2026-07-13-memory-system-design.md` §2). Written by
`/self-improve` capture mode and the `/session-handoff` lessons-check sweep. Validated
by `store_check.py` in the pre-commit hook.

**Entry contract:**

- Header: `## L-<seq> · YYYY-MM-DD · high|normal · open|promoted|declined|pruned`
- Body fields (all required): **Lesson** (one line — what went wrong and the rule that
  prevents it), **Owning surface** (which file, if edited, prevents recurrence),
  **Source** (session ref, commit sha, artifact path, or `Q-<seq>`), **Occurrences**
  (comma-separated dates).
- Identity = (owning surface, failure pattern). Recurrence appends a date to
  Occurrences — never a duplicate entry.
- Untraceable lesson = invention: no Source, no entry.
- Retirement is a status change (`pruned`/`declined`), never deletion — git is the
  archive.
- Severity: `high` = data loss, governance breach, or user-visible failure (promotes
  at N=1); `normal` promotes at N=2. Severity is never silently lowered.

## Entries
