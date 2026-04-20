---
name: "Context Warrant — Mandatory Justified Data Package"
summary: "Before any agent decision, the system assembles a context warrant: a formally justified, minimum-necessary data package that pulls only the specific dimensions required (history, policy, etc.) while enforcing data freshness requirements and rejecting extraneous context."
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: "P1 (Strong, Directly Applicable)"
applicability:
  - "General"
adopted_in: []
sources:
  - "11-step-governance-build-order-multi-agent-systems.md"
related_findings:
  - file: governed-dependency-chain-build-order.md
    rel: part-of
  - file: actor-passport-schema-bound-identity.md
    rel: depends-on
  - file: policy-as-data-machine-readable-constraints.md
    rel: depends-on
  - file: agent-context-kiss-commandments-minimum-viable.md
    rel: same-problem
  - file: ace-delta-updates-over-monolithic-rewrites.md
    rel: same-problem
date_discovered: "2026-04-19"
last_updated: "2026-04-19"
pipeline_status: "raw"
---

## What It Is

Step 5 of the 11-step governed multi-agent build order. Before an agent executes, the system must assemble the specific information needed for a safe decision. The context warrant is that assembly mechanism — a mandatory, formally justified data package.

**Key properties:**

1. **Justified** — every piece of context must have an explicit reason for inclusion. "Pull only the specific dimensions required, like history or policy." Context without a justification is rejected.

2. **Minimum-necessary** — the warrant pulls exactly what's needed and rejects extraneous assembly. This is not a retrieval system that returns everything potentially relevant; it is a constrained selection that returns only what is required.

3. **Freshness-enforced** — strict requirements for data freshness. Stale data (outdated policy versions, expired actor states, old history snapshots) is rejected, not just flagged. The context warrant ensures the system "never makes a decision based on stale or irrelevant signals."

4. **Dimension-scoped** — context is organized by dimension (history, policy, actor state, tool state) and the warrant specifies which dimensions are required for this specific decision. Dimensions not required for the current decision are excluded even if data exists for them.

**Position in dependency chain:** The context warrant is assembled after actor identity is validated (Step 4) and before coordination state machines run (Step 6). It ensures that every automated decision is made with the right information, not the maximum available information.

## Why It Matters

Over-context is a governance failure mode as dangerous as under-context. An agent with excessive context can make decisions that appear plausible but are based on irrelevant signals. An agent with stale context makes decisions that were valid at the data's timestamp, not the current moment. Both produce outputs that are ungovernable: you cannot audit why a decision was made if the context that drove it was not formally justified.

The context warrant pattern makes context assembly an auditable, governed step. The audit trail (Step 8) can capture what the context warrant contained, making it possible to reconstruct exactly what information was available to the agent at decision time.

This is directly applicable to MetaSystem: when skills execute, context is assembled ad-hoc from CLAUDE.md files, conversation history, and whatever files are read. A context warrant pattern would formalize this — defining which dimensions each skill needs, enforcing freshness, and logging what was actually assembled.

## Why People Are Using It

Practitioner-documented in the 11-step governance build order as a prerequisite for preventing "automated decisions from being made with excessive data or executed out of sequence." The pattern has conceptual overlap with RAG retrieval governance (what should and should not be retrieved) but extends it to all forms of context assembly, not just vector retrieval.

## Potential Improvements

- Warrant templates by decision type: high-risk decisions have mandatory dimension checklists; low-risk decisions have minimal warrants
- Freshness enforcement tooling: automated staleness detection that blocks warrant assembly if any required dimension exceeds its freshness threshold
- Cross-warrant consistency: for multi-step decisions, verify that the context assembled at each step is consistent with prior warrants in the same session

## Potential Failure Modes

- **Warrant inflation**: Over time, teams add more mandatory dimensions to warrants "just in case," eroding the minimum-necessary property
- **Freshness threshold tuning**: Thresholds that are too aggressive block valid decisions; thresholds that are too lenient allow stale data through
- **Dimension definition drift**: What counts as "history" or "policy" in the warrant dimensions changes as the system evolves, breaking warrant compatibility
- **Performance overhead**: Formally assembling and validating a context warrant before every decision adds latency; poorly implemented warrants become bottlenecks
- **Justification theater**: Teams write justifications for context that satisfy the formal requirement without actual analytical rigor
