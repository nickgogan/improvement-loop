# Delta Report — 2026-04-20 (Session 45, Final Batch Intake)

## Scan Summary
- **Session:** 45 — Researcher final batch intake
- **Sources processed:** 5 (1 GitHub repo, 1 Anthropic blog, 2 arXiv papers, 1 Simon Willison guide)
- **New findings added to KB:** 12
- **Existing findings updated:** 6 (3 content updates + 3 reverse-crosslink-only)
- **New authorities:** 3 (Simon Willison, UC Berkeley EPIC Lab, Memongo/romiluz13)
- **Watched libraries added:** 1 (Memongo — explicit Nick override on session scope)
- **Previous report:** 2026-04-20 (Batch 2 delta report, closed by Codifier in sessions 43–44)

All new findings at `pipeline_status: raw`. No classification, no extraction, no guide work — per session scope, handoff is to a future Codifier run.

## KB State Change

| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| Findings | 533 | 545 | +12 |
| Sources | 131 | 136 | +5 |
| Authorities | 67 | 70 | +3 |
| Watched Libraries | 15 | 16 | +1 |
| Dimensions | 11 | 11 | 0 |
| Null-priority findings | 0 | 0 | 0 |

## Sources Processed

| # | Source | Type | Authority | New Findings | Notes |
|---|--------|------|-----------|--------------|-------|
| 1 | Memongo (GitHub) | Documentation | Memongo/romiluz13 | 6 | MongoDB-native agent memory framework; Nick owns this and wants improvement ideas |
| 2 | Anthropic — Session Management + 1M Context | Blog Post | Anthropic | 2 | Canonical context-management decision matrix |
| 3 | arXiv 2603.20576 — DAB | Research Paper | UC Berkeley EPIC Lab | 1 | Data Agent Benchmark — 38% pass@1 for Gemini-3-Pro |
| 4 | arXiv 2509.00997 — Agent-First Data Systems | Research Paper | UC Berkeley EPIC Lab | 1 | Position paper — four characteristics of agentic speculation |
| 5 | Simon Willison — Linear Walkthroughs | Blog Post | Simon Willison | 2 | Agent-generated codebase walkthrough + anti-hallucination shell extraction |

## New Findings

| Finding | Priority | Category | Source |
|---------|----------|----------|--------|
| mongodb-single-store-polymorphic-evidence-memory | P2 | Memory Architecture | #1 |
| rank-fusion-hybrid-retrieval-mongodb-atlas | P2 | Memory Architecture | #1 |
| query-decomposition-sub-query-rrf-merge | P2 | Memory Architecture | #1 |
| post-retrieval-reranking-weighted-signal-composition | P2 | Memory Architecture | #1 |
| importance-based-decay-permanent-exemption | P3 | Memory Architecture | #1 |
| surprisal-novelty-as-memory-write-gate | P2 | Memory Architecture | #1 |
| claude-code-context-management-decision-matrix-five-tools | **P1** | Context Engineering | #2 |
| proactive-compaction-before-intelligence-degradation | P2 | Context Engineering | #2 |
| data-agent-benchmark-dab-cross-dbms-pipeline-eval | P2 | Evaluation | #3 |
| agentic-speculation-four-characteristics-data-system-redesign | P3 | Memory Architecture | #4 |
| agent-generated-codebase-walkthrough-for-onboarding | P2 | Context Engineering | #5 |
| programmatic-snippet-extraction-via-shell-anti-hallucination | P2 | Prompt Craft | #5 |

**Priority distribution:** P1: 1, P2: 9, P3: 2

### P1 Highlights

1. **claude-code-context-management-decision-matrix-five-tools** — Anthropic's canonical decision matrix for Continue / /rewind / /compact / /clear / Subagents. Anchor framework for any MetaSystem doc that touches Claude Code context management. The 5-tool vocabulary is now product-official and should be adopted in preference to ad-hoc language.

### P2 Highlights

