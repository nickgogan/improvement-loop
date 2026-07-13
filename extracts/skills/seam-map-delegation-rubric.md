---
title: "Seam-Map Delegation Rubric — Three-Question Workflow Partition"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "human-ai-seam-identification-three-question-rubric"
extraction_date: "2026-07-13"
last_change_session: 146
last_change_report: "writing-agent-specifications.harvest-queue"
identification_report: "writing-agent-specifications.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "an operator deciding which parts of a candidate workflow to hand to an AI agent versus keep human-owned"
    - "advisory tooling that partitions a proposed workflow into human, AI, and joint responsibilities rather than returning a binary automate/don't-automate verdict"
    - "intake for design interviews that decide whether a workflow deserves an agent at all"
    - "operators who want to surface the tacit structure of their own work before writing an agent specification"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "specify"
  reversibility: "trivial — produces an advisory seam map; revising or re-running the partition has no migration cost"
  auditability: "high — the output is an explicit three-column seam map (human / AI / joint) that a reviewer can inspect against the workflow; the question-by-question rationale is recorded"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Source is one practitioner's taught procedure grounded in her own newsletter case (avoided work → agent-assisted setup that improved quality of life); no quantified experiment. Not yet applied in practice at time of extraction."
contract:
  preconditions: "An operator has a specific candidate workflow in mind and a declared goal (North Star) that the workflow is meant to serve. The operator can answer the three elicitation questions honestly. A human is available to own the resulting partition decision."
  invariants: "The output is always a partition (human-owned / AI-owned / joint), never a binary automate-or-not verdict. Problem identification, standards, and direction remain on the human side of the seam. The partition is marked with a re-evaluation trigger — it is treated as a snapshot that goes stale as agent capability grows, not a permanent boundary."
  governance: "Advisory only. The human operator owns the seam map and any delegation decision that follows it; the rubric never itself moves work across the seam. Re-running the rubric is unrestricted. Acting on its output — actually delegating a partitioned workflow — is a separate human-gated decision."
  recovery: "If avoided work turns out to require human judgment or authority → keep it human-owned regardless of the avoidance signal (avoidance is not sufficient evidence of delegability). If the operator cannot actually write the playbook for the 'hireable' work → the hireable classification is unsafe; route the workflow back to human ownership or to tacit-knowledge elicitation before delegating. If a prior seam map has gone stale (capability has shifted) → re-run the rubric and re-partition."
tags:
  - "extracted-artifact"
  - "skill"
  - "delegation"
  - "human-ai-seam"
  - "intent-engineering"
---

# Seam-Map Delegation Rubric — Three-Question Workflow Partition

**Source:** [[human-ai-seam-identification-three-question-rubric]]
**Form:** skill
**Extraction date:** 2026-07-13

## Purpose

A procedure for locating the seam between what belongs to the human and what belongs to the AI in a candidate workflow. Most delegation guidance answers "what *can* the agent do." This rubric answers the harder question — "which parts of this workflow *should* leave the human" — and returns a **seam map** (human-owned / AI-owned / joint) rather than a yes/no on automation.

