---
notion_id: 32b1e08b-9b34-8142-9904-c453264a9b64
name: Four-Zone Agent Architecture Framework
summary: 'Every agent — regardless of tool — is composed of four zones: trigger (what wakes it), context (what is injected per turn), tools (what it can interact with), and output/memory (where work goes
  and how state persists). This decomposition makes any agent debuggable and rebuildy from a spec.'
implementation_notes: null
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- building-ai-agents-that-actually-work-full-course.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: agent-architecture-layer-impermanence.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Four-Zone Agent Architecture Framework

## What It Is
Roman frames all agentic systems using four zones: (1) Trigger — the event that initiates the agent (cron job, Telegram message, heartbeat, API call); without a trigger, the agent never runs. (2) Context — everything injected into the model's context window on each turn: system prompt, CLAUDE.md, conversation history, retrieved files. (3) Tools — the capabilities that let the LLM read/write/interact with external systems: bash, MCP servers, Gmail API, browser. Tools are activated by specific token sequences in model output. (4) Output/Memory — where work persists between turns (files on disk, session state, database). The model has no persistent memory by default; all statefulness must be explicitly designed into Zone 4. Using `claude -p` in Claude Code, all four zones can be controlled programmatically in a few lines of bash.

## Why It Matters
This framework turns any black-box agent system into a glass box. Debugging is systematic — a broken agent has a broken zone. Spec-driven development using this framework allows rebuilding any agent from scratch in minutes. It also exposes why tools like OpenClaw are frustrating: they obscure all four zones from the developer.

## Why People Are Using It
The four-zone model is an intuitive taxonomy that transfers across all agent platforms. It gives practitioners a mental model for designing novel agents from first principles rather than copying templates.

## Potential Alternatives
Agent frameworks like LangChain, CrewAI, AutoGen have their own abstractions — but these hide the four zones rather than exposing them. Anthropic's reference architectures express similar ideas but with different terminology.

## Potential Improvements
A formal spec template that covers all four zones per agent would make the architecture reproducible. Monitoring tools that visualize live state per zone would aid debugging.

## Potential Failure Modes
Zone 2 (context) is the most common failure point: too much context causes rot, too little causes the agent to be underinformed. Zone 4 (output/memory) failures cause agents to lose state across turns if not explicitly designed.
