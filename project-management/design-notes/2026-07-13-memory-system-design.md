---
title: "Memory-system design — the engine as one big agent, decomposed by its own subsystems"
id: "memory-system-design-2026-07-13"
type: "design-note"
category: "memory-architecture"
target_system:
  - "improvement-loop"
stage: "review"
created: "2026-07-13"
updated: "2026-07-13"
author: "claude"
source_dd:
  - "DD-116"
tags:
  - "design-note"
  - "memory"
  - "self-improvement"
  - "restructure-program"
---

# Memory-System Design — One Big Agent, Subsystem Decomposition

**Status: brainstormed inline with Nick (session 142); rulings below are his, recorded
at decision time.** Supersedes the residue-triage scoping of
`2026-07-12-second-brain-proposal.md` (rejected in its session-141 ruling); absorbs
IB-172, the G9 encounter question, and the calibration-registry proposal (P1).

**Plain English.** The IL loop is treated as one agent with a memory system decomposed
by the engine's own subsystems. The centerpiece is a CareerBuddy-style self-improvement
loop: an append-only lesson store plus a demand ledger (query/intent log), one scan-mode
review loop over both, and a human-gated promotion pipeline that turns recurring
observations into system changes. Markdown + git stays canonical everywhere; every
derived layer is disposable and rebuildable.

Deliberation inputs: the four research reports in `operations/research-reports/`
(2026-07-12/13), the CareerBuddy `ops-self-improve` finding cluster (7 findings via
`research-sources/careerbuddy-ops-self-improve.md`), and a query/intent-logging web
sweep (session 142; Rasa CDD / Dialogflow fallback analytics / zero-result-query mining
as lineage; Datadog `/agent-observability-session-classify` + LangSmith Engine as 2026
agent-scale practice; claude-mem-lite hooks→SQLite and Gbrain reports as within-class
persistence precedent).

---

## 1 — Settled substrate (research-converged, not debated)

- Markdown + git canonical; any index derived, disposable, gitignored, rebuildable.
- Two layers with gated promotion: append-only capture + curated distillate; scheduled
  distillation, never inline curation mid-task; targeted deltas, never whole-store LLM
  rewrites (ACE context-collapse); never batch approval.
- Memory is a hint, not an authority: provenance per entry; raw observations never
  share a bucket with behavioral instructions.
- Retirement = status change or folder move, never deletion; git is the archive. No
  TTL machinery (decay is unsolved everywhere; supersession + editorial pruning is the
  frontier norm and what git gives free).

## 2 — The self-improvement loop (ruled: build as specced)

**Store** at `operations/self/` — git-tracked standing files, never dated per run:

| File | Role |
|---|---|
| `lessons.md` | Append-only lessons. Identity = (owning surface, failure pattern); recurrence appends a date to Occurrences, never a duplicate. Entry: `## L-<seq> · date · high\|normal · open\|promoted\|declined\|pruned` + one-line Lesson + Owning surface + Source + Occurrences. Untraceable lesson = invention, no entry. |
| `query-log.md` | Demand ledger. One row per incoming intent: `Q-<seq> · date · query gist · route (skill/agent/disposition or ad-hoc) · why · served\|partial\|unserved`. Multi-intent queries get one row each. |
| `proposal-log.md` | Append-only audit of every promotion: `P-<seq> · date · L-<seq> · applied\|declined` + proposal/surface/diff-summary/grade. Rollback = git revert + new P-row; history never rewritten. |
| `retro-latest.md` | Scan-mode report, overwritten each run (history in git). |

Plus a **gitignored capture buffer** (`operations/self/.query-capture.jsonl`) fed by
the hook (§4). No `eval-candidates.md` in v1 — the demand ledger carries eval material
(phrasing + route + outcome); harvest into eval sets when Phase 4/5 harness work starts.

**Skill** — one skill, four modes (capture / scan / promote / status), Owner-owned.

**Thresholds (tunable, rationale recorded):** N=2 occurrences normal severity, N=1
high (data loss, governance breach, user-visible failure). **Threshold gates agent
autonomy, never Nick's direction** — operator-directed promotion below threshold is
always allowed. Severity never silently lowered.

**Promotion pipeline** (per lesson at threshold): draft minimal edit against the owning
surface → shadow sandbox (copy to temp, apply, run the surface's own validators;
fail-closed) → separate-context grade (fresh assessor context; binary rubric: grounded /
minimal / effective / non-regressive — generator-assessor rule already standing) →
**per-proposal Nick gate, never batch** → append-only log. Applying commit carries
`Refs: ops-self L-<seq>`. Governance surfaces are proposal-only without exception. A
declined proposal is signal (often: owning surface misidentified), not failure.

