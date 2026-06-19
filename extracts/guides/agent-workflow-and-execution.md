---
title: "Agent Workflow and Execution"
type: "guideline"
category: "Orchestration"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-04-19"
updated: "2026-04-19"
author: "claude"
source_findings:
  - "planner-executor-deterministic-guardrails"
  - "workflow-state-vs-conversation-state"
  - "session-persistence-crash-resilient"
  - "claude-code-loop-in-session-cron-scheduling"
  - "durable-workflow-engine-for-agent-systems"
  - "session-as-append-only-event-log"
  - "skill-vs-process-distinction-deterministic-rails"
  - "archon-yaml-defined-harness-workflows"
  - "agent-cost-blowup-mitigation-strategies"
  - "graceful-degradation-modes-for-agent-failure"
  - "gsd-stall-detection-revision-loop-escalation"
  - "structured-streaming-events-observability"
  - "unified-tracing-opentelemetry-for-agents"
  - "review-pipeline-bottleneck-and-quality-at-source"
  - "staged-delivery-for-review-digestibility"
  - "task-complexity-tiering-quick-campaign-deep-build"
  - "sprint-contract-negotiation-pattern"
  - "multi-day-autonomous-scientific-computing-workflow"
  - "cloud-local-plan-handoff-teleport-pattern"
  - "bmad-help-adaptive-module-routing"
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "orchestration"
  - "workflow"
  - "execution"
  - "operations"
contract:
  preconditions: "Agent architecture chosen (see G3); moving to production execution design"
  invariants: "Planning is probabilistic; execution is deterministic; every workflow is observable and recoverable"
  governance: "IL-owned draft; Nick deploys"
  recovery: "If workflows fail silently, add observability first; if costs explode, add budgets; if crashes lose state, add persistence"
---

# Agent Workflow and Execution

You have chosen your agent architecture (see *Agent Architecture Decisions*, G3). Now: how do you run it in production? How do you separate planning from execution, persist state across crashes, observe what agents are doing, control costs, handle failures gracefully, and deliver work at a pace humans can review?

This guide covers the "how" of agent operations -- workflow engines, execution patterns, observability, cost management, degradation modes, and delivery cadence. It is the production companion to G3's architectural choices.

## When to Use This Guide

- You have an agent architecture and need to implement it with reliable execution.
- Your agents crash mid-task and lose all progress.
- Your agent costs are unpredictable or growing without clear correlation to value.
- You cannot trace what an agent did or why it failed.
- Your agents produce work faster than humans can review it.
- You need to run agents on schedules or as long-running background workers.

**Do not use for:** choosing between single-agent and multi-agent (see G3), specifying what an agent does (see G1), managing context within an agent (see G2), or evaluating agent output quality (see G4).

## Key Concepts

**1. Planning is probabilistic; execution is deterministic.** The LLM decides what to do. Deterministic infrastructure guarantees it gets done reliably. Never let an LLM decide process flow for operations with irreversible consequences.

**2. Skills are not processes.** Agent skills (send email, query DB, compose text) are atomic capabilities. Business processes are deterministic sequences with known handoffs and exception paths. The agent operates within each step; the process flow itself is hardcoded infrastructure.

**3. Workflow state is not conversation state.** "What was said" (transcript) and "what step the agent is on" (state machine) are separate concerns. Separating them makes operations retry-safe -- crashing and restarting will not re-execute side effects.

**4. Observability is not optional.** "If you can't trace it, you can't improve it." Multi-agent systems fail in ways that are impossible to diagnose without end-to-end tracing. The error taxonomy (retrieval fail vs reasoning fail vs tool fail) determines the fix.

**5. Review bandwidth is the bottleneck, not generation speed.** AI accelerates generation 100x but review capacity grows only 3x. Every additional review layer adds ~10x wall-clock time. Build quality at source; deliver in reviewer-calibrated chunks.

---

## Procedure

### Step 1: Separate Planning from Execution

The foundational architectural boundary for any agent workflow with side effects.

```
[Planner]  →  step plan  →  [Executor]  →  output  →  [Verifier]  →  next step
  (LLM)       (structured)    (deterministic)           (validation)
```

**The planner** (LLM) produces step plans with explicit dependencies and quality constraints. It reasons about what to do, in what order, and what success looks like.

