---
name: Surgical Change Constraint — Agents Must Touch Only What Was Asked
summary: 'A CLAUDE.md rule encoding the principle that agents should make the minimum diff required: no refactoring unrelated code, no removing comments, no reorganizing structure outside the task scope.
  Prevents the ''productivity theater'' failure mode where agents look helpful but silently degrade codebases.'
implementation_notes: null
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General / Cross-System
adopted_in: []
sources:
- karpathy-skills-claudemd-four-principles.md
related_findings:
- file: agent-clarification-over-assumption-pattern.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: bmad-outcome-based-skill-rewrite-pattern.md
  rel: same-problem
- file: seven-rung-minimal-code-decision-ladder.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-20'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- rules/surgical-change-agent-scope.md
- model-resilient-prompt-engineering.md
---

## What It Is

A behavioral constraint encoded in CLAUDE.md: agents must apply changes only to the exact scope of the task, leaving all unrelated code — comments, formatting, structure, import ordering — untouched. Derived from Karpathy's observation that agents "still sometimes change or remove comments in code that they don't like or don't sufficiently understand, even if it is orthogonal to the task at hand."

The rule targets a specific failure mode called "productivity theater": the agent produces more lines of code than requested, appears to have done more work, and may even confirm success — but the extra changes introduce drift, break unrelated behavior, or erode codebase coherence. Because the extra work looks helpful, users often don't notice until later.

Concrete example from Karpathy Skills demo: a font-family replacement task. Surgical agent: found every instance of the old font, replaced it, left Google Fonts URL structure and all surrounding declarations intact. Non-surgical agent: burned tokens attempting multiple passes, confirmed success, but the font was unchanged in the running application.

## Why It Matters

Unrequested changes are a token tax and a trust erosion problem. Each unsolicited modification:
1. Consumes additional tokens (more code generated, more reasoning cycles)
2. Introduces unreviewed changes the human did not approve
3. Can mask the actual task outcome — if the agent changes 10 things when asked to change 1, the human must diff all 10 to verify the intent
4. Compounds across sessions into "diff sprawl" where the codebase diverges from its intended architecture

The surgical constraint is the complement to the simplicity constraint: simplicity governs how much new code is written; surgical governs how much existing code is touched.

## Why People Are Using It

Karpathy Skills CLAUDE.md (43K GitHub stars in one week) encodes this as Principle 3. Karpathy's original tweet framing it as one of the most common agent failure categories gives it strong provenance. Practitioners building on real codebases have experienced this as a recurring frustration — agents that "improve" things while breaking others.

## Potential Improvements

Could be combined with a pre-task scope declaration step: agent states the exact files and line ranges it plans to modify before executing, human approves scope, then agent executes within that scope. This turns surgical constraint from a behavioral nudge into a verifiable contract.

## Potential Failure Modes

Over-constraining to surgical changes can prevent the agent from making necessary refactors when a feature genuinely requires restructuring adjacent code. The rule works best when tasks are well-scoped; ambiguous tasks may require scope negotiation before the surgical constraint applies. Agents may still make "invisible" changes (e.g., normalizing whitespace, reordering dict keys) that pass surgical inspection but pollute diffs.

## Extraction Note — 2026-04-20
Extracted as **rule**: [[surgical-change-agent-scope]] in `extracts/rules/`
