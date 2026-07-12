---
title: "Librarian Boundary-Case Tracking Mechanism"
type: "design-note"
stage: "accepted"
target_system:
  - "improvement-loop"
created: "2026-04-22"
updated: "2026-04-22"
author: "owner"
autonomy_tier: "Proposal-First"
source_dd:
  - "DD-29"
  - "DD-52"
  - "DD-80"
  - "DD-82"
  - "DD-86"
tags:
  - "proposal"
  - "librarian"
  - "telemetry"
  - "owner"
  - "boundary-cases"
aliases:
  - "Librarian encounter tracking"
  - "Boundary-case tracking"
---

# Librarian Boundary-Case Tracking Mechanism

**Status:** **Accepted by Nick in session 52 (2026-04-22).** All six §6 Proposal-First items ratified; infrastructure deployed the same session (schema amendment; `assess-agent` / `assess-prompt` / `assess-skill` SKILL.md addenda with Write-tool permission scoped to `operations/system-log/`; DD-82 Librarian write scope amended). The `/summarize-encounters` skill remains named-but-not-built per §6 item 5; build trigger is volume or Nick's brief.

Answers Nick's session-49 read-contract §9 annotation: *"Definitely capture these somewhere (let's explicitly think about where) so that way we can make sure the Librarian remains useful over time and tracks with what the world needs from it."*

---

## Why this matters

The Librarian's reference layer (Option α') was authored against a predicted use-case distribution — 35 canonicalized use cases, frequency weights estimated at ~80/20 core/long-tail. Those weights are unverified. The read-contract bakes in fallbacks for every boundary case (missing concept file, missing operation file, ambiguous verb, hop-ceiling hit, Tier-3 read, KB gap) but currently **discards the encounter after the fallback fires**. No substrate accumulates.

Two failure modes follow from that:

1. **Unknown unknowns stay unknown.** A consumer asks a query the Librarian silently degrades on (e.g., `(audit, mcp.md)` where `mcp.md` is unauthored). The Librarian falls back to the guide routing table, delivers a serviceable answer, and the gap is never logged — so the Codifier's authoring backlog doesn't get pressure from real demand.
2. **Tuning parameters don't calibrate.** The 3-hop Tier-2 ceiling, the ~500-line artifact threshold, the variant-selection heuristics — all picked as educated guesses. Without traces of where they fired, refining them is guesswork.

The fix is a structured encounter record that accumulates at query time and supports pattern detection over time.

---

## 1 — Taxonomy: what qualifies as a boundary-case encounter

Every Librarian query passes through a deterministic pipeline (parse → load → compose → read → assemble → cite). An encounter is any query-handling event where the pipeline **deviated from the Tier-1 happy path** — took a fallback, asked a clarifying question, escalated tiers, or reported a gap. These are the cases where the reference layer met friction.

Thirteen encounter types, consolidated from the read-contract. Each is independently detectable by the Librarian (or by an assess-* skill acting as Librarian) at the step it fires.

| # | Encounter type | Fires at step | Trigger |
|---|---|---|---|
| 1 | `missing-concept` | Step 1.2(c) | No concept file resolves the noun |
| 2 | `missing-operation` | Step 2 / §9.2 | No operation file resolves the verb |
| 3 | `ambiguous-verb` | Step 1.1 / §9.3 | Query blends verbs or verb is non-canonical |
| 4 | `ambiguous-variant` | Step 1.2(b) | Variant-selection heuristic does not disambiguate |
| 5 | `cross-concept` | Step 1.4 / §9.5 | Query spans two concept files |
| 6 | `verb-noun-mismatch` | §9.6 | Operation doesn't semantically apply to the concept |
| 7 | `oversized-artifact` | Step 1.5 / §9.4 | Submitted artifact > ~500 lines |
| 8 | `hop-ceiling-hit` | Step 4.2 | Tier-2 traversal stopped at 3-hop ceiling |
| 9 | `tier-3-read` | Step 5 | External / watched-library read performed |
| 10 | `low-confidence` | Step 6.1 | Substrate supports claim weakly or indirectly |
| 11 | `kb-gap` | Step 6.4 | No substrate found for a requested aspect |
| 12 | `redirect` | Step 8.1 | Query routed out of scope (e.g., `/prompt-evaluator`, `/security-review`) |
| 13 | `clarification-asked` | Steps 1.2, 1.5, 8.2–8.5 | Librarian asked the consumer one disambiguating question |

