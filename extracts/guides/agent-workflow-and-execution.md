---
title: "Agent Workflow and Execution"
type: "guideline"
category: "Orchestration"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-04-19"
updated: "2026-07-16"
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
  - "claude-routines-webhook-triggered-pipeline-chaining"
  - "build-loop-skill-autonomous-phase-driver"
  - "cross-project-workflow-portability-register-and-run"
  - "dark-factory-ai-only-codebase-management"
  - "description-based-workflow-routing-lazy-dispatch"
  - "ecosystem-monitoring-meta-loop"
  - "headless-cron-composition-autonomous-scheduled-workflows"
  - "headless-multi-pass-iterative-review"
  - "scheduled-skill-chaining-with-file-based-activation"
  - "self-improvement-dispatch-table-route-never-reimplement"
  - "concept-family-explorer-five-neighborhood-gap-mapping"
  - "scheduled-task-dashboard-observability-layer"
  - "token-budget-pre-turn-projection"
  - "github-label-as-workflow-state"
  - "correct-course-mid-project-pivot-command"
  - "org-redesign-for-agentic-throughput-high-speed-rail"
  - "end-to-end-sequential-bug-fix-pipeline"
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "orchestration"
  - "workflow"
  - "execution"
  - "operations"
  - "scheduling"
  - "autonomy"
contract:
  preconditions: "Agent architecture chosen (see G3); moving to production execution design"
  invariants: "Planning is probabilistic; execution is deterministic; every workflow is observable and recoverable; autonomy is earned per-workflow, never assumed"
  governance: "IL-owned draft; Nick deploys"
  recovery: "If workflows fail silently, add observability first; if costs explode, add budgets; if crashes lose state, add persistence; if unattended runs misbehave, drop an autonomy level"
---

# Agent Workflow and Execution

You have chosen your agent architecture (see *Agent Architecture Decisions*, G3). Now: how do you run it in production? How do you separate planning from execution, persist state across crashes, observe what agents are doing, control costs, handle failures gracefully, deliver work at a pace humans can review, run agents unattended on schedules, and route incoming work to the right workflow?

This guide covers the "how" of agent operations -- workflow engines, execution patterns, observability, cost management, degradation modes, delivery cadence, scheduled and autonomous execution, and workflow routing. It is the production companion to G3's architectural choices.

## When to Use This Guide

- You have an agent architecture and need to implement it with reliable execution.
- Your agents crash mid-task and lose all progress.
- Your agent costs are unpredictable or growing without clear correlation to value.
- You cannot trace what an agent did or why it failed.
- Your agents produce work faster than humans can review it.
- You need to run agents on schedules, as background workers, or fully unattended.
- Your portfolio of scheduled loops is growing and nothing monitors whether they still work.
- You have many workflows and users cannot discover which one to invoke.

**Do not use for:** choosing between single-agent and multi-agent (see G3), specifying what an agent does (see G1), managing context within an agent (see G2), maintaining memory and session continuity (see G7), or evaluating agent output quality (see G4).

## Key Concepts

**1. Planning is probabilistic; execution is deterministic.** The LLM decides what to do. Deterministic infrastructure guarantees it gets done reliably. Never let an LLM decide process flow for operations with irreversible consequences. The corollary at node level: steps that don't need reasoning (formatting, linting, applying a label, triggering a deploy) should be plain code, not LLM calls -- reliability by subtraction.

**2. Skills are not processes.** Agent skills (send email, query DB, compose text) are atomic capabilities. Business processes are deterministic sequences with known handoffs and exception paths. The agent operates within each step; the process flow itself is hardcoded infrastructure.

**3. Workflow state is not conversation state.** "What was said" (transcript) and "what step the agent is on" (state machine) are separate concerns. Separating them makes operations retry-safe -- crashing and restarting will not re-execute side effects. The state store can be as simple as a label set on the work item itself.

**4. Observability is not optional.** "If you can't trace it, you can't improve it." Multi-agent systems fail in ways that are impossible to diagnose without end-to-end tracing. The error taxonomy (retrieval fail vs reasoning fail vs tool fail) determines the fix. As scheduled loops accumulate, observability must extend from single runs to the whole loop portfolio.

**5. Review bandwidth is the bottleneck, not generation speed.** AI accelerates generation 100x but review capacity grows only 3x. Every additional review layer adds ~10x wall-clock time. Build quality at source; deliver in reviewer-calibrated chunks. At organizational scale this means redesigning around handoff points, not piling review work on the same team.

**6. Autonomy is earned per-workflow, then oversight is subtracted.** Unattended execution is a trust decision, not a configuration flag. The decision criterion for going headless is output verifiability: only run unattended what is easy to verify after the fact. Stay at supervised operation until a specific workflow has earned trust, then remove oversight from that workflow -- never leap to full autonomy in one step.

**7. Route work; never re-implement.** As workflows multiply, discovery becomes the problem. Match intent against short descriptions (lazy-load the full definition after routing), classify by owning surface, and route to the workflow that owns the work. A workflow that quietly re-implements another's job grows without bound.

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

#### Deterministic Nodes for Non-Reasoning Steps

