---
name: "Interpretive Boundary Layer (Fact vs. Judgment)"
summary: "Every AI-powered knowledge system that surfaces information to decision-makers must explicitly label outputs as either 'act on this' (factual, verified, low-risk) or 'interpret this first' (judgment call, causal inference, novel pattern) — because presenting both at the same confidence level is an architectural failure that silently degrades decision quality."
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P1 (Implement Now)"
applicability:
  - "General"
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "world-models-orgs-three-architectures.md"
related_findings:
  - file: org-world-model-three-architecture-patterns.md
    rel: part-of
  - file: governance-ontology-semantic-foundation.md
    rel: related
  - file: context-warrant-justified-data-package.md
    rel: related
  - file: structural-vs-psychological-vs-economic-governance.md
    rel: related
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: classified
consumed_by: []
---

## What It Is

An explicit architectural layer that classifies every system output as one of two types before it reaches a human decision-maker:

**"Act on this"** — output that is:
- Factual, verified, low-risk
- Status rollup, dependency flag, metric that crossed a threshold with clear historical precedent
- The system is operating within its competence

**"Interpret this first"** — output that involves:
- A judgment call the system isn't equipped to make reliably
- A trend that might be significant or might be noise
- A correlation that might be causal or might be coincidental
- A prioritization that might reflect strategic reality or might reflect model bias
- The system is making an inference

The boundary is never perfect, but it must be explicitly drawn and surfaced in the interface. Failure to draw it means the system presents high-confidence and low-confidence outputs at the same salience — and the organization treats both with the same level of trust.

**Why this is architectural, not cosmetic:**
The failure is not a database choice, an embedding model choice, or an ingestion frequency choice. It is a fundamental failure in how the system presents its outputs. Once a team begins treating system output the way they treat a director's analysis, the damage is structural — a slow degradation of decision quality that looks like bad luck or market shifts rather than "the system was making editorial choices it was never equipped to make."

**Three silent failure modes this prevents:**
1. System flags a seasonal revenue dip as significant → drives a prioritization change → no one catches it because the person who knew it was seasonal was removed in a reorg
2. System surfaces a correlation between feature launch and churn → team kills the feature → actual cause was a billing change that shipped the same week
3. System develops information drift → stops routing certain signals to certain people → nobody notices because the absence of information is invisible in organizational noise

## Why It Matters

All three org world-model architectures share this blind spot. The vector DB approach never draws the boundary. The structured ontology draws it too conservatively (blind to emergent patterns). The signal fidelity approach creates false confidence because clean inputs make interpretive moves feel authoritative. The interpretive boundary layer is the meta-solution that applies to all three.

It is the difference between a world model that helps an organization and one that slowly degrades it.

## Why People Are Using It

Practitioner-documented by the author of this video as a missing layer in nearly every world-model implementation they surveyed. The video cites three concrete failure-mode examples with plausible real-world mechanisms. The concept maps to established AI safety concerns about confidence calibration and to governance concerns about audit trails.

## Potential Improvements

- UI patterns for surfacing the boundary: different visual treatment for factual vs. inferential outputs, explicit uncertainty scores, mandatory human confirmation before action on inferential outputs
- Automated classification: rules-based routing of system outputs to fact/judgment buckets based on output type (metric vs. trend, status vs. prioritization)
- Calibration feedback loop: track cases where humans override "act on this" outputs or confirm "interpret this first" outputs to improve classification over time

## Potential Failure Modes

- Boundary drift: over time, outputs initially labeled "interpret this first" get treated as "act on this" due to organizational habituation
- False precision: drawing the boundary creates a sense of safety that is not warranted if the classification itself is wrong
- Interpretation fatigue: too many "interpret this first" flags overwhelm humans, who start ignoring them — defeating the purpose
- The boundary requires organizational agreement on what counts as a judgment call, which is itself a judgment call