**Not every encounter is a failure.** `tier-3-read` and `clarification-asked` are healthy pipeline behavior; their frequency is still useful signal (Tier-3 volume = cost watch; clarification volume = parser or input-contract signal).

**An encounter can carry multiple types.** A query may be both `cross-concept` and `low-confidence`. The record allows a list, not a single label.

---

## 2 — Where encounters live

Nick's session-49 gate: *"the Librarian's operations log … will live in the IL system log for now"* — rejecting a separate parallel usage log. That framing governs location.

### Candidate evaluation

Four candidates against the criteria Nick named (write cost, query cost, auditability, SL displacement), plus one I add (**fit with DD-52 fractal pattern**).

| Candidate | Write cost | Query cost | Auditability | SL displacement | Fractal fit |
|---|---|---|---|---|---|
| **A. Each encounter = new SL file** | Low per write, but **high volume** — 10+ files per session would swamp SL's session-shape signal | Medium — Dataview queryable but noise-to-signal drops | High — fully auditable via git | **High** — SL would read as "encounters + sessions" not "sessions" | Weak — SL was shaped as session/structural-event log |
| **B. Per-session encounter log file in SL** (one file per Librarian-active session, multiple encounters per file, distinct `type:` tag) | Low — one file touched per session | Low — `type: librarian-encounter-log` is Dataview-queryable; per-encounter body is grep-scannable | High — per-session file matches SL's audit unit (git-reversible at session granularity) | **Low** — files co-located but type-tagged, so SL queries filter them out; session-SL entries unchanged | Strong — SL stays append-only, file-per-event semantics preserved |
| **C. Dedicated `operations/librarian-encounters/` folder** | Low | Low — isolated folder | High | None | Strong in isolation, but **contradicts Nick's "lives in SL" framing** |
| **D. Rolling single file** (`operations/system-log/librarian-encounters.md`, append-only) | Very low | Low for grep, hard for temporal pattern | Medium — single file grows unbounded | Low | **Violates one-file-per-entry convention** and risks concurrent-write issues |
| **E. Per-skill companion logs** (each assess-* writes its own) | Low | **High** — data fragmented across N skills | Low — aggregation required | None | Weak — fragmentation undermines pattern detection |

### Reconciliation with Nick's SL-is-home call

The session-49 rejection was of a **parallel duplicate usage log** — a full activity trace. Boundary-case tracking is not that. It is a **structured pattern substrate** for a specific purpose: calibrating the reference layer against actual demand. The two concerns are different:

| Concern | Carrier | Granularity |
|---|---|---|
| Usage record (the "did the Librarian run, with what cost") | SL one-line note per cost-bearing event (Tier-3 reads per read-contract §5.3) | Per-read |
| Boundary-case patterns (the "where did the reference layer meet friction") | Structured encounter record, aggregated | Per-session |

Honoring Nick's framing means: **encounters live in SL, but as their own file type**, not mixed into session SL entries.

### Recommendation: Option B (per-session encounter log in SL, type-tagged)

- **Location:** `operations/system-log/` (flat, co-located with session SL entries).
- **File naming:** `session-<N>-librarian-encounters.md` — one file per session of Librarian activity.
- **Distinction:** `type: librarian-encounter-log` in frontmatter. Session-level SL entries keep `type: system-log`. Dataview and grep queries filter cleanly.
- **Creation trigger:** A Librarian-invoking skill (currently the three assess-* skills) creates or appends to the file on first encounter of a session. Sessions with zero boundary-case encounters produce no file — absence is signal too.
- **Lifecycle:** Append-only during the session. Session-close workflow flushes to disk, commit, done.

**What this does not do:** it does not replace the read-contract §5.3 SL one-liner for Tier-3 reads. Those remain as session-level SL notes — Nick's existing call. `tier-3-read` encounters appear **twice**: once as the SL one-line usage record, once as a structured entry in the encounter log. Different purposes, different carriers.

---

## 3 — Entry shape

### Frontmatter (file-level)

