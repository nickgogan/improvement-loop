---
operation: whats-new
type: operation
target_system:
  - "improvement-loop"
created: "2026-04-22"
updated: "2026-04-22"
author: "claude"
stage: "draft"
tags:
  - "librarian-operation"
  - "whats-new"
  - "currency"
  - "date-filtered"
aliases:
  - "Whats new"
  - "Recent"
  - "Latest"
  - "Since date"
---

# What's New

## Short definition

**What's-new** returns substrate material added or updated since a consumer-supplied date. Input is a scope (concept, variant, dimension, or `*` meta) plus a `since` date (absolute or natural-language resolvable). Output is a date-ordered listing of findings, sources, guides, and patterns that crossed the date threshold, attributed by substrate kind.

Per Nick's session-49 gate on the use-case registry: `whats-new` is **consumer-parameterized by date**, not system-timestamped by a staleness ledger. This removes the dependency on the lifecycle-spec Phase-1 DDs (still deferred). The consumer supplies the date; the Librarian filters by `created` / `updated` frontmatter fields.

## Default composition rule

`whats-new` composes three inputs:

1. **Concept file** for the noun (or `*` for meta-scoped queries) — narrows substrate to the concept's composition-table tier targets.
2. **Date threshold** — the consumer-supplied `since` value. If the consumer says "since last week," the Librarian resolves to an absolute date and confirms ("interpreted as 2026-04-15 and later").
3. **Frontmatter filter** — findings and sources have `created` dates; guides have `updated` dates. The filter is `>= threshold`.

No cross-guide stitching. No rubric build. `whats-new` is a listing operation — the work is in the filter + date resolution + attribution.

### Composition details

**(a) Date resolution.** Natural-language dates ("last week," "in the past month," "since the last session") resolve to absolute dates first. State the resolution explicitly so the consumer can correct.

**(b) Tier discipline.** For Tier 1 (guides), `updated` is the filter field; a guide updated after the threshold surfaces with a note on what changed (if a changelog or a recent SL entry documents the change, cite it). For Tier 2 (findings, patterns, sources), `created` is the filter field; newly added findings surface with their `Key insight` line for scanning.

**(c) Scope narrowing by noun.** A concept-scoped query (UC-7.1 "what's current on memory architectures?") filters substrate to the concept's composition-table tier targets. A `*` meta query (UC-7.3) filters across all substrate but partitions the output by dimension or concept so the listing is navigable.

**(d) No inferred "freshness" claims.** The Librarian does not assert that unchanged material is *current* or *stale* — that's a staleness-ledger question (deferred). What's-new only reports what crossed the date threshold.

## Procedure

Four phases.

### Phase 0 — Parse the query

Parse verb + noun(s) + date. Verb: `whats-new` or a synonym ("what's new," "recent," "latest," "since"). Noun identifies the concept scope or `*` meta scope. Date is the `since` value.

**If no date is supplied, ask.** Per read-contract §8.3: "whats-new becomes consumer-parameterized rather than system-timestamped" — the Librarian does not pick a default window silently. "Since last week" or "since 2026-04-01" — the consumer supplies scope.

If the scope is ambiguous (meta query with no dimension named), ask for one dimension or offer a top-level cross-dimension listing.

### Phase 1 — Load composition and resolve date

Read the concept file (or skip for `*` meta queries — route to the dimension registry / `_index.md` files instead). Resolve the natural-language date to an absolute date and confirm inline.

For concept queries, identify the composition-table rows that map substrate to filter: guides for Tier 1, findings / patterns for Tier 2. Tier 3 is not in scope for `whats-new` — watched-library registry deltas are handled by `/watch-upstream`, not by the Librarian.

### Phase 2 — Filter substrate

Walk the substrate files in the concept's scope. For each file:

1. Read frontmatter (`created`, `updated`).
2. Compare against threshold. Include if `>= threshold` for the relevant field.
3. Read one line of the body for attribution (for findings: `Key insight:`; for guides: latest changelog entry or SL-referenced section; for sources: title + priority).

### Phase 3 — Assemble date-ordered listing

Sort by date descending. Partition by substrate kind (guides / findings / patterns / sources) or by dimension (for meta queries). For each entry, emit: date, substrate kind, path, and the one-line attribution.

### Phase 4 — Gap + next-step pass

- If nothing crossed the threshold, state it: "No substrate crossed the 2026-04-15 threshold in the `<concept>` scope. Closest-adjacent activity: <X>."
- Offer next steps only when the listing suggests one: "finding A extends finding B — you might want to re-audit your <artifact> against A's invariants."

## Consumer input handling

Expected input: concept / dimension / variant scope + `since` date. If date is omitted, ask. If scope is omitted for a meta query, ask for a dimension or offer a top-level cross-dimension listing.

| Query shape | How to read |
|---|---|
| Concept-scoped (UC-7.1 "what's current on agent memory architectures?") | `memory.md` → G7 Tier 1 + memory-cluster Tier 2; `since` filter |
| Variant-scoped (UC-7.2 "what's new on hybrid second-brain patterns this quarter?") | `second-brain.md` variant C → Agentic Systems cluster findings; `since` filter |
| Cross-dimension (UC-7.3 "what did the KB add about agents over the last N sessions?") | `*` meta + dimension registry; partition by dimension; `since` filter |

## Output shape

```
## What's New — <concept scope> since <resolved date>

**Interpreted as:** (verb: whats-new, scope: <concept / variant / dimension / meta>, since: <absolute date>)
**Filter field:** <created for Tier 2; updated for Tier 1>
**Matches:** <N total>

### Updates

| Date | Kind | Path | One-line attribution |
|---|---|---|---|
| 2026-04-21 | Finding | `research-findings/<slug>.md` | Key insight: … |
| 2026-04-20 | Guide update | `extracts/guides/<guide>.md` | Changelog: … |
| … |

### Nothing found (if applicable)

<State the empty result + closest-adjacent activity.>

### Next-step suggestion (optional)

<One line: "finding A extends B — consider re-auditing" etc.>
```

## Governance and boundaries

- What's-new is **read-only on substrate**. The Librarian does not promote findings, mark guides stale, or update frontmatter timestamps.
- What's-new does not invent a default date window. Consumer supplies `since`; Librarian asks if omitted.
- What's-new does not conflate "added" with "load-bearing." A new finding may or may not be consequential; the Librarian lists; the consumer judges.
- What's-new reads Tier 1 and Tier 2. Tier 3 (watched-library deltas) is out of scope — that's `/watch-upstream`.
- Per Nick's session-49 gate: no inferred staleness — "freshness" is a staleness-ledger concern (deferred Phase-1 lifecycle DDs). Until that lands, what's-new only reports dates.

## Cross-references

- Read-contract (Step 1 verb extraction, §8.3 input handling for whats-new): `project-management/design-notes/2026-04-21-librarian-read-contract.md`.
- Related operations: `coverage.md` (this directory) — coverage lists what exists; whats-new lists what crossed a date threshold.
- Related concepts: all concept files — whats-new can scope to any concept.
- Relevant workflow: `/watch-upstream` handles Tier 3 watched-library deltas; `whats-new` does not overlap.
- Use-case registry (UC-7.1–7.3): `project-management/design-notes/2026-04-21-librarian-use-case-registry.md`.
- Governing DDs: DD-82 (IL 4-agent architecture), DD-90 (telemetry — `whats-new` answers may reference SL-entry dates but does not itself emit telemetry).
