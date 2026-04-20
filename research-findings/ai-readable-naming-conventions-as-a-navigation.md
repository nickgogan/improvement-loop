---
notion_id: 32b1e08b-9b34-81af-b2a7-cd92001100e9
name: AI-Readable Naming Conventions as a Navigation System
summary: Establishing and documenting file naming conventions in CLAUDE.md (e.g., {topic}-draft.md, {YYYY}-{MM}-{topic}.md, demo-v{N}.md) allows the agent to locate specific files by pattern matching without
  querying a database or building an index.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- stop-building-ai-agents-use-this-folder-system-ins.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# AI-Readable Naming Conventions as a Navigation System

## What It Is
Jake's CLAUDE.md includes a naming conventions section: blog drafts follow {filename}-draft.md or {filename}-v2.md; newsletters follow {YYYY}-{MM}-{topic}.md; production outputs follow demo-{name}-v{N}.md. The agent, having read this convention, can be told 'pull the API-guide demo v2 and build a spec from it' and immediately knows the file is named demo-api-guide-v2.md without a directory listing. This eliminates the need for database queries, vector search, or file indexes for routine navigation.

## Why It Matters
File system navigation is a major source of tool calls (and therefore tokens and latency) in agentic workflows. If the agent must list directories and read multiple files to find what it needs, context fills with navigation overhead. Named conventions convert discovery from a search problem into a pattern-match lookup.

## Why People Are Using It
Zero infrastructure — no database, no vector store, no Python injection. Works with any Claude Code setup. Human-readable conventions also improve the operator's own navigation. Jake explicitly: 'I have zero code technically speaking running any sort of Python injection or framework or database.'

## Potential Alternatives
File indexes (maintained as a separate manifest file), SQLite/vector databases, Notion databases as file references, git tag-based discovery.

## Potential Improvements
Convention validation: the agent could check that newly created files follow the declared naming convention and warn when they don't. Automated convention discovery: AI analyzes existing files and proposes conventions from observed patterns.

## Potential Failure Modes
Convention drift: users create files outside the convention, agent can't find them. Multiple conventions for the same file type creating ambiguity. Naming collisions if convention doesn't include enough disambiguation tokens.
