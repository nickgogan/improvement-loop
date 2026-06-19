---
title: "Agent Architecture Decisions"
type: "guideline"
category: "Orchestration"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-04-19"
updated: "2026-05-25"
author: "claude"
source_findings:
  - "capability-saturation-threshold-45-percent"
  - "l-d-hypothesis-information-loss-across-agent-bound"
  - "legitimate-multi-agent-domains-taxonomy"
  - "specialization-theater-anti-pattern"
  - "task-contract-pattern-schema-first-agent"
  - "advisor-executor-api-pattern"
  - "worktree-isolation-for-parallel-agent-sessions"
  - "task-specific-model-routing-table-march-2026-bench"
  - "frontier-release-compression-march-2026"
  - "agent-teams-shared-communication-channel"
  - "deep-plan-multi-agent-exploration-pattern"
  - "agent-sprawl-anti-pattern-microservices-redux"
  - "agent-type-system-six-roles"
  - "google-a2a-protocol-agent-to-agent-interoperabilit"
  - "brain-hands-decoupling-architecture"
  - "bmad-method-v6-multi-agent-sdlc"
  - "gstack-specialist-role-architecture"
  - "agent-architecture-layer-impermanence"
  - "transitional-lock-in-risk-and-shim-assessment"
  - "six-layer-agent-infrastructure-stack"
  - "claude-code-12-agent-primitives"
  - "specialized-harness-engineering-deterministic-rail"
  - "oz-multi-agent-room-model"
  - "agui-human-control-layer-not-ui"
  - "model-tier-routing-expensive-orchestrator-cheap-s"
  - "orchestrated-execution-one-task-per-sub-agent-wit"
  - "superpowers-plugin-spec-driven-sub-agent-orchestra"
  - "autoresearch-loop-autonomous-metric-driven"
  - "claude-dispatch-native-mobile-to-local-agent-orch"
  - "error-aware-backtracking-as-compound-error-mitigation"
  - "execution-topology-as-runtime-selection"
  - "four-zone-agent-architecture-framework"
  - "gsd-get-shit-done-plugin"
  - "harness-engineering-third-evolution"
  - "parallel-claude-code-instances-per-workspace"
  - "review-triggered-remediation-dispatch"
  - "skill-phase-pipeline-shared-session-orchestrator"
  - "skills-as-markdown-sop-files-encode-processes"
  - "sub-agent-context-isolation-for-parallel-complex"
  - "subagent-as-uniform-tool-interface"
  - "subagent-exploration-mode-parallel-codebase-mappi"
  - "claude-code-max-plan-subsidy-vs-api-cost-tool"
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "orchestration"
  - "architecture"
contract:
  preconditions: "Agent system design phase; topology not yet committed; harness-spectrum position is a deliberate decision, not a default"
  invariants: "Architecture choices traceable to task requirements; every agent decomposable into four zones (trigger, context, tools, output); harness-determinism position chosen against an explicit reliability requirement; specialized-harness investments classified as bets or shims; sub-agent dispatch treated as a uniform tool interface"
  governance: "IL-owned draft; Nick deploys"
  recovery: "If architecture shows specialization theater symptoms, revisit single-agent default. If specialized harness brittleness blocks real-world inputs, reconsider spectrum position. If sub-agent wiring failures accumulate, add post-wave integration verification."
---

# Agent Architecture Decisions

Should you use one agent or many? How should they coordinate? Which model should each use? How permanent is the infrastructure you are building?

This guide provides empirically-grounded decision frameworks for agent system topology -- from the single-agent default through legitimate multi-agent domains to composition patterns, sub-agent orchestration primitives, model routing, and infrastructure longevity assessment. It covers the "what" of agent architecture: what topology to choose, what boundaries to draw, what models to assign, and where on the harness-determinism spectrum to position. For the "how" -- running agents in production with workflow engines, observability, cost management, and failure handling -- see *Agent Workflow and Execution* (G3b).

## When to Use This Guide

- You are designing a new agent system and choosing between single-agent and multi-agent.
- You have a multi-agent system that underperforms and want to evaluate whether the architecture is the problem.
- You are adding a new agent to an existing system and need to decide how to integrate it.
- You are choosing which model to assign to which agent role.
- You are auditing existing infrastructure for lock-in risk or layer impermanence.
- You are evaluating whether your multi-agent system needs a central orchestrator or whether room-based peer-to-peer coordination (Pattern F) is a better fit.
- You are defining human control points in boundary contracts and need to classify which steps require observe, approve, or cancel semantics (AGUI).
- You are designing sub-agent dispatch mechanics and need to decide between execution topologies (sub-agent-per-task vs. inline batch).
- You are positioning on the harness-determinism spectrum and need to evaluate prompt-driven vs. generic vs. specialized.

**Do not use for:** specifying what an agent does (see *Writing Agent Specifications*, G1), managing context within an agent (see *Managing Agent Context*, G2), running agents in production (see *Agent Workflow and Execution*, G3b), or evaluating agent output quality (see *Building Agent Evaluation Suites*, G4).

## Key Concepts

**1. Single agent is the default (L > D).** Information loss across agent boundaries (L) typically exceeds context degradation from long context within a single agent (D). Multi-agent swarms degrade sequential tasks by 39-70%. Independent agents amplify errors 17.2x versus centralized coordination at 4.4x. Start with one agent and only split when you have empirical evidence that splitting helps.

**2. The 45% saturation threshold.** Multi-agent coordination yields diminishing or negative returns once a single agent exceeds ~45% baseline performance. Past this point, invest in making the single agent better -- better context, better specs, better tooling -- rather than adding agents.

**3. Decompose by task characteristics, not roles.** Agent "teams" that mirror human organizational structure (engineer, QA, PM) are specialization theater -- they add cost and complexity without improving outcomes. The correct decomposition criteria are parallelizability, information flow dependencies, and error sensitivity.

**4. Contracts at every boundary.** Without explicit input/output schemas, quality constraints, and tool permissions at every agent boundary, agents negotiate interfaces in natural language -- introducing ambiguity, drift, and hallucination that compounds across boundaries.

**5. Infrastructure is impermanent -- plan for it.** Current agent infrastructure layers (retrieval pipelines, heavy prompt scaffolding, verification gates) will be progressively absorbed by model-native capabilities. Classify each dependency as an architectural bet or a transitional shim, and design for easy removal.

**6. Rooms are a coordination boundary, not a UI feature.** In room-based multi-agent systems, the room is the bounded context: agents coordinate peer-to-peer via @mentions without a central orchestrator. This is categorically different from orchestrator→worker delegation (Patterns A-E). The design question is: "What is the natural bounded context for this set of agents?"

