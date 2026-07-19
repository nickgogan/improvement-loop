---
name: "Ensemble Eval: Require Majority Agreement, Not Union-of-Successes"
summary: "When an ensemble system reports a success rate, the aggregation rule matters enormously. 'Union-of-successes' — success if any of N independent paths reaches the correct answer — systematically inflates scores and has no production analog (you can't run 8 paths and know which one was right). The disciplined aggregation is majority-vote or best-of-N with a picker; report that, not the union. Plain English: 'we got 99% because at least one of our 8 runs was right' doesn't mean 99% of real users got the right answer. Only the vote-then-report number tells you what the product actually does."
implementation_notes: null
category: "Evaluation"
evidence_strength: "Medium (practitioner-documented + inferential)"
adoption_status: "Not Yet Started"
priority: P2
applicability:
  - "General"
adopted_in: []
sources:
  - "supermemory-99-sota-blog.md"
related_findings:
  - file: tool-enforced-dev-heldout-split.md
    rel: same-problem
  - file: benchmark-operating-contract.md
    rel: same-problem
  - file: production-configuration-baseline-discipline.md
    rel: same-problem
  - file: repeated-sampling-scaling-law-and-verifier-ceiling.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-07-13"
pipeline_status: synthesized
consumed_by:
  - "guides/verifying-agent-output.md"
---

## What It Is

A discipline for aggregating ensemble / multi-path evaluation results. Ensemble systems run N independent reasoning paths per query (multiple prompts, multiple models, multiple decompositions) and produce N answers per question. To report a single "accuracy" number, the evaluator must pick an aggregation rule:

- **Union-of-successes** (anti-pattern): score the question correct if *any* of the N paths reached ground truth. Inflates the reported number because the probability that at least one of N independent imperfect classifiers is right approaches 1 as N grows. No production analog exists — at serve time the system can't run 8 paths and retroactively pick "the one that would have been right."
- **Majority vote**: score the question correct if the majority of N paths agree and agree on the correct answer. Closer to a production aggregation (run the ensemble, take the majority). Score is bounded above by the per-path ceiling, not inflated.
- **Best-of-N with picker**: train/select a picker model that chooses among the N paths per query. Production-realizable if the picker is cheap enough. Score reflects picker quality, not union inflation.
- **Single-path with seed variance**: run one path per query, report variance across seeds. Standard in ML; orthogonal to ensemble aggregation questions.

The discipline: whichever rule the production system uses is the one to report. If the production serves the output of a majority vote, report majority-vote accuracy. If the production serves the output of a picker, report picker-chosen accuracy. If the production runs one path, report single-path accuracy. Never report union-of-successes as "the accuracy."

## Why It Matters

Agentic systems increasingly use ensembles of reasoning paths. When the ensemble is reported as "N parallel agents / M variants / K-variant decision forest," a casual reader assumes the final output is some kind of aggregated consensus. If the published accuracy is actually union-of-successes, the number is uninterpretable as a product capability claim.

For MetaSystem's future IL artifacts:
- **Prompt evaluation via `/prompt-evaluator`.** If we ever evaluate a prompt with ensemble rubrics (multi-dimension scoring with multiple LLM judges per dimension), the per-dimension score needs a declared aggregation rule. Union across judges = inflated; majority or single-judge-with-seed-variance = honest.
- **`/assess-skill`, `/assess-agent`, `/assess-prompt` outputs.** These audits rely on LLM judgment; when that judgment is sampled multiple times, how we aggregate is load-bearing.
- **Any benchmark MetaSystem publishes.** For comparing internal agent patterns, the aggregation discipline has to be declared up front; anything else invites union-inflation drift.

Complements [[production-configuration-baseline-discipline]]: that finding says "test the config you ship"; this one says "aggregate the way you ship." Both close union-of-tricks loopholes in benchmark publication.

## Why People Are Using It

The anti-pattern is documented in [Supermemory's 99% SOTA ASMR blog post](https://supermemory.ai/blog/we-broke-the-frontier-in-agent-memory-introducing-99-sota-memory-system/) — see [[supermemory-99-sota-blog]] for the source. The headline result: 99% on LongMemEval_s via an 8-variant decision forest. The disclosed aggregation rule: *"if _any_ of the 8 distinct reasoning paths successfully arrived at ground truth."* This is union-of-successes. The vendor labels the system as experimental (per [[experimental-sandbox-labeling-discipline]]) and discloses the aggregation rule in the same post — so the governance is transparent. But the published number is not what a user running the system would see.

Counter-example: MemPalace's 99.4% R@5 from two independent pipelines ([[independent-convergence-retrieval-ceiling]]) uses each pipeline's best single-path score and compares them. It's not union-of-successes — the 99.4% applies to each pipeline individually. That's a disciplined ensemble claim.

The discipline itself — declare the aggregation rule, prefer majority/picker/single-path over union — is implicit in all rigorous ML benchmark publication (SuperGLUE, HELM, MMLU-Pro all specify). What makes this finding load-bearing is the agent-memory space's tendency to run experimental ensembles and report union-style, obscuring the production-available number.

## Potential Alternatives

- **Union-of-successes with explicit labeling.** If you report it, label it: "Union of 8 paths: 99%; majority vote: 85%; single-path median: 82%." Preserves research insight without inflating the marketing surface.
- **Always report single-path accuracy + path count.** Simple, defensible, uninflatable. Loses information about ensemble structure.
- **Pareto frontier reporting** (accuracy vs latency/cost). When the ensemble has real latency/cost implications, a single accuracy number understates the tradeoff; publish multiple (N, accuracy, cost) points.
- **Replayable ensembles.** Publish the per-question path outputs so any reader can recompute under any aggregation rule they care about. MemPalace's per-question JSONL commits ([[benchmark-operating-contract]]) enable this.

## Potential Improvements

- **Standardize an "aggregation rule" metadata field** on every published benchmark result: `aggregation: single-path | majority-vote | best-of-N-picker | union-of-successes`. Aggregators (REM Labs, leaderboards) can then annotate or filter.
- **Adopt a published-configuration-must-match-product-configuration norm.** If the product serves single-path, the leaderboard number must be single-path. Link to [[production-configuration-baseline-discipline]].
- **Cross-aggregation audit reports.** When a vendor publishes union-of-successes, third-party adjudicators compute the other aggregation rules from the same data and publish the comparison.
- **Picker training as a requirement for best-of-N claims.** You don't get to report "best-of-8" without demonstrating the picker exists and runs in production latency.

## Potential Failure Modes

- **Aggregation rule not disclosed.** Most vendor publications don't specify. Readers assume whichever interpretation favors the vendor. Mitigation: treat missing aggregation rule as reason to exclude a result from comparative analysis.
- **Aggregation rule changes mid-publication.** A vendor starts reporting single-path, then switches to majority-vote when single-path degrades. Looks like improvement; is actually aggregation-rule drift. Mitigation: require aggregation-rule to be a tuple element on every published score (per [[benchmark-dataset-deprecation-lifecycle]] discipline).
- **Union disguised as "ensemble diversity."** Framing the union rule as a feature ("our system tries 8 different approaches!") obscures that the reported number isn't what the user gets. Mitigation: the number reported has to match the serving configuration, period.
- **Single-path reporting that hides best-path selection.** Publishing "single-path" numbers where the path was selected post-hoc from several candidates is union-with-extra-steps. Mitigation: path selection has to be per-query reproducible from the reported configuration, not from a human picker.
