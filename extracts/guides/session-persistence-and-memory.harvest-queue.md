# Co-occurrence Harvest Queue — Session Persistence and Memory

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

> Ruled 2026-07-13 (session 146) under Nick's delegated-judgment grant; per-row statuses set accordingly.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-13 | extracted | rule | [[append-only-run-log-as-working-memory]] | "append-only-no-edit-delete-log-invariant" | extracted to [[append-only-no-edit-delete-log-invariant]] |
| 2026-07-13 | extracted | template | [[append-only-lesson-store-owning-surface-identity]] | "lesson-store-entry-schema" | extracted to [[lesson-store-entry-schema]] |
| 2026-07-13 | extracted | rule | [[append-only-lesson-store-owning-surface-identity]] | "pruning-is-status-change-never-deletion" | extracted to [[pruning-is-status-change-never-deletion]] |
| 2026-07-13 | extracted | rule | [[derive-dont-edit-artifacts-as-log-renders]] | "one-writer-per-artifact-derive-dont-edit" | merged into [[derived-artifacts-single-writer-rule]] |
| 2026-07-13 | nick-dismissed | template | [[memory-system-evaluation-triad-storage-injection-recall]] | "memory-system-triad-scorecard" | dismissed |
| 2026-07-19 | extracted | rule | [[incremental-snapshotting-copy-on-write-block-diffing]] | "block-level-incremental-snapshot-not-full-disk" | extracted to [[block-level-incremental-snapshot-not-full-disk]] |
| 2026-07-19 | extracted | rule | [[posix-tiered-cache-persistence-over-object-storage]] | "posix-compliant-sandbox-storage-not-nfs" | extracted to [[posix-compliant-sandbox-storage-not-nfs]] |
| 2026-07-19 | nick-dismissed | rule | [[agentic-file-classification-reliability-calibration]] | "consequence-weighted-classification-review-gate" | dismissed |

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
- **Status:** extracted
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
- **Resolution:** extracted to [[lesson-store-entry-schema]]

Extracted 2026-07-13 — Session 146 — [[session-persistence-and-memory.harvest-queue]] — to [[lesson-store-entry-schema]]. DD-100 create-new ruled (false-positive override): distinct object from the per-skill [[skill-self-improvement-lessons-log-template]] — a central cross-cutting lesson STORE keyed by (owning surface, failure pattern) with occurrence-dedup and a closed status lifecycle, not the per-skill co-located LOG. New baseline template written; no version bump.

### append-only-lesson-store-owning-surface-identity::rule::pruning-is-status-change-never-deletion

- **Date queued:** 2026-07-13
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[append-only-lesson-store-owning-surface-identity]]
- **Source excerpt:**
  > "Status transitions only: `open → promoted | declined`, `open|declined → pruned`.
  > Resolved entries stay in the file as the durable record — pruning is an
  > operator-approved status change, never a deletion."
- **Codifier's reading:** Imperative, binary-checkable directive (entries never deleted; only enumerated status transitions permitted) — machine-enforceable over any lesson-store file.
- **Suggested headline:** pruning-is-status-change-never-deletion
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[pruning-is-status-change-never-deletion]]

Extracted 2026-07-13 — Session 146 — [[session-persistence-and-memory.harvest-queue]] — to [[pruning-is-status-change-never-deletion]]. DD-97 create-new ruled (false-positive override): the matched [[append-only-no-edit-delete-log-invariant]] governs run logs, explicitly scopes lesson stores OUT, and forbids a mutable status field — the candidate governs a lesson store and REQUIRES a status-transition-on-a-field primitive (opposite primitives, distinct object). New rule written; no merge.

### derive-dont-edit-artifacts-as-log-renders::rule::one-writer-per-artifact-derive-dont-edit

- **Date queued:** 2026-07-13
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[derive-dont-edit-artifacts-as-log-renders]]
- **Source excerpt:**
  > "1. **Artifacts are derived, not edited.** … 'SPEC.md … DERIVED from .memlog.md, never
  > hand-edited.' A hand-edit is not merged — it is overwritten on the next derive.
  > 2. **One writer per artifact.**"
- **Codifier's reading:** The finding itself names this "a write-discipline rule pair" — imperative directives (never hand-edit derived artifacts; exactly one writer per artifact) with a structural enforcement path (overwrite-on-derive).
- **Suggested headline:** one-writer-per-artifact-derive-dont-edit
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** merged into [[derived-artifacts-single-writer-rule]]

### memory-system-evaluation-triad-storage-injection-recall::template::memory-system-triad-scorecard