Within a workflow, audit every node: does this step actually need an LLM? Steps that are pure mechanics -- fetching a list of issues, reading a rules file, applying a label, running a linter, triggering a deploy -- should be plain code. Production autonomous pipelines apply this systematically: a triage workflow fetches untriaged issues deterministically (CLI call), reads governance files deterministically, classifies with an LLM (the one step that needs judgment), then applies labels deterministically. Separating the "decide" step (agentic) from the "act" step (deterministic) is what makes the decision auditable and the action reliable.

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

#### Labels as a Distributed State Machine

For pipelines whose work items already live in an external system (GitHub issues, tickets), encode workflow state as labels on the work item itself rather than in a separate database. A production dark-factory label design:

| Label | State Meaning |
|-------|--------------|
| `factory-accepted` | Triage classified as in-scope |
| `factory-rejected` | Triage classified as out-of-scope |
| `in-progress` | Implementation workflow currently running |
| `needs-fixed` | Implementation failed; awaiting retry or human |
| `needs-human` | Failed 2+ times or flagged ambiguous; requires human review |
| `factory-rate-limit` | Daily spend limit reached; pause until reset |

The orchestrator reads labels before dispatching: no label means eligible for triage; `in-progress` means skip (already being processed); `needs-human` means skip until a human clears it. This solves the double-dispatch problem (two orchestrator cycles picking up the same item) without a separate state store, and provides free observability -- a human scanning the issue list sees the full pipeline state with no dashboard. Guard against orphaned `in-progress` labels: a workflow that crashes without cleanup strands its item forever unless a timeout mechanism auto-clears stale labels.

#### Session Persistence Patterns

Three levels of persistence, from simplest to most robust:

**Level 1: File-based checkpoints.** Persist state to a file (PROGRESS.md, JSON checkpoint) after every significant event. On recovery, load the file and reconstruct state.

```
load(checkpoint_file) → reconstruct(state) → restore(session)
```

**Level 2: Git-based persistence.** Commit and push after every meaningful work unit. Provides recoverable history, visible progress, and resilience to compute interruptions. Validated by Anthropic's multi-day scientific computing workflow where Claude ran autonomous multi-day sessions reimplementing a cosmological Boltzmann solver, using git commits as the persistence layer.

**Level 3: Append-only event log.** Externalize session state as an append-only stream of events outside both the context window and the sandbox. Three core APIs: `getSession(id)` fetches the log, `wake(sessionId)` reboots from the log, `emitEvent(id, event)` appends events durably. The log supports flexible context slicing via `getEvents()` -- rewind for additional context, fast-forward to resume. Prior approaches (compaction, trimming) make irreversible cuts; the event log preserves everything and lets the brain select what to load.

For deeper treatment of session persistence and memory, see *Session Persistence and Memory* (G7).

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

Without observability, debugging agent systems requires reading raw conversation logs. Build structured observability at three levels: real-time events within a run, post-hoc traces across a run, and portfolio health across all recurring runs.

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

#### Scheduled-Task Dashboard (Management Layer)

Once agents run on schedules, per-run observability is not enough -- you need a single pane showing every scheduled task: active/inactive state, last-run status, next scheduled run, and links to output logs. Without it, scheduled tasks become invisible infrastructure whose failures surface only when someone happens to look. Anthropic ships this natively for cloud routines (grid view, calendar view, "Run Now" test button, per-run transcript with full tool-call trace); local schedulers need at minimum a status file per job (last-run timestamp, last-run outcome). Beware the false-green trap: a green status means the task ran without error, not that it produced correct output -- pair the dashboard with output spot-checks.

#### Portfolio Health: The Loop That Manages Loops

Every scheduled loop added to a system adds operational debt. As the portfolio grows, run a periodic meta-loop with three mechanisms:

1. **Shared run-log utility.** Every loop calls one shared `write-run-log` skill that writes results to a single folder. One place to update logging; one place to read health. Cross-referencing the logs shows which loops are silently broken or no longer earning their tokens -- most loop operators are burning tokens on loops worth killing, and this makes them visible enough to turn off.
2. **Convention-based discovery.** Name every loop `<name>-loop` and have the meta-loop glob for the pattern each run. New loops are picked up automatically; there is no registry file to maintain or drift.
3. **Composability scan.** Scan the loop library for logic repeated across loops (two loops both fetching the same data) and propose extracting it into a shared skill -- but only on clear recurrence (2-3+ repetitions), not first duplication.

Caveat: the meta-loop is itself a loop. It can fail silently, and nothing monitors the monitor -- keep its output on a surface a human actually sees.

### Step 6: Control Costs

Agent cost blowup is the second most common production failure after context rot. Six mitigation strategies:

**1. Per-step budgets + global budget cap.** Each workflow step has a token/cost budget. The total workflow has a global cap. Exceeding either triggers graceful degradation, not unbounded spending.

**2. Pre-turn budget projection.** Project the token cost of each call *before* making it; if the projection exceeds the remaining budget, stop before the call, not after. Post-hoc limits waste the final call's cost; pre-turn projection catches overruns before they happen. Configuration: max turns, max tokens, compaction threshold. Watch for over-conservative projections that stop agents too early.

**3. Loop termination rules.** Every iterative pattern (generate-critique, retry, search) has explicit maximum iterations. The GSD stall detection pattern monitors issue-count trajectory across revision loop iterations -- when the delta plateaus (agent is not making progress), escalate early rather than waiting for a hard iteration limit.

