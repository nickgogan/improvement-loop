---
title: "Calibration registry — empirical operating numbers for engine skills"
type: "resource"
target_system:
  - "improvement-loop"
created: "2026-07-13"
updated: "2026-07-13"
---

# Calibration Registry

Raw empirical numbers from the engine's own operating history, distilled once from
the frozen System Log corpus (IB-176 ship step 2; design note §5). **Numbers only,
never behavioral instructions.** Each section names its consumer skill and the
read-moment — read on demand at that moment, never at cold-start. New numbers land
here via `/self-improve` (scan mode routes them; source citation required). A
section never consumed across ~3 scans is flagged for a gated pruning decision.

Every figure carries its date — treat older numbers as priors, not truths; the KB,
models, and skills have all evolved since the early measurements.

## /research-loop — read when planning extraction passes and sizing batches

- Transcript vs summary extraction density: 17.6 patterns/video (transcript) vs 2.1
  (Perplexity summary) = 8.4×; summary-only miss rate 46.5% — worst-missed:
  implementation details 31%, named patterns 23%, tool names 15%,
  process/methodology 15%, numbers 9%, architectural concepts 7% (2026-04-07).
- Pass 2 deep-extraction yield: 15 under-extracted video sources → 100 new + 47
  updated findings ≈ 6.7 new/source (2026-05-25); 131 flagged "missed patterns"
  compressed to 21 genuinely-new ≈ 16% genuine (2026-04-07).
- Pass 1 intake yield: Anthropic blog corpus ~1.9 new + ~2 updated findings/post
  (2026-04-09); mixed 5-source batch → 12 new + 3 updated (2026-04-20); 23 Tier-1/2
  sources → 59 new via 5 parallel agents (2026-04-07).
- Wave sizing: 3–4 sources per extraction subagent recurs across batches
  (2026-04-07 … 2026-05-25).
- Context budget: 14 sources → 17 findings + 3 authorities ≈ 40% of a 1M window;
  dense sources cost disproportionately (≈900-line docs, ≈10K-word transcripts)
  (2026-04-23).

## /link-intake — read when sizing a batch

- 18 links → 17 new findings + 11 sources + 3 watched-libraries (2026-05-24);
  6 links → 12 findings + 4 analysis docs (2026-05-24).

## /identify-artifacts — read post-run as a distribution sanity check, and when sizing fan-out

- Pattern-share baseline ≈ 92% (session-22 calibration). Observed: 94% (17/18),
  92.9% (26/28), 91.7% (11/12), 89% (64), 83% (90), 100% (5/5, 2026-07-13).
  **Corpus-type caveat:** practitioner/production-technique corpora run 15–20 pts
  below baseline — 76% (13/17), 74% (14/19), 80% (12/15) (2026-04-24…2026-05-25).
  Large deviation unexplained by corpus type = rubric-drift signal.
- Guided-tier redirect rate on human review: 8/31 ≈ 26% redirected to pattern
  (2026-05-25).
- Fan-out sizing: ~6–7 findings per Sonnet subagent (28 → 4 subagents; 17 → 3
  batches of 6/6/5); ≤12 findings → run inline, below batch-efficiency threshold
  (2026-04-20/26).

## /extract-artifacts — read when sizing drafting/harvest fan-out and reviewing tiers

- Drafting batch envelope: 3–6 artifacts per subagent (41 via 7 subagents; 40 via 8
  with 0 validation failures; 26-file backfill as 4 batches of ~6–7)
  (2026-04-24 … 2026-05-25).
- Harvest-mode throughput: 20 whole-skill-invocation subagents in 3 form-batched
  waves (11 rules → 6 skills → 3 templates) in one session (2026-04-27).
- DD-97 extension-proposal fire rate: rules ≈ 14% cumulative (3/22), skills and
  templates 0%; false-positive volume 0 at that calibration (2026-04-27).

## /synthesize-guide — read when planning a regen and its ruling session

- DD-101 harvest candidate-per-finding density by cluster shape: mid cluster (G7)
  8/27 ≈ 30%; large (G2) 16/44 ≈ 36%; small/governance (G9) 14/16 ≈ 87.5% —
  policy-shaped findings run far denser (2026-04-26/27).
