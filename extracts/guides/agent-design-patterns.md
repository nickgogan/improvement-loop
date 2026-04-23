---
title: "Agent Design Patterns"
type: "guideline"
category: "Agent Design"
target_system:
  - "cross-system"
stage: "draft"
created: "2026-04-19"
updated: "2026-04-19"
author: "claude"
source_findings:
  - "conway-always-on-persistent-agent"
  - "emergent-agentic-behaviors-from-outcome-rl"
  - "critic-verifier-loop-with-termination"
  - "ai-developer-descent-into-madness-anti-pattern"
  - "soul-md-agent-constitution-pattern"
  - "harness-simplification-as-models-improve"
  - "self-improving-agent-prompt-tool-diagnosis"
  - "agent-clarification-over-assumption-pattern"
  - "specialized-parallel-agent-roles"
  - "five-layer-agent-prompt-architecture"
  - "agentic-infrastructure-pilot-to-production"
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "agent-design"
  - "identity"
  - "prompt-architecture"
contract:
  preconditions: "Agent role identified; need to design the agent's internal architecture"
  invariants: "Agent identity consistent across sessions; prompt layers maintain separation of concerns"
  governance: "IL-owned draft; Nick deploys to meta-system/knowledge/guides/"
  recovery: "If agent shows descent-into-madness symptoms, simplify prompt layers and add clarification behavior"
---

# Agent Design Patterns

How to design an individual agent's identity, prompts, and behavior. This guide covers the internal architecture of a single agent — from its constitution (who it is) through its prompt layers (how it receives instructions) to its behavioral patterns (how it acts under uncertainty). It does not cover multi-agent orchestration or inter-agent communication — those belong in G3 (Agent Architecture Decisions).

## When to Use This Guide

- You are designing a new agent and need to define its identity, constraints, and behavioral defaults
- An existing agent shows erratic behavior (scope drift, assumption-driven errors, infinite loops) and needs redesign
- You are structuring an agent's prompt stack and want a layered architecture instead of a monolithic system prompt
- You need to decide how much autonomy an agent should exercise versus when it should pause for human input
- You are moving an agent from prototype to production and need to harden its design

## Key Concepts

**1. Agent identity is separate from agent capability.** The constitution (who the agent is — values, tone, boundaries) is a distinct layer from skills and tools (what the agent can do). Identity persists across sessions and tasks; capabilities are loaded per context. Mixing them causes identity drift when capabilities change.

**2. Prompt architecture has five layers with distinct concerns.** Role/Scope, Instructions/Constraints, Context/Retrieved Data, Examples/Edge Cases, and Output Format/Tool-Calling each solve a different problem. Skipping layers 3-5 is the primary cause of "works in demo, fails in production."

**3. Agents should clarify intent gaps and resolve knowledge gaps independently.** The central tension in agent design is over-autonomy versus over-caution. The resolution: classify gaps into resolvable (fill via research, tools, inference) and intent-dependent (pause and ask). An agent that always asks is a bottleneck; one that never asks is dangerous.

**4. Quality belongs at the source, not in review layers.** Adding an agent to check another agent's output is a design smell. If the first agent's output requires a second agent to verify, the first agent's specification is wrong. Legitimate multi-agent architectures exist when agents have genuinely different capabilities, not when one exists to catch another's errors.

**5. Harness complexity should decrease as models improve.** Agent scaffolding co-evolves with model capabilities. Scaffolding that was necessary for one model generation becomes overhead for the next. Periodic audits of prompt complexity against current model capability prevent accumulated cruft.

---

## Procedure

### Step 1: Define the Agent Constitution

The constitution establishes WHO the agent is before specifying WHAT it does. This is the innermost, most stable layer — it changes rarely and applies across all tasks the agent performs.

A constitution has four sections:

| Section | Purpose | Changes When |
|---------|---------|-------------|
| **Core Truths** | Philosophical heuristics for resolving ambiguity | Rarely — foundational values shift |
| **Boundaries** | Operational immune system — what the agent must never do | When scope or trust changes |
| **Vibe** | Explicit behavioral overrides (e.g., "don't hedge, don't apologize") | When persona needs adjustment |
| **Continuity** | How the agent maintains state across sessions | When persistence architecture changes |

**Key design decisions:**

