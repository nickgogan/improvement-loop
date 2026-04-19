---
title: "Tool-Shaped Object Evaluation Lens"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "tool-shaped-object-evaluation-lens"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "A system or component exists that consumes tokens, compute, or human attention. At least one measurable output metric has been defined for the system's purpose."
  invariants: "Every agent component must have at least one named output metric. The relationship between resources consumed and value produced is validated empirically, not assumed. Evaluation of the evaluation itself is subject to the same lens."
  governance: "Component owners review token-to-value ratios at regular intervals. New orchestration layers require an upfront success metric definition before adoption. The lens is applied before adding complexity, not after."
  recovery: "If a component is identified as a tool-shaped object, freeze its expansion, measure its actual output contribution over a defined window, then either define a concrete metric it must improve or remove it."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Tool-Shaped Object Evaluation Lens

**Source:** [[tool-shaped-object-evaluation-lens]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agent systems produce activity that feels like productive work -- logs scroll, dashboards update, orchestrators coordinate -- but no measurable output improves. The market for feeling productive vastly exceeds the market for being productive, and LLMs are uniquely capable of producing the sensation of anything. Teams add orchestration layers, monitoring infrastructure, and multi-agent swarms without validating whether these components improve the metrics they claim to serve.

## Forces

- **Activity vs. output:** Agent components that produce visible activity (logs, metrics, coordination messages) are psychologically rewarding even when they contribute nothing to user-facing value.
- **Partial functionality masks waste:** The most dangerous tool-shaped objects genuinely perform some functions, making them harder to identify than pure waste. An orchestrator that routes 30% of tasks correctly feels like infrastructure, not overhead.
- **FOMO-driven adoption:** Not adopting orchestrators or agent teams feels like falling behind, creating a ratchet effect where complexity increases without evidence of benefit.
- **Measurement difficulty vs. inaction risk:** Some genuinely valuable agent work is hard to measure, creating tension between demanding metrics and paralyzing productive work with evaluation overhead.
- **Evaluation overhead as its own trap:** The evaluation framework itself can become a tool-shaped object -- extensive measurement apparatus that produces the feeling of rigor without changing decisions.

## Solution

Apply a diagnostic filter before and during any agent component's lifecycle:

1. **Name the metric upfront.** Before adopting any orchestration layer, agent team, or monitoring component, answer: "What number are we trying to make go up, and how will we know if it is actually going up?" If no concrete metric can be named, the component is speculative at best.

2. **Measure token-to-value ratio.** For each agent component, track three quantities: tokens consumed, wall-clock time spent, and measurable output delta. If a component consumes significant resources without a corresponding output improvement, it is scrap, not infrastructure.

3. **Apply the specialization theater test.** When adopting multi-agent patterns, check whether the team structure mirrors an org chart (specialization theater) rather than reflecting a genuine decomposition of the problem. Org-chart-shaped agent teams inherit human coordination overhead without human judgment to compensate.

4. **Validate empirically, not architecturally.** A component that is "theoretically sound" or "architecturally elegant" but does not demonstrably improve latency, cost, or output quality is a tool-shaped object until proven otherwise.

5. **Re-evaluate periodically.** Components that provided genuine value at adoption may become tool-shaped objects as the system evolves. The lens is not a one-time gate but a recurring diagnostic.

## Consequences

**Positive:**
- Prevents accumulation of orchestration complexity that consumes tokens without improving output
- Catches specialization theater before it becomes entrenched architecture
- Creates a shared vocabulary ("tool-shaped object") for naming the problem without blame
- Forces upfront metric definition, which clarifies purpose even when the component turns out to be valuable

**Negative:**
- Risk of measurement paralysis -- teams may avoid adopting genuinely useful components because they cannot immediately prove value
- The lens is easier to apply to quantifiable outputs than to qualitative improvements (e.g., code readability, developer experience)
- Simple diagnostics may be too blunt for components with diffuse, indirect benefits
- Can create adversarial dynamics where component owners game metrics to survive the evaluation

## Known Uses

- Documented in the "Tool-Shaped Objects" essay (significant practitioner distribution) with the FarmVille analogy for dashboard culture
- Extended by "Agent Orchestrators Are Bad" to specifically target orchestration layers as "the most sophisticated tool-shaped object ever created"
- The specialization theater anti-pattern is a named instantiation -- adopting agent teams because they mirror org structure rather than because they improve output
- MetaSystem's own multi-agent patterns are subject to this lens: does adding a verification agent improve output quality, or does it produce the feeling of rigor?

## Contract

### Preconditions
A system or component exists that consumes tokens, compute, or human attention. At least one measurable output metric has been defined (or is definable) for the system's stated purpose. The evaluator has access to resource consumption data and output quality signals.

### Invariants
Every agent component must have at least one named output metric that is tracked over time. The relationship between resources consumed and value produced is validated empirically, not assumed from architecture diagrams. The evaluation lens itself is subject to its own criteria -- if the evaluation process consumes resources without changing decisions, it is a tool-shaped object.

### Governance
Component owners review token-to-value ratios at regular intervals (not just at adoption time). New orchestration layers, agent teams, or monitoring infrastructure require an upfront success metric definition before adoption is approved. The lens is applied before adding complexity, not retroactively. Periodic re-evaluation catches components that have become tool-shaped objects through system evolution.

### Recovery
If a component is identified as a tool-shaped object: freeze its expansion immediately, measure its actual output contribution over a defined observation window (not a single run), then either define a concrete metric it must improve within a bounded timeframe or remove it. If the evaluation process itself is identified as overhead, simplify it to the single most informative diagnostic: "What number went up?"
