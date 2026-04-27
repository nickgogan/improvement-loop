---
name: "Surprisal Novelty as Memory Write Gate"
summary: "Memongo includes a `mongodb-novelty.ts` module that computes surprisal-based novelty for incoming memory candidates and uses that score to gate what enters long-term memory. A candidate that closely matches an existing memory is low-novelty and either merged or dropped; high-novelty candidates are written as new memories. This is an upstream write-time filter, complementary to downstream decay."
implementation_notes: "Surprisal is the information-theoretic complement to importance: importance asks 'does this matter?', surprisal asks 'is this new?'. A mature agent memory system needs both — high-importance-but-redundant signals should merge rather than duplicate, and high-novelty-but-low-importance signals shouldn't clutter the index. Memongo exposes surprisal as a named module, which suggests it's intended to be tunable. For Memongo improvement: pair novelty gating with explicit deduplication and contradiction detection; surprisal alone doesn't catch 'new phrasing of same fact' when the semantic embedding is coarse."
category: "Memory Architecture"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "memongo-mongodb-native-agent-memory-github.md"
related_findings:
  - file: structured-fact-extraction-from-conversations.md
    rel: extends
  - file: dreaming-memory-consolidation.md
    rel: same-problem
  - file: memory-field-immutability-via-merge-operations.md
    rel: same-problem
  - file: concept-graph-support-contradiction-detection.md
    rel: same-problem
  - file: content-derived-temporal-expiration-contradiction-resolution.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: synthesized
consumed_by:
  - "session-persistence-and-memory.md"
---

## What It Is

A write-path filter that evaluates each memory-write candidate against the existing corpus and computes a **surprisal** score — how unexpected the candidate is given what's already stored. Memongo implements this in `mongodb-novelty.ts`. Operationally:

- Candidate arrives at the ingestion pipeline.
- Novelty score is computed against the existing `chunks` collection (likely via embedding similarity + lexical overlap against the nearest neighbors).
- High-novelty: write as a new memory.
- Low-novelty: merge with the existing match, or drop entirely.

This runs in addition to Memongo's LLM-based enrichment (fact extraction, QA pair generation) and in parallel with the consolidation agent ("Dreamer").

## Why It Matters

Most memory systems treat every turn as writeable, relying on downstream retrieval to surface the relevant subset. That works until the corpus accumulates many near-duplicate entries ("User prefers JSON" written 40 times across sessions), at which point retrieval precision drops and decay can't help because none of the duplicates is old. A write-time novelty gate catches this before the corpus bloats.

Surprisal is also a principled signal: if a candidate memory would not update the agent's retrieval distribution, writing it is wasted work.

## Why People Are Using It

Observed in [Memongo](https://github.com/romiluz13/Memongo) as an explicit named module. The concept has older roots in active learning (expected information gain) and cognitive models of memory (novel → encoded, familiar → merged). Few production agent memory frameworks expose it as a first-class gating stage; Memongo's packaging of it is the distinguishing evidence.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Write-everything + downstream dedup | Save all candidates, run dedup jobs later | When write cost is negligible and dedup precision matters more than write-rate |
| Rule-based dedup (exact-match on key fields) | Drop candidates with identical keys | When entity schema is strict and exact-match works |
| No novelty filter | Every turn becomes a memory | For session-level memory with short retention |

## Potential Improvements

- **Pair novelty with contradiction detection** — surprisal catches redundant agreements, but "User says A" followed by "User says not-A" is a contradiction, not a novelty; needs explicit contradiction checking (already a known gap in the Memongo README).
- **Dynamic novelty threshold** — early in a session or corpus, threshold should be low (everything is novel); late, threshold should rise to avoid over-writing.
- **Explain novelty decisions in the Dream Diary** (if Memongo's Dreamer surfaces one) — humans should be able to audit why a candidate was accepted or rejected.
- **Per-evidence-type thresholds** — facts, QA pairs, and session evidence have different novelty baselines; a single threshold is a blunt instrument.

## Potential Failure Modes

- **Embedding-driven novelty misses fine-grained facts** — two memories may be embedding-nearby but semantically distinct (e.g., "deploys at 3pm Tuesday" vs. "deploys at 3am Tuesday").
- **Novelty cold start** — with an empty corpus, everything is novel; the gate provides no filtering early.
- **Threshold tuning is brittle** — too high filters signal, too low admits noise.
- **Merge instead of write can hide corrections** — if a corrected fact is merged into a stale fact rather than written, the correction is lost.
- **Compute cost at write time** — every ingestion pays a similarity-search cost against the full corpus.