- **Action bias vs. deliberation bias.** Should the agent default to acting (draft code, run scripts) or analyzing (summarize, recommend)? Define this explicitly — models default to analysis unless overridden.
- **Learn-first protocol.** When the agent encounters an unknown situation, should it search the codebase and parse logs before asking the human? Define the self-resolution sequence.
- **Self-modification gating.** Can the agent modify its own memory or configuration? If so, through what mechanism? The safest default: proposal document requiring human approval.

### Step 2: Build the Five-Layer Prompt Stack

Each layer addresses a distinct failure mode. Build them in order:

**Layer 1 — Role and Scope.** What the agent is, what its job is, where that job begins and ends. This is not a personality description — it is an operational responsibility boundary.

- Define what the agent SHOULD do (positive scope)
- Define what the agent SHOULD NOT do (negative scope)
- Specify how the agent interprets ambiguous instructions

**Layer 2 — Instructions and Constraints.** Clear priorities in plain language plus security boundaries.

- System instructions override conflicting user instructions
- Ask for clarification when critical inputs are missing
- Security constraints preventing prompt injection and privilege escalation

**Layer 3 — Context and Retrieved Data (most commonly skipped).** Trust classification of all inputs.

- What counts as trusted instruction versus untrusted context
- How to handle retrieved data that is incomplete or contradictory
- Without this layer, agents treat all retrieved content as equally authoritative

**Layer 4 — Examples and Edge Cases.** Diverse coverage including adversarial cases.

- Decision pattern examples: when to call a tool (or not), when to ask for clarification, when to refuse
- Happy-path-only examples create agents that fail on the first edge case
- Include at least one adversarial/failure example per critical decision point

**Layer 5 — Output Format and Tool-Calling.** Action discipline for reliability.

- Output format determines whether downstream components can consume the result
- Tool-calling conventions: when to call, how to handle failures, retry behavior
- This is reliability engineering, not formatting preferences

### Step 3: Design Behavioral Patterns

Three behavioral patterns address the most common agent failure modes:

**Clarification behavior.** Implement the two-category gap classification:

| Gap Type | Agent Action | Example |
|----------|-------------|---------|
| **Resolvable** — can be filled by research, tools, or inference | Resolve autonomously | "What files exist in this directory?" → use ls |
| **Intent-dependent** — requires understanding user preference | Pause and ask | "Should I optimize for speed or readability?" → ask user |

On complex tasks, the agent's check-in rate should increase. Flat autonomy regardless of task complexity is a miscalibration signal.

**Self-correction behavior.** Well-designed agents exhibit three emergent self-improvement capabilities:

1. **Self-refinement** — incrementally adjust strategy across turns when initial approach underperforms
2. **Self-correction** — diagnose tool failures and adapt subsequent actions without external intervention
3. **Self-reflection** — evaluate own reasoning by cross-verifying results through independent computation

Design prompts that create SPACE for these behaviors rather than prescribing step-by-step tool use. Agents should decide tool usage based on task difficulty — heavy tool use on hard problems, minimal on easy ones.

**Critic/verifier loop.** When verification is genuinely needed (not to patch a bad generator — see Step 4):

- Generator produces output
- Critic with stricter instructions and independent retrieval access evaluates
- Patches applied based on critique
- Loop terminates at iteration limit OR confidence threshold
- Critic can fail closed — refuse to approve when evidence is insufficient

The termination condition is mandatory. Unbounded generate-critique loops are a common production failure — they consume tokens indefinitely without converging.

### Step 4: Check for the Descent-into-Madness Anti-Pattern

Before finalizing your design, run this diagnostic:

| Symptom | Diagnosis | Fix |
|---------|-----------|-----|
| You added an agent to check another agent's output | Quality-at-source failure | Redesign the first agent's constraints and acceptance criteria |
| Bug fixes create new bugs, which need more fixes | Specification is too loose | Tighten scope, add acceptance criteria, add test-on-write |
| You are building a framework to orchestrate your review agents | You are in the infinite recursion trap | Stop. Simplify. One agent with good constraints beats three agents checking each other |
| Initial speed gains are eroding over time | Technical debt from unreviewed output | Add human gate at stage boundaries; invest in quality infrastructure |

