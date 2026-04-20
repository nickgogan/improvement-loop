---
name: Eval-Driven Tool Iteration Loop
summary: Run structured evaluations on tools using real-world tasks, then feed evaluation transcripts to Claude to refactor the tools — creating a systematic improvement loop. Slack MCP tools outperformed
  human-written baselines after agent-driven refactoring.
implementation_notes: Could apply to MetaSystem's MCP tool definitions and skill procedures. Run evals, read transcripts, let Claude suggest tool improvements.
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- Improvement Loop
adopted_in: []
sources:
- anthropic-writing-effective-tools-for-agents.md
related_findings:
- file: eval-driven-development-autonomous-quality.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-19'
pipeline_status: extracted
consumed_by:
- skills/eval-driven-tool-iteration-loop.md
---

## What It Is

A three-phase process: (1) Build prototype tools, test locally. (2) Run evaluations with realistic multi-step tasks tracking accuracy, runtime, tool calls, tokens, errors. (3) Concatenate transcripts, feed to Claude Code for tool refactoring. Use held-out test sets to prevent overfitting.

## Why It Matters

Human intuition about what makes a good tool diverges from what actually helps agents. Eval transcripts reveal patterns humans miss — unexpected tool-calling sequences, workflow consolidation opportunities. This closes the feedback loop between tool design and agent performance with empirical evidence.

## Why People Are Using It

Anthropic's internal process. Slack MCP tools improved beyond human-written baselines after Claude-driven optimization.

## Potential Improvements

Continuous integration — run tool evals on every tool change. Automated transcript pattern detection without human review.

## Potential Failure Modes

Overfitting tools to specific eval tasks. Agent may optimize for eval-specific shortcuts rather than general utility. Need diverse, held-out test sets.

## Extraction Note — 2026-04-19
Extracted as **skill**: [[eval-driven-tool-iteration-loop]] in `extracts/skills/`