**4. Caching.** Cache retrieval results and tool outputs to avoid redundant expensive calls. File read deduplication alone eliminates ~18% of redundant reads in production Claude Code.

**5. Model tier routing.** Use expensive models for orchestration and planning; cheap models for narrow sub-tasks. Per-node model selection in workflow DAGs prevents the common anti-pattern of running Opus for every step. See G3, Step 5 for the full routing table.

**6. Fast-fail on missing evidence.** Agents refuse to proceed ("insufficient evidence") rather than hallucinating to fill gaps. This prevents cascading token waste on bad premises.

**For unattended pipelines, add batch caps and rate-limit states.** An autonomous pipeline triggered by external input (issue queues, webhooks) must cap work per cycle (e.g., 10 issues per orchestrator run) so an input spike cannot cause runaway spend, and must have an explicit rate-limit state (e.g., a `factory-rate-limit` label) that pauses all dispatch when the daily budget is hit. Scheduled runs burn tokens continuously; a misconfigured cron job is an unbounded liability without these caps. Multi-pass patterns multiply fast -- 5 review iterations x 7 sub-agents is 35 invocations per PR -- so add a cost-estimate gate before execution.

**Stall detection:** Monitor revision loops for plateauing issue counts across iterations. An agent stuck at 5 issues for 3 iterations is stalled even though 5 is below most absolute thresholds. Combine trajectory monitoring (catches subtle stalls), hard stop gates (catches everything), and consecutive-call guards (prevents runaway autonomous execution) for defense in depth. In multi-agent pipelines, also watch for handoff stalls: an agent waiting on input from a crashed upstream agent waits forever for an input that is never going to arrive -- detect these with per-stage timeouts.

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

**Escalation ladders for autonomous pipelines.** In unattended operation, "human escalation" needs a concrete trigger: after N failed attempts (2 is a common production value) or an ambiguity flag from the classifier, mark the item for human review (`needs-human`) and stop retrying. Without a retry ceiling, a failing item consumes budget indefinitely; without the explicit escalation state, it fails silently.

#### Course Correction: Structured Mid-Workflow Pivots

Degradation modes handle failures; course correction handles scope changes. When reality invalidates the plan mid-execution (a forgotten requirement, a new dependency, a significant scope change), do not hack the change into the running plan or restart from scratch. Run a structured correct-course procedure:

1. Analyze how far execution has progressed (completed units, in-progress work)
2. Decide: revert to an earlier stage, re-plan forward from current state, or recommend a restart
3. Identify which planned units need modification, addition, or removal
4. Update upstream artifacts (plan, spec, architecture doc) as explicit side effects
5. Produce a revised backlog that preserves completed work

This is the escape hatch that makes plan-heavy execution survivable when it meets reality. Watch for over-conservative recommendations (full restart when incremental adjustment would suffice); the quality of the correction depends on how well the current state is readable from artifacts -- another reason for Step 2's explicit state.

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

#### Organizational Redesign: The High-Speed Rail

When agents 10x production capacity, the bottleneck moves to human evaluation -- and the fix is organizational, not just technical. The operating analogy: agent workflows are a high-speed rail running through the middle of a highway. The rail is dedicated infrastructure no human touches while trains move; humans drive on the highway (adjacent work) and cluster at the stations -- the handoff points where data enters the pipeline (design intent, requirements, goal definition) and exits it (evaluation, quality judgment, deployment decision).

Structural implications:

- **Individual contributors become agent managers.** Supervising, directing, and evaluating agent output is a distinct skill set that must be trained, not assumed.
- **Review capacity must be planned alongside production capacity.** A real case: ad creative scaled from 20 to 2,000 pieces -- and the organization then had to invent review-at-scale it had not planned for. Tokens spent on generation that is never reviewed are wasted.
- **Avoid the mini-me fallacy.** An agent configured as a digital copy of one person doing their tasks slightly faster misses the point; the win is agent-first infrastructure with humans providing judgment and direction at the stations.

Do not redesign prematurely: the analogy assumes clean boundaries between agent work and human work, and org change before agent capabilities are proven creates disruption without benefit.

### Step 9: Configure Scheduling and Long-Running Execution

For agents that run on schedules, as background workers, or across multi-day autonomous sessions. Choose the scheduling surface by persistence need, then compose it with the execution patterns below.

#### The Scheduling Surface Ladder

| Surface | Persistence | Best For |
|---------|-------------|----------|
| `/loop` (in-session) | Session-bound; up to 50 concurrent tasks; auto-expire ~3 days | PR babysitting, CI polling, short-horizon monitoring |
| Desktop Scheduled Tasks | Machine-bound, persistent across sessions | Personal recurring workflows on an always-on machine |
| OS scheduler + headless (`cron`/`launchd` + `claude -p`) | Infrastructure-level; survives reboots; integrates with DevOps tooling | Batch tasks, nightly/weekly runs, anything needing full OS capability |
| Cloud routines | Runs when your machine is off; webhook-triggerable | Event-driven pipelines, always-on business processes |

```
/loop 5m "check CI pipeline status and report failures"
```

**Use cases:** PR babysitting, deployment monitoring, CI pipeline polling, code quality scans, daily summaries, morning reports generated before the developer wakes up.

#### Headless Composition Rules

