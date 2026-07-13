---
title: "Artifact Identification Report"
type: "report"
target_system:
  - "improvement-loop"
created: "2026-07-13"
scope: "Post-sweep P1/P2 crop from the session-144 priority reassessment (2 new P1s, 4 new P2s)"
findings_scanned: 6
findings_filtered: 1
---

# Artifact Identification Report — 2026-07-13

> **Gate outcome (2026-07-13):** Nick accepted all recommendations as-is — all 5
> findings APPROVED as pattern; `/detect-drift` pre-step authorized; synthesis
> destinations per the routing table below (append-only-run-log → G7,
> file-mediated-handoff → G2b, plans-contract → G1, capability-primitive +
> framework-tax → G10); DD-98/DD-99 observations noted with no action.

**Scope:** the post-sweep P1/P2 crop from the session-144 priority reassessment — the 2
new P1s and 4 new P2s Nick accepted in `priority-reassessment-2026-07-13.md`.
**Findings scanned:** 6 | **Filtered out:** 1 (dedup: 1, weak: 0, adopted: 0)
**Classified:** 5

**Filter notes:**
- `ralph-wiggum-execution-pattern` — filtered (dedup). Already staged in `extracts/`
  (`pipeline_status: extracted`; classified in the 2026-05-24 identification run). Its
  session-144 updates (P1 upgrade, Ralph/PIV sibling-variant gate note, Archon crosslink)
  post-date the extraction — that is `/detect-drift` territory, not re-identification.
  Recommend a `/detect-drift` pass before the next `/extract-artifacts` run.
- `framework-abstraction-tax-for-agents` — `adoption_status: Already Adopted` would
  normally pre-filter it, but it is explicitly named in the scope (one of the 4 new
  P2s; the reassessment's rationale is that the bump buys codification, not
  implementation). Kept in.

## Summary

| Form | Count | % | Auto | Guided | HITL |
|------|-------|---|------|--------|------|
| pattern | 5 | 100% | 4 | 1 | 0 |
| rule | 0 | 0% | 0 | 0 | 0 |
| template | 0 | 0% | 0 | 0 | 0 |
| skill | 0 | 0% | 0 | 0 | 0 |
| agent | 0 | 0% | 0 | 0 | 0 |

100% pattern is consistent with the 92% calibration baseline (patterns are the default
at the philosophy/approach altitude findings are written at). Co-occurrences noted: 4.

## Candidates

### HITL — Needs Human Decision

_(none)_

### GUIDED — Review Recommended

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 1 | [[framework-abstraction-tax-for-agents]] | pattern | MED | — | APPROVED |

### AUTO — Ready for Extraction

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 2 | [[append-only-run-log-as-working-memory]] | pattern | HIGH | rule | APPROVED |
| 3 | [[file-mediated-subagent-handoff-workspace]] | pattern | HIGH | skill | APPROVED |
| 4 | [[plans-that-carry-their-own-contract]] | pattern | HIGH | template | APPROVED |
| 5 | [[capability-as-agent-composition-primitive]] | pattern | HIGH | template | APPROVED |

## Details

### 1. framework-abstraction-tax-for-agents

- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** it-depends-tradeoff, single-strong-source, debugging-heuristic
- **Co-occurrence:** —
- **Rationale:** Center of gravity is a heuristic/design-approach observation — "prefer
  simple composable patterns over complex frameworks because abstraction obscures the
  prompt/response boundary needed for debugging" — a tradeoff-laden "how should I
  structure this?" claim rather than a procedure, deterministic check, scaffold, or
  persona. Excluded from rule (no deterministic enforceable boundary; advisory, not
  binary) and from skill (no ordered steps or defined inputs/outputs).
- **Orchestrator note:** the classifier's MED partially rested on "single source
  (Anthropic)" — but the finding's frontmatter lists 3 independent sources (the body
  excerpt only cites Anthropic). Per the rubric amendment, confidence measures
  form-certainty, not evidence; the form call (pattern) is unaffected and guided tier
  is kept conservatively. The body is also the thinnest of the crop (2026-04-09
  vintage) — worth a body refresh before extraction if this becomes the
  platform-native-harness evidence spine.
- **Status:** APPROVED

### 2. append-only-run-log-as-working-memory

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** compositional-shape, multiple-known-uses, tradeoffs-present, downstream-instantiable
- **Co-occurrence:** rule (the append-only/no-edit-delete invariant is a deterministic
  constraint instantiating the shape)
- **Rationale:** Center of gravity is the reusable shape "reserve an append-only,
  write-only, resume-by-tail log as durable working memory" — confirmed independently
  by two unrelated repos (BMAD memlog, Superpowers progress ledger) with differing
  concrete mechanisms, the pattern signature of convergent shape / divergent instance.
  Excluded from skill (an architectural discipline applied throughout a run, not a
  callable procedure) and from rule (the invariant set is richer than one boundary
  check; the no-edit/delete detail is a rule-shaped instantiation, noted as
  co-occurrence).
- **Note:** direct input to IB-176 (memory-system build) — extraction timing aligns
  with the current milestone.
- **Status:** APPROVED

### 3. file-mediated-subagent-handoff-workspace

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** compositional-shape, multiple-known-uses, tradeoffs-present, context-residency-forces
- **Co-occurrence:** skill (the task-brief / review-package / sdd-workspace scripts are
  procedural instantiations of the shape)
