---
notion_id: 3351e08b-9b34-81cb-9a66-c573db51d8a1
name: Intent Engineering Framework -- Seven-Part Agent Intent Specification
summary: 'Formal framework for encoding intent in AI agents beyond task lists or prompts. Seven components: Objective + Desired Outcomes (2-4 max) + Health Metrics (steer but don''t block) + Strategic Context
  + Constraints (two types: prompt-layer steering vs. orchestration-layer hard enforcement) + Decision Types/Autonomy (which decisions agent may make vs. must escalate) + Stop Rules. "Context without intent
  is noise." Health metrics vs. hard guardrails distinction is the key design insight.'
implementation_notes: 'The KB has no Intent dimension findings at all -- this is the first. Most complete intent specification framework found. Applicable to any agent in the KB workflow. The two-type constraint
  distinction (steering via prompt layer vs. hard enforcement in orchestration) is directly actionable. Source: https://www.productcompass.pm/p/intent-engineering-framework-for-ai-agents'
category: Intent Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- General
adopted_in: []
sources:
- intent-engineering-framework-for-ai-agents-product.md
- intent-engineering-pathmode-glossary.md
proposals: []
date_discovered: '2026-04-01'
last_updated: '2026-04-08'
related_findings:
- file: health-metrics-vs-hard-constraints-distinction.md
  rel: enabled-by
- file: autonomy-gradient-not-binary-delegation.md
  rel: same-problem
- file: stop-rules-as-execution-boundaries.md
  rel: extends
pipeline_status: "synthesized"
consumed_by:
  - "writing-agent-specifications.md"
---
# Intent Engineering Framework -- Seven-Part Agent Intent Specification

## What It Is
A formal framework for encoding intent in AI agents. "Intent is what determines how an agent acts when instructions run out."

**Seven-Part Intent Structure:**
1. **Objective** -- The problem + why it matters
2. **Desired Outcomes** -- Measurable results, 2-4 max
3. **Health Metrics** -- What must not degrade; steer but don't block
4. **Strategic Context** -- The broader system the agent operates within
5. **Constraints** -- Two types: steering (prompt layer) and hard (orchestration layer)
6. **Decision Types / Autonomy** -- Which decisions the agent may make vs. must escalate
7. **Stop Rules** -- Explicit conditions for halting

## Why It Matters
"Context without intent is noise." Health metrics vs. hard guardrails is the key design distinction.

## Why People Are Using It
Rigorous framework published Jan 2026. Multiple independent sources converge on intent engineering as the 2026 breakthrough discipline.

## Potential Failure Modes
Stop Rules are often omitted. Health metrics require quantification. Two-type constraint distinction requires architectural separation. Autonomy scope creep.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[intent-engineering-seven-part-specification.md]] in `extracts/patterns/`
