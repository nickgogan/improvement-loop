---
name: Production Memory Architecture Spectrum
summary: Five distinct memory architectures observed across 7 repos, from no memory (context window only) to triple storage service (vector + graph + SQLite). Memory sophistication correlates with deployment
  persistence. Maps the full spectrum of production memory approaches.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- cross-repo-comparison.md
related_findings:
- file: four-tier-agent-memory-model-with-write-policy.md
  rel: same-problem
- file: four-layer-enterprise-memory-stack.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
## What It Is

Five distinct memory architectures observed across 7 analyzed repos, ordered by sophistication:

1. **No memory — context window only** (Superpowers) — all state lives in the current context window. When the session ends, everything is lost. Simplest possible approach.

2. **Flat file state — STATE.md** (GSD) — a single markdown file tracks project state across sessions. Human-readable, version-controllable, but no semantic search or structured queries.

3. **Cross-session learnings log — JSONL append-only** (gstack) — learnings appended to a JSONL file across sessions. Searchable by content, but no semantic retrieval. Grows without consolidation.

4. **Structured file memory with consolidation — Dreaming/PARA with scoring and decay** (OpenClaw, Paperclip) — memories organized in structured files (PARA method), with periodic consolidation ("dreaming") that scores memories for relevance and applies decay to outdated entries.

5. **Triple storage service — vector + graph + SQLite with scoped access** (mem0) — full memory service with semantic similarity search, relationship-aware graph queries, and metadata management. See [[triple-storage-memory-architecture]] for details.

Memory sophistication correlates with deployment persistence.

## Why It Matters

The spectrum maps the full range of production memory approaches observed in the wild. Existing KB findings cover enterprise memory tiers conceptually (four-layer stack, four-tier model with write policy); this finding grounds those concepts in 5 concrete implementations with real trade-offs.

The correlation with deployment persistence provides a selection heuristic: ephemeral agents don't need memory infrastructure, session-persistent agents need flat file state, and persistent agents need structured or service-based memory. Over-engineering memory for the deployment model wastes effort; under-engineering creates degraded experiences.

## Why People Are Using It

Comparative analysis across 7 repos — see [[cross-repo-comparison]] for full details.

Each repo's memory architecture matches its deployment model. Superpowers (a Cursor skill pack) has no persistence because Cursor sessions are ephemeral. GSD (a framework) uses flat file state because frameworks need to survive across sessions without infrastructure. mem0 (a memory service) implements triple storage because its entire purpose is memory infrastructure.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Pick one level from the spectrum | Commit to exactly one memory architecture | For most projects — choose the level matching deployment persistence |
| Hybrid approach | Different memory levels for different data types | When some data needs semantic search and other data needs simple persistence |
| External memory service | Outsource memory to a third-party service (e.g., mem0 as a service) | When building memory infrastructure is outside the project's scope |

## Potential Improvements

- Map MetaSystem's current memory approach to this spectrum (likely level 2 — flat file state via PROGRESS.md and CLAUDE.md)
- Evaluate whether MetaSystem would benefit from moving to level 3 (JSONL learnings) or level 4 (structured with consolidation)
- Create a decision matrix matching deployment model to recommended memory level

## Potential Failure Modes

- **Over-engineering**: Implementing level 5 memory for a level 2 deployment model wastes resources and adds operational burden
- **Under-engineering**: Using level 1 memory for a persistent agent creates inconsistent user experiences
- **Migration difficulty**: Moving up the spectrum requires restructuring how memories are stored, indexed, and retrieved
- **Consolidation complexity**: Levels 4 and 5 require periodic maintenance (dreaming, scoring, decay) that adds operational overhead
- **Spectrum as prescription**: The 5 levels are observed patterns, not a maturity model — level 5 is not inherently "better" than level 2
- **Storage cost**: Higher levels accumulate more persistent data with associated storage, indexing, and maintenance costs
