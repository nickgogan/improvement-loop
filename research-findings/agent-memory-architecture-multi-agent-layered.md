---
notion_id: 32b1e08b-9b34-8101-a3ec-cbb1833f2fdc
name: Agent Memory Architecture (Multi-Agent, Layered)
summary: 'Production multi-agent systems communicate through shared memory layers rather than direct message passing. Key layers: working (PROGRESS.md), episodic (agent-log/), semantic (reference/), procedural
  (skills/). Governance logging should be designed in from day one.'
implementation_notes: null
category: Memory Architecture
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in:
- S3 (Claude Code Build)
sources:
- march-18-agent-memory-architecture-research.md
proposals: null
date_discovered: '2026-03-18'
last_updated: 2026-04-08
related_findings:
- file: memory-cross-layer-promotion-governance.md
  rel: enables
- file: biomimetic-memory-auto-recall-over-tool-based.md
  rel: same-problem
- file: claude-code-hooks-for-automatic-session-memory.md
  rel: same-problem
- file: claude-code-long-term-memory-via-pre-prompt-recall.md
  rel: same-problem
- file: compounding-knowledge-loop-internal-data.md
  rel: same-problem
- file: context-file-taxonomy-claudemd-soulmd-agentsmd.md
  rel: same-problem
- file: four-layer-enterprise-memory-stack.md
  rel: same-problem
- file: memory-bank-isolation-per-agent-per-project.md
  rel: same-problem
- file: memorymd-cross-session-preference-persistence.md
  rel: same-problem
- file: structured-fact-extraction-from-conversations.md
  rel: same-problem
- file: ace-agentic-context-engineering-rag-based.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Agent Memory Architecture (Multi-Agent, Layered)

## What It Is
An architecture pattern for multi-agent systems where agents share context through structured memory layers instead of passing messages directly to each other. The four layers are: working memory (PROGRESS.md — current task state), episodic memory (agent-log/ — history of past runs), semantic memory (reference/ — durable knowledge), and procedural memory (skills/ — reusable capabilities). Governance logging tracks all agent actions from the start.

## Why It Matters
Direct message passing between agents creates tight coupling and makes it hard to audit what each agent knew and when. Shared layered memory decouples agents, makes state inspectable, and enables governance — you can reconstruct what happened by reading the logs rather than replaying message chains.

## Why People Are Using It
Documented in LangGraph and CrewAI implementations. The Household OS vault structure already maps to these four layers. Directly informs how CPO, CTO, and specialized agents share context without stepping on each other.

## Potential Improvements
Could add a governance log database in Notion that tracks all agent actions with timestamps, agent identity, and outcome — making the episodic layer queryable across runs, not just readable as flat files.

## Potential Failure Modes
Shared memory without access control allows one agent's noise to pollute another agent's context. A misbehaving or poorly scoped agent writing to shared memory can corrupt the working state for all other agents in the system.
