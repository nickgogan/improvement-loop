---
name: Hook-Based Enforcement for Agent Outputs
summary: Archon's triage agent uses hooks.PostToolUse with a prompt-based hook that validates whether label application commands include exactly one type, effort, priority label plus area labels. This is
  enforcement-by-hook — the hook runs after every Bash tool call and can reject invalid operations before they take effect.
implementation_notes: null
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources: []
related_findings:
- file: policy-guarded-tool-execution.md
  rel: same-problem
- file: ide-first-claude-code-with-deterministic-hooks.md
  rel: extends
- file: post-session-hooks-autonomous-version-control.md
  rel: same-problem
- file: two-level-verification-agent-run-plus-harness-inte.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-19'
pipeline_status: synthesized
consumed_by:
- rules/hook-based-enforcement-for-agent-outputs.md
- building-agent-evaluation-suites.md
---

## What It Is

Archon's triage agent defines a `PostToolUse` hook in its agent frontmatter that fires after every Bash tool call. The hook uses a prompt-based validator that checks whether GitHub label application commands include exactly one label from each required category (type, effort, priority) plus appropriate area labels. If the validation fails, the hook rejects the operation and the agent must correct its output before proceeding.

This is **enforcement-by-hook** — a pattern where the harness (not the agent, not the user) validates agent outputs against structural rules in real-time. The agent's instructions say "apply one of each label type," but the hook enforces it. The distinction matters: instructions are suggestions that agents can ignore under pressure or context drift; hooks are hard gates.

## Why It Matters

Agent instructions (in CLAUDE.md, agent definitions, or system prompts) are soft constraints — the agent can misinterpret, forget, or override them, especially in long contexts. Hooks provide hard enforcement at the tool-call boundary, catching violations before they reach external systems (GitHub, databases, APIs).

This pattern is particularly valuable for agent outputs that modify shared state. A mislabeled GitHub issue is annoying; a mislabeled production incident ticket could delay response. Hook-based enforcement ensures structural correctness regardless of how well the agent follows its instructions.

## Why People Are Using It

Observed in [Archon](https://github.com/coleam00/archon) v0.3.2 — see [[archon-analysis]] for structural details. The triage agent's `PostToolUse` hook is defined in the agent's frontmatter alongside `name`, `description`, `model`, and `tools`. This makes enforcement a configurable property of the agent definition, not a hardcoded behavior in the execution engine.

## Potential Alternatives

Pre-tool-use hooks that validate inputs before execution (prevents rather than catches). Post-execution verification in a separate review step (catches but slower). Structured output schemas that constrain the agent's output format (prevents at the prompt level).

## Potential Improvements

A library of reusable hook validators (label validation, file path validation, API parameter validation). Hook composition — multiple validators per tool call. Hook metrics — tracking how often hooks reject agent outputs to identify prompt quality issues.

## Potential Failure Modes

Overly strict hooks that block valid agent actions. Hook validation that doesn't cover all invalid states (partial enforcement is sometimes worse than none). Performance overhead from running prompts on every tool call.

## Extraction Note — 2026-05-25
Extracted as **rule**: [[hook-based-enforcement-for-agent-outputs]] in `extracts/rules/`