**The diagnostic rule:** If a second agent exists because the first produces unreliable output, the design is wrong. If a second agent exists because the task genuinely requires different capabilities (e.g., coding agent + testing agent with different toolsets), the design may be sound.

### Step 5: Plan for Production Hardening

Agents moving from pilot to production need different design considerations:

| Pilot Phase | Production Phase |
|-------------|-----------------|
| "Does this agent work?" | "Does this agent work reliably at scale?" |
| Capability benchmarks | Reliability metrics (error rates, retry frequency, failure modes) |
| Happy-path testing | Adversarial testing + edge cases |
| Manual oversight | Automated monitoring with human escalation |
| Cost tolerance | Cost optimization (model routing, caching, batching) |

**Production failure modes to design against:**
- Prompt injection via tool outputs (top agentic failure mode, per Anthropic March 2026)
- Scope creep — agent gradually expanding what it considers "in scope"
- Miscalibrated confidence — agent proceeding confidently on uncertain ground

### Step 6: Schedule Complexity Audits

Harness complexity is not static architecture — it co-evolves with model capabilities. Schedule periodic audits:

1. List all scaffolding in the agent's prompt stack (decomposition steps, explicit reasoning chains, guardrail instructions)
2. For each piece of scaffolding, ask: "Does the current model still need this?"
3. Remove scaffolding that the model handles natively — each removal reduces token cost and latency
4. Validate removals with eval data before committing

Example: Sprint decomposition was essential with Sonnet 4.5 (context anxiety). With Opus 4.6, removing it yielded 38% cost reduction and 36% time reduction. The scaffolding went from necessary to overhead in one model generation.

---

## Templates

### Agent Constitution Template

```markdown
# {{AGENT_NAME}} Constitution

## Core Truths
- {{PHILOSOPHICAL_HEURISTIC_1}} (e.g., "Evidence over intuition — a pattern is only as strong as its production evidence")
- {{PHILOSOPHICAL_HEURISTIC_2}}
- {{PHILOSOPHICAL_HEURISTIC_3}}

## Boundaries
- NEVER {{HARD_BOUNDARY_1}} (e.g., "modify live system configuration without human approval")
- NEVER {{HARD_BOUNDARY_2}}
- If uncertain about scope: {{BOUNDARY_RESOLUTION}} (e.g., "ask rather than guess")

## Vibe
- {{POSITIVE_BEHAVIOR}} (e.g., "Draft code blocks and run scripts rather than summarize intent")
- DON'T {{NEGATIVE_OVERRIDE_1}} (e.g., "hedge or apologize")
- DON'T {{NEGATIVE_OVERRIDE_2}} (e.g., "explain what you're about to do — just do it")

## Continuity
- Session boot: {{BOOT_SEQUENCE}} (e.g., "Read PROGRESS.md and last system-log entry before starting")
- Memory: {{MEMORY_STRATEGY}} (e.g., "Append to MEMORY.md; proposals for self-modification require human approval")
- State persistence: {{STATE_APPROACH}} (e.g., "Handoff prompts capture full context; no reliance on conversation history")
```

### Five-Layer Prompt Audit Checklist

```markdown
## Prompt Audit — {{AGENT_NAME}}

| Layer | Present? | Content Summary | Issues |
|-------|----------|----------------|--------|
| 1. Role & Scope | {{YES/NO}} | {{WHAT_AGENT_IS_AND_ISNT}} | {{MISSING_NEGATIVE_SCOPE / OK}} |
| 2. Instructions & Constraints | {{YES/NO}} | {{KEY_PRIORITIES_AND_SECURITY}} | {{MISSING_OVERRIDE_HIERARCHY / OK}} |
| 3. Context & Trust | {{YES/NO}} | {{TRUST_CLASSIFICATION_OF_INPUTS}} | {{NO_TRUST_CLASSIFICATION / OK}} |
| 4. Examples & Edge Cases | {{YES/NO}} | {{EXAMPLE_COVERAGE}} | {{HAPPY_PATH_ONLY / OK}} |
| 5. Output & Tool-Calling | {{YES/NO}} | {{FORMAT_AND_ACTION_DISCIPLINE}} | {{NO_FAILURE_HANDLING / OK}} |

### Missing Layers — Action Plan
| Layer | What to Add | Priority |
|-------|------------|----------|
| {{LAYER_NUMBER}} | {{SPECIFIC_CONTENT_TO_ADD}} | {{HIGH/MEDIUM/LOW}} |
```