- **Date queued:** 2026-07-13
- **Status:** nick-dismissed
- **Target form:** template
- **Source finding:** [[memory-system-evaluation-triad-storage-injection-recall]]
- **Source excerpt:**
  > "1. **Storage** — when something that matters is discussed, how does it get saved …
  > 2. **Injection** — at session start, what is loaded automatically …
  > 3. **Recall** — when the user asks about something old, what mechanism finds it …"
- **Codifier's reading:** The three-question rubric could render as a per-axis scorecard scaffold; but the finding notes a per-axis scoring rubric is a *potential improvement*, not yet defined — thin as a standalone template today. Guide Step 1.7 already carries the usable form inline.
- **Suggested headline:** memory-system-triad-scorecard
- **Recommendation:** dismiss as inline
- **Resolution:** dismissed

### incremental-snapshotting-copy-on-write-block-diffing::rule::block-level-incremental-snapshot-not-full-disk

- **Date queued:** 2026-07-19
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[incremental-snapshotting-copy-on-write-block-diffing]]
- **Source excerpt:**
  > "Four requirements are stated explicitly as the bar any such system must clear:
  > incremental (not full) snapshots, fast save, fast restore, and configurable scope …
  > plus a deliberate choice of block-level over file-level diffing specifically to avoid
  > write amplification on large files that change only slightly."
- **Codifier's reading:** Imperative, machine-checkable infrastructure directive ("snapshot agent disk state incrementally at block level with configurable scope, never full-disk") instantiating the pattern's stated requirement bar — a crisp, reusable rule for any agent-sandbox persistence layer. Applicability caveat: no live code-execution surface in the engine today (design-stage grounding); the rule is a general external best-practice, not engine-enforced.
- **Suggested headline:** block-level-incremental-snapshot-not-full-disk
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[block-level-incremental-snapshot-not-full-disk]]

Extracted 2026-07-19 — Session 152 — [[session-persistence-and-memory.harvest-queue]] — to [[block-level-incremental-snapshot-not-full-disk]].

Extracted 2026-07-19 — Session 152 — [[session-persistence-and-memory.harvest-queue]] — to [[block-level-incremental-snapshot-not-full-disk]].

### posix-tiered-cache-persistence-over-object-storage::rule::posix-compliant-sandbox-storage-not-nfs

- **Date queued:** 2026-07-19
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[posix-tiered-cache-persistence-over-object-storage]]
- **Source excerpt:**
  > "NFS was considered and explicitly rejected as the underlying mechanism: it is both
  > less performant and not POSIX-compliant, and the coding/agentic models being sandboxed
  > are pre-trained overwhelmingly on standard POSIX filesystem behavior, so a non-standard
  > mount degrades their reliability on ordinary file operations."
- **Codifier's reading:** Imperative, machine-checkable directive ("expose agent sandbox storage through POSIX-compliant filesystem semantics; do not use NFS or other non-standard mounts") with an explicit reliability rationale (models trained on POSIX behavior). Reusable rule for any sandbox persistence substrate. Same no-live-sandbox applicability caveat as the companion snapshot rule.
- **Suggested headline:** posix-compliant-sandbox-storage-not-nfs
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[posix-compliant-sandbox-storage-not-nfs]]

Extracted 2026-07-19 — Session 152 — [[session-persistence-and-memory.harvest-queue]] — to [[posix-compliant-sandbox-storage-not-nfs]].

### agentic-file-classification-reliability-calibration::rule::consequence-weighted-classification-review-gate

- **Date queued:** 2026-07-19
- **Status:** nick-dismissed
- **Target form:** rule
- **Source finding:** [[agentic-file-classification-reliability-calibration]]
- **Source excerpt:**
  > "A consequence-weighted human-review gate: … stakes vary … routing designs could flag
  > only classifications whose downstream cost of error is high for review, rather than
  > reviewing uniformly or not at all."
- **Codifier's reading:** Reads as a rule-shape ("gate small-taxonomy classifications for human review by consequence, not uniformly"), but the finding itself explicitly disclaims directive status ("not a mandate to add gates … evidence, not a directive"), and the guidance is already carried inline in the regenerated guide's Step 5.1. Surfaced for the audit trail; better left inline than extracted as a standalone rule today.
- **Suggested headline:** consequence-weighted-classification-review-gate
- **Recommendation:** dismiss as inline
- **Resolution:** dismissed

Dismissed 2026-07-19 — Session 152 — [[session-persistence-and-memory.harvest-queue]] — per --harvest-dismiss invocation.
