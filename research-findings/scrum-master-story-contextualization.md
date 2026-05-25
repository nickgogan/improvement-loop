---
name: Scrum Master as Context Curator for Dev Agent Stories
summary: The Scrum Master agent reads architecture docs, tech stack, and prior stories to produce self-contained developer story files that embed all needed context -- so the dev agent never searches for
  information, reducing token waste and context drift.
implementation_notes: MetaSystem's skill files partially implement this -- each skill is self-contained. The explicit pattern of a curator agent reading multiple sources and producing a context-complete
  handoff file could improve how tasks are dispatched to sub-agents.
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- bmad-method-masterclass.md
date_discovered: '2026-04-07'
last_updated: 2026-04-08
related_findings:
- file: bmad-method-v6-multi-agent-sdlc.md
  rel: enabled-by
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- structuring-agent-context.md
---
## What It Is

In the BMad Method, the Scrum Master agent sits between planning (PM/Architect) and execution (Developer). Its core function is **context curation**: reading the epic, architecture docs, coding standards, tech stack, source tree, and any prior story notes, then producing a self-contained developer story file that embeds exactly the context the dev agent needs.

Key implementation details:
- The dev agent has a `dev-load-always-files` config listing files it reads on every execution (coding-standards.md, tech-stack.md, source-tree.md)
- The Scrum Master embeds additional story-specific context (relevant architecture sections, data models, directory structure) directly into the story file
- Stories carry forward notes from previous stories when dependencies exist
- Stories include acceptance criteria, step-by-step implementation tasks, and placeholder sections for dev and QA notes
- Stories start in `draft` status and must be manually set to `approved` before the dev agent will execute them

Brian frames this as "the core of context engineering -- giving the agent exactly what it needs to build its little piece of the kingdom."

## Why It Matters

Without context curation, dev agents waste tokens searching for information, load irrelevant context, or hallucinate implementation details. The Scrum Master pattern ensures the dev agent starts with a focused, complete context window -- no searching, no guessing.

## Why People Are Using It

The pattern produces measurably better dev agent output because the context window contains only relevant information. Combined with document sharding, it keeps token usage minimal while maintaining implementation accuracy.

## Potential Improvements

Automated context relevance scoring to help the Scrum Master select only the most pertinent architecture sections. Dynamic story complexity estimation to adjust context depth.

## Potential Failure Modes

The Scrum Master may include too much or too little context. If architecture docs change after story creation, the embedded context becomes stale. The two-agent overhead (SM + Dev) may be unnecessary for trivial stories.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[scrum-master-story-contextualization.md]] in `extracts/patterns/`
