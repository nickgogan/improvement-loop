---
title: "Discount Development Cost in Design Decisions"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "dev-cost-estimation-bias-correction"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "model-resilient-prompt-engineering.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agents making design, architecture, or scoping decisions between multiple candidate approaches"
    - "always-loaded agent memory or instruction files where a small set of high-leverage standing rules is worth the context cost"
    - "teams noticing their AI agents repeatedly proposing the cheaper, lower-quality option without a stated quality tradeoff"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — a one-line addition to an always-loaded instruction file; removal has no migration cost"
  auditability: "medium — the rule's effect shows up as a shift in which design options get proposed and chosen over time; there is no single mechanical check that confirms the bias was corrected, only pattern observation across decisions"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Practitioner-reported standing rule in a production coding-agent operator's minimal always-loaded global memory file, kept there after repeatedly observing the estimate-vs-actual mismatch."
contract:
  preconditions: "An agent is weighing multiple design or implementation options and has access to an always-loaded instruction or memory layer where standing rules can be placed. At least one candidate option is materially higher-quality but appears more expensive to build under a human-timeline estimate."
  invariants: "When comparing design options, the agent does not let an implicit human-development-timeline cost estimate dominate the choice. Development cost is treated as reduced, not zero — quality, scalability, and maintainability considerations are not suppressed by an inflated cost estimate for the better option. The correction is scoped to technical design/architecture decisions; it does not apply to human-facing project planning or deadline estimation, where human timelines are still real."
  governance: "Owner: whoever maintains the agent's always-loaded instruction or memory file (a global CLAUDE.md-equivalent, an agent constitution). Adding or changing this rule is a deployment decision gated by the human who owns that file, since always-loaded context changes affect every session. The rule interacts with any standing minimal-abstraction or Occam's-razor preference already in force — this rule corrects cost mis-estimation; it does not license gold-plating, and the minimal-viable-abstraction preference still applies on top of it."
  recovery: "If the agent starts gold-plating or ignoring cost entirely after adoption → the correction has over-corrected; add an explicit counter-balancing heuristic (e.g., price options by tokens and review burden, not calendar time) rather than removing the rule outright. If the rule is observed leaking into human-facing project planning or real deadline estimation → scope it explicitly to technical design decisions in the instruction text. If design proposals still skew toward cheap/low-quality options after adoption → the rule may need to be more prominent or reinforced with a worked example, not merely stated once."
tags:
  - "extracted-artifact"
  - "rule"
  - "prompt-craft"
  - "design-decisions"
  - "cost-bias"
---

# Discount Development Cost in Design Decisions

**Source:** [[dev-cost-estimation-bias-correction]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

An agent is choosing between design or implementation options where one option is materially better on quality, scalability, or maintainability but appears more expensive to build if the agent implicitly estimates cost on a human development timeline.

## Action

**Required:** State explicitly, in an always-loaded instruction or memory layer, that development cost should not be given too much weight when making technical decisions. Let quality, scalability, and maintainability considerations dominate design-option selection rather than an inflated, human-timeline-based cost estimate.

**Forbidden:** Letting an unstated, human-timeline cost bias silently steer the agent toward the cheaper, lower-quality option without the tradeoff being surfaced. Applying this correction to human-facing project planning or real deadline estimation, where human timelines genuinely matter.

## Boundary

Enforced at the point an agent evaluates and selects among design options — architecture decisions, scoping calls, design-authoring skills. Lives in an always-loaded instruction/memory file so it applies to every relevant session, not just ones where someone remembers to invoke it.

## Enforcement

- **Mechanism:** A one-line standing rule in the always-loaded global instruction file (e.g., "when making technical decisions, don't give too much weight to development cost").
- **Check (deterministic):** No single mechanical check confirms compliance in the moment; the rule is a framing instruction, not a checkable field. **Check (pattern-level):** over a sample of design decisions, options are not systematically rejected on cost alone without a stated quality tradeoff.
- **Violation response:** If a design proposal favors a cheap/low-quality option, ask the agent to re-evaluate weighing quality/maintainability over the human-timeline cost estimate; if the pattern recurs, reinforce the rule's placement or add a worked example.
- **Cannot be self-certified:** the agent cannot reliably self-report whether its own cost estimate was biased; compliance is observed as a pattern across decisions, ideally by a human reviewing which options got proposed and chosen over time.

## Rationale

Models trained on human development data implicitly price design options at human implementation cost — the same 3D game that a frontier model estimates would take a human days-to-months to build, it can produce a playable version of in minutes when asked to just build it. This mispricing silently steers technical decisions toward the "cheap" option, which is often lower quality, less scalable, or harder to maintain — not because the agent judged the tradeoff, but because it mispriced the alternative. Design-option selection is upstream of everything an agent subsequently builds, so a small, always-loaded correction has outsized leverage: in an agentic workflow, development cost has collapsed relative to human timelines, so the factors that should dominate the decision are quality, scalability, and maintainability.

## Failure Modes

- **Over-correction into gold-plating.** The agent stops considering cost entirely and over-engineers, when development cost is lower, not zero — tokens, review burden, and maintenance costs are still real. Mitigation: pair the rule with an existing minimal-abstraction or Occam's-razor standing preference so the correction doesn't license unbounded scope growth.
- **Leakage into human-facing estimation.** The rule is scoped to technical design decisions, but could bleed into contexts where cost genuinely matters for humans (project planning, real deadlines for people who must execute the work). Mitigation: scope the rule explicitly to technical/architecture decisions in its wording.
- **Weak evidence base.** The bias observation rests on one practitioner's repeated informal observation rather than a controlled evaluation; the magnitude may vary by model generation and task type. Mitigation: treat the rule as a low-cost, easily-reversible correction rather than a load-bearing claim requiring rigorous validation before adoption.

## Contract

### Preconditions
An agent is weighing multiple design or implementation options and has access to an always-loaded instruction or memory layer where standing rules can be placed. At least one candidate option is materially higher-quality but appears more expensive to build under a human-timeline estimate.

### Invariants
When comparing design options, the agent does not let an implicit human-development-timeline cost estimate dominate the choice. Development cost is treated as reduced, not zero — quality, scalability, and maintainability considerations are not suppressed by an inflated cost estimate for the better option. The correction is scoped to technical design/architecture decisions; it does not apply to human-facing project planning or deadline estimation, where human timelines are still real.

### Governance
Owner: whoever maintains the agent's always-loaded instruction or memory file (a global CLAUDE.md-equivalent, an agent constitution). Adding or changing this rule is a deployment decision gated by the human who owns that file, since always-loaded context changes affect every session. The rule interacts with any standing minimal-abstraction or Occam's-razor preference already in force — this rule corrects cost mis-estimation; it does not license gold-plating, and the minimal-viable-abstraction preference still applies on top of it.

### Recovery
If the agent starts gold-plating or ignoring cost entirely after adoption → the correction has over-corrected; add an explicit counter-balancing heuristic (e.g., price options by tokens and review burden, not calendar time) rather than removing the rule outright. If the rule is observed leaking into human-facing project planning or real deadline estimation → scope it explicitly to technical design decisions in the instruction text. If design proposals still skew toward cheap/low-quality options after adoption → the rule may need to be more prominent or reinforced with a worked example, not merely stated once.
