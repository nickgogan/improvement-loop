---
title: "DeepTutor -- Structural Analysis"
id: "deep-tutor-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "2026-05-24"
updated: "2026-05-24"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "deep-tutor"
  - "agent-framework"
  - "orchestration"
  - "tools"
  - "capabilities"
analyzed_version: "latest (2026-05-24)"
analyzed_date: "2026-05-24"
repo_url: "https://github.com/HKUDS/DeepTutor"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
---

# DeepTutor -- Structural Analysis

## Metadata
- **Repo:** https://github.com/HKUDS/DeepTutor
- **Version analyzed:** latest (2026-05-24, cloned at /tmp/DeepTutor)
- **Date:** 2026-05-24
- **Spectrum position:** study
- **Stars:** 24k | Python | Agent-native tutoring platform

---

## 1. Structural Inventory

### File Tree
```
deeptutor/
  agents/         — Base agent class
  api/            — WebSocket API server
  app/            — Application facade
  book/           — Knowledge base (compiler, context, engine, storage, streaming)
  capabilities/   — Level 2 multi-stage pipelines (7 capabilities)
  runtime/
    orchestrator.py   — ChatOrchestrator (unified entry)
    launcher.py       — Backend + frontend lifecycle
    registry/         — Tool + Capability registries
deeptutor_cli/    — CLI-only package (Typer)
deeptutor_web/    — Web frontend
tests/            — Test suite
```

### Entry Points
| Entry | Stack |
|-------|-------|
| CLI (Typer) | `deeptutor run <capability> "prompt"` or `deeptutor chat` (REPL) |
| WebSocket API | `/api/v1/ws` — real-time streaming |
| Python SDK | `from deeptutor.app import facade` |

---

## 2. Context File Map

### Agent Context
| File | Purpose |
|------|---------|
| `AGENTS.md` | Full architecture description for coding agents |
| `SKILL.md` | Skill definition for AI assistants working on DeepTutor |
| `CONTRIBUTING.md` | Development workflow, testing, PR conventions |
| `.pre-commit-config.yaml` | Pre-commit hooks (secrets baseline) |

### AGENTS.md Content
Comprehensive agent briefing:
1. Architecture diagram (ASCII) showing orchestrator → registry → capabilities
2. Level 1 Tools table (9 context-gated + 5 user-toggleable)
3. Level 2 Capabilities table (7 capabilities with stage breakdowns)
4. CLI usage examples
5. Key file paths
6. Runtime settings location

---

## 3. Workflow Topology

### Two-Layer Plugin Model

**Level 1 — Tools (single-shot, LLM picks on demand):**
| Category | Tools |
|----------|-------|
| Context-gated (always-on) | `rag`, `read_source`, `read_memory`, `write_memory`, `web_fetch`, `list_notebook`, `write_note`, `github`, `ask_user` |
| User-toggleable | `brainstorm`, `web_search`, `paper_search`, `code_execution`, `reason` |
| Coming soon | `geogebra_analysis` |

**Level 2 — Capabilities (multi-stage pipelines that own the turn):**
| Capability | Stages |
|------------|--------|
| `chat` | thinking → acting → observing → responding (agentic loop, default) |
| `auto` | analyzing → delegating → synthesizing (meta-router) |
| `deep_solve` | planning → reasoning → writing |
| `deep_question` | ideation → generation |
| `deep_research` | rephrasing → decomposing → researching → reporting |
| `visualize` | analyzing → generating → reviewing (routes to sub-types) |
| `math_animator` | concept_analysis → concept_design → code_generation → code_retry → summary → render_output |

### ChatOrchestrator
Routes `UnifiedContext` to selected capability:
1. Receives input from any entry point
2. Resolves capability (explicit or `auto` routes)
3. Dispatches to capability with context
4. Capability executes stages sequentially
5. All capabilities converge on `emit_capability_result()` (shared envelope: response + cost_summary)

### StreamBus Architecture
All capabilities emit events on a shared `StreamBus`:
- Fan-out to all connected consumers
- Enables real-time streaming across entry points
- Status updates per capability stage
- Cost tracking via `UsageTracker`

### i18n
Capability prompts in `capabilities/prompts/{en,zh}/<name>.yaml` — full internationalization of agent behavior.

---

## 4. Governance Model

### Development
- Pre-commit hooks with secrets baseline detection
- Docker-based deployment (3 compose variants: dev, production, GHCR)
- `CITATION.cff` for academic attribution
- Multi-package distribution: `deeptutor` (full) and `deeptutor-cli` (CLI-only)

### Configuration
Runtime settings in `data/user/settings/*.json`:
- Project-root `.env` files intentionally ignored
- User-specific configuration isolated from code

---

## 5. Cross-Agent Protocol

### Tool Interaction Pattern
- `ask_user` tool pauses the turn and resumes with user's reply (human-in-the-loop within tool call)
- `reason` tool makes a dedicated deep-reasoning LLM call (model delegation within tool layer)
- Context-gated tools auto-mount based on active KB/sources (dynamic toolset)

### Capability Delegation
The `auto` capability acts as a meta-router:
1. Analyzes the user's intent
2. Delegates to the most appropriate capability
3. Synthesizes the result

This creates a two-level routing: orchestrator routes to capability, `auto` capability routes between capabilities.

---

## Findings Candidates

Already extracted in session 89 (bypassed /promote-findings gate — flagged for retroactive review):

| # | Finding (already in KB) | Priority | Status |
|---|------------------------|----------|--------|
| 1 | Two-Layer Plugin Model: Tools vs Capabilities | P2 | `pipeline_status: raw` — needs retroactive gate approval |

### Additional candidates (not yet extracted):

| # | Pattern | Priority | Category | Evidence |
|---|---------|----------|----------|----------|
| 2 | **StreamBus Event Fan-Out for Capability Observability** — All capabilities emit on a shared bus; consumers get real-time stage-by-stage progress. Decouples capability execution from presentation layer. | P3 | Orchestration | `_shared.py`, StreamBus architecture in AGENTS.md |
| 3 | **Meta-Router Capability (`auto`)** — A capability that analyzes intent and delegates to other capabilities. Two-level routing: orchestrator → capability → sub-capability. | P3 | Orchestration | `capabilities/auto.py`, AGENTS.md |
| 4 | **Context-Gated vs User-Toggleable Tool Visibility** — Tools divided into always-on (mounted based on active KB/sources) and user-controlled (explicit opt-in via settings). Reduces tool noise. | P3 | Tool Integration | AGENTS.md Level 1 Tools section |
