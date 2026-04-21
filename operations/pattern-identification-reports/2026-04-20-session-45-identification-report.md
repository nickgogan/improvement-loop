---
title: "Artifact Identification Report — Session 45 Findings"
type: "report"
target_system:
  - "improvement-loop"
created: "2026-04-20"
scope: "12 new findings from session 45 Researcher final batch intake (1 P1, 9 P2, 2 P3)"
findings_scanned: 12
findings_filtered: 0
---

# Artifact Identification Report — Session 45

**Scope:** 12 new findings from session 45 Researcher final batch intake — Memongo (6), Anthropic session-management blog (2), UC Berkeley DAB + agentic-speculation papers (2), Simon Willison walkthroughs (2).
**Findings scanned:** 12 | **Filtered out:** 0 (dedup: 0, weak: 0, adopted: 0)
**Classified:** 12

Dedup check: all 12 findings confirmed absent from `extracts/` staging (no `source_finding:` matches). Weak-evidence pre-filter N/A: one Weak-theoretical finding (`agentic-speculation-four-characteristics`) is explicitly named in scope per handoff.

## Summary

| Form | Count | % | Auto | Guided | HITL |
|------|-------|---|------|--------|------|
| pattern | 11 | 91.7% | 7 | 4 | 0 |
| rule | 1 | 8.3% | 1 | 0 | 0 |
| template | 0 | 0% | 0 | 0 | 0 |
| skill | 0 | 0% | 0 | 0 | 0 |
| agent | 0 | 0% | 0 | 0 | 0 |
| **Total** | **12** | **100%** | **8** | **4** | **0** |

**Calibration comparison:**
- 50-finding calibration (session 22): 92% pattern
- P1 batch (session 24): 92% pattern
- Session 42 Batch 2 (2026-04-19): 83% pattern
- Session 42 Batch 2 (2026-04-20, 28 findings): 92.9% pattern
- **Session 45 (this run): 91.7% pattern (11/12)** — matches calibration baseline

**Co-occurrences noted:** 4 findings
- rule: 1 (proactive-compaction — "don't defer /compact" is co-occurring anti-pattern constraint)
- pattern: 1 (programmatic-snippet-extraction — primary rule, pattern co-occurs as "move work from inference to execution")
- skill: 1 (agent-generated-codebase-walkthrough — could instantiate as a skill; primary is pattern)
- template: 1 (decision-matrix — 5×5 matrix layout has template-like scaffold; primary is pattern)

**Guide routing:** 11 pattern findings routed.
- G7 (Session Persistence and Memory): 7 findings — 6 Memory Architecture (Memongo cluster) + 1 agentic-speculation (vision-level Memory Architecture)
- G2 (Managing Agent Context): 3 findings — decision-matrix, proactive-compaction, walkthrough
- G4 (Building Agent Evaluation Suites): 1 finding — DAB benchmark
- **Unrouted: 0.** No additions to unrouted bucket this run.

**Staleness impact on guide cluster counts (for /synthesize-guide gating):**
- G7: current count 14 → will grow to ~21 (7 new routed). Staleness now +11 since session 42 close.
- G2: current count 26 → will grow to ~29 (3 new routed). Staleness now +3 (at threshold).
- G4: current count 30 → will grow to ~31 (1 new). Staleness +1 (below threshold).
- **G9 Agent Governance and Trust still flagged from session 44** — no new findings in Governance dimension this batch.

