---
title: "Watched Libraries"
id: "watched-libraries-index"
type: "governance"
category: "governance"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-07"
updated: "2026-04-07"
author: "nick"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "catalog"
  - "upstream-tracking"
  - "moc"
aliases:
  - "Watched Libraries MOC"
  - "Upstream Registry"
---

# Watched Libraries

Registry of external agentic tooling packages that MetaSystem monitors for relevant changes. Each entry tracks what we use, where it sits on the [[upstream-dependency-spectrum]], and what changed since we last looked.

No repo clones — only metadata, snapshots, and change summaries. See the upstream-dependency-spectrum pattern for why.

Structural analyses live in [[watched-library-analyses-index|analysis/]] — produced by `/repo-analyzer`.

## How This Gets Updated

1. **Manual** — Nick or JR adds a new library to watch
2. **`/watch-upstream` skill** (planned) — periodically fetches changelogs/READMEs and produces triage reports
3. **research-loop** — may flag new external projects worth tracking

## Catalog

| Library | Spectrum Position | Last Evaluated | What We Use |
|---------|-------------------|----------------|-------------|
| [[bmad-method\|BMAD Method]] | cherry-pick | v6.10.0 (2026-07-13) | Agent team patterns, docs-as-code, context sharding |
| [[gsd\|GSD]] | wholesale | v1.34.2 (2026-04-07) | Primary build orchestration — spec-driven phases, context management |
| [[superpowers\|Superpowers]] | thin-wrapper | v6.1.1 (2026-07-13) | TDD enforcement, skill auto-activation, subagent orchestration |
| [[openclaw\|OpenClaw]] | cherry-pick | v2026.4.5 (2026-04-07) | SOUL.md constitution pattern, memory file taxonomy |
| [[paperclip\|Paperclip]] | cherry-pick | v2026.403.0 (2026-04-07) | Multi-agent governance — goal ancestry, approval gates, budget tracking |
| [[gstack\|gstack]] | cherry-pick | v0.15.16.0 (2026-04-07) | Role-based specialist tools, Conductor parallel sessions |
| [[mem0\|mem0]] | evaluating | v1.0.11 (2026-04-07) | Memory architecture — auto-extraction, triple storage, scoped memory |
| [[archon\|Archon]] | cherry-pick | v0.5.0 (2026-07-13) | DAG workflow engine, YAML workflows, worktree isolation, multi-platform adapters |
| [[n8n\|n8n]] | cherry-pick | v2.29.10 (2026-07-13) | Context file architecture (CLAUDE.md→AGENTS.md chain-loading), plugin namespacing, spec-driven development |
| [[langgraph\|LangGraph]] | cherry-pick | v1.1.6 (2026-04-09) | Pregel BSP orchestration, typed channels, interrupt/Command primitives, threat model pattern |
| [[beads\|Beads]] | cherry-pick | v1.0.2 (2026-04-19) | Hash-based collision avoidance, dependency graph links, semantic memory decay, agent state machine |
| [[openviking\|OpenViking]] | cherry-pick | latest (2026-04-19) | L0/L1/L2 tiered context loading, filesystem-as-context paradigm, workspace file taxonomy |
| [[sandbox\|AIO Sandbox]] | evaluating | v1.0.0.150 (2026-04-19) | MCP Hub aggregation, all-in-one container, protocol adapter pattern |
| [[deer-flow\|DeerFlow]] | cherry-pick | v2.0 (2026-04-19) | Middleware-as-enforcement, batched parallel subagents, three-tier sandbox provisioner |
| [[ob1\|OB1 (Open Brain)]] | cherry-pick | latest (2026-04-20) | Skill template architecture, self-improving skills, two-layer review gate, personal OS domain extensions |
| [[memongo\|Memongo]] | evaluating | latest (2026-04-20) | MongoDB-native memory — single-store polymorphic evidence, $rankFusion hybrid retrieval, query decomposition + RRF, weighted-signal reranking, importance decay, surprisal novelty gate |
| [[mempalace\|MemPalace]] | evaluating | 3.3.2 (2026-04-23) | Local-first AI memory — verbatim-storage thesis, structured-index + unstructured-retrieval (wings/rooms/drawers + AAAK closets), background-hooks save model, AGENTS.md↔CLAUDE.md symlink, retraction log as governance artifact, tool-enforced dev/held-out split |
| [[supermemory\|Supermemory]] | evaluating | latest (2026-04-23) | Cloud-capable extraction-based memory — typed-relationship evolution graph (updates/extends/derives), static+dynamic profile composition, memory-vs-RAG framing, content-derived temporal expiration, hierarchical container-tag multi-tenancy, cross-provider benchmarking framework (MemoryBench), SKILL-as-package-export |
| [[taches-cc-resources\|TÂCHES CC Resources]] | cherry-pick | latest (2026-05-24) | Claude Code harness patterns, context loading, rules |
| [[deep-tutor\|Deep Tutor]] | monitor | latest (2026-05-24) | Pedagogical agent patterns |
| [[hermes-agent\|Hermes Agent]] | monitor | latest (2026-05-24) | Agent communication protocols |
| [[pi-agent\|Pi Agent]] | monitor | latest (2026-05-24) | Personal intelligence agent patterns |
| [[oz-workspace\|Oz Workspace]] | monitor | latest (2026-05-24) | Workspace management patterns |
| [[warp\|Warp]] | monitor | latest (2026-05-24) | Terminal AI integration |
| [[langflow\|Langflow]] | monitor | v1.9.3 (2026-05-25) | Multi-agent orchestration, flow composition, conversation management, component customization |
| [[adk-python\|ADK-Python]] | cherry-pick | v2.0.0 (2026-05-25) | Agent evaluation framework, tool integration abstractions, agent composition, deployment patterns |
| [[autogpt\|AutoGPT]] | cherry-pick | v0.5.0 (2026-05-25) | Continuous agent execution, workflow automation, block-based composition, fleet orchestration |
| [[autogen\|AutoGen]] | monitor | v0.7.5 (2026-05-25) | Multi-agent conversation patterns, group chat orchestration, composable termination, ledger-based orchestration |
| [[crewai\|CrewAI]] | cherry-pick | v1.14.6 (2026-05-25) | Role-based agent composition, crew orchestration, task delegation, prompt registry, memory primitives |
| [[letta\|Letta]] | cherry-pick | v0.16.8 (2026-05-25) | Hierarchical memory, self-editing memory, sleeptime pattern, tool rules, provider-adaptive rendering |

## Dataview Query

```dataview
TABLE spectrum_position, last_evaluated_version, last_evaluated_date
FROM "systems/improvement-loop/watched-libraries"
WHERE type = "watched-library"
SORT last_evaluated_date DESC
```