The headless pattern (`claude -p "<prompt>"`) removes the human from the loop entirely -- no conversation, no approvals. Three rules govern safe composition:

1. **Gate on output verifiability.** Only run headless what is easy to verify after the fact. Hard-to-undo operations do not run headless.
2. **Constrain permissions with allowed-tools.** Give the headless agent the minimum tool envelope (read-only for reporting tasks). Autonomy inside a bounded permission envelope is the trust model. Escalate incrementally: start read-only, expand as the workflow earns confidence. Too-restrictive envelopes fail silently, so verify the tool set against the task upfront.
3. **Standardize output.** Headless results should land in a predictable format (JSON, report template, known file path) so downstream automation -- and the Step 5 dashboard -- can consume them.

#### Scheduled Skill Chaining with File-Based Activation

Schedule *workflows*, not single prompts. A single scheduled prompt produces raw output; a chained sequence of skills produces a business-ready deliverable:

```
Weekly digest (Mon 9AM): pull-sources → analyze → generate-drafts → drop in review folder
```

Each skill's output feeds the next; the chain ends at a human review folder, not at publication. Control jobs with file-based activation: each scheduled job has a config entry with an active/inactive flag; the scheduler skips inactive jobs. This runs entirely locally (OS scheduler + headless mode) -- no VPS, no cloud connectors -- and every step is transparent. Two hard-won caveats: a typo in the config silently disables a job, and a failed early step feeds garbage to subsequent steps -- add per-step failure checks and alerting (practitioners report ~20% failure rates in fully autonomous chains, much of it chain-propagation).

#### Event-Driven Pipelines: Webhook-Triggered Routine Chaining

For processes triggered by external events rather than clocks, chain cloud routines via webhooks: an external event (transcript ready, form submitted, contract signed) fires Routine A; A's output triggers Routine B; and so on. Each routine is a discrete, stateless cloud agent with its own SOP prompt and connectors.

This differs from skill chaining in one fundamental way: skill chains run within a single session and share context; routine chains are asynchronous, event-driven, and cross-session. Use routine chains to decompose long-running processes -- instead of one agent session that must survive a 2-hour business cycle, discrete short agents wake at event boundaries. Known gaps to engineer around: no native retry or dead-letter queue (a mid-chain failure stalls silently -- add a fallback notification webhook), per-routine debugging (each routine's run log must be checked individually), and payload schema drift between routines (validate at each boundary, per G3's schema-validation rule).

#### Multi-Day Autonomous Execution

