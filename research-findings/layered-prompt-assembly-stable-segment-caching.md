---
name: "Layered Prompt Assembly with Stable-Segment Caching"
summary: "System prompt is assembled from ordered layers (identity, memory, skills, project context, provider instructions, ephemeral state). Stable layers (SOUL.md, MEMORY.md, USER.md, project context) are marked with Anthropic cache_control markers via a dedicated module. Ephemeral layers (budget warnings, context pressure hints) are injected as separate content blocks to avoid invalidating the cache. This decouples the caching boundary from the prompt structure boundary."
implementation_notes: "MetaSystem's CLAUDE.md files are loaded as system context but not explicitly marked with cache_control. This finding suggests a dedicated prompt assembly module that separates stable segments (CLAUDE.md, agent definitions) from ephemeral segments (task state, progress updates) for optimal cache hit rates."
category: "Prompt Craft"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "hermes-agent-nousresearch-analysis.md"
proposals: null
date_discovered: "2026-05-24"
last_updated: "2026-05-24"
related_findings:
  - file: "five-layer-agent-prompt-architecture.md"
    rel: "extends"
pipeline_status: "synthesized"
consumed_by:
  - "model-resilient-prompt-engineering.md"
  - "templates/seven-layer-prompt-assembly-with-cache-control.md"
  - "rules/never-inline-ephemeral-into-cached-layers.md"
tags:
  - "prompt-engineering"
  - "context-engineering"
  - "caching"
---

# Layered Prompt Assembly with Stable-Segment Caching

## What It Is

A system prompt architecture assembled from ordered layers at each API call:

1. Core role/persona
2. SOUL.md (global personality)
3. MEMORY.md + USER.md (persistent facts)
4. Relevant skills metadata (titles, "When to use" sections)
5. Project context file (AGENTS.md / .hermes.md)
6. Provider-specific tool-calling instructions
7. Ephemeral layers (budget warnings, context pressure hints)

Stable layers (1-5) are marked with Anthropic `cache_control: {"type": "ephemeral"}` via a dedicated `prompt_caching.py` module. Dynamic layers (6-7) are sent without cache markers.

## Why It Matters

Prompt caching reduces cost and latency for repeated API calls. The key insight: decoupling the caching boundary from the prompt structure boundary. Stable segments (identity, memory, skills) change infrequently and benefit from caching. Ephemeral segments (budget warnings, context state) change every call and would invalidate the cache if included in cached blocks.

## How It Could Fail

Cache markers add complexity to prompt assembly. Over-caching (marking semi-dynamic content as stable) causes stale context. Under-caching (not marking stable content) wastes cost savings. The five-minute TTL on Anthropic's cache means benefits only accrue for rapid multi-turn conversations.