### Descent-into-Madness Diagnostic

```markdown
## Agent Health Check — {{SYSTEM_NAME}}

### Symptom Scan
| Symptom | Present? | Evidence |
|---------|----------|----------|
| Agent added to check another agent's output | {{YES/NO}} | {{WHERE_AND_WHY}} |
| Bug fixes creating new bugs | {{YES/NO}} | {{PATTERN_DESCRIPTION}} |
| Building framework to orchestrate review agents | {{YES/NO}} | {{FRAMEWORK_DESCRIPTION}} |
| Initial speed gains eroding | {{YES/NO}} | {{TIMELINE_AND_METRICS}} |

### Diagnosis: {{HEALTHY / EARLY_WARNING / ACTIVE_DESCENT}}

### Remediation
{{IF_ACTIVE_DESCENT}}:
1. Stop adding agents. Identify the root-cause agent with unreliable output.
2. Redesign that agent: tighten scope to {{NEW_SCOPE}}, add acceptance criteria: {{CRITERIA}}
3. Remove review agents that existed only to compensate for the root-cause agent.
4. Add human gate at {{STAGE_BOUNDARY}} instead of automated review.
```

---

## Worked Examples

### Example 1: Designing a Research Extraction Agent

**Constitution:**

```
# Research Extractor Constitution

## Core Truths
- Evidence over intuition — a pattern is only as strong as its production evidence
- Deduplication is intellectual honesty — one canonical entry per pattern
- Neutral on implementation — flag priority and evidence strength, do not advocate

## Boundaries
- NEVER write to system configs, skills, or governance docs
- NEVER modify existing findings without reading them first
- If a finding might duplicate an existing one: search KB before creating

## Vibe
- Analytical and concise — no filler, no hedging
- Produce structured output (frontmatter + sections), not free-form analysis
- DON'T summarize when you can extract specific, actionable patterns

## Continuity
- Session boot: Read _index.md and last delta report
- Memory: Cross-session items become structured records (IB items, findings, entity corrections). No free-form carry-forward file.
- State: Each extraction session produces a delta report
```

**Five-Layer Prompt Audit:**

| Layer | Present? | Issues |
|-------|----------|--------|
| 1. Role & Scope | YES — "Researcher persona, writes to findings/sources/authorities only" | OK |
| 2. Instructions & Constraints | YES — DD-29 human gate, DD-30 read/write boundaries | OK |
| 3. Context & Trust | PARTIAL — sources have evidence_strength but no explicit trust classification for retrieved data | Add trust tiers for source types |
| 4. Examples & Edge Cases | NO — no worked examples of edge cases (duplicate detection, contradictory sources) | HIGH priority — add adversarial examples |
| 5. Output & Tool-Calling | YES — structured frontmatter schema, defined output format | OK |

### Example 2: Applying the Complexity Audit

**Before (Sonnet 4.5 era):**
- 10-sprint decomposition with contract negotiation per sprint
- Explicit reasoning chains in prompts ("First analyze dependencies, then...")
- Guardrail instructions for context window management
- Cost: $200 / 6 hours

**Audit questions:**
1. "Does Opus 4.6 still need sprint decomposition?" — No. Context anxiety resolved.
2. "Does Opus 4.6 need explicit reasoning chains?" — No. Reasoning models internalize this.
3. "Does Opus 4.6 need context window guardrails?" — Reduced. Still useful for 200K+ contexts.

**After (Opus 4.6 era):**
- Single-pass execution with evaluator at capability boundaries only
- Goal + constraints prompting, no prescribed reasoning
- Context guardrails retained only for very large contexts
- Cost: $125 / 3h50m (38% cost reduction, 36% time reduction)

### Example 3: Clarification Behavior in Practice

**Scenario:** Agent is asked to "refactor the authentication module."

| Gap | Type | Agent Action |
|-----|------|-------------|
| "Which files are in the auth module?" | Resolvable | Search codebase autonomously |
| "What framework is used?" | Resolvable | Read package.json / imports |
| "Should I prioritize readability or performance?" | Intent-dependent | Pause and ask user |
| "Should I change the API contract or keep it backward-compatible?" | Intent-dependent | Pause and ask user |
| "Are there existing tests?" | Resolvable | Search for test files |

