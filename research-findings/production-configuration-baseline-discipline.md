---
name: "Production-Configuration Baseline Discipline"
summary: "The benchmark number you publish must come from the same configuration the product ships with. If the 96.6% headline was scored with the product's distinctive features disabled (rooms, compression, selective retrieval) and scores drop 12.4pp when you turn them on, the headline is measuring the substrate, not the product. Plain English: run your benchmark on what you actually sell, not on a stripped-down version that happens to score higher."
implementation_notes: null
category: "Evaluation"
evidence_strength: "Medium (third-party adjudicated + independent-reproduction-corroborated)"
adoption_status: "Not Yet Started"
priority: P2
applicability:
  - "General"
adopted_in: []
sources:
  - "vectorize-mempalace-benchmarks-article.md"
related_findings:
  - file: retraction-log-as-governance-artifact.md
    rel: same-problem
  - file: tool-enforced-dev-heldout-split.md
    rel: same-problem
  - file: benchmark-operating-contract.md
    rel: same-problem
  - file: independent-convergence-retrieval-ceiling.md
    rel: same-problem
  - file: experimental-sandbox-labeling-discipline.md
    rel: extends
  - file: ensemble-eval-majority-required-for-success.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-26"
pipeline_status: synthesized
consumed_by:
  - "guides/verifying-agent-output.md"
---

## What It Is

A benchmark-discipline requiring that published scores be produced by the same configuration the product actually serves. Three specific failure modes this rules out:

1. **Feature-disabled baseline.** Headline number is scored on the underlying substrate (e.g., raw ChromaDB with default embeddings) with the product's distinctive features turned off. The score measures the substrate, not the product. When features are enabled — as they are in production — the score drops materially.
2. **Out-of-path optimization.** The benchmark invocation bypasses layers the production serves through. "Fast path" benchmarks that skip the safety/governance/retrieval layers the product enables.
3. **Scale-free testing.** Benchmark runs on corpora small enough that the product's scalability mechanisms never activate. The product's main value proposition (handling tens of thousands of sessions, millions of tokens) never enters the measurement.

Requirements for a production-configuration baseline:

- **All product features enabled** that a default-configuration user would encounter.
- **Serving path matches.** Benchmark queries traverse the same code path production queries do — same caching, same retrieval stack, same reranking.
- **Corpus size representative.** If the product claims "scales to millions of sessions," benchmarks should exercise at a size where the scalability mechanism matters.

Complements [[ensemble-eval-majority-required-for-success]] (production aggregation rule) and [[benchmark-operating-contract]] (methodology declaration). This finding specifically targets the configuration axis.

## Why It Matters

Agent-memory and agent-harness benchmarks are increasingly used as product-selection signals. A developer reads "96.6% on LongMemEval" and picks Product A over Product B. If the 96.6% is a feature-disabled baseline and real-world performance is 84.2%, the selection was made on noise.

For MetaSystem specifically:
- **Memongo comparative work.** Any LongMemEval numbers we use to position Memongo against competitors need to specify the configuration. If a competitor's headline is feature-disabled, we should either reproduce at the competitor's feature-disabled config (fair-to-headline) or at their production config (fair-to-product) — declared either way.
- **`/assess-*` skills.** When these skills compare against baseline prompts/agents/skills, the baselines need to be the ones consumers actually run, not stripped-down versions that score differently.
- **Future IL benchmarking.** If the IL ever publishes prompt-quality or skill-quality benchmarks, production-configuration discipline applies: test the prompt as it's actually used, not a variant the author never shipped.

Also: this finding is the positive-space counterpart to the feature-disabled-baseline anti-pattern. Per `feedback_positive_space_governance.md`, the positive invariant ("test what you ship") is bounded and enforceable; the rejection list ("don't test stripped-down baselines, don't test out-of-path, don't test at the wrong scale, don't...") is unbounded.

## Why People Are Using It

Documented as an absence by [Vectorize's third-party adjudication of MemPalace benchmarks](https://vectorize.io/articles/mempalace-benchmarks) — see [[vectorize-mempalace-benchmarks-article]] for the source entry. Vectorize's central empirical claim: MemPalace's headline 96.6% uses the raw ChromaDB path with *no MemPalace-specific logic* (confirmed by independent reproduction lhl/agentic-memory, Thin Signal, and GitHub Issue #39). Turning on the actual product features (rooms, compression, selective retrieval) drops performance by up to 12.4pp from the baseline.

The positive-space adoption is inferable from:
- **MemPalace's own retraction log** ([[retraction-log-as-governance-artifact]]) corrects the original table that mixed metrics and configurations. The retraction is evidence that the discipline is becoming normative.
- **Supermemory's separate research page vs blog post**: the 85% number ([[supermemory-research-page]]) is described as the product config; the 99% number ([[supermemory-99-sota-blog]]) is labeled experimental ([[experimental-sandbox-labeling-discipline]]).

So the discipline is currently enforced by third-party adjudicators more than by vendors voluntarily. The load-bearing governance is that readers (and downstream aggregators) demand configuration disclosure; vendors update practice under that pressure.

## Potential Alternatives

- **Publish multiple configurations** (baseline, features-on, at-scale, production). Honest but information-dense. Readers pick the number relevant to their use case.
- **Publish only the production number.** Conservative; loses research-framework insight. The full matrix of what-was-run is not visible.
- **Per-feature ablation reporting.** Publish (config + delta-from-baseline) for each feature. Reveals mechanism; still requires a headline-config choice.
- **Feature-disabled baseline with explicit label.** "Raw substrate baseline: 96.6%; full-product: 84.2%." Honest; requires discipline to prevent the baseline from being promoted to the headline in downstream references.
- **No headline number at all.** Publish only per-category detailed breakdowns. Maximizes honesty; reduces communicability.

## Potential Improvements

- **Configuration hash in every published result.** `config_hash: sha256(...)` so runs are reproducible and anyone can spot config-drift.
- **Leaderboards reject runs that don't publish configuration.** Structural enforcement at the aggregator layer.
- **Feature-enablement audit logs.** When a vendor publishes a benchmark run, log which features were on. Downstream review can recompute.
- **Scale-stratified reporting.** Separate numbers for 500-question / 5K-question / 50K-question / 500K-question corpus sizes. Makes scalability-ceiling effects visible before a reader uses the number.
- **Production-config definition in the product repo.** Vendors commit a `production.config` file or equivalent; any benchmark that cites "production config" must reference this exact file.

## Potential Failure Modes

- **Config drift.** Production config changes between benchmark run and product release; published number is stale. Mitigation: version-pin configs and re-run on change.
- **Gaming via "what's production" redefinition.** When the benchmark-favorable config is declared "production," discipline becomes a rubber stamp. Mitigation: third-party adjudication of production-config claims; independent reproduction against claimed configs.
- **Legitimate exploratory runs suppressed.** Researchers can't publish interesting non-production findings without violating the discipline. Mitigation: combine with [[experimental-sandbox-labeling-discipline]] — exploratory runs explicitly labeled, not folded into product claims.
- **Scale-representative corpora not available.** No agreed-upon 500K-session benchmark exists. Vendors test what's available. Mitigation: acknowledge the scale-testing gap as an open governance problem; encourage community dataset growth.
- **Configuration complexity breaks reader comprehension.** A full config disclosure might run dozens of flags; readers glaze over. Mitigation: short-form summary (feature-list on, version pinned) + long-form appendix (complete flag set).
