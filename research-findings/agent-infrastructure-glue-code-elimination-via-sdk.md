---
name: "Agent Infrastructure Glue Code Elimination via SDK"
summary: "Traditional framework-based agents require substantial glue code: RAG pipeline (chunking, embedding, ingestion), conversation history storage, session management, state management, and tool wiring. Batteries-included SDKs (Claude Agent SDK, Codex SDK) eliminate this infrastructure layer entirely, reducing entire agents to single-file implementations. The tradeoff is speed, cost, and control."
implementation_notes: null
category: "Agentic Systems"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P3
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "sdk-vs-framework-decision-ai-agents.md"
related_findings:
  - file: framework-abstraction-tax-for-agents.md
    rel: same-problem
  - file: sdk-vs-framework-decision-for-agent-building.md
    rel: enables
  - file: six-layer-agent-infrastructure-stack.md
    rel: same-problem
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "classified"
consumed_by: []
tags:
  - "session-95-reextract"
---

## What It Is

A concrete enumeration of the infrastructure glue code that framework-based agents require and that SDK-based agents eliminate. The traditional agent build stack (2024-2025 standard) requires:

1. **Framework selection and configuration** -- choosing and learning Pydantic AI, LangGraph, n8n, etc.
2. **Tool definition** -- defining each capability as a typed function with descriptions
3. **RAG pipeline** -- chunking strategy, embedding model selection, ingestion pipeline, vector database setup
4. **Database management** -- tables for documents, chunks, messages, sessions
5. **Agent loop wiring** -- state management, short-term memory, conversation history storage
6. **Session management** -- storing and retrieving conversation history across interactions

SDK-based agents collapse all six layers into SDK configuration: tools are declared as permissions, RAG is replaced by built-in file search, conversation history is managed automatically, and the agent loop is the SDK itself. The result: entire agents in single files with more capabilities and less code than their framework equivalents.

## Why It Matters

The framework abstraction tax finding (already in KB) focuses on debugging opacity -- frameworks hide what's happening. This finding addresses a different cost: the sheer volume of infrastructure code required before an agent can do anything useful. A practitioner estimates "hundreds of lines" for the framework stack vs. a single-file SDK implementation with more features. This infrastructure burden is the primary reason practitioners are shifting to SDKs for personal and small-team agents.

The distinction matters for MetaSystem: while we don't build framework-based agents today, understanding the infrastructure layers helps assess which components of our agent system are genuinely load-bearing vs. which could be simplified.

## Why People Are Using It

- Dramatically less code for equivalent (or greater) capability
- No database setup or management required for conversation history
- Built-in file search replaces the entire RAG pipeline for small corpora
- Skills and MCP servers provide extensible capability without custom tool wiring
- Faster time-to-working-agent: prototype in hours instead of days

## Potential Improvements

- SDK "eject" commands that generate the equivalent framework code when you need to migrate
- Lightweight SDK modes that strip unnecessary infrastructure for simple use cases
- Plugin architectures that let you replace individual SDK layers (e.g., swap built-in file search for custom RAG)

## Potential Failure Modes

- Losing the ability to inspect and debug agent behavior because infrastructure is hidden in the SDK
- Building complex agents on SDK that outgrow its capabilities, requiring a painful full rewrite to a framework
- Assuming SDK-managed conversation history is sufficient for production observability requirements
- SDK infrastructure becoming the new "glue code" when multiple SDKs need to interoperate
