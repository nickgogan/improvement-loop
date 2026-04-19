---
name: "LangGraph"
type: "watched-library"
repo_url: "https://github.com/langchain-ai/langgraph"
description: "Low-level orchestration framework for building stateful, multi-actor agents with graph-based execution (Pregel/BSP), durable checkpointing, human-in-the-loop interrupts, and both declarative (StateGraph) and functional (@entrypoint/@task) APIs"
spectrum_position: "cherry-pick"
what_we_use: "Graph-based agent orchestration patterns, channel-based state management, interrupt/Command primitives for human-in-the-loop, checkpoint persistence architecture, threat model documentation pattern"
local_derivations: []
last_evaluated_version: "v1.1.6"
last_evaluated_date: "2026-04-09"
maintainer: "langchain-ai"
status: "active"
tags:
  - "orchestration"
  - "agent-framework"
  - "state-management"
  - "python"
  - "multi-agent"
related_findings: []
related_sources: []
date_added: "2026-04-09"
---

## What It Does

Low-level Python framework for building stateful, multi-actor AI agent applications. Provides a graph-based execution model (Bulk Synchronous Parallel via the Pregel engine) where user-defined nodes process shared state through typed channels. Two authoring APIs: declarative StateGraph (add_node/add_edge/compile) and functional (@entrypoint/@task decorators). Features durable execution with checkpoint persistence (Postgres/SQLite), human-in-the-loop via interrupt() primitives, Command for graph control flow, Send for fan-out, subgraph composition, remote graph composition via SDK, and Docker-based deployment via CLI.

Part of the LangChain ecosystem — integrates with LangChain, LangSmith, and Deep Agents. Used by Klarna, Replit, Elastic, and others.

## What We Use From It

Cherry-pick patterns:
1. **Graph-based agent orchestration** — StateGraph with typed channels, Pregel execution engine (BSP), topological node execution
2. **Channel-based state management** — Typed channels (LastValue, BinaryOperator, EphemeralValue, Topic, NamedBarrier) as the state primitive, not raw dicts
3. **Interrupt/Command primitives** — `interrupt()` function for human-in-the-loop, `Command` for graph control flow (goto + state update), `Send` for fan-out to multiple nodes
4. **Checkpoint persistence architecture** — BaseCheckpointSaver with Postgres/SQLite implementations, JsonPlusSerializer with msgpack/JSON/pickle codecs, EncryptedSerializer
5. **Threat model documentation** — Auto-generated threat model with trust boundaries, data classification, component inventory, and threat enumeration

## Spectrum Rationale

**Cherry-pick** — LangGraph is a Python agent framework deeply integrated with the LangChain ecosystem. MetaSystem operates in the Claude Code / TypeScript context engineering space. The orchestration patterns (graph execution, channels, interrupts) are conceptually relevant but the implementation is not directly adoptable. The threat model documentation pattern is novel and worth studying independently.

## Change Signals

Watch for:
- New channel types or state management primitives
- Changes to interrupt/Command control flow patterns
- Checkpoint architecture changes
- Functional API (@entrypoint/@task) evolution
- New multi-agent coordination patterns
- Subgraph composition patterns
