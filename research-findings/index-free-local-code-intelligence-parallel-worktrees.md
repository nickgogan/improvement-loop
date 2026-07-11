---
name: "Index-Free, Local-Only, Rule-Based Code Intelligence Survives Parallel Worktrees"
summary: |-
  As we run more agents in parallel git worktrees, any code-intelligence tool that depends on a
  build index becomes a liability: each checkout needs either a shared cache (staleness, contention)
  or its own index copy (duplication, warm-up cost). ast-grep outline's design point — parse files
  on demand, no index, no cross-file resolution, declarative extraction rules — means "each worktree
  is just source text on disk," so N parallel agent worktrees cost nothing extra and can never serve
  stale structure. The trade: it deliberately gives up import resolution, call graphs, and type
  inference to keep speed and predictable failure modes.
implementation_notes: null
category: "Tool Integration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "ast-grep-outline-structural-summaries.md"
related_findings:
  - file: "worktree-isolation-for-parallel-agent-sessions.md"
    rel: "enables"
proposals: null
date_discovered: "2026-07-11"
last_updated: "2026-07-11"
---

## What It Is

A deliberate design position for agent-facing code tooling, articulated by the ast-grep project: parse source files on demand with declarative extraction rules (YAML pattern rules per language construct, e.g. `pattern: $VIS struct $NAME { $$$BODY }`), maintain no index, and perform no cross-file analysis — no "import resolution, follow references, construct call graphs, infer receiver types." The project positions this on an explicit spectrum: grep (fast, local, textual) → ast-grep outline (fast, local, structure-aware) → AST indexing (fast-ish, global, approximate semantics) → LSP (slow, global, accurate semantics).

## Why It Matters

The worktree-parallelism argument is the sharp edge: "agents often work in multiple git worktree checkouts at once." Index-based tools force a choice between a shared cache (which goes stale the moment one worktree diverges, and contends under concurrent writes) and per-worktree index duplication (disk, memory, and warm-up cost multiplied by N agents). Index-free tooling sidesteps both — "each worktree is just source text on disk, so parallel agent worktrees do not create parallel copies of the same codebase index." A second benefit is predictable failure: when an outline misses syntax, the gap is a missing extractor rule (fixable, enumerable), not an opaque heuristic or a stale cache. As worktree-parallel agent fleets become the norm, index-freedom becomes a tool-selection criterion, not an implementation detail.

## Why People Are Using It

Stated design rationale of the ast-grep project (Tier-2 community tool, benchmarks author-measured); the constraint set was chosen specifically because the primary consumer is parallel coding agents rather than a single human IDE session.

## Potential Alternatives

- LSP servers per worktree (accurate semantics; heavy, one server per checkout, slow startup).
- Shared code-intelligence indexes (Sourcegraph-style; global and powerful, but stale against uncommitted worktree state).
- ctags per worktree (cheap index; still a generated artifact that drifts from disk).

## Potential Improvements

- Custom extraction rules (planned upstream) let projects extend coverage without waiting for built-in language support.
- Hybrid strategies: index-free for structure and navigation, escalate to LSP only for the rare query needing type resolution.

## Potential Failure Modes

- The local-only constraint is a real capability ceiling: questions requiring reference-following or call graphs need a different tool — misapplying outline there produces confidently incomplete answers.
- Re-parsing on every invocation trades CPU for freshness; on very hot loops over huge trees the absent cache is paid for repeatedly.
