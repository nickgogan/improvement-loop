---
title: "Librarian Reference Layer"
type: "index"
target_system:
  - "improvement-loop"
created: "2026-04-21"
updated: "2026-04-21"
---

# Librarian Reference Layer

Pointer artifacts for the Librarian agent — small files that encode *how to decompose consumer queries into reads* against guides, patterns, findings, and watched-library repos. Not a knowledge base. A routing table.

## Purpose

Consumer queries arrive as **verb + noun(s)** — "audit my agent.md" is (audit, agent); "how does context rot manifest in multi-agent systems?" is (explain, context-rot × multi-agent). The Librarian's job is to read the relevant pointer files, compose their references, and execute targeted reads against substrate — not to aggregate the substrate at query time.

This directory holds two file types, distinguished by frontmatter `type:`:

| Type | Keyed by | Contains |
|---|---|---|
| `concept` | Noun (term) | Definition, disambiguation ("not to be confused with"), optional variants, composition pointers (aspect → where to look), Librarian read rule. |
| `operation` | Verb | Definition, default composition rule, procedure, consumer-input handling, output shape. |

Substrate audit (`2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md`) introduced this layer under Option α'. Contract-section spot check (`2026-04-21-contract-section-spotcheck-agent-audit.md`) validated that composition works and surfaced four procedural refinements now embedded in `audit.md`.

## Directory structure

Flat. Concept and operation files live side by side; `type:` distinguishes them. No sub-folders.

## Catalog

### Concepts (noun-keyed)

| Term | Variants | Summary |
|---|---|---|
| [Agent](agent.md) | prompt-based / harness-based / autonomous-vs-supervised | A model-plus-context assembly authored to perform a bounded class of tasks. Three variants distinguish whether the prompt, the harness, or the autonomy envelope is load-bearing. |
| [Harness](harness.md) | — | The runtime + tooling surface an agent operates inside — CLI/IDE/API harness distinct from the agent's own prompt. |
| [Prompt](prompt.md) | — | An authored instruction a model executes. Audit behavior is an *extension over `/prompt-evaluator`* — adds only what the 4-discipline rubric cannot reach. |
| [Second Brain](second-brain.md) | Human / AI / Hybrid | A personal or shared knowledge store. Three variants carry genuinely distinct referents. |
| [Skill](skill.md) | — | A procedural packaging of a bounded operation (canonical shape: `SKILL.md`). Safety-critical skills fire G9.I6 unconditionally. |

### Operations (verb-keyed)

| Operation | Summary |
|---|---|
| [Audit](audit.md) | Evaluate a consumer-submitted artifact (agent.md, prompt, SKILL.md, etc.) against Contract-derived criteria from relevant guides. |

## Next entries (planned, not yet authored)

Per use-case registry (`project-management/design-notes/2026-04-21-librarian-use-case-registry.md`) authoring backlog:

- **Concepts (P2):** `memory.md` (variants: working / episodic / semantic / global-learnings), `context-rot.md` (no variants).
- **Concepts (P3):** `agentic-systems.md` (no variants), `prompt-caching.md` (no variants), `mcp.md` (no variants).
- **Operations (P2):** `diagnose.md`, `design.md`.
- **Operations (P3):** `decide.md`, `fetch.md`, `explain.md`, `whats-new.md`, `coverage.md`.
- **Operations (P4):** `plan.md`.

## Contracts on entries here

Composition pointers must resolve to actual guide sections, findings, or watched-library paths; broken pointers are a write-time rejection per the acceptance-rubric follow-up (substrate audit §"What Option α' implies for existing work"). Entries are **pointer-only** — if a concept or operation needs more than pointers (e.g., materialized criteria), it's a view artifact and doesn't belong here.

## Cross-references

- Substrate audit: `project-management/design-notes/2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md`
- Contract-section spot check: `project-management/design-notes/2026-04-21-contract-section-spotcheck-agent-audit.md`
- Guide routing table (primary substrate Tier 1): `operations/references/guide-routing-table.md`
- Librarian agent definition: `agents/librarian/agent.md`
- Governing DDs: DD-78 (ContractSpec), DD-82 (IL 4-agent architecture)
