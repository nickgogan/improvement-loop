---
title: "Lesson Store Entry Schema"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "append-only-lesson-store-owning-surface-identity"
extraction_date: "2026-07-13"
last_change_session: 146
last_change_report: "session-persistence-and-memory.harvest-queue"
identification_report: "session-persistence-and-memory.harvest-queue.md::append-only-lesson-store-owning-surface-identity::template::lesson-store-entry-schema"
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams running a self-improvement loop who need one durable, cross-cutting home for operational lessons rather than lessons scattered per tool or per session"
    - "agent systems that must distinguish 'seen once' from 'seen ten times' mechanically, so recurring failures accumulate evidence on a single entry"
    - "operators who want a human-gated promotion pipeline sitting on top of a lesson record — where each lesson carries a status the operator advances"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "low — entries accumulate as the durable record and are never deleted; migrating off the schema means rekeying every entry's identity and rebuilding the occurrence-dedup history"
  auditability: "high — every entry carries a required source (session ref, commit sha, or artifact path), a monotonic id, and a status drawn from a closed enum; compliance is verifiable field-by-field, and version-control diffs show only additions plus status changes"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "One production system runs this schema: a lesson store with 20 entries accumulated over ~5 days of sessions, all four statuses in use, with lessons about the store's own schema captured and fixed through the store's gated promotion path. No local adoption yet."
contract:
  preconditions: "A single central lesson-store file exists (or is being created) as the append-target for operational lessons across all surfaces — not a per-tool or per-session file. An operator (human or gated agent) can advance a lesson's status. Every candidate lesson can name at least one traceable source (session ref, commit sha, or artifact path); untraceable observations are excluded by construction."
  invariants: "Each entry's identity is the pair (owning surface, failure pattern) — the owning surface being the path that, if edited, prevents recurrence. A recurrence of the same identity appends a date to the existing entry's Occurrences list; it never creates a second entry. Every entry carries all required fields: a monotonic id, a date, a severity, a status, a one-line lesson, an owning surface, at least one source, and an occurrences list. The id increments monotonically and is never reused, even after pruning. Status is drawn from the closed enum {open, promoted, declined, pruned}; entries are never deleted — pruning is a status change and version control is the archive. Severity may be raised on recurrence but never silently lowered."
  governance: "Owner: the operator (or the gated agent acting under operator approval) who maintains the store. Status transitions are operator-gated: open → promoted | declined, and open | declined → pruned. Adding a new status value, changing the identity key, or permitting deletion of an entry is a schema change requiring deliberate review — the whole dedup and audit guarantee rests on the identity key and the no-delete invariant. A lesson with no traceable source is invention and gets no entry."
  recovery: "Owning-surface misidentification (the fix went to the wrong file, or a declined promotion signals the surface was misread) → append a correcting occurrence or open a new entry under the corrected identity; do not rewrite the original. Duplicate entries for one identity discovered after the fact → merge occurrence dates into the lower-id entry and prune the duplicate via status change, never deletion. Store growth beyond the pruning threshold → run an operator-approved pruning pass (surface no longer exists, superseded elsewhere, or stale singleton past the age bound), flipping status to pruned while the entry stays in the file."
tags:
  - "extracted-artifact"
  - "template"
  - "lesson-store"
  - "append-only"
  - "owning-surface"
  - "self-improvement"
---

# Lesson Store Entry Schema

**Source:** [[append-only-lesson-store-owning-surface-identity]]
**Form:** template
**Extraction date:** 2026-07-13

A fillable schema for a single entry in a **central, cross-cutting lesson store** — one durable home for operational lessons where each entry's identity is the pair *(owning surface, failure pattern)*. This is the storage half of a self-improvement loop: the promotion half reads it. It is distinct from a per-skill co-located lessons log — the store is one file that spans every surface, keyed for mechanical dedup, and carries a status lifecycle an operator advances.

## Variables

| Variable | Type | Description |
|----------|------|-------------|
| `{{SEQ}}` | integer | Monotonic sequence number. Increments by one across the whole store; never reused, even after an entry is pruned. Rendered as `L-<SEQ>`. |
| `{{DATE}}` | date (YYYY-MM-DD) | The date the entry was first created. Recurrences add to Occurrences, not to this field. |
| `{{SEVERITY}}` | enum `high` \| `normal` | `high` = data loss, governance breach, or user-visible failure. May be raised on recurrence; never silently lowered. |
| `{{STATUS}}` | enum `open` \| `promoted` \| `declined` \| `pruned` | Lifecycle state. New entries start `open`. Transitions are operator-gated (see Variation Axis). |
| `{{LESSON}}` | one line | What went wrong and the rule that prevents it — a single sentence pairing the failure with its preventing rule. |
| `{{OWNING_SURFACE}}` | path | The workspace path that, if edited, prevents recurrence. Half of the entry's identity key. |
| `{{SOURCE}}` | one or more references | At least one of: session ref, commit sha, or artifact path. An entry with no traceable source is invention and is not written. |
| `{{OCCURRENCES}}` | list of dates | Every date this identity was observed, first date included. A recurrence appends here — it never creates a second entry. |

