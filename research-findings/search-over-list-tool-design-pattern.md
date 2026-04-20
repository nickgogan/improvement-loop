---
name: Search-Over-List Tool Design Pattern
summary: Replace list/enumerate tools with search/filter tools to match agent affordances — agents have limited context windows but abundant compute, so searching is cheaper than listing.
implementation_notes: Audit current MCP tool definitions for list-style patterns that could be converted to search-style. Especially relevant for research-sources and research-findings queries.
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General / Cross-System
adopted_in: []
sources:
- anthropic-writing-effective-tools-for-agents.md
related_findings:
- file: gpt-54-tool-search-deferred-tool-loading.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-19'
pipeline_status: synthesized
consumed_by:
- designing-agent-tools.md
---

## What It Is

Instead of providing list_contacts that returns all records, provide search_contacts that accepts query parameters. This aligns tool design with the agent's constraint profile: limited context window but abundant compute cycles. Validated across Anthropic's internal MCP servers (Claude Code, Slack MCP, Asana MCP).

## Why It Matters

Agents waste context reading through large result sets. Search-oriented tools match human intuition and dramatically reduce token consumption, enabling more complex multi-step workflows within context limits.

## Why People Are Using It

Anthropic applies this as a core design principle across all internal MCP server tools. The pattern emerged from observing agents failing when given list-style tools that returned too many results.

## Potential Improvements

Could evolve toward adaptive result sizing where the tool adjusts verbosity based on the agent's remaining context budget.

## Potential Failure Modes

Search requires the agent to know what to search for — fails when the agent needs to browse or discover unexpected items. May need a "browse top N" fallback for exploration tasks.
