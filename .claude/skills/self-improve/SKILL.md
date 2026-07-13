---
name: self-improve
description: >-
  The engine's self-improvement loop (IB-176): append-only lesson store + demand
  ledger at operations/self/, one scan-mode review loop, and a human-gated promotion
  pipeline that turns recurring observations into system changes. Four modes:
  capture (append a lesson or query-log row at the moment of observation), scan
  (one retro over the capture buffer, feedback/, open lessons, and recent run
  reports — absorbs the retired /process-feedback), promote (draft → shadow-sandbox
  → fresh-context grade → per-proposal Nick gate), status (store counts + flags).
  Owner-owned (DD-86). Use when a failure or unserved intent is noticed ("capture a
  lesson"), for the periodic retro ("run a scan", "self-improve scan"), when
  store_check.py flags PROMOTE ("run promote mode"), or to check store health
  ("self-improve status").
user-invocable: true
allowed-tools: Read Grep Glob Write Edit Bash Agent
argument-hint: "capture | scan | promote [L-<seq>] | status"
---

# Self-Improve — the Engine's Memory-Backed Improvement Loop

One skill, four modes, over the store at `systems/improvement-loop/operations/self/`
(`lessons.md`, `query-log.md`, `proposal-log.md`, `retro-latest.md`, plus the
gitignored `.query-capture.jsonl` buffer fed by the `UserPromptSubmit` hook).
Design of record: `project-management/design-notes/2026-07-13-memory-system-design.md`.

**Cognitive disposition: Owner.** Evidence over invention; provenance per entry;
memory is a hint, not an authority.

## When to use

- A failure, mistake, or unserved intent is noticed mid-work → **capture**
- Periodic retro, `/system-review` step 3, or "process feedback" → **scan**
- `store_check.py` printed a PROMOTE flag, or Nick directs a promotion → **promote**
- Store-health question ("how many open lessons?") → **status**

Four modes share one skill deliberately (design-note ruling): they operate one store
under one identity contract and one dispatch table — splitting them would duplicate
that contract across four files.

## Standing rules (all modes)

1. **Append-only.** Lessons, query rows, and proposal rows are never edited or
   deleted — recurrence appends a date to Occurrences; retirement is a status
   change; rollback is git revert + a new P-row. `retro-latest.md` is the one
   overwrite-per-run file.
2. **Untraceable lesson = invention.** No Source (session ref, commit sha, artifact
   path, or `Q-<seq>`), no entry.
3. **Raw observations never share a bucket with behavioral instructions.** Lessons
   record what happened; only the promotion pipeline turns them into surface edits.
4. **Thresholds gate agent autonomy, never Nick's direction.** Normal severity
   promotes at 2 occurrences, high (data loss, governance breach, user-visible
   failure) at 1. Nick may direct promotion below threshold at any time. Severity is
   never silently lowered.
5. **Per-proposal Nick gate, never batch.** Governance surfaces (DDs, CHARTER,
   governance/) are proposal-only without exception.
6. **Targeted deltas, never whole-store rewrites** (ACE context-collapse class).
7. Entry/row schemas live in the store files' own headers; `store_check.py`
   (pre-commit) enforces them deterministically.

## Dispatch table

Classification keys on **owning surface** — "which file, if edited, prevents
recurrence" — not topic. Unknown class → capture a lesson + flag Nick; never invent
a route. Amendments to this table go through the promotion gate.

| Observation shape | Route |
|---|---|
| Decision-shaped (a choice was made or is needed) | DD (`/dd`) |
| Pattern-shaped (reusable design insight) | `knowledge/` |
| Work-shaped (deferred implementation) | IB item (`/ib`) |
| Doc drift (docs contradict reality) | `/maintain-docs` |
| Operational lesson (residual class — a failure with an owning surface) | `lessons.md`, owned end-to-end here |
| Unserved/partial intent (demand-side gap) | `query-log.md` row; recurring themes → IB proposal via promote mode |

## Mode: capture

At the moment a failure or unserved intent is noticed (inline), or when directed.

1. Classify via the dispatch table. Non-lesson shapes route out — do not also write
   a lesson unless there is a distinct operational failure.
2. For a lesson: Grep `lessons.md` for the owning-surface path to find an existing
   entry with the same (owning surface, failure pattern) identity. Match → append
   today's date to its Occurrences. No match → append a new `L-<seq>` entry (next
   seq, status `open`) per the file's entry contract.
3. For a demand observation outside the hook's reach (e.g. an intent surfaced
   mid-conversation): append a `Q-<seq>` row to `query-log.md`.
4. Run `python3 operations/kb-maintenance-scripts/store_check.py` and report any
   PROMOTE flags.

## Mode: scan

The one periodic retro — **the anti-graveyard rule: no log gets its own unread
reflection ritual**; everything is read here, on one cadence.

1. **Distill the capture buffer.** Read `.query-capture.jsonl`; collapse to one
   `query-log.md` row per distinct intent (multi-intent prompts get one row each):
   gist (not verbatim), route actually taken (skill/agent/disposition or ad-hoc),
   why, outcome `served|partial|unserved`. Then truncate the buffer.
