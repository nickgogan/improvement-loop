---
name: Interrupt/Command Primitives for Human-in-the-Loop
summary: LangGraph provides interrupt(value) to pause graph execution at any point with full state persistence via checkpoint, and Command(goto=..., update=...) to combine state mutation with routing control
  in a single atomic primitive. Together they provide a clean abstraction for human-agent collaboration more flexible than simple approval gates.
implementation_notes: null
category: Intent Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3
applicability:
- General
adopted_in: []
sources: []
related_findings:
- file: dag-vs-bsp-two-graph-based-orchestration-models.md
  rel: extends
- file: human-on-the-loop-hotl-autonomy-tiering-framework.md
  rel: same-problem
- file: agui-human-control-layer-not-ui.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-05-24'
pipeline_status: raw
consumed_by: []
---

## What It Is

LangGraph provides two complementary primitives for human-in-the-loop workflows:

**`interrupt(value)`** — Pauses graph execution at any node. The current state is persisted via the checkpoint system (Postgres, SQLite, or memory). The `value` parameter is returned to the caller as the interrupt payload — it can be a question, a proposed action for approval, or any data the human needs to make a decision. Each interrupt has a unique ID (xxhash-based) to prevent stale or incorrect resumption.

**`Command(goto="node_name", update={"key": "value"})`** — Combines a state update with a routing decision in a single atomic primitive. When a human resumes from an interrupt, they can provide a Command that both updates the graph state (e.g., with their decision) and controls where execution goes next (e.g., skip to deployment, go back to planning).

Together, these provide a more flexible human-in-the-loop model than the binary approval gates used by most other frameworks (Archon's `approval:` nodes, GSD's human gates). With interrupt/Command, the human can:
- Approve and continue (Command with goto=next_node)
- Reject and redirect (Command with goto=different_node)
- Modify state and continue (Command with update={...})
- Ask the agent to reconsider (Command with goto=same_node, update={feedback: "..."})

## Why It Matters

Most agent frameworks model human-in-the-loop as a binary gate: approve or reject. Real human-agent collaboration is richer — the human might approve with modifications, redirect to a different path, provide additional context, or ask the agent to reconsider with specific feedback. The interrupt/Command pattern captures this richness without requiring a complex API.

The checkpoint-based persistence is equally important: the human can take hours to respond to an interrupt without the agent session timing out. The full graph state is reconstructed from the checkpoint when the human resumes.

## Why People Are Using It

Observed in [LangGraph](https://github.com/langchain-ai/langgraph) v1.1.6 — see [[langgraph-analysis]] for structural details. LangGraph reports production usage at Klarna, Replit, and Elastic. The interrupt/Command primitives are a core part of the framework's human-in-the-loop story, with dedicated examples in `examples/human_in_the_loop/`.

## Potential Alternatives

Binary approval gates (Archon — simpler but less flexible). Chat-based interaction loops (conversational but no structured state management). External approval systems (Slack buttons, email approvals — more accessible but disconnected from graph state).

## Potential Improvements

Interrupt timeout policies (auto-approve or auto-reject after N hours). Interrupt delegation (route to a different human based on the interrupt type). Interrupt analytics (tracking how often humans override vs. approve).

## Potential Failure Modes

Humans forgetting about pending interrupts (needs notification mechanism). State drift between interrupt and resume (external state changed while waiting). Complex Command routing creating spaghetti-like control flow that's hard to debug.
