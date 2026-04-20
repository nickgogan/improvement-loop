---
notion_id: 3311e08b-9b34-8133-9a46-dc48016bab5e
name: 'Thinking Models: Mental Framework Commands for Coding Agents'
summary: TACHES implements 12 slash commands (/consider:*) that apply mental models -- Pareto, first principles, inversion, second-order effects, 5 whys, Occam's razor, SWOT, Eisenhower matrix, and others
  -- as structured reasoning frameworks within Claude Code sessions, making cognitive tools invocable on demand.
implementation_notes: Directly applicable to Perplexity skill design -- could port mental model slash commands as reasoning patterns within research-loop, research-proposer, or brainstorming phases. Design
  work needed to determine which models are most valuable and how to integrate without adding overhead.
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- Perplexity Skills
adopted_in: []
sources:
- taches-claude-code-resources-commands-skills-thinki.md
proposals: []
date_discovered: '2026-03-28'
last_updated: 2026-04-08
related_findings:
- file: advanced-elicitation-techniques-library.md
  rel: same-problem
pipeline_status: extracted
consumed_by:
- skills/thinking-models-mental-framework-commands.md
---
# Thinking Models: Mental Framework Commands for Coding Agents

## What It Is
A set of 12 slash commands in the /consider:* namespace, each invoking a specific mental model for structured reasoning: pareto, first-principles, inversion, second-order, 5-whys, occams-razor, one-thing, swot, eisenhower-matrix, 10-10-10, opportunity-cost, and via-negativa.

## Why It Matters
Coding agents typically operate in a single reasoning mode. Mental models force the agent to examine problems from different angles before committing to a solution.

## Why People Are Using It
TACHES packages them as zero-friction slash commands. Each model has its own .md file with structured instructions.

## Potential Alternatives
Manual prompting, chain-of-thought in system prompts, dedicated reasoning MCP servers, custom CLAUDE.md sections.

## Potential Improvements
Composable chains -- applying multiple models in sequence. Context-aware model suggestions.

## Potential Failure Modes
Overhead if applied indiscriminately. Risk of cargo-culting where the framework is followed mechanically.

## Extraction Note — 2026-04-19
Extracted as **skill**: [[thinking-models-mental-framework-commands]] in `extracts/skills/`
