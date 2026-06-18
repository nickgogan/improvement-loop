---
name: "Letta"
type: "watched-library"
repo_url: "https://github.com/letta-ai/letta"
description: "Formerly MemGPT — framework for AI agents with advanced memory that can learn and self-improve over time. Features hierarchical memory (core, recall, archival), self-editing memory, skills system, subagents, and model-agnostic CLI tool."
spectrum_position: "cherry-pick"
what_we_use: "Hierarchical memory architecture, self-editing memory patterns, memory-driven learning loops, skills and subagent composition, continual learning primitives"
local_derivations: []
last_evaluated_version: "v0.16.8"
last_evaluated_date: "2026-05-25"
maintainer: "letta-ai"
status: "active"
tags:
  - "memory-architecture"
  - "self-improvement"
  - "continual-learning"
  - "agent-framework"
  - "python"
  - "cli"
related_findings: []
related_sources: []
date_added: "2026-05-25"
---

## What It Does

Framework for building AI agents with advanced memory that learn and self-improve over time. Formerly known as MemGPT — pioneered the concept of LLM agents managing their own memory hierarchically (core memory for always-available context, recall memory for conversation history, archival memory for long-term storage). Features include self-editing memory (agents modify their own memory), skills system for capability extension, subagent composition, and a CLI tool (Letta Code) for local agent operation. Model-agnostic.

## What We Use From It

Cherry-pick patterns:
1. **Hierarchical memory architecture** — Core/recall/archival memory tiers with different access patterns and persistence
2. **Self-editing memory patterns** — How agents modify their own context/memory during operation
3. **Memory-driven learning loops** — Continual learning through memory accumulation and self-improvement
4. **Skills and subagent composition** — Extensibility via skills and subagent delegation
5. **CLI agent patterns** — Terminal-first agent operation with local memory

## Spectrum Rationale

**Cherry-pick** — Letta (MemGPT) is the canonical reference for memory-centric agent design. Its hierarchical memory model directly informs IL's research on memory architecture (Dimension 1, Sub-dimensions 1.A and 1.B). The self-editing memory pattern and continual learning loop are novel and worth deep study. The CLI-first operation model (Letta Code) parallels MetaSystem's Claude Code integration.

## Change Signals

Watch for:
- Memory architecture changes (new tiers, new access patterns)
- Self-improvement mechanism evolution
- Memory decay/compaction strategies
- Multi-agent memory sharing patterns
- Skills system architecture
- CLI and local operation patterns
