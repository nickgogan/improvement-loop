---
name: Proprietary Extension Layer on Open Protocol (Google Play Services Pattern)
summary: 'Conway''s CNW.zip extension format creates a proprietary layer on top of MCP (Anthropic''s own open standard). Extensions include custom interface panels, information handlers, and tools that
  work only inside Conway. This mirrors the Google Play Services pattern: Android is open-source, but the valuable commercial layer (Maps, payments, Play Store) is proprietary. Developers face the same
  App Store vs. Open Web choice mobile devs faced in 2008.'
implementation_notes: MCP tools remain portable but will face distribution disadvantage vs. proprietary extensions. Monitor all three labs for similar proprietary layers.
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- General
adopted_in: []
sources:
- conway-anthropics-always-on-agent.md
related_findings: []
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: raw
consumed_by: []
---
# Proprietary Extension Layer on Open Protocol (Google Play Services Pattern)

## What It Is
MCP (Model Context Protocol) is Anthropic's open standard for connecting AI tools to data sources — adopted by OpenAI, Google, and the Linux Foundation. Conway's extension format (CNW.zip) sits on top of MCP and adds a proprietary layer: custom interface panels, information handlers, and tools that work specifically inside Conway's environment. Developers face two paths: (1) Build a standard MCP tool — portable across all clients, but no distribution mechanism, no app store, no featured placement. (2) Build a Conway extension — only works in Conway, but discoverable in a built-in extensions directory to millions of Claude subscribers. This is the Google Play Services pattern: the open kernel (Android/MCP) doesn't matter commercially when the valuable apps require the proprietary services (Play Services/Conway extensions).

## Why It Matters
The open MCP standard may become the "open web" of the agent era — architecturally correct but commercially secondary to proprietary extension ecosystems. OpenAI and Google will likely build similar proprietary layers, fragmenting the tool ecosystem by platform.

## Why People Are Using It
Not yet available. The pattern is predictive, based on historical precedent (Google Play Services, Apple App Store) and the Conway leak.

## Potential Failure Modes
- Tool fragmentation — same capability must be built 3 times for 3 platforms
- MCP becomes a lowest-common-denominator standard while real innovation happens in proprietary extensions
- Small tool developers forced to pick a platform rather than build universally