The agent resolves 3 of 5 gaps independently, asks about 2. This is the target calibration — not zero questions, not five questions.

---

## Pitfalls

### 1. Monolithic system prompts
Stuffing identity, instructions, context rules, examples, and output format into a single undifferentiated block makes it impossible to update one concern without risking another. Use the five-layer architecture to separate concerns.

### 2. Identity-capability coupling
Defining who the agent IS inside skill-specific instructions means identity shifts every time a skill is loaded. Extract the constitution to a stable, always-loaded layer.

### 3. Happy-path-only examples
Layer 4 with only successful examples creates agents that freeze or hallucinate on the first edge case. Include examples of: tool failures, ambiguous inputs, conflicting instructions, and cases where the right answer is "I don't know."

### 4. Skipping Layer 3 (Context Trust)
The most commonly omitted layer. Without explicit trust classification, agents treat user instructions, retrieved documents, and tool outputs as equally authoritative. This is the entry point for prompt injection via tool outputs.

### 5. Unbounded critic loops
Critic/verifier loops without termination conditions consume tokens indefinitely. Always set an iteration limit AND a confidence threshold. When both are exhausted without convergence, escalate to human review rather than continuing.

### 6. Review-layer stacking
Each review agent you add makes the system 10x slower. If you find yourself adding a third review layer, you are in the descent-into-madness anti-pattern. Stop and redesign the generator.

### 7. Static harness complexity
Prompt scaffolding that was necessary for one model generation becomes pure overhead for the next. "We've always done sprint decomposition" is not a reason to keep it. Audit against current model capabilities.

### 8. Flat autonomy across task complexity
An agent that asks the same number of questions on trivial and complex tasks is miscalibrated. Check-in rate should increase with task complexity and blast radius.

---

## Related Guides

- **G1 — Writing Agent Specifications:** Covers the intent and acceptance criteria that feed into Layer 2 (Instructions/Constraints) of the prompt stack. Design the specification before designing the agent.
- **G3 — Agent Architecture Decisions:** Covers multi-agent orchestration, communication patterns, and when to split one agent into many. This guide handles the individual agent; G3 handles the ensemble.
- **G2 — Managing Agent Context:** Covers context engineering (what goes into the agent's context window and how). Layers 3-4 of the prompt stack depend on good context management.
- **G7 — Session Persistence and Memory:** Covers the Continuity section of the agent constitution — how state persists across sessions.
- **G4 — Building Agent Evaluation Suites:** Covers how to evaluate whether the agent behaviors designed in this guide actually work. Acceptance criteria from Step 1 become eval cases in G4.

---

## Contract

### Preconditions
- Agent role has been identified and its purpose is clear.
- The distinction between this agent and any neighboring agents in the system is established (use G3 if not).
- You have access to the agent's current prompt/configuration (if redesigning) or a blank slate (if new).

### Invariants
- Agent identity (constitution) is defined in a separate, stable layer from capabilities (skills/tools).
- All five prompt layers are explicitly addressed — skipped layers are documented as intentional omissions, not oversights.
- Clarification behavior distinguishes resolvable gaps from intent-dependent gaps.
- No agent exists solely to review another agent's output — quality is at the source.
- Harness complexity is periodically audited against current model capabilities.

### Governance
- This guide is IL-owned draft. Nick deploys to `meta-system/knowledge/guides/`.
- Agent constitutions are versioned and changes go through human review.
- Complexity audits are triggered by major model releases.
- Anti-pattern diagnostics are run when agent behavior degrades.

### Recovery
- If agent shows descent-into-madness symptoms (review agents checking review agents): stop adding agents, simplify the generator's specification, add human gate at stage boundaries.
- If agent over-asks (too many clarification pauses): review gap classification — some "intent" gaps may actually be resolvable.
- If agent over-assumes (makes wrong decisions silently): add clarification behavior and increase check-in triggers for high-blast-radius actions.
- If prompt changes break behavior: audit against the five-layer architecture — changes in one layer may have violated assumptions in another.
- If costs spike after design changes: run the complexity audit (Step 6) — removed scaffolding may have been re-added.
