---
operation: coverage
type: operation
target_system:
  - "improvement-loop"
created: "2026-04-22"
updated: "2026-04-22"
author: "claude"
stage: "draft"
tags:
  - "librarian-operation"
  - "coverage"
  - "meta"
  - "kb-query"
aliases:
  - "Coverage"
  - "What does the KB cover"
  - "Which guides discuss X"
  - "KB query"
---

# Coverage

## Short definition

**Coverage** answers meta-queries about the KB itself — "what does the KB cover on governance?"; "which guides discuss multi-agent orchestration?"; "are there any `contradicts` pairs in the memory findings?". Input is a scope (dimension, concept, or pattern class). Output is a coverage map — a listing of what the KB holds in that scope, attributed by substrate kind and cited by path.

Coverage is a *consumption* operation on the KB's own metadata — the `_index.md` files, the guide routing table, the research dimensions registry, the `related_findings` graph. Coverage does not read the substrate bodies; it reads the manifests, indices, and frontmatter that describe the substrate. Cost is low by design — coverage is a navigational primitive.

## Default composition rule

`coverage` composes three inputs (different from most operations — coverage reads *indices*, not guide bodies):

1. **Scope** — dimension, concept, or pattern class. Determines which index file(s) to read.
2. **Index substrate:**
   - For dimension scope: `operations/references/research-dimensions.md` + `guide-routing-table.md`.
   - For concept scope: concept file (for composition-table tier pointers) + `_index.md` files in `research-findings/`, `extracts/guides/`, etc.
   - For pattern-class scope: `related_findings` graph — findings with typed edges of the named kind.
3. **Optional filter** — by status (`pipeline_status`), priority (`priority`), or `related_findings` edge type.

No cross-guide stitching. No rubric build. Coverage is a listing + filtering operation over metadata.

### Composition details

**(a) Dimension scoping via research-dimensions registry.** The dimensions registry partitions the KB — any dimension-scoped query routes through it first. Cite the dimension definition in the coverage response so the consumer understands the scoping.

**(b) Concept scoping via concept composition table + frontmatter.** A concept-scoped query lists substrate named in the concept's composition table *plus* any substrate tagged with the concept's aliases / tags in frontmatter. This catches material not yet wired into the composition table.

**(c) Graph-class queries via `related_findings`.** UC-8.3 ("are there any `contradicts` pairs in the memory findings?") is a graph query. The Librarian walks findings in scope, filters by `related_findings` edge type, and surfaces the typed pairs. No body reads — only frontmatter and edge labels.

**(d) No coverage inference.** The Librarian does not assert "the KB has comprehensive coverage of X" or "this area is under-covered." Those are editorial claims that require Owner / Researcher judgment. Coverage lists; it does not grade.

## Procedure

Four phases.

### Phase 0 — Parse the query

Parse verb + scope + optional filter. Verb: `coverage` or a synonym ("what does the KB cover," "do we have anything on," "how many findings on," "which guides discuss"). Scope is the partition (dimension / concept / pattern class). Filter is optional (status, priority, edge type).

If the scope is omitted ("what does the KB cover?" with no noun), the response is a top-level listing of dimensions + counts — serviceable as a starting point. But ask for a narrower scope for a useful answer: "everything" is not a serviceable scope (per read-contract §8.4).

### Phase 1 — Load indices

For the named scope, read:

- **Dimension scope:** research-dimensions.md (definition), guide-routing-table.md (dimension → guide mapping), `research-findings/*.md` filtered by dimension (ripgrep frontmatter `category:`).
- **Concept scope:** concept file (composition table), `research-findings/*.md` / `extracts/guides/*.md` filtered by concept's aliases / tags (ripgrep frontmatter `tags:` or `aliases:`).
- **Pattern-class scope:** `research-findings/` files' frontmatter `related_findings` entries, filtered by edge type.

Do not read substrate bodies. If the consumer wants body-level detail after the coverage map, hand off to `fetch` or `explain`.

