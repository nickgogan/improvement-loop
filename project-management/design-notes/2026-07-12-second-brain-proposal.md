---
title: "Second-brain proposal — minimum mechanism for the DD-116 routing residue (IB-172 near-term slice)"
id: "second-brain-proposal-2026-07-12"
type: "design-note"
category: "memory-architecture"
target_system:
  - "improvement-loop"
stage: "review"
created: "2026-07-12"
updated: "2026-07-12"
author: "claude"
source_dd:
  - "DD-116"
tags:
  - "design-note"
  - "second-brain"
  - "memory"
  - "restructure-program"
---

# Second-Brain Proposal — Minimum Mechanism for the DD-116 Routing Residue

**Plain English.** After the System Log retired, learnings route by shape (decision → DD,
pattern → knowledge/, work → IB). The substrate audit found what that routing drops:
measurement numbers that would ground future recalibration, and (potentially) the
Librarian's boundary-case encounters (gate G9). The question Nick gates: does that loss
justify any store mechanism beyond the routing rule? **Recommendation: almost none.**
One small calibration registry file for the numbers — because they have named incidents
and nameable readers — and an explicit *defer* ruling for encounters, whose observed
base rate is zero. No new memory layer, no ingestion automation, no derived database.
The full layered-memory architecture stays in IB-172 with concrete promotion triggers.

Grounding: a Librarian Builder-mode consult over the IB-172 finding cluster (citations
inline below as `slug`), and a web sweep of frontier memory architectures (Hermes,
OpenClaw Dreaming, Gbrain, OKF v0.1, MemGPT/Letta, Mem0, A-MEM, LongMemEval, ACE,
Anthropic memory tool). Both tracks converged independently on the same shape.

---

## 1 — The gate question, sized honestly (Rule 11)

The drop-inventory, from the substrate audit:

| Item | Evidence | Recurrence? |
|---|---|---|
| Stranded calibration data | ~10 SL entries routed their *fix* but left their *measurements* entry-local. Three verified, consumer-nameable examples: crosslink error rates by link type (contradicts ~0% / enables ~40% / same-problem ~60% → `/finding-crosslink` threshold discipline), transcript-extraction 8× density hierarchy (→ transcript-first pipeline calibration), YAML defect-class taxonomy A/B/C (→ DD-114 hook context) | **Yes — 3+ verified incidents** |
| Boundary-case encounter records (G9) | 13-type taxonomy exists (`operations/references/librarian/boundary-cases.md`); persistence destination retired with the SL | **No — zero written in 27+ sessions** |
| IB closure-note overflow | Pre-DD-116 IBs absorbed session reports and rulings (IB-155, IB-159–166, IB-164 amendment) | Resolved — DD-116 routing now covers this class |

Rule 11 verdict per item: calibration data passes (recurring, multiple consumers,
observable cost of absence — recalibration would re-measure blind). Encounters fail
(zero base rate is the *absence* of recurrence evidence). Overflow needs no mechanism.

## 2 — The questions we should be asking (frontier-derived, answers inferred)

Distilled from 18 design questions grounded in 2025–26 frontier systems. Inferred
answers below; the three genuinely contested ones are pulled out in §5.

**Build vs don't-build**

| Question | Inferred answer for the engine |
|---|---|
| Can you name 3 incidents the store would have prevented? (LongMemEval) | Yes for calibration (§1); no for encounters → build for the first only |
| Who reads it, at what exact workflow moment? ("unread memory = no memory" — the strongest discriminator) | Each registry section must name its consumer skill and read-moment; a section with no consumer is debt, not memory |
| Is git + existing artifacts already the memory? (Letta context-repos, OKF) | Yes for episodes — git/HISTORY/frozen SL corpus are the free episodic layer. The only residue is what must be **tallied across sessions**, not found: measurements. That is the registry's entire scope |
| Weekly curation cost, paid by whom? | ~Zero at this size; hard scope cap (below) replaces curation machinery |
| Kill criterion decided before building? (OpenClaw recall gates) | Contested — §5, Q-A |

**Write path**

| Question | Inferred answer |
|---|---|
| Inline vs offline writes? | Write-back at decision time (`write-back-discipline-memory-is-not-the-brain`) — the session that produces a measurement writes the row. No cron, no Dreaming-style sweep |
| What earns promotion? | The evergreen test (`evergreen-vs-volatile-ingestion-rule`): only measurements that ground a *future* decision enter; per-instance events don't |
| Episodic/semantic split? | Already exists: git + HISTORY + frozen SL = episodic; DDs + knowledge/ + registry = curated. Nothing new needed |
| Size cap on the always-loaded layer? | Registry is **never cold-start-loaded** — on-demand read only. The engine's pinned layer (PROGRESS.md, 150/250 pre-commit cap) already implements the frontier's hard-cap pattern (Hermes ~800 tokens) |
| Append, replace, or version? | Gbrain's compiled-truth-plus-timeline: current value at the top of each section, dated measurement rows below, git holds versions |
| Deltas or whole-store rewrites? | Targeted section edits only; never LLM whole-file rewrite (ACE context-collapse: 18k→122 tokens in one rewrite step) |
| Atomic unit + metadata? | One dated row per measurement with a provenance pointer; one file, per-topic sections, split only on felt pain (OKF one-concept-per-file applies *then*) |

