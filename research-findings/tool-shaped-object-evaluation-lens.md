---
notion_id: 32c1e08b-9b34-819c-a785-ee32e5c86467
name: Tool-Shaped Object Evaluation Lens
summary: Agent complexity that produces 'the feeling of work' without measurable output is a tool-shaped object. The relationship between tokens consumed and value produced should be validated empirically.
  Applies to orchestration layers, agent swarms, and monitoring overhead.
implementation_notes: 'Directly applicable to evaluating whether our multi-agent patterns produce measurable value vs activity. Simple diagnostic: ''What number are we trying to make go up, and is it actually
  going up?'' Should inform any proposal to add orchestration complexity.'
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- General
adopted_in: []
sources:
- tool-shaped-objects.md
- agent-orchestrators-are-bad.md
proposals: []
date_discovered: '2026-03-23'
last_updated: '2026-05-24'
related_findings:
- file: capability-saturation-threshold-45-percent.md
  rel: same-problem
- file: specialization-theater-anti-pattern.md
  rel: extends
- file: acceptance-criteria-as-verifiable-eval-anchor.md
  rel: same-problem
- file: ace-execution-feedback-no-labels-required.md
  rel: same-problem
- file: agent-proof-of-work-ui-trust-building.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- verifying-agent-output.md
---
# Tool-Shaped Object Evaluation Lens

## What It Is
A critical evaluation framework for distinguishing productive agent tool use from 'tool-shaped objects' -- systems that produce the sensation of work without generating actual output.

## Why It Matters
The market for feeling productive is orders of magnitude larger than the market for being productive. Agent systems are uniquely susceptible because LLMs can produce the sensation of anything.

## Why People Are Using It
The essay reached significant distribution. The FarmVille analogy maps directly to agent dashboard culture where logs, metrics, and orchestration activity substitute for user-facing value.

## Potential Improvements
Could be formalized into a quantitative evaluation rubric: for each agent component, measure tokens consumed, wall-clock time, and measurable output delta.

## Potential Failure Modes
The evaluation itself can become a tool-shaped object. Some valuable agent work is genuinely hard to measure. The framework may create paralysis.

## April 2026 Update: Orchestrator Evidence

**"Agent Orchestrators Are Bad"** extends the tool-shaped object lens specifically to agent orchestrators: "the most sophisticated tool-shaped object ever created" because they genuinely perform some functions while hiding their ineffectiveness. The "specialization theater" anti-pattern (adopting agent teams because they mirror org structure) is a specific instantiation. FOMO-driven adoption creates a ratchet effect where not adopting orchestrators feels like falling behind, even when evidence shows they are suboptimal. Recommended diagnostic: define success metrics upfront -- if an orchestrator doesn't demonstrably improve latency, cost, or output quality, it is scrap, not infrastructure.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[tool-shaped-object-evaluation-lens.md]] in `extracts/patterns/`