### Phase 2 — Filter and count

Apply any consumer-named filter (status, priority, edge type). Produce counts per substrate kind: guides, findings, patterns, sources, authorities, watched-libraries. Cite each file by path.

### Phase 3 — Assemble coverage map

Emit a scannable map: scope → partition → counts → file listing. Partition by substrate kind (guides first, then findings, then other). For graph queries, emit the typed pair list with slugs on both sides of the edge.

### Phase 4 — Gap + next-step pass

- If the scope yields zero matches, state it: "No substrate exists for `<scope>`. Closest-adjacent coverage: <X> (see `guide-routing-table.md`)."
- If substrate is sparse, state the count but don't editorialize. The consumer decides whether sparse = "under-covered" or "adequately-covered-for-its-use."
- Offer one next-step suggestion: "fetch a specific entry," "explain a specific finding," "design something using this material."

## Consumer input handling

Expected input: scope (dimension / concept / pattern class) + optional filter. If scope is missing, ask. If the scope is a concept not yet authored, fall back to dimension-level routing and flag the concept-file gap.

| Query shape | How to read |
|---|---|
| Dimension-scoped (UC-8.1 "what does the KB cover about governance?") | `research-dimensions.md` entry for Governance → `guide-routing-table.md` + findings with Governance dimension tag |
| Concept-scoped (UC-8.2 "which guides discuss multi-agent orchestration?") | `agentic-systems.md` composition table + G3 / G3b / G7 / G9 mapping + findings tagged multi-agent / orchestration |
| Graph-class (UC-8.3 "any `contradicts` pairs in the memory findings?") | `memory.md` composition table scope + walk findings' `related_findings` for `contradicts` edges |

## Output shape

```
## Coverage — <scope>

**Interpreted as:** (verb: coverage, scope: <dimension / concept / pattern-class>, filter: <if any>)

### Scope definition

<Short citation: "Governance dimension — research-dimensions.md#governance" or "memory concept — memory.md" etc.>

### Substrate in scope

| Kind | Count | Files |
|---|---|---|
| Guides | 2 | G9 `agent-governance-and-trust.md`, G7 §Part 1 |
| Findings | 17 | (listed below or by slug) |
| Patterns | 4 | … |
| Sources | 8 | … |

### Listing (or typed pairs for graph queries)

<File list or `contradicts` / `extends` / `same-problem` / `enables` typed pair listing for graph queries.>

### Gap or adjacency (if applicable)

<State zero / sparse results with closest-adjacent pointer.>

### Next-step suggestion

<Fetch specific entry; explain specific mechanism; etc.>
```

## Governance and boundaries

- Coverage is **read-only on substrate metadata**. The Librarian does not modify indices, rewrite frontmatter, or propose re-tagging.
- Coverage does not grade the KB. "Under-covered" / "over-covered" / "stale" are editorial calls outside Librarian scope.
- Coverage does not read substrate bodies — it reads manifests, indices, and frontmatter. For body content, hand off to `fetch` or `explain`.
- Coverage does not invent `related_findings` edges. If a graph query yields zero matches, state it; do not synthesize a pair from body content.

## Cross-references

- Read-contract (Step 1 verb extraction, §8.4 input handling for meta / coverage): `operations/references/librarian/read-contract.md`.
- Related operations: `whats-new.md` (date-filtered version of coverage), `fetch.md` (body-level follow-up to coverage), `explain.md` (mechanism follow-up).
- Related concepts: all concept files and `*` meta — coverage can scope to any.
- Key substrate: `operations/references/research-dimensions.md` (dimension partitions), `operations/references/guide-routing-table.md` (dimension → guide routing — note: currently outside `librarian/` subdirectory).
- Use-case registry (UC-8.1–8.3): `operations/references/librarian/use-case-registry.md`.
- Governing DDs: DD-82 (IL 4-agent architecture).
