---
name: "Benchmark Operating Contract — Lane Taxonomy and Publishable-Claim Invariants"
summary: "A discipline document governing how benchmark numbers become public claims. Separates benchmark runs into named lanes (official / internal / regression / advisory / release-proof) with different standards for publishability. Every result carries a machine-checkable receipt (dataset, commit, topology, embedding, command). No receipt → not publishable. Blocks apples-to-oranges comparisons and question-patching."
implementation_notes: "Adoptable by any MetaSystem component that publishes numbers (IL finding priorities, agent performance scoring, MetaSystem-scoped benchmarks). Start with the core rule (`numbers are product claims only when the run proves the product path being claimed`) and the receipt envelope; lane taxonomy and release gates can follow if volume warrants."
category: "Evaluation"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: null
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: benchmark-signal-mismatch-optimization-gap.md
    rel: same-problem
  - file: infrastructure-noise-agentic-eval-confounding.md
    rel: same-problem
  - file: eval-awareness-autonomous-benchmark-identification.md
    rel: same-problem
  - file: cross-provider-benchmarking-framework.md
    rel: same-problem
  - file: tool-enforced-dev-heldout-split.md
    rel: extended-by
  - file: benchmark-dataset-deprecation-lifecycle.md
    rel: same-problem
  - file: ensemble-eval-majority-required-for-success.md
    rel: same-problem
  - file: production-configuration-baseline-discipline.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-23"
pipeline_status: raw
consumed_by: []
tags:
  - "evaluation"
  - "benchmark"
  - "governance"
  - "memongo"
  - "publishable-discipline"
---

# Benchmark Operating Contract — Lane Taxonomy and Publishable-Claim Invariants

## What It Is

A rule set Memongo uses to decide when a benchmark number is allowed to become a public claim.

Three moves:
1. **Separate lanes for separate purposes.** Every benchmark run is assigned to one of five lanes, each with its own standard. Only the "official retrieval" and "proof pack" lanes can produce public numbers. Internal regression and advisory probes stay internal unless explicitly labeled otherwise.
2. **Every result comes with a receipt.** Alongside the score, the system records a structured envelope: dataset version, code commit, MongoDB topology, embedding model, exact command, and any warnings/degradations. The envelope is machine-checkable. No complete envelope → not publishable.
3. **Can't cherry-pick the corpus.** If the benchmark didn't score every question (`corpus.scoredCases === corpus.cases`), the result is a warning, not a publishable win. Also: "do not compare numbers from different corpora, embedding models, or MongoDB topologies without labeling the comparison as non-equivalent."

The five lanes: **Official retrieval** (publishable), **Internal retrieval** (internal diagnostic only), **Conversation recall regression** (regression gate only), **Query governance** (advisory only), **Proof pack** (release evidence).

## Why It Matters

For MetaSystem specifically: this is a ready-made discipline we can adopt the moment we start publishing any kind of score — IL finding priorities backed by confidence metrics, agent performance over time, skill/guide effectiveness measurements, cross-repo comparison numbers. Without it, we drift into "our number looks good" without being able to prove the number means what we say. With it, any number we put in front of Nick (or eventually a third party) comes with its own audit trail.

The contract also provides concrete guardrails against two common benchmark-engineering failures that have already surfaced in the KB's own source cluster: (a) the "patch the 3 questions you failed, retest on the same set, claim 100%" move (MemPalace's disclosed methodology issue — see `operations/next-scan-notes.md` leaderboard bullet); (b) the "compare retrieval recall against end-to-end QA accuracy" move that makes systems look better than they are.

## Why People Are Using It

Observed in [Memongo](https://github.com/romiluz13/Memongo) (latest, 2026-04-23) — see `[[memongo-analysis]]` for structural details. Memongo is a MongoDB-native long-term memory framework for AI agents whose primary public claim is a LongMemEval-S score (R@5 98.1% with `$vectorSearch exact:true` for zero ANN noise). The contract exists because the maintainer wanted that claim to survive scrutiny; the publishable-claim invariants are what make the claim defensible. The build-identity envelope is concrete enough to wire into CI: env vars (`MEMONGO_BUILD_COMMIT`, `MEMONGO_BUILD_ID`, `MEMONGO_BUILD_LABEL`) with CI fallback to `GITHUB_SHA`, `GITHUB_RUN_ID`, `VERCEL_GIT_COMMIT_SHA`, `VERCEL_DEPLOYMENT_ID`.

Pattern is transferable to any agent framework or pipeline tool that wants to publish performance numbers without drifting into vendor-benchmark fiction.

## Potential Improvements

- **Judge/evaluator identity in the envelope.** Memongo's envelope records build and corpus but the source doc doesn't explicitly log which LLM judge (e.g., GPT-4o at specific version) evaluated LLM-as-judge runs. Judge drift is a real confound.
- **Cross-run diff registry.** The contract records PR and release deltas (base commit vs candidate, `hitRate`, `emptyRate`, `p95LatencyMs`, `rAt5`, `rAt10`, `ndcgAt10`) but doesn't define how/where those diffs are persistently archived for trend analysis.

## Potential Failure Modes

- **Receipt completeness is soft-enforced.** The contract is a doc, not a machine-enforced gate. An agent or maintainer who skips recording the topology or embedding still ships; the publishable-claim check catches the publication, not the run. Full hardening would require CI wiring.
- **Lane boundaries require maintainer discipline.** "Internal diagnostic" vs "official win" is a label decision. If the label slips, the public claim inherits internal-diagnostic error bars without disclosing them.
