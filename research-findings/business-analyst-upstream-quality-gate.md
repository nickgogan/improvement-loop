---
name: Business Analyst as Upstream Quality Gate
summary: A dedicated Business Analyst agent (Mary in BMad) that runs before the PM phase, using 20+ brainstorming techniques and interactive coaching to clarify intent and produce a project brief before
  any implementation begins.
implementation_notes: null
category: Intent Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- bmad-method-masterclass.md
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
related_findings:
- file: bmad-method-v6-multi-agent-sdlc.md
  rel: enabled-by
- file: qa-agent-independent-compliance-review.md
  rel: same-problem
- file: yaml-templates-with-embedded-elicitation-instructions.md
  rel: same-problem
- file: advanced-elicitation-techniques-library.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Business Analyst as Upstream Quality Gate

## What It Is
The BA agent is the first agent in the pipeline. It uses 20 brainstorming techniques (What-if scenarios, First principles, SCAMPER, Six Thinking Hats, etc.) in three modes: Recommend, Random creative chaos, Progressive creative journey. Outputs: brainstorming artifact (techniques used, key insights, now/future/moonshots) + project brief (executive summary, problem, pain points, solution, target users). Brian's claim: "Mary the business analyst is probably the most special agent in the whole BMAD method."

## Why It Matters
If the intent is unclear, everything downstream is misaligned. The BA forces clarification before committing to implementation, catching scope issues at the cheapest point.

## Why People Are Using It
BMad Method positions the BA as the "most powerful" agent in the pipeline. The structured brainstorming techniques produce higher-quality briefs than unstructured human input.

## Potential Alternatives
- Human-written project briefs.
- PM agent with built-in requirements elicitation.
- Spec-first approaches (OpenSpec, PRD templates).

## Potential Improvements
- Integration with existing project context (not just greenfield).
- Adaptive technique selection based on project type.
- Cost-benefit analysis of BA phase vs skipping to PM.

## Potential Failure Modes
Overkill for small changes or bug fixes. BA phase adds latency to project start. Brainstorming techniques may produce quantity over quality. Human may check out during extended BA session.
