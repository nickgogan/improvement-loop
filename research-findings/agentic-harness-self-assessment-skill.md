---
name: Agentic Harness Self-Assessment Skill (Design + Evaluation Modes)
summary: 'A Claude Code skill with two modes: Design Mode (walks through structured design of a new agent harness, recommending primitives and phased implementation) and Evaluation Mode (points at an existing
  harness codebase and identifies missing primitives, ordered by severity). Grounded in the 12-primitive framework from the Claude Code leak.'
implementation_notes: null
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropics-2-5-billion-leak-12-critical-pieces.md
date_discovered: '2026-04-07'
last_updated: 2026-04-08
related_findings:
- file: ace-execution-feedback-no-labels-required.md
  rel: same-problem
pipeline_status: extracted
consumed_by:
- skills/agentic-harness-self-assessment.md
---

## What It Is

Nate B Jones released a Claude Code skill (also ported to OpenAI Codex) that operationalizes the 12-primitive framework from the Claude Code leak into an interactive assessment tool. It has two modes:

**Design Mode:** Describe the agent you want to build (chat assistant, workflow orchestrator, code agent, etc.). The skill walks through a structured design process:
- Recommends a harness architecture shape
- Identifies the minimum useful set of primitives for your use case
- Sequences implementation into phases
- Defines verification criteria
- All before writing any code

**Evaluation Mode:** Point the skill at an existing codebase (CLAUDE.md, architecture docs, etc.). It evaluates every dimension:
- Architecture completeness
- Safety and permissions coverage
- State and durability mechanisms
- Returns findings ordered by severity
- Provides a prioritized upgrade path
- Specifies tests that confirm each fix works

The skill is deliberately opinionated: it biases toward lean, solo-maintainable architecture unless given compelling reasons for complexity. It starts with single-agent design and resists premature multi-agent orchestration. This is intentional because "the most common failure mode in agentic systems is not underengineering -- it is overengineering."

## Why It Matters

The 12-primitive framework is valuable as knowledge but hard to apply systematically. A skill that interactively walks through assessment makes it actionable. The anti-complexity bias addresses a real failure mode: teams building multi-agent coordination before they have working permission systems, or implementing plugin marketplaces before sessions survive crashes.

## Why People Are Using It

Released by Nate B Jones alongside his analysis of the Claude Code leak. Cross-platform (Claude Code + OpenAI Codex) to demonstrate that the primitives are LLM-agnostic.

## Potential Improvements

Could be adapted into a MetaSystem-specific variant that evaluates against MetaSystem's own governance requirements (DD compliance, fractal pattern adherence, human gate enforcement) in addition to the generic primitives.

## Potential Failure Modes

- The skill's recommendations reflect one analyst's interpretation of the Claude Code leak, not Anthropic's official guidance
- Opinionated bias toward simplicity may conflict with legitimately complex multi-agent requirements
- Assessment quality depends on the agent's ability to read and understand the harness codebase accurately

## Extraction Note — 2026-04-19
Extracted as **skill**: [[agentic-harness-self-assessment]] in `extracts/skills/`
