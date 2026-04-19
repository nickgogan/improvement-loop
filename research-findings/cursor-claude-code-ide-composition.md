---
notion_id: 32b1e08b-9b34-8152-9947-fba0f0ef34cb
name: Cursor + Claude Code IDE Composition
summary: Cursor as primary IDE with .cursor/mcp.json as canonical MCP config source, terminal panel for Claude Code CLI, and semantic search via Turbopuffer vector DB — architected to respect the 40-tool
  MCP limit.
implementation_notes: null
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in:
- S3 (Claude Code Build)
sources:
- cursor-ai-mcp-server-configuration-setup-auth-best.md
proposals: null
date_discovered: '2026-03-15'
last_updated: '2026-04-08'
related_findings:
- file: gpt-54-tool-search-deferred-tool-loading.md
  rel: same-problem
pipeline_status: "raw"
consumed_by: []
---
# Cursor + Claude Code IDE Composition

## What It Is
This is the S3 developer environment architecture: Cursor serves as the primary IDE with `.cursor/mcp.json` as the canonical MCP configuration source, Claude Code runs in Cursor's terminal panel as a CLI tool, and Turbopuffer provides semantic vector search across the vault. The design deliberately stays within Claude Code's 40-tool MCP limit by centralizing tool definitions in one config file.

## Why It Matters
Without a deliberate composition strategy, having both Cursor and Claude Code active simultaneously leads to conflicting MCP registrations and tool routing confusion. This pattern assigns each layer a clear role — Cursor for IDE intelligence, Claude Code for agentic execution — so they complement rather than collide.

## Why People Are Using It
Practitioners building agentic development environments have converged on Cursor + Claude Code as the de facto pairing for AI-assisted coding. The .cursor/mcp.json convention emerged from production use as a way to keep tool configs version-controlled and portable.

## Potential Improvements
The setup could benefit from auto-detection logic that warns when registered tools approach the 40-tool ceiling and suggests pruning low-priority tools. A dashboard showing active MCP registrations across both Cursor and Claude Code would reduce guesswork.

## Potential Failure Modes
When both Cursor and Claude Code are active, their MCP layers can conflict — tools registered in one may shadow or duplicate tools in the other. If .cursor/mcp.json is not treated as the single source of truth, config drift between the two environments becomes a silent failure.