```yaml
---
title: "Session <N> — Librarian encounters"
type: "librarian-encounter-log"
target_system:
  - "improvement-loop"
session: <N>
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
actor: "librarian"
invoking_skills:
  - "assess-agent"
  - "assess-prompt"
  - "assess-skill"
tags:
  - "librarian-encounter"
  - "telemetry"
---
```

The `invoking_skills` list is populated as skills append. Enables per-skill pattern queries without fragmenting storage.

### Per-encounter body shape

Append-only under session-dated sub-headings. Each encounter is a short block — structured enough for grep/Dataview, loose enough to not add write friction at query time.

```markdown
## <ISO timestamp> — <encounter-type>[, <encounter-type>...]

- **Query:** <natural-language query, ≤1 line>
- **Parsed as:** (verb: `<v>`, noun(s): `<n>`[; variant: `<var>`])
- **Invoking skill:** `<skill-name>` (or `direct` if Librarian invoked without a skill)
- **Substrate read:** Tier-1=<N sections>; Tier-2=<M findings>; Tier-3=<K reads>
- **Resolution:** <how the Librarian proceeded — fallback, degraded, asked, escalated, redirected>
- **Gap (if any):** <what was missing — e.g., "no concept file for `mcp.md`">
- **Consumer disposition:** <optional — answered / user abandoned / user redirected>
```

### Required vs. optional fields

- **Required:** timestamp, encounter-type(s), query, parsed-as, resolution.
- **Optional but encouraged:** substrate read (cost visibility), gap, consumer disposition.
- **Tags on encounter-types are controlled vocabulary.** Enumerated in §1. Skills that write encounter records must use those tags verbatim; this is what makes pattern queries cheap.

### Cost envelope

Each encounter block is ~5–8 lines. A session with 10 encounters produces a ~70-line file. Well under any token/storage concern. Write cost is Librarian-side composition time, which is already part of the query-handling flow.

---

## 4 — How patterns surface

Three candidate surfacing mechanisms. I recommend one primary + one deferred.

### 4.1 Candidates

| Mechanism | Description | Cost to build | Cost to run |
|---|---|---|---|
| **Owner workflow (on brief)** | Nick points the Owner at a question; Owner reads encounter logs, groups by type, reports patterns. No new skill. | None — uses existing Owner tools (Read, Grep, Glob) | Per-request |
| **Periodic dimension in `/system-audit`** | Add an "encounter patterns" dimension to the existing `/system-audit` skill; runs as part of full audit. | Low — one new section in the skill | Only on audit |
| **Dedicated skill `/librarian-patterns`** | Purpose-built skill that reads all encounter logs, groups, ranks, produces a patterns report. | Medium — new SKILL.md, new workflow | Per-invocation |

### 4.2 Recommendation

**Primary (now): Owner workflow on brief.** This is Stream B of session 50 — exactly what Nick described: *"I imagine that the Owner will examine the system log for any particular patterns, given something to pay attention to and why by me (Nick)."* No new skill needed; Owner tools handle it. Pattern: Nick asks → Owner reads the relevant encounter files → Owner reports. Patterns that warrant action become proposals at the Owner's Proposal-First tier.

**Deferred (build when volume justifies): `/system-audit` dimension.** Once enough encounter files exist that manual scan becomes costly, add an "encounter patterns" section to `/system-audit`. Minor — not worth building now.

**Not building: dedicated `/librarian-patterns` skill.** Adds ceremony without the problem: the Owner can do the grouping in conversation. The system must earn its complexity (Owner constitution).

### 4.3 What "patterns" to surface

Five pattern classes the Owner should look for when Nick invokes this:

1. **Authoring-demand patterns.** Which missing concepts or operations appear most often? (Ranks next-wave authoring.)
2. **Parser friction patterns.** Which aliases/triggers miss? Which queries get `ambiguous-verb`? (Feeds canonical-verb-map refinement.)
3. **Threshold calibration.** How often does the 3-hop ceiling fire? Is ~500 lines the right oversized-artifact threshold? (Tuning.)
4. **Tier-distribution drift.** What fraction of queries require Tier-2? Tier-3? (Validates use-case registry frequency weights.)
5. **Redirect-shape patterns.** Where is the Librarian pointing people out of scope? (Might indicate scope-expansion candidates, or might confirm scope discipline.)

