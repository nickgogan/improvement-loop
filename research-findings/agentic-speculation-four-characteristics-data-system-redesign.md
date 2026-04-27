---
name: "Agentic Speculation — Four Characteristics That Redesign Data Systems"
summary: "UC Berkeley position paper (Parameswaran group + Stoica + Zaharia + Gonzalez + Cheung + Crooks) argues LLM-agent workloads are characterized by 'agentic speculation' — high-throughput exploration and solution formulation — and that four properties demand rethinking of data systems: scale (volume dwarfs traditional workloads), heterogeneity (queries cross modalities/schemas/systems), redundancy (repeated near-duplicate exploration), and steerability (queries redirect mid-flight). Proposes new research directions across query interfaces, query processing, and agentic memory stores."
implementation_notes: "Not immediately actionable (vision paper, no benchmarks) but a useful lens for MetaSystem: any data-retrieval surface an agent talks to will exhibit these four properties. Particularly relevant: redundancy — agent exploration paths overlap, so caching or dedup at the retrieval layer may pay off more than in human-query workloads. Also relevant: the 'agentic memory stores' research direction aligns with active work on Memongo and the broader Context Engineering dimension (Sub-dim 1.A/1.B)."
category: "Context Engineering"
evidence_strength: "Weak (theoretical)"
adoption_status: "Not Yet Started"
priority: "P3"
applicability:
  - "General"
adopted_in: []
sources:
  - "arxiv-2509-00997-agent-first-data-systems.md"
related_findings:
  - file: data-agent-benchmark-dab-cross-dbms-pipeline-eval.md
    rel: same-problem
  - file: mongodb-single-store-polymorphic-evidence-memory.md
    rel: same-problem
  - file: rank-fusion-hybrid-retrieval-mongodb-atlas.md
    rel: same-problem
  - file: programmatic-tool-calling-code-orchestrated-tool-use.md
    rel: same-problem
  - file: production-memory-architecture-spectrum.md
    rel: same-problem
  - file: six-layer-agent-infrastructure-stack.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-27"
pipeline_status: raw
consumed_by: []
---

## What It Is

A position paper from UC Berkeley (Shu Liu, Soujanya Ponnapalli, Shreya Shankar, Aditya G. Parameswaran, plus Ion Stoica, Matei Zaharia, Joseph E. Gonzalez, Alvin Cheung, Natacha Crooks, and others) arguing that LLM-agent workloads — which the authors call **agentic speculation** — will dominate future data systems and that current systems must adapt.

Four characteristics of agentic speculation:

| Characteristic | Definition |
|----------------|------------|
| **Scale** | Volume of exploratory queries per task far exceeds traditional workloads. |
| **Heterogeneity** | Queries cross modalities, schemas, and data systems. |
| **Redundancy** | Exploration paths repeat or near-duplicate within and across tasks. |
| **Steerability** | Queries can be redirected mid-flight based on intermediate findings. |

Proposed research directions:
- New query interfaces adapted to agent-first usage.
- New query processing techniques that exploit redundancy and steerability.
- New agentic memory stores.

No benchmarks. Vision paper.

## Why It Matters

The paper frames a set of workload characteristics that agent engineers already sense intuitively but few have named precisely. Two are particularly load-bearing for any practitioner building retrieval or memory surfaces:

- **Redundancy**: agent exploration produces overlapping queries across and within tasks. Traditional caching was designed for human query patterns (rare exact hits); agentic workloads may make aggressive cache/dedup economical.
- **Steerability**: queries are not submitted and forgotten — the agent can redirect based on what intermediate results say. This invites interactive query APIs (streaming, partial results, cancellation) more than batch APIs.

The four-characteristic framing is useful as a design lens: when you're sketching a new data-facing agent surface, check each of the four — does my interface handle the scale? the heterogeneity? am I exploiting redundancy? am I supporting steerability?

## Why People Are Using It

UC Berkeley position paper, v2 December 2025. Academic work at this stage — no production adoption evidence. Co-author group (Stoica, Zaharia, Gonzalez) has a strong track record of academic frameworks making their way into production systems (Spark, Ray, etc.), so the paper's framing may well propagate into future systems work.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Treat agent queries as normal DB queries | Ignore the workload shift; use existing query engines | For low-volume agent workloads where the four characteristics don't yet dominate |
| Dedicated vector-DB-only stack | Treat agent data access as pure similarity search | When the agent's interaction with structured data is minimal |

## Potential Improvements

- Empirical validation — the paper's characteristics are argued from first principles; benchmarks that measure real agent workloads against traditional workloads would quantify the claim.
- Connection to specific query engines — the paper is abstract about which engines should adopt which techniques. A follow-up paper mapping the four characteristics onto Snowflake / BigQuery / Spark / Postgres concrete roadmaps would make it actionable.

## Potential Failure Modes

- **Vision paper trap**: the framing is adopted rhetorically but systems don't actually redesign. The four characteristics become buzzwords rather than design constraints.
- **Redundancy assumption fragility**: if agent training shifts toward less-exploratory solution styles, the redundancy axis weakens.
- **Over-specialization**: data systems redesigned for agent workloads may regress on human-query performance, creating forced-choice architectures.