The surface form is three selection questions (Vicky Zhao's cohort rubric). The deeper output is a partition: problem identification, standards, and direction stay with the person "in the driver's seat"; playbook-executable execution crosses to the AI. Working the questions also forces the operator to articulate where they are blocked and why — surfacing tacit structure that then makes any downstream agent specification concrete.

## Inputs

- A specific candidate workflow the operator is considering delegating.
- The operator's honest answers to the three elicitation questions (avoided work, hireable work, North-Star relevance).
- The declared goal / North Star the workflow is meant to serve.

## Outputs

- A **seam map**: three columns — human-owned parts, AI-owned parts, joint parts — for the workflow.
- A judgment on whether the workflow is worth delegating at all (some workflows fail all three questions and should not be automated).
- Surfaced tacit structure — where the operator is blocked and why — as raw material for a concrete agent specification.

## Steps

### 1. What are you avoiding?
Elicit procrastinated-but-important work. A complicated, energy-expensive first hurdle is exactly where an agent that unlocks the *start* changes quality of life. Explicitly counter the default of automating nice-to-haves ("I never looked at that morning brief again") — the high-leverage target is avoided-important work, not easy-to-spin-up work.

### 2. What would you hire for?
If the operator already understands the work well enough to onboard an intern or assistant with a playbook, that same playbook can onboard an agent. **Guard:** if the operator cannot actually write the playbook, the "hire for" answer overestimates their ability to articulate the work — flag it and do not classify the work as cleanly delegable yet.

### 3. What moves the North Star?
Tie workflow selection to the goal already declared for the operator's system, not to what is easy to build. A workflow that scores on avoidance and hireability but does not move the North Star is a lower-priority candidate.

### 4. Partition into a seam map.
For the selected workflow, ask explicitly: "what can I do, what can AI do, what can a combination of us do." Place problem identification, standards, and direction on the **human** side — "it's always you, the person who's thinking, that is in the driver's seat." Place playbook-executable execution on the **AI** side. Everything that requires human framing but AI execution goes in the **joint** column. Emit the three-column map.

### 5. Re-evaluation trigger.
Mark the seam map as a snapshot. Seams move as agent capability grows; a static partition goes stale. Record a condition or date for re-running the rubric rather than treating the boundary as permanent.

## Failure Modes

- **Avoidance ≠ delegable.** Some avoided work is avoided precisely because it requires human judgment or authority — the very parts that must not cross the seam. Avoidance is a *candidate* signal, not proof of delegability.
- **Rubric applied once, not re-applied.** Seams move; a partition captured today is stale tomorrow. Without a re-evaluation trigger the map decays silently.
- **North-Star question degenerates** into justifying whatever the operator already wanted to automate. Keep the goal check honest — it is a filter, not a rationalization.
- **Playbook overestimation.** The "what would you hire for" answer assumes articulable knowledge the operator may not actually be able to write down (the tacit-knowledge barrier). If the playbook can't be written, the hireable classification is unsafe.

## Adaptation Notes

Nick's ruled framing (wave-3 gate, 2026-07-13) sets how this rubric is meant to live inside the engine: it is extracted as a **Librarian advisory capability**, not merely a workflow-selection checklist. The Librarian helps an operator see which parts of a potential workflow should belong to the human rather than the AI (or the AI system), returning the seam map as the advisory product. Concretely, the three questions are folded into two places: the Librarian's **design-mode intake**, and the **Phase 4 agent-vs-skill interview script**. "Avoided work + hireable work + North-Star relevance" is a compact intake for eliciting which workflows deserve agents at all — the interview's ready-made front door. The rubric's value is the partition it produces, so any host should render the output as an explicit human/AI/joint artifact rather than an implicit answer.

## Contract

### Preconditions
An operator has a specific candidate workflow in mind and a declared goal (North Star) that the workflow is meant to serve. The operator can answer the three elicitation questions honestly. A human is available to own the resulting partition decision.

### Invariants
The output is always a partition (human-owned / AI-owned / joint), never a binary automate-or-not verdict. Problem identification, standards, and direction remain on the human side of the seam. The partition is marked with a re-evaluation trigger — it is treated as a snapshot that goes stale as agent capability grows, not a permanent boundary.

### Governance
Advisory only. The human operator owns the seam map and any delegation decision that follows it; the rubric never itself moves work across the seam. Re-running the rubric is unrestricted. Acting on its output — actually delegating a partitioned workflow — is a separate human-gated decision.

### Recovery
If avoided work turns out to require human judgment or authority → keep it human-owned regardless of the avoidance signal. If the operator cannot actually write the playbook for the "hireable" work → the hireable classification is unsafe; route the workflow back to human ownership or to tacit-knowledge elicitation before delegating. If a prior seam map has gone stale (capability has shifted) → re-run the rubric and re-partition.
