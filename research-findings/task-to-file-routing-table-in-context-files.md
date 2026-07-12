---
notion_id: 32b1e08b-9b34-81dd-972b-cb643a3985aa
name: Task-to-File Routing Table in Context Files
summary: A simple markdown table within each workspace's context file maps task types to the specific files that must be read, files to skip, and optional skills to invoke -- replacing token-expensive full-directory
  reads with targeted selective loading.
implementation_notes: null
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- stop-building-ai-agents-use-this-folder-system-ins.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-07-12'
related_findings:
- file: skills-inside-workspace-contextual-skill.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: intent-based-meta-routing-skill.md
  rel: same-problem
pipeline_status: extracted
consumed_by:
- templates/task-to-file-routing-table-in-context-files.md
---
# Task-to-File Routing Table in Context Files

## What It Is
Jake shows a routing table inside a workspace context file with columns: Task | Read These Files | Skip These Files | Skills Needed. Example rows: 'Write blog post -> read: voice-context.md, blog-template.md; skip: production-outputs/; skill: humanizer'. The agent reads this table at the start of any task in that workspace and only loads the specified files. Jake calls this 'the most important pattern in the whole system' -- without it, the agent either reads everything (wastes tokens) or guesses wrong about what matters.

## Why It Matters
Token management is the core constraint in long agentic sessions. Loading irrelevant files wastes context window space, increases cost, and degrades response quality (noise in context). The routing table is a deterministic, human-readable solution to selective context loading.

## Why People Are Using It
Directly actionable: editors can see exactly what context the agent has for a given task. Trivially maintainable: edit a markdown table to add/remove file dependencies. Interpretable: a non-technical stakeholder can review what information the agent uses for each task type.

## Potential Alternatives
Vector embedding retrieval (semantic search over files), hardcoded file lists in system prompts, agent self-directed file discovery, MCP-based resource fetching.

## Potential Improvements
Dynamic routing based on task analysis: the agent reads the routing table but also proposes additions when it encounters a task type not covered.

## Potential Failure Modes
Routing table becomes stale as workspace evolves (files referenced in table no longer exist or have been renamed). Task ambiguity: a task that spans multiple rows creates confusion about which context to load.

## Extraction Note — 2026-04-26
Extracted as **template**: [[task-to-file-routing-table-in-context-files]] in `extracts/templates/`