**The executor** runs steps deterministically -- no LLM reasoning during execution, only schema validation and tool invocation. It follows the railroad tracks laid by the planner.

**The verifier** checks each output against quality constraints before the next step proceeds. Verification can be deterministic (schema validation, test execution) or LLM-assisted (semantic quality check), but it must be a separate step, not interleaved with execution.

**The railroad analogy:** Letting an agent decide workflow sequencing is "like ripping up your railroad and sticking your train on the ground and saying kind of go that way." The agent's value is within each step (composing text, calling tools), not deciding which step comes next. Business processes have known steps, known handoffs, known exception paths. These should be hardcoded infrastructure.

**When to relax this boundary:** Exploratory tasks (research, brainstorming, debugging) where the path is unknown. Even then, side effects (file writes, API calls) should be gated through deterministic execution.

#### YAML-Defined Workflow DAGs

For repeatable workflows, encode the plan-execute-verify pattern as a YAML DAG:

```yaml
workflow: {{WORKFLOW_NAME}}
nodes:
  - name: classify
    type: agentic
    model: haiku
    prompt: "Classify the input as {{CATEGORIES}}"
  - name: implement
    type: agentic
    model: sonnet
    prompt: "Implement based on classification"
    depends_on: [classify]
  - name: lint
    type: deterministic
    command: "npm run lint"
    depends_on: [implement]
  - name: review
    type: human_gate
    depends_on: [lint]
```

Each node is either agentic (LLM prompt), deterministic (bash command), or a human gate. Per-node model selection prevents the anti-pattern of running the most expensive model for every step. Evidence: Stripe Minion ships 1,300 AI-only PRs/week using harnessed workflows; raw AI PR acceptance is 6.7%, harnessed acceptance is ~70%.

### Step 2: Implement Workflow State and Persistence

#### Separate Workflow State from Conversation State

Track explicit workflow states independent of the conversation transcript:

```
planned → awaiting_approval → executing → waiting_on_external → completed/failed
```

This separation makes operations retry-safe. If the agent crashes during `executing`, the workflow engine knows which step failed and can resume from that point without replaying the entire conversation or re-executing completed side effects.

**Idempotent tool calls:** Every tool call within a workflow step should be idempotent -- calling it twice with the same input produces the same result. This prevents double-execution of side-effectful operations (duplicate emails, double payments, redundant deployments) when a crash forces a retry.

#### Session Persistence Patterns

Three levels of persistence, from simplest to most robust:

**Level 1: File-based checkpoints.** Persist state to a file (PROGRESS.md, JSON checkpoint) after every significant event. On recovery, load the file and reconstruct state.

```
load(checkpoint_file) → reconstruct(state) → restore(session)
```

**Level 2: Git-based persistence.** Commit and push after every meaningful work unit. Provides recoverable history, visible progress, and resilience to compute interruptions. Validated by Anthropic's multi-day scientific computing workflow where Claude ran autonomous multi-day sessions reimplementing a cosmological Boltzmann solver, using git commits as the persistence layer.

**Level 3: Append-only event log.** Externalize session state as an append-only stream of events outside both the context window and the sandbox. Three core APIs: `getSession(id)` fetches the log, `wake(sessionId)` reboots from the log, `emitEvent(id, event)` appends events durably. The log supports flexible context slicing via `getEvents()` -- rewind for additional context, fast-forward to resume. Prior approaches (compaction, trimming) make irreversible cuts; the event log preserves everything and lets the brain select what to load.

#### Durable Workflow Engines

For multi-hour and multi-day workflows, use a durable execution platform (Temporal, Restate) that provides:
- Persisted workflow state surviving process crashes
- Crash-safe retries with configurable policies
- Idempotent tool calls preventing double-execution
- Resumption without replaying entire workflows

The architectural separation: "LLMs decide what to do; the workflow engine guarantees it gets done reliably."

### Step 3: Classify Task Complexity

Not every task needs the same execution depth. Classify before executing:

| Tier | Description | Planning Depth | Session Architecture |
|------|-------------|---------------|---------------------|
| **Quick Task** | Single-turn or short iterative exchange | Minimal -- inline execution | One session, no phases |
| **Campaign** | Multiple deliverables, subtask decomposition | Medium -- subtask breakdown | Parallel sessions possible |
| **Deep Build** | Full phase-based planning, extensive output | Full -- phase gates, architecture review | Multi-session, phased delivery |

