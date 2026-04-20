---
name: Response Format Enum for Adaptive Tool Verbosity
summary: Add a response_format enum parameter (detailed vs. concise) to tool return values, letting the agent choose verbosity based on current task needs. ~65% token reduction when using concise format.
implementation_notes: Consider adding response_format to MCP tools that return variable-length results. Especially useful for tools that return full document content when often only metadata is needed.
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General / Cross-System
adopted_in: []
sources:
- anthropic-writing-effective-tools-for-agents.md
related_findings: []
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- managing-agent-context.md
---

## What It Is

Implement a response_format parameter on tools with an enum of DETAILED (~206 tokens) and CONCISE (~72 tokens). Detailed preserves IDs and full metadata for chaining; concise returns only high-signal information. The agent selects format based on current task needs.

## Why It Matters

Not every tool call requires full detail. When summarizing, concise output saves ~65% of tokens. When chaining operations that need returned IDs, detailed output preserves necessary state. Gives agents the same adaptive behavior humans use when scanning vs. deep-reading.

## Why People Are Using It

Production-tested at Anthropic. The measured token savings (206 vs 72 tokens) make this one of the simplest high-ROI context optimizations.

## Potential Improvements

Could extend to more than two levels (e.g., minimal/concise/standard/detailed). Could make the default adaptive based on remaining context budget.

## Potential Failure Modes

Agent may default to concise when it actually needs detailed, causing missing-ID errors in downstream tool calls. Need clear descriptions of when each format is appropriate.