- **mongodb-single-store-polymorphic-evidence-memory** — Memongo's architectural counter-stance to mem0/Letta/layered enterprise stacks: one database, one collection, one retrieval authority. Testable against multi-store benchmarks.
- **rank-fusion-hybrid-retrieval-mongodb-atlas** — Atlas-native `$rankFusion` / `$scoreFusion` moves hybrid retrieval from application code into the database. Benchmark discipline bonus: `$vectorSearch exact:true` eliminates ANN noise.
- **query-decomposition-sub-query-rrf-merge** — Cheap small-model (GPT-4-mini) sub-query rewrite fanned out into native rank fusion. Natural fit for improving Memongo's weakest LongMemEval-S category (multi-hop/temporal reasoning at 84.0%).
- **post-retrieval-reranking-weighted-signal-composition** — Interpretable alternative to neural rerankers with explicit weights (keyword 0.30, temporal 0.40, entity 0.40, quoted phrase 0.60) — auditable without retraining.
- **surprisal-novelty-as-memory-write-gate** — Upstream write-time filter complementary to downstream decay. Catches redundant-fact-pollution at ingestion.
- **proactive-compaction-before-intelligence-degradation** — Anthropic's argument against deferring `/compact`: "model is at its least intelligent point when compacting." Schedule compaction at stable state, not at capacity pressure.
- **data-agent-benchmark-dab-cross-dbms-pipeline-eval** — 38% pass@1 ceiling for frontier models on enterprise data agent workloads. Reality check for any data-heavy MetaSystem agent work.
- **agent-generated-codebase-walkthrough-for-onboarding** — Periodic agent-generated walkthrough per MetaSystem incubator project could serve as onboarding doc + implicit drift detection.
- **programmatic-snippet-extraction-via-shell-anti-hallucination** — Cheap, directly-adoptable prompt rule: "use `sed`, `grep`, `cat` to extract snippets; don't type from memory."

## Updated Findings

| Finding | What Changed |
|---------|-------------|
| dreaming-memory-consolidation | Added Memongo as corroborating source; cross-linked to importance-based-decay and surprisal-novelty. |
| structured-fact-extraction-from-conversations | Added Memongo corroboration (fact extraction + QA pair generation + session evidence synthesis at ingestion); cross-linked to surprisal-novelty and query-decomposition. |
| trajectory-engineering-non-linear-session-forking | Added Anthropic's canonical framing as official source; promoted from practitioner technique to product-level default. Cross-linked to decision-matrix and proactive-compaction. |
| triple-storage-memory-architecture | Reverse-linked `contradicts → mongodb-single-store-polymorphic-evidence-memory`. Sets up the single-store vs. multi-store architectural debate. |
| hybrid-retrieval-pattern-semantic-lexical-graph | Reverse-linked `extended-by` to three new Memongo retrieval findings. |
| pass-at-k-vs-pass-caret-k-eval-metrics | Reverse-linked `extended-by → data-agent-benchmark-dab`. |

## Crosslink Pass

Forward crosslinks were written inline during finding authoring (~55 entries across the 12 new findings). Targeted reverse crosslinks added to 3 high-value hub findings (triple-storage, hybrid-retrieval-pattern, pass-at-k). No separate `/finding-crosslink` sub-agent batch run this session — the authoring pass was dense enough that a follow-up scan would surface few new candidates. A future periodic crosslink pass against the new findings is low priority.

## Memongo Improvement Surfaces (Nick's question)

Session 45 was framed as "help Nick find ideas to improve Memongo." The intake surfaced six concrete improvement surfaces, captured in `watched-libraries/memongo.md`:

1. **Contradiction handling** — Surprisal novelty catches redundant agreement but not "User said A" followed by "User said not-A." README doesn't detail a contradiction resolver.
2. **Importance score provenance** — How is the score computed, and is it recomputed as corpus grows or fixed at write time?
3. **Decomposition-model choice** — GPT-4-mini sub-query rewrites. Multi-hop/temporal-reasoning is Memongo's weakest LongMemEval-S category (84.0%); a larger decomposer may help.
4. **Reranker weight sensitivity sweep** — Weights appear hand-tuned; publishing a LongMemEval-S sensitivity sweep would strengthen the evidence.
5. **Per-type index tuning** inside a polymorphic `oneOf` collection — benchmarks on non-LongMemEval-S workloads would clarify whether specialized indexes per evidence type are necessary.
6. **External benchmark comparison** — Nick cited Mampalace (~96.6% raw) and Supermemory (~70%); neither appears in the README. Locate and process that leaderboard source in a future scan.

