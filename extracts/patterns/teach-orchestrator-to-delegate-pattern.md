---
title: "Teach Orchestrator to Delegate with Structured Subtask Descriptions"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "teach-orchestrator-to-delegate-pattern"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Orchestrator agent exists with the ability to spawn or invoke subagents. Tasks are decomposable into independent or loosely-coupled subtasks. Output format expectations are defined for each subtask type."
  invariants: "Every subagent invocation includes all four delegation elements (objective, output format, tool/source guidance, task boundaries). No subagent receives a bare topic keyword as its only instruction. Task boundaries explicitly state what is out of scope to prevent overlap between parallel subagents."
  governance: "Owned by Meta-System knowledge layer. Delegation templates are reviewed and updated when new skill types or subagent capabilities are added. Modifications require a Design Decision."
  recovery: "If subagents produce duplicate or overlapping results, the orchestrator detects overlap at merge time and re-decomposes with tighter boundaries. If a subagent returns empty results due to over-constrained boundaries, the orchestrator widens scope and retries with adjusted tool/source guidance."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Teach Orchestrator to Delegate with Structured Subtask Descriptions

**Source:** [[teach-orchestrator-to-delegate-pattern]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Orchestrator agents that delegate work to subagents using vague, topic-level instructions ("research semiconductor shortage," "analyze the codebase") produce duplicated effort, coverage gaps, and misinterpreted scope. Multiple subagents given the same loose brief independently search for the same information, while important angles go unexamined. The orchestrator's decomposition quality is the single highest-leverage variable in multi-agent system performance, yet it is routinely under-specified.

## Forces

- **Autonomy vs. direction.** Subagents need enough freedom to apply judgment, but too little guidance causes them to converge on the same obvious approach rather than covering complementary angles.
- **Decomposition cost vs. execution waste.** Investing tokens in detailed delegation descriptions costs upfront, but vague delegation wastes far more tokens through duplication and rework downstream.
- **Generality vs. specificity.** Generic delegation templates are reusable across domains but may not match the actual information landscape for a specific query. Over-specified templates constrain subagent creativity.
- **Maintenance burden vs. reliability.** Detailed delegation structures must be kept current as tools, sources, and capabilities evolve. Stale guidance is worse than no guidance if it points subagents at nonexistent resources.

## Solution

Require orchestrator agents to provide **four structured elements** for every subtask delegated to a subagent:

1. **Objective.** A clear statement of what the subagent should find, produce, or verify. Not a topic -- a deliverable. "Find the top 3 supply chain disruption events in 2025 with quantified impact" rather than "research supply chain."

2. **Output format.** How the result should be structured -- bullet list, table, prose summary with citations, structured data. This prevents merge-time incompatibilities when the orchestrator reassembles results.

3. **Tool and source guidance.** Which tools to use, which sources to prefer or avoid, and any access constraints. This prevents subagents from all hitting the same default search and missing domain-specific resources.

4. **Task boundaries.** What is explicitly out of scope for this subagent. Boundaries prevent overlap between parallel subagents and signal where another subagent is responsible. "Do NOT cover pricing impacts -- subagent B handles that."

The orchestrator constructs these four elements during its planning phase, before any subagent is spawned. For recurring task types (compare, enumerate, analyze, audit), delegation templates codify the standard decomposition so the orchestrator does not reinvent it each time.

## Consequences

**Positive:**
- Eliminates duplicate work across parallel subagents by making boundaries explicit.
- Enables the orchestrator to detect coverage gaps at planning time rather than discovering them at merge time.
- Anthropic's system with structured delegation outperforms single-agent Opus 4 by 90.2% on their internal eval -- the delegation quality is the differentiating factor.
- Standardized output formats simplify result merging and reduce post-processing errors.

**Negative:**
- Delegation description overhead adds latency and token cost to the planning phase, which is wasted if the task turns out to be simple enough for a single agent.
- Over-specification can constrain subagent creativity and cause failures when the prescribed sources or tools do not contain the needed information.
- Delegation templates require ongoing maintenance as the tool and source landscape evolves.
- The orchestrator must have sufficient domain knowledge to decompose well -- garbage decomposition with perfect formatting is still garbage.

## Known Uses

- **Anthropic multi-agent research system.** Production system where the pattern was discovered through failure analysis: early versions with vague delegation produced duplicate results and missed important angles. Structured delegation was the fix that unlocked the 90.2% improvement over single-agent.
- **MetaSystem skill orchestration.** Skills that spawn subagents (e.g., `/research-loop`, `/identify-artifacts`) implicitly use elements of this pattern but lack the full four-element structure as a codified requirement.

## Contract

### Preconditions

- An orchestrator agent exists with the ability to spawn or invoke subagents.
- Tasks are decomposable into independent or loosely-coupled subtasks.
- Output format expectations are defined for each subtask type.
- The orchestrator has sufficient domain context to perform meaningful decomposition.

### Invariants

- Every subagent invocation includes all four delegation elements: objective, output format, tool/source guidance, and task boundaries.
- No subagent receives a bare topic keyword as its only instruction.
- Task boundaries explicitly state what is out of scope to prevent overlap between parallel subagents.

### Governance

- Owned by Meta-System knowledge layer.
- Delegation templates are reviewed and updated when new skill types or subagent capabilities are added.
- Modifications to the pattern require a Design Decision.

### Recovery

- If subagents produce duplicate or overlapping results, the orchestrator detects overlap at merge time and re-decomposes with tighter boundaries before retrying.
- If a subagent returns empty results due to over-constrained boundaries, the orchestrator widens scope and retries with adjusted tool/source guidance.
- If delegation templates reference tools or sources that no longer exist, the orchestrator falls back to objective-only delegation with a warning surfaced to the human operator.
