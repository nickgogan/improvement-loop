---
name: "Declarative Goal-Driven Agent Prompting — Define Done, Not Steps"
summary: "Shift prompts from imperative (tell the agent what to do step-by-step) to declarative (state success criteria and let the agent explore). LLMs are exceptionally good at looping until they meet specific goals; imperative prompts constrain this capability and produce inferior results."
implementation_notes: null
category: "Prompt Craft"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General / Cross-System"
adopted_in: []
sources:
  - "karpathy-skills-claudemd-four-principles.md"
related_findings:
  - file: "bmad-outcome-based-skill-rewrite-pattern.md"
    rel: "same-problem"
  - file: "context-enrichment-for-task-clarity.md"
    rel: "enables"
  - file: "acceptance-criteria-as-verifiable-eval-anchor.md"
    rel: "same-problem"
  - file: "agent-clarification-over-assumption-pattern.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: classified
consumed_by: []
---

## What It Is

A prompting philosophy where the human specifies *what done looks like* rather than *how to get there*. Instead of prescribing steps ("add a button in the top-right corner that opens a modal with 5 icons"), the prompt defines the goal and success criteria ("let the user select an icon for each agent"). The agent then explores implementation options autonomously.

Karpathy's original framing: "LLMs are exceptionally good at looping until they meet specific goals. Instead of telling it what to do, just give it success criteria or a specific goal in mind and just leave it to explore." The contrast is imperative vs. declarative:
- **Imperative**: "Do step 1, then step 2, then step 3 using approach X"
- **Declarative**: "The user must be able to accomplish Y. Figure out how."

Karpathy Skills demo: asked for "a way for the user to be able to select an icon for each agent" — no specification of UI location, icon count, or design. The agent placed an icon picker inline, offered a palette of options, and updated the UI state cleanly on selection.

## Why It Matters

Imperative prompts create three problems:
1. **Premature optimization**: the human specifies an approach before the agent has analyzed the codebase, often missing better options
2. **Reduced autonomy yield**: the agent's search space is constrained to the prescribed approach even when alternatives are superior
3. **Fragility**: if the prescribed approach fails (wrong file, API change, missing dependency), the agent gets stuck rather than adapting

Declarative prompts leverage the core LLM strength — loop-until-goal — while keeping the human in control of outcomes rather than implementation details. This is the runtime analog to the outcome-based skill rewrite pattern (which applies the same principle to skill instruction authoring).

## Why People Are Using It

Karpathy encodes this as Principle 4 in Karpathy Skills CLAUDE.md (43K GitHub stars). The viral tweet framing gave it broad practitioner exposure. The principle aligns with how modern agents are architected — ReAct loops, tool-use cycles, and agentic search are all built around goal pursuit, not script execution. Prescriptive prompts fight the architecture; declarative prompts work with it.

## Potential Improvements

Combine with explicit success criteria format: instead of just describing the goal, provide measurable acceptance criteria (e.g., "Done when: user can click any agent card and change its icon, change persists across page reload"). This gives the agent a verifiable loop-exit condition rather than a fuzzy goal, reducing over-iteration. See `acceptance-criteria-as-verifiable-eval-anchor.md`.

## Potential Failure Modes

Purely declarative prompts can produce unexpected implementations when the agent's design intuitions diverge from the human's unstated preferences. The agent may choose a technically correct but aesthetically or architecturally wrong approach. For tasks with strong constraints (accessibility requirements, API budget limits, specific UX conventions), a hybrid — declarative goal + constraint list — performs better than pure declarative. Also: agents still need sufficient context about the codebase to make good exploration decisions; declarative prompts don't eliminate the need for context engineering.