**7. Human control points are a contract field, not an afterthought.** The AG-UI protocol (AGUI) encodes where humans must observe, approve, edit, or cancel running agent work. Alongside MCP (agent-to-resource) and A2A (agent-to-agent), AGUI completes the core protocol stack for production systems. Every boundary contract should include a `human_control_points` definition.

**8. Harnesses lie on a determinism spectrum -- choose position deliberately.** Agent systems sit somewhere between "entirely LLM-initiated via prompts" and "mostly deterministic with code-wired workflows." The position is not a default -- it is a decision tied to a reliability requirement.

**9. Every agent is four zones.** Regardless of tool or framework, every agent decomposes into: trigger (what wakes it), context (what is injected per turn), tools (what it can interact with), and output/memory (where work goes and how state persists). Debugging is systematic -- a broken agent has a broken zone. A well-designed spec covers all four zones; an opaque framework hides them.

**10. Sub-agent dispatch is a tool call, not a special mechanism.** Sub-agents should be dispatched through the same interface as any other tool -- same hooks, same logging, same permission checks. Interface homogeneity means hooks work for free, the tool registry is the single source of capabilities, and sub-agent calls can be mocked like any other tool. Frameworks that give delegation its own API surface add complexity that the uniform interface avoids.

**11. Harness engineering is the third evolution.** The progression from prompt engineering (single LLM, single output) to context engineering (single agent, curated context) to harness engineering (multiple agent sessions, orchestrated workflow) represents maturation of AI development. 40% of Claude Code's codebase is harness infrastructure. Each evolution builds on the previous -- harness engineering requires good context engineering at each node.

---

## Procedure

### Step 1: Measure the Single-Agent Baseline

Before designing any architecture, establish what one agent can do.

1. Run the task with a single well-configured agent (appropriate model, good context, clear spec).
2. Measure baseline performance against your acceptance criteria.
3. If baseline exceeds 45%, **stop**. Invest in improving context, tooling, and specification rather than adding agents.
4. If baseline is below 45%, proceed to Step 2 to evaluate whether the task characteristics justify multi-agent.

The 45% threshold is conservative -- the actual breakeven varies by task. But the principle is empirically robust: coordination overhead (information loss at boundaries, handoff costs, error amplification) almost always exceeds the marginal benefit of additional agents past this point.

### Step 2: Evaluate Task Characteristics

Use this decision tree to determine whether multi-agent architecture is justified:

```
Is the task parallelizable?
├── YES: Can subtasks run independently without sharing context?
│   ├── YES: Is information loss between agents acceptable?
│   │   ├── YES → Multi-agent justified (legitimate domain)
│   │   └── NO → Single agent with sequential execution
│   └── NO: Do subtasks have dependencies?
│       └── YES → Single agent (sequential reasoning degrades 39-70% when split)
└── NO: Is the task sequential?
    └── YES → Single agent (always)
```

**Four legitimate multi-agent domains** (parallelizable, lossy-tolerant):

| Domain | Why Multi-Agent Works | Example |
|--------|----------------------|---------|
| **Research** | Many sources processed independently; irrelevant results discarded | Processing 20 URLs through parallel extractors |
| **Debugging** | Multiple hypotheses tried in parallel; validated empirically | Testing 5 fix approaches simultaneously |
| **Mechanical operations** | No context dependency between units of work | Batch file renames, format conversions |
| **Review** | Fresh perspective is a feature; not having full history avoids anchoring bias | Independent code review, verification |

**Harmful domains** (sequential, context-dependent):

| Domain | Why Multi-Agent Hurts | What to Do Instead |
|--------|----------------------|-------------------|
| **Implementation** | Decisions in file A affect file B; 39-70% degradation | Single agent with full codebase context |
| **Planning** | Step dependencies require full context of previous decisions | Single agent with structured output |
| **Integration** | Connecting components requires understanding both sides | Single agent with broader context window |

**The specialization theater test:** For any proposed multi-agent decomposition, ask: "Is this decomposition based on task characteristics or on familiar human roles?" If the decomposition mirrors an org chart (engineer, QA, PM, designer), it is theater. If it is based on parallelizability, isolation requirements, or human gate needs, it may be justified.

**The agent sprawl test:** Draw the parallel to microservices circa 2018. If you cannot answer these five questions, you are sprawling: (1) Can you list every agent and its scope? (2) Do you have observability over what each agent is doing? (3) Is there coordination infrastructure for parallel agent work? (4) Do you have standard failure/recovery patterns? (5) Do you know cost-per-successful-task for each agent?

**The four-zone audit:** Before deciding on architecture, confirm that each proposed agent's four zones are well-defined. If you cannot specify the trigger, context, tools, and output/memory for an agent, it is under-designed. This audit also exposes framework opacity -- opaque platforms that hide zones from the developer make debugging impossible.