- **Rationale:** Center of gravity is "mediate orchestrator/subagent handoffs through
  files, not pasted content, to protect context residency" — a reusable design shape
  independently converged on by Superpowers (reversing its own prior doctrine) and
  BMAD, with differing concrete file layouts. The litmus test passes: the insight
  (write once, dispatch paths, thin returns) applies without the specific scripts.
  Excluded from skill because the value is the architectural rationale, not one ordered
  stateless procedure — the scripts are mechanisms, not the center of gravity.
- **Status:** APPROVED

### 4. plans-that-carry-their-own-contract

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** compositional-shape, multiple-known-uses, tradeoffs-present, addresses-ld-hypothesis
- **Co-occurrence:** template (Global Constraints header / Interfaces block /
  sealed-frontmatter manifest are fillable scaffolds instantiating the shape)
- **Rationale:** Center of gravity is the design approach "front-load binding context
  into the plan itself so context-isolated implementers don't re-derive or miss it" —
  confirmed by two frameworks converging on shape while diverging on syntax (the
  finding itself states "the pattern, not the syntax, is the durable part"). Excluded
  from template because the insight is the rationale (moving derivation cost to the
  point of maximum context), not merely a variable/body scaffold — though the concrete
  blocks could be instantiated as templates downstream (noted as co-occurrence).
- **Status:** APPROVED

### 5. capability-as-agent-composition-primitive

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** compositional-shape, surface-structure-trap, composition-primitive, industry-convergence
- **Co-occurrence:** template (a capability's instructions+tools+hooks+guardrails
  bundle could be rendered as a scaffold with named slots)
- **Rationale:** Center of gravity is the composition question "what is the reusable
  unit that bundles instructions + tools + hooks + guardrails + settings around one
  responsibility" — the finding itself frames the novelty as unifying
  previously-separate pieces into one shape. This is the surface-structure trap
  resolved correctly: Pydantic AI's "capability" object is a specific mechanism, but
  the insight (bundle governance-relevant pieces as one shareable, progressively
  disclosed unit) applies without that exact API. Excluded from agent (a composition
  unit, not a persona) and skill (no ordered procedure).
- **Status:** APPROVED

## Curator Priority Review (Step 3.5)

No priority revisions proposed. All five findings had their priorities set **today** by
the Nick-gated session-144 reassessment (`priority-reassessment-2026-07-13.md`), which
already applied the KB-wide signal (link clusters, cross-framework convergence, IB-176
timing premium, North Star weighting) that this pass would otherwise bring. Nothing has
changed in the KB since that gate.

## Guide Routing (Step 6, DD-81)

All 5 pattern findings are **routed**; unrouted bucket remains empty.

| Finding | Category → Cluster | Note |
|---------|--------------------|------|
| append-only-run-log-as-working-memory | Context Engineering → G2a/G2b (secondary G7) | Per the G2a/G2b/G7 disambiguation note, the content (cross-session resume, compaction recovery) leans **G7 Session Persistence and Memory** — recommend G7 as the synthesis destination |
| file-mediated-subagent-handoff-workspace | Context Engineering → G2a/G2b | Context-residency economics = G2b's cost-control territory; orchestration secondary |
| plans-that-carry-their-own-contract | Intent Engineering → G1 Writing Agent Specifications | Clean 1:1 |
| capability-as-agent-composition-primitive | Agent Design → G10 Agent Design Patterns | Composition-unit question; G3 architecture secondary |
| framework-abstraction-tax-for-agents | Agent Design → G10 Agent Design Patterns | Also anchors the platform-native-harness stance (G3-adjacent) |

**Staleness note:** these routings push G1, G2a/G2b (or G7), and G10 further past their
Findings-at-Synthesis counts — all were already 3+ over per the wave-3 intake, so the
re-synthesis indicator was already lit before this run.

### DD-98 Split-Trigger Observations (Step 6.a)

No new split proposals emitted this run. State of the count threshold (≥25, snapshot
counts from the routing table's Synthesis Status):

- **Open proposals already exist** (2026-05-25, `operations/split-proposals/`) for G3
  (42), G9 (38), G10 (37) — awaiting Nick's ruling; re-emission would duplicate open
  proposals, not add signal. G2's proposal was executed as the G2a/G2b split
  (session 104).
- **Monitor (count ≥25, single coherent question):** G4 at 46 findings; G2a at 35;
  G2b at 30; G11 at 30; G7 at 27. Each still answers its single practitioner question
  per the cluster table; no question bifurcation asserted without a deeper read.
  Monitor for bifurcation on next cycle — G4 (46) is the largest single-question
  cluster and the first candidate for a dedicated split evaluation.

### DD-99 Graduation Check (Step 6.b)

No-op — the unrouted bucket is empty.

## Next Steps

1. **Nick gates this report:** set Status per finding (APPROVED / REJECTED / REDIRECTED);
   the guided-tier item (#1) is the one needing an actual read.
2. All 5 are **pattern** → the extraction path is `/synthesize-guide` (DD-81), not
   `/extract-artifacts`: G7 (or G2b) re-synthesis picks up #2 and #3; G1 picks up #4;
   G10 picks up #1 and #5. Co-occurrence harvesting (rule/skill/template noted above)
   happens at read time per DD-77.
3. Recommended pre-step: `/detect-drift` over `extracts/` — ralph-wiggum's staged
   artifact predates its session-144 finding updates.
4. After Nick's gate: back-annotate `pipeline_status: "classified"` on the 5 findings
   (Step 7).
