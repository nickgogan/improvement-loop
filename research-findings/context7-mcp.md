---
notion_id: 32b1e08b-9b34-8153-853f-e36e5d11a592
name: Context7 MCP
summary: An MCP server that provides library-specific documentation to Claude Code dynamically at query time, replacing reliance on potentially outdated training data. Reduces API hallucination when building
  against specific libraries like the Notion API.
implementation_notes: null
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- claude-code-works-better-when-you-do-this.md
proposals: null
date_discovered: '2026-03-15'
last_updated: '2026-04-08'
related_findings:
- file: context7-plugin-live-api-documentation-injection.md
  rel: extends
- file: mcp-n-plus-m-integration-economics.md
  rel: enabled-by
pipeline_status: raw
consumed_by: []
---
# Context7 MCP

## What It Is
Context7 is an MCP server that serves live, library-specific documentation directly into Claude Code's context at query time. Instead of relying on training data that may be months behind a library's current API, Context7 fetches the relevant documentation dynamically and injects it as context. It integrates via the standard MCP protocol.

## Why It Matters
LLMs hallucinate API details when their training data predates library updates. For code-generating agents working against fast-moving APIs — like Notion, Stripe, or GitHub — this produces incorrect function calls, wrong parameter names, and subtle bugs. Context7 grounds the agent in current documentation, making generated code significantly more reliable.

## Why People Are Using It
Documented in v5 of the AI coding tools report as a notable addition to Claude Code's MCP ecosystem. Particularly valuable when building against APIs that update frequently. The pattern of injecting live docs rather than relying on training data is a recognized best practice in production agent setups.

### CLI + Skills Integration (2026-04-07)

Newer practitioner evidence recommends configuring Context7 as a **CLI + Skills** integration rather than an MCP server. This avoids eager loading of tool schemas into context (see CLI-first finding). The recommended workflow:

1. Context7 is configured as a CLI tool with a skill document teaching Claude the commands
2. During the Superpowers review phase, Claude is prompted to use Context7 to fact-check code against current library documentation
3. A system prompt query instruction is stored in a `.md` file: "When you need [X], query the NotebookLM KB using [API method]" — this same pattern applies to Context7 queries

This represents an evolution from the original MCP-based integration approach.

## Potential Improvements
Frequently accessed documentation could be cached locally to eliminate latency on repeat calls. A fallback to cached snapshots when the documentation server is unavailable would improve reliability. Selective injection — only pulling docs for the specific methods being used — would keep context window usage efficient.

## Potential Failure Modes
Adds latency to every tool call that triggers a documentation lookup, which can slow down agent execution in fast-paced build sessions. If the Context7 server is slow or unreliable, it becomes a bottleneck. Over-injection of documentation can consume context window space and crowd out other relevant information.
