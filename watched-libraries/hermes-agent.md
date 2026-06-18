---
name: "hermes-agent"
repo: "nousresearch/hermes-agent"
url: "https://github.com/nousresearch/hermes-agent"
description: "Self-hosted, self-improving autonomous agent with persistent server daemon, CLI, HTTP API, and web UI. Closed learning loop — creates and refines skills from experience, maintains persistent user model, compresses context automatically."
language: "Python"
stars: 165598
spectrum_position: "study"
tracking_focus:
  - "Auxiliary model slots pattern"
  - "Bounded tiered memory design"
  - "Layered prompt assembly with prompt caching"
  - "hermes-compression-eval methodology"
version_tracked: "latest (2026-05-24)"
last_analyzed: "2026-05-24"
analysis_doc: "watched-libraries/analysis/hermes-agent-analysis.md"
tags:
  - "agent-framework"
  - "memory"
  - "context-engineering"
  - "prompt-craft"
  - "self-improvement"
---

# hermes-agent

NousResearch's self-hosted autonomous agent. Most mature open-source implementation of several patterns the IL is researching: bounded tiered memory, layered prompt assembly, auxiliary model routing, and inference-driven skill creation from task experience.

## Key Architecture

- Single `AIAgent` class, multi-entrypoint (CLI, HTTP, Telegram, Discord, cron)
- Hot/warm/cold memory tiers with hard character ceilings
- Per-task-type model slots in config (main, compression, vision, summarization, approval, router, title, skills)
- Layered system prompt assembly with Anthropic prompt caching on stable segments
- Self-improvement loop: after N completions, reflects on outcomes and creates/edits skill files
- Companion repos: `hermes-agent-self-evolution` (DSPy offline optimization), `hermes-compression-eval` (compression quality evaluation)