The tier determines how much planning overhead is justified. A quick task should complete in minutes with minimal review. A deep build might run for hours across multiple phases. Selecting the wrong tier wastes resources: over-planning simple tasks burns tokens on unnecessary architecture; under-planning complex tasks produces shallow output.

**Auto-detection opportunity:** Task complexity could be inferred from the goal description, eliminating manual tier selection. Until then, select explicitly.

### Step 4: Negotiate Sprint Contracts

For campaigns and deep builds, negotiate explicit success criteria before execution begins.

**The pattern:** Before each sprint or phase, the generator proposes implementation scope and success criteria. The evaluator (human or verification agent) reviews and negotiates until both agree on what "done" looks like. These contracts contain granular, testable criteria -- not vague quality standards.

**Example:** Sprint 3 of a retro game project had 27 testable criteria for the level editor alone. Each criterion is independently verifiable, making evaluation deterministic rather than subjective.

**Why this matters:** Without pre-agreed success criteria, evaluation becomes subjective and generators can game vague standards. Sprint contracts surface scope disagreements before coding begins, reducing wasted iteration cycles.

### Step 5: Build Observability

Without observability, debugging agent systems requires reading raw conversation logs. Build structured observability at two levels.

#### Streaming Events (Real-Time)

Emit typed events during execution rather than treating streaming purely as token output:

| Event Type | Purpose | Example |
|------------|---------|---------|
| `message_start` | New agent turn beginning | Track turn count |
| `tool_match` | Tool invocation detected | Monitor tool usage |
| `command_match` | Command execution | Audit side effects |
| `crash` (with reason) | Agent failure | Post-mortem "black box" |
| `budget_warning` | Approaching cost/token limit | Preemptive intervention |

Crash events with a reason field function as a "black box" for post-mortem analysis. Custom event types for domain-specific monitoring (e.g., `finding_extracted`, `source_processed`) provide workflow-level visibility.

#### Distributed Tracing (Post-Hoc)

Standards-based telemetry (OpenTelemetry) linking every component of an agent run into a single trace:

```
user request → retrieval calls → model calls → tool calls → output → evaluation
                                    ↓
                            trace ID links all
```

Each run gets a unique trace ID. The trace enables a structured error taxonomy:

| Failure Type | Root Cause | Fix |
|-------------|-----------|-----|
| Retrieval fail | Wrong documents retrieved | Improve retrieval pipeline |
| Reasoning fail | Model hallucination | Improve prompt, switch model |
| Tool fail | API error, timeout | Fix tool, add retry logic |

Without this taxonomy, teams change prompts when the problem is retrieval, or change models when the problem is a broken API. "If you can't trace it, you can't improve it."

### Step 6: Control Costs

Agent cost blowup is the second most common production failure after context rot. Five mitigation strategies:

**1. Per-step budgets + global budget cap.** Each workflow step has a token/cost budget. The total workflow has a global cap. Exceeding either triggers graceful degradation, not unbounded spending.

**2. Loop termination rules.** Every iterative pattern (generate-critique, retry, search) has explicit maximum iterations. The GSD stall detection pattern monitors issue-count trajectory across revision loop iterations -- when the delta plateaus (agent is not making progress), escalate early rather than waiting for a hard iteration limit.

**3. Caching.** Cache retrieval results and tool outputs to avoid redundant expensive calls. File read deduplication alone eliminates ~18% of redundant reads in production Claude Code.

**4. Model tier routing.** Use expensive models for orchestration and planning; cheap models for narrow sub-tasks. Per-node model selection in workflow DAGs prevents the common anti-pattern of running Opus for every step. See G3, Step 5 for the full routing table.

**5. Fast-fail on missing evidence.** Agents refuse to proceed ("insufficient evidence") rather than hallucinating to fill gaps. This prevents cascading token waste on bad premises.

**Stall detection:** Monitor revision loops for plateauing issue counts across iterations. An agent stuck at 5 issues for 3 iterations is stalled even though 5 is below most absolute thresholds. Combine trajectory monitoring (catches subtle stalls), hard stop gates (catches everything), and consecutive-call guards (prevents runaway autonomous execution) for defense in depth.

### Step 7: Define Degradation Modes

