---
name: GSD Queryable Codebase Intelligence Store
summary: Persistent .planning/intel/ store with structured JSON for files, exports, symbols, patterns, and dependencies — queryable via CLI with incremental updates.
implementation_notes: null
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- General / Cross-System
adopted_in: []
sources:
- gsd-v1340-v1342-changelog.md
related_findings:
- file: gsd-global-learnings-store-cross-session-persistence.md
  rel: same-problem
- file: first-principles-context-management-taxonomy.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
pipeline_status: synthesized
consumed_by:
- designing-agent-tools.md
---

## What It Is

A persistent codebase intelligence store located in `.planning/intel/` that maintains structured JSON files covering files, exports, symbols, patterns, and dependencies. Agents query the store via `gsd-tools intel` subcommands rather than rescanning the codebase each session. A dedicated `gsd-intel-updater` agent performs incremental updates so the store stays current without full rescans. The feature is opt-in — projects without an intel store are unaffected.

## Why It Matters

Codebase understanding is one of the most expensive operations in agentic coding — agents spend significant tokens scanning, parsing, and building mental models of code structure every session. A pre-built, queryable intelligence layer converts this repeated O(n) cost into an O(1) lookup. The structured JSON format (not freeform markdown) enables precise queries rather than fuzzy search.

## Why People Are Using It

As codebases grow, the cost of codebase re-discovery per session becomes a bottleneck for both token budgets and session latency. The incremental update model means the intel store stays fresh without the cost of full rescans. The opt-in design respects project diversity — small projects that don't need it aren't burdened by it.

## Potential Improvements

The intel store could integrate with version control hooks to trigger incremental updates on commit, keeping the store current without explicit agent invocation. Schema versioning for the JSON files would prevent stale-format issues across tool upgrades. A staleness indicator per entry would let querying agents gauge confidence in the returned data.

## Potential Failure Modes

Stale intel is worse than no intel — an agent trusting outdated symbol maps or dependency graphs will generate incorrect code with high confidence. If the incremental updater misses changes (e.g., bulk refactors, branch switches), the store silently drifts from reality. The structured JSON format also creates a maintenance surface — schema changes in the codebase (new export patterns, new frameworks) require corresponding updates to the intel schema.
