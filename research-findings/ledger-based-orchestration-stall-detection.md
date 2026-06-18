---
name: "Ledger-Based Orchestration Stall Detection"
summary: "MagenticOne uses explicit task/fact/progress ledgers as structured JSON for orchestration decisions. The orchestrator maintains a record of known facts, completed subtasks, and progress assessments — enabling stall detection when progress stops advancing and replanning when approaches fail."
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P3
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "gsd-stall-detection-via-progress-metrics.md"
    rel: same-problem
  - file: "dag-vs-bsp-two-graph-based-orchestration-models.md"
    rel: extends
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: raw
consumed_by: []
---

## What It Is

MagenticOne's orchestrator maintains three structured JSON ledgers during multi-agent task execution: a **task ledger** (overall objective decomposed into subtasks), a **fact ledger** (known facts discovered during execution), and a **progress ledger** (assessment of advancement toward the goal). The orchestrator consults these ledgers at each decision point to select the next agent, detect when progress has stalled, and trigger replanning when an approach fails.

The state is serialized as `MagenticOneOrchestratorState` — facts, plan, and progress ledger — all JSON-serializable via Pydantic models. This makes the orchestration decision-making process inspectable and resumable: the orchestrator can be paused, its state persisted, and execution resumed with full context.

## Why It Matters

Most multi-agent orchestrators rely on conversation history alone to make routing decisions — the orchestrator reads recent messages and decides what to do next. This works for simple tasks but fails for multi-step problems where progress is non-linear. Without an explicit progress record, the orchestrator cannot distinguish "still working" from "stuck in a loop."

The ledger pattern introduces a structured substrate for orchestration decisions. Progress becomes measurable: if the progress ledger shows no advancement after N turns, the system can definitively detect a stall rather than relying on heuristics over raw conversation. This also enables replanning — the orchestrator can reference what has been tried (from the fact ledger) and what hasn't worked (from the progress ledger) to generate a new plan.

## Why People Are Using It

Observed in [AutoGen (Microsoft)](https://github.com/microsoft/autogen) v0.7.5 — see [[autogen-analysis]] for structural details.

The pattern is used for complex multi-step problem solving where simple round-robin or LLM-selector patterns are insufficient. MagenticOne is positioned as the most capable orchestration mode, handling tasks that require multiple specialized agents working toward a goal with uncertain paths.

## Potential Alternatives

- Conversation-history-only routing: orchestrator reads the full message history and decides next steps without maintaining separate state. Simpler but loses structured progress tracking.
- Turn-count-based termination: use MaxMessageTermination to cap execution rather than detecting stalls. Crude but avoids the complexity of progress assessment.
- Agent-initiated escalation: agents themselves signal when they are stuck rather than the orchestrator detecting it externally. Relies on agent self-awareness.

## Potential Improvements

- Confidence scoring on progress assessments to distinguish "slow progress" from "no progress" from "negative progress" (backsliding).
- Automatic strategy rotation: when progress stalls, systematically try alternative approaches from a pre-defined playbook before escalating.
- Cross-task learning: persist ledger patterns across tasks to build heuristics about which approaches tend to stall for which task types.

## Potential Failure Modes

- **Progress assessment accuracy**: The LLM assessing progress may hallucinate advancement or fail to detect subtle stalls, making the ledger unreliable.
- **Ledger bloat**: For long-running tasks, the fact and progress ledgers grow indefinitely, consuming context window budget that could be used for actual task execution.
- **Replan oscillation**: Aggressive stall detection may trigger replanning too frequently, preventing approaches that require many turns to succeed.
- **Structured state overhead**: Maintaining three separate ledgers adds complexity to the orchestrator prompt; simpler tasks pay this overhead without benefiting from it.