For extended autonomous sessions (validated by Anthropic's multi-day scientific computing workflows):

1. **CLAUDE.md as iterative plan:** High-level goals, design decisions, deliverables. The agent references it continuously and edits it iteratively.
2. **CHANGELOG.md as long-term memory:** "Lab notes" logging completed tasks, failed approaches (preventing re-attempts of dead ends), accuracy checkpoints, and limitations.
3. **Test oracle against reference implementation:** Continuous testing against a known-good reference. Essential for deeply coupled pipelines where errors propagate causally.
4. **Git for crash recovery:** Commit and push after every meaningful work unit. Provides recoverable history and resilience to compute interruptions (e.g., SLURM HPC cluster timeouts).

This pattern compresses months of domain work into days by shifting the human role from line-by-line coding to occasional oversight and plan refinement.

### Step 10: Run Autonomous Pipelines at the Right Autonomy Level

Scheduling removes the human from *when* work runs; autonomy removes the human from *whether the work is right*. Treat them separately, and climb the autonomy ladder deliberately.

#### The Five Autonomy Levels

| Level | Name | Human Role |
|-------|------|-----------|
| 0 | AI as search | Human does the work, AI informs |
| 1 | Coding intern / cruise control | Human directs every step |
| 2 | Pair programmer | Human reviews continuously |
| 3 | Hands-off but monitoring | Human supervises outputs; **recommended operating point for most** |
| 4 | Engineering team with harnesses | Human gates merges/deploys only |
| 5 | Dark factory | No human steering wheel; monitoring dashboards only |

**The production recommendation is level 3, subtracting oversight per-workflow as trust is earned.** The practitioner who built a public level-5 pipeline reported afterward: "it was a lot of work and there were still a million things I needed to do to truly make it reliable" -- and explicitly recommends *against* reaching for level 5. Reliability of the base workflows is necessary but not sufficient; the orchestration layer (spec-to-task splitting, handoff management, duplicate-work and stall detection) is a separate engineering effort on top.

#### Anatomy of a Full Autonomous Pipeline (Dark Factory)

When a pipeline does earn high autonomy, the production-validated shape is:

- **A cron orchestrator** that wakes on schedule, reads workflow state (labels, Step 2), and dispatches work -- with a batch cap per cycle (Step 6).
- **A small set of single-purpose workflows** (triage → implement → validate → fix), each a plan-execute-verify DAG (Step 1), each mixing agentic decision nodes with deterministic action nodes.
- **A governance layer injected everywhere:** a mission file and a rules file included as shared context in every workflow, so autonomous decisions stay anchored to intent.
- **Blind validation:** the validating agent runs regression without knowing what was just implemented, preventing sycophantic confirmation of the implementer's choices (the holdout pattern -- see G4).
- **Human escalation states** built into the state machine (`needs-human` after 2 failures).

Evidence: StrongDM runs a production dark factory shipping AI-authored PRs continuously; Stripe Minion ships 1,300 AI-only harnessed PRs/week with human review. Between those two poles, pick the least autonomy that meets the need.

**The autonomous failure taxonomy** (from the same retrospective): cascading failures; agents stalled waiting on handoffs from crashed agents; evaluation gaming; agents veering off-spec into nonsense task fan-out; and a single spec error amplifying into dozens of shipped deployments -- all with low visibility *by design*, because the whole point is that no one is watching. Every mechanism in Steps 5-7 exists to compensate for exactly this.

#### Single-Invocation Pipeline Automation

Below full autonomy, two mid-ladder patterns convert multi-hour human workflows into one invocation while keeping human gates:

- **Sequential end-to-end pipelines.** Chain every stage of a fixed process in strict order within one orchestrator thread (read ticket → reproduce → research → implement → review → verify → commit → deploy → QA). Stage N cannot start before N-1 completes; sub-agents appear *within* stages (research, review) but results return to the main thread before the next stage. The pipeline encodes institutional process -- you cannot skip verification, you cannot deploy without review. Add conditional halts (if reproduction fails, stop and notify) and human gates before irreversible stages.
- **Autonomous phase drivers.** A driver skill reads a phase-queue state file, dispatches each incomplete phase as a fresh headless subprocess, collects the summary, updates the state file, and loops until all phases complete -- breadth-first across a project (contrast with an iteration loop, which is depth-first on one task). The orchestrator session stays under ~10% context because it only manages dispatch. Known limits: no mid-run human gate (a bad phase poisons subsequent phases), exit-code-only completion checks miss quality failures, and sequential dispatch wastes time on independent phases.
- **Fresh-context multi-pass review.** Run N headless review passes over the same target, each with a fresh context window (no memory of prior passes), each internally fanning out sub-agent reviewers; aggregate all findings, weighting issues flagged by multiple passes. Fresh context eliminates implementation-aware reviewer bias. Budget-gate it first (Step 6) -- the invocation count multiplies quickly.

### Step 11: Route Work to the Right Workflow

As agent ecosystems grow, discovery becomes the bottleneck: which workflow or skill should handle this work? Route deliberately -- and never let one workflow quietly re-implement another's job.

#### Description-Based Lazy Routing

Give every workflow a short natural-language `description` (what it does, when to use it). At routing time, the agent reads *only the descriptions*, matches intent, then loads the selected workflow's full definition. The full specification never enters context until routing is complete. This is lazy loading applied to workflow dispatch: a lightweight routing layer that fits in context cheaply, with full specs deferred until after selection. Failure modes to manage: ambiguous descriptions cause misrouting (add confidence scoring with fallback to human selection), and description drift -- the description no longer matches the workflow after edits to its body (review descriptions whenever the definition changes).

#### Context-Aware Routing

**The BMAD Help pattern:** (1) inspect all installed modules and skills, (2) check whether the user has completed prior project steps, (3) interpret user intent, (4) recommend the appropriate workflow with exact commands to run. Adaptive routing can recommend skipping phases based on context (e.g., skip brainstorming if the idea is already solid). This prevents both under-planning (jumping to execution without preparation) and over-planning (running full analysis on a task that needs a quick fix).

#### Dispatch Tables: Classify by Owning Surface, Never Re-Implement

When one intake surface (a retro loop, a triage skill, a support queue) receives work of many kinds, maintain an explicit dispatch table: one row per work class, each row carrying **signals** (how to recognize the class), **route** (which workflow owns it), and **residual duty** (what the intake surface still does even when routing -- usually recording the routed item). Three rules make it robust:

- **Owning surface decides, not topic.** Classify by asking "which file/workflow, if changed, prevents recurrence?" -- not "what is this about?"
- **Unknown class → hold and flag, never invent a route.** The routing topology is governance; it changes through the gated amendment path, not ad hoc.
- **Recommending a route is autonomous; invoking the routed workflow asks first.** Routing sheds the fix, not the record.

Audit residual-duty rows periodically -- that column is where scope creep hides -- and re-check the table when workflows are added or retired (a stale table routes to dead workflows).

#### Cross-Project Workflow Portability

Decouple workflow definitions from target codebases: workflows live with the orchestrator, projects are registered as lightweight records, and execution targets a registered project at runtime. A "fix issue" workflow written once runs identically across a React app, a Python service, and a Go CLI, because its nodes contain generic prompts the agent interprets in the target's context. This gives teams "define standards once" -- the approved workflow (plan, implement, test, review, PR) applied uniformly across all repos. Guard against generic workflows missing project-specific validation (a TypeScript project needs type-checking even if the generic workflow doesn't mention it) -- support per-project override nodes.

#### Coverage Routing: Explore Before You Build

Routing has a proactive twin: deciding what work *should exist*. When operating a workflow portfolio against a domain, periodically map the domain's conceptual family across five neighborhoods -- parent (what contains this), sibling (what sits alongside it), child (what it decomposes into), adjacent (what overlaps), frontier (what is emerging) -- score the discovered gaps (novelty, usefulness, coverage), and feed only viable gaps to the build workflow with bounded briefs. The division of labor: use the explorer to complete coverage of a domain; invoke the build workflow directly when the topic is already known. Human review gates the scored shortlist, not the full map.

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
- Non-reasoning steps implemented as deterministic nodes: {{YES/NO}} -- LLM-node audit date: {{DATE}}

