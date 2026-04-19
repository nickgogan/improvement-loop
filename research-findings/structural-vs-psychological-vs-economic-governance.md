---
name: Structural vs Psychological vs Economic Governance
summary: Three distinct governance enforcement philosophies observed across 7 repos. Structural (tool allowlists, validators, CI checks), Psychological (persuasion engineering, rationalization prevention), and Economic (budget hard-stops, atomic checkout exclusion). No repo uses all three.
implementation_notes: null
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- cross-repo-comparison.md
related_findings: []
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-08'
pipeline_status: "raw"
consumed_by: []
---
## What It Is

Three distinct governance enforcement philosophies observed across 7 repos:

1. **Structural** (GSD, BMAD, OpenClaw) — enforcement via architecture. Tool allowlists restrict available actions. Validator rules check outputs against schemas. SDK boundaries prevent unauthorized API calls. CI architecture checks verify compliance. Hard to bypass because enforcement is built into the system's structure.

2. **Psychological** (Superpowers) — enforcement via persuasion engineering. Prompts are designed to prevent rationalization ("I know the rule says X, but in this case..."). Red Flags tables enumerate known failure patterns. Iron Laws are stated as non-negotiable principles. Based on Meincke et al. 2025 research on AI behavioral compliance. Works because the agent wants to follow the rules.

3. **Economic** (Paperclip) — enforcement via resource constraints. Budget hard-stops prevent overspending regardless of agent intent. Atomic checkout exclusion prevents conflicting concurrent modifications. Board approval gates require authorization before resource-intensive operations. Agent can't overspend because the server stops it. Works because rule-breaking is impossible, not just discouraged.

No repo uses all three approaches.

## Why It Matters

Most agent governance discussions focus exclusively on structural enforcement — allowlists, validators, and architectural constraints. The psychological and economic approaches represent underexplored dimensions of the governance design space.

A layered model using all three could be more robust than any single approach: structural enforcement as the primary guardrail, psychological enforcement to catch cases that slip through structural gaps, and economic enforcement as the hard backstop that makes catastrophic failures impossible regardless of the other layers' effectiveness.

## Why People Are Using It

Comparative analysis across 7 repos — see [[cross-repo-comparison]] for full details.

The three philosophies correlate with product type. Frameworks (GSD, BMAD) naturally lean structural because they control the execution environment. Products with real money at stake (Paperclip) naturally lean economic because the consequences of governance failure are financial. The psychological approach (Superpowers) is unique in treating agent compliance as a persuasion problem rather than an enforcement problem.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Pure structural | Only architectural enforcement | When the system architecture is fully controllable and complete |
| Layered defense model | All three philosophies in concert | For high-stakes systems where no single approach is sufficient |
| Formal verification | Mathematical proof of compliance properties | For safety-critical systems where probabilistic compliance is unacceptable |
| Human-in-the-loop only | No automated governance; human reviews all actions | For low-volume, high-stakes operations |

## Potential Improvements

- Design a layered governance model that combines all three philosophies with clear escalation between layers
- Evaluate how MetaSystem's current governance maps to these three categories (likely primarily structural + psychological via CLAUDE.md rules)
- Investigate whether economic governance principles apply to token budgets and context window management

## Potential Failure Modes

- **Structural gaps**: Architectural enforcement can't cover every edge case — novel actions may not be in the allowlist
- **Psychological fragility**: Persuasion-based compliance may degrade with model updates or adversarial prompting
- **Economic rigidity**: Hard budget stops may prevent legitimate high-value actions that exceed thresholds
- **Layer interaction**: Multiple governance philosophies may conflict (structural allows an action, economic blocks it) creating confusion
- **Complexity burden**: Maintaining three governance layers increases system complexity and debugging difficulty
- **False confidence**: Having all three layers may create overconfidence that governance is comprehensive when gaps exist between layers
