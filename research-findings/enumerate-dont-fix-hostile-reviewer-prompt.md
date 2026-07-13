---
name: Enumerate-Don't-Fix Hostile-Reviewer Prompt (Task Flip as Reliability Mechanism)
summary: 'Plain English: a model catches many of its own class of mistakes if you flip its task

  from "generate/fix" to "only enumerate problems" — the reviewer must be forbidden from

  fixing anything. The prompt: read the deck/workbook as a skeptical reviewer who suspects

  every claim and number; for each slide/sheet identify claims without source attribution,

  numbers without a data source, charts whose underlying data isn''t traceable, formulas

  inconsistent across parallel rows/columns, and assumptions presented as facts; produce a

  written list of every issue found; "don''t fix anything, just enumerate." The task flip is

  the mechanism: finding problems and solving them are different tasks with different

  outputs, and mixing them lets the fix impulse paper over the audit. Human review then

  concentrates on the consequential claims — the numbers that travel.'
implementation_notes: 'P2: direct prompt-craft enrichment candidate for the engine''s /assess-* skills and any

  verifier subagent — their report-only, findings-not-fixes posture is this pattern; the

  delta worth importing is the explicit five-category enumeration checklist and the

  verbatim "don''t fix anything, just enumerate" terminal instruction as a contract line.'
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: P2 (Design Required)
applicability:
- IL (assess-* skills, verifier prompts)
- General
adopted_in:
- Improvement Loop
sources:
- i-built-a-deck-with-ai-then-made-a-second-ai-attack-it.md
related_findings:
- file: generator-assessor-separation-in-skill-iteration.md
  rel: extends
- file: llm-as-judge-pattern-for-verification-agents.md
  rel: same-problem
- file: meta-prompting-separating-analysis-from-execution.md
  rel: same-problem
- file: cross-vendor-adversarial-build-attack-loop.md
  rel: enables
- file: controller-deauthorization-reviewer-independence.md
  rel: same-problem
- file: review-triage-admissible-scope-authority.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-13'
pipeline_status: raw
---

# Enumerate-Don't-Fix Hostile-Reviewer Prompt

## What It Is

A verification prompt pattern with two load-bearing parts. **The hostile stance:** the
reviewer "suspects every claim and every number" and works a concrete checklist —
unattributed claims, sourceless numbers, untraceable chart data, formulas inconsistent
across parallel rows/columns, assumptions dressed as facts. **The task flip:** the
reviewer's only permitted output is a written enumeration of issues. "That last
instruction — don't fix, just enumerate — is what makes it work. The model is just trying
to find the problems, not solve them. Different task, different output, different value.
A model can catch a lot of its own mistakes when you flip the task from generation to
enumeration." The source notes it works even with the same model reviewing its own output,
though the author prefers cross-vendor pairing.

## Why It Matters

It isolates *why* generator-assessor separation works and shows the cheapest possible
version of it: you don't need a second model or even a second context to get a large share
of the benefit — you need a different task. That makes it the entry-level rung under the
KB's separation findings (fresh context > same context; different model > same model; but
task flip is the mechanism all of them share). The failure it targets is the polish trap:
AI-generated office artifacts look finished long before they are correct ("a financial
model in a costume"), and generation-mode review is biased toward completing, not
doubting.

## Why People Are Using It

Applied in the author's production document workflow (the attack loop finding); the
checklist targets the ordinary, quiet failures that survive human skim review — blended
actuals/plan data, formulas copied from the wrong anchor cells.

## Potential Improvements

Domain-specific enumeration checklists (the five categories here are office-file-shaped;
code, specs, and governance docs each need their own). Structured output (issue ID,
location, category, severity) so the fix pass is mechanically consumable.

## Potential Failure Modes

Enumeration without severity ranking buries the two real problems under twenty nitpicks.
The reviewer only finds what the checklist names — novel failure classes need the open
"suspect everything" stance to actually fire. Same-model enumeration still shares the
generator's blind spots (shared training priors); cross-model review reduces but does not
eliminate this.
