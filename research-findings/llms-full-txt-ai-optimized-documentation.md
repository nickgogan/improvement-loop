---
name: "llms-full.txt: AI-Optimized Documentation Endpoint"
summary: "Documentation sites produce an llms-full.txt file that agents can consume directly. BMad's docs site at docs.bmadmethod.org provides this endpoint. \"You can point your AI agent to this URL and the agent can answer questions for you.\""
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: "P3 (Monitor)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "bmad-v6-is-finally-here.md"
proposals: []
date_discovered: "2026-04-07"
last_updated: 2026-04-08
related_findings:
  - file: "agent-context-kiss-commandments-minimum-viable.md"
    rel: "same-problem"
pipeline_status: "raw"
consumed_by: []
---

# llms-full.txt: AI-Optimized Documentation Endpoint

## What It Is
An emerging convention where documentation sites produce a single pre-formatted text file (llms.txt or llms-full.txt) containing all documentation in a format optimized for AI agent consumption. Instead of scraping HTML and parsing it, agents fetch one URL and get structured, complete documentation. BMad's implementation at docs.bmadmethod.org covers their full method documentation.

## Why It Matters
AI agents waste significant tokens and time on HTML parsing, navigation, and deduplication when consuming web documentation. A single llms-full.txt endpoint eliminates this overhead and provides a canonical, complete representation that the documentation maintainer controls.

## Why People Are Using It
BMad's docs site demonstrates the pattern in production. The convention is gaining traction as more teams build agent-first tooling. Related to Context7 MCP (which also provides structured docs to agents), but llms.txt is simpler -- no MCP server required, just a static file.

## Potential Improvements
MetaSystem could adopt this convention for its own documentation -- an llms.txt endpoint for governance docs, patterns, and guides. This would make MetaSystem's knowledge accessible to external agents or new sessions without requiring full workspace context.

## Potential Failure Modes
Large llms.txt files may exceed context windows; needs a chunking strategy or tiered approach (llms.txt for summary, llms-full.txt for complete docs). Stale files if not regenerated on documentation updates.
