---
title: "Thinking Models: Mental Framework Commands for Coding Agents"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "thinking-models-mental-framework-commands-for-codi"
extraction_date: "2026-04-19"
last_change_session: 44
last_change_sl: "session-44-codifier-extraction-run"
identification_report: "2026-04-19-identification-report-4.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "coding agents that need structured multi-angle reasoning before committing to a design or implementation decision"
    - "agent skill libraries where on-demand reasoning frameworks can be invoked as slash commands"
    - "specification and architecture phases where single-mode reasoning risks missing trade-offs or root causes"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — each command invocation is stateless reasoning; no files or configs are modified by the framework execution itself"
  auditability: "medium — framework outputs are explicit structured reasoning artifacts that can be inspected; however, whether the correct framework was selected and genuinely applied (vs. cargo-culted) requires human review"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "TACHES packages these as installable slash commands with per-model .md definition files; no production deployments known within this system at time of extraction."
contract:
  preconditions: "Problem statement or decision context is available and sufficiently defined. The agent has access to the .md definition file for the selected framework(s)."
  invariants: "Each framework is applied independently before synthesis. Framework output is never treated as the final deliverable — it must produce a concrete downstream artifact."
  governance: "Owner: MetaSystem / Claude Build system. The 12-command set is defined by the TACHES implementation; additions or removals require a Design Decision."
  recovery: "If a framework produces no new information: document the null result and proceed without the framework. If framework selection was incorrect: re-run with a more appropriate command."
tags:
  - "extracted-artifact"
  - "skill"
---

# Thinking Models: Mental Framework Commands for Coding Agents

**Source:** [[thinking-models-mental-framework-commands-for-codi]]
**Form:** skill
**Extraction date:** 2026-04-19

## Purpose

A set of 12 slash commands in the `/consider:*` namespace, each invoking a distinct mental model to force structured reasoning from a specific angle before the agent commits to a solution.

## Inputs

- A problem statement or decision context
- Selection of one or more `/consider:*` commands appropriate to the problem type
- (Optional) Prior analysis or draft solution to subject to the selected framework

## Outputs

- Structured reasoning output from the selected mental model
- Explicit reframing of the problem from the model's perspective
- Identified gaps, risks, or alternatives that single-mode reasoning would miss
- (Optional) Recommendation or prioritized action set

## Commands and Mental Models

| Command | Mental Model | Primary Use |
|---|---|---|
| `/consider:pareto` | Pareto (80/20) | Identify the 20% of effort producing 80% of value |
| `/consider:first-principles` | First Principles | Decompose assumptions; reason from fundamentals |
| `/consider:inversion` | Inversion | Define what failure looks like; work backward |
| `/consider:second-order` | Second-Order Thinking | Surface downstream consequences of a decision |
| `/consider:5-whys` | Five Whys | Trace root cause through iterative questioning |
| `/consider:occams-razor` | Occam's Razor | Prefer the simplest sufficient explanation |
| `/consider:one-thing` | One Thing | Identify the single highest-leverage action |
| `/consider:swot` | SWOT | Strengths, weaknesses, opportunities, threats |
| `/consider:eisenhower-matrix` | Eisenhower Matrix | Classify by urgency and importance |
| `/consider:10-10-10` | 10-10-10 | Assess decision impact at 10 min, 10 months, 10 years |
| `/consider:opportunity-cost` | Opportunity Cost | Name what is foregone by choosing this path |
| `/consider:via-negativa` | Via Negativa | Improve by removing rather than adding |

## Steps

1. **Problem intake.** Receive the problem statement or decision context. Confirm the problem is well-defined enough to reason about.

2. **Framework selection.** Choose one or more commands appropriate to the problem type. Selection heuristics:
   - Debugging or root cause → `/consider:5-whys`, `/consider:first-principles`
   - Prioritization → `/consider:pareto`, `/consider:one-thing`, `/consider:eisenhower-matrix`
   - Architecture or design → `/consider:inversion`, `/consider:second-order`, `/consider:via-negativa`
   - Trade-off evaluation → `/consider:opportunity-cost`, `/consider:10-10-10`
   - Risk assessment → `/consider:swot`, `/consider:inversion`

3. **Framework execution.** Apply the selected model's structured instructions. Produce output strictly within the framework's perspective — do not blend frameworks during execution.

4. **Synthesis.** If multiple frameworks were applied, synthesize findings. Note where frameworks converge (high confidence) and where they conflict (requires judgment).

5. **Decision or recommendation.** Produce a concrete output: a decision, a prioritized list, or a set of identified risks.

## Failure Modes

- **Indiscriminate application.** Applying frameworks to every decision imposes overhead disproportionate to the benefit.
- **Mechanical cargo-culting.** Following a framework's structure without genuine engagement produces formatted noise, not insight.
- **Framework mismatch.** Selecting a framework poorly suited to the problem type yields low-signal output.
- **Over-synthesis.** Blending incompatible frameworks mid-execution produces incoherent output.

## Contract

### Preconditions
Problem statement or decision context is available and sufficiently defined. The agent has access to the .md definition file for the selected framework(s).

### Invariants
Each framework is applied independently before synthesis. Framework output is never treated as the final deliverable — it must produce a concrete downstream artifact.

### Governance
Owner: MetaSystem / Claude Build system. The 12-command set is defined by the TACHES implementation; additions or removals require a Design Decision.

### Recovery
If a framework produces no new information: document the null result and proceed without the framework. If framework selection was incorrect: re-run with a more appropriate command.
