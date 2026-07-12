---
type: "delta-report"
topic: >-
  Session-136 Pass 2 extraction sweep — the 28 Nick-accepted KB-ONLY video sources
  from the 2026-07-12 link-intake triage, plus the two Anthropic primary-source
  fetches. Companion to the wave-2 retry addendum (0/20 recovered).
date: "2026-07-12"
input: >-
  operations/research-reports/2026-07-12-link-intake-triage.md (verdicts + pairing
  instructions); transcript cache app/transcript-fetcher/transcripts/
---

# Delta Report — 2026-07-12 (Session 136 extraction sweep)

## Scan Summary

- **Mode:** Pass 2 transcript deep extraction (no web scan, no arXiv scan)
- **Sources processed:** 30 — the 28 KB-ONLY videos (8 topical subagent clusters) + 2
  Anthropic primary blogs fetched per the triage follow-up queue
- **New findings:** 65 across the 8 clusters + the field-guide technique set
- **Existing findings updated:** 24 (recency-weighted updates, corroboration
  annotations, and 2 first-party evidence upgrades)
- **Authorities:** 5 existing entries updated; 8 new entries created (standard Step 5
  mechanics); 3 candidates held for the Nick gate (Nate Herk, Tonbi's AI Garage,
  Austin Marchese)
- **Pairing instructions honored:** OKF spec-conventions finding written once
  (2 sources); Marchese three-bucket finding written once (2 sources); Pocock pair
  processed as one cluster; Nate-Jones econ pair extracted as one shared framework
- **Validator:** corpus-wide `validate_frontmatter.py` exit 0
- **Previous report:** 2026-07-12 link-intake triage (session 135)

## New Findings (by cluster)

### OKF / knowledge substrate (3)
`okf-open-knowledge-format-curated-bundle-spec` (P2), `knowledge-substrate-standardization-cross-agent-interop` (P2), `curated-spine-plus-rag-hybrid-query-router` (P3)

### Second brain / memory / folder structure (11)
`query-shape-first-storage-design` (P2), `evergreen-vs-volatile-ingestion-rule` (P2), `per-folder-heterogeneous-retrieval-levels` (P2), `memory-wiki-world-kb-trichotomy` (P2), `stateful-mcp-subprocess-vs-cli-shell-out` (P2), `docs-split-by-lifespan-not-topic` (P2), `root-context-file-edit-guard` (P2), `escalating-search-order-routing` (P3), `markdown-git-system-of-record-derived-disposable-db` (P3), `write-back-discipline-memory-is-not-the-brain` (P3), `distribution-as-floor-raising-one-click-skill-buttons` (P3)

### Harness / infrastructure (6)
`harness-composition-six-pattern-taxonomy` (P2, **upgraded to Strong** on the primary), `agent-owner-card-human-facing-registry` (P2), `pairwise-tournament-judging-over-absolute-scoring` (P3), `ai-gateway-model-traffic-layer` (P3), `smart-model-routing-catch-22` (P3), `job-diet-boundaries-review-loop-operating-framework` (P3), `semantic-caching-failure-modes` (Not Flagged)

### Skills / prompting — Pocock pair (8)
`leading-words-lexical-steering-reasoning-trace-verification` (P2, Strong), `leg-work-amplification-hiding-future-steps` (P2), `branch-analysis-externalization-rule-skill-reference` (P2), `skill-pruning-failure-modes-noop-deletion-test` (P2), `reference-only-skill-shape-for-afk-agents` (P2), `wayfinder-issue-tracker-decision-map` (P3), `fowler-code-smell-names-as-prior-invocation` (P3), `two-axis-parallel-code-review-standards-vs-spec` (P3)

### Loops / self-improvement (12)
`ecosystem-monitoring-meta-loop` (P2), `north-star-drift-loop-trajectory-extrapolation` (P2), `three-bucket-change-approval-tiering` (P2, governance-gated — touches DD-29), `session-history-mining-for-skill-discovery` (P2), `with-without-skill-ab-baseline-measurement` (P2), `persona-clone-review-board` (P2), `critical-call-checkpoint-gate-placement-heuristic` (P3), `process-optimizer-agent-loop-improvement` (P3), `multi-perspective-review-council` (P3), `automation-verification-gate-skill` (P3, corroborates Rule 11), `closed-loop-floor-open-exploration` (P3), `legible-executable-verifiable-agent-readiness-triad` (P3)

### Models / economics — econ pair (4)
`center-vs-edge-of-distribution-task-classification` (P2), `harness-non-portability-across-model-families` (P2, Strong — Lindy rewrite), `prototype-at-frontier-then-downshift` (P2), `frontier-capability-probing-scouting` (P3)