When agents fail, they should degrade gracefully rather than hallucinate or crash silently. Four degradation modes:

| Mode | When to Use | Behavior |
|------|-------------|----------|
| **Retrieval-only fallback** | Planning fails | Skip planning, answer from retrieved evidence |
| **Clarification request** | Inputs ambiguous | Ask for clarification instead of guessing |
| **Human escalation** | Confidence below threshold | Escalate with full context to human review |
| **Partial answer with uncertainty** | Some parts answerable | Return confident parts, mark uncertain parts explicitly |

These are paired with **hard budget enforcement**: maximum tool calls per run, token budget per phase, wall-clock time limits, max context size, approval thresholds for privileged actions. When budgets are exceeded, the agent enters a degradation mode rather than continuing to spend.

**The key insight:** Most agent failures in production are not binary (works / does not work). They are degraded states where the agent produces plausible but incorrect output. Explicit degradation modes make failure visible and controlled rather than silent and compounding.

### Step 8: Calibrate Delivery to Review Bandwidth

AI generates at 100x; organizations review at 3x. Each review layer adds ~10x wall-clock time. Two strategies:

#### Quality at Source (Deming)

Build quality into generation rather than adding review layers after the fact. Every review/approval layer is overhead -- the structural fix is eliminating the need for review, not speeding it up.

- Linting, type-checking, and test-on-write during generation
- Sprint contracts that define success criteria before coding (Step 4)
- Schema validation at every boundary (see G3, Step 4)
- Deterministic execution rails that prevent creative detours (Step 1)

The "AI Developer's Descent into Madness" cycle: generate code -> find bugs -> add review agents -> need a framework to coordinate agents -> repeat. Quality at source breaks this cycle.

#### Staged Delivery

Deliver work in reviewer-calibrated chunks, not agent-calibrated chunks.

```
Agent production capacity:  [========================================]  500 lines
Reviewer absorption capacity:  [==========]  ~100 lines per sitting

Split into staged deliveries:
  Stage 1: [==========]  independently reviewable
  Stage 2: [==========]  independently reviewable
  Stage 3: [==========]  independently reviewable
  ...
```

Each stage is independently reviewable and reversible. The chunk size is calibrated to the reviewer's demonstrated capacity, not the agent's production speed. A phase that produces 500 lines of changes may need further splitting if the reviewer cannot meaningfully evaluate 500 lines at once.

### Step 9: Configure Scheduling and Long-Running Execution

For agents that run on schedules, as background workers, or across multi-day autonomous sessions.

#### In-Session Scheduling

Claude Code's `/loop` command creates persistent background tasks within a session:

```
/loop 5m "check CI pipeline status and report failures"
```

Three scheduling surfaces with increasing persistence:
1. `/loop` -- CLI-based, session-bound, up to 50 concurrent tasks, auto-expire after 3 days
2. Desktop Scheduled Tasks -- GUI-based, machine-bound, persistent across sessions
3. Cloud Scheduled Tasks -- Anthropic infrastructure, runs when machine is off

**Use cases:** PR babysitting, deployment monitoring, CI pipeline polling, code quality scans, daily summaries.

#### Multi-Day Autonomous Execution

