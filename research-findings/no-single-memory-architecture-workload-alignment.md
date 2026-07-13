---
name: No Single Memory Architecture Dominates — Align Structure to the Workload Bottleneck
summary: 'Ends the "which memory framework is best" question for us: a systematic 12-system benchmark shows

  every architecture wins somewhere and loses somewhere else, so the design question is which

  bottleneck your workload has, not which system is best. Trace-preserving stores win

  long-conversation QA, graph/temporal stores win cross-session aggregation and knowledge updates,

  raw long context wins order-sensitive procedural work but collapses under distractors. Also

  corroborates the verbatim thesis: retaining original content beats added abstraction, and heavy

  structure costs orders of magnitude more without proportional accuracy gains.'
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (empirical benchmarks)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- General
adopted_in: []
sources:
- arxiv-agent-native-memory-system-survey.md
related_findings:
- file: four-module-agent-memory-decomposition.md
  rel: extends
- file: verbatim-storage-thesis-for-memory.md
  rel: extends
- file: converged-memory-substrate-vs-patchwork.md
  rel: same-problem
- file: production-memory-architecture-spectrum.md
  rel: extends
- file: four-module-agent-memory-decomposition.md
  rel: enabled-by
- file: memory-system-evaluation-triad-storage-injection-recall.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-11'
last_updated: '2026-07-13'
---

## What It Is

The headline result of the first systematic which-architecture-for-which-workload comparison of
agent memory systems: 12 representative systems + 2 baselines (long context, naive RAG) evaluated
across 5 benchmark workloads spanning 11 datasets. Per-workload winners differ:

- **Long-conversation QA (LoCoMo):** trace-preserving memories strongest (MemoChat, MemOS)
- **Cross-session aggregation (LongMemEval):** temporal/graph-organized memory dominates (Zep)
- **Procedural execution (DB-Bench):** raw long context wins — operation order determines
  correctness, so any restructuring hurts
- **Long-context QA with distractors (LongBench):** structured memory holds accuracy steady while
  raw long context collapses (42.6 → 19.0) as distractors accumulate
- **Knowledge updates:** graph-based methods handle revisions best; append-only stores return
  "stale facts, leading to hallucinations of the past"

Quoted conclusion: "No single memory architecture dominates all scenarios; instead, effectiveness
depends heavily on how well the memory structure aligns with the workload bottleneck."

Two secondary results with design weight: (1) retaining original conversational content matters
more than increasing abstraction or hierarchy — compression and aggressive summarization degrade
exact matching without compensatory gains; (2) highly structured systems incur
orders-of-magnitude higher index-construction and query cost without proportional accuracy gains.

## Why It Matters

The KB holds many individual memory-architecture patterns but had no systematic comparative
evidence across them (the 1.C gap). This finding supplies the missing decision rule: identify the
workload bottleneck first (distractor filtering? cross-session aggregation? update correctness?
order preservation?), then pick the structure that addresses it. It also independently corroborates
the verbatim-storage thesis (content fidelity beats abstraction) from a benchmark suite unrelated
to MemPalace, upgrading confidence in that pole of the design triangle.

## Why People Are Using It

Zhou et al., arXiv:2606.24775 (Tsinghua / SJTU database groups), submitted 2026-06-23. The
evaluation quantifies effects on representation quality, retrieval accuracy, update reliability,
and long-horizon performance; code published at OpenDataBox/MemoryData.

## Potential Improvements

- Map the engine's own workloads onto the bottleneck taxonomy (the KB is closest to the
  cross-session-aggregation + knowledge-update profile, which favors structured/temporal
  organization over append-only accumulation)
- Track follow-up work replicating the comparison as new systems ship

## Potential Failure Modes

- Benchmark workloads are conversational-agent-centric; coding-agent memory (repo state, plans,
  governance) may have bottlenecks the suite doesn't measure
- Per-system scores reflect implementations at one point in time; rankings will drift as systems
  iterate
- v1 preprint, not yet peer-reviewed
