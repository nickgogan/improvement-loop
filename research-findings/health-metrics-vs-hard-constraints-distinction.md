---
name: Health Metrics vs. Hard Constraints Distinction
summary: 'Intent Engineering distinguishes two types of boundaries: health metrics (what must not degrade while pursuing the objective -- steer but don''t block) and hard constraints (enforced in the orchestration
  layer, not the prompt layer). Health metrics prevent Goodhart''s Law; hard constraints prevent catastrophic violations. Prompt-layer steering guides reasoning; orchestration-layer enforcement guarantees
  compliance.'
implementation_notes: MetaSystem's current constraints are all prompt-layer (CLAUDE.md rules, skill instructions). The finding suggests identifying which constraints truly require orchestration-layer enforcement
  (e.g., 'never modify files outside system boundary' could be enforced via filesystem permissions or hooks, not just a CLAUDE.md instruction). Health metrics like 'don't degrade existing test coverage'
  should be measurable and checked automatically.
category: Intent Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- General
adopted_in: []
sources:
- intent-engineering-framework-for-ai-agents-product.md
related_findings:
- file: intent-engineering-framework-seven-part-agent-inten.md
  rel: enables
- file: stop-rules-as-execution-boundaries.md
  rel: same-problem
- file: autonomy-gradient-not-binary-delegation.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: "synthesized"
consumed_by:
  - "writing-agent-specifications.md"
---
## What It Is

A key design insight from Huryn's Intent Engineering Framework: not all boundaries are the same, and mixing them degrades both.

**Health Metrics** (steering constraints):
- What must not degrade while the agent pursues its objective
- Expressed as observable measures, not instructions
- Prevent Goodhart's Law: the agent optimizing one metric at the expense of everything else
- Example: "Customer satisfaction must not drop below 4.2/5" while optimizing resolution speed
- Live in the prompt layer as context that guides reasoning

**Hard Constraints** (enforced boundaries):
- Non-negotiable rules that must never be violated
- Enforced in the orchestration/infrastructure layer, not via prompts
- Example: "Never access customer financial data without explicit consent" -- enforced via API permissions, not an instruction
- If a constraint matters enough to be hard, it should not depend on the LLM choosing to follow it

The critical insight: "If a constraint matters, enforce it. If a decision is risky, gate it." Prompt-layer instructions are probabilistic guidance; orchestration-layer enforcement is deterministic compliance.

## Why It Matters

Most agent systems put all constraints in the prompt (CLAUDE.md, system prompt). The ETH Zurich study shows agents follow prompt instructions precisely -- but "precisely" is not "always." For constraints where violation is catastrophic (data deletion, unauthorized access, production deployment), prompt-layer enforcement is insufficient. The distinction forces architects to classify each constraint and route it to the appropriate enforcement mechanism.

## Why People Are Using It

This maps to well-understood patterns in software engineering: input validation (hard) vs. code style (steering), authentication (hard) vs. UX guidelines (steering). Huryn's contribution is formalizing this for agent systems where the boundary between "instruction" and "enforcement" is blurred by the prompt interface.

## Potential Improvements

A constraint registry that classifies each system constraint as health metric or hard constraint, with the enforcement mechanism documented alongside. Automated audit: check that every hard constraint has a corresponding enforcement mechanism outside the prompt.

## Potential Failure Modes

Over-classifying constraints as "hard" creates a rigid system where the agent has too little freedom to solve novel problems. Under-classifying creates safety risks. Health metrics that are not actually measured provide false comfort -- "don't degrade test coverage" means nothing if test coverage isn't checked automatically.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[health-metrics-vs-hard-constraints.md]] in `extracts/patterns/`
