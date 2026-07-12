---
name: 'Append-Only Lesson Store Keyed by Owning Surface'
summary: 'A central, markdown-native, append-only store of operational lessons where each entry''s identity is the pair (owning surface, failure pattern). Recurrence appends a date to the existing entry — never a duplicate. Entries carry a status lifecycle (open → promoted/declined/pruned) and are never deleted; pruning is a status change and git is the archive. CareerBuddy runs this in production: 20 lessons and 16 gated proposals accumulated in ~5 days of sessions.'
implementation_notes: 'Directly applicable to the MetaSystem engine — Phase 2 of its restructure program will size a second-brain-for-operations against this store model; IB-172 (layered memory architecture) is the related backlog item. The retired System Log corpus is read-only feedstock the store could supersede: SL entries lacked owning-surface keying and a promotion lifecycle, which is exactly what made them terminal rather than actionable.'
category: Context Engineering
evidence_strength: Medium (practitioner-documented, single production system with live store evidence)
adoption_status: Not Yet Started
priority: P1 (Direct Adoption)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-ops-self-improve.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: raw
consumed_by: []
tags:
- lesson-store
- append-only
- owning-surface
- self-improvement
- memory
---

# Append-Only Lesson Store Keyed by Owning Surface

## Why It Matters

Agent systems repeat the same operational mistakes because observations die with the session. This pattern gives every lesson one durable home, one identity, and one lifecycle — so a recurring failure gets *stronger evidence on one entry* instead of scattered duplicates, and the system can tell "seen once" from "seen ten times" mechanically. It is the storage half of a self-improvement loop: the promotion half reads it.

## What It Is

CareerBuddy's `ops-self-improve` skill maintains a central store at `ops/self/` — five git-tracked standing files, never dated per run:

- `lessons.md` — append-only lesson entries (the core).
- `eval-candidates.md` — real (never invented) skill-invocation phrasings with verdicts, raw material for eval sets.
- `proposal-log.md` — append-only audit log of every promotion attempt, applied or declined.
- `retro-latest.md` — the scan-mode report, overwritten each run (history lives in git; no dated files).
- `improve-backlog.md` — freeform non-failure polish items, exempt from the deterministic checker.

## How It Works

**Lesson identity is the pair (owning surface, failure pattern).** The owning surface is "the workspace path that, if edited, prevents recurrence." A recurrence of the same identity appends a date to the entry's **Occurrences** list — it never creates a second entry. Live evidence: lesson L-12 carries 10 occurrence dates on a single entry (a bare-filename invocation idiom the skill description kept missing).

**Entry schema (all fields required):** header `## L-<seq> · <date> · <high|normal> · <open|promoted|declined|pruned>`, plus one-line **Lesson** (what went wrong and the rule that prevents it), **Owning surface**, **Source** (session ref, commit sha, or artifact path — at least one), and **Occurrences**. An untraceable lesson "is invention and gets no entry."

**Rules with teeth:**
- `L-<seq>` increments monotonically; numbers are never reused, even after pruning.
- Severity: `high` = data loss, governance breach, or user-visible failure; may be raised on recurrence, never silently lowered.
- Status transitions only: `open → promoted | declined`, `open|declined → pruned`. Resolved entries stay in the file as the durable record — pruning is an operator-approved status change, never a deletion.
- Growth bound: pruning pass triggered when open lessons exceed ~50 (candidates: surface no longer exists, superseded elsewhere, stale singletons >90 days).
- One deliberate exception: `eval-candidates.md` allows operator-gated deletion of entries "fully banked elsewhere" — git is the archive; `lessons.md` remains status-change-only.

**Live store evidence (2026-07-06 → 07-11):** 20 lessons spanning skill descriptions, terminal pitfalls, memory files, and the store's own schema; all four statuses in use; lessons about the store itself (L-7, L-17, L-19) were captured in the store and fixed through its own gated promotion path — the loop maintains its own substrate.

## How It Could Fail

- Without the identity rule, one recurring idiom becomes N near-identical entries (CareerBuddy hit exactly this in `eval-candidates.md` before adding a dedup rule as L-19/P-15).
- Append-only files still grow; the ~50-open pruning trigger and section compaction are load-bearing, not optional.
- Owning-surface misidentification sends the fix to the wrong file — CareerBuddy treats a declined proposal as signal the surface was misidentified.
