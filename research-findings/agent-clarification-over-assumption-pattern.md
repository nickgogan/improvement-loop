---
name: Agent Clarification Over Assumption Pattern
summary: Agents must distinguish resolvable gaps (can be solved by research or tool use) from intent/preference questions requiring user input — and pause for the latter rather than assuming. Anthropic
  trains this via ambiguity scenarios and constitutional guidance.
implementation_notes: null
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General / Cross-System
adopted_in: []
sources:
- anthropic-trustworthy-agents-in-practice.md
related_findings:
- file: autonomy-gradient-not-binary-delegation.md
  rel: same-problem
- file: trust-calibration-progressive-autonomy-ramp.md
  rel: enables
- file: mcp-elicitation-for-user-input.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- agent-design-patterns.md
---
# Agent Clarification Over Assumption Pattern

## What It Is
A design principle where agents learn to classify gaps in their knowledge into two categories: (1) resolvable gaps that can be filled through research, tool use, or inference, and (2) intent/preference questions that require user input. The agent should autonomously resolve the first category and pause to ask for the second. Anthropic implements this through training scenarios that simulate ambiguity, reinforcing pauses over assumptions. Claude's Constitution explicitly trains models to "raise concerns, seek clarification, or decline" rather than assume user intent.

Key evidence from Anthropic: on complex tasks, user interruptions rise slightly, but Claude's check-in rate doubles. This demonstrates effective calibration — the model asks more questions when stakes are higher, rather than maintaining a flat rate of autonomy.

## Why It Matters
The over-autonomy vs. over-caution tradeoff is the central tension in agent design. An agent that always asks is useless (HITL bottleneck); an agent that never asks is dangerous (assumption-driven errors). The clarification-over-assumption pattern provides the decision framework: pause only when the gap is genuinely about user intent, not when it can be resolved independently.

## Why People Are Using It
Anthropic deploys this in production across Claude.ai, Claude Desktop, and Claude Code. The training approach (ambiguity scenarios + constitutional guidance) demonstrates that this can be embedded in the model rather than enforced purely by harness logic. This is significant because harness-level enforcement (e.g., "always ask before doing X") is brittle and task-specific, while model-level calibration generalizes across contexts.

## Potential Improvements
Could be combined with the autonomy gradient (DD finding) to create a two-dimensional classification: gap type (resolvable vs. intent) x blast radius (low vs. high). Low blast radius + resolvable = full autonomy. High blast radius + intent = mandatory pause. The intermediate combinations require calibrated judgment.

## Potential Failure Modes
The model may misclassify resolvable gaps as intent questions (over-asking) or vice versa (over-assuming). The check-in rate doubling on complex tasks could become annoying if not well-calibrated — users may train the model to stop asking by dismissing questions, degrading the safety signal. Cultural differences in communication style may affect what counts as "ambiguous."
