---
name: Builder-Validator Chain Pattern
summary: A two-sub-agent pattern where one agent builds an artifact and a second agent independently reviews it, with results funneled through the main orchestrator. Provides built-in quality checks without
  human review, leveraging the hub-and-spoke sub-agent topology.
implementation_notes: null
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in:
- S3 (Claude Code Build)
sources:
- five-agentic-patterns-claude-code.md
- anthropic-harness-design-long-running-apps.md
- anthropic-effective-harnesses-long-running-agents.md
- anthropic-multi-agent-research-system.md
related_findings:
- file: agent-self-reporting-unreliability-independent-eval.md
  rel: same-problem
- file: claude-code-skills-20-four-mode-skill-lifecycle-wi.md
  rel: same-problem
- file: context-pollution-same-window-verification-bias.md
  rel: same-problem
- file: cross-model-verification-for-bug-finding.md
  rel: same-problem
- file: goal-backward-verification.md
  rel: same-problem
- file: gstack-review-army-parallel-specialist-dispatch.md
  rel: same-problem
- file: independent-eval-and-scoped-authority-commandments.md
  rel: same-problem
- file: iterative-refinement-loop-with-quality-gate.md
  rel: same-problem
- file: llm-as-judge-pattern-for-verification-agents.md
  rel: same-problem
- file: qa-agent-independent-compliance-review.md
  rel: extended-by
- file: test-driven-development-as-counterweight-to-agenti.md
  rel: same-problem
- file: two-level-verification-agent-run-plus-harness-inte.md
  rel: same-problem
- file: two-stage-sequential-review.md
  rel: extended-by
- file: ultra-review-multi-agent-bug-hunting-fleet.md
  rel: extended-by
- file: verification-agent-seven-prompt-patterns.md
  rel: same-problem
- file: controller-deauthorization-reviewer-independence.md
  rel: enables
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-07-13'
pipeline_status: synthesized
consumed_by:
  - "building-agent-evaluation-suites.md"
---

## What It Is
Within Claude Code's sub-agent architecture (hub-and-spoke, max 10 concurrent), a builder sub-agent creates an artifact (code, plan, document), then the main agent passes the result to a validator sub-agent for independent review. The validator has its own fresh context, reducing confirmation bias. Since sub-agents cannot communicate directly, the main agent acts as coordinator, relaying the builder's output to the validator.

## Why It Matters
This is the simplest implementation of the "two-level verification" pattern — independent creation and review without requiring human intervention at every step. It catches errors that the builder's context might have normalized.

## Why People Are Using It
Practitioners use this within single Claude Code sessions for code generation + review, document drafting + fact-checking, and plan creation + feasibility assessment. It's a natural application of the sub-agent topology.

## Potential Improvements
- N-of-M validation (multiple validators, majority vote)
- Cross-model validation (different model for validator than builder)
- Specialized validator personas (security reviewer, performance auditor)

## Potential Failure Modes
- Both sub-agents share the same model, so systematic model biases are not caught
- Token cost doubles (build + validate)
- The main agent may not faithfully relay all builder context to the validator