---

## Body

Append the following block to the central lesson-store file (one block per lesson identity). Fill every field — all are required.

```markdown
## L-{{SEQ}} · {{DATE}} · {{SEVERITY}} · {{STATUS}}

- **Lesson:** {{LESSON}}
- **Owning surface:** {{OWNING_SURFACE}}
- **Source:** {{SOURCE}}
- **Occurrences:** {{DATE}}[, {{RECURRENCE_DATE}} ...]
```

**Worked example:**

```markdown
## L-12 · 2026-07-06 · normal · open

- **Lesson:** Skill description kept missing the bare-filename invocation idiom, so the resume command was described instead of given literally; state the literal `cat <path>` line in the skill.
- **Owning surface:** .claude/skills/resume/SKILL.md
- **Source:** session-141, commit a1b2c3d
- **Occurrences:** 2026-07-06, 2026-07-07, 2026-07-08, 2026-07-08, 2026-07-09, 2026-07-09, 2026-07-10, 2026-07-10, 2026-07-11, 2026-07-11
```

The example carries ten occurrence dates on a single entry — that is the dedup rule doing its job: the same *(owning surface, failure pattern)* identity recurred ten times and accumulated evidence on one entry rather than spawning ten near-duplicates.

---

## Usage

1. **Before writing, resolve identity.** Determine the *(owning surface, failure pattern)* pair. The owning surface is the path that, if edited, prevents recurrence — not merely where the failure was observed.
2. **Check for an existing entry with the same identity.** If one exists, append today's date to its Occurrences list and stop. Do **not** create a second entry. If severity has escalated, raise it on the existing entry.
3. **If the identity is new, allocate the next `L-<SEQ>`.** Take the highest existing seq and add one; never reuse a number, even one freed by a pruned entry.
4. **Require a source.** If no session ref, commit sha, or artifact path can be named, the observation is untraceable — do not write an entry.
5. **Render the block** with `{{STATUS}}` = `open` and today's date in both the header and Occurrences.

Render this template at the moment a failure or correction is observed — the store is written to as observations happen, not batched at session end.

---

## Variation Axis

What drives different renderings and lifecycle movement:

- **Status lifecycle (operator-gated).** The only permitted transitions are `open → promoted | declined` and `open | declined → pruned`. A promoted lesson has driven a system change; a declined one was reviewed and rejected (often signalling the owning surface was misidentified); a pruned one is retired but retained. Entries are never deleted — version control is the archive.
- **Severity escalation.** `normal` entries may be raised to `high` when a recurrence reveals data loss, a governance breach, or a user-visible failure. Severity is monotonic upward within an entry's life; it is never silently lowered.
- **Recurrence vs. new identity.** The single most consequential rendering decision: a same-identity observation appends a date; a genuinely new *(owning surface, failure pattern)* pair allocates a new entry. Collapsing distinct identities loses signal; splitting one identity into N entries (the failure mode this schema exists to prevent) destroys the dedup guarantee.
- **Growth management.** When open entries exceed the store's threshold (~50 in the reference implementation), an operator-approved pruning pass flips stale singletons, superseded lessons, and dead-surface entries to `pruned` status — a status change, never a deletion.

## Contract

### Preconditions
A single central lesson-store file exists (or is being created) as the append-target for operational lessons across all surfaces — not a per-tool or per-session file. An operator (human or gated agent) can advance a lesson's status. Every candidate lesson can name at least one traceable source (session ref, commit sha, or artifact path); untraceable observations are excluded by construction.

### Invariants
Each entry's identity is the pair (owning surface, failure pattern) — the owning surface being the path that, if edited, prevents recurrence. A recurrence of the same identity appends a date to the existing entry's Occurrences list; it never creates a second entry. Every entry carries all required fields: a monotonic id, a date, a severity, a status, a one-line lesson, an owning surface, at least one source, and an occurrences list. The id increments monotonically and is never reused, even after pruning. Status is drawn from the closed enum {open, promoted, declined, pruned}; entries are never deleted — pruning is a status change and version control is the archive. Severity may be raised on recurrence but never silently lowered.

### Governance
Owner: the operator (or the gated agent acting under operator approval) who maintains the store. Status transitions are operator-gated: open → promoted | declined, and open | declined → pruned. Adding a new status value, changing the identity key, or permitting deletion of an entry is a schema change requiring deliberate review — the whole dedup and audit guarantee rests on the identity key and the no-delete invariant. A lesson with no traceable source is invention and gets no entry.

### Recovery
Owning-surface misidentification (the fix went to the wrong file, or a declined promotion signals the surface was misread) → append a correcting occurrence or open a new entry under the corrected identity; do not rewrite the original. Duplicate entries for one identity discovered after the fact → merge occurrence dates into the lower-id entry and prune the duplicate via status change, never deletion. Store growth beyond the pruning threshold → run an operator-approved pruning pass (surface no longer exists, superseded elsewhere, or stale singleton past the age bound), flipping status to pruned while the entry stays in the file.