### State Management
- Persistence level: {{FILE_CHECKPOINT/GIT_BASED/EVENT_LOG/DURABLE_ENGINE}}
- Workflow states: {{LIST_OF_STATES}}
- State store: {{STATE_FILE/LABELS_ON_WORK_ITEM/DATABASE/ENGINE_NATIVE}}
- Idempotent tool calls: {{YES/NO}} -- non-idempotent calls: {{LIST}}
- Crash recovery: {{RESUME_FROM_CHECKPOINT/REPLAY_FROM_LOG/RESTART}}
- Stale in-progress cleanup: {{TIMEOUT_AND_AUTO_CLEAR/MANUAL/NONE}}

### Budget Controls
- Per-step token budget: {{TOKENS}}
- Global workflow budget: {{TOKENS_OR_DOLLARS}}
- Pre-turn projection: {{YES/NO}}
- Loop iteration limit: {{MAX_ITERATIONS}}
- Batch cap per cycle (if externally triggered): {{N_ITEMS}}
- Wall-clock limit: {{HOURS}}
- Stall detection: {{TRAJECTORY_MONITORING/HARD_STOP/BOTH}} + per-stage handoff timeout: {{DURATION}}

### Degradation Modes
| Trigger | Mode | Behavior |
|---------|------|----------|
| Planning failure | {{MODE}} | {{BEHAVIOR}} |
| Budget exceeded | {{MODE}} | {{BEHAVIOR}} |
| Confidence below threshold | {{MODE}} | {{BEHAVIOR}} |
| Tool failure | {{MODE}} | {{BEHAVIOR}} |
| {{N}} failed attempts | Human escalation | Mark {{ESCALATION_STATE}}, stop retrying |

### Observability
- Streaming events: {{EVENT_TYPES}}
- Trace ID assignment: {{YES/NO}}
- Error taxonomy: retrieval / reasoning / tool
- Cost attribution: {{PER_STEP/PER_AGENT/GLOBAL_ONLY}}
- Run-log destination (if recurring): {{SHARED_RUN_LOG_PATH}}

### Delivery
- Chunk size: {{LINES_OR_UNITS}} (reviewer-calibrated)
- Stage boundaries: {{DESCRIPTION}}
- Sprint contracts: {{YES/NO}} -- criteria count per sprint: {{N}}

### Scheduling (if applicable)
- Schedule type: {{ONE_SHOT/LOOP/DESKTOP/OS_CRON_HEADLESS/CLOUD_ROUTINE}}
- Interval or trigger: {{INTERVAL_OR_WEBHOOK_EVENT}}
- Expiry: {{DURATION}}
- Long-running strategy: {{CLAUDE_MD_PLAN/CHANGELOG_MEMORY/GIT_PERSISTENCE}}

### Autonomy
- Autonomy level (0-5): {{LEVEL}}
- Oversight subtracted so far: {{LIST}}
- Trust evidence: {{RUNS_WITHOUT_INTERVENTION/QUALITY_METRICS}}
```

**Variable Reference:**

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `WORKFLOW_NAME` | string | Yes | Human-readable workflow identifier |
| `QUICK_TASK/CAMPAIGN/DEEP_BUILD` | enum | Yes | Complexity tier determining planning depth |
| `TOKENS` | number | Yes | Token budget per step |
| `MAX_ITERATIONS` | number | Yes | Loop termination ceiling |
| `MODE` | enum | Yes | Degradation mode (retrieval-only / clarification / escalation / partial) |
| `LEVEL` | number (0-5) | Yes | Autonomy level per the five-level ladder (Step 10) |
| `N_ITEMS` | number | If externally triggered | Max work items dispatched per orchestrator cycle |

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
- [ ] Pre-turn budget projection (stop BEFORE the over-budget call)
- [ ] Loop termination rules for every iterative pattern
- [ ] Batch cap per cycle for externally-triggered pipelines: {{N_ITEMS}}
- [ ] Rate-limit pause state when daily budget hit
- [ ] Stall detection monitoring issue-count trajectory
- [ ] Per-stage handoff timeouts (no waiting on inputs that will never arrive)
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
- [ ] Non-reasoning steps converted to deterministic nodes (no model at all)

### Fast-Fail
- [ ] Agents refuse to proceed on insufficient evidence
- [ ] Hallucination-to-fill-gaps explicitly prohibited
- [ ] Partial answers with uncertainty markers preferred over fabrication

### Monitoring
- [ ] Cost-per-successful-task tracked
- [ ] Budget warnings emitted before limits hit
- [ ] Degradation mode triggered on budget exceedance (not unbounded spend)
- [ ] Multi-pass patterns cost-estimate-gated before execution
```

### Scheduled Workflow Definition

