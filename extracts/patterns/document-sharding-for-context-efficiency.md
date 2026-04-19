---
title: "Document Sharding for Context Efficiency"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "document-sharding-for-context-efficiency"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Large documentation artifacts exist that exceed the context needs of individual agent tasks. A sharding taxonomy (what categories of content to split by) has been defined before splitting begins."
  invariants: "Every shard is self-contained enough to be useful without loading sibling shards. The union of all shards covers the full content of the source document — no information is lost. Shard-to-source traceability is maintained."
  governance: "Nick owns the sharding taxonomy and decides which documents to shard. Agents may propose shard splits but must not auto-shard without approval. Shard refresh after source changes requires a human gate."
  recovery: "If a shard is found to be incomplete or stale relative to its source, flag it as stale and reload the full source document until the shard is regenerated. If cross-shard dependencies are discovered at runtime, escalate to the human operator to merge or restructure shards."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Document Sharding for Context Efficiency

**Source:** [[document-sharding-for-context-efficiency]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Large documentation artifacts (PRDs, architecture specs, governance documents) are loaded in full when an agent only needs a fraction of their content. This wastes context window tokens, degrades model attention on the actual task, and creates a ceiling on the number of documents an agent can consult in a single session.

## Forces

- **Completeness vs. economy.** Loading the full document guarantees nothing is missed, but most of the content is irrelevant to any single task.
- **Coherence vs. granularity.** Splitting too aggressively produces shards that lack the context to be understood in isolation. Splitting too conservatively preserves the original problem.
- **Freshness vs. stability.** Source documents evolve. Shards derived from them can drift out of sync, creating a maintenance burden that scales with shard count.
- **Discoverability vs. proliferation.** More files means more things to find. Without clear naming and indexing, shards become harder to locate than the monolith they replaced.

## Solution

Break large documentation artifacts into focused, role-aligned shard files. Each shard covers one coherent topic (e.g., coding standards, tech stack, source tree structure, individual epics/stories). Agents load only the shards relevant to their current task.

**Key mechanics:**

1. **Define a sharding taxonomy** before splitting. Categories should align with agent roles or task types, not arbitrary document sections.
2. **Each shard must be self-contained.** Include enough context (a brief header, scope statement) that the shard is usable without its siblings.
3. **Maintain a shard manifest** that maps shards back to their source document and records the source version at time of sharding.
4. **Re-shard on source change.** When the source document is updated, regenerate affected shards. The manifest enables targeted refresh rather than full re-generation.
5. **Validate cross-shard coverage.** Periodically verify that the union of shards still covers the full source content — no gaps, no orphaned information.

The BMad Method's `/shard` command automates steps 1-3 for PRDs and architecture docs, claiming 90% token savings versus full-document loading.

## Consequences

**Positive:**
- Dramatic reduction in wasted context tokens (reported 90% savings in BMad Method).
- Improved model attention — less irrelevant content competing for the model's focus.
- Enables loading from more sources in a single session by reducing per-source cost.
- Aligns naturally with role-based agent architectures where each agent has a specific concern.

**Negative:**
- Over-sharding creates file proliferation and discoverability problems.
- Cross-shard dependencies can be missed when loading individual shards — information that spans two shards may be invisible to an agent loading only one.
- Shard drift introduces a maintenance burden: source updates require shard regeneration.
- The sharding taxonomy itself is a design decision that can be wrong — bad categories produce shards that don't match actual task boundaries.

## Known Uses

- **BMad Method v6** (43.7K GitHub stars): `/shard` command auto-splits PRDs and architecture docs into coding-standards.md, tech-stack.md, source-tree.md, and individual story files.
- **MetaSystem fractal pattern (DD-52):** Produces focused, role-specific files by design — a structural form of document sharding applied at the system level rather than the document level.

## Contract

### Preconditions

- Large documentation artifacts exist that exceed the context needs of individual agent tasks.
- A sharding taxonomy (what categories of content to split by) has been defined before splitting begins.
- The target directory structure for shards has been established.

### Invariants

- Every shard is self-contained enough to be useful without loading sibling shards.
- The union of all shards covers the full content of the source document — no information is lost.
- Shard-to-source traceability is maintained via a manifest or naming convention.

### Governance

- Nick owns the sharding taxonomy and decides which documents to shard.
- Agents may propose shard splits but must not auto-shard without approval (human gate).
- Shard refresh after source document changes requires review before deployment.

### Recovery

- If a shard is found to be incomplete or stale relative to its source, flag it as stale and reload the full source document until the shard is regenerated.
- If cross-shard dependencies are discovered at runtime (agent needs information spanning multiple shards), escalate to the human operator to merge or restructure the affected shards.
- If the sharding taxonomy proves misaligned with actual task boundaries, re-evaluate the taxonomy before re-sharding — do not patch individual shards.