**Dispatch table** — DD-116 routing generalized into a maintained table: decision→DD,
pattern→knowledge/, work→IB, doc drift→`/maintain-docs`, operational lesson→store
(residual class, owned end-to-end). Classification keys on owning surface ("which file,
if edited, prevents recurrence"), not topic. Unknown class → lesson + flag Nick; never
invent a route. Table amendments go through the promotion gate.

**Deterministic checker** (`store_check.py`): schema validity, occurrence counts,
PROMOTE flags at threshold, `Q-<n>` reference existence, growth bound (~50 open lessons
→ gated pruning pass). Wired into the existing pre-commit hook.

## 3 — Demand ledger rationale (ruled: build)

Failure-side telemetry (lessons) misses demand-side gaps: an unserved intent usually
doesn't look like a failure — the agent handles it ad-hoc, nothing errors, nothing is
recorded. The ledger is the zero-result-query pattern ported to the engine: log query +
route + why + outcome; scan mode surfaces recurring unserved themes; at threshold they
become IB proposals through the same gate ("expand the system to serve this intent?" is
a per-proposal Nick decision). Strategic bonus: the ledger accumulates the ground-truth
corpus (real phrasings → correct route → outcome) the future implicit-routing harness
needs as its eval set.

**Lessons reference queries** (ruled): `Q-<seq>` becomes a fourth accepted value in the
lesson Source field. One-directional (lesson → query), optional — only when the lesson
originated from an ask. No back-references, no join maintenance beyond the checker's
existence check; reverse lookup is `rg "Q-12" lessons.md`.

## 4 — Capture timing (ruled: both), and the hook question

Division of labor — **hooks for determinism, agent for judgment**:

| Moment | Mechanism | Why |
|---|---|---|
| Query capture | `UserPromptSubmit` hook → one raw line to the capture buffer | Mechanical append; no LLM; can't be forgotten. First concrete instance of the North-Star harness layer (harness-enforced, not agent-remembers). |
| Lesson capture, inline | Agent (capture mode) at the moment a failure is noticed | Authoring a lesson requires judgment (failure pattern + owning surface); hooks can't do it. |
| Lesson capture, sweep | Lessons-check step added to `/session-handoff` | Session close catches what inline capture missed, without per-task friction. |
| Store validation | `store_check.py` in the pre-commit hook | Deterministic; runs with the existing frontmatter/FOUNDATIONS/PROGRESS checks. |

## 5 — Scan mode: one review loop (ruled: fold feedback/ in)

Scan reads **all observation sources in one retro**: the capture buffer (distill →
`query-log.md` rows), `feedback/` (human-driven funnel — folded in; `/process-feedback`
retires as a standalone skill, roster change flagged), open lessons, recent run reports
in `operations/`. Each item classifies via the dispatch table; recurring unserved
intents and at-threshold lessons emit PROMOTE flags for promote mode. One loop, one
cadence — the anti-graveyard rule: no log gets its own unread reflection ritual.

**First scan run = the SL backfill** (ruled: distill-then-close): mine the frozen SL
corpus once — calibration numbers → `operations/references/calibration-registry.md`
(per-topic sections, each with a **named consumer skill + read-moment**; raw numbers
only, never behavioral instructions; on-demand read, never cold-start) — lesson-shaped
residue → `lessons.md`. Then the SL corpus closes as a read-only archive with no
standing reader. This discharges the drop-inventory (G9 encounters become capture-mode
lessons; the Occurrences tally is the recurrence-noticing mechanism).

## 6 — Other subsystems

- **Knowledge management (KB + retrieval).** Vector search on `research-findings/`
  (907 files) remains **designed in** per the session-141 refinement — a component of
  this design, not trigger-gated. Implementation shape (lean: hybrid FTS5 + local
  embeddings, one gitignored file under `app/`, rebuild-on-demand) — **parked by Nick
  (session 142)**; the component stands, the implementation choice is deferred.
- **Task processing (DDs + IB).** Cruft audit + DD↔IB coupling map + queue-structure
  study (BMAD project structure, superpowers/GSD task queues) — **deferred to converge
  with the wave-3 named-deps gap-check** (same reading list, one pass).
- **Agent layer.** One big agent → one shared store; no per-agent memory. Agent-private
  `reflections/` stay as-is (feed `/solicit-proposals`, a different cadence).
- **Docs / portability.** CareerBuddy `onboarding/` pattern + portable-kernel tie —
  defers to Phase 4/5 where the kernel work lives.

## 7 — Archiving policy (per layer, positive-space)

| Layer | Rule |
|---|---|
| Working (PROGRESS/CLAUDE chain) | Line caps + `/session-handoff` compaction (exists) |
| DDs | DD-44 supersession (exists; ahead of frontier practice) |
| IB | Done items move to `archive/` at milestone close (new) |
| Lessons | Status change only; ~50 open triggers gated pruning pass (new) |
| Findings | Dated evidence + existing sweeps (`/detect-drift`, `/reassess-priorities`); no TTL |
| Run reports | Move to `archive/` when their consuming phase closes (new) |
| HISTORY.md / git | Governance memory — append-only is correct; keep forever |
| Frozen SL | Closed archive after the one-time distill (§5) |

## 8 — Non-goals

No world-KB, no autonomous ingestion crons, no TTL machinery, no per-agent stores, no
`eval-candidates.md` (v1), no OKF native adoption (export target only, later), no
whole-store LLM rewrites ever.

## 9 — Ship order

1. `operations/self/` store + 4-mode skill + `UserPromptSubmit` hook + `store_check.py`
   pre-commit wiring + `/session-handoff` lessons-check step.
2. First scan run: SL distill (calibration registry + lesson residue) → close SL corpus.
3. Parked/deferred: findings search implementation (parked); DD/IB audit +
   queue-structure study (waits on wave-3 gap-check); docs/portability (Phase 4/5).

## Open items

- Findings-search implementation shape — parked (Nick, session 142).
- `/process-feedback` retirement mechanics (absorb into scan mode) — execute with ship
  step 1; roster/docs update via `/maintain-docs`.
- Kill criterion (Q-A of the superseded proposal): scan mode's own telemetry answers
  it — a ledger/store section never consumed across N scans is flagged by the checker
  for a gated pruning decision. Adopted implicitly; N tunable.