---

## 5 — Feedback path: from encounter → authoring

When encounters accumulate, gaps surface. The feedback path connects those to existing authoring surfaces.

### 5.1 The three surfaces that can consume encounter signal

1. **Use-case registry** (`project-management/design-notes/2026-04-21-librarian-use-case-registry.md`) — the authoritative list of planned concept/operation files with P2/P3/P4 priorities. Natural home for demand-driven reprioritization.
2. **Implementation Backlog** (`project-management/implementation-backlog/`) — for structural changes that don't fit the registry (e.g., a new parser alias, a new variant, a threshold change).
3. **Researcher queue** via IB items — if an encounter reveals a gap in research coverage (KB-gap type), it becomes a research scan target filed as an IB item, not an authoring target.

### 5.2 Routing rules (proposed)

| Encounter type | Primary feedback path | Who acts |
|---|---|---|
| `missing-concept` | Use-case registry → promote concept to higher priority; Codifier authors next session | Codifier (after Nick re-prioritizes) |
| `missing-operation` | Use-case registry → promote operation; Codifier authors | Codifier |
| `ambiguous-verb` | IB item → canonical-verb-map refinement (read-contract §1.1) | Codifier or Owner |
| `ambiguous-variant` | Concept file update (variant-selection heuristics) | Codifier |
| `hop-ceiling-hit` (frequent) | IB item → revisit 3-hop ceiling; tune with evidence | Owner proposal |
| `oversized-artifact` (frequent) | IB item → scope protocol refinement | Owner proposal |
| `kb-gap` | IB item → Researcher queues for next scan | Researcher |
| `redirect` (frequent to same target) | Read-contract §8.1 update, or scope-expansion proposal | Owner |
| `low-confidence` (pattern by aspect) | Evidence-strength review; possibly Researcher scan | Researcher or Codifier |
| `verb-noun-mismatch` | Usually parser-side; IB if frequent | Codifier |
| `clarification-asked` (frequent for same reason) | Input-contract refinement (e.g., require `since:` for `whats-new`) | Codifier |
| `tier-3-read` | Watch-only. Volume → cost signal. | Owner monitors |
| `cross-concept` | Subagent template work (read-contract Q4) — already session-50+ backlog | Codifier |

### 5.3 The Owner's role in routing

The Owner does not silently move items into these queues. The Owner **proposes** routing during Stream B pattern reports: "these 4 encounters show `missing-concept: mcp.md` — recommend promoting `mcp.md` from P3 to P2 in the use-case registry." Nick gates the reprioritization. The Codifier picks it up on the next authoring session.

---

## 6 — Proposal-First items Nick gates

What this proposal asks Nick to approve before deployment:

1. **File type convention.** Adopt `type: librarian-encounter-log` in `operations/system-log/`. No new directory; files co-locate with session SL entries, distinguished by type.
2. **Entry schema.** The frontmatter shape (§3) and per-encounter body shape (§3) become the contract. Controlled vocabulary of 13 encounter types (§1).
3. **Skill contract update.** The three deployed assess-* skills (`assess-agent`, `assess-prompt`, `assess-skill`) must write encounter records when they hit boundary cases. Minor SKILL.md addendum — "On encounter, append to `operations/system-log/session-<N>-librarian-encounters.md` following the entry schema." Additive, not structural. Requires Nick's gate because it modifies deployed skill contracts. Write-tool permission expanded to `operations/system-log/` only (confirmed §7.Q2).
4. **Feedback routing table.** The routing rules in §5.2 become operational guidance for the Owner during Stream B. Not a DD; a convention. Nick's approval makes it authoritative.
5. **New Owner skill — `/summarize-encounters`.** Reads accumulated `librarian-encounter-log` files, produces a summary report covering pattern frequencies and calibration signals (authoring-demand ranks, parser-friction patterns, threshold calibration, tier-distribution drift, redirect patterns per §4.3), archives raw logs past a threshold age to `archive/librarian-encounters/<year>/`, and commits both the summary and the archive move for Nick's review. Invoked periodically on Nick's brief or at milestone boundaries — not continuously. The skill itself is Proposal-First (new Owner skill); once gated, the archival operation is Guarded (append-only summary + git-reversible moves). Not built this session — named as a downstream need. Build trigger: first session where manual scan of encounter logs becomes costly (heuristic: ~20+ session-logs accumulated, or Nick asks).
6. **Controlled-vocabulary amendment path.** New encounter types are added via Owner proposal → Nick gate → read-contract + this proposal both updated (confirmed §7.Q4).

