---
title: "Librarian Reference Layer"
type: "index"
target_system:
  - "improvement-loop"
created: "2026-04-21"
updated: "2026-04-22"
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
| [Agentic Systems](agentic-systems.md) | — | A topology of multiple agents + shared state. Single-agent-is-default is the load-bearing invariant; multi-agent fits four legitimate domains (research / debugging / synthesis / monitoring). |
| [Context Rot](context-rot.md) | — | Gradual, silent degradation of an agent's attention over a session — attention-budget depletion compounded by noise accumulation. The working-tier failure mode. |
| [Harness](harness.md) | — | The runtime + tooling surface an agent operates inside — CLI/IDE/API harness distinct from the agent's own prompt. |
| [MCP](mcp.md) | — | Harness-level protocol for exposing external resources to agents over a uniform `execute(name, input) → string` interface. Baseline-infrastructure posture per G5 §Step 7 (ecosystem figures cited from source; not restated here). Single referent — boundary with A2A, tool-loading discipline, and permissions all live in composition table. |
| [Memory](memory.md) | working / episodic / semantic / global-learnings | Deliberate read/write policy system by which an agent retains information across time. Four tiers of one architecture; global-learnings is a widely cited practitioner surface. |
| [Prompt](prompt.md) | — | An authored instruction a model executes. Audit behavior is an *extension over `/prompt-evaluator`* — adds only what the 4-discipline rubric cannot reach. |
| [Prompt Caching](prompt-caching.md) | — | Harness-level stable-prefix cache. Cache hits cost ~10× less than standard tokens; any character change invalidates the block. |
| [Second Brain](second-brain.md) | Human / AI / Hybrid | A personal or shared knowledge store. Three variants carry genuinely distinct referents. |
| [Skill](skill.md) | — | A procedural packaging of a bounded operation (canonical shape: `SKILL.md`). Safety-critical skills fire G9.I6 unconditionally. |

### Operations (verb-keyed)

| Operation | Summary |
|---|---|
| [Audit](audit.md) | Evaluate a consumer-submitted artifact (agent.md, prompt, SKILL.md, etc.) against Contract-derived criteria from relevant guides. |
| [Coverage](coverage.md) | Answer meta-queries about the KB itself — what it holds, how much, which typed-pairs exist. Reads indices / manifests / frontmatter, not bodies. |
| [Decide](decide.md) | Produce a tradeoff comparison between options. Reads Key Concepts + proactively surfaces `contradicts`-typed pairs for design debates. |
| [Design](design.md) | Produce step-by-step guidance for building an artifact or architecture the consumer hasn't built yet. Composes Procedure / Step subsections + Templates + Examples. |
| [Diagnose](diagnose.md) | Map consumer-reported symptoms to likely causes with recovery pointers. Composes Pitfalls + Recovery subsections; optional Key Concepts for mechanism depth. |
| [Explain](explain.md) | Short mechanism + evidence response to "why" / "how does X work" queries. Reads Key Concepts; escalates to Tier 2 findings on ask. |
| [Fetch](fetch.md) | Return a named artifact (template, rule, scaffold, or catalog). Anchor-lifts the source subsection; does not synthesize. |
| [Plan](plan.md) | Phase-ordered roadmap across the lifecycle axis (specify → build → verify → secure → operate). Names substrate + handoff gates per phase; hands off to `design` for within-phase depth and `audit` for phase verification. |
| [What's New](whats-new.md) | Date-filtered listing of substrate that crossed a consumer-supplied `since` date. Reads `created` / `updated` frontmatter. |

## Next entries (planned, not yet authored)

Authoring backlog from the session-49 use-case registry is **closed** as of session 54 — all P1–P4 concept and operation files are authored. Further entries will be added on demand when new consumer queries or use cases arrive that the current reference layer does not cover; prioritization then follows the registry-update process in `project-management/design-notes/2026-04-21-librarian-use-case-registry.md`.

Iterative depth is expected on some files (notably `agent.md` variant stubs — see use-case registry §Variant-authoring hotspots). Per Nick's session-49 guidance, variant stubs distinguish referents; deeper per-variant composition iterates per query rather than pre-covering hypothetical variants.

## Contracts on entries here

Composition pointers must resolve to actual guide sections, findings, or watched-library paths; broken pointers are a write-time rejection per the acceptance-rubric follow-up (substrate audit §"What Option α' implies for existing work"). Entries are **pointer-only** — if a concept or operation needs more than pointers (e.g., materialized criteria), it's a view artifact and doesn't belong here.

## Cross-references

- Substrate audit: `project-management/design-notes/2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md`
- Contract-section spot check: `project-management/design-notes/2026-04-21-contract-section-spotcheck-agent-audit.md`
- Guide routing table (primary substrate Tier 1): `operations/references/guide-routing-table.md`
- Librarian agent definition: `agents/librarian/agent.md`
- Governing DDs: DD-78 (ContractSpec), DD-82 (IL 4-agent architecture)