```markdown
## Scheduled Workflow -- {{JOB_NAME}}

- Active: {{TRUE/FALSE}}                # file-based activation flag
- Surface: {{LOOP/DESKTOP/OS_CRON_HEADLESS/CLOUD_ROUTINE}}
- Schedule or trigger: {{CRON_EXPRESSION_OR_WEBHOOK_EVENT}}
- Skill chain: {{ORDERED_LIST_OF_SKILLS}}
- Output destination: {{REVIEW_FOLDER_OR_REPORT_PATH}}
- Output verifiability: {{HOW_A_HUMAN_CHECKS_THE_RESULT_AFTER_THE_FACT}}
- Allowed tools: {{MINIMUM_TOOL_ENVELOPE}}
- Per-run budget: {{TOKENS_OR_DOLLARS}}
- Failure alerting: {{NOTIFICATION_CHANNEL_OR_NONE}}
- Run log: {{SHARED_RUN_LOG_PATH}}
- Last run / status: {{TIMESTAMP}} / {{OK/FAILED}}   # maintained by the scheduler
```

**Variable Reference:**

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `JOB_NAME` | string | Yes | Unique job identifier (use a `<name>-loop` convention for auto-discovery) |
| `CRON_EXPRESSION_OR_WEBHOOK_EVENT` | string | Yes | Time trigger (cron) or event trigger (webhook source) |
| `ORDERED_LIST_OF_SKILLS` | list | Yes | The chained skills; single-prompt jobs are a chain of one |
| `HOW_A_HUMAN_CHECKS_THE_RESULT` | string | Yes | The output-verifiability gate; if unanswerable, the job must not run headless |
| `MINIMUM_TOOL_ENVELOPE` | list | Yes | Allowed-tools constraint; start read-only, expand as trust is earned |

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
- Future: OS-cron + headless periodic scanning of watched
  blogs/libraries (see second worked example)

AUTONOMY:
- Level 2-3: agent executes, human gates every KB commit
- Oversight subtracted so far: none (human gate is constitutional
  for this workflow -- DD-29)
```

## Worked Example: Scheduled Blog-Watch Run

A filled-in Scheduled Workflow Definition for running the engine's blog monitoring unattended.

```
Scheduled Workflow -- watch-blogs-loop

- Active: true
- Surface: OS_CRON_HEADLESS (launchd + claude -p)
- Schedule or trigger: 0 7 * * 1   (Mondays 07:00)
- Skill chain: /watch-blogs → triage report → queue EXTRACT verdicts
  as research-source entries
- Output destination: operations/research-reports/ (triage report)
- Output verifiability: human reads the Monday triage report; every
  claim links to the post it triages; no KB writes happen in the run
- Allowed tools: Read, Grep, Glob, WebFetch, Write (report path only)
- Per-run budget: ~30K tokens; abort run if projection exceeds budget
  before a fetch batch
- Failure alerting: run failure appends FAILED row to run log AND
  drops a flag file the next interactive session surfaces
