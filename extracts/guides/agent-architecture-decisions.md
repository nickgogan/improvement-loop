---
title: "Agent Architecture Decisions"
type: "guideline"
category: "Orchestration"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-04-19"
updated: "2026-07-19"
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
  - "five-pattern-complexity-escalation-ladder"
  - "four-estimate-agent-routing-test"
  - "effort-scaling-rules-embedded-in-orchestrator"
  - "harness-composition-six-pattern-taxonomy"
  - "hub-and-spoke-10-agent-ceiling-with-queueing"
  - "three-tier-orchestration-hierarchy-scheduler-worker-framework"
  - "ralph-wiggum-execution-pattern"
  - "loop-node-anatomy-schema-enforced-ralph-primitive"
  - "archon-yaml-defined-harness-workflows"
  - "planner-executor-deterministic-guardrails"
  - "skill-forked-subagent-execution"
  - "file-based-task-locking-parallel-agents"
  - "issue-based-agent-orchestration-replacing-markdown-plans"
  - "database-as-shared-memory-coordination"
  - "work-ticket-contract-prompt-mode-vs-work-mode"
  - "standardized-io-as-infrastructure-scaling-prerequisite"
  - "three-layer-core-agent-protocol-stack"
  - "task-complexity-tiering-quick-campaign-deep-build"
  - "framework-tension-taxonomy-superpowers-gsd-gstack"
  - "gstack-spec-team-parallel-research-agents"
  - "parallel-independent-workflow-execution-at-scale"
  - "per-function-recursive-loop-composition"
  - "meta-agent-prompt-generation-bootstrap-pattern"
  - "five-pattern-multi-agent-communication-taxonomy"
  - "missions-three-role-architecture-serial-targeted-parallelization"
  - "flat-parentless-cross-model-agent-communication"
  - "droid-whispering-per-role-model-assignment"
  - "structured-handoff-schema-self-healing-multi-agent-missions"
  - "pre-code-validation-contracts-dual-blind-validators"
  - "oracle-evaluator-architect-domain-expert-progression"
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "orchestration"
  - "architecture"
contract:
  preconditions: "Agent system design phase; topology not yet committed; harness-spectrum position is a deliberate decision, not a default"
  invariants: "Architecture choices traceable to task requirements; every agent decomposable into four zones (trigger, context, tools, output); pattern position chosen at the lowest escalation-ladder level whose ceiling is not hit; every autonomous loop declares completion signal, deterministic check, iteration budget, and context policy; coordination substrate is an explicit decision; harness-determinism position chosen against an explicit reliability requirement; specialized-harness investments classified as bets or shims; sub-agent dispatch treated as a uniform tool interface"
  governance: "IL-owned draft; Nick deploys"
  recovery: "If architecture shows specialization theater symptoms, revisit single-agent default. If token cost blows up after escalation, drop one ladder level. If a loop never converges, tighten pass/fail criteria and add a deterministic check plus iteration budget. If specialized harness brittleness blocks real-world inputs, reconsider spectrum position. If sub-agent wiring failures accumulate, add post-wave integration verification."
---

# Agent Architecture Decisions

Should you use one agent or many? How should they coordinate? Which model should each use? How permanent is the infrastructure you are building?

This guide provides empirically-grounded decision frameworks for agent system topology -- from the single-agent default through legitimate multi-agent domains to composition patterns, coordination substrates, autonomous loops, sub-agent orchestration primitives, model routing, and infrastructure longevity assessment. It covers the "what" of agent architecture: what topology to choose, what boundaries to draw, what models to assign, and where on the harness-determinism spectrum to position. For the "how" -- running agents in production with workflow engines, observability, cost management, and failure handling -- see *Agent Workflow and Execution* (G3b).

## When to Use This Guide

- You are designing a new agent system and choosing between single-agent and multi-agent.
- You have a multi-agent system that underperforms and want to evaluate whether the architecture is the problem.
- You are adding a new agent to an existing system and need to decide how to integrate it.
- You are choosing which model to assign to which agent role.
- You are auditing existing infrastructure for lock-in risk or layer impermanence.
- You are evaluating whether your multi-agent system needs a central orchestrator, room-based peer-to-peer coordination (Pattern F), or orchestrator-free coordination through a shared substrate (Pattern I).
- You are deciding whether a long-running task should be an autonomous loop, and what the loop's anatomy must declare (Pattern J).
- You are defining human control points in boundary contracts and need to classify which steps require observe, approve, or cancel semantics (AGUI).
- You are designing sub-agent dispatch mechanics and need to decide between execution topologies (sub-agent-per-task vs. inline batch).
- You are positioning on the harness-determinism spectrum and need to evaluate prompt-driven vs. generic vs. specialized.

**Do not use for:** specifying what an agent does (see *Writing Agent Specifications*, G1), managing context within an agent (see *Managing Agent Context*, G2), running agents in production (see *Agent Workflow and Execution*, G3b), or evaluating agent output quality (see *Building Agent Evaluation Suites*, G4).

## Key Concepts

**1. Single agent is the default (L > D).** Information loss across agent boundaries (L) typically exceeds context degradation from long context within a single agent (D). Multi-agent swarms degrade sequential tasks by 39-70%. Independent agents amplify errors 17.2x versus centralized coordination at 4.4x. Start with one agent and only split when you have empirical evidence that splitting helps.

**2. The 45% saturation threshold.** Multi-agent coordination yields diminishing or negative returns once a single agent exceeds ~45% baseline performance. Past this point, invest in making the single agent better -- better context, better specs, better tooling -- rather than adding agents.

**3. Decompose by task characteristics, not roles.** Agent "teams" that mirror human organizational structure (engineer, QA, PM) are specialization theater -- they add cost and complexity without improving outcomes. The correct decomposition criteria are parallelizability, information flow dependencies, and error sensitivity.

**4. Contracts at every boundary.** Without explicit input/output schemas, quality constraints, and tool permissions at every agent boundary, agents negotiate interfaces in natural language -- introducing ambiguity, drift, and hallucination that compounds across boundaries. Standardized I/O is also the scaling prerequisite: composability, reliability, team sharing, and monitoring all depend on it.

**5. Infrastructure is impermanent -- plan for it.** Current agent infrastructure layers (retrieval pipelines, heavy prompt scaffolding, verification gates) will be progressively absorbed by model-native capabilities. Classify each dependency as an architectural bet or a transitional shim, and design for easy removal.

**6. Rooms are a coordination boundary, not a UI feature.** In room-based multi-agent systems, the room is the bounded context: agents coordinate peer-to-peer via @mentions without a central orchestrator. This is categorically different from orchestrator→worker delegation (Patterns A-E). The design question is: "What is the natural bounded context for this set of agents?"

**7. Human control points are a contract field, not an afterthought.** The AG-UI protocol (AGUI) encodes where humans must observe, approve, edit, or cancel running agent work. Alongside MCP (agent-to-resource) and A2A (agent-to-agent), AGUI completes the core protocol stack for production systems. Every boundary contract should include a `human_control_points` definition. Each missing layer creates a named debt: integration debt (no MCP), coordination debt (no A2A), supervision debt (no AGUI).

**8. Harnesses lie on a determinism spectrum -- choose position deliberately.** Agent systems sit somewhere between "entirely LLM-initiated via prompts" and "mostly deterministic with code-wired workflows." The position is not a default -- it is a decision tied to a reliability requirement. The hard rule inside the spectrum: planning can be probabilistic; execution of side effects must be deterministic.

**9. Every agent is four zones.** Regardless of tool or framework, every agent decomposes into: trigger (what wakes it), context (what is injected per turn), tools (what it can interact with), and output/memory (where work goes and how state persists). Debugging is systematic -- a broken agent has a broken zone. A well-designed spec covers all four zones; an opaque framework hides them.

**10. Sub-agent dispatch is a tool call, not a special mechanism.** Sub-agents should be dispatched through the same interface as any other tool -- same hooks, same logging, same permission checks. Interface homogeneity means hooks work for free, the tool registry is the single source of capabilities, and sub-agent calls can be mocked like any other tool. Frameworks that give delegation its own API surface add complexity that the uniform interface avoids.

**11. Harness engineering is the third evolution.** The progression from prompt engineering (single LLM, single output) to context engineering (single agent, curated context) to harness engineering (multiple agent sessions, orchestrated workflow) represents maturation of AI development. 40% of Claude Code's codebase is harness infrastructure. Each evolution builds on the previous -- harness engineering requires good context engineering at each node.

**12. Escalate patterns only at the ceiling.** Orchestration patterns form a five-level escalation ladder -- sequential flow → operator → split-and-merge → agent teams → headless -- ordered by complexity, cost, and autonomy. Each level has a specific ceiling and an explicit escalation trigger. Start at the simplest level that fits and escalate only when the current level's ceiling is hit; agent teams cost 4-7x tokens versus a single session.

**13. Composition has a closed micro-pattern vocabulary.** Six named patterns (classify-and-act, fan-out + synthesize, adversarial verification, generate-and-filter, tournament, loop-until-done) cover how harnesses compose agents, and each cures a named single-context failure mode -- agentic laziness, self-preferential bias, goal drift after compaction. Select patterns by the task's failure-mode profile, not by available compute.

**14. The coordination substrate is a design decision.** Orchestrator-free multi-agent coordination is real and production-proven: parallel agents can coordinate entirely through a shared substrate -- lock files plus git, a queryable issue graph, a versioned database, or a ticket queue with explicit work contracts. Anthropic built a 100,000-line Rust C compiler with parallel Claude instances coordinating through nothing but lock files and git. Choose the substrate as deliberately as the topology.

