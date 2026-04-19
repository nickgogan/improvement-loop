---
name: Orchestration Correlates with Product Type
summary: Coordination mechanism correlates with product architecture across 7 repos. Frameworks use file-based coordination, products use API-based coordination, skill packs use context-window coordination.
  The mechanism is not a free architectural choice — it follows from the product's nature.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: Not Flagged
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- cross-repo-comparison.md
related_findings:
- file: production-memory-architecture-spectrum.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
## What It Is

Coordination mechanism correlates with product architecture across 7 analyzed repos:

1. **Frameworks** (GSD, BMAD) use **file-based coordination** — artifacts serve as handoff documents between agents. The file system is the coordination bus. Agent A writes a plan file; Agent B reads it to execute. No runtime infrastructure required.

2. **Products** (OpenClaw, Paperclip) use **API-based coordination** — database records, REST endpoints, and server-side state manage inter-agent communication. The coordination bus is the product's backend infrastructure.

3. **Skill packs** (Superpowers, gstack) use **context-window coordination** — the main agent holds all state in its context window. Sub-agents receive state via prompt injection and return results via tool output. No persistent coordination layer exists.

mem0 falls outside these categories as a library/service, using its own API as the coordination mechanism.

The coordination mechanism is not a free architectural choice — it follows from the product's nature.

## Why It Matters

This is practical guidance for system designers. The correlation reveals a constraint that's easy to violate: trying to use API-based coordination in a framework context adds unnecessary infrastructure (you need a server for something that could be a file). Trying to use file-based coordination in a product context sacrifices the durability and queryability that databases provide.

Choosing a coordination mechanism that matches the product type reduces accidental complexity. Choosing one that doesn't creates friction at every integration point.

## Why People Are Using It

Comparative analysis across 7 repos — see [[cross-repo-comparison]] for full details.

The correlation appears to be emergent rather than deliberate — none of the repos explicitly state "we chose file-based coordination because we're a framework." Instead, the natural constraints of each product type push toward the matching coordination mechanism. Frameworks don't have servers, so they coordinate via files. Products have servers, so they coordinate via APIs.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Hybrid coordination | File-based for planning, API-based for execution | When the product spans framework and deployed contexts |
| Message queue coordination | Async message passing between agents | For high-throughput multi-agent systems with decoupled agents |
| Shared memory coordination | Agents read/write a shared memory store (e.g., mem0) | When coordination requires semantic understanding of shared state |

## Potential Improvements

- Map MetaSystem's coordination needs to this framework — is MetaSystem a framework, a product, or a skill pack?
- Evaluate whether hybrid coordination (file-based for governance, context-window for session work) is appropriate for MetaSystem
- Track whether new repos confirm or break this correlation

## Potential Failure Modes

- **Mismatched coordination**: Choosing API-based coordination for a framework forces unnecessary infrastructure dependencies
- **Over-indexing on the pattern**: The correlation is observed across 7 repos — a small sample that may not generalize
- **Product type evolution**: A project that starts as a framework and evolves into a product may need to migrate its coordination mechanism
- **Coordination mechanism lock-in**: The choice is deeply embedded in architecture — switching coordination mechanisms is effectively a rewrite
- **Context-window limits**: Context-window coordination for skill packs breaks down as state grows beyond context capacity