- Guide lifecycle thresholds (empirically exercised): staleness re-synthesis at +3
  newly-routed findings; bifurcation evaluation at 45 findings (DD-102; G2 split at
  64 → 35+30); new-guide graduation at 5; sub-dimension graduation at ≥10
  (2026-04-20 … 2026-05-25).

## /finding-crosslink — read when calibrating subagent prompts and validation sampling

- Error rates by evaluation depth: bulk-migration classification 85% error (5/34
  correct); summary-only dedicated evaluation ≈ 40% FP on `enables`, ≈ 30% FP on
  `same-problem` (≈60% on deliberately-borderline samples), ≈ 0% on `contradicts`;
  post-write deep validation caught 2.3% FP (5/218) (2026-04-08).
- Subagent precision bias: ≈ 32% miss rate on true links — a manual second pass
  recovered 15 links on top of 32 subagent-approved (2026-04-19).
- Throughput: full-KB pass = 800 candidate pairs via 16 parallel Sonnet subagents
  at 50 pairs/batch (2026-04-08); incremental post-intake pass hit rate ≈ 3.5%
  (28/800, 2026-04-20); ~800 pairs per ~29 new findings (2026-05-24).
- Structure: hub soft cap ≈ 15 links/finding; KB `enables` base rate ≈ 5% of links;
  isolation baseline 39.0% → 23.8% after first full pass (2026-04-08).

## /linkage-repair, /source-triage — read when deciding whether a maintenance pass is due

- First-audit baselines: 43% of sources (32/74) had zero linked findings; 39%
  finding isolation (2026-04-07/08).

## /promote-findings, /repo-analyzer — read when estimating a repo-intake session

- Dedup rate on mature KB: ≈ 69% of individual candidates (36/52) duplicated
  existing findings (2026-05-25).
- Structural-analysis subagent runtime ≈ 5 min/repo (2026-05-25).

## /watch-blogs — read when triaging an Anthropic-blog batch

- Signal density: 17/18 posts passed relevance; 21/24 EXTRACT verdicts ≈ 175
  estimated patterns; top posts 11–19 patterns each; neither Anthropic blog has RSS
  (WebFetch discovery required) (2026-04-09).

## /audit-artifacts — read at Step 2–4 sizing and pre-run cost estimation

- Bin-packing constants: 250k-token ceiling per Librarian subagent (ceiling, not
  floor); variant-aware substrate estimates {skill 18k, agent-A 22k, agent-B 32k,
  agent-C 28k, prompt 20k}; FFD packing; MOC pre-filter skips CLAUDE.md with body
  <100 words or `type: index` (2026-06-12).
- Observed run costs: IL 43 artifacts → 9 bins, ~7 min, ~1.6M subagent tokens
  (est.); MetaSystem 8 artifacts → 2 bins (212.5k + 187.0k), ~3 min, ~340k actual
  (2026-06-12).

## /reassess-priorities — read when applying the P1 evidence rubric

- P1 threshold in practice: 5+ independent sources with production evidence — held
  correctly at 3, fired cleanly at a conservative count of 5 (2026-04-24/26).

## /detect-drift — precedent for codifying deterministic steps

- Deterministic-helper read collapse: O(2N) LLM file reads → 1 script call + O(K)
  source reads; measured 62 reads → 2 (2026-04-26).

## /cleanup-cache — read when judging purge timing

- Repo-cache footprint ≈ 70 MB/repo (976 MB for 14 clones, 2026-05-25).

## Codifier gating cadence — read when proposing autonomy-tier changes

- Recommendation accuracy vs Nick rulings: 51/51 (100%) cumulative — 38/38
  harvest-queue recos + 10/10 Branch-B drafts + 3/3 Branch-C Option-A matches
  (2026-04-27).

## Librarian reference layer — read when authoring operation/concept files

- File budgets: operation files ≈ 600 lines, concept files ≈ 300 lines,
  split-when-forced (2026-04-21).

## Sweep-session planning (no dedicated skill) — read when triaging rolled-forward backlog

- Locate-only backlog economics: 46% of items (6/13) yielded net-new findings at
  ~5 min actual cost each; 23% (3/13) were already-resolved bookkeeping lag
  (2026-04-23).
