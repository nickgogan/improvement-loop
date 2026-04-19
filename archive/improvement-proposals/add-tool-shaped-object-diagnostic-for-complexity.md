---
notion_id: "32c1e08b-9b34-818b-83cc-f40fad2ab056"
name: "Add Tool-Shaped Object Diagnostic for Complexity Decisions"
proposal: "Add a mandatory diagnostic question to any proposal or design decision that increases system complexity: 'What measurable output does this improve, and how will we verify the improvement?' If the answer is vague or unmeasurable, the proposal is flagged as potential tool-shaped object risk."
rationale: "Tool-Shaped Object Evaluation Lens (Medium evidence): Agent complexity that produces the feeling of work without measurable output is a tool-shaped object. The token-to-value relationship is often a cloud, not a line. This diagnostic prevents activity theater from masquerading as improvement."
status: "Not started"
target_system: "General / Cross-System"
priority: "P1 (Implement Now)"
risk_level: "Low"
implementation_complexity: "Low"
effort: "Low (< 1 hour)"
door_type: "Two-Way"
ops_impact: "Reduces Ops Burden"
conflicts: false
conflict_group: null
findings: []
date_proposed: "2026-03-23"
date_resolved: null
---

# Add Tool-Shaped Object Diagnostic for Complexity Decisions

## Current State
The improvement loop evaluates proposals on Implementation Complexity, Ops Impact, Risk Level, and Effort. There is no explicit check for whether a proposed change produces measurable output improvement vs. just adding activity. The research-proposer skill's Phase 4 assesses cost and complexity but not output-value validation.

## Proposed Change
Add a "Value Validation" gate to the improvement loop:

**For every proposal that adds complexity (new agent steps, new orchestration layers, new monitoring):**
1. What specific, measurable output does this improve?
2. How will we verify the improvement after implementation?
3. What's the baseline measurement today?

If the proposer cannot answer these concretely, the proposal gets a "Tool-Shaped Object Risk" flag in its page body. This doesn't block the proposal -- it surfaces the risk for human review.

This diagnostic should be embedded in the research-proposer skill's Phase 4 (Cost & Complexity Assessment) as a standard evaluation criterion.

## Rationale
The Tool-Shaped Object concept identifies a gradient between genuine tools and objects that merely feel like tools. LLMs are uniquely susceptible because they can produce the sensation of anything. Token budgets treated as linear-to-output capex, agent dashboard activity substituting for user-facing value, orchestration complexity that exists for its own sake -- all are tool-shaped object patterns. The diagnostic is simple: "What number are we trying to make go up, and is it actually going up?"

## Door Type Assessment
Two-way door. This is an additive evaluation criterion. If it proves unhelpful or creates analysis paralysis, it can be removed from the proposer template without affecting any other system behavior.

## Implementation Assessment
Low complexity. Requires adding 3 evaluation questions to the research-proposer skill's Phase 4 template and adding a "Tool-Shaped Object Risk" flag option to the proposal page body template. Text-only changes.

## Operational Impact
Reduces ops burden. Prevents the addition of complexity that doesn't produce measurable value. Catches activity theater before it gets implemented. No new monitoring required -- the diagnostic is evaluated at proposal time, not runtime.

## Implementation Steps
1. Add "Value Validation" section to the research-proposer skill's Phase 4 (Cost & Complexity Assessment)
2. Add "Tool-Shaped Object Risk" as an optional flag in the proposal page body template
3. For any flagged proposal, require the proposer to note the measurement gap in the page body's Implementation Assessment section