- Run log: operations/self/run-logs/watch-blogs-loop.md
- Last run / status: 2026-07-14 07:00 / OK
```

Note what makes this safe to run unattended: the run is read-only against the KB (triage only -- extraction still passes the human gate), the output is a single reviewable report (verifiability), the tool envelope is minimal, and failure is loud (run log + flag file) rather than silent.

---

## Pitfalls

### 1. Mixing planning and execution
When LLM reasoning and side-effect execution happen in the same step, hallucinations can trigger irreversible actions. Separate them: probabilistic planning, deterministic execution, verification before proceeding. The agent decides what; the infrastructure decides how and when.

### 2. Skills that contain processes
A skill that has multi-step conditional logic with branching is not a skill -- it is a process wearing a skill's clothes. Skills should be atomic capabilities. Processes should be deterministic sequences that invoke skills. Audit for this confusion when workflows produce inconsistent results.

### 3. Conversation state as workflow state
Without explicit workflow state separation, retrying after a crash re-executes side effects (duplicate API calls, double writes). Track `planned -> awaiting_approval -> executing -> waiting_on_external` as a state machine independent of the conversation transcript.

### 4. No cost controls
A single infinite loop or poorly-configured retry can consume an entire budget in minutes. Per-step budgets, pre-turn projection, loop termination rules, and fast-fail on missing evidence are not optional -- they are the difference between a controlled system and an expensive random walk.

### 5. Silent degradation
Most agent failures are not binary. Agents produce plausible but incorrect output. Without explicit degradation modes, these failures compound silently. Make failure visible: retrieval-only fallback, clarification requests, human escalation, partial answers with uncertainty markers.

### 6. Generating faster than reviewing
The 100x/3x mismatch means review becomes the bottleneck. Adding review agents creates the "Descent into Madness" cycle (more agents -> more framework -> more agents). Build quality at source, deliver in reviewer-calibrated chunks, and plan review capacity alongside production capacity.

### 7. No persistence for long-running work
30+ minute sessions are common. A crash without persistence means complete loss. At minimum, persist state to a file after every significant event. For multi-day autonomous work, git-based persistence is validated at scale.

### 8. Unstructured observability
Reading raw conversation logs to debug agent failures is unsustainable. Without typed events and distributed tracing, you cannot distinguish retrieval failures from reasoning failures from tool failures -- and each requires a different fix.

### 9. Scheduling without failure alerting
A scheduled job that fails silently produces its bad output (or no output) every cycle until someone happens to notice -- a bad morning-report template makes bad reports every day. File-based activation flags fail silently on typos; laptops close; schedulers stop. Every scheduled job needs loud failure (notification, run-log FAILED row, flag file) and a dashboard row showing last-run status. Green status means "ran without error," not "output was correct" -- spot-check outputs too.

### 10. Leaping to the dark factory
Full autonomy (level 5) before per-workflow trust is earned produces the autonomous failure taxonomy at full blast: cascading failures, stalled handoffs, evaluation gaming, spec errors amplified into dozens of shipped deployments -- all invisible by design. The practitioner consensus, including from those who built one: stay at supervised level 3 and subtract oversight workflow-by-workflow. The orchestration layer of a high-autonomy pipeline is a separate engineering effort; budget for it or don't climb.

### 11. Loop sprawl without a portfolio monitor
Each scheduled loop added is standing operational debt. Without a shared run log and periodic portfolio review, broken and useless loops silently burn tokens indefinitely. Use convention-based discovery (no registry to drift) and remember the monitor is itself a loop -- its output must land where a human looks.

### 12. Routing by memory instead of by description
When workflow discovery depends on the human remembering what exists, the human is the router and the bottleneck. Ambiguous or stale workflow descriptions misroute work; workflows that quietly re-implement each other's jobs grow without bound. Maintain routable descriptions, re-check them when definitions change, and classify by owning surface with an explicit dispatch table.

---

## Related Guides

- **Execution patterns <- architecture decisions:** The topology and composition patterns in *Agent Architecture Decisions* (G3) determine what workflows you need to implement here. G3's loop-anatomy and harness-composition patterns are the design-time view of the execution surfaces this guide operates.
- **Workflow state -> session persistence:** The persistence patterns in Step 2 are expanded in *Session Persistence and Memory* (G7).
- **Model routing -> cost control:** The model routing table in G3, Step 5 is a key input to cost management (Step 6).
- **Sprint contracts -> agent specifications:** The contract negotiation pattern (Step 4) extends the contract design in *Writing Agent Specifications* (G1).
- **Quality at source -> evaluation:** The quality-at-source strategy (Step 8) and blind validation (Step 10) connect to the evaluation frameworks in *Building Agent Evaluation Suites* (G4).
- **Observability -> context engineering:** The tracing and event patterns (Step 5) complement context management strategies in *Managing Agent Context* (G2).
- **Autonomy levels -> safety and permissions:** The allowed-tools envelopes and permission escalation in Steps 9-10 connect to *Agent Safety and Permissions* (G6).
- **Scheduled tasks and proactive loops:** *[[building-agentic-systems]]* (G11) Sections 4 (Ingestion) and 6 (Proactive Loops) build on G3b's operational primitives — durable workflows, scheduled execution, and observability patterns.

---

## Contract

### Preconditions
- Agent architecture has been chosen (topology, composition pattern, model routing) per G3.
- The workflow involves side effects (file writes, API calls, deployments), runs longer than a single interactive turn, or runs unattended.
- You have identified what "done" looks like for the workflow (acceptance criteria exist).

### Invariants
- Planning is probabilistic; execution is deterministic. LLMs decide what; infrastructure decides how and when. Steps that need no reasoning are plain code.
- Every workflow has explicit state tracking independent of conversation history.
- Every iterative pattern has a termination condition (loop limit, stall detection, or both); every externally-triggered pipeline has a batch cap and a rate-limit state.
- Degradation modes and escalation states are defined before the system goes live, not designed after the first failure.
- Delivery chunk size is calibrated to reviewer capacity, not agent production speed.
- Cost controls (budgets, pre-turn projection, termination rules, caching, fast-fail) are in place before autonomous execution.
- Nothing runs headless whose output cannot be verified after the fact; autonomy is raised per-workflow as trust is earned, never assumed globally.
- Every scheduled job logs its runs to a shared, human-visible surface and fails loudly.

### Governance
- Workflow specifications are documented before execution begins (spec before build).
- Sprint contracts are negotiated and approved before each sprint or phase.
- Cost monitoring data is reviewed periodically to detect drift.
- Observability infrastructure is treated as a first-class requirement, not an afterthought.
- Autonomy-level changes (subtracting oversight from a workflow) are deliberate, recorded decisions with trust evidence attached.
- Routing topology (dispatch tables, workflow descriptions) is governance -- amended through the gated change path, never ad hoc.
- This guide is owned by the Meta-System knowledge layer and updated when new execution findings are integrated.

### Recovery
- If workflows fail silently: add observability first (Step 5). You cannot fix what you cannot see.
- If costs explode: add per-step budgets, pre-turn projection, and loop termination rules (Step 6). Check for stall loops, missing batch caps, and Opus overuse.
- If crashes lose state: implement workflow state separation (Step 2). Start with file-based checkpoints; upgrade to event logs or durable engines as needed.
- If review becomes the bottleneck: audit quality-at-source practices (Step 8). Reduce review need rather than adding review agents; redesign around handoff points if the mismatch is organizational.
- If agents hallucinate on failure: implement explicit degradation modes (Step 7). Clarification requests and partial answers are better than fabricated completions.
- If the plan is invalidated mid-execution: run the correct-course procedure (Step 7) rather than hacking the change in or restarting from scratch.
- If unattended runs misbehave: drop the workflow one autonomy level (Step 10), re-verify at supervised operation, and re-earn the subtracted oversight.
- If scheduled loops accumulate unmonitored: stand up the shared run-log and portfolio meta-loop (Step 5); kill loops that are not earning their tokens.
- If the wrong workflow runs for a task: implement complexity tiering (Step 3) and deliberate routing (Step 11).
