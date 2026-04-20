---
notion_id: 32b1e08b-9b34-815e-b4b7-cbe59e53b3f8
name: 'LLM Intuition: ''You Are Absolutely Right'' as Reliability Collapse Signal'
summary: Seeing 'you are absolutely right' appear more than once in a session's reasoning trace is a reliable early warning signal that the model is entering a sycophantic loop and output quality is collapsing
  — cut your losses and restart.
implementation_notes: null
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- your-ai-coding-is-bad-heres-how-to-fix-it.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: agent-self-reporting-unreliability-independent-eval.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# LLM Intuition: 'You Are Absolutely Right' as Reliability Collapse Signal

## What It Is
One of the most actionable model intuition heuristics: when a Claude model uses the phrase 'you are absolutely right' multiple times within a session, it is almost certainly entering a sycophantic/agreement loop where it has lost its own reasoning independence and is validating whatever the user says rather than genuinely reasoning. This is a reliable signal to stop the session, clear context, and restart from a clean state. Similarly, if a model fails to find a bug in its first two debugging passes, continuing to prompt it to look harder will not produce results without significant context intervention.

## Why It Matters
Sycophantic loops waste tokens, produce false confidence, and generate plausible-sounding but incorrect outputs. Catching this early prevents chasing phantom bugs for hours.

## Why People Are Using It
A simple, memorable heuristic that requires no tooling — just attention to the model's language patterns during monitoring.

## Potential Alternatives
Automated sentiment/sycophancy detection in model outputs. Regular session reviews with the model asked to critique its own previous outputs.

## Potential Improvements
Claude Code hooks that flag repeated sycophantic phrases and prompt the developer to restart. Automated session health scoring based on language patterns.

## Potential Failure Modes
False positives: models may legitimately agree with a correct assessment. Context is needed — one instance is normal, multiple instances in succession is the signal.