2. **Read `feedback/`** (the human-driven funnel — this absorbs the retired
   `/process-feedback`): classify each item via the dispatch table, propose routes,
   note root cause where evident. Feedback items get a `triage_status` frontmatter
   stamp; they are closed only when their action lands.
3. **Read open lessons + recent run reports** in `operations/` (reports newer than
   the last scan). Classify anything lesson-shaped that inline capture missed.
4. **Emit PROMOTE flags:** at-threshold open lessons and recurring
   `partial`/`unserved` query themes.
5. **Write `retro-latest.md`** (overwrite): sources read, rows/lessons added,
   dispatch-routed items, PROMOTE flags, and store-health counts from
   `store_check.py --status`. Consumption telemetry: a store section never consumed
   across ~3 scans is flagged for a gated pruning decision.
6. Nothing beyond the store and the retro is modified in scan mode — routed items
   (DDs, IB, knowledge/) are proposed in the retro, executed only per the routes'
   own gates.

## Mode: promote

Per lesson at threshold (or Nick-directed below it). One lesson per pass through the
pipeline; never batch.

1. **Draft** the minimal edit against the lesson's owning surface. Minimal = the
   smallest diff that prevents recurrence.
2. **Shadow sandbox:** copy the surface to a temp dir, apply the edit, run the
   surface's own validators (frontmatter check, store_check, skill/agent contract
   checks — whatever governs that file). Fail-closed: any validator failure kills
   the proposal at this stage.
3. **Fresh-context grade:** dispatch to a separate assessor subagent
   (generator-assessor rule). It **consumes** exactly: the lesson entry, the drafted
   diff, the owning surface's current content, and the rubric — no other session
   context. It **produces** four binary verdicts + one-line rationale each:
   grounded (traces to the lesson's evidence) / minimal / effective (prevents the
   recurrence) / non-regressive. Any `no` → revise (at most 2 revise cycles, each
   re-sandboxed and re-graded) → still failing → decline.
4. **Nick gate:** present the proposal (lesson, diff, grade) for a per-proposal
   ruling. Governance surfaces stop here always. **Only an `applied` ruling writes
   the diff to the live surface; on `declined`, nothing is touched beyond the
   P-row and the lesson's status.**
5. **Log:** append a `P-<seq>` entry to `proposal-log.md` (`applied|declined`);
   update the lesson's status to `promoted`/`declined`. An applying commit carries
   `Refs: ops-self L-<seq>`. A declined proposal is signal — often a misidentified
   owning surface — not failure.

## Mode: status

Run `python3 operations/kb-maintenance-scripts/store_check.py --status`; report
counts, PROMOTE flags, growth-bound state (~50 open lessons → gated pruning pass),
and the date of the last scan (git log on `retro-latest.md`).

## Output shape

| Mode | Output |
|---|---|
| capture | Appended `L-`/`Q-` entry (or an Occurrences date), plus any PROMOTE flags from `store_check.py`, echoed to the user |
| scan | Overwritten `retro-latest.md` + new `query-log.md` rows + swept lessons; routed items are *proposed* in the retro, not executed |
| promote | One proposal presented at the Nick gate; then one `P-<seq>` row + one lesson status change (+ the surface diff, only if `applied`) |
| status | One-line counts + flags; no writes |

## Boundary conditions

**Halt:** shadow-sandbox validator failure kills the proposal at that stage
(fail-closed); an observation the dispatch table cannot classify becomes a lesson +
a Nick flag, never an invented route; if `store_check.py` itself errors, stop the
mode and report the error — do not write around a broken checker.
**Escalation:** governance surfaces (DDs, CHARTER, `governance/`) never pass the
gate autonomously; anything cross-system routes to Nick.
**Completion:** capture ends when the entry is written and flags are echoed; scan
ends when `retro-latest.md` is written; promote ends at the P-row; status is
read-only.
**Empty state:** empty buffer + empty `feedback/` + no new reports → scan is a
no-op; say so, update `retro-latest.md`'s date line only.
**First scan ever** = the one-time SL distill (design note §5) — mine the frozen
System Log corpus for calibration numbers (→
`operations/references/calibration-registry.md`, raw numbers only, each section
with a named consumer skill + read-moment) and lesson-shaped residue (→
`lessons.md`), then the SL corpus closes as a read-only archive.
**Capture-buffer lines that aren't engine work** — still one row each; route
`ad-hoc`, outcome per reality. The ledger measures demand, not engine flattery.

## Constraints

- **Safety-critical: yes** (writes cross-file ops state; promote mode edits live
  surfaces). HITL boundary: promote-mode edits land only after the per-proposal
  Nick gate; everything else touches only `operations/self/`. All writes are
  git-reversible.
- **Tool tiering:** the flat `allowed-tools` grant is intentional (one skill file),
  but per mode: status is read+Bash only; capture/scan add store writes; **only
  promote** may touch a surface outside `operations/self/` (and only post-gate).
  The fresh-context assessor subagent gets a strict subset: Read + the sandbox
  validators — no Write/Edit on live surfaces.
- Store writes go through Edit/Write on the specific entry — never regenerate a
  store file wholesale.
- This skill never writes System Log entries (retired producer, session 138).
