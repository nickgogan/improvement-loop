---
name: Tool Registry with Metadata-First Design
summary: 'Defining all agent tool capabilities as a data-structure registry (metadata + lazy loading) so agents can reason about their own capabilities without executing them. Claude Code maintains two
  parallel registries: command registry (207 user-facing) and tool registry (184 model-facing).'
implementation_notes: MetaSystem's skills serve a similar role but lack the metadata-first registry pattern. Skills are discovered via Glob/Grep rather than a queryable registry.
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropics-2-5-billion-leak-12-critical-pieces.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
related_findings:
- file: claude-code-12-agent-primitives.md
  rel: extended-by
- file: mcp-server-cards-discovery.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- designing-agent-tools.md
---
# Tool Registry with Metadata-First Design

## What It Is
Tools are defined as data first — each entry has name, source hint, responsibility description. Two parallel registries serve different consumers: command registry for user-facing commands, tool registry for model-facing tools. Implementations load on demand (lazy loading). Pattern: define capabilities as data before implementing them; list_tools() returns metadata + supports runtime filtering.

## Why It Matters
Enables agents to reason about available capabilities without executing anything. Supports runtime filtering, dynamic tool pool assembly, and permission management at the metadata level. Foundation for other primitives (permission tiers, tool pool assembly).

## Why People Are Using It
Proven in Anthropic's $2.5B Claude Code production system. Nate B Jones identifies it as a Tier 1 "day one non-negotiable" primitive.

## Potential Alternatives
Hardcoded tool lists in prompts. Tool descriptions inline in system prompts. Dynamic discovery from OpenAPI/MCP schemas.

## Potential Improvements
Auto-generation of registry entries from code annotations. Version-aware registries for tool evolution tracking.

## Potential Failure Modes
Registry/implementation drift if not kept in sync. Over-indexing on metadata without testing actual tool behavior. Registry maintenance burden at scale.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[tool-registry-metadata-first-design.md]] in `extracts/patterns/`
