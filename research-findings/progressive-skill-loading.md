---
name: Progressive Skill Loading
summary: Skill descriptions (~50 tokens each) injected at boot as XML elements. Full SKILL.md content (~500-2000 tokens) loaded on-demand when agent calls read_file. Prevents context bloat from 16+ skills
  while maintaining discoverability.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: gpt-54-tool-search-deferred-tool-loading.md
  rel: same-problem
- file: mcp-as-code-api-progressive-tool-discovery.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: document-sharding-for-context-efficiency.md
  rel: same-problem
- file: dynamic-tool-pool-assembly-transcript-compaction.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
---

## What It Is

A two-phase skill loading pattern: at boot time, all enabled skills are scanned and only their `name` + `description` fields (~50 tokens each) are injected into the system prompt as `<skill>` XML elements. The agent knows what skills exist and what they do but doesn't have the full workflow. When a task matches a skill, the agent calls `read_file` on the SKILL.md path to load the full workflow (~500-2000 tokens). A background thread warms the skill cache at startup.

## Why It Matters

The existing KB covers deferred tool loading (Claude Code's tool-search pattern) and progressive tool discovery (MCP). This pattern applies the same concept at the skill level — skills are higher-level than tools (they contain multi-step workflows, references, templates) and therefore more expensive to load. With 16+ skills, bulk loading would consume 8-32k tokens of context before the first user message. Progressive loading keeps boot context minimal.

## Why People Are Using It

Observed in [DeerFlow](https://github.com/bytedance/deer-flow) v2.0 — see [[deer-flow-analysis]] for structural details. DeerFlow scans `skills/public/*/SKILL.md` at startup, extracts YAML frontmatter, and injects `<skill>` elements. The agent must explicitly call `read_file` to access full skill content. MetaSystem's skill system already does this partially — skill descriptions are in CLAUDE.md tables, full content loaded on invocation.

## Potential Alternatives

- Bulk loading all skills into system prompt (simple but wasteful)
- Skill search/discovery tool (agent queries for relevant skills by keyword)
- No skill catalogue (agent discovers skills only when user invokes them)

## Potential Improvements

Could add skill relevance scoring — the agent sees a ranked subset of skill descriptions based on the current conversation topic, not all skills.

## Potential Failure Modes

- Agent may not recognize when a skill is relevant if the description is too terse
- `read_file` adds a tool-call round trip before skill execution begins
- Background cache warming adds startup latency
