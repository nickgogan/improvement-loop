---
notion_id: 32b1e08b-9b34-816f-ae96-dab636759387
name: Spec-as-Source-of-Truth for Agent Construction
summary: For agentic builds, the spec file is the complete implementation artifact — a single markdown file that covers all four zones, environmental configuration, and behavioral instructions, from which
  the entire agent can be recreated at any time.
implementation_notes: null
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources: []
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: acceptance-criteria-as-verifiable-eval-anchor.md
  rel: same-problem
- file: task-contract-pattern-schema-first-agent.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Spec-as-Source-of-Truth for Agent Construction

## What It Is
When building a `claude -p` agent, Roman writes a full spec.md that covers: agent purpose and identity, trigger mechanism (Telegram listener + cron schedule), context zone (system prompt file path and content summary), tools zone (allowed tools and scripts), output zone (session persistence approach and reset mechanism), environmental variables required, directory structure, safety constraints (allowed user IDs), model selection, and implementation instructions. This spec is passed to Claude Code to build the agent. Because it covers everything, the agent can be fully recreated from the spec alone — making it an effective version-control artifact and a handoff document.

## Why It Matters
In agentic coding, specs serve as the long-term memory of what was built. A spec-as-source-of-truth approach means no agent is a one-time artifact — all agents are reproducible, auditable, and modifiable.

## Why People Are Using It
Separates the design decision (what the agent does) from the implementation (how it does it), reducing cognitive load during builds and simplifying debugging.

## Potential Alternatives
README-as-documentation (post-hoc, often incomplete). Agent framework configuration files (e.g., LangChain YAML). Storing implementation in the agent script itself without a separate spec.

## Potential Improvements
A structured spec template with mandatory fields for all four zones. Version control diffs on specs as a change log for agent behavior.

## Potential Failure Modes
Spec drift: the agent implementation diverges from the spec over time if the spec is not kept updated. Specs that are too high-level leave ambiguous implementation decisions.