**Error-aware backtracking.** For long-horizon workflows where compound errors are a concern (90% per-step accuracy on 10 steps = 35% overall), design agents that can backtrack to a decision point and try a different branch rather than continuing on a corrupt path. Checkpoint-based backtracking (save state at each decision point) is more practical than undo chains. Confidence-gated progression (don't advance to step N+1 until step N passes a threshold) prevents silent error propagation.

### Step 3: Choose a Composition Pattern

If multi-agent is justified, select the appropriate pattern based on your coordination needs.

#### Pattern A: Parallel Worktree Isolation

For independent tasks that can run concurrently without shared context.

```
[Operator (human)]
├── Terminal 1: claude -w "task A"  →  worktree A (branch-a)
├── Terminal 2: claude -w "task B"  →  worktree B (branch-b)
└── Terminal 3: claude -w "task C"  →  worktree C (branch-c)
```

**When to use:** 3-5 independent tasks that do not share files or context. Filesystem-level isolation via git worktrees prevents cross-contamination. Human coordinates and merges results. Also works with parallel Claude Code instances in different workspace folders -- each instance reads only its own workspace context, with cross-workspace file transfer done explicitly.

**Limits:** Human attention bottleneck at 5+ sessions. No inter-session communication -- if tasks are actually dependent, the operator must relay context manually. Merge conflicts when worktrees modify overlapping files.

#### Pattern B: Advisor-Executor (Dynamic Consultation)

For tasks where a cheaper model handles most work but occasionally needs guidance from a stronger model.

```
[Executor (Sonnet)]  ←→  [Advisor (Opus)]
   handles tools          reasoning guidance
   most decisions         consulted as needed
   cheaper per call       full shared context
```

**When to use:** API-based applications where you want Opus-quality decisions at Sonnet-level cost. Benchmarks: SWE-Bench 74.8 (with advisor) vs 72.1 (Sonnet alone) at ~50% lower cost ($0.96 vs $1.89 per task). The `max_uses` parameter controls advisory consultations per task -- set too low and the executor makes bad decisions; set too high and you pay for unnecessary consultations.

**Key distinction from planner-executor:** This is not a one-shot plan followed by execution. It is an ongoing dynamic relationship where the executor consults the advisor at decision points throughout the task.

#### Pattern C: Fan-Out / Fan-In Exploration

For problems that benefit from multiple perspectives before committing to a plan.

```
                    ┌── [Architecture Analyzer]
[Problem] ──fan-out─┼── [File Identifier]        ──fan-in── [Synthesized Plan]
                    ├── [Risk Detector]
                    └── [Critique Pass]
```

**When to use:** Complex planning where single-agent analysis misses perspectives. Claude Code's deep plan mode implements this natively. Each sub-agent analyzes the problem from a different angle, then outputs are synthesized into a unified plan.

**Limits:** Token cost scales linearly with agent count. Conflicting recommendations from different agents need a clear resolution strategy. Over-exploration delays execution.

#### Pattern D: Shared Communication Channel

For multi-agent work where subtasks have real-time interdependencies.

```
[Orchestrator]
├── [Agent A] ←──shared channel──→ [Agent B]
│   frontend                        backend
└── Channel monitors for deadlock / noise
```

**When to use:** When isolated sub-agents plus orchestrator breaks down because agents have real-time interdependencies (e.g., frontend and backend negotiating API contracts). The shared channel lets agents resolve interdependencies directly rather than routing everything through the orchestrator.

**Limits:** Channel noise consumes tokens without adding value. Circular dependency risk (A waits on B waits on A). Channel content loaded into each agent's context accelerates degradation.

#### Pattern E: Brain-Hands Decoupling

For systems that need independent scaling, failure isolation, or many-to-many topology.

```
[Brain (LLM + harness)] ──execute(name, input) → string──→ [Hand (sandbox/tool/MCP)]
   stateless, scalable                                       independently provisioned
   can connect to many hands                                 crash = tool error, not session end
```

**When to use:** Production systems where you need brains and execution environments to scale independently. Lazy sandbox provisioning drops p50 TTFT by ~60% and p95 by >90%. Sandbox crashes are treated as tool errors, not session-ending failures.

**Key insight:** The uniform `execute(name, input) -> string` interface means the brain does not care what the hand is -- container, phone, emulator, MCP server, or custom tool.

#### Pattern F: Room-Based Peer-to-Peer Coordination

For multi-agent work where peer-to-peer coordination is preferable to a central orchestrator, and where human observers need real-time visibility into agent work.

```
[Room: bounded context]
├── [Agent A] ──@mention──→ [Agent B]
│   produces: PR          produces: plan
├── [Agent C] ──@mention──→ [Agent A]
│   produces: docs         reviews: PR
└── [Human observer] (real-time SSE stream of agent activity)
    per-room kanban task board visible to all participants
```

**When to use:** Complex collaborative tasks where multiple agents need to negotiate directly without routing every message through a central orchestrator. The room defines the bounded context: agents assigned to a room communicate via @mentions over Server-Sent Events (SSE), self-manage a per-room kanban, and produce typed artifacts.

**Key distinction from Pattern D:** Pattern D routes interdependencies through a channel monitored by an orchestrator. Pattern F is structurally orchestrator-free -- agents coordinate as peers within the room boundary.

**Limits:** Room scope must be bounded deliberately; a room that grows too large collapses back into Pattern D dynamics. @mention routing becomes complex when agents within a room form dependencies that span multiple concurrent rooms.

#### Pattern G: Wave-Based Sub-Agent Orchestration

For batch execution of many independent tasks with validation between waves.

```
[Orchestrator]
├── Wave 1: [Sub-agent 1] [Sub-agent 2] ... [Sub-agent N]  → Validate
├── Wave 2: [Sub-agent N+1] ... [Sub-agent 2N]             → Validate
└── Wave 3: ...                                             → Final check
```

**When to use:** Processing large backlogs of independent tasks (IB queues, batch analysis, parallel file operations). Each wave launches up to 15 parallel sub-agents with fresh context windows. Between waves, a validation step checks system state before the next wave begins -- preventing compounding errors from cascading.

**Key principles:**
- **One task per sub-agent.** Fresh context dedicated to a single problem produces dramatically better output than one agent handling many tasks.
- **Wiring verification after each wave.** Sub-agents frequently complete their task but fail to integrate output with the rest of the system, leaving "isolated islands." Explicit integration checks after each wave catch this.
- **Context isolation enables model tiering.** The orchestrator uses an expensive model for planning and aggregation; sub-agents use a cheaper model for narrow tasks. In production, this means 7K orchestrator tokens vs 323K total sub-agent tokens -- the harness makes cost control tractable.

**Limits:** Spawning too many parallel agents can overwhelm MCP connections. Without tight validation criteria, waves can proceed on corrupted state. The one-task-per-agent principle means wave count grows linearly with task count.

#### Pattern H: Review-Triggered Remediation Chain

For workflows where an evaluation step automatically chains into fix dispatch.

```
[Implementation] → [Review Skill] → classify(critical/important/info)
                                      ├── critical → [Fix Sub-Agent 1] → verify
                                      ├── important → [Fix Sub-Agent 2] → verify
                                      └── info → defer to human
```

**When to use:** When review findings should chain directly into automated remediation rather than sitting in a report for human triage. The review skill identifies issues, classifies severity, and dispatches a fresh fix sub-agent per issue. The fix agent gets only the issue description and relevant code -- minimal context, maximum focus.

**Generalizable composition primitive:** Any evaluation step that produces a structured issue list can chain into a dispatch queue. This applies beyond code review: spec compliance → fix non-compliant sections, security review → fix vulnerabilities, test failure analysis → fix failing tests.

**Limits:** Fix agents may introduce new bugs due to narrow context. Severity misclassification wastes tokens. Parallel fix dispatch on the same file creates conflicts.

### Step 3b: Select Execution Topology

After choosing a composition pattern, decide how the plan executes. This is a runtime parameter, not an architectural constant.

| Topology | When to use | Tradeoff |
|----------|-------------|----------|
| **Sub-agent per task** | Complex tasks, context isolation matters, human review between tasks | Higher token cost, slower, better isolation |
| **Inline batch** | Simple tasks, trust the plan, context from previous tasks helps | Faster, cheaper, context rot risk |
| **Hybrid** | Mixed complexity plan | Some tasks inline, high-risk tasks via sub-agent |

**The plan should be topology-agnostic.** A well-designed plan specifies WHAT (tasks, acceptance criteria) but not HOW the execution engine dispatches them. The topology is an orthogonal concern selected at runtime based on project shape, risk tolerance, and human availability.

**Shared-session vs. artifact-only handoff.** Two orchestration models exist in tension:

- **Shared-session orchestrator:** A single persistent session carries accumulated context across all phase invocations (brainstorm → plan → execute → review). Conversational context, user preferences, and design rationale persist without serialization. Tradeoff: richness of inter-phase context vs. context rot on long sessions.
- **Artifact-only handoff:** Each phase gets a fresh context window and reads inter-phase state exclusively from files. Tradeoff: crash-resilient and context-fresh, but conversational nuance and informal design rationale get lost at phase boundaries.

Neither is universally better. Use shared-session for brainstorm-to-plan (where conversational context matters most) and artifact-only for execute-to-review (where fresh context matters more). The critical design decision is where to draw the session boundary.

### Step 4: Define Contracts at Every Boundary

Every interaction between agents gets an explicit contract:

| Contract Component | What to Define |
|-------------------|---------------|
| Input schema | Structure, types, required fields |
| Output schema | Structure, types, required fields |
| Quality constraints | Must-constraints (reject) and should-constraints (warn) |
| Cost/latency budgets | Maximum tokens, wall-clock time, API calls |
| Allowed tools | Explicit allowlist per agent role |
| Degradation mode | What happens when the agent fails or exceeds budget |
| `human_control_points` | Observe / approve-before-proceed / cancellable per step |

Without contracts, agents negotiate interfaces in natural language -- introducing ambiguity, drift, and hallucination at every boundary. Validate contracts at runtime, not just in documentation.

**Agent type enforcement:** Consider a formal type system where each role (Explore, Plan, Verify, Execute) has its own allowed tool set and explicit behavioral constraints. An Explore agent that physically cannot edit files eliminates an entire class of errors. Claude Code implements six built-in types; you can define custom types per project.

**Sub-agent dispatch as tool call.** Implement sub-agent dispatch as a standard entry in the tool registry -- called identically to bash, file-read, or web-search. This ensures hooks, logging, and permission checks work on sub-agent calls without modification. The tool registry becomes the single source of capabilities. Frameworks that give delegation its own API surface add complexity that the uniform interface avoids.

**Cross-organizational boundaries:** For agents that delegate across organizational boundaries, the A2A protocol (Google, Linux Foundation, 50+ enterprise partners) defines Agent Cards (`/.well-known/agent.json`) with capability declarations, authentication requirements, and a six-state task lifecycle (`submitted -> working -> input-required -> completed -> failed -> cancelled`). MCP handles agent-to-resource; A2A handles agent-to-agent; AGUI handles human-to-agent.

**AGUI supervision debt.** Teams that skip human control point definitions accumulate "supervision debt" -- the aggregate cost of missed human intervention opportunities that compounds into downstream errors and trust failures. When defining each boundary contract, add a `human_control_points` field listing which steps are observe-only, which require approval before proceeding, and which can be cancelled mid-execution.

### Step 5: Select Models for Each Role

Use task characteristics to route to the appropriate model:

| Task Type | Recommended Model | Key Evidence |
|-----------|------------------|--------------|
| Repository-level coding, knowledge work | Claude Sonnet 4.6 | SWE-bench ~79.6%, GDPval Elo 1633 |
| Complex reasoning, architectural decisions | Claude Opus 4.6 | Reserved for decisions where quality premium justifies 3.5x cost |
| Computer use, browser automation | GPT-5.4 | WebArena-Verified 67.3% |
| Abstract reasoning, long-horizon math | Gemini 3.1 Pro | ARC-AGI-2 77.1% |
| Extraction, batch processing | Gemini Flash | $0.003/task, 97.1% quality |
| Orchestrator (planning, aggregation) | Premium model (Opus/Pro) | Orchestration quality justifies cost; sub-agents absorb volume |
| Sub-agent (narrow, well-defined tasks) | Cheap/fast model (Sonnet/Flash) | Sub-task requirements are within smaller model capability |

**Model-tier routing principle:** Use a premium model for orchestration (user interaction, planning, aggregation) and a cheaper/faster model for narrow sub-agent tasks. This makes parallel sub-agent architectures economically viable at scale. In production, one harness consumed 7K orchestrator tokens vs. 323K total sub-agent tokens -- model tiering kept the cost tractable.

**Subscription vs. API economics.** Claude Code Max plan ($200/month) provides effectively $2,500-$5,000 in subsidized API-equivalent usage. Any tool that requires bypassing Max (using API credentials directly) faces a 12.5-25x cost headwind. For tool selection decisions, the correct question is "does this tool provide enough incremental value to justify API costs vs. the Max plan subsidy?"

**Per-node model selection:** In YAML-defined workflow DAGs (Archon pattern), assign models per workflow node -- Haiku for classification, Sonnet for implementation, Opus for planning. This prevents the anti-pattern of running the most expensive model for every step.

**Benchmarks are snapshots.** This table reflects March 2026 data. Five major model releases occurred in a 23-day window (March 3-22, 2026), compressing the competitive gap between labs from months to weeks. The routing structure (task-based, not provider-based) remains valid even when specific model recommendations change. Establish a monthly review cadence for model routing tables.

### Step 6: Assess Infrastructure Longevity

Before investing in infrastructure, audit each layer for impermanence and lock-in risk.

**Seven infrastructure layers** (from most to least mature):

| Layer | Examples | Maturity | Risk |
|-------|----------|----------|------|
| 1. Compute & Sandboxing | E2B, Daytona | Mature | Low |
| 2. Identity & Communication | Email-as-identity, A2A | Shim-heavy | High migration cost |
| 3. Memory & State | Mem0, session persistence | Emerging | Platform risk |
| 4. Tools & Integration | MCP, Compose.io | Maturing | MCP may absorb managed layers |
| 5. Provisioning & Billing | Stripe Projects | Emerging | Gaps in agent-native billing |
| 6. Orchestration & Coordination | Missing | Biggest gap | No standard exists |
| 7. Human Control Surface | AGUI | Maturing standard | Supervision debt if skipped |

**Reliability compounds across layers.** When an agent depends on five different infrastructure layers, end-to-end reliability is the product of each layer's reliability. Five layers at 99% each = 95% system reliability. Five layers at 97% each = 86%.

**Four-question impermanence audit:**

1. Am I over-specifying *how* instead of *what/why*? (Outcome specs outlast process specs)
2. Is my retrieval rigid or dynamic? (Hardcoded RAG pipelines are fragile)
3. Am I injecting knowledge the model already scales to learn? (Block cut 50-60% of plumbing with this lens)
4. Can model-native checks replace my verification gates?

**Three-question lock-in assessment** for every dependency:

1. Is this a pragmatic bet or an architectural bet?
2. What is the migration cost when a native protocol arrives?
3. Am I willing to swap this out within 12-18 months?

**The bitter lesson for agents:** Bigger models demand simplification, not more scaffolding. Teams investing in complex RAG, prompt chains, and verification gates risk building on sand. Safety infrastructure (security, permissions, audit trails) should never be simplified away -- the bitter lesson applies to intelligence tasks, not safety constraints.

**Specialized harnesses are deliberate bets against this lesson.** Step 8 introduces the harness determinism spectrum, where specialized harnesses deliver reliability the model alone can't yet provide. Both Step 6 and Step 8 can be correct simultaneously: don't over-build scaffolding the model will absorb, *and* if your reliability requirement is unmet, build the scaffolding anyway with a planned review trigger.

### Step 7: Build the Infrastructure Layer

Production agent systems need infrastructure beyond the model. Audit against this three-tier checklist:

| Tier | Primitives | Status Check |
|------|-----------|-------------|
| **1: Tools & Permissions** | Tool registry with metadata, permission tiers per tool, security boundaries | Can you list every tool available to each agent role? |
| **2: Persistence & Execution** | Session state persistence (crash-resilient), budget tracking, workflow state machine | Can your agent recover from a crash mid-task? |
| **3: Observability & Verification** | Structured event logging, multi-layer verification, failure recovery with rollback | Can you trace what the agent did and verify it was correct? |

**Agents are 80% infrastructure, 20% model.** Anthropic's Claude Code invests 80% of its 512K-line TypeScript codebase in infrastructure. Most teams build the model layer and skip the plumbing -- then hit scaling walls when they cannot debug, recover from crashes, or control costs.

**Skills as infrastructure.** Skills are markdown files that encode a complete workflow process -- the steps, tools, format, and preferences from a successful manual run. Once created, invoking the skill by name reproduces the full process without re-explaining it. BMAD Method v6.1.0 migrated all 68 workflows from YAML/XML to skills-as-markdown, achieving a 91% package size reduction (533 to 348 files, 6.2MB to 555KB). Every repeated process in a workflow is a candidate for a skill.

**Remote orchestration infrastructure.** Claude Dispatch creates a communication bridge between a mobile app and a local desktop agent. The user sends commands from their phone; the local machine executes using locally-configured skills and MCP connectors; results report back asynchronously. This enables remote trigger of skills, multi-task parallelism, and asynchronous result delivery without exposing credentials to third-party services.

For detailed guidance on implementing each tier in production -- workflow engines, observability, cost management, and degradation modes -- see *Agent Workflow and Execution* (G3b).

### Step 8: Position on the Harness Spectrum

Once topology, contracts, models, and infrastructure tiers are decided, decide *how much of the workflow is prompt-driven vs. wired together in code*. This is the harness-determinism axis -- orthogonal to topology (Step 3) and to layer impermanence (Step 6). Three zones:

| Zone | What it looks like | Reliability | Engineering cost | Brittleness | Examples |
|------|--------------------|-------------|------------------|-------------|----------|
| **Prompt-driven** | The agent decides phase transitions, output shape, and sub-task routing in the prompt. The "harness" is conversation + tool calls. | Variable | Low | Low (model upgrades absorb improvements) | Vanilla chat, Manus, ad-hoc Claude Code sessions |
| **Generic harness** | Reusable scaffolding (skills, hooks, slash commands) that runs across many tasks. Phase transitions and tool permissions are codified but the agent still decides most steps. | Higher | Medium (amortized) | Medium | Claude Code (the harness), GSD, Cursor's agent mode |
| **Specialized harness** | Purpose-built code wraps LLM calls with explicit phase gates, structured output schemas, sub-agent delegation, persistent state, and model-tier routing. Each phase is a function with validation. | Highest (determinism by construction) | High | High (rigid schemas break on real-world drift) | Stripe's PR validator (1,300 PRs/week), contract-review harness, Archon YAML DAGs |

**The harness engineering evolution.** This spectrum reflects a broader maturation: prompt engineering (2022-2024, single LLM output) → context engineering (2024-2025, single agent, curated context window) → harness engineering (2025-2026, multiple agent sessions, orchestrated workflow). Each evolution builds on the previous. Harness engineering requires good context engineering at each node -- a harness that wraps poorly contexted agents just produces bad output faster.

**Specialized-harness primitives** (when you commit to that zone):

- **Phase-gating.** Phase N+1 only proceeds after Phase N output passes validation. State transitions are explicit, not emergent.
- **Structured output schemas at every phase.** Each phase produces validated JSON or equivalent, not free text. Downstream phases consume by schema, not by parsing.
- **Sub-agent delegation per unit.** Each independent unit of work gets its own LLM call with fresh context. Prevents context pollution at the unit level.
- **State management via a database.** A `harness_runs` table tracks current phase, status, outputs. Crashes restart from the last successful phase.
- **Virtual file system / scratch pad.** Every phase writes its output as a file. The full run is replayable and auditable.
- **Model tier routing.** Expensive orchestrator model for main reasoning; cheap fast model for sub-agent extraction.

**Autonomous execution loops.** At the specialized end of the spectrum, fully autonomous loops run on fixed intervals (e.g., cron-triggered) without human involvement. Each cycle: read prior results → generate challenger variant → deploy both → measure → harvest winner → append learnings. The human sets the initial baseline and metric definition; the loop runs continuously. Requires a clear objective metric as feedback signal. Applies to A/B testing, ad optimization, content generation, pricing experiments, and any domain with a measurable outcome and fast feedback loop.

**When to invest in a specialized harness:**

| Trigger | What it tells you |
|---------|-------------------|
| Single-agent baseline below 45% **and** task is repeated production work | You can't fix it with better prompts; the variance has to be engineered out. |
| Cost-of-failure is high (financial, safety, compliance) | Determinism is a feature buyers pay for. |
| Task structure is genuinely phase-decomposable | If the work has natural phases, the harness adds clarity. If it's exploratory, the harness will fight the work. |
| You will run this workflow >100 times | Engineering cost amortizes. Below ~100 runs, generic harness is usually enough. |

**When *not* to invest:**

- The task runs <10 times. Generic harness is cheaper end-to-end.
- The model is improving fast enough that next-generation will absorb your scaffolding.
- The task is exploratory and the right phase decomposition isn't yet known.
- The cost of failure is low. Variance is acceptable; reliability investment isn't.

**Migration paths between zones:**

- Prompt-driven → Generic: codify recurring conventions into skills, hooks, or slash commands. Reusability is the trigger.
- Generic → Specialized: when conventions stop catching the failures, and the failures cost real money or trust. Phase-gate the most failure-prone transition first; expand from there.
- Specialized → Generic (reverse migration): when the next model generation makes one of the harness's deterministic checks redundant, retire that check. Keep the harness; shrink its surface.

---

## Templates

### Architecture Decision Record

```markdown
## Agent Architecture Decision -- {{SYSTEM_NAME}}

### Task Analysis
- Task description: {{TASK}}
- Single-agent baseline performance: {{BASELINE_PERCENT}}%
- Parallelizable: {{YES/NO}} -- {{PARALLELISM_RATIONALE}}
- Information flow: {{INDEPENDENT/DEPENDENT/MIXED}}
- Error sensitivity: {{LOW/MED/HIGH}} -- cascading: {{YES/NO}}

### Four-Zone Audit
| Agent | Trigger | Context | Tools | Output/Memory |
|-------|---------|---------|-------|---------------|
| {{AGENT_1}} | {{TRIGGER}} | {{CONTEXT}} | {{TOOLS}} | {{OUTPUT}} |
| {{AGENT_2}} | {{TRIGGER}} | {{CONTEXT}} | {{TOOLS}} | {{OUTPUT}} |

### Specialization Theater Check
- Is decomposition based on task characteristics? {{YES/NO}}
- Does decomposition mirror org chart roles? {{YES/NO}} -- if yes, STOP
- Agent sprawl check: can I list all agents, their scopes, and cost-per-task? {{YES/NO}}

### Decision
- Architecture: {{SINGLE/MULTI}} agent
- Justification: {{WHY}} (must reference task characteristics, not roles)
- If multi-agent:
  - Pattern: {{A_WORKTREE/B_ADVISOR/C_FAN_OUT/D_CHANNEL/E_BRAIN_HANDS/F_ROOM/G_WAVE/H_REVIEW_CHAIN/CUSTOM}}
  - Execution topology: {{SUB_AGENT_PER_TASK/INLINE_BATCH/HYBRID}}
  - Agent count: {{N}} -- each justified by: {{REASON_PER_AGENT}}
  - Contracts defined: {{YES/NO}}
  - Sub-agent dispatch via uniform tool interface: {{YES/NO}}
  - Human control points defined (AGUI): {{YES/NO}}
  - Room boundaries defined (if Pattern F): {{YES/NO}}
  - Type enforcement: {{YES/NO}} -- tool allowlists per role

### Model Routing
| Agent Role | Model Tier | Model | Rationale |
|------------|-----------|-------|-----------|
| Orchestrator | Premium | {{MODEL}} | {{WHY}} |
| {{SUB_ROLE}} | Cheap/fast | {{MODEL}} | {{WHY}} |

### Harness Position
- Zone: {{PROMPT_DRIVEN/GENERIC/SPECIALIZED}}
- Classification: {{BET/SHIM}} (intended life: {{N}} model generations)
- Review trigger: {{WHEN_TO_RECONSIDER}}

### Infrastructure Assessment
- [ ] Tier 1: Tool registry and permissions defined
- [ ] Tier 2: Session persistence and workflow state machine
- [ ] Tier 3: Event logging and verification
- [ ] Contracts validated at runtime (not documentation-only)
- [ ] Impermanence audit: layers classified as bet vs shim
- [ ] Lock-in assessment: migration cost estimated per dependency

### Risk Assessment
- Coordination overhead: {{ESTIMATE}}
- Information loss at boundaries: {{ACCEPTABLE/UNACCEPTABLE}}
- Reliability compounding: {{N}} layers x {{RELIABILITY}}% = {{SYSTEM_RELIABILITY}}%
- Fallback: if multi-agent underperforms, collapse to {{FALLBACK}}
```

**Variable Reference:**

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `SYSTEM_NAME` | string | Yes | System being designed |
| `TASK` | string | Yes | What the agent system will do |
| `BASELINE_PERCENT` | number | Yes | Single-agent performance on acceptance criteria |
| `PARALLELISM_RATIONALE` | string | Yes | Why the task is or is not parallelizable |
| `FALLBACK` | string | Yes | What to collapse to if multi-agent underperforms |

### Pre-Spawn Checklist

Before adding a new agent to an existing system:

```markdown
## Pre-Spawn Checklist -- {{NEW_AGENT_NAME}}

1. [ ] Single-agent baseline measured: {{PERCENT}}%
2. [ ] Baseline exceeds 45%? If yes, STOP -- improve the existing agent instead
3. [ ] Task is parallelizable? {{YES/NO}}
4. [ ] Information loss at boundary is acceptable? {{YES/NO}}
5. [ ] Decomposition is based on task characteristics, not roles? {{YES/NO}}
6. [ ] Contract defined for the new boundary? {{YES/NO}}
7. [ ] Four zones defined (trigger/context/tools/output)? {{YES/NO}}
8. [ ] Sub-agent dispatch via uniform tool interface? {{YES/NO}}
9. [ ] Agent type defined with tool allowlist? {{YES/NO}}
10. [ ] Model selected based on task-type and tier routing? {{MODEL_TIER}}: {{MODEL}}
11. [ ] Sprawl check passed (scope, observability, cost known)? {{YES/NO}}
12. [ ] Infrastructure layer dependencies classified (bet vs shim)? {{YES/NO}}
13. [ ] Human control points defined for the new boundary (AGUI)? {{OBSERVE/APPROVE/CANCEL}} at step {{STEP}}
14. [ ] Fallback plan if new agent degrades system performance? {{PLAN}}

If any answer is NO for items 3-6, do not spawn the agent.
```

### Infrastructure Longevity Audit

```markdown
## Infrastructure Longevity Audit -- {{SYSTEM_NAME}}

### Layer Assessment
| Layer | Current Solution | Classification | Migration Cost | Native Alternative ETA |
|-------|-----------------|----------------|---------------|----------------------|
| Compute & Sandboxing | {{SOLUTION}} | {{BET/SHIM}} | {{LOW/MED/HIGH}} | {{MONTHS}} |
| Identity & Communication | {{SOLUTION}} | {{BET/SHIM}} | {{LOW/MED/HIGH}} | {{MONTHS}} |
| Memory & State | {{SOLUTION}} | {{BET/SHIM}} | {{LOW/MED/HIGH}} | {{MONTHS}} |
| Tools & Integration | {{SOLUTION}} | {{BET/SHIM}} | {{LOW/MED/HIGH}} | {{MONTHS}} |
| Provisioning & Billing | {{SOLUTION}} | {{BET/SHIM}} | {{LOW/MED/HIGH}} | {{MONTHS}} |
| Orchestration & Coordination | {{SOLUTION}} | {{BET/SHIM}} | {{LOW/MED/HIGH}} | {{MONTHS}} |
| Human Control Surface (AGUI) | {{SOLUTION}} | {{BET/SHIM}} | {{LOW/MED/HIGH}} | {{MONTHS}} |

### Harness Spectrum Position
- Current zone: {{PROMPT_DRIVEN/GENERIC/SPECIALIZED}}
- Harness evolution stage: {{PROMPT_ENG/CONTEXT_ENG/HARNESS_ENG}}
- Classification: {{BET/SHIM}} -- intended life: {{GENERATIONS}} model generations
- Review trigger: {{CONDITION}}

### Impermanence Audit
1. Over-specifying how instead of what/why? {{YES/NO}} -- {{DETAILS}}
2. Retrieval rigid or dynamic? {{RIGID/DYNAMIC}} -- {{DETAILS}}
3. Injecting knowledge the model scales to learn? {{YES/NO}} -- {{DETAILS}}
4. Verification gates replaceable by model-native checks? {{YES/NO}} -- {{DETAILS}}

### Reliability Calculation
- Total layers depended on: {{N}}
- Per-layer reliability: {{PERCENT}}%
- System reliability: {{PRODUCT}}%
- Acceptable? {{YES/NO}}
```

---

## Worked Example: MetaSystem Research Pipeline

How MetaSystem's Improvement Loop applies these architecture decisions.

```
Architecture Decision -- Improvement Loop Research Pipeline

TASK ANALYSIS:
- Task: Extract findings from 20+ research sources per session
- Single-agent baseline: ~30% throughput (sequential processing
  takes 4+ hours for 20 sources -- agent context degrades)
- Parallelizable: YES -- each source is independent
- Information flow: INDEPENDENT -- finding from source A doesn't
  affect extraction from source B
- Error sensitivity: LOW -- a bad extraction is caught at human
  gate, doesn't cascade

FOUR-ZONE AUDIT:
| Agent | Trigger | Context | Tools | Output/Memory |
|-------|---------|---------|-------|---------------|
| Orchestrator | /research-loop invocation | CLAUDE.md + IL PROGRESS.md + dimension registry | Read, Write, Grep, Glob, Agent | Delta report, PROGRESS.md |
| Extractor (sub) | Orchestrator dispatch | Source URL + finding template + KB context | Read, Write, WebFetch, Perplexity | Finding files with frontmatter |

SPECIALIZATION THEATER CHECK:
- Decomposition based on task characteristics? YES -- parallelizable
  independent source processing
- Mirrors org chart? NO -- not "researcher + editor + reviewer";
  it's "N independent extractor sub-agents"
- Sprawl check: 4-6 parallel extractors, scoped to one source each,
  cost = Sonnet per source

DECISION: Multi-agent (parallel extraction)
- Pattern: G (wave-based) -- subagents per batch with validation
- Execution topology: sub-agent-per-task
- Agent count: 4-6 parallel Sonnet subagents per batch
- Justification: Research is a legitimate multi-agent domain --
  parallelizable, lossy-tolerant, independent sources
- Each subagent gets: one source + finding template + KB context
- Sub-agent dispatch via uniform tool interface: YES -- Agent tool

SEQUENTIAL STEPS (single agent):
- /identify-artifacts -- classification requires full KB context,
  cross-finding comparison. Sequential, context-dependent. SINGLE.
- /synthesize-guide -- synthesis requires understanding all findings
  together. Sequential, context-dependent. SINGLE.

MODEL ROUTING:
| Role | Tier | Model | Rationale |
|------|------|-------|-----------|
| Orchestrator | Premium | Opus | Complex reasoning, architecture decisions |
| Source extractors | Cheap/fast | Sonnet | Coding/knowledge work, parallelizable |
| Form classifiers | Cheap/fast | Sonnet | Pattern matching against rubric |

HARNESS POSITION:
- Zone: Generic harness (Claude Code + IL skills + slash commands)
- Classification: Bet (skills + slash commands expected to outlast
  several model generations). PROGRESS.md as session-persistence is
  a shim (plan to retire when native session continuity matures).
- Rationale: Workflow runs ~weekly (well below the >100-run threshold
  for specialized harness); cost-of-failure is low (Nick gates every
  output); task structure is exploratory enough that rigid phase
  schemas would fight the work.
- Review trigger: if extraction throughput plateaus and Nick's
  gate-cost becomes the bottleneck, evaluate phase-gating the
  identify→extract transition with structured-output validation.

INFRASTRUCTURE STATUS:
- Tier 1: Skills define tool permissions per role ✓
- Tier 2: PROGRESS.md for session persistence (manual) △
- Tier 3: Delta reports for observability ✓
  Missing: automated session persistence, budget tracking
```

---

## Pitfalls

### 1. Multi-agent by default
The strongest driver of unnecessary multi-agent complexity is familiarity bias and FOMO -- teams adopt orchestrators because they feel innovative, not because they produce measurable improvement. Measure single-agent baseline first. Always. Gartner reported a 1,445% surge in multi-agent system inquiries between Q1 2024 and Q2 2025; the interest far outpaces the cases where multi-agent is justified.

### 2. Role-based decomposition (specialization theater)
"Let's have an engineer agent, a QA agent, and a PM agent" mirrors org charts, not task characteristics. The interface to the user remains unchanged; only costs and complexity increase. The correct question: "Is this decomposition based on parallelizability, isolation requirements, or human gate needs?"

### 3. Agent sprawl (microservices redux)
The same mistake that plagued microservices in 2018: decomposing everything into agents without orchestration, observability, or coordination infrastructure. Five missing pieces define the gap: scheduling/lifecycle management, merge coordination, supervision hierarchies, financial observability, and standard failure/recovery patterns.

### 4. Ignoring the 45% threshold
If your single agent already achieves 45%+ on the task, adding agents will likely make things worse. Invest in better context, better specs, and better tooling instead.

### 5. Missing contracts at boundaries
Without explicit schemas, quality constraints, and tool permissions, agents negotiate interfaces in natural language. Independent agents amplify errors 17.2x vs. centralized coordination at 4.4x. Validate contracts at runtime, not just in documentation.

### 6. Opus for everything
Opus costs 3.5x Sonnet with no accuracy premium on most benchmarks. Use model-tier routing: premium model for orchestration, cheap/fast model for sub-agent tasks. One production harness ran 7K orchestrator tokens vs. 323K sub-agent tokens -- tier routing kept costs tractable.

### 7. Building on impermanent layers
Heavy prompt chaining, external RAG pipelines, and human verification gates are candidates for model absorption within 18 months. Block cut 50-60% of agent plumbing by asking "will this still be needed when models 2x?" Safety infrastructure is the exception -- never simplify away security, permissions, or audit trails.

### 8. No fallback plan
Every multi-agent architecture should document what happens if it underperforms: "collapse back to single agent" or "reduce to 2 agents" with specific triggers for when to make that call.

### 9. Framework-as-architecture (26 agents for a solo project)
Full SDLC frameworks like BMAD (26 agents, 68 workflows) are powerful for team-scale projects but overkill for solo developers or small tasks. Match framework complexity to project complexity.

### 10. Supervision debt from missing human control points
Designing multi-agent systems without defining where humans must observe, approve, edit, or cancel running work. AGUI is a control-surface specification, not a UI-rendering layer. Adding `human_control_points` to the boundary contract is a one-time decision that prevents compounding debt.

### 11. Premature harness engineering
Building a specialized Python harness with phase gates and schema validation before the prompt-driven or generic-harness baseline has been measured. Real-world inputs rarely match clean schemas; rigid validation breaks where flexible LLM judgment would have absorbed the variance. Under-100-run workflows almost never amortize the engineering cost. Decision rule: only commit to specialized harness when (a) generic baseline is measured and insufficient, (b) >100 runs, *and* (c) cost-of-failure justifies brittleness.

### 12. Ignoring sub-agent wiring verification
Sub-agents frequently complete their individual task but fail to integrate output with the rest of the system. The most common failure in sub-agent orchestration is "isolated islands" -- modules that build but are unreachable from the application's entry point. Run explicit wiring verification after each wave of sub-agent completion. Automated connectivity checks (is every new module reachable?) catch this before multiple waves compound the problem.

### 13. Context rot from inline execution of large plans
Choosing inline batch execution for a large plan (10+ tasks) defeats the context-isolation benefit of sub-agent dispatch. Context utilization beyond 40% shows noticeable accuracy degradation; beyond 60-80%, hallucination risk increases significantly. For large plans, use sub-agent-per-task execution or hybrid topology. The framework should warn when inline is selected for plans that will likely exceed context thresholds.

---

## Related Guides

- **Architecture decisions → execution patterns:** The topology and composition chosen here must be implemented with workflow engines, persistence, and observability. See *Agent Workflow and Execution* (G3b) for the production implementation of these architectural choices.
- **Architecture decisions → agent specifications:** The autonomy gradient and blast radius classification in *Writing Agent Specifications* (G1) determine whether a decision type justifies a separate agent and where human control points belong in the boundary contract.
- **Human control points → human-in-the-loop design:** The AGUI `human_control_points` contract field established here maps directly to approval gates and interrupt points in the execution workflow. See *Agent Workflow and Execution* (G3b) for runtime implementation of observe/approve/cancel control surfaces.
- **Model routing → prompt resilience:** The model routing table in Step 5 is expanded with benchmark rationale in *Model-Resilient Prompt Engineering* (G8).
- **Infrastructure tiers → session persistence:** The persistence and workflow state infrastructure in Step 7 is detailed in *Session Persistence and Memory* (G7).
- **Boundary contracts → tool design:** Risk classification for agent boundaries maps to tool registry design in *Designing Agent Tools* (G5).
- **Architecture evaluation → testing:** Validating that architecture choices produce expected outcomes uses the frameworks in *Building Agent Evaluation Suites* (G4).
- **Per-agent context scope → context curation:** The "scope each agent's context to the minimum it needs" principle for multi-agent designs is detailed in *Managing Agent Context* (G2), particularly the sub-agent context package pattern and atomic-session scoping defense.
- **Four-zone anatomy → agent design:** The four-zone agent framework (trigger/context/tools/output) links to individual agent identity and constitution design in *Agent Design Patterns* (G10).
- **Harness evolution → agentic systems:** The prompt→context→harness engineering evolution in Step 8 connects to the broader system-design principles in *Building Agentic Systems* (G11).

---

## Contract

### Preconditions
- You are designing or evaluating an agent system architecture.
- You have a task or set of tasks that an agent will perform.
- You can measure or estimate single-agent baseline performance on the task.
- You understand the task's characteristics: parallelizability, information flow dependencies, and error sensitivity.

### Invariants
- Architecture decisions are justified by task characteristics (parallelizability, information flow, error sensitivity), not organizational structure or technology trends.
- Single-agent is the default until empirical evidence justifies multi-agent.
- Every agent boundary has an explicit contract validated at runtime, including `human_control_points` and uniform tool interface for sub-agent dispatch.
- Every agent decomposes into four zones (trigger, context, tools, output/memory); zones are specified, not hidden.
- Room scope (Pattern F) is defined by bounded-context characteristics, not by convenience or org-chart structure.
- Model selection is task-based and tier-aware, not provider-based or prestige-based.
- Infrastructure dependencies are classified as architectural bets or transitional shims.
- Harness-determinism position (prompt-driven / generic / specialized) is a deliberate decision tied to an explicit reliability requirement, not a default.
- Specialized-harness investments are classified as bets (with intended life) or shims (with planned removal trigger).
- Execution topology (sub-agent-per-task / inline batch / hybrid) is a runtime parameter, not an architectural constant.

### Governance
- Architecture decisions that affect system boundaries are documented as Design Decisions (DDs).
- The agent count decision tree is re-evaluated when task scope changes significantly or model capabilities improve.
- Model routing tables are re-evaluated monthly given the compressed release cadence.
- Infrastructure longevity audits are performed when new native protocols emerge.
- This guide is owned by the Meta-System knowledge layer and updated when new orchestration findings are integrated.

### Recovery
- If a multi-agent system produces worse results than expected: measure single-agent baseline. If single-agent exceeds 45%, collapse back to single agent and invest in improving it.
- If coordination overhead is the bottleneck: check for missing contracts at agent boundaries. Information loss at undocumented boundaries is the most common cause.
- If model costs are unexpectedly high: check for Opus overuse. Apply model-tier routing -- premium orchestrator, cheap sub-agents.
- If the system fails to recover from crashes: implement workflow state separation and session persistence (see G3b).
- If infrastructure feels fragile: run the four-question impermanence audit and the three-question lock-in assessment.
- If a specialized harness is breaking on real-world inputs: reconsider the spectrum position. The right zone may be one step left -- generic harness with conventions that flex where LLM judgment is sound.
- If specialized-harness scaffolding has been surpassed by model-native capability: retire that check rather than the whole harness. Keep the harness; shrink its surface.
- If supervision debt is accumulating: audit boundary contracts for missing `human_control_points` definitions. Add AGUI control points at the highest-risk transitions first.
- If room-based coordination (Pattern F) produces rooms that grow too large: split rooms at natural bounded-context seams.
- If sub-agent wiring failures accumulate silently: add post-wave integration verification. Check that every new module is reachable from the application's entry point.
- If context rot degrades inline execution quality: switch to sub-agent-per-task execution topology or introduce session checkpointing at phase boundaries.
- If error-aware backtracking loops indefinitely: add retry limits and fall back to human escalation after N failed branches.