### Fable usage / cost engineering (14)
`war-game-plan-format-for-executor-handoff` (P2), `effort-level-tuning-as-first-order-cost-lever` (P2), `nine-primitive-document-agent-skeleton` (P2), `receipt-artifact-as-agent-trust-mechanism` (P2), `enumerate-dont-fix-hostile-reviewer-prompt` (P2), `task-risk-gradient-for-verification-depth` (P2), `seven-rung-minimal-code-decision-ladder` (P2), `frontier-model-as-unknown-unknown-elicitor` (P3, **first-party upgraded** same session), `on-policy-vs-naive-trace-distillation` (P3), `structure-addressed-retrieval-for-cited-document-domains` (P3), `data-normalization-as-cheap-model-enabler` (P3), `cross-vendor-adversarial-build-attack-loop` (P3), `measured-delta-and-staging-clone-for-ai-refactors` (P3), `on-demand-vs-always-on-skill-activation` (Not Flagged — validates existing engine design)

### Multi-agent / agentic engineering (6)
`work-ticket-contract-prompt-mode-vs-work-mode` (P2, schematic candidate), `dev-cost-estimation-bias-correction` (P2), `memory-file-to-skill-migration` (P2), `no-mistakes-post-implementation-validation-pipeline` (P2), `skill-popularity-vs-measured-efficacy` (P2), `autonomy-progression-gated-by-maturity` (P2)

### Anthropic primaries (1 + 2 upgrades)
`unknowns-reduction-phase-anchored-technique-set` (P2). First-party upgrades applied: `frontier-model-as-harness-designer` → **Strong (production-tested)** (Bun Zig→Rust case study; shipped /deep-research skill); `harness-composition-six-pattern-taxonomy` → Strong, with the naming correction (first-party "adversarial verification" vs the digest's "worker-critic").

## Updated Findings (highlights — full lists in each cluster's files)

Recency-weighted reframes Nick should see:
- `advisor-executor-api-pattern` — "API feature, not Claude Code" caveat superseded by the CLI `/advisor` surface; old framing kept as lineage.
- `dark-factory-ai-only-codebase-management` — author-retrospective failure-mode taxonomy added (cascading failures, stalled handoffs, evaluation gaming).

Corroboration annotations staged for `/reassess-priorities` (priorities untouched):
- thin-router + scale-threshold cluster (`scale-threshold-heuristic-obsidian-vs-rag`, `intent-based-meta-routing-skill`, `skills-as-pointers-to-second-brain-files`) — 4+ independent channels
- `generator-assessor-separation-in-skill-iteration` — third independent corroboration (rule 10)
- DD-108 supervised-autonomy set (`trust-calibration-progressive-autonomy-ramp`, `autonomy-gradient-not-binary-delegation`, `human-on-the-loop-hotl-autonomy-tiering-framework`) — 3 distinct source sets
- `frontier-model-as-harness-designer` — hub finding, 3 extending sources + first-party upgrade
- `three-bucket-change-approval-tiering` — 3 independent sources at creation

## Blocked

The 20-video retry backlog remains blocked (wave-2 retry failed same-day; IP-level 429).
See `2026-07-12-link-intake-triage-wave2.md` — retry ≥1 calendar day out.

## Follow-ups filed by this sweep (not actioned)

- Source→authority backfill: the 8 new authority entries list their sources, but several
  new source entries carry empty `authority` arrays — a `/linkage-repair` pass target.
- related_findings reciprocity: subagents recorded one-way links into lanes they didn't
  own (by design) — a `/finding-crosslink` pass target.
- Duplicate authority pair noted: `nate-b-jones.md` vs `ai-news-strategy-daily-nate-b-jones.md`
  (merge candidate, echoes the known duplicate-source pair).
- CLI-first rule refinement: `stateful-mcp-subprocess-vs-cli-shell-out` proposes a
  statefulness clause for `prefer-cli-over-mcp-when-both-exist` — Codifier lane.
- `/maintain-docs` docs-lifecycle deltas named in `docs-split-by-lifespan-not-topic`
  implementation_notes.

## Recommendations

### Priority 2 (Design Required) — richest Codifier seams
1. **Harness substrate cluster:** six-pattern taxonomy (Strong) + work-ticket contract +
   pairwise tournament — direct schematic-library / future `/design-harness` input.
2. **Skill-authoring substrate cluster (Pocock):** six rubric-relevant axes flagged for
   the `/assess-skill`//design-skill` criteria refresh (restructure Phase 2).
3. **Plan-artifact cluster:** war-game format + decision-led ordering + Deviations log —
   candidate enrichment for engine handoff/plan templates.
4. **Reduce-Nick-bottleneck cluster:** three-bucket approval tiering (governance-gated,
   DD-29) + receipt artifacts + quiz-me gate — DD-108 trajectory material.

### Priority 3 (Monitor)
Gateway/model-traffic layer (no engine surface yet), distillation evidence (no
fine-tuning surface), OKF spec maturation (v0.1 single-vendor draft).

## Evaluation Handoff

**Queue `/reassess-priorities`** on the five corroboration sets listed above — the
evidence-strength deltas are annotated in-file and ready for the Curator pass.
