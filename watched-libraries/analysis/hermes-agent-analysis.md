---
title: "hermes-agent -- Structural Analysis"
id: "hermes-agent-analysis"
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
  - "hermes-agent"
  - "agent-framework"
  - "memory"
  - "context-engineering"
  - "self-improvement"
analyzed_version: "latest (2026-05-24)"
analyzed_date: "2026-05-24"
repo_url: "https://github.com/nousresearch/hermes-agent"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
---

# hermes-agent -- Structural Analysis

## Metadata
- **Repo:** https://github.com/nousresearch/hermes-agent
- **Version analyzed:** latest (2026-05-24, via source entry + watched-library metadata)
- **Date:** 2026-05-24
- **Spectrum position:** study
- **Stars:** 165k | Python | Self-hosted autonomous agent

---

## 1. Structural Inventory

### Architecture
Single `AIAgent` class with multiple entry points:
- CLI (interactive/batch)
- HTTP API (persistent daemon)
- Telegram bot
- Discord bot
- Cron scheduler

### Key Components
| Component | Purpose |
|-----------|---------|
| AIAgent | Core agent class — routing, execution, memory management |
| Memory tiers | Hot/warm/cold with hard character ceilings per tier |
| Model slots | Per-task-type model configuration (8 slot types) |
| System prompt assembler | Layered prompt construction with cache markers |
| Skill system | Self-created/edited skill files from task experience |
| Companion repos | `hermes-agent-self-evolution` (DSPy), `hermes-compression-eval` |

---

## 2. Context File Map

### System Prompt Assembly
Layered construction with Anthropic `cache_control` markers on stable segments:
1. Core identity/personality (stable — cached)
2. System rules and boundaries (stable — cached)
3. Active skill instructions (semi-stable)
4. Memory context (dynamic — hot tier loaded per-turn)
5. Conversation history (dynamic)

The stable layers get `cache_control: { type: "ephemeral" }` markers so repeated requests hit Anthropic's prompt cache, reducing cost and latency.

---

## 3. Workflow Topology

### Auxiliary Model Slot Architecture
8 distinct model slots in config, each assignable to a different model:

| Slot | Purpose | Typical Model |
|------|---------|---------------|
| `main` | Primary conversation/reasoning | Large model (Opus/Sonnet) |
| `compression` | Context summarization | Fast model |
| `vision` | Image analysis | Vision-capable model |
| `summarization` | Document summarization | Fast model |
| `approval` | Safety/quality gate | Small model |
| `router` | Task routing decisions | Small/fast model |
| `title` | Session title generation | Small model |
| `skills` | Skill creation/editing | Capable model |

### Bounded Tiered Memory
```
Hot tier   — recent, high-relevance (loaded every turn, hard char ceiling)
Warm tier  — medium-relevance (loaded on demand, larger ceiling)
Cold tier  — archival (searched, not loaded unless queried)
```

Inference-driven curation: the agent itself decides what to promote/demote between tiers based on recency, relevance to current task, and usage frequency.

### Self-Improvement Loop
After N task completions:
1. Reflect on outcomes (success/failure patterns)
2. Create or edit skill files based on reflection
3. Skills become available for future tasks
4. Companion repo (`hermes-agent-self-evolution`) uses DSPy for offline prompt optimization

---

## 4. Governance Model

### Compression Quality Evaluation
Companion repo `hermes-compression-eval` provides:
- Evaluation framework for context compression quality
- Metrics for information loss during summarization
- Comparison across compression strategies

### Safety
- `approval` model slot acts as quality/safety gate
- Separate model for routing decisions (prevents main model from self-selecting)

---

## 5. Cross-Agent Protocol

### Multi-Channel Gateway
Single agent instance serving multiple channels simultaneously:
- Shared memory across channels
- Channel-specific conversation history
- Unified skill set regardless of entry point

### Companion Repos
| Repo | Purpose |
|------|---------|
| `hermes-agent-self-evolution` | DSPy offline optimization of prompts/skills |
| `hermes-compression-eval` | Evaluation framework for compression quality |

---

## Findings Candidates

Already extracted in session 89 (bypassed /promote-findings gate — flagged for retroactive review):

| # | Finding (already in KB) | Priority | Status |
|---|------------------------|----------|--------|
| 1 | Auxiliary Model Slot Architecture | P1 | `pipeline_status: raw` — needs retroactive gate approval |
| 2 | Bounded Tiered Memory with Inference-Driven Curation | P2 | `pipeline_status: raw` — needs retroactive gate approval |
| 3 | Layered Prompt Assembly with Stable-Segment Caching | P2 | `pipeline_status: raw` — needs retroactive gate approval |