For extended autonomous sessions (validated by Anthropic's multi-day scientific computing workflows):

1. **CLAUDE.md as iterative plan:** High-level goals, design decisions, deliverables. The agent references it continuously and edits it iteratively.
2. **CHANGELOG.md as long-term memory:** "Lab notes" logging completed tasks, failed approaches (preventing re-attempts of dead ends), accuracy checkpoints, and limitations.
3. **Test oracle against reference implementation:** Continuous testing against a known-good reference. Essential for deeply coupled pipelines where errors propagate causally.
4. **Git for crash recovery:** Commit and push after every meaningful work unit. Provides recoverable history and resilience to compute interruptions (e.g., SLURM HPC cluster timeouts).

This pattern compresses months of domain work into days by shifting the human role from line-by-line coding to occasional oversight and plan refinement.

### Step 10: Route to the Right Workflow

As agent ecosystems grow, users face a discovery problem: which workflow or skill should I use?

**Context-aware routing** inspects installed capabilities, checks project state, and recommends the appropriate next action. The BMAD Help pattern: (1) inspect all installed modules and skills, (2) check whether the user has completed prior project steps, (3) interpret user intent, (4) recommend the appropriate workflow with exact commands to run.

Adaptive routing can recommend skipping phases based on context (e.g., skip brainstorming if the idea is already solid). This prevents both under-planning (jumping to execution without preparation) and over-planning (running full analysis on a task that needs a quick fix).

#### Cloud-Local Handoff

When planning and execution happen in different environments:

```
Local draft → Cloud refinement (critique, multi-agent analysis) → Teleport back → Local execution
```

The "start new session" option when teleporting back prevents stale conversation history from contaminating execution. The plan text is the handoff artifact; relevant local context (which files were read, what errors were encountered) may need to be re-discovered.

---

## Templates

### Workflow Execution Specification

```markdown
## Workflow Specification -- {{WORKFLOW_NAME}}

### Complexity Tier
- Tier: {{QUICK_TASK/CAMPAIGN/DEEP_BUILD}}
- Estimated duration: {{DURATION}}
- Review cadence: {{REVIEW_FREQUENCY}}

### Plan-Execute-Verify Boundary
- Planning mode: {{LLM_PLANNING/HUMAN_PLANNING/HYBRID}}
- Execution mode: {{DETERMINISTIC/YAML_DAG/MANUAL}}
- Verification mode: {{SCHEMA_VALIDATION/TEST_SUITE/LLM_REVIEW/HUMAN_GATE}}

### State Management
- Persistence level: {{FILE_CHECKPOINT/GIT_BASED/EVENT_LOG/DURABLE_ENGINE}}
- Workflow states: {{LIST_OF_STATES}}
- Idempotent tool calls: {{YES/NO}} -- non-idempotent calls: {{LIST}}
- Crash recovery: {{RESUME_FROM_CHECKPOINT/REPLAY_FROM_LOG/RESTART}}

### Budget Controls
- Per-step token budget: {{TOKENS}}
- Global workflow budget: {{TOKENS_OR_DOLLARS}}
- Loop iteration limit: {{MAX_ITERATIONS}}
- Wall-clock limit: {{HOURS}}
- Stall detection: {{TRAJECTORY_MONITORING/HARD_STOP/BOTH}}

### Degradation Modes
| Trigger | Mode | Behavior |
|---------|------|----------|
| Planning failure | {{MODE}} | {{BEHAVIOR}} |
| Budget exceeded | {{MODE}} | {{BEHAVIOR}} |
| Confidence below threshold | {{MODE}} | {{BEHAVIOR}} |
| Tool failure | {{MODE}} | {{BEHAVIOR}} |

### Observability
- Streaming events: {{EVENT_TYPES}}
- Trace ID assignment: {{YES/NO}}
- Error taxonomy: retrieval / reasoning / tool
- Cost attribution: {{PER_STEP/PER_AGENT/GLOBAL_ONLY}}

### Delivery
- Chunk size: {{LINES_OR_UNITS}} (reviewer-calibrated)
- Stage boundaries: {{DESCRIPTION}}
- Sprint contracts: {{YES/NO}} -- criteria count per sprint: {{N}}

### Scheduling (if applicable)
- Schedule type: {{ONE_SHOT/LOOP/DESKTOP/CLOUD}}
- Interval: {{INTERVAL}}
- Expiry: {{DURATION}}
- Long-running strategy: {{CLAUDE_MD_PLAN/CHANGELOG_MEMORY/GIT_PERSISTENCE}}
```

**Variable Reference:**

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `WORKFLOW_NAME` | string | Yes | Human-readable workflow identifier |
| `QUICK_TASK/CAMPAIGN/DEEP_BUILD` | enum | Yes | Complexity tier determining planning depth |
| `TOKENS` | number | Yes | Token budget per step |
| `MAX_ITERATIONS` | number | Yes | Loop termination ceiling |
| `MODE` | enum | Yes | Degradation mode (retrieval-only / clarification / escalation / partial) |

### Sprint Contract

```markdown
## Sprint Contract -- {{SPRINT_NAME}}

### Scope
- Sprint goal: {{GOAL}}
- Deliverables: {{LIST}}
- Out of scope: {{EXCLUSIONS}}

### Success Criteria
| # | Criterion | Testable | Verification Method |
|---|-----------|----------|-------------------|
| 1 | {{CRITERION}} | {{YES}} | {{METHOD}} |
| 2 | {{CRITERION}} | {{YES}} | {{METHOD}} |
| ... | ... | ... | ... |

### Budget
- Token budget: {{TOKENS}}
- Iteration limit: {{MAX_ITERATIONS}}
- Wall-clock limit: {{HOURS}}

### Negotiation
- Generator proposed: {{DATE}}
- Evaluator approved: {{DATE}}
- Modifications from negotiation: {{CHANGES}}
```

### Cost Control Checklist

```markdown
## Cost Control Audit -- {{SYSTEM_NAME}}

### Budget Controls
- [ ] Per-step token budgets defined: {{BUDGET_PER_STEP}}
- [ ] Global workflow budget cap: {{GLOBAL_CAP}}
- [ ] Loop termination rules for every iterative pattern
- [ ] Stall detection monitoring issue-count trajectory
- [ ] Hard stop gates as absolute iteration ceilings
- [ ] Consecutive-call guards for autonomous execution

### Caching
- [ ] Retrieval results cached
- [ ] Tool outputs cached for idempotent calls
- [ ] File read deduplication enabled

### Model Routing
- [ ] Per-node model selection (not one model for everything)
- [ ] Expensive models reserved for planning/orchestration
- [ ] Cheap models used for classification, extraction, batch work

### Fast-Fail
- [ ] Agents refuse to proceed on insufficient evidence
- [ ] Hallucination-to-fill-gaps explicitly prohibited
- [ ] Partial answers with uncertainty markers preferred over fabrication

### Monitoring
- [ ] Cost-per-successful-task tracked
- [ ] Budget warnings emitted before limits hit
- [ ] Degradation mode triggered on budget exceedance (not unbounded spend)
```

---

## Worked Example: Research-Loop Workflow Execution

How the Improvement Loop's research extraction workflow implements these execution patterns.

```
Workflow Specification -- Research Source Extraction

COMPLEXITY TIER: Campaign (multiple sources, parallel extraction)

PLAN-EXECUTE-VERIFY BOUNDARY:
- Planning: Human selects sources + orchestrator allocates to subagents
- Execution: Each subagent runs finding extraction deterministically
  against the finding template (schema-first, not freeform)
- Verification: Human gate reviews each finding before KB commit
  Quality-at-source via template constraints, not post-hoc review agents

STATE MANAGEMENT:
- Persistence: PROGRESS.md (Level 1 file checkpoint)
- Workflow states: sources_selected → extracting → extracted →
  human_review → committed
- Crash recovery: Resume from PROGRESS.md; re-extract only
  uncommitted sources
- Gap: No automated state tracking; manual checkpoint discipline

BUDGET CONTROLS:
- Per-source token budget: ~50K tokens (Sonnet)
- Global session budget: Managed by Claude Code Max subscription
- Loop termination: Each subagent extracts one source, then stops
  (no iterative refinement loops)
- Stall detection: Not applicable (single-pass extraction)

DEGRADATION MODES:
- Source fetch failure → Skip source, log in delta report
- Extraction quality below threshold → Flag for human review
  rather than re-extracting (fast-fail over retry-loop)
- Context window exceeded → Split source into chunks, extract
  per-chunk (documented in skill)

OBSERVABILITY:
- Delta reports serve as structured event summary per session
- No real-time streaming events (gap)
- No distributed tracing (gap)
- Error taxonomy implicit in delta report: source unreachable
  (retrieval) vs bad extraction (reasoning) vs tool error

DELIVERY:
- Chunk size: One delta report per session (~10-20 findings)
- Human reviews findings in report format, not individual files
- Stage boundary: extraction complete → identification →
  artifact drafting (each stage is a separate session)

SCHEDULING:
- One-shot per research session (not scheduled)
- Future: /loop-based periodic scanning of watched blogs/libraries
```

---

## Pitfalls

### 1. Mixing planning and execution
When LLM reasoning and side-effect execution happen in the same step, hallucinations can trigger irreversible actions. Separate them: probabilistic planning, deterministic execution, verification before proceeding. The agent decides what; the infrastructure decides how and when.

### 2. Skills that contain processes
A skill that has multi-step conditional logic with branching is not a skill -- it is a process wearing a skill's clothes. Skills should be atomic capabilities. Processes should be deterministic sequences that invoke skills. Audit for this confusion when workflows produce inconsistent results.

### 3. Conversation state as workflow state
Without explicit workflow state separation, retrying after a crash re-executes side effects (duplicate API calls, double writes). Track `planned -> awaiting_approval -> executing -> waiting_on_external` as a state machine independent of the conversation transcript.

### 4. No cost controls
A single infinite loop or poorly-configured retry can consume an entire budget in minutes. Per-step budgets, loop termination rules, and fast-fail on missing evidence are not optional -- they are the difference between a controlled system and an expensive random walk.

### 5. Silent degradation
Most agent failures are not binary. Agents produce plausible but incorrect output. Without explicit degradation modes, these failures compound silently. Make failure visible: retrieval-only fallback, clarification requests, human escalation, partial answers with uncertainty markers.

### 6. Generating faster than reviewing
The 100x/3x mismatch means review becomes the bottleneck. Adding review agents creates the "Descent into Madness" cycle (more agents -> more framework -> more agents). Build quality at source and deliver in reviewer-calibrated chunks.

### 7. No persistence for long-running work
30+ minute sessions are common. A crash without persistence means complete loss. At minimum, persist state to a file after every significant event. For multi-day autonomous work, git-based persistence is validated at scale.

### 8. Unstructured observability
Reading raw conversation logs to debug agent failures is unsustainable. Without typed events and distributed tracing, you cannot distinguish retrieval failures from reasoning failures from tool failures -- and each requires a different fix.

---

## Related Guides

- **Execution patterns <- architecture decisions:** The topology and composition patterns in *Agent Architecture Decisions* (G3) determine what workflows you need to implement here.
- **Workflow state -> session persistence:** The persistence patterns in Step 2 are expanded in *Session Persistence and Memory* (G7).
- **Model routing -> cost control:** The model routing table in G3, Step 5 is a key input to cost management (Step 6).
- **Sprint contracts -> agent specifications:** The contract negotiation pattern (Step 4) extends the contract design in *Writing Agent Specifications* (G1).
- **Quality at source -> evaluation:** The quality-at-source strategy (Step 8) connects to the evaluation frameworks in *Building Agent Evaluation Suites* (G4).
- **Observability -> context engineering:** The tracing and event patterns (Step 5) complement context management strategies in *Managing Agent Context* (G2).
- **Scheduled tasks and proactive loops:** *[[building-agentic-systems]]* (G11) Sections 4 (Ingestion) and 6 (Proactive Loops) build on G3b's operational primitives — durable workflows, scheduled execution, and observability patterns.

---

## Contract

### Preconditions
- Agent architecture has been chosen (topology, composition pattern, model routing) per G3.
- The workflow involves side effects (file writes, API calls, deployments) or runs longer than a single interactive turn.
- You have identified what "done" looks like for the workflow (acceptance criteria exist).

### Invariants
- Planning is probabilistic; execution is deterministic. LLMs decide what; infrastructure decides how and when.
- Every workflow has explicit state tracking independent of conversation history.
- Every iterative pattern has a termination condition (loop limit, stall detection, or both).
- Degradation modes are defined before the system goes live, not designed after the first failure.
- Delivery chunk size is calibrated to reviewer capacity, not agent production speed.
- Cost controls (budgets, termination rules, caching, fast-fail) are in place before autonomous execution.

### Governance
- Workflow specifications are documented before execution begins (spec before build).
- Sprint contracts are negotiated and approved before each sprint or phase.
- Cost monitoring data is reviewed periodically to detect drift.
- Observability infrastructure is treated as a first-class requirement, not an afterthought.
- This guide is owned by the Meta-System knowledge layer and updated when new execution findings are integrated.

### Recovery
- If workflows fail silently: add observability first (Step 5). You cannot fix what you cannot see.
- If costs explode: add per-step budgets and loop termination rules (Step 6). Check for stall loops and Opus overuse.
- If crashes lose state: implement workflow state separation (Step 2). Start with file-based checkpoints; upgrade to event logs or durable engines as needed.
- If review becomes the bottleneck: audit quality-at-source practices (Step 8). Reduce review need rather than adding review agents.
- If agents hallucinate on failure: implement explicit degradation modes (Step 7). Clarification requests and partial answers are better than fabricated completions.
- If the wrong workflow runs for a task: implement complexity tiering (Step 3) and context-aware routing (Step 10).
