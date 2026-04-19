---
name: Two-Level Verification (Agent Run + Harness Integrity)
summary: 'Verification must operate at two levels: (1) did a specific agent run produce correct output, and (2) when you modify the agentic harness itself, do all existing guardrails still hold. Level 2
  is a regression test suite for the harness, not the agent''s work.'
implementation_notes: null
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropics-2-5-billion-leak-12-critical-pieces.md
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
related_findings:
- file: agent-type-system-six-roles.md
  rel: enabled-by
- file: ace-execution-feedback-no-labels-required.md
  rel: same-problem
- file: builder-validator-chain-pattern.md
  rel: same-problem
- file: cross-model-verification-for-bug-finding.md
  rel: same-problem
pipeline_status: "synthesized"
consumed_by:
  - "building-agent-evaluation-suites.md"
---
## What It Is

Nate B Jones identifies two distinct verification levels in the Claude Code leak, only one of which is commonly discussed:

**Level 1 (Agent Run Verification):** Did the agent complete its task correctly? This is the well-known pattern -- a verification step checks the work product. The existing "Verification Agent: Seven Prompt Patterns" finding covers this level thoroughly.

**Level 2 (Harness Integrity Verification):** When you change the agentic harness (CLAUDE.md, hooks, skills, rules, settings.json), does the agent still behave correctly against known guardrails? This is a regression test suite for the harness itself, not for any specific agent run.

Example Level 2 checks:
- Do destructive tools still require approval after this CLAUDE.md change?
- When tokens run out, does the agent gracefully stop or hard crash?
- Are permission boundaries still enforced after adding a new skill?
- Does the session persistence mechanism still work after updating hooks?

The key insight: **the harness evolves over time**, and each evolution can silently break previously working safety properties. Level 2 verification catches these regressions.

## Why It Matters

Most teams think about verification as "did the agent do the right thing?" They rarely think about "did my change to the agent's configuration break something?" This is especially dangerous because harness changes affect every subsequent agent run, not just one. A broken permission boundary or disabled safety check propagates silently until it causes a visible failure.

MetaSystem modifies CLAUDE.md, rules, skills, and hooks regularly. Without Level 2 verification, each change is a potential regression that only surfaces when something goes wrong.

## Why People Are Using It

Anthropic's production Claude Code system. Nate B Jones frames this as one of the 12 critical primitives, noting it is "the second level of verification in a harness that we don't think about a lot because you have to provide for the harness evolving."

## Potential Improvements

A standard suite of harness smoke tests could be defined as a skill or hook that runs automatically after any modification to CLAUDE.md, settings.json, or skill files. Tests would verify: permission enforcement, token budget compliance, graceful degradation, and safety constraint preservation.

## Potential Failure Modes

- Over-testing: running extensive verification on every minor CLAUDE.md edit creates friction
- False security: passing smoke tests does not guarantee the harness works for all edge cases
- Maintenance burden: as the harness grows, the verification suite must grow with it

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[two-level-verification-agent-run-plus-harness-integrity.md]] in `extracts/patterns/`
