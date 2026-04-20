---
notion_id: 32b1e08b-9b34-818a-8457-c4fc1fb0b2e4
name: Bidirectional Prompting for Spec Creation
summary: Before implementation, alternate questions between you and Claude until both share an identical mental model of the plan — Claude's questions surface implicit assumptions that would have been silent
  bugs; your questions validate edge cases.
implementation_notes: null
category: Prompt Craft
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: advanced-elicitation-techniques-library.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Bidirectional Prompting for Spec Creation

## What It Is
Instead of dumping a spec and immediately starting implementation, bidirectional prompting is an iterative Q&A phase in plan mode. The user dumps their thoughts, Claude asks targeted clarifying questions that surface implicit assumptions it would otherwise silently fill in from training data. The user then asks counter-questions to verify Claude correctly understands edge cases and architecture constraints. Only when both parties have no more questions does implementation begin. The resulting spec and implementation plan (with checkbox bullet points per task) is then signed off by the human line by line.

## Why It Matters
Implicit assumptions injected from training data are the root cause of most cascading bugs in long agentic runs. When the human is not in the loop for the implementation (as in Ralph loops), pre-aligning every assumption is critical — there is no opportunity to course-correct mid-implementation.

## Why People Are Using It
Most developers skim the plan after a few back-and-forth exchanges and jump to implementation. Bidirectional prompting is a discipline upgrade that pays dividends proportional to project complexity.

## Potential Alternatives
Writing specs manually without LLM assistance. Using structured prompt templates that enumerate all required spec fields. Architecture diagrams as supplementary alignment tools.

## Potential Improvements
Tooling that automatically flags unchecked assumptions in a spec (e.g., LLM-as-critic reviewing the plan for gaps) before implementation begins.

## Potential Failure Modes
If the spec is written in plan mode but the implementation plan exceeds 30k tokens, the model cannot hold it in context during implementation — the spec must be decomposed into sub-plans. Bidirectional prompting takes significantly longer than just starting to build, which creates adoption friction.
