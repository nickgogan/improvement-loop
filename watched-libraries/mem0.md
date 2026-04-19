---
name: "mem0"
type: "watched-library"
repo_url: "https://github.com/mem0ai/mem0"
description: "Universal memory layer for AI agents"
spectrum_position: "evaluating"
what_we_use: "Memory architecture patterns — automatic fact extraction, triple storage (vector+KV+graph), user/session/agent-scoped memory"
local_derivations: []
last_evaluated_version: "v1.0.11"
last_evaluated_date: "2026-04-07"
maintainer: "mem0ai"
status: "active"
tags:
  - "memory"
  - "context-engineering"
  - "tools"
related_findings:
  - "agent-memory-architecture-multi-agent-layered.md"
related_sources: []
date_added: "2026-04-07"
---

## What It Does

An intelligent memory layer that enables AI agents to remember user preferences, adapt to individual needs, and continuously learn. Extracts facts and preferences from conversations automatically. Triple storage architecture (vector DB + key-value DB + graph DB). Python and JavaScript SDKs. Integrations with OpenAI, LangGraph, CrewAI. Self-hosted or managed platform options. ~50.2K GitHub stars.

## What We Use From It

Memory architecture patterns — particularly automatic fact/preference extraction from conversations, user/session/agent-scoped memory, and the triple storage approach. MetaSystem's auto-memory system (file-based) is a simpler version of this pattern. Evaluating whether mem0's architecture could inform a future enhancement to MetaSystem's memory layer.

## Spectrum Rationale

Evaluating. mem0 solves a problem MetaSystem has (persistent memory across sessions) but MetaSystem's current file-based approach (MEMORY.md + individual memory files) works at current scale. The triple storage architecture (vector+KV+graph) is interesting for future scaling but adds infrastructure MetaSystem doesn't need yet. Default thin-wrapper position pending scale needs.

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-04-07 | v1.0.6 | Initial evaluation. Triple storage, auto-extraction, scoped memory. |
| 2026-04-07 | v1.0.11 | reasoning_effort parameter, soft-delete graph relationships, memory leak prevention, OpenClaw plugin refactor (modular arch, 329 tests). |
