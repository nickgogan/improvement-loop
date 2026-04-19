---
name: Non-Deterministic Tool Contract Model
summary: Tools for agents represent a fundamentally different contract than traditional APIs — the agent chooses whether to use a tool and how to interpret its response, requiring design for persuasion
  rather than specification.
implementation_notes: Reframes MetaSystem's tool/skill design philosophy. Tool descriptions should make the right tool the obvious choice, not just the available one.
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General / Cross-System
adopted_in: []
sources:
- anthropic-writing-effective-tools-for-agents.md
related_findings: []
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- designing-agent-tools.md
---

## What It Is
Unlike function calls in deterministic code where the caller must invoke and handle the return, agent tools operate under a non-deterministic contract. The agent decides whether to call a tool at all, which tool to call, what parameters to pass, and how to interpret the response. Tool design must make the right tool the obvious choice — closer to UX design than API design.

## Why It Matters
Designing tools as if agents will always use them correctly leads to tools that work in demos but fail in production. The non-deterministic contract means tool designers must think about discoverability, disambiguation, and response interpretability. This reframing is the prerequisite for all other tool design principles.

## Why People Are Using It
Anthropic positions this as the foundational insight behind their tool design methodology. It explains why SWE-bench performance improved more from tool description quality than from prompt engineering.

## Potential Improvements
Formal tool selection metrics (was the right tool chosen?) as a first-class eval dimension separate from task completion.

## Potential Failure Modes
Over-designing for "persuasion" could lead to verbose tool descriptions that consume context. Need to balance clarity with conciseness.
