---
name: Outcome-Based Skill Rewrite Pattern
summary: Rewriting skill instructions from procedural step-by-step format to outcome-based design, cutting token consumption ~50% while letting the LLM choose its own execution path.
implementation_notes: null
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General / Cross-System
adopted_in: []
sources:
- bmad-v610-v622-changelog.md
related_findings:
- file: skill-as-script-wrapper-for-complex-pipelines.md
  rel: same-problem
- file: context-curation-over-context-stuffing.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: context-curation-over-context-stuffing.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: 2026-04-08
pipeline_status: synthesized
consumed_by:
- model-resilient-prompt-engineering.md
---
# Outcome-Based Skill Rewrite Pattern

## What It Is
A pattern for restructuring skill instructions from procedural step-by-step format ("do step 1, then step 2, then step 3") to outcome-based design ("ensure X is true, ensure Y is complete"). The BMAD Method applied this in v6.2.2 when rewriting the bmad-help skill from an 8-step procedural execution sequence to an outcome-focused design, achieving approximately 50% reduction in instruction length and token consumption. The outcome-based format specifies *what the skill should achieve* rather than *how to achieve it step by step*, allowing the LLM to select its own execution path to satisfy the stated outcomes.

## Why It Matters
Procedural skill instructions consume tokens linearly with complexity — every step, substep, and conditional branch must be spelled out. Outcome-based instructions compress the same intent into fewer tokens because they describe end-state invariants rather than traversal paths. The 50% reduction in bmad-help demonstrates that a significant portion of procedural skill instructions are execution scaffolding that the LLM can reconstruct from outcome specifications alone. This has direct implications for context window budgets in systems that load multiple skills simultaneously.

## Why People Are Using It
The BMAD Method's bmad-help skill was rewritten from 8 procedural steps to an outcome-focused design in v6.2.2. The motivation was token economy — shorter instructions that produce equivalent or better results. Outcome-based design also makes skills more resilient to model upgrades, since the instructions don't encode assumptions about the LLM's specific reasoning strategy. The pattern aligns with the broader trend of treating LLMs as goal-seeking agents rather than script executors.

## Potential Improvements
A hybrid format could preserve outcome-based design for the main flow while retaining procedural guardrails for steps where execution order is genuinely load-bearing (e.g., validation must precede deployment). Metrics beyond token count — such as output quality variance across runs — would strengthen the evidence for when outcome-based rewrites are safe versus when procedural specificity is needed.

## Potential Failure Modes
Outcome-based instructions may underperform when the desired execution path is non-obvious or when the LLM lacks domain knowledge to infer correct sequencing. Skills with strict ordering dependencies (e.g., file creation before file reference) may produce errors if the LLM chooses an incorrect execution order. The 50% token reduction claim is from a single skill rewrite — generalizability across skill types is not yet established.
