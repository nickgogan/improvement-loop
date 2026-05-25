---
name: "Data Agent Benchmark (DAB) — Cross-DBMS Pipeline Evaluation"
summary: "UC Berkeley's Data Agent Benchmark evaluates AI agents on full-pipeline enterprise data work: integration, transformation, and analysis across multiple heterogeneous database systems. 54 queries, 12 datasets, 9 domains, 4 DBMS types. Best frontier model (Gemini-3-Pro) achieves only 38% pass@1. Grounded in a formative study of enterprise workloads across six industries. First benchmark to move beyond single-task NL-to-SQL into cross-system agent reliability."
implementation_notes: "For MetaSystem: useful reality-check on frontier-model reliability for data-heavy agent workloads. 38% pass@1 is the current ceiling — if a sub-pipeline in MetaSystem asks a frontier model to reason across heterogeneous data sources (e.g., Notion + files + API responses), expect low raw reliability without guardrails, retrieval scaffolding, or verification loops. The benchmark itself (github.com/ucbepic/DataAgentBench) is worth running if we build any data-agent capability."
category: "Evaluation"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
priority: "P2"
applicability:
  - "General"
adopted_in: []
sources:
  - "arxiv-2603-20576-data-agent-benchmark-dab.md"
related_findings:
  - file: pass-at-k-vs-pass-caret-k-eval-metrics.md
    rel: extends
  - file: holdout-validation-pattern-blind-regression.md
    rel: same-problem
  - file: agent-self-reporting-unreliability-independent-eval.md
    rel: same-problem
  - file: acceptance-criteria-as-verifiable-eval-anchor.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: synthesized
consumed_by:
  - "building-agent-evaluation-suites.md"
---

## What It Is

The Data Agent Benchmark (DAB) is a 54-query evaluation spanning 12 datasets, 9 domains, and 4 database management systems. Unlike prior benchmarks that test individual sub-tasks (NL-to-SQL, small-table QA), DAB evaluates the full pipeline of:

1. **Integration** — combining data from multiple heterogeneous sources.
2. **Transformation** — cleaning, joining, reformatting.
3. **Analysis** — answering the user's natural-language question.

Grounded in a **formative study of enterprise data agent workloads across six industries**, so the query shapes reflect real-world data-fragmentation patterns: inconsistent entity references, mixed structured/unstructured data, cross-DBMS joins.

Headline result: **best frontier model (Gemini-3-Pro) achieves only 38% pass@1 accuracy**.

## Why It Matters

Most agent-eval work lives in closed, well-scoped benchmarks (SWE-bench for code, HumanEval for programming) where the agent operates in a single-system world. Enterprise reality is the opposite — data is fragmented across Salesforce, a data warehouse, production Postgres, legacy Oracle, S3 buckets of CSVs. DAB is the first published benchmark to put that full pipeline in front of frontier models and measure.

The 38% pass@1 figure is the load-bearing datapoint. It means:
- Naive "ask a frontier model to answer a data question" workflows will fail ~60% of the time on realistic enterprise queries.
- Any production data agent needs verification loops, retrieval scaffolding, or human gates — you cannot rely on raw frontier-model reliability.
- Reporting single-trial success numbers in this regime is meaningless without explicit `pass^k` considerations (see [[pass-at-k-vs-pass-caret-k-eval-metrics.md]]).

## Why People Are Using It

Published March 2026 by UC Berkeley EPIC Lab (Parameswaran group) and collaborators. Benchmark code at github.com/ucbepic/DataAgentBench. Authors also published the companion agent-first data systems vision paper ([[agentic-speculation-four-characteristics-data-system-redesign.md]]).

Adoption outside the authoring group is early — this is a recent publication and too new for broad industry use, but the benchmark's framing (enterprise-grounded, full-pipeline, cross-DBMS) makes it a likely canonical reference for enterprise data-agent evaluation.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Spider / BIRD (NL-to-SQL) | Single-DB text-to-SQL benchmarks | When evaluating SQL generation in isolation |
| Custom enterprise eval | Hand-rolled queries specific to your stack | When your data shape is unusual and DAB doesn't reflect it |
| End-to-end integration tests | Test the agent against a staging copy of production | For final gating before deployment, when DAB-style benchmark is too abstract |

## Potential Improvements

- Integration with agent harnesses — DAB measures a model in isolation; a harness-aware version would measure different agent frameworks.
- Longitudinal tracking — rerun the benchmark on each frontier release to plot reliability over time.
- Per-failure-mode breakdown — 38% pass@1 hides which sub-tasks fail most. The paper includes failure-mode analysis; worth distilling in a follow-up extraction.

## Potential Failure Modes

- **Small benchmark size** (54 queries) — statistical power on per-model comparisons is limited.
- **Formative study sampling bias** — six industries may not cover the shape of the workload you care about.
- **Benchmark gameability** — once published, models can be tuned against it; the pass@1 numbers drift up without a corresponding real-world improvement.
- **Heavy LLM-cost to evaluate** — running 54 pipeline queries across frontier models is non-trivial.
