---
name: "NousResearch hermes-agent Structural Analysis"
source_type: "Tool Release"
status: "Done"
key_takeaways: "165k-star self-improving agent framework. Key patterns: auxiliary model slot architecture (per-task-type model config), bounded tiered memory with inference-driven curation (hot/warm/cold with char ceilings), layered system prompt assembly with Anthropic cache_control markers on stable segments. Companion compression-eval repo validates context compression quality."
relevance: "High"
added_by: "Nick"
tags:
  - "context-engineering"
  - "agent-design"
  - "prompt-engineering"
  - "tools"
url: "https://github.com/nousresearch/hermes-agent"
authority: []
findings:
  - "auxiliary-model-slot-architecture.md"
  - "bounded-tiered-memory-inference-driven-curation.md"
  - "layered-prompt-assembly-stable-segment-caching.md"
date_added: "2026-05-24"
date_processed: "2026-05-24"
---

# NousResearch hermes-agent Structural Analysis

Structural analysis of `nousresearch/hermes-agent` (165k stars, Python). Self-hosted autonomous agent with persistent daemon, multi-channel gateway, and closed learning loop.