What this proposal does **not** ask for in this session:

- No skill built this session — `/summarize-encounters` is proposed, not built.
- No new directory beyond the implicit `archive/librarian-encounters/` that the archival skill will create when first invoked.
- No DD filing (this is a proposal, not a DD; a DD may follow if the mechanism stabilizes over multiple sessions).
- No change to read-contract §5.3 Tier-3 SL one-liner — that remains as-is.

---

## 7 — Resolved by Nick (session 50, 2026-04-22)

| # | Question | Nick's decision | Where reflected |
|---|---|---|---|
| Q1 | Location consent — Option B (per-session encounter log in SL, type-tagged) vs. dedicated subfolder (Option C). | **Accept Option B.** | §2 Recommendation — unchanged. |
| Q2 | Skill write contract — add **Write**-tool permission to `operations/system-log/` only, or route writes through a wrapper. | **Acceptable** — expand permission on the three assess-* skills. | §6 item 3 — now reflects the confirmed permission expansion. |
| Q3 | Retroactive capture — seed the first encounter log from assess-* skill test runs against real artifacts. | **Acceptable.** | §5.1 deferred note — first logs will come from deferred testing of assess-* skills. |
| Q4 | Controlled-vocabulary governance — amendment path for new encounter types. | **Accept** the path (Owner proposes → Nick gates → both read-contract and this proposal updated). | §6 item 6 — added as explicit Nick-gated item. |
| Q5 | Expiration / compaction — summarize and move old logs, or keep raw trail forever. | **New skill.** Owner should have a skill that summarizes encounter logs, archives older entries, and writes a report about its work for review. | §6 item 5 — added as a Proposal-First Nick-gated item; not built this session. |

**No open questions remain for session 50.** All five decisions integrated into §2, §5.1, and §6.

---

## 8 — Summary

- **What this proposes:** a structured boundary-case tracking substrate that lives in the IL System Log as a distinct file type (`librarian-encounter-log`), written per session, readable by Dataview and grep.
- **Why:** the reference layer needs demand signal to calibrate; the read-contract currently loses that signal on fallback.
- **How the world-tracks-Librarian loop closes:** encounters accumulate → Owner surfaces patterns on Nick's brief (Stream B) or during `/system-audit` → patterns route to the use-case registry, IB, or research queue → Codifier/Researcher/Owner act → Nick gates deployment.
- **What's new, what's reused:** new file type and entry schema; reuses SL as home, Owner tooling for pattern surfacing, existing authoring surfaces for feedback.
- **What Nick gates:** file type convention, entry schema, skill contract addendum, routing table.

End-state after Nick's gate: the three deployed assess-* skills begin accumulating encounter records. The first real Stream B pattern report becomes possible after ~3–5 sessions of accumulated data. The registry's estimated frequency weights become measurable. The 3-hop ceiling and ~500-line threshold become calibrate-able rather than guessed.

---

## Cross-References

- Source question: `project-management/design-notes/2026-04-21-librarian-read-contract.md` §9 (Nick's inline annotation)
- Use-case registry (authoring backlog feedback target): `project-management/design-notes/2026-04-21-librarian-use-case-registry.md`
- Reference layer: `operations/references/librarian/`
- Deployed assess-* skills (encounter writers): `systems/improvement-loop/.claude/skills/assess-agent/`, `.../assess-prompt/`, `.../assess-skill/`
- Companion DD proposal (where Owner artifacts live): `governance/proposals/2026-04-22-dd-proposal-owner-design-artifact-placement.md`
- Owner agent definition (autonomy tiers, proposal-first): `agents/owner/agent.md`
- Governing DDs: DD-29 (human gate), DD-52 (fractal pattern), DD-80 (pipeline), DD-82 (4-agent arch, Librarian role), DD-86 (Owner responsibility)
