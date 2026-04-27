---
name: "Typed-Relationship Memory Graph (updates/extends/derives)"
summary: "Three named edge types capture how memories evolve over time: `updates` (new fact supersedes old, old is retained with `isLatest: false`), `extends` (adds context to an existing fact), `derives` (system inferred a new memory from patterns across several). Typed evolution graph, not untyped similarity edges — gives a concrete API shape for 'update without losing history' and for making inferred knowledge auditable."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: null
applicability:
  - "General"
  - "S3 (Claude Code Build)"
adopted_in: []
sources: []
related_findings:
  - file: triple-storage-memory-architecture.md
    rel: same-problem
  - file: mongodb-single-store-polymorphic-evidence-memory.md
    rel: same-problem
  - file: verbatim-storage-thesis-for-memory.md
    rel: same-problem
  - file: agentic-search-memory-retrieval-architecture.md
    rel: extended-by
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-27"
pipeline_status: raw
consumed_by: []
---

## What It Is

Three relationship types on a memory graph, each carrying distinct semantics:

- **Updates** — state mutation. Memory v2 *updates* Memory v1 when a fact changes (e.g., "User prefers React" → "User prefers React with TypeScript"). The old memory is not deleted; it's kept with `isLatest: false`. Queries can request the latest version only (default), the full version chain, or a specific version.
- **Extends** — context enrichment. Memory B *extends* Memory A when it adds detail about the same subject without changing the original claim ("User prefers TypeScript" → "User completed advanced TypeScript course"). The extension is cumulative; both memories remain true and retrievable.
- **Derives** — cross-memory inference. Memory D is *derived* from Memories A, B, C when the system identifies a pattern across them (A: "reads ML papers daily" + B: "asks about neural networks" + C: "works on AI projects" → derived: "is an ML engineer/researcher"). Derived memories are auditable — the provenance edges point back to the source memories.

The three types are not ad-hoc tags; they are first-class relationship categories with specific query and retrieval behavior. Contrasts with untyped similarity edges (Pinecone, Weaviate) and with `contradicts` / `related_findings` patterns that mix semantics.

## Why It Matters

Any system that tracks user state or domain facts over time faces the "how do I update without losing history?" problem. Three concrete options: (a) overwrite (loses provenance), (b) append (grows unboundedly with no notion of which is current), (c) typed versioning (solves both).

For MetaSystem directly:

- **Household OS user-state tracking** — preferences, schedules, relationships evolve. Each of the three relationship types maps to a real scenario: moving apartments (updates), adding a new pet to "has pets" (extends), inferring "is parenting teens" from scattered evidence (derives).
- **IL `pipeline_status` transitions** — our current model is a flat enum (raw → classified → synthesized → extracted). `updates` is implicit; we lose the intermediate states. A typed-relationship model would record *why* a finding was reclassified.
- **Librarian-grade auditability** — when an agent presents a "derived" claim, the provenance edges expose which memories supported the inference. Relevant for future governance.

Positions alongside but distinct from:
- [[mongodb-single-store-polymorphic-evidence-memory]] — about storage substrate, not relationship semantics.
- [[triple-storage-memory-architecture]] — about data-substrate split (vector + graph + SQL), not typed evolution.
- [[verbatim-storage-thesis-for-memory]] — refuses the extraction that this pattern presupposes.

## Why People Are Using It

Observed in [Supermemory](https://github.com/supermemoryai/supermemory) latest — see [[supermemory-analysis]] for structural details. The three types are declared in `skills/supermemory/references/architecture.md` §"Indexing" and the `isLatest` flag is documented under "Memory Versioning." The graph is built at write time; `client.add()` triggers extraction + relationship inference; retrievals can follow relationships for "expanded" results (§Retrieval Mechanism). Supermemory uses this model to deliver their "user profiles that evolve" value prop and their `memory-graph-playground` app visualizes the graph as a first-class UI surface.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Untyped similarity edges | Edges carry only a similarity score; no semantic type | When all relationships are equivalent and retrieval is purely similarity-driven |
| Overwrite on update | Replace old memory with new; no history | When storage cost dominates and provenance is not needed |
| Append-only versioning | Keep every version with a timestamp; no typed relationships | When evolution is strictly linear and "extend" / "derive" aren't meaningful |
| Taxonomy-based tags | Tag each memory with its source/type; filter at query time | When the relationship set is open-ended and hard to pre-name |

## Potential Improvements

- **Confidence on derived edges.** Derivations are inferred; exposing a confidence score on the derive edge makes downstream consumers able to filter low-confidence inferences.
- **Explicit `contradicts` relationship** for cases where two memories are both current and conflict, before resolution via `updates` happens.
- **Bulk-mutation semantics.** Current shape assumes one-at-a-time writes; batch updates to multiple related memories need a transactional shape.

## Potential Failure Modes

- **Derives-explosion.** A system that infers derived memories from every pattern quickly bloats the graph with weakly-supported inferences. Needs a confidence threshold or a human-gate for graduating inferred memories to retrievable status.
- **Stale `isLatest` flags** after partial failures. If an update write partially succeeds, two memories can both carry `isLatest: true`. Needs transactional guarantees at the storage layer.
- **Semantic drift in relationship types.** Without tight documentation, developers tag an `extends` as an `updates` (or vice versa) and retrieval behavior diverges from user expectation. The three types are not self-evident.
- **Pruning discipline.** Without a forgetting layer, the graph grows unboundedly as extensions and derivations accumulate. Supermemory pairs this with [[content-derived-temporal-expiration-contradiction-resolution]] as the pruning mechanism.