**15. A loop is a composition primitive with a required anatomy.** Any agent-in-a-loop needs a complete, checkable spec: a completion signal, a deterministic completion check, a hard iteration budget, an explicit per-iteration context policy, optional human gates, and iteration-level observability. "The model says it's done" and "the tests pass" are different facts -- declare both. Dangerous omissions (no budget) should be structurally unrepresentable.

**16. Agent-to-agent communication has a five-pattern vocabulary.** How agents talk is a distinct design axis from how they are composed. Five structurally different patterns cover it -- delegation (spawn-and-return), creator-verifier (a stakeless second agent checks the first), direct communication (peer-to-peer, no coordinator), negotiation (agents coordinate over a shared resource), and broadcast (one-to-many status/context). Each has a named cost and failure mode; direct communication is the most expensive and the most fragile (state fragments with no single source of truth), which is why production systems (Factory's Missions) deliberately compose the other four and omit it. Pick the communication pattern by the coordination need, not by whichever is easiest to wire (which is always delegation).

**17. Mandatory rules belong in the harness, not in prose.** The strongest cross-vendor consensus in the harness landscape (surveyed across three LLM-first harnesses -- Claude Code, Codex, opencode -- and confirmed in code-first, orchestrator, and platform classes) is that anything the system declares *mandatory* must be enforced *outside the model's reach*: a `PreToolUse`-style hook or a deny-by-default permission rule that makes the disallowed action invisible, never a CLAUDE.md instruction the model is asked to remember. LLM-first harnesses describe *control flow*; they must not be trusted to *enforce*. A source-verified "hard" rule is necessary but not sufficient -- opencode's Plan Mode is a hard ruleset in source yet leaks in practice (subagent delegation, background/resumed sessions, mode transitions), so enforcement must be *empirically tested* on those exact leak-prone paths, not assumed from the design. (See `operations/plans/memory-spec-inputs/C-synthesis-harness-memory-harmonization.md` §4b.)

**18. Structured handoffs make multi-agent runs self-healing.** A worker that reports "done" gives the orchestrator nothing to check; a worker that fills a fixed handoff schema -- what was completed, what was left undone, every command run with its exit code, issues discovered, whether it abided by the defined procedure -- lets the orchestrator catch and scope corrective work at each milestone boundary. This field-level schema (not an abstract gesture) is the specific mechanism by which Factory's multi-day missions "self-heal" across dozens of workers; it is the concrete way to reduce information loss (L) at agent boundaries.

---

## Procedure

### Step 1: Route the Task, Then Measure the Single-Agent Baseline

**First, run the four-estimate routing test** (one minute, before any architecture work). Estimate:

1. **Size** -- is the task bigger than one agent can hold at full quality?
2. **Independence** -- can the parts be done without knowing what the other parts did?
3. **Separation of concerns** -- do any parts need different minds (a real critic who didn't write the draft)?
4. **Checkability** -- is checking an answer much cheaper than producing one? If checking is expensive, the value of extra attempts tops out fast.

Verdicts: small problem → **chat**; fits one context window and checks its own work → **single agent with a goal**; bigger than one perspective or needs separate minds → **team of agents**; judgment call where expert instinct beats model instinct → **human, no AI**. The anti-delegation edge matters: for hires, naming, and product direction, models are a wall to bounce ideas off, not a decision-maker. The test's most valuable output is often the reminder to keep a task human. Re-anchor the size estimate periodically -- what needed a team last quarter may fit one agent now.

**Then establish the single-agent baseline** for anything routed past chat:

1. Run the task with a single well-configured agent (appropriate model, good context, clear spec).
2. Measure baseline performance against your acceptance criteria.
3. If baseline exceeds 45%, **stop**. Invest in improving context, tooling, and specification rather than adding agents.
4. If baseline is below 45%, proceed to Step 2 to evaluate whether the task characteristics justify multi-agent.

The 45% threshold is conservative -- the actual breakeven varies by task. But the principle is empirically robust: coordination overhead (information loss at boundaries, handoff costs, error amplification) almost always exceeds the marginal benefit of additional agents past this point.

### Step 2: Evaluate Task Characteristics and Size the Investment

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

**The specialization theater test:** For any proposed multi-agent decomposition, ask: "Is this decomposition based on task characteristics or on familiar human roles?" If the decomposition mirrors an org chart (engineer, QA, PM, designer), it is theater. If it is based on parallelizability, isolation requirements, or human gate needs, it may be justified. One nuance: role-*named* agents in a parallel review fan-out (e.g., five specialists surfacing spec gray areas, including a devil's advocate) can pass the test -- the decomposition there is by *perspective for independent review*, a legitimate domain, not by persistent org-chart delegation. The devil's advocate role is structurally important: without an agent explicitly tasked with attacking the others' conclusions, parallel perspectives converge on consensus that papers over legitimate concerns.

**The agent sprawl test:** Draw the parallel to microservices circa 2018. If you cannot answer these five questions, you are sprawling: (1) Can you list every agent and its scope? (2) Do you have observability over what each agent is doing? (3) Is there coordination infrastructure for parallel agent work? (4) Do you have standard failure/recovery patterns? (5) Do you know cost-per-successful-task for each agent?

**The four-zone audit:** Before deciding on architecture, confirm that each proposed agent's four zones are well-defined. If you cannot specify the trigger, context, tools, and output/memory for an agent, it is under-designed. This audit also exposes framework opacity -- opaque platforms that hide zones from the developer make debugging impossible.

**Size the coordination investment.** Once multi-agent is justified, scale the resource allocation to query complexity rather than spawning maximally. Anthropic's production tiers: simple factual queries → 1 subagent, 3-10 tool calls; comparison queries → 2-4 subagents, 10-15 tool calls; complex multi-source research → 10+ subagents with explicitly divided roles. Token usage explains ~80% of performance variance in multi-agent systems, so these effort-scaling rules are the primary budget-control mechanism -- without them, orchestrators spawn 50 subagents for a factual question. The same logic applies at the human interface as task-complexity tiering: **quick task** (inline, minimal planning) / **campaign** (subtask decomposition, multiple deliverables) / **deep build** (full phase-based planning) -- the tier signals expected planning depth and session architecture.

**Error-aware backtracking.** For long-horizon workflows where compound errors are a concern (90% per-step accuracy on 10 steps = 35% overall), design agents that can backtrack to a decision point and try a different branch rather than continuing on a corrupt path. Checkpoint-based backtracking (save state at each decision point) is more practical than undo chains. Confidence-gated progression (don't advance to step N+1 until step N passes a threshold) prevents silent error propagation.

**Size the human-in-the-loop role, not just the agent count.** Where the domain expert sits relative to the assess-and-improve loop is its own architecture decision, and over-building it is a documented cause of AI-project failure. Three modes form a necessity-driven progression -- do not skip ahead of what your quality signal supports:

| Mode | The expert's role | Precondition |
|------|-------------------|--------------|
| **Oracle** | The expert personally *assesses and improves* output (reads traces, tweaks prompts/docs/tools). No measurement layer, no engineers. | Quality is a taste call -- cannot be measured objectively. |
| **Evaluator** | The expert *defines* quality (metrics, capture system: user signals, hired reviewers, LLM-as-judge); a separate engineer loop does the fixing. | Quality is objectively measurable, and manual iteration (expert flags → engineer fixes) still keeps pace. |
| **Architect** | The expert designs a system that *measures and improves itself* with minimal human-in-the-loop, learning from usage. | Quality is measurable *and* manual iteration can no longer keep pace with the variation. |

Answer two questions in order: (1) Can quality be measured objectively, or is it a taste call? If taste → **Oracle** (and if one person can't hold the whole domain, a *decentralized oracle* -- several experts each owning a subset). (2) If measurable: is manual iteration still fast enough? Yes → **Evaluator**; no → **Architect**. The dominant failure is *mode misdiagnosis* -- building Architect-grade self-improvement before quality is even measurable (nothing solid to optimize against), or formalizing Evaluator dashboards while manual iteration was still fine. The dual-blind validation apparatus of Step 3/Step 4 is what the *Architect* end of this progression operationalizes; a taste-domain product may correctly stay Oracle forever.

### Step 3: Choose a Composition Pattern

**Position on the escalation ladder first.** The macro-patterns below sit on a five-level ladder ordered by complexity, cost, and autonomy. Start at the lowest level that fits; escalate only when you hit the current level's ceiling:

| Level | Pattern | Ceiling | Escalation trigger |
|-------|---------|---------|-------------------|
| 1. Sequential flow | Single session, tasks build on shared context | Context window fills (context rot) | Accumulated context degrades quality |
| 2. Operator | Human runs multiple parallel terminals/worktrees (Pattern A) | Human attention (~4-5 streams) | Too many streams to track manually |
| 3. Split-and-merge | Sub-agent fan-out within one session (Patterns C, G) | Sub-agents cannot coordinate with each other | Real-time interdependencies between tasks |
| 4. Agent teams | Shared communication channel (Patterns D, F) at 4-7x token cost | Token cost and complexity | Output needs human-free autonomous execution |
| 5. Headless | `claude -p`, no human in the loop (Pattern J; scheduling in G3b) | Verifiability without watching | -- |

Decision criteria at each boundary: task dependency, context budget, human attention budget, coordination need (hub-and-spoke vs. peer-to-peer), and trust level (can you verify output without watching each step?). Premature escalation wastes tokens; under-escalation wastes human attention.

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

**Worked instance -- spec gray areas:** After a design doc is approved, dispatch 5 parallel specialists (backend, frontend, QA, product, devil's advocate) to research the design decisions the doc left unresolved, then fold their findings into the spec before implementation. Each gray area gets evaluated from multiple angles simultaneously, with no single perspective dominating. Cost is real (~200k tokens for a spec-research fan-out) -- reserve it for specs where ambiguity would propagate into implementation.

**Limits:** Token cost scales linearly with agent count. Conflicting recommendations from different agents need a clear resolution strategy. Over-exploration delays execution.

#### Pattern D: Shared Communication Channel

For multi-agent work where subtasks have real-time interdependencies.

```
[Orchestrator]
├── [Agent A] ←──shared channel──→ [Agent B]
│   frontend                        backend
└── Channel monitors for deadlock / noise
```

**When to use:** When isolated sub-agents plus orchestrator breaks down because agents have real-time interdependencies (e.g., frontend and backend negotiating API contracts). The shared channel lets agents resolve interdependencies directly rather than routing everything through the orchestrator. This is escalation-ladder level 4: expect 4-7x the token cost of a single session, and escalate here only when the hub-and-spoke ceiling (Pattern G limits) is actually hit.

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

**When to use:** Processing large backlogs of independent tasks (IB queues, batch analysis, parallel file operations). Each wave launches parallel sub-agents with fresh context windows. Between waves, a validation step checks system state before the next wave begins -- preventing compounding errors from cascading.

**Key principles:**
- **One task per sub-agent.** Fresh context dedicated to a single problem produces dramatically better output than one agent handling many tasks.
- **Wiring verification after each wave.** Sub-agents frequently complete their task but fail to integrate output with the rest of the system, leaving "isolated islands." Explicit integration checks after each wave catch this.
- **Context isolation enables model tiering.** The orchestrator uses an expensive model for planning and aggregation; sub-agents use a cheaper model for narrow tasks. In production, this means 7K orchestrator tokens vs 323K total sub-agent tokens -- the harness makes cost control tractable.

**Platform topology constraints (Claude Code):** the sub-agent topology is strictly hub-and-spoke -- sub-agents report only to the main agent and cannot communicate with each other, and at most 10 run concurrently (further tasks are queued and dispatched as slots free). Consequences: work must decompose into pieces that execute without cross-coordination (mid-execution shared state has to route through the hub, creating a bottleneck); batches beyond 10 pay queueing latency, and queued tasks can go stale if earlier results change the relevant context; and the hub's merge step itself consumes significant context when many sub-agents return large results. When tasks genuinely require inter-agent communication, this ceiling is the explicit escalation trigger to Pattern D agent teams -- at 4-7x token cost.

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

#### Pattern I: Shared-Substrate Coordination (Orchestrator-Free)

For parallel agents that coordinate through a shared state store instead of an orchestrator or communication channel.

```
[Agent 1] ──claim/update──→ ┌──────────────────────┐ ←──claim/update── [Agent 2]
                            │  Shared substrate     │
[Agent 3] ──claim/update──→ │  locks / issues / DB  │ ←──claim/update── [Agent N]
                            │  / ticket queue       │
                            └──────────────────────┘
        no orchestrator, no inter-agent messages -- the substrate IS the coordination
```

**When to use:** Many parallel workers on a shared backlog where tasks are individually claimable and the substrate can arbitrate contention. No orchestrator means no single point of failure; no inter-agent communication means no protocol complexity. Anthropic built a 100,000-line Rust C compiler (compiling Linux 6.9, QEMU, FFmpeg at 99% test pass rate) with parallel Claude instances coordinating purely through lock files and git.

**Choose the substrate by coordination needs:**

| Substrate | Mechanism | Best for | Watch out for |
|-----------|-----------|----------|---------------|
| **Lock files + git** | Agent writes `current_tasks/<task>.txt` to claim; pull/merge/work/push; remove lock | Simplest viable coordination; audit trail free in git history | Abandoned locks from crashed agents; no dependency ordering |
| **Issue graph** (Beads-style) | Structured issues with IDs, status, event log, typed dependency links (`discovered-from`, blocking); agents query ready-work (`bd ready`), file discovered problems, update atomically | Multi-session work where markdown plan hierarchies decay; agents hold only local context while the store holds the global work graph | Issue proliferation; dependency-cycle deadlock; stale `in_progress` without timeout/requeue |
| **Versioned database** (Dolt-style) | Shared SQL store with git-like versioning; hash-based IDs prevent collision; cell-level three-way merge resolves concurrent writes | High write concurrency needing ACID transactions, queryable state, and version history | DB as bottleneck; complex concurrent merges may still need manual resolution |
| **Ticket queue + work contract** | Queue (Linear/Jira/anything both humans and agents read/write) where each item carries a work-ticket contract (see Step 4) | Mixed human + multi-vendor agent teams; cross-harness delegation with no integration -- "the ticket is where unintegrated agents talk" | Contract theater: boilerplate fields, receipts that assert rather than prove |

**Key insight:** structured issues with explicit `discovered-from` links solve the "dementia problem" -- an agent in a 10-minute session re-establishes context from the issue itself instead of holding a plan hierarchy in memory. Chat threads, Slack, and markdown plan files are all rejected as state managers here; the substrate must be queryable and atomically updatable.

**Limits:** Requires tasks that are claimable as units. Race conditions on claim (mitigate with atomic creation). Hidden dependencies between "independent" tasks surface as merge conflicts or contradictory outputs.

#### Pattern J: Autonomous Loop (Ralph / PIV)

For heavyweight single items that need iterated passes at full model intelligence, without a human between passes.

```
[Loop driver (bash / workflow engine)]
└── iterate N=1..max_iterations:
      spawn fresh headless session (claude -p)
      ├── read spec.md + plan.md          (state lives in files, not context)
      ├── pick highest-leverage unchecked task
      ├── implement + verify (unbiased test)
      └── mark complete in plan.md
    until: completion signal AND/OR deterministic check passes
```

**When to use:** Complex individual items -- schema migrations, multi-file refactors, long reimplementations -- that cannot complete in one pass. The loop is the depth complement to Pattern G's breadth: waves handle many simple items in parallel; the loop handles one hard item thoroughly. Anthropic used this shape for multi-day autonomous scientific computing (a cosmological Boltzmann solver reimplementation reaching sub-percent accuracy), explicitly as scaffolding against "agentic laziness."

**The critical implementation detail:** spawn a *fresh headless session per iteration* -- not a loop inside one session, which accumulates context rot. State externalizes to spec/plan files, so every iteration runs below the "dumb zone" threshold (~100k tokens for Opus-class models) at full intelligence regardless of project length.

**Declare the full loop anatomy** (schema-enforced in mature engines like Archon's `loop:` node):

| Element | What to declare |
|---------|-----------------|
| Completion signal | String matched in agent output (e.g., `<promise>COMPLETE</promise>`) |
| Deterministic check | Script run after each iteration; exit 0 = done. "Model says done" ≠ "tests pass" -- pair them |
| Iteration budget | `max_iterations`, required; exceeding it fails the loop (retry-on-loop rejected -- the loop manages its own iteration) |
| Context policy | Fresh context per iteration, with the prior iteration's cleaned output explicitly bridged across |
| Human gate | Optional per-iteration approval with feedback injection |
| Observability | Iteration started/completed/failed events; iteration count + cost in run metrics |
| Pause/resume | Iteration counter + session id persisted; resume continues at N+1 |

**Sibling variants:** Ralph iterates *one item to convergence*; PIV (plan → implement → verify) stages the same fresh-context-plus-verification moves *once per unit of work*. Both drive long-running autonomous implementation through iterated fresh-context passes with per-pass verification -- pick by whether the work is one convergence target or a sequence of units.

**Limits:** A bad spec cascades -- each iteration builds on the previous one's output, so an early bug poisons later loops. Model-written tests may be biased toward passing. Signal-string completion is spoofable (the model can emit the token without the work being done) -- the deterministic check is the guard. Cost scales super-linearly for parallel loop runs. Ambiguous pass/fail criteria produce infinite marginal-change cycles -- the iteration budget is the backstop.

#### Composition Micro-Patterns: the Six-Pattern Vocabulary

Below the macro-patterns (A-J) sits a closed vocabulary of six composition micro-patterns -- Anthropic's first-party taxonomy of what harnesses compose at runtime. Each cures a named failure mode of running a whole job in one context:

| Micro-pattern | Shape | Cures |
|---------------|-------|-------|
| **Classify-and-act** | Classifier types the task, routes to a specialized branch (bug → fixer, question → answerer); can also pick each branch's model | Wrong-tool-for-subtask; one-size model spend |
| **Fan-out + synthesize** | Split across many agents, each in a clean context; a synthesize barrier waits for all and merges | Bias contamination across work items |
| **Adversarial verification** | A worker produces; a completely separate critic attacks it against a rubric; keep only what survives | Self-preferential bias (the critic has no attachment to the answer) |
| **Generate-and-filter** | Generate many candidates, filter by rubric or actual verification, dedupe, keep the best | Taste tasks (naming, design) where first-draft anchoring hurts |
| **Tournament** | Multiple agents attempt the same task; a judge compares two at a time until a champion remains | Absolute-scoring unreliability (head-to-head beats scores) |
| **Loop-until-done** | Agent runs; a gate asks "any new findings?"; yes triggers another pass -- the loop decides when it's finished, not a tired context window | Agentic laziness (quitting after 35 of 50 review tasks) |

These compose: a production document-verification harness is fan-out (one agent extracts claims) + adversarial verification (another checks each) + generate-and-filter on sources. The Bun Zig→Rust rewrite composed subagent-per-fix in isolated worktrees + adversarial review + merge. Selection rule: justify each micro-pattern by the task's failure modes, not by available compute -- most tasks don't need a panel of five reviewers. Loop-until-done needs a hard cap or it degenerates into an unbounded loop.

**Two further composition notes:**

- **Prompt as handoff artifact.** One agent system can generate a complete, context-compressed prompt for a different agent system to execute from cold start (dashboard agent → "here's the prompt, paste into Claude Code"). The two agents share no state -- the prompt is the entire connection point. Useful for bootstrapping integrations; fragile as a recurring mechanism (no feedback loop if the target misinterprets).
- **Composition at organizational scale.** The same loop template (sensor → policy → tool → quality gate → learning) can be instantiated once per function/domain as N independent self-improving loops rather than one global loop. Each loop optimizes its domain at its own pace with its own quality gate. Watch for local optimization creating global incoherence, and apply the agent-sprawl test to loop proliferation too.

#### The Communication-Pattern Axis: How Agents Talk

Orthogonal to *how agents are composed* (macro-patterns A-J) and *what they compose into at runtime* (the six micro-patterns) is *how they talk to each other*. Five structurally distinct communication patterns cover the field; naming the one you mean prevents defaulting to delegation for coordination it can't carry.

| Pattern | Shape | Best for | Cost / failure mode |
|---------|-------|----------|---------------------|
| **Delegation** | One agent spawns another, gets a response | Standard sub-agent usage; the default | Cheapest; over-used as a substitute for real coordination |
| **Creator-verifier** | One agent builds, a separate *stakeless* agent checks | Any generate-then-assess step (same logic as human code review) | Cheap; degenerates if the verifier shares the creator's context/bias |
| **Direct communication** | Agents message peer-to-peer, no coordinator | Genuinely peer tasks with no natural hub | Most fragile -- state fragments across conversations with no single source of truth |
| **Negotiation** | Agents coordinate over a *shared resource* (same API, code region) | Interdependent work where a win-win exists (best case is positive-sum) | Expensive; can deadlock or thrash on the shared resource |
| **Broadcast** | One agent → many (status, new shared context, constraints) | Keeping many workers coherent over a long-running task | Cheap but easily skipped; its absence shows up as drift, not an error |

**Production evidence:** Factory's Missions (a multi-day production agent system) deliberately composes *four* of the five -- delegation, creator-verifier, broadcast, and negotiation -- and **omits direct communication** as a coordination primitive, precisely because peer-to-peer messaging fragments state. Treat direct communication (and its structural cousin, Pattern F rooms and the flat/parentless topology in Step 3b) as the pattern that must justify itself against the "no single source of truth" cost. The taxonomy is descriptive of what one production system built, not proven exhaustive -- a market/auction allocation pattern may be a sixth; blend patterns where a real system needs two at once.

### Step 3b: Select Execution Topology

After choosing a composition pattern, decide how the plan executes. This is a runtime parameter, not an architectural constant.

| Topology | When to use | Tradeoff |
|----------|-------------|----------|
| **Sub-agent per task** | Complex tasks, context isolation matters, human review between tasks | Higher token cost, slower, better isolation |
| **Inline batch** | Simple tasks, trust the plan, context from previous tasks helps | Faster, cheaper, context rot risk |
| **Hybrid** | Mixed complexity plan | Some tasks inline, high-risk tasks via sub-agent |

**The plan should be topology-agnostic.** A well-designed plan specifies WHAT (tasks, acceptance criteria) but not HOW the execution engine dispatches them. The topology is an orthogonal concern selected at runtime based on project shape, risk tolerance, and human availability.

**Three scopes of parallelism -- name which one you mean:**

1. **Sub-agent parallelism** -- one task split into parallel sub-tasks within a session (Patterns C, G).
2. **Workspace parallelism** -- multiple operator-driven sessions in separate worktrees (Pattern A).
3. **Task-level parallelism** -- multiple *complete, independent workflow instances* running concurrently, each producing an independent output (e.g., six issue-fix workflows each running its full classify → investigate → implement → validate → PR pipeline). This converts a serial queue of N tasks into N concurrent workflows; per-node model tiering keeps the economics viable. Watch for rate-limit exhaustion when many instances hit expensive nodes simultaneously, and for merge conflicts when parallel workflows touch the same files.

**Serial-with-targeted-parallelization -- the production default for interdependent work.** Factory's Missions system tried naive N-way parallelism (≈10 agents at once) and *rejected it*: agents "conflict, step on each other's changes, duplicate work, make inconsistent architectural decisions." The shipped topology instead runs **exactly one worker or validator active at any point on the feature graph**, and confines parallelism to **read-only operations** -- searching the codebase, researching APIs, parallel code-review passes inside a validator. This is the same L > D finding at the topology layer: interdependent *write* work degrades when split, so it stays serial; independent *read* work is a legitimate parallel domain. The payoff is throughput, not per-task speed -- the same 5-engineer team went from ~10 to ~30 concurrent workstreams, on a system whose longest completed mission ran 16 days. The discipline scales because each worker starts on **clean context** ("no accumulated baggage, no degraded attention"), commits via git, and hands off through a structured schema (Step 4) rather than shared memory.

**The flat / parentless extreme -- and why it is rarely worth it.** At the opposite end from serial hierarchy sits fully flat, orchestrator-free topology: N independent *top-level* sessions (not sub-agents), each named so peers can address it, messaging peer-to-peer with no parent agent -- optionally each on a *different model* (a demo mixed four frontier models across four named sessions). It is the structural opposite of both the Missions hierarchy and standard sub-agent dispatch. Its honest failure-mode profile is the reason to reach for it only as a human-supervised idea pre-filter, never an autonomous loop:

- **Speed-mismatch bottleneck** -- mixing models of different inference speed stalls the group on the slowest; match model *speed* as a selection criterion, not just capability (Step 5).
- **Sycophantic false consensus** -- with no hierarchy forcing dissent, peers converge into "four agents nodding at each other" unless critique is a *structurally assigned* role (the devil's-advocate lesson from Pattern C, made mandatory).
- **Emergent informal leadership** -- an agent assigned a role spontaneously began asserting authority ("No, I'm in charge"); flat design does not prevent hierarchy, it just leaves it unmanaged.
- **No structural circuit-breaker** -- there is no built-in human gate; safety depends entirely on operator discipline.

Choose serial-with-read-only-parallelism as the default for interdependent build work; reserve flat/parentless topology for bounded, human-observed divergent-thinking tasks where the fragmented-state cost is acceptable.

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

**Standardized I/O is the scaling prerequisite.** The transition from "individual agent that works" to "automation infrastructure" is the standardization of what goes in and what comes out. Composability (A's output feeds B's input), reliability (same agent, consistent results), team sharing, and monitoring all depend on it -- without it, each agent is a bespoke integration. Don't over-standardize prematurely: lock in contracts once the domain is understood, and version I/O schemas for backward-compatible updates.

**The work-ticket contract** is the boundary contract for work moving between agents (or agent and human) over a queue (Pattern I). "A prompt asks for an answer; a ticket asks for a result." A conformant ticket carries: **outcome** (result wanted, not request), **owner**, **sources** (background material travels with the work -- nothing depends on reading a chat transcript), **scope limits** (where the agent must stop), **definition of done**, and **receipt** (what it must show when finished). Three lifecycle mechanics map to three failure modes: **claim receipt** (claim-lock before working; no claim → duplicate work), **done receipt** (auditable proof of what was done, explicitly replacing trust in the agent's self-report; no receipt → unverifiable completion), and **needs-input escalation** (on ambiguity the agent parks the ticket carrying the exact blocking question rather than guessing; no such state → silent stalls or invented answers).

**The structured handoff schema** is the boundary contract for a *worker returning to an orchestrator* (as opposed to the work-ticket, which travels with work *into* an agent). "Done" is not a handoff. A conformant handoff forces the worker to fill a fixed schema: **(1) what was completed**, **(2) what was explicitly left undone**, **(3) every command run paired with its exit code**, **(4) issues discovered along the way**, and **(5) whether the worker's actual behavior abided by the orchestrator's defined procedure**. This is what makes a multi-agent run *self-healing*: the orchestrator reads accumulated handoffs at each milestone boundary, detects gaps against the plan, and scopes corrective work precisely from the documented account rather than hoping the next worker infers upstream state. It is the field-level implementation of "reduce information loss (L) at agent boundaries," and in production it is credited as the specific enabling condition for multi-day (16+ day) missions. Two failure modes to design against: **schema blind spots** (a worker fills every field and still omits what matters because no slot exists for it -- version the schema as gaps surface) and **opaque commands** (one large script yields one exit code that hides everything inside -- prefer granular commands so field 3 stays informative). The self-heal only works if the orchestrator actually reads and acts on every handoff; skipping that step under load captures the information but leaves the mission to drift.

**The pre-code validation contract** moves correctness *upstream of implementation*. The orchestrator writes the contract **during planning, before any code exists** -- for a complex project, hundreds of individual assertions, with every feature assigned one or more assertions such that the union of all features' assertions covers the whole contract. Because the assertions predate the code, they cannot be shaped by what the code happens to do (the failure mode of tests-written-after-implementation, which "confirm decisions rather than catch bugs"). The contract is then checked after each milestone by **two blind adversarial validators, neither of which has seen the implementation**: a **scrutiny validator** (test suite, type-check, lint, plus code-review sub-agents spawned per completed feature) and a **user-testing validator** (spawns the running app and drives it via computer-use-style interaction -- fills forms, clicks, checks rendering -- validating behavior end-to-end, not just static shape). This is the Step 3 *adversarial-verification* and *creator-verifier* micro-patterns made concrete at the contract layer; validator blindness is enforced structurally (the validators' tool access must not incidentally surface implementation) and hardened further by assigning the validators a *different model provider* than the implementer (Step 5). Expect it to "never succeed on the first go" -- follow-up features are normal, and the user-testing validator, waiting on real execution, is usually the dominant wall-clock cost. The contract is only as good as the planning conversation that produced it: a wrong assertion is faithfully validated against the wrong thing.

**Agent type enforcement:** Consider a formal type system where each role (Explore, Plan, Verify, Execute) has its own allowed tool set and explicit behavioral constraints. An Explore agent that physically cannot edit files eliminates an entire class of errors. Claude Code implements six built-in types; you can define custom types per project. This is the same enforcement-locus principle as Key Concept 17 -- a tool the agent *cannot call* is a stronger constraint than an instruction it is asked to obey.

**Sub-agent dispatch as tool call.** Implement sub-agent dispatch as a standard entry in the tool registry -- called identically to bash, file-read, or web-search. This ensures hooks, logging, and permission checks work on sub-agent calls without modification. The tool registry becomes the single source of capabilities. Frameworks that give delegation its own API surface add complexity that the uniform interface avoids.

**Skill-as-forked-subagent is the composable dispatch primitive.** A skill can declare `context: fork` + `agent: <type>` to run its body as an isolated subagent's task: the skill supplies the *task*, the named agent type supplies the *persona and tool set*, and the fork gets no access to the main conversation. This unifies skills, subagents, and named invocations -- write the task once, choose where it runs and as whom by changing one frontmatter line. Two contract obligations follow: the skill body must encode all needed context (the fork can't see "the bug we just discussed"), and guidelines-only skills must not target fork mode (the subagent receives conventions but no actionable prompt and returns nothing useful). The inverse composition also exists: a subagent's frontmatter can preload `skills:` as reference material.

**Cross-organizational boundaries:** For agents that delegate across organizational boundaries, the A2A protocol (Google, Linux Foundation, 50+ enterprise partners) defines Agent Cards (`/.well-known/agent.json`) with capability declarations, authentication requirements, and a six-state task lifecycle (`submitted -> working -> input-required -> completed -> failed -> cancelled`). MCP handles agent-to-resource; A2A handles agent-to-agent; AGUI handles human-to-agent.

**The protocol stack composes -- and each missing layer is a named debt.** MCP, A2A, and AGUI are complementary layers, not competitors: MCP answers "what can the agent use?", A2A "who can it work with?", AGUI "how does the human stay in control?" Teams adopt layers incrementally and discover the missing ones through failure -- integration debt (no MCP), coordination debt (no A2A), supervision debt (no AGUI). Supervision debt is the most dangerous because it manifests only after the agent is doing real work with real consequences. Maturity model: MCP-only is valid for simple workflows; MCP+A2A for multi-agent; the full stack for production systems with oversight requirements. A single-user single-agent system may legitimately need only MCP -- applying the full stack there is overhead.

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

**Model-tier routing principle:** Use a premium model for orchestration (user interaction, planning, aggregation) and a cheaper/faster model for narrow sub-agent tasks. This makes parallel sub-agent architectures economically viable at scale. In production, one harness consumed 7K orchestrator tokens vs. 323K total sub-agent tokens -- model tiering kept the cost tractable. Since token usage explains ~80% of multi-agent performance variance, model tiering plus effort-scaling rules (Step 2) are the two levers that control the budget.

**Role-based model assignment (beyond tier routing).** Tier routing (premium orchestrator / cheap sub-agent) is a *cost* axis. A second, orthogonal axis is assigning *different models to different roles by capability*, because no single model or provider is simultaneously best at planning, implementation, and validation: planning rewards slow careful reasoning; implementation rewards fast code fluency; validation rewards precise instruction-following. The distinguishing move -- Factory calls it "droid whispering" -- is running **validation on a different provider entirely than implementation**, so the validator's failure modes are *decorrelated* from the implementer's (different training data, not merely a different context window). This is a capability/bias decision, not a cost one, and it is the concrete way to harden the "validator hasn't seen the implementation" property of the pre-code validation contract (Step 4). A model-agnostic architecture is a structural advantage: "you're only as strong as your weakest link -- if you're locked into one provider, you're constrained by that family's weakest capability," and good surrounding structure (validation contracts, milestone checkpoints) lets weaker or open-weight models safely fill some roles. Two cautions: cross-provider assignment multiplies operational surface (auth, rate limits, cost tracking, differing tool-call semantics -- post-training is harness-specific), and the decorrelation premise weakens silently as frontier labs converge on similar data and techniques. Treat the per-role model map as a versioned, customizable default, not fixed tribal knowledge. When agents of different providers run *concurrently* (flat topology, Step 3b), add inference *speed* to the selection criteria -- the group stalls on the slowest member.

**Subscription vs. API economics.** Claude Code Max plan ($200/month) provides effectively $2,500-$5,000 in subsidized API-equivalent usage. Any tool that requires bypassing Max (using API credentials directly) faces a 12.5-25x cost headwind. For tool selection decisions, the correct question is "does this tool provide enough incremental value to justify API costs vs. the Max plan subsidy?"

**Per-node model selection:** In YAML-defined workflow DAGs (Archon pattern), assign models per workflow node -- Haiku for classification, Sonnet for implementation, Opus for planning. This prevents the anti-pattern of running the most expensive model for every step. In practice the savings compound across parallel workflows: four concurrent issue-fix pipelines with per-node tiering consumed ~20% of a 5-hour subscription window. Beware the silent failure: a Haiku-assigned node that needed Sonnet-level reasoning degrades output without erroring.

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

**Specialized harnesses are deliberate bets against this lesson.** Step 8 introduces the harness determinism spectrum, where specialized harnesses deliver reliability the model alone can't yet provide. Both Step 6 and Step 8 can be correct simultaneously: don't over-build scaffolding the model will absorb, *and* if your reliability requirement is unmet, build the scaffolding anyway with a planned review trigger. (Even the Ralph loop's originators expect it to become less necessary as models improve -- it is scaffolding with a planned obsolescence.)

### Step 7: Build the Infrastructure Layer

Production agent systems need infrastructure beyond the model. Audit against this three-tier checklist:

| Tier | Primitives | Status Check |
|------|-----------|-------------|
| **1: Tools & Permissions** | Tool registry with metadata, permission tiers per tool, security boundaries | Can you list every tool available to each agent role? |
| **2: Persistence & Execution** | Session state persistence (crash-resilient), budget tracking, workflow state machine, coordination substrate (Pattern I) | Can your agent recover from a crash mid-task? Can parallel agents claim work without colliding? |
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

**The harness engineering evolution.** This spectrum reflects a broader maturation: prompt engineering (2022-2024, single LLM output) → context engineering (2024-2025, single agent, curated context window) → harness engineering (2025-2026, multiple agent sessions, orchestrated workflow with deterministic validation steps). Each evolution builds on the previous. Harness engineering requires good context engineering at each node -- a harness that wraps poorly contexted agents just produces bad output faster. The payoff is measurable: raw AI PR acceptance runs ~6.7%; harnessed, ~70%; 40% of Claude Code's own codebase is harness infrastructure, and Stripe ships 1,300 AI PRs/week through one. Independent corroboration comes from outside the Anthropic/Stripe/Archon evidence base: the term's originator (Ryan Lopopolo, after nine months building software exclusively through agents at OpenAI) defines a good harness operationally as "giving the model text at the right time so it can look at the work it has done and the information around what a good job looks like" -- the discipline is about *when* context arrives, not merely *that* it exists. The human's job shifts from writing code to durably encoding the **~500 small non-functional-requirement decisions that separate acceptable code from slop** -- ADRs, personas, QA plans, lint rules, review-agent instructions -- surfaced just-in-time at lint/test/review checkpoints rather than front-loaded into a plan. (Reported there: 3-5 PRs/engineer/day, a 750-package workspace, >1B output tokens/day.)

**The determinism rule inside any zone: plans may be probabilistic; execution of side effects must be deterministic.** The planner (LLM) produces step plans with explicit dependencies and quality constraints; the executor runs steps deterministically -- schema validation and tool invocation, no LLM reasoning mid-execution; a verifier checks each output before the next step proceeds. Letting an agent decide process flow at runtime is "like ripping up your railroad and sticking your train on the ground and saying kind of go that way" -- the agent's value is *within* each step (composing text, calling tools), not deciding step order. Compliance controls and retry logic should be deterministic, not probabilistic.

**The enforcement-locus consensus: mandatory rules live in the harness, never in prose.** The single strongest cross-vendor finding in the harness landscape is a refinement of the determinism rule for *governance* specifically: an LLM-first harness describes control flow but must never be trusted to *enforce* it. Three LLM-first harnesses (Claude Code, Codex, opencode) independently designed every safety-critical guardrail to live *outside the model's reach*, and code-first, orchestrator, and platform classes enforce structurally too. The practical rule: anything you declare *mandatory* belongs in a `PreToolUse`-equivalent hook or a **deny-by-default permission rule** -- which makes the disallowed action *invisible*, never entering the model's option set -- and **never** in a CLAUDE.md instruction the model is asked to remember. Evidence that prose is not enforcement: Codex correctly *summarized* a rule and then stopped *applying* it a few turns later; opencode's own governance table labels its instruction file "Soft." And a source-verified "hard" rule is necessary but not sufficient -- opencode's Plan Mode is a hard ruleset in source that nonetheless *leaks* in practice (subagents bypass the read-only restriction, Bash executes during Plan Mode, files get edited despite the mode), because it is delivered through two mechanisms that do not always agree and subagent delegation slips between them. So **empirically test** enforcement on the exact leak-prone paths -- subagent delegation, background/resumed sessions, mode transitions -- with a deliberately seeded violation; do not infer delivered enforcement from designed enforcement. Distinguish this from the capability question: METR found a specialized scaffold beat a generic ReAct baseline in only ~50.7% of samples, so do *not* gold-plate the capability-boosting surface (elaborate skill routing, dynamic sub-harnesses) on faith -- but the enforcement surface (hooks, deny-rules) is load-bearing and consensus-backed. The discipline that resolves "how much harness is enough": build only what observably breaks when you remove it. (Both findings: `operations/plans/memory-spec-inputs/C-synthesis-harness-memory-harmonization.md` §4b.)

**Position the harness on six dimensions, not one.** The prompt-driven / generic / specialized spectrum is the most visible axis, but a harness-landscape survey cuts real systems along six, which together locate a harness more precisely than the single spectrum does. Naming your position on each is a sharper design act than picking a zone:

| Dimension | The question | The engine's / a governance-first position |
|-----------|--------------|-------------------------------------------|
| **D1 -- shape ownership** | Does your code compile the loop's shape ahead of time (a graph/state-machine), or does the model reach the loop's controls *through* ordinary tool calls? | Model-reached (LLM-first) -- Plan Mode is a permission gate its tool calls trip against, not a script outside its reach. Steering is ~always the model's; *shape* is the real discriminator. |
| **D2 -- persistence** | Where does memory live -- ephemeral, or a durable external store? | This is *where memory lives*, and it is a near-deterministic function of harness class (see below). |
| **D3 -- enforcement locus** | Advisory (prose) or structural (hooks/deny-rules)? | Structural. The most load-bearing dimension for a governance-first system -- see the consensus above. |
| **D4 -- coordination topology** | Single, fixed graph, or dynamic routing? | Configurable autonomy is table stakes; most frameworks offer both code- and model-owned routing as a knob. |
| **D5 -- lifecycle layer** | Is this surface dev-time, run-time, or ops-time? | Separates an inspector/ADE (dev) from the harness (run) from evaluation/optimization (ops) -- resolves apparent overlaps. |
| **D6 -- packaging** | A library you embed, a product you enter, a substrate, or a managed service? | "Meta-harness" / "agent-OS" is a marketing umbrella, not a cell -- always specify posture (wrap / own / generate) + lifecycle layer. |

**Harness class largely picks your memory home.** Because D2 is near-deterministic given the harness class, choosing a class chooses which memory patterns come free and which you must fight for. The evidenced pairings: **LLM-first harness + file-first markdown memory** (CLAUDE.md/AGENTS.md + hooks as the attach point -- the engine's own pairing, and the strongest-evidenced one); **code-first framework + typed checkpointer/store split** (LangGraph/CrewAI/ADK -- but embedding one into a file-first system reintroduces two sources of truth); **cloud platform + managed metered DB memory** (non-file, non-inspectable across all three hyperscalers); **personal daemon + always-on accumulation to markdown+index**. A capability that fights its class is a bolt-on to budget for -- e.g., semantic/embedding recall is non-native to every LLM-first harness (Codex, a frontier vendor, *chose* grep), so grep-first with embeddings deferred is the path of least resistance, not a limitation to route around. (Full harness × memory join: `operations/plans/memory-spec-inputs/C-synthesis-harness-memory-harmonization.md` §3.)

**Specialized-harness primitives** (when you commit to that zone):

- **Phase-gating.** Phase N+1 only proceeds after Phase N output passes validation. State transitions are explicit, not emergent.
- **Structured output schemas at every phase.** Each phase produces validated JSON or equivalent, not free text. Downstream phases consume by schema, not by parsing.
- **Sub-agent delegation per unit.** Each independent unit of work gets its own LLM call with fresh context. Prevents context pollution at the unit level.
- **State management via a database.** A `harness_runs` table tracks current phase, status, outputs. Crashes restart from the last successful phase.
- **Virtual file system / scratch pad.** Every phase writes its output as a file. The full run is replayable and auditable.
- **Model tier routing.** Expensive orchestrator model for main reasoning; cheap fast model for sub-agent extraction.
- **Typed node vocabulary.** Mature workflow-DAG harnesses (Archon) declare each node as *agentic* (a prompt into a coding-agent session), *deterministic* (a script that always runs the same way), *human gate* (pause for approval), or *loop* (Pattern J anatomy, schema-enforced). Per-node context policy (`fresh` vs `continue`) prevents planning bias from leaking into implementation; per-node model selection controls spend. Separating the "decide" node from the "act" node (an agentic classify step followed by a deterministic apply step) keeps side effects on the deterministic side of the rule.

**Three-tier orchestration hierarchy.** When a specialized or generic harness runs multi-phase autonomous builds, separate three tiers with different context scopes and lifetimes: the **scheduler** (owns the phase queue and dispatch logic; lives the whole project; stays under ~10% context by only reading state and ingesting summaries), the **worker** (one headless session per phase, full fresh context, exits after producing a summary), and the **framework** (TDD discipline, role-based decision tools -- invoked *within* a worker session). Information flows down (scheduler → worker → framework) but only summaries flow up -- the asymmetry is what keeps the upper tiers lean. Empirical marker: a 16-phase overnight build completed with the orchestrator at <10% context. Tier-boundary leakage (a worker deciding what runs next; a scheduler reading code) breaks the isolation; for simple 2-3 phase projects, three tiers are overhead.

**Frameworks solve different constraints -- pick or stack accordingly.** The popular Claude Code orchestration frameworks are not interchangeable: gstack enforces role-separated *thinking* (specialist chaining), GSD enforces context *stability* (fresh instance per phase, artifact handoff), Superpowers enforces execution *discipline* (one mega-orchestrator driving a TDD workflow). "gstack thinks, GSD stabilizes, Superpowers executes." Each architecture predicts its failure mode: one-big-brain orchestrators hit context limits on marathon sessions; fresh-session-per-phase pays an explicit-handoff tax on small tasks; role chains resist ad-hoc work. They stack cleanly (specialist thinking inside phases, phase isolation between them, execution primitives within a phase) -- but adopt each for the constraint it solves, or you pay all three taxes at once.

**Autonomous execution loops.** At the specialized end of the spectrum, fully autonomous loops run on fixed intervals (e.g., cron-triggered) without human involvement. Each cycle: read prior results → generate challenger variant → deploy both → measure → harvest winner → append learnings. The human sets the initial baseline and metric definition; the loop runs continuously. Requires a clear objective metric as feedback signal, and the full Pattern J loop anatomy (budget, deterministic check, observability). Applies to A/B testing, ad optimization, content generation, pricing experiments, and any domain with a measurable outcome and fast feedback loop.

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
- Four-estimate routing verdict: {{CHAT/SINGLE_AGENT/TEAM/HUMAN}}
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
  (exception: role-named perspectives in a parallel review fan-out)
- Agent sprawl check: can I list all agents, their scopes, and cost-per-task? {{YES/NO}}

### Decision
- Architecture: {{SINGLE/MULTI}} agent
- Escalation ladder level: {{1_SEQUENTIAL/2_OPERATOR/3_SPLIT_MERGE/4_AGENT_TEAMS/5_HEADLESS}}
  -- ceiling hit at previous level: {{CEILING_EVIDENCE}}
- Justification: {{WHY}} (must reference task characteristics, not roles)
- If multi-agent:
  - Pattern: {{A_WORKTREE/B_ADVISOR/C_FAN_OUT/D_CHANNEL/E_BRAIN_HANDS/F_ROOM/G_WAVE/H_REVIEW_CHAIN/I_SHARED_SUBSTRATE/J_LOOP/CUSTOM}}
  - Micro-patterns composed: {{CLASSIFY/FAN_OUT_SYNTH/ADVERSARIAL/GEN_FILTER/TOURNAMENT/LOOP_UNTIL_DONE}} -- each justified by failure mode: {{FAILURE_MODES}}
  - Coordination substrate (if Pattern I or orchestrator-free): {{LOCK_FILES/ISSUE_GRAPH/VERSIONED_DB/TICKET_QUEUE/NONE}}
  - Effort-scaling tier: {{N_SUBAGENTS}} subagents / {{N_CALLS}} tool calls -- matched to: {{QUERY_CLASS}}
  - Execution topology: {{SUB_AGENT_PER_TASK/INLINE_BATCH/HYBRID}}
  - Agent count: {{N}} -- each justified by: {{REASON_PER_AGENT}}
  - Contracts defined: {{YES/NO}}
  - Sub-agent dispatch via uniform tool interface: {{YES/NO}}
  - Human control points defined (AGUI): {{YES/NO}}
  - Room boundaries defined (if Pattern F): {{YES/NO}}
  - Loop anatomy declared (if Pattern J): {{YES/NO/N_A}}
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
- [ ] Tier 2: Session persistence, workflow state machine, coordination substrate
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
| `CEILING_EVIDENCE` | string | Yes (if level >1) | What ceiling was hit at the previous ladder level |
| `FALLBACK` | string | Yes | What to collapse to if multi-agent underperforms |

### Pre-Spawn Checklist

Before adding a new agent to an existing system:

```markdown
## Pre-Spawn Checklist -- {{NEW_AGENT_NAME}}

1. [ ] Four-estimate routing re-run: task still routes to {{SINGLE/TEAM}}? {{YES/NO}}
2. [ ] Single-agent baseline measured: {{PERCENT}}%
3. [ ] Baseline exceeds 45%? If yes, STOP -- improve the existing agent instead
4. [ ] Escalation ladder: is the current level's ceiling actually hit? {{CEILING_EVIDENCE}}
5. [ ] Task is parallelizable? {{YES/NO}}
6. [ ] Information loss at boundary is acceptable? {{YES/NO}}
7. [ ] Decomposition is based on task characteristics, not roles? {{YES/NO}}
8. [ ] Contract defined for the new boundary? {{YES/NO}}
9. [ ] Four zones defined (trigger/context/tools/output)? {{YES/NO}}
10. [ ] Sub-agent dispatch via uniform tool interface? {{YES/NO}}
11. [ ] Agent type defined with tool allowlist? {{YES/NO}}
12. [ ] Model selected based on task-type and tier routing? {{MODEL_TIER}}: {{MODEL}}
13. [ ] Sprawl check passed (scope, observability, cost known)? {{YES/NO}}
14. [ ] Infrastructure layer dependencies classified (bet vs shim)? {{YES/NO}}
15. [ ] Human control points defined for the new boundary (AGUI)? {{OBSERVE/APPROVE/CANCEL}} at step {{STEP}}
16. [ ] Fallback plan if new agent degrades system performance? {{PLAN}}

If any answer is NO for items 4-8, do not spawn the agent.
```

### Loop Anatomy Spec

For any Pattern J autonomous loop -- declare all elements before the first iteration runs. Omissions are how loops run forever or lie about completion.

```markdown
## Loop Anatomy Spec -- {{LOOP_NAME}}

- Objective: {{OBJECTIVE}}
- Completion signal: {{UNTIL_SIGNAL}} (string matched in agent output)
- Deterministic check: {{UNTIL_CHECK}} (script; exit 0 = done) -- {{REQUIRED/OMITTED_BECAUSE}}
- Iteration budget: max_iterations = {{MAX_ITERATIONS}} (required; loop fails past it)
- Context policy: {{FRESH_PER_ITERATION/CONTINUE}} -- carryover artifact: {{CARRYOVER}}
- State externalization: {{STATE_FILES}} (spec/plan files the loop reads and updates)
- Human gate: {{NONE/PER_ITERATION/ON_ESCALATION}} -- gate message: {{GATE_MESSAGE}}
- Observability: {{ITERATION_EVENTS}} (started/completed/failed + cost per iteration)
- Pause/resume: {{RESUME_SEMANTICS}}
- Cost ceiling: {{BUDGET_USD_OR_TOKENS}}
```

**Variable Reference:**

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `UNTIL_SIGNAL` | string | Yes | Completion token the agent emits (spoofable alone -- pair with check) |
| `UNTIL_CHECK` | string | Strongly recommended | Deterministic verification (tests pass, artifact exists) |
| `MAX_ITERATIONS` | number | Yes | Hard budget; never omit |
| `CARRYOVER` | string | Yes (if fresh context) | What bridges iteration N's output into N+1's fresh session |
| `STATE_FILES` | string | Yes | Where progress lives so no iteration depends on conversation memory |

**Worked example -- engine IB-item deep-execution loop:**

```markdown
## Loop Anatomy Spec -- ib-deep-execution

- Objective: Complete IB-172 (layered-memory design) implementation to passing state
- Completion signal: "ALL PLAN TASKS COMPLETE" in final output
- Deterministic check: `./scripts/verify-ib-172.sh` (frontmatter validation + link check) -- REQUIRED
- Iteration budget: max_iterations = 8
- Context policy: FRESH_PER_ITERATION -- carryover: plan.md checked-task state + prior iteration summary
- State externalization: spec.md (immutable), plan.md (task checklist, updated per iteration)
- Human gate: ON_ESCALATION -- gate message: "Iteration flagged a design ambiguity; ruling needed"
- Observability: per-iteration one-line summary appended to loop-log.md with token cost
- Pause/resume: iteration counter in loop-log.md; resume re-reads plan.md and continues
- Cost ceiling: 500K tokens total
```

### Worker Handoff Schema

For any worker returning to an orchestrator (Step 4). "Done" is not a handoff -- every field is a checkable account the orchestrator reads at the milestone boundary to catch and scope corrective work.

```markdown
## Worker Handoff -- {{WORKER_ID}} / {{FEATURE}}

- Completed: {{WHAT_WAS_DONE}}
- Left undone (explicit): {{WHAT_WAS_NOT_DONE}}
- Commands run (each with exit code):
  - `{{COMMAND_1}}` → exit {{CODE_1}}
  - `{{COMMAND_2}}` → exit {{CODE_2}}
- Issues discovered: {{ISSUES}}
- Abided by defined procedure? {{YES/NO}} -- deviations: {{DEVIATIONS}}
- Handoff artifact / commit: {{COMMIT_OR_FILE}}
```

**Variable Reference:**

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `WHAT_WAS_NOT_DONE` | string | Yes | Explicit scope of the incomplete -- the field that makes the run self-healing |
| `CODE_n` | number | Yes | Exit code per command; prefer granular commands so one opaque script doesn't hide failures |
| `DEVIATIONS` | string | Yes | Where actual behavior diverged from the orchestrator's procedure |

### Pre-Code Validation Contract

For the Step 4 correctness contract, written during planning before code exists. Assertions predate implementation so they can't be shaped by it; two blind validators (neither having seen the code) check them per milestone.

```markdown
## Validation Contract -- {{PROJECT}}

### Assertions (written before implementation)
- A1: {{ASSERTION}} — owning feature(s): {{FEATURE}}
- A2: {{ASSERTION}} — owning feature(s): {{FEATURE}}
  (union of all features' assertions MUST cover the whole contract)

### Validators (blind to implementation)
- Scrutiny validator: {{TEST_SUITE / TYPECHECK / LINT / PER-FEATURE CODE-REVIEW SUBAGENTS}}
- User-testing validator: {{APP_LAUNCH + COMPUTER-USE FLOWS}} — flows: {{FLOWS}}
- Validator model provider: {{PROVIDER}} (DIFFERENT from implementer's provider — decorrelation)

### Expectations
- First-pass success expected? NO (follow-up features are normal)
- Dominant wall-clock cost: {{USUALLY THE USER-TESTING VALIDATOR}}
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
- Four-estimate routing: size = bigger than one context (20+ sources);
  independence = high (sources don't interact); separation of concerns =
  no (same extraction lens per source); checkability = cheap (human gate
  scans finding quality). Verdict: TEAM (parallel extractors)
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
- Escalation ladder level: 3 (split-and-merge) -- level 1 ceiling hit
  (context rot over 20 sequential sources); level 2 skipped (no human
  attention available for parallel terminals); level 4 not needed
  (extractors have zero interdependencies)
- Pattern: G (wave-based) -- subagents per batch with validation
- Micro-patterns composed: fan-out + synthesize (per wave);
  adversarial verification deferred to the human gate
- Effort-scaling tier: 4-6 subagents per wave, matched to
  "complex multi-source research" class
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

COORDINATION SUBSTRATE:
- Pattern I lite: file-mediated handoffs via pipeline_status
  frontmatter -- findings are the shared substrate between
  Researcher, Codifier, and Librarian agents. No orchestrator
  persists between stages; Nick's gates are the phase boundaries.

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
Full SDLC frameworks like BMAD (26 agents, 68 workflows) are powerful for team-scale projects but overkill for solo developers or small tasks. Match framework complexity to project complexity -- and when stacking frameworks, adopt each for the specific constraint it solves (thinking, stability, execution discipline), or you pay all their taxes at once.

### 10. Supervision debt from missing human control points
Designing multi-agent systems without defining where humans must observe, approve, edit, or cancel running work. AGUI is a control-surface specification, not a UI-rendering layer. Adding `human_control_points` to the boundary contract is a one-time decision that prevents compounding debt.

### 11. Premature harness engineering
Building a specialized Python harness with phase gates and schema validation before the prompt-driven or generic-harness baseline has been measured. Real-world inputs rarely match clean schemas; rigid validation breaks where flexible LLM judgment would have absorbed the variance. Under-100-run workflows almost never amortize the engineering cost. Decision rule: only commit to specialized harness when (a) generic baseline is measured and insufficient, (b) >100 runs, *and* (c) cost-of-failure justifies brittleness.

### 12. Ignoring sub-agent wiring verification
Sub-agents frequently complete their individual task but fail to integrate output with the rest of the system. The most common failure in sub-agent orchestration is "isolated islands" -- modules that build but are unreachable from the application's entry point. Run explicit wiring verification after each wave of sub-agent completion. Automated connectivity checks (is every new module reachable?) catch this before multiple waves compound the problem.

### 13. Context rot from inline execution of large plans
Choosing inline batch execution for a large plan (10+ tasks) defeats the context-isolation benefit of sub-agent dispatch. Context utilization beyond 40% shows noticeable accuracy degradation; beyond 60-80%, hallucination risk increases significantly. For large plans, use sub-agent-per-task execution or hybrid topology. The framework should warn when inline is selected for plans that will likely exceed context thresholds.

### 14. Premature ladder escalation (and its mirror)
Jumping to agent teams at 4-7x token cost for tasks that split-and-merge handles at 1/5 the price -- or staying sequential when parallelism would save hours. Both come from not checking the current level's ceiling. Escalate only on ceiling evidence (context rot, attention overload, real interdependencies, autonomy need); de-escalate one level when token costs blow up without quality gains. Real tasks sometimes straddle levels (mostly independent with one dependency) -- handle the exception explicitly rather than escalating the whole workload.

### 15. Loops without anatomy
An agent loop with no `max_iterations` runs forever on ambiguous pass/fail criteria; a loop with only a signal-string completion check gets spoofed (the model emits the done-token without the work being done); a loop inside one long session accumulates context rot the pattern exists to prevent. Declare the full anatomy (Pattern J table) before the first iteration. And remember spec poisoning: each iteration builds on the last, so a bad early spec cascades through every subsequent pass.

### 16. Contract theater at coordination boundaries
Work-ticket fields filled with boilerplate, receipts that assert completion rather than prove it, and definition-of-done copied from a template defeat the point of the contract -- which is to replace trust in agent self-reports with auditable evidence. If the receipt can be written without doing the work, it is not a receipt. Lint tickets at creation: reject items missing definition-of-done or scope limits.

### 17. Overestimated independence
Parts that look separable share hidden state, and the merged result contradicts itself -- the most common failure of both parallel workflows and shared-substrate coordination. Symptoms: merge conflicts between parallel workers, contradictory outputs the hub must reconcile, queued tasks gone stale because earlier results changed the context. The independence estimate (four-estimate test #2) deserves the most skepticism of the four; track verdicts against outcomes to learn where it misjudges.

### 18. Mandatory rules written as prose instead of enforcement
Putting a must-never rule in CLAUDE.md and trusting the model to remember it. Prose is control-flow guidance, not enforcement -- production harnesses show a model faithfully *summarizing* a rule and then ceasing to *apply* it a few turns later. Anything genuinely mandatory belongs in a hook or a deny-by-default permission rule that removes the action from the model's option set. Worse: assuming a source-verified "hard" rule is actually delivered -- hard rulesets leak through subagent delegation, resumed/background sessions, and mode transitions. Test enforcement with a deliberately seeded violation on those exact paths; don't infer it from the design.

### 19. Flat/parentless topology mistaken for cheap parallelism
Launching N peer agents with no orchestrator looks like free parallelism but degenerates predictably: sycophantic false consensus (peers nod at each other with no structurally-assigned dissenter), emergent informal leadership (an agent spontaneously asserts authority the flat design didn't grant), and a group that stalls on its slowest model when providers are mixed. It has no built-in human circuit-breaker. Reserve it for bounded, human-observed divergent-thinking pre-filters; make critique a mandatory role; never run it as an autonomous loop.

### 20. Unread plans that still bind the agent
Approving a plan you didn't read is a *distinct* failure mode from having no plan -- not a safer middle ground. An unread but approved plan still "encodes a bunch of instructions you don't necessarily want followed," silently steering the harness. Either read and own the plan, or lean on just-in-time instruction surfacing at lint/test/review checkpoints; don't rubber-stamp a plan whose contents you haven't accepted.

### 21. Building Architect-grade automation before quality is measurable
Investing in self-measuring, self-improving review architecture (the Architect mode) while output quality is still a taste call, or standing up Evaluator dashboards while manual expert-flags-then-engineer-fixes iteration was still fast enough. The oracle→evaluator→architect progression is necessity-driven: diagnose the mode from the two-question tree (measurable? manual iteration fast enough?) before building the apparatus. Over-building the human-in-the-loop layer is a documented root cause of abandoned AI projects.

### 22. Cross-provider decorrelation treated as permanent
Assigning validators a different model provider than the implementer decorrelates their failure modes -- a real hardening move today -- but the premise erodes silently as frontier labs converge on similar data and techniques, and it multiplies operational surface (auth, rate limits, cost tracking, tool-call semantics). Treat the per-role model map as a versioned, revisited default, not a set-once convention that calcifies into unversioned tribal knowledge.

---

## Related Guides

- **Architecture decisions → execution patterns:** The topology and composition chosen here must be implemented with workflow engines, persistence, and observability. See *Agent Workflow and Execution* (G3b) for the production implementation of these architectural choices, including scheduling (cron/headless), dispatch mechanics, and cost operations.
- **Architecture decisions → agent specifications:** The autonomy gradient and blast radius classification in *Writing Agent Specifications* (G1) determine whether a decision type justifies a separate agent and where human control points belong in the boundary contract.
- **Human control points → human-in-the-loop design:** The AGUI `human_control_points` contract field established here maps directly to approval gates and interrupt points in the execution workflow. See *Agent Workflow and Execution* (G3b) for runtime implementation of observe/approve/cancel control surfaces.
- **Model routing → prompt resilience:** The model routing table in Step 5 is expanded with benchmark rationale in *Model-Resilient Prompt Engineering* (G8).
- **Infrastructure tiers → session persistence:** The persistence and workflow state infrastructure in Step 7 -- including workflow-state vs. conversation-state separation and state files as orchestrator memory -- is detailed in *Session Persistence and Memory* (G7).
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
- Single-agent is the default until empirical evidence justifies multi-agent; the four-estimate test may also route a task to chat or to human judgment (no AI).
- Orchestration pattern position is the lowest escalation-ladder level whose ceiling is not hit; escalation requires ceiling evidence.
- Every agent boundary has an explicit contract validated at runtime, including `human_control_points` and uniform tool interface for sub-agent dispatch; completion claims at coordination boundaries are receipt-backed, not self-reported.
- Every agent decomposes into four zones (trigger, context, tools, output/memory); zones are specified, not hidden.
- The coordination substrate (hub, channel, room, or shared substrate) is an explicit design decision, not an accident of tooling.
- Every autonomous loop declares its full anatomy: completion signal, deterministic check, iteration budget, context policy, and observability.
- Composition micro-patterns are selected by the task's failure-mode profile, not by available compute.
- The agent-to-agent communication pattern (delegation / creator-verifier / direct / negotiation / broadcast) is a named choice, not the default of delegation; direct/peer communication must justify itself against its no-single-source-of-truth cost.
- Interdependent write work stays serial; parallelism is confined to independent read-only work unless empirical evidence shows the split is safe.
- Worker→orchestrator handoffs use a structured schema (completed / left-undone / commands+exit-codes / issues / procedure-adherence), not a "done" report.
- Anything declared mandatory is enforced structurally (hook or deny-by-default rule), never as prose the model is asked to remember; delivered enforcement is verified with a seeded violation on subagent/resumed-session/mode-transition paths.
- Correctness contracts are written before implementation and checked by validators blind to the implementation; validators are decorrelated from the implementer (different provider where feasible).
- The human-in-the-loop role (oracle / evaluator / architect) is sized to the quality signal, not built ahead of it.
- Room scope (Pattern F) is defined by bounded-context characteristics, not by convenience or org-chart structure.
- Model selection is task-based and tier-aware, not provider-based or prestige-based; resource allocation follows effort-scaling rules matched to query class.
- Infrastructure dependencies are classified as architectural bets or transitional shims.
- Harness-determinism position (prompt-driven / generic / specialized) is a deliberate decision tied to an explicit reliability requirement, not a default; within any zone, planning may be probabilistic but execution of side effects is deterministic.
- Specialized-harness investments are classified as bets (with intended life) or shims (with planned removal trigger).
- Execution topology (sub-agent-per-task / inline batch / hybrid) is a runtime parameter, not an architectural constant.

### Governance
- Architecture decisions that affect system boundaries are documented as Design Decisions (DDs).
- The agent count decision tree and ladder position are re-evaluated when task scope changes significantly or model capabilities improve (size estimates drift as models improve -- what needed a team last quarter may fit one agent now).
- Model routing tables are re-evaluated monthly given the compressed release cadence.
- Infrastructure longevity audits are performed when new native protocols emerge.
- This guide is IL-owned (engine knowledge layer) and updated when new orchestration findings are integrated; Nick deploys.

### Recovery
- If a multi-agent system produces worse results than expected: measure single-agent baseline. If single-agent exceeds 45%, collapse back to single agent and invest in improving it.
- If token costs blow up after escalation without quality gains: drop one escalation-ladder level (agent teams → split-and-merge; split-and-merge → sequential).
- If coordination overhead is the bottleneck: check for missing contracts at agent boundaries. Information loss at undocumented boundaries is the most common cause.
- If model costs are unexpectedly high: check for Opus overuse. Apply model-tier routing -- premium orchestrator, cheap sub-agents -- and effort-scaling rules matched to query class.
- If the system fails to recover from crashes: implement workflow state separation and session persistence (see G3b, G7).
- If infrastructure feels fragile: run the four-question impermanence audit and the three-question lock-in assessment.
- If a specialized harness is breaking on real-world inputs: reconsider the spectrum position. The right zone may be one step left -- generic harness with conventions that flex where LLM judgment is sound.
- If specialized-harness scaffolding has been surpassed by model-native capability: retire that check rather than the whole harness. Keep the harness; shrink its surface.
- If supervision debt is accumulating: audit boundary contracts for missing `human_control_points` definitions. Add AGUI control points at the highest-risk transitions first.
- If room-based coordination (Pattern F) produces rooms that grow too large: split rooms at natural bounded-context seams.
- If sub-agent wiring failures accumulate silently: add post-wave integration verification. Check that every new module is reachable from the application's entry point.
- If context rot degrades inline execution quality: switch to sub-agent-per-task execution topology or introduce session checkpointing at phase boundaries.
- If an autonomous loop never converges: tighten ambiguous pass/fail criteria, add a deterministic completion check alongside the signal string, and rely on the iteration budget as the backstop; on repeated budget exhaustion, escalate to human.
- If parallel "independent" outputs contradict each other: reassess the independence estimate; route the shared state through an explicit coordination substrate (Pattern I) or collapse the parallel branches.
- If error-aware backtracking loops indefinitely: add retry limits and fall back to human escalation after N failed branches.