**Read path + lifecycle**

| Question | Inferred answer |
|---|---|
| Mid-session freshness? | No — on-demand read at the consumer skill's calibration step |
| Retrieval proportional to size? | Read/grep; index infrastructure rejected below ~hundreds of entries (`scale-threshold-heuristic-obsidian-vs-rag` — we're ~150 files against a ~1000-doc threshold) |
| Memory as hint or authority? | Hint. Rows carry provenance and are calibration *priors*; consumers re-measure when the decision is consequential (PersistBench: 97% memory-induced sycophancy when stores are trusted as authority) |
| What decays? | Newer rows supersede; staleness is visible via dates; pruning at substrate audits. No TTL machinery |
| Provenance / instructions-vs-observations separation? | Registry holds **raw numbers only, never behavioral instructions** (those are DDs/rules). Guards the `write-time-vs-query-time-synthesis-kb-poisoning` risk — no LLM-synthesized narrative re-consumed as ground truth |
| Scope boundary? | Engine-scoped (`operations/references/`); operator prefs stay in Claude memory — already separate |

## 3 — Proposal (three rulings requested)

**P1 — Calibration registry (build).** One file:
`operations/references/calibration-registry.md`. Per-topic sections; each section
carries: current value/table at top, dated measurement rows with provenance pointers
below, and a **named consumer** (skill + step) — a section that cannot name its reader
is not written. Header rules: raw numbers only; targeted edits only; on-demand read
only (never cold-start). Backfill = one small distill pass over only the
consumer-nameable stranded SL entries (the three verified in §1, plus any of the
remaining seven that pass the named-reader test on body-read); the rest of the frozen
corpus stays as IB-172 feedstock, undistilled. Placement matches existing
`operations/references/` precedent; per `docs-split-by-lifespan-not-topic`, these are
reference-lifespan, not knowledge-pattern-shaped.

**P2 — G9 ruling: encounters defer, with a noticing mechanism (rule, don't build).**
Keep surface-in-run-report (already the contract in `boundary-cases.md`). Persistence:
none — the run reports that already land in `operations/` *are* the record; recurrence
noticing = `/system-audit` greps encounter-type tags across recent reports and flags
any type at ≥3 (the existing "frequent → IB item" routing then fires). Build trigger:
first audit that flags a type. This closes the audit's "no mechanism to notice
recurrence" gap without a standing store for a zero-base-rate event stream.

**P3 — Closure-note overflow: declare resolved.** DD-116 routing covers the class;
no mechanism. The pre-DD-116 monsters stay as immutable records.

**Non-goals (explicit, so scope can't creep):** no derived/vector database
(`markdown-git-system-of-record-derived-disposable-db` labels it the not-yet-needed
upgrade), no autonomous ingestion (Gbrain's own author declines "level 5"; matches the
human-gate value), no memory/wiki/world-KB trichotomy, no OKF adoption now (v0.1
single-vendor draft — conformance is an IB-172 evaluation item, not a premise here).

**Relationship to IB-172:** this is the near-term slice. IB-172 (full layered-memory
+ OKF evaluation) stays Backlog with concrete promotion triggers: KB approaching the
~1000-doc threshold, felt per-folder retrieval pain, or a second consumer for any
memory surface. The registry, if adopted, becomes one input to that design, not a
prejudgment of it.

## 4 — What the failure literature says we're avoiding

Write-only graveyards (the most common documented failure — stores nobody reads),
context collapse from whole-store LLM rewrites (ACE), stale-memory drift from
append-only fact stores, and memory poisoning via re-ingested agent-synthesized
content (OpenClaw's Dreaming bug wrote raw candidates into MEMORY.md and re-ingested
them). P1's named-reader rule, targeted-edits rule, and raw-numbers-only rule are each
aimed at one of these.

## 5 — Questions for Nick (conflicted or genuinely his to rule)

- **Q-A — Kill criterion strictness.** The frontier is emphatic: decide *before
  building* how you'll know the store earned its keep, and delete what goes unread.
  My conflict: a hard rule ("any registry section not cited by its consumer since the
  previous substrate audit is auto-flagged for deletion") is exactly the discipline
  that prevents graveyards — but it is also a standing mechanism adopted at first
  occurrence, which your tolerate-one-offs rule counsels against. **Lean:** adopt the
  hard flag (audits already run; the check is one grep), but this is a values call
  between two of your standing rules, so it's yours.
- **Q-B — G9 destination (designated Nick gate).** P2 recommends defer + audit-time
  grep. The live alternative is a single standing tally file (one line per encounter).
  I'm confident in defer given the zero base rate, but the gate is yours by
  construction, and the tally is the right answer if you expect the assess-* skills'
  usage to grow sharply this phase.
- **Q-C — Does P1–P3 discharge the "second-brain" milestone scope?** I.e., is the
  near-term slice of IB-172 *done* on adoption, with the full layered-memory design
  waiting on its triggers — or do you want the full IB-172 design note scheduled into
  the current program regardless? Roadmap-priority call, not inferable.

---

*Deliberation inputs: Librarian Builder-mode consult (KB citations above) and web
question-sweep (18 questions, convergence patterns, 5 failure stories) — session-142
working artifacts; the distilled content is carried in full here.*