**Non-pattern routing:** 1 rule finding proceeds to `/extract-artifacts` as a standalone artifact (pending Nick's approval of this report).

---

## Candidates

### HITL — Needs Human Decision (0 findings)

_None this run._

### GUIDED — Review Recommended (4 findings)

| # | Finding | Form | Conf | Co-occurrence | Status |
|---|---------|------|------|---------------|--------|
| 1 | [[claude-code-context-management-decision-matrix-five-tools]] | pattern | MED | template | PENDING |
| 2 | [[data-agent-benchmark-dab-cross-dbms-pipeline-eval]] | pattern | MED | — | PENDING |
| 3 | [[agentic-speculation-four-characteristics-data-system-redesign]] | pattern | MED | — | PENDING |
| 4 | [[agent-generated-codebase-walkthrough-for-onboarding]] | pattern | MED | skill | PENDING |

### AUTO — Ready for Extraction (8 findings)

| # | Finding | Form | Conf | Co-occurrence | Status |
|---|---------|------|------|---------------|--------|
| 5 | [[mongodb-single-store-polymorphic-evidence-memory]] | pattern | HIGH | — | PENDING |
| 6 | [[rank-fusion-hybrid-retrieval-mongodb-atlas]] | pattern | HIGH | — | PENDING |
| 7 | [[query-decomposition-sub-query-rrf-merge]] | pattern | HIGH | — | PENDING |
| 8 | [[post-retrieval-reranking-weighted-signal-composition]] | pattern | HIGH | — | PENDING |
| 9 | [[importance-based-decay-permanent-exemption]] | pattern | HIGH | — | PENDING |
| 10 | [[surprisal-novelty-as-memory-write-gate]] | pattern | HIGH | — | PENDING |
| 11 | [[proactive-compaction-before-intelligence-degradation]] | pattern | HIGH | rule | PENDING |
| 12 | [[programmatic-snippet-extraction-via-shell-anti-hallucination]] | rule | HIGH | pattern | PENDING |

---

## Details

### GUIDED — Pattern (4 findings)

#### 1. claude-code-context-management-decision-matrix-five-tools
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** template
- **Category:** Context Engineering | **Priority:** P1
- **Reason codes:** decision-framework-with-tradeoffs, heuristic-shape, mechanism-is-instantiation, surface-structure-trap-test-applied
- **Rationale:** Center of gravity is the decision-matrix approach to in-session context management (match situation → tool). Reusable shape: any agent harness with multiple context-management primitives can adopt this decision structure; the specific 5 cells (Continue/Rewind/Compact/Clear/Subagent) are Claude-Code-specific instantiations. Template co-occurs because the 5×5 matrix has a fillable scaffold (situation / tool / rationale rows). Pattern wins because the insight is the framework-for-choosing, not the specific tool set. MED — genuine risk of classifying as template since the matrix itself is highly structured; rubric's "Can this be written as `{{VAR}} → body` without loss?" test — losing Anthropic's specific situation/rationale content would gut the insight, so it's pattern with template co-occurrence.
- **Guide routing:** G2 (Managing Agent Context).
- **Status:** PENDING

#### 2. data-agent-benchmark-dab-cross-dbms-pipeline-eval
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** —
- **Category:** Evaluation | **Priority:** P2
- **Reason codes:** reality-check-heuristic, has-baseline-claim, borderline-reference-data
- **Rationale:** The finding describes one specific benchmark with one headline number, but the center-of-gravity per `implementation_notes` is the design heuristic — "treat 38% pass@1 as baseline for frontier-model data-agent reliability; assume raw reliability ~1/3 without scaffolding." That's a reusable shape: use enterprise-grounded cross-DBMS benchmarks as reality checks for data-agent work. MED because the finding could plausibly be read as reference data (one benchmark, one number) rather than pattern; pattern wins because the implementation framing is prescriptive (use this as baseline) and the "what to expect from frontier models on realistic enterprise workloads" framing generalizes beyond this specific benchmark. Not a skill: no procedure. Not a rule: not a deterministic check.
- **Guide routing:** G4 (Building Agent Evaluation Suites).
- **Status:** PENDING

#### 3. agentic-speculation-four-characteristics-data-system-redesign
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** —
- **Category:** Memory Architecture | **Priority:** P3
- **Reason codes:** design-lens-framework, four-property-heuristic, weak-theoretical-evidence, borderline-P3-defer
- **Rationale:** Four-characteristic design lens (scale, heterogeneity, redundancy, steerability) for agent-facing data surfaces. Reusable shape — check any new data-retrieval surface against the four properties. Not a procedure, not a constraint, not a scaffold. MED because evidence is explicitly Weak (theoretical) — vision paper with no benchmarks. The skill pre-filter skips `Weak (anecdotal)` not `Weak (theoretical)`, and the handoff explicitly named this finding in scope, so it is classified. Nick should decide whether a P3 weak-theoretical finding justifies guide routing or should defer until empirical corroboration arrives.
- **Guide routing:** G7 (Session Persistence and Memory) via Memory Architecture dimension.
- **Status:** PENDING

#### 4. agent-generated-codebase-walkthrough-for-onboarding
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** skill
- **Category:** Context Engineering | **Priority:** P2
- **Reason codes:** center-of-gravity-is-reusable-shape, mechanism-is-instantiation, contains-procedure-as-example, skill-co-occurrence-strong
- **Rationale:** Center of gravity is the design approach — "maintain agent-readable onboarding docs via periodic agent self-walkthroughs; serves as onboarding + drift detection." The Simon-Willison + Showboat + Swift app configuration is one instantiation; the insight transfers to MetaSystem's incubator projects and Nick's vibe-coded skills. Skill co-occurs strongly — the finding describes an invocation procedure (agent reads codebase → produces walkthrough.md) that could stand as its own skill (`/generate-walkthrough`). MED because the procedural detail (harness choice, output shape) is concrete enough that a practitioner might treat it as a skill-first finding; pattern wins because the real value is the *practice* of periodic walkthrough regeneration as a maintenance discipline, not the specific procedure.
- **Guide routing:** G2 (Managing Agent Context) — via Context Engineering.
- **Status:** PENDING

### AUTO — Pattern (7 findings)

#### 5. mongodb-single-store-polymorphic-evidence-memory
- **Assigned form:** pattern | **Confidence:** HIGH | **Tier:** auto
- **Category:** Memory Architecture | **Priority:** P2
- **Reason codes:** architectural-counter-stance, forces-tradeoffs, it-depends-character, multiple-contrasting-sources
- **Rationale:** Explicit architectural counter-stance — "one DB, one collection, one retrieval authority" vs. multi-store splits. Pattern-shape with clear forces (operational simplicity vs. per-type optimization), testable against multi-store alternatives. `related_findings` explicitly carry `contradicts` (triple-storage) and `same-problem` (multi-store stacks), which is the classic pattern-level design debate signature.
- **Guide routing:** G7 (Session Persistence and Memory) via Memory Architecture.
- **Status:** PENDING

#### 6. rank-fusion-hybrid-retrieval-mongodb-atlas
- **Assigned form:** pattern | **Confidence:** HIGH | **Tier:** auto
- **Category:** Memory Architecture | **Priority:** P2
- **Reason codes:** reusable-shape, database-native-primitive, instantiation-across-vendors
- **Rationale:** Reusable shape — combine semantic + lexical retrieval inside the database using rank-fusion primitives. Atlas's `$rankFusion` / `$scoreFusion` is one instantiation; the shape (DB-native hybrid retrieval vs. application-side RRF) applies wherever equivalent primitives exist. Not a skill (no step sequence), not a rule (no binary constraint), not a template (no fillable scaffold).
- **Guide routing:** G7.
- **Status:** PENDING

#### 7. query-decomposition-sub-query-rrf-merge
- **Assigned form:** pattern | **Confidence:** HIGH | **Tier:** auto
- **Category:** Memory Architecture | **Priority:** P2
- **Reason codes:** reusable-shape, cross-source-convergence, economic-tradeoffs
- **Rationale:** Reusable shape — decompose user query → parallel retrieve → RRF merge. Multiple independent uses (Memongo, academic RAG literature, Anthropic programmatic tool calls). Forces: decomposition cost vs. retrieval quality, over-decomposition dilution. Clear pattern — the insight is the shape, not Memongo's specific GPT-4-mini choice.
- **Guide routing:** G7.
- **Status:** PENDING

#### 8. post-retrieval-reranking-weighted-signal-composition
- **Assigned form:** pattern | **Confidence:** HIGH | **Tier:** auto
- **Category:** Memory Architecture | **Priority:** P2
- **Reason codes:** design-choice-with-tradeoffs, interpretability-vs-precision, mechanism-is-instantiation
- **Rationale:** Reusable shape — post-retrieval reranking via human-inspectable weighted signals (auditability + tuneability + no retraining) as alternative to learned rerankers. The specific 4 signals + 4 weights are one instantiation. Pattern with clear forces (opacity vs. precision), composable downstream of any retrieval surface.
- **Guide routing:** G7.
- **Status:** PENDING

#### 9. importance-based-decay-permanent-exemption
- **Assigned form:** pattern | **Confidence:** HIGH | **Tier:** auto
- **Category:** Memory Architecture | **Priority:** P3
- **Reason codes:** architectural-alternative, forces-tradeoffs, escape-hatch-primitive
- **Rationale:** Design approach — decay by importance score, not wall-clock; permanent/ongoing exemption for identity facts. Counter-pattern to TTL expiry, pure-recency, reinforcement decay. Pattern with clear forces (unbounded storage vs. identity retention; stale scores vs. recomputation cost). P3 priority but classification is unambiguous.
- **Guide routing:** G7.
- **Status:** PENDING

#### 10. surprisal-novelty-as-memory-write-gate
- **Assigned form:** pattern | **Confidence:** HIGH | **Tier:** auto
- **Category:** Memory Architecture | **Priority:** P2
- **Reason codes:** reusable-shape, write-path-filter, complementary-to-decay
- **Rationale:** Reusable shape — gate memory writes on surprisal/novelty to prevent corpus bloat; upstream complement to downstream decay. Pattern with forces (embedding-coarse misses vs. blocking signal; cold-start problem vs. later precision). Clean pattern — the insight is the write-gate position + surprisal signal type.
- **Guide routing:** G7.
- **Status:** PENDING

#### 11. proactive-compaction-before-intelligence-degradation
- **Assigned form:** pattern | **Confidence:** HIGH | **Tier:** auto | **Co-occurrence:** rule
- **Category:** Context Engineering | **Priority:** P2
- **Reason codes:** reusable-shape, reframes-existing-primitive, tradeoffs-named
- **Rationale:** Reusable shape — "compact at stable state, not at capacity pressure; compaction is a quality-of-summary decision, not capacity management." Reframes `/compact` from fallback to regular-cadence tool. Rule co-occurs ("don't defer /compact to autocompact trigger") but the insight is the design-level reframing, not the specific constraint — applies to any harness with user-controlled compaction. Pattern with clear forces (over-compaction dilution vs. under-compaction summary degradation).
- **Guide routing:** G2 (Managing Agent Context).
- **Status:** PENDING

### AUTO — Rule (1 finding)

#### 12. programmatic-snippet-extraction-via-shell-anti-hallucination
- **Assigned form:** rule | **Confidence:** HIGH | **Tier:** auto | **Co-occurrence:** pattern
- **Category:** Prompt Craft | **Priority:** P2
- **Reason codes:** binary-constraint, anti-pattern-framing, named-boundary, enforceable-at-hook, deterministic-check
- **Rationale:** Classic rule shape — binary constraint at a named boundary (agent output containing code snippets). Anti-pattern phrasing ("do not type code from memory; use sed/grep/cat"). Enforcement mechanism is either prompt-level or hook (implementation_notes flag the hook path explicitly). Per rubric Amendment 2: "anti-pattern findings are natural rule candidates when the anti-pattern is expressible as a deterministic check at a named boundary" — both tests satisfied. Pattern co-occurs as the broader design approach ("move work from inference to execution, like programmatic-tool-calling"), but the finding's center of gravity is the specific constraint, not the general principle. Session-20 calibration note: "rules tend to be autonomous-tier eligible because their blast radius at the artifact level is small" — applies here.
- **Routing:** Non-pattern — proceeds to `/extract-artifacts` as a standalone rule artifact (pending approval). Likely enforcement location: `.claude/rules/` at workspace root, or system-scoped `{system}/governance/` if deployed narrowly. Extraction should include co-occurring pattern note so `/extract-artifacts` can harvest the "move work from inference to execution" pattern during body scan (DD-77 resolves at read time).
- **Status:** PENDING

---

## Guide Routing Check

All 11 pattern findings routed to existing guide clusters. No additions to Unrouted Bucket this run.

| Guide | Existing Count | New from Session 45 | Post-Run Count | Staleness | Sync Rec |
|-------|----------------|---------------------|----------------|-----------|----------|
| G7 Session Persistence and Memory | 14 | 7 | ~21 | +11 | **Re-synthesize (gated on Stream B)** |
| G2 Managing Agent Context | 26 | 3 | ~29 | +3 | **Re-synthesize (gated on Stream B)** |
| G4 Building Agent Evaluation Suites | 30 | 1 | ~31 | +1 | Defer (below threshold) |
| G9 Agent Governance and Trust | 10 | 0 | 10 | unchanged (still +? from session 44) | **Re-synthesize (gated on Stream B)** |

**Unrouted bucket unchanged.** Agentic OS theme remains at 3 findings (graduation trigger at 5 not reached).

**Re-synthesis blocker (per session-46 handoff):** Nick has explicitly gated G7/G2/G9 re-syntheses on the Stream B artifact lifecycle spec. This report does not trigger re-synthesis automatically; the spec governs merge semantics before the next synthesis runs.

---

## Recommendations

1. **Approve 8 auto-tier classifications** for extraction/routing (7 pattern → G7/G2 staleness ledger; 1 rule → `/extract-artifacts`).
2. **Decide on 4 guided-tier classifications** — particularly the decision-matrix finding (pattern vs. template) and the weak-theoretical agentic-speculation finding (whether P3 evidence justifies guide inclusion).
3. **Hold G7 / G2 / G9 re-syntheses** until Stream B artifact lifecycle spec is approved. Staleness is now material (+11 on G7) but Nick has directed that merge semantics be documented before next synthesis.
4. **Route the rule finding** (`programmatic-snippet-extraction`) to `/extract-artifacts` for standalone rule extraction once approved — plus ensure the co-occurring "inference-to-execution" pattern is harvested during extract-artifacts body scan.
5. **No new sources needed** — this is a Codifier-only session; the Researcher queue is closed for this cycle.

---

## Co-occurrence Harvest Queue

Per DD-77, findings classify to a single primary form; secondary forms are noted as co-occurrences and resolved at read-time by downstream consumers. Pattern-classified findings route to guide synthesis, but their embedded non-pattern artifacts (templates, skills, rules) would be absorbed into the guide body and disappear as standalone candidates unless explicitly flagged.

This section catalogs co-occurrences in the session-45 set so Nick can pull them out as their own artifacts during `/synthesize-guide` or a follow-up `/extract-artifacts` pass. Nothing is auto-extracted — these are **candidates for review**, not drafts.

| # | Finding | Primary | Co-occurrence | Embedded artifact sketch | Recommended action |
|---|---------|---------|---------------|--------------------------|--------------------|
| 1 | `claude-code-context-management-decision-matrix` | pattern | **template** | 5×5 decision matrix scaffold (situation / tool / rationale) — directly usable as a template for future multi-tool decision docs | Extract as `extracts/templates/multi-tool-decision-matrix.md` if Nick wants a reusable scaffold for other decision-framework docs (not just context management). |
| 7 | `proactive-compaction-before-intelligence-degradation` | pattern | **rule** | Binary constraint: "don't defer `/compact` to autocompact trigger" — expressible as a prompt-level or hook-level constraint | Extract as `extracts/rules/compact-proactively-rule.md` if Nick wants this as an enforceable constraint in harness CLAUDE.md. |
| 11 | `agent-generated-codebase-walkthrough` | pattern | **skill** | Procedure: agent reads codebase → extracts snippets via shell → emits walkthrough.md — candidate for `/generate-walkthrough` skill | Extract as `extracts/skills/generate-codebase-walkthrough.md` if Nick wants this as a directly-invocable skill on incubator projects. |
| 12 | `programmatic-snippet-extraction-via-shell-anti-hallucination` | **rule** | pattern | Broader "move work from inference to execution" design shape — already captured by `programmatic-tool-calling` extract (`extracts/patterns/programmatic-tool-calling-code-orchestrated-tool-use.md`) | Cross-link only; pattern is already staged. No new extraction needed — confirm dedup against existing pattern extract. |

**Policy note:** this queue is informational for this run. Stream B's proposed **DD-X9** (co-occurrence harvesting during guide synthesis) would make this a standing mechanism rather than a one-off flag. Until DD-X9 is decided, Nick's approval of each row above is the gate for extracting the embedded artifact.

---

## Status Dispatch (contract with /extract-artifacts)

All 12 findings have `Status: PENDING`. Per DD-29 human gate, Nick edits the report setting `APPROVED`, `REJECTED`, or `REDIRECTED` (with form edit) before `/extract-artifacts` runs. The only finding that would go to `/extract-artifacts` under current routing (DD-81 pattern filter) is #12 — the rule. The 11 pattern findings route to guide synthesis gated on Stream B.

---

## Methodology Note

This run classified 12 findings via direct rubric application rather than parallel Sonnet subagent fan-out. Rationale: 12 findings is below the efficiency threshold where subagent overhead pays back, and all rubric tests (center-of-gravity, surface-structure-trap, exclusion tests, level-of-abstraction) were applied per-finding against the §1–§5 rubric as extracted by the Codifier. Rubric fidelity preserved; parallelization deferred to larger batches.

---

## Cross-References

- Session 45 delta report: `operations/research-reports/2026-04-20-session-45-delta-report.md`
- Form classification rubric: `operations/references/form-classification-rubric.md`
- Guide routing table: `operations/references/guide-routing-table.md`
- Codifier agent definition: `agents/codifier/agent.md`
- DD-77 (single-form classification): `project-management/design-decisions/DD-77.md`
- DD-81 (pattern filter — patterns route to guide synthesis, not individual extracts)
- Lifecycle spec (Stream B — gates re-syntheses): `project-management/design-notes/2026-04-20-artifact-lifecycle-spec.md`
