---
name: "OpenViking"
type: "watched-library"
repo_url: "https://github.com/volcengine/OpenViking"
description: "Context database for AI agents — filesystem paradigm for unified memory/resource/skill management, three-tier context loading (L0/L1/L2), directory recursive retrieval with semantic search, visualized retrieval trajectories"
spectrum_position: "cherry-pick"
what_we_use: "Three-tier context loading architecture (L0/L1/L2), filesystem paradigm for context management, directory recursive retrieval, automatic session compression, visualized retrieval trajectories for debugging"
local_derivations: []
last_evaluated_version: "latest"
last_evaluated_date: "2026-04-19"
maintainer: "volcengine (ByteDance)"
status: "active"
tags:
  - "context-engineering"
  - "memory"
  - "retrieval"
  - "filesystem"
related_findings: []
related_sources: []
date_added: "2026-04-19"
---

## What It Does

An open-source context database designed specifically for AI agents. Replaces fragmented vector storage with a unified filesystem paradigm for memory, resource, and skill management. Three-tier context loading (L0/L1/L2) reduces token consumption by loading progressively more detail on demand. Combines native filesystem methods with semantic search for directory recursive retrieval. Features visualized retrieval trajectories for debugging context assembly, and automatic session management that compresses conversations and extracts long-term memory. Python primary with Rust CLI/core components.

Key capabilities:
- **Filesystem paradigm**: Directories as context namespaces, files as context units
- **Tiered loading (L0/L1/L2)**: Progressive detail — summaries first, full content on demand
- **Directory recursive retrieval**: Filesystem traversal + semantic search hybrid
- **Visualized retrieval**: Observable context retrieval trajectories for debugging
- **Auto-session management**: Conversation compression + long-term memory extraction

## What We Use From It

Cherry-pick patterns:
1. **Three-tier context loading** — L0 (summary), L1 (structure), L2 (full content) as a general pattern for progressive context assembly
2. **Filesystem paradigm for context** — treating context like a filesystem with directories, files, and traversal operations
3. **Retrieval trajectory visualization** — making context assembly observable and debuggable
4. **Auto-session compression** — automatic conversation summarization with long-term memory extraction

## Spectrum Rationale

**Cherry-pick** — OpenViking is a standalone context database server. MetaSystem doesn't need the server infrastructure, but the tiered loading architecture and filesystem-as-context paradigm are directly relevant to Context Engineering research. The L0/L1/L2 pattern maps to how CLAUDE.md chain-loading already works in practice.

## Change Signals

Watch for:
- Changes to the tier loading strategy
- New retrieval algorithms
- MCP integration
- Agent framework adapters
