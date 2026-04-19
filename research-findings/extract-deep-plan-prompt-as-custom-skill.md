---
name: Extract Deep Plan Prompt as Custom Skill (Ultra Plan Bypass)
summary: Extract Claude Code's deep plan system prompt (multi-agent with critique pass) and use it directly as a custom skill. Bypasses server-controlled A/B randomization, guarantees the critique-pass
  variant every time, and works offline.
implementation_notes: Obtain the deep plan prompt from Ray Amjad's analysis. Create a MetaSystem skill that implements the 4-agent planning pipeline (planner, critic, refiner, finalizer).
category: Prompt Craft
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- anthropic-just-dropped-ultra-plan.md
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
related_findings:
- file: claude-code-ultra-plan-three-mode-planning.md
  rel: enabled-by
pipeline_status: synthesized
consumed_by:
- model-resilient-prompt-engineering.md
- skills/deep-plan-four-agent-pipeline.md
---
# Extract Deep Plan Prompt as Custom Skill (Ultra Plan Bypass)

## What It Is
Ray Amjad reverse-engineered Claude Code's Ultra Plan feature and discovered that Anthropic uses remote config to A/B test planning variants (simple, visual, deep). The deep plan variant uses a 4-agent pipeline: planner, critic, refiner, and finalizer. By extracting this prompt as a custom skill, users get deterministic access to the best variant without server dependency.

## Why It Matters
Users cannot choose which Ultra Plan variant they receive -- it is server-controlled via A/B randomization. The deep plan variant consistently produces higher-quality plans due to its critique pass, but there is no guarantee of receiving it. Extracting the prompt removes this randomness.

## Why People Are Using It
The deep plan variant with its 4-agent pipeline (planner, critic, refiner, finalizer) produces measurably better plans than the simple or visual variants. Practitioners want deterministic access to the best available planning approach. It also enables customization -- for example, adding domain-specific critic criteria.

## Potential Improvements
MetaSystem could create a custom skill implementing the 4-agent planning pipeline with MetaSystem-specific critic criteria (e.g., constitution compliance, fractal pattern adherence, governance checks).

## Potential Failure Modes
The prompt may drift as Anthropic updates Ultra Plan -- requires periodic re-extraction to stay current. The extracted prompt is a snapshot of one version and may lose optimizations from future Anthropic updates.

## Extraction Note — 2026-04-19
Extracted as **skill**: [[deep-plan-four-agent-pipeline.md]] in `extracts/skills/`
