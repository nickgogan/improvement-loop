---
title: "Pruning Is a Status Change, Never a Deletion"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "append-only-lesson-store-owning-surface-identity"
extraction_date: "2026-07-13"
last_change_session: 146
last_change_report: "session-persistence-and-memory.harvest-queue"
identification_report: "session-persistence-and-memory.harvest-queue.md::append-only-lesson-store-owning-surface-identity::rule::pruning-is-status-change-never-deletion"
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams maintaining a durable lesson store or knowledge record where resolved entries must remain readable as the historical account, not vanish"
    - "self-improvement loops whose promotion pipeline needs to tell 'reviewed and rejected' apart from 'never seen' — a distinction deletion would erase"
    - "any append-with-lifecycle record that grows unbounded and needs a bounded-growth mechanism that does not sacrifice the audit trail"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "operate"
  reversibility: "low — once deletion is permitted the record can no longer prove what was reviewed-and-retired versus never-recorded; restoring that distinction means reconstructing history from version control"
  auditability: "high — compliance is a field check plus a diff check: every entry retains an id and a status from a closed enum, and version-control diffs show status flips and additions but no removed entries"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "One production lesson store enforces this: resolved entries stay in the file as the durable record with status advanced to pruned, all four statuses observed in use across 20 entries. One deliberate carve-out was documented — a sibling candidates file permits operator-gated deletion of entries fully banked elsewhere — precisely to keep the lesson store itself status-change-only. No local adoption yet."
contract:
  preconditions: "The record is a lesson store, knowledge log, or equivalent durable account with per-entry lifecycle state. Each entry carries a status field drawn from a closed enum that includes a terminal 'retired' value (e.g., pruned). An operator (or gated agent under operator approval) authorizes lifecycle transitions. Version control tracks the file."
  invariants: "No entry is ever removed from the record. Retiring an entry is a status transition to the terminal retired value (open | declined → pruned), leaving the entry in the file as the durable record. Entry ids are never reused, even after an entry is pruned. The status field is mutable by design — a resolved entry's status advances through its lifecycle — which is exactly what distinguishes this record from an immutable run log or audit log where no mutable status field may exist. Growth is bounded by pruning (a status change), never by deletion."
  governance: "Owner: the operator who maintains the record. Deletion of any entry is forbidden without an explicit, documented carve-out ruled entry-class by entry-class — the default is status-change-only. Any such carve-out (e.g., permitting deletion of entries fully banked in another store) must be named in the record's own governance and must not apply to the lesson store proper. Adding a status value or altering the transition set is a schema change requiring review. Contrast with the append-only run-log invariant, which forbids a mutable status field entirely: that rule governs event streams; this rule governs lifecycle records — do not apply one to the other."
  recovery: "Entry deleted in error → restore it from version control and re-apply the status it should have carried; never silently re-create it with a fresh id. Record grown past its bound → run an operator-approved pruning pass flipping stale, superseded, or dead-surface entries to pruned; the file keeps every entry. Deletion carve-out found leaking into the lesson store → treat as a governance breach, restore any removed entries from version control, and re-scope the carve-out to its intended sibling record."
tags:
  - "extracted-artifact"
  - "rule"
  - "lesson-store"
  - "append-only"
  - "lifecycle"
  - "self-improvement"
---

# Pruning Is a Status Change, Never a Deletion

**Source:** [[append-only-lesson-store-owning-surface-identity]]
**Form:** rule
**Extraction date:** 2026-07-13

## Condition

A durable lesson store (or equivalent knowledge record) holds entries that carry a per-entry lifecycle status. Over time some entries become resolved, stale, superseded, or attached to a surface that no longer exists, and the store grows past a comfortable size. The operator wants to keep the store bounded **without** losing the historical account of what was recorded and how it was resolved.

Scope of application: **lifecycle records** — lesson stores, gated knowledge logs, promotion registers — where an entry's status is a first-class, mutable field that advances through a closed lifecycle. This rule deliberately does **not** govern append-only event streams or audit logs; those are a different object governed by their own no-mutable-status invariant.

## Action

**Required:**
- Retire an entry by **advancing its status** to the terminal retired value (`open | declined → pruned`). The entry stays in the file as the durable record.
- Keep the **status field mutable** — a resolved entry's status is expected to move through its lifecycle. This mutability is intentional and is the defining difference from an immutable run/audit log.
- Bound growth through a **pruning pass**: an operator-approved sweep that flips qualifying entries (surface no longer exists, superseded elsewhere, or stale singleton past the age bound) to the retired status.
- Preserve entry **ids permanently** — a pruned entry's id is never reused; the next entry takes the next unused number.

**Forbidden:** Deleting an entry from the store. Reusing the id of a pruned entry. Bounding store growth by removal rather than status change. Applying this rule to an append-only run log or audit log (which forbid a mutable status field) — the two are opposite primitives.

## Boundary

