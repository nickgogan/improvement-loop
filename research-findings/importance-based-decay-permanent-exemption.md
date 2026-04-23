---
name: "Importance-Based Memory Decay with Permanent Exemption"
summary: "Memongo decays memory relevance by importance score rather than wall-clock TTL, via `computeImportanceDecay()`. Memories flagged as permanent or ongoing are exempt from decay entirely. No time-based expiry: a low-importance memory may persist indefinitely if nothing contends with it, while a high-churn workload naturally crowds out low-signal content through retrieval competition rather than deletion."
implementation_notes: "Contrasts with TTL-based schemes (Redis-style expiry) and with strict decay-curve models. Easier to tune (one axis: importance threshold) but requires a working importance score that's stable across sessions. The permanent/ongoing tag is a first-class escape hatch — useful for identity facts and long-running project state that should never be subject to decay. Memongo improvement question: what produces the importance score, and how well does it correlate with downstream retrieval utility?"
category: "Memory Architecture"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "memongo-mongodb-native-agent-memory-github.md"
related_findings:
  - file: semantic-memory-decay-compaction.md
    rel: same-problem
  - file: memory-decay-compaction-convergence.md
    rel: same-problem
  - file: dreaming-memory-consolidation.md
    rel: same-problem
  - file: memory-field-immutability-via-merge-operations.md
    rel: same-problem
  - file: content-derived-temporal-expiration-contradiction-resolution.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: classified
consumed_by: []
---

## What It Is

A memory decay model where the relevance of a stored memory degrades as a function of an **importance score**, computed via `computeImportanceDecay()` in Memongo's implementation. Decay is **not** tied to wall-clock age. Two explicit exemption tags suppress decay entirely: `permanent` and `ongoing`.

Operationally:
- High-importance memories rank strongly regardless of age.
- Low-importance memories rank weakly regardless of age.
- Permanent/ongoing memories bypass the decay function and always retrieve at full weight.
- There is no TTL, no delete job, no age-threshold purge.

## Why It Matters

Time-based TTL treats all memories of a given age equivalently — useful for session caches, wrong for agent memory where some decade-old facts (user identity, core preferences) are load-bearing forever. Pure recency weighting has the opposite failure: important old memories get buried by trivial recent ones. Importance decay decouples relevance from age, and the permanent/ongoing exemption creates a first-class escape hatch for identity-level memory that must never be lost.

For an agent that persists across months or years of interactions, this model plausibly generalizes better than time-based expiry.

## Why People Are Using It

Observed in [Memongo](https://github.com/romiluz13/Memongo) as `computeImportanceDecay()` with permanent/ongoing exemption flags. Related work in cognitive architectures (ACT-R's activation-based decay, Soar's chunking) uses similar importance/utility signals; Memongo is one of a handful of production-oriented agent memory systems to surface this model at the API level.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| TTL / wall-clock expiry | Memories expire after N days regardless of content | Session caches, ephemeral context, regulatory retention caps |
| Pure recency weighting | Score = importance × e^(-age/tau) | When recency is a reliable relevance signal for the workload |
| Reinforcement decay | Decay unless reinforced by retrieval/access | When retrieval patterns correlate with long-term relevance |
| No decay | Keep everything at full weight forever | When storage is cheap and retrieval quality handles noise |

## Potential Improvements

- **Importance score provenance** — README doesn't detail how importance is computed. If it's fixed at write time, late-arriving context can't upgrade it; if it's recomputed, compute cost grows with corpus size.
- **Reinforcement signal** — combine importance decay with access-count reinforcement. Memongo tracks access via `AccessTracker`, so this is close at hand.
- **Importance recomputation job** — periodically rescore old memories against current agent goals. Importance is not a static property.
- **Per-user or per-project importance scales** — a fact about Project X may be 10/10 importance in Project X's agent context and 0/10 in another.

## Potential Failure Modes

- **Stale importance scores** — if importance is set at write time and never updated, early-session misjudgments become permanent weight.
- **Permanent-tag abuse** — users or agents mark too many memories permanent, effectively reverting to no-decay.
- **No hard TTL means unbounded storage growth** — cost and query performance degrade slowly without visible trigger.
- **Importance score gaming** — if an LLM computes importance, it may systematically over- or under-weight certain memory types.
- **Privacy retention** — no wall-clock deletion makes compliance (GDPR right-to-erasure, session-bound retention) harder to implement.