The adjacent P2 findings (query-decomposition, reranking weights, surprisal novelty) each carry their own "Potential Improvements" sections that read as direct improvement menus for Memongo.

## Deferred Items — Status After Session 45

| Deferred Item | Status |
|---|---|
| Playwright DOM selector update (session 42) | Untouched — no new evidence this session. |
| Batch 1 deferred video `ib2m9HVX7as` | Still deferred. |
| `/tmp/metasystem-repo-cache/` cleanup | Untouched. |
| Dark Code channel identity | Untouched — no new evidence. |
| Agentic OS dimension registry trigger | **Count unchanged at 3.** No new Agentic OS findings this session (all routed to Memory Architecture, Context Engineering, Evaluation, or Prompt Craft). Graduation trigger (5 findings) not reached. |
| Mampalace / Supermemory leaderboard | **New deferred item** — referenced by Nick but not in Memongo README. Locate and process in a future scan. |

## Dimension Distribution Check

New findings by dimension:

| Dimension | Count |
|-----------|-------|
| Memory Architecture | 7 |
| Context Engineering | 3 |
| Evaluation | 1 |
| Prompt Craft | 1 |

Memory Architecture is heavily weighted this batch — expected, given the Memongo + arXiv agentic-memory focus. No finding resisted categorization, no new dimension needed. Agentic OS theme remains at 3 findings (threshold 5).

**Implication for G7 (Session Persistence and Memory):** The guide was flagged for re-synthesis at the end of session 44 (+4 Batch 2 findings). Session 45 adds at minimum 7 more Memory Architecture findings plus 2 Context Engineering findings with memory overlap. G7 staleness has grown materially; the re-synthesis is increasingly overdue.

## Watched Libraries Update

Added:
- **Memongo** (spectrum_position: evaluating) — MongoDB-native agent memory. Nick explicitly requested the watch entry despite session scope saying "no new watched libraries this session" — override respected. See `watched-libraries/memongo.md` for the full entry with six improvement surfaces noted.

No other repos added. Mampalace, Supermemory, and the DAB benchmark repo (github.com/ucbepic/DataAgentBench) are in `next-scan-notes.md` for a future `/repo-analyzer` or `/watch-upstream` scan.

## Recommendations

### For Next Codifier Run
1. **Run `/identify-artifacts`** on the 12 new raw findings. Expected classification: mostly pattern, with `programmatic-snippet-extraction-via-shell-anti-hallucination` potentially classifying as rule.
2. **Re-synthesize G7 (Session Persistence and Memory)** — now +11 findings since last synthesis (4 from Batch 2 + 7 Memory Architecture from session 45). Staleness threshold (3+) significantly exceeded.
3. **Re-synthesize G2 (Managing Agent Context)** — gains 3 Context Engineering findings (decision matrix, proactive compaction, walkthrough). Approaching staleness threshold.
4. **Re-synthesize G9 (Agent Governance and Trust)** — still flagged from session 44; not touched this session.

### For MetaSystem
1. **Adopt the 5-tool decision matrix vocabulary** in any CLAUDE.md or skill that references Claude Code context management.
2. **Add the anti-hallucination shell-extraction rule** to any skill that generates outputs containing code snippets (doc generators, PR description writers, walkthrough skills).
3. **Evaluate periodic agent-generated walkthroughs** for incubator projects as onboarding + drift-detection artifact.
4. **Treat 38% pass@1 (DAB result) as baseline** for any frontier-model data-agent work — assume raw reliability is ~1/3 without scaffolding.

### For Memongo
See the six improvement surfaces above and `watched-libraries/memongo.md`. The three highest-leverage ideas Nick could try:
- **Contradiction detector** paired with the existing surprisal novelty gate.
- **Weight-sensitivity sweep** on the reranker coefficients — publishable and directly informs tuning.
- **Larger decomposition model** experiment against the multi-session / temporal-reasoning LongMemEval-S categories specifically.

## Next Scan Notes (Session 45 carry-forward)

Will be applied as an update to `operations/next-scan-notes.md` in this session's close-out.