Enforced at the record's write path (what operations the maintainer may perform on an entry) and at any pruning tooling (which must flip status, not remove lines). Applies for the whole life of the store. A single deliberate carve-out — operator-gated deletion of entries *fully banked in another store* — is permitted only when named explicitly in the record's governance and only for the carved-out entry class; it must not touch the lesson store proper.

## Enforcement

- **Mechanism:** The maintaining tool or procedure exposes a status-transition operation, not a delete operation, on lesson entries. Version control provides the secondary check: diffs must show status changes and additions, never removed entries (outside a documented carve-out class).
- **Check (deterministic):** `(entry_count_never_decreases_except_documented_carveout == true) AND (every_retirement_is_a_status_flip_to_pruned == true) AND (no_pruned_id_is_reused == true) AND (status_field_is_mutable == true)`. Any branch false → violation.
- **Violation response:**
  - *Entry removed from the store:* restore it from version control, re-apply its correct status; investigate whether a deletion path leaked in from a carve-out class.
  - *Pruned id reused:* re-number the offending new entry to the next unused id; the pruned entry keeps its original number.
  - *Growth "managed" by deletion:* revert the removals from version control and re-run the pass as status flips.
- **Prose-enforced residue:** the carve-out boundary (which entry classes, if any, permit deletion) is a governance statement, not a tool-shape guarantee — it must be written in the record's governance and checked in review.

## Rationale

A lesson store earns its value from telling *"seen and resolved"* apart from *"never seen."* Deletion collapses that distinction: a removed entry is indistinguishable from one that was never recorded, so the promotion pipeline loses the memory that a lesson was already reviewed and declined — and the same failure gets re-litigated. Keeping resolved entries in place, with a status that says how they resolved, is what makes the store a durable record rather than a scratchpad.

The subtlety is that this is the **inverse** of the append-only run-log invariant. A run log forbids a mutable status field — lifecycle state there is recorded as appended events in an immutable stream. A lesson store *requires* a mutable status field — the whole point is that an entry's disposition advances under operator approval. Same family (append-heavy, deletion-averse), opposite primitive on the status field. Conflating the two — applying no-mutable-status to a lesson store, or applying status-change-only to a run log — breaks whichever record it is misapplied to.

Growth is real: an append-with-lifecycle record never shrinks on its own. Pruning-as-status-change is the load-bearing answer — it bounds the *open* working set while preserving the full account, with version control as the archive of record.

## Failure Modes

- **Deletion creeps in for "cleanup."** An operator prunes by deleting lines to keep the file short; the reviewed-vs-never-seen distinction silently erodes. Mitigation: tool exposes status-flip only; review diffs for removed entries.
- **Carve-out leaks.** A documented deletion allowance for a sibling record gets applied to the lesson store. Mitigation: scope carve-outs to a named entry class and check them in governance review.
- **Rule misapplied to a run log.** A maintainer adds a mutable status field to an append-only event stream because "the lesson store has one." Mitigation: keep the two objects and their opposite status-field primitives explicitly distinguished; this rule governs lifecycle records only.
- **Id reuse after pruning.** A pruned entry's number is recycled, breaking monotonic identity and any cross-reference to the old id. Mitigation: allocate ids from the high-water mark, never from freed numbers.

## Contract

### Preconditions
The record is a lesson store, knowledge log, or equivalent durable account with per-entry lifecycle state. Each entry carries a status field drawn from a closed enum that includes a terminal 'retired' value (e.g., pruned). An operator (or gated agent under operator approval) authorizes lifecycle transitions. Version control tracks the file.

### Invariants
No entry is ever removed from the record. Retiring an entry is a status transition to the terminal retired value (open | declined → pruned), leaving the entry in the file as the durable record. Entry ids are never reused, even after an entry is pruned. The status field is mutable by design — a resolved entry's status advances through its lifecycle — which is exactly what distinguishes this record from an immutable run log or audit log where no mutable status field may exist. Growth is bounded by pruning (a status change), never by deletion.

### Governance
Owner: the operator who maintains the record. Deletion of any entry is forbidden without an explicit, documented carve-out ruled entry-class by entry-class — the default is status-change-only. Any such carve-out (e.g., permitting deletion of entries fully banked in another store) must be named in the record's own governance and must not apply to the lesson store proper. Adding a status value or altering the transition set is a schema change requiring review. Contrast with the append-only run-log invariant, which forbids a mutable status field entirely: that rule governs event streams; this rule governs lifecycle records — do not apply one to the other.

### Recovery
Entry deleted in error → restore it from version control and re-apply the status it should have carried; never silently re-create it with a fresh id. Record grown past its bound → run an operator-approved pruning pass flipping stale, superseded, or dead-surface entries to pruned; the file keeps every entry. Deletion carve-out found leaking into the lesson store → treat as a governance breach, restore any removed entries from version control, and re-scope the carve-out to its intended sibling record.
