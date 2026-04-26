---
name: 'Progressive Search: Wide Then Narrow'
summary: Prompt agents to start with short, broad search queries, evaluate information availability, then narrow. Counters the default LLM behavior of generating overly specific queries that yield few results.
  Mimics expert human research strategy.
implementation_notes: Applicable to MetaSystem's research-loop and any agent that uses web search tools.
category: Prompt Craft
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-multi-agent-research-system.md
related_findings: []
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: extracted
consumed_by: ["patterns/progressive-search-wide-then-narrow.md"]
---

## What It Is

A search strategy heuristic embedded in agent prompts. Instead of generating long, specific search queries (the default LLM behavior), agents are instructed to: (1) start with short, broad queries to assess information availability, (2) evaluate which sources exist and what formats are available, (3) progressively narrow queries based on what was found. This mirrors how expert human researchers operate -- broad scan first, then targeted deep dives.

## Why It Matters

LLMs default to generating verbose, highly specific search queries that often return zero results or miss relevant sources. This is especially problematic for research tasks where the information landscape is unknown. Starting wide ensures the agent discovers the actual information topology before committing to specific search paths.

## Why People Are Using It

Anthropic's production multi-agent research system. Combined with parallel tool calling (3+ tools per subagent, 3-5 subagents per query), the progressive search strategy cuts complex query resolution time by up to 90%.

## Potential Improvements

Automated breadth-to-depth transition based on result quality signals. Source type preferences (prefer primary sources over secondary, PDFs/blogs over SEO farms).

## Potential Failure Modes

Broad queries may return overwhelming volumes of irrelevant results. The transition from broad to narrow requires judgment that the agent may not have for unfamiliar domains. Too many broad queries consume the search budget before targeted queries begin.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[progressive-search-wide-then-narrow.md]] in `extracts/patterns/`
