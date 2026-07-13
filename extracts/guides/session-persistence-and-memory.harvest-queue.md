# Co-occurrence Harvest Queue — Session Persistence and Memory

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

> Ruled 2026-07-13 (session 146) under Nick's delegated-judgment grant; per-row statuses set accordingly.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-13 | extracted | rule | [[append-only-run-log-as-working-memory]] | "append-only-no-edit-delete-log-invariant" | extracted to [[append-only-no-edit-delete-log-invariant]] |
| 2026-07-13 | nick-approved | template | [[append-only-lesson-store-owning-surface-identity]] | "lesson-store-entry-schema" | extract via /extract-artifacts |
| 2026-07-13 | nick-approved | rule | [[append-only-lesson-store-owning-surface-identity]] | "pruning-is-status-change-never-deletion" | extract via /extract-artifacts |
| 2026-07-13 | nick-approved | rule | [[derive-dont-edit-artifacts-as-log-renders]] | "one-writer-per-artifact-derive-dont-edit" | extract via /extract-artifacts |
| 2026-07-13 | queued | template | [[memory-system-evaluation-triad-storage-injection-recall]] | "memory-system-triad-scorecard" | dismiss as inline |

## Per-row details

### append-only-run-log-as-working-memory::rule::append-only-no-edit-delete-log-invariant

- **Date queued:** 2026-07-13
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[append-only-run-log-as-working-memory]]
- **Source excerpt:**
  > "**Append-only chronological.** `memlog.py` has no edit or delete subcommand — the
  > discipline is enforced by the tool's shape, not by prose. Writes are atomic
  > (temp file + fsync + rename)."
- **Codifier's reading:** Deterministic, machine-enforceable boundary ("no edit/delete operation may exist on a run log") instantiating the pattern's invariant set — flagged as rule co-occurrence in the 2026-07-13 identification report.
- **Suggested headline:** append-only-no-edit-delete-log-invariant
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[append-only-no-edit-delete-log-invariant]]

Extracted 2026-07-13 — Session 146 — [[session-persistence-and-memory.harvest-queue]] — to [[append-only-no-edit-delete-log-invariant]].

### append-only-lesson-store-owning-surface-identity::template::lesson-store-entry-schema

- **Date queued:** 2026-07-13
- **Status:** nick-approved
- **Target form:** template
- **Source finding:** [[append-only-lesson-store-owning-surface-identity]]
- **Source excerpt:**
  > "**Entry schema (all fields required):** header `## L-<seq> · <date> · <high|normal> ·
  > <open|promoted|declined|pruned>`, plus one-line **Lesson** (what went wrong and the rule
  > that prevents it), **Owning surface**, **Source** (session ref, commit sha, or artifact
  > path — at least one), and **Occurrences**."
- **Codifier's reading:** A structural scaffold with named required fields and a closed status enum — directly renderable as a fillable lesson-entry template; relevant to the IB-172/IB-176 lessons.md design.
- **Suggested headline:** lesson-store-entry-schema
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### append-only-lesson-store-owning-surface-identity::rule::pruning-is-status-change-never-deletion

- **Date queued:** 2026-07-13
- **Status:** nick-approved
- **Target form:** rule
- **Source finding:** [[append-only-lesson-store-owning-surface-identity]]
- **Source excerpt:**
  > "Status transitions only: `open → promoted | declined`, `open|declined → pruned`.
  > Resolved entries stay in the file as the durable record — pruning is an
  > operator-approved status change, never a deletion."
- **Codifier's reading:** Imperative, binary-checkable directive (entries never deleted; only enumerated status transitions permitted) — machine-enforceable over any lesson-store file.
- **Suggested headline:** pruning-is-status-change-never-deletion
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### derive-dont-edit-artifacts-as-log-renders::rule::one-writer-per-artifact-derive-dont-edit

- **Date queued:** 2026-07-13
- **Status:** nick-approved
- **Target form:** rule
- **Source finding:** [[derive-dont-edit-artifacts-as-log-renders]]
- **Source excerpt:**
  > "1. **Artifacts are derived, not edited.** … 'SPEC.md … DERIVED from .memlog.md, never
  > hand-edited.' A hand-edit is not merged — it is overwritten on the next derive.
  > 2. **One writer per artifact.**"
- **Codifier's reading:** The finding itself names this "a write-discipline rule pair" — imperative directives (never hand-edit derived artifacts; exactly one writer per artifact) with a structural enforcement path (overwrite-on-derive).
- **Suggested headline:** one-writer-per-artifact-derive-dont-edit
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### memory-system-evaluation-triad-storage-injection-recall::template::memory-system-triad-scorecard

- **Date queued:** 2026-07-13
- **Status:** queued
- **Target form:** template
- **Source finding:** [[memory-system-evaluation-triad-storage-injection-recall]]
- **Source excerpt:**
  > "1. **Storage** — when something that matters is discussed, how does it get saved …
  > 2. **Injection** — at session start, what is loaded automatically …
  > 3. **Recall** — when the user asks about something old, what mechanism finds it …"
- **Codifier's reading:** The three-question rubric could render as a per-axis scorecard scaffold; but the finding notes a per-axis scoring rubric is a *potential improvement*, not yet defined — thin as a standalone template today. Guide Step 1.7 already carries the usable form inline.
- **Suggested headline:** memory-system-triad-scorecard
- **Recommendation:** dismiss as inline
- **Resolution:**
