---
title: "Autonomous and Scheduled Agent Operation"
type: "guideline"
category: "Orchestration"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-07-19"
updated: "2026-07-19"
author: "claude"
source_findings:
  - "claude-code-loop-in-session-cron-scheduling"
  - "headless-cron-composition-autonomous-scheduled-workflows"
  - "scheduled-skill-chaining-with-file-based-activation"
  - "claude-routines-webhook-triggered-pipeline-chaining"
  - "build-loop-skill-autonomous-phase-driver"
  - "dark-factory-ai-only-codebase-management"
  - "multi-day-autonomous-scientific-computing-workflow"
  - "headless-multi-pass-iterative-review"
  - "ecosystem-monitoring-meta-loop"
  - "scheduled-task-dashboard-observability-layer"
  - "github-label-as-workflow-state"
  - "end-to-end-sequential-bug-fix-pipeline"
  - "loop-trigger-taxonomy-poll-then-wake-combo"
  - "loop-contract-anatomy-and-evolve-session-cadence"
  - "pre-merge-reconciliation-queue"
  - "durable-workflow-engine-for-agent-systems"
  - "archon-yaml-defined-harness-workflows"
  - "agent-cost-blowup-mitigation-strategies"
  - "graceful-degradation-modes-for-agent-failure"
  - "durable-checkpointed-sessions-as-framework-default"
source_dd:
  - "DD-81"
  - "DD-122"
tags:
  - "guide"
  - "orchestration"
  - "scheduling"
  - "autonomy"
  - "headless"
  - "operations"
contract:
  preconditions: "A supervised workflow already runs reliably (see G3c); you are removing the human from the loop — scheduling, headless, or autonomous"
  invariants: "Autonomy is earned per-workflow, never assumed; nothing runs headless whose output cannot be verified; every scheduled job logs its runs and fails loudly; mandatory constraints live in structural gates, not prose"
  governance: "IL-owned draft; Nick deploys"
  recovery: "If unattended runs misbehave, drop an autonomy level; if scheduled loops accumulate unmonitored, stand up the shared run-log and portfolio meta-loop; if a must-not action leaks, move it from prose into a hook"
---

# Autonomous and Scheduled Agent Operation

You have a supervised workflow that runs reliably (see *Production Agent Execution*, G3c). Now: how do you run it *unattended* — on a schedule, as a background worker, headless with no human in the loop, or as a fully autonomous pipeline? How do you wake a loop, compose headless steps, govern a recurring automation, observe a whole portfolio of loops, cap costs that would otherwise run continuously, and climb the autonomy ladder without producing the autonomous-failure taxonomy at full blast?

This guide covers unattended operation: scheduling surfaces, trigger shapes, headless composition, skill and routine chaining, loop-contract governance, portfolio observability, and the five autonomy levels. It is the sibling of G3c (they split from one guide per DD-122); the shared substrate — durable execution, cost caps, degradation modes, YAML DAGs — appears in both.

## When to Use This Guide

- You need to run agents on schedules, as background workers, or fully unattended.
- You are removing human approvals from a workflow that has earned trust.
- Your portfolio of scheduled loops is growing and nothing monitors whether they still work.
- You are building an autonomous pipeline (triage → implement → validate → fix) and need to know how autonomous is too autonomous.
- Many agent-authored changes are landing against one codebase and PR-as-unit-of-work is straining.

**Do not use for:** hardening a *supervised* production workflow — plan/execute separation, state, observability, cost, degradation, review bandwidth, routing (see G3c); choosing between single-agent and multi-agent (see G3); specifying what an agent does (see G1); managing context within an agent (see G2); maintaining memory and session continuity (see G7); or evaluating agent output quality (see G4).

## Key Concepts

**1. Autonomy is earned per-workflow, then oversight is subtracted.** Unattended execution is a trust decision, not a configuration flag. The decision criterion for going headless is output verifiability: only run unattended what is easy to verify after the fact. Stay at supervised operation until a specific workflow has earned trust, then remove oversight from that workflow -- never leap to full autonomy in one step.

**2. Scheduling and autonomy are orthogonal.** Scheduling removes the human from *when* work runs; autonomy removes the human from *whether the work is right*. A cron job can still gate every action on a human; a fully autonomous pipeline can be triggered manually. Treat the two axes separately.

**3. "Scheduled" rarely means "native."** Claude Code has no built-in cron -- neither timed nor event-based wake ships with the harness. A cadence you assume is built in is really an external scheduler (OS cron/launchd around `claude -p`, a native-scheduler harness, or an orchestrator wake layer), and event triggers need your own webhook daemon. The wake/dispatch layer fails independently of the work and needs its own observability.

**4. Mandatory constraints belong in gates, not prose.** For an unattended pipeline, anything the agent *must not* do belongs in a `PreToolUse`-equivalent hook or a deny-by-default permission rule that removes the action from the model's option set -- never in a rules file the model may summarize correctly and then stop applying. Intent-anchoring steers judgment; it does not enforce.

**5. Every scheduled job fails loudly and logs to a human-visible surface.** A silently-failing scheduled job produces bad output (or none) every cycle until someone notices. Loud failure (notification, run-log FAILED row, flag file) plus a portfolio dashboard is the price of running anything unattended.

---

## Procedure

### Step 1: Choose the Scheduling Surface and Trigger Shape

For agents that run on schedules, as background workers, or across multi-day autonomous sessions. Choose the scheduling surface by persistence need, then choose how the loop wakes -- these are two orthogonal decisions.

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

#### Trigger Shapes: How the Loop Wakes

The surface ladder above is about *where* a scheduled agent runs and how long its state survives. Orthogonal to it is *how the loop is woken* -- and there are four distinct trigger shapes, not one. Choosing the wrong shape is a common cost and correctness bug.

| Trigger shape | Wakes on | Native support | Best for |
|---------------|----------|----------------|----------|
| **Continuous** | Runs in a while-loop until a goal condition or budget is hit | Native (`go`/goal commands) | Tasks with immediate feedback and a well-defined spec |
| **Cron / schedule** | A fixed time interval | Native (`/loop`, OS cron, cloud routines, Codex Automations) | Recurring monitoring, digests, periodic scans |
| **Event-based** | An external signal (new email, incident, webhook) | **Not native** to Claude Code or Codex -- requires your own local daemon exposing a webhook URL | Things needing immediate handling on an external trigger |
| **Combo / workflow** | A cron ticker runs a **cheap deterministic pre-check** first; only if there is real new work does it wake the expensive LLM agent | Composed from cron + a script | The most useful in practice -- the general cost lever |

**The combo pattern is the concrete cost lever.** A support-inbox loop that polls every 30 minutes and skips the run entirely when nothing changed pays LLM cost only for cycles with real work. Any cron-shaped periodic job -- a blog watcher, an upstream-dependency watcher -- can gain a cheap pre-check (compare a feed's last-modified/etag before invoking the agent subagent) to skip no-op runs. This is the same "decide cheaply, act expensively" subtraction as G3c's deterministic nodes, applied at the wake boundary.

**The scheduling gap.** Claude Code has *no native cron* -- neither timed nor event-based wake is provided by the harness itself, so any scheduled or event-driven cadence must ride an *external* scheduler: OS cron/launchd around `claude -p` (the documented pattern), a native-scheduler harness (Codex Automations is the exception that ships cron/webhook/app-event triggers surviving machine-off), or a workflow-orchestrator wake layer over the harness. Event-based triggers specifically require standing up your own daemon with a webhook endpoint -- there is no built-in listener. Design consequence: a "scheduled" agent operation on a cron-less harness is really *two* components -- the wake/dispatch layer (external) and the work (the harness invocation) -- and they fail independently, so the wake layer needs its own observability (Step 5) just as much as the work does. The harness-landscape survey documents this gap and the option space in full (`operations/plans/memory-spec-inputs/C-synthesis-harness-memory-harmonization.md` §4a, "the scheduling gap bites"): external cron around `claude -p`, a native-scheduler harness, adopting a workflow orchestrator as the wake layer, or a custom scheduler -- an unsettled engineering choice, not a configuration flag.

### Step 2: Compose Headless and Chained Workflows

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

This pattern compresses months of domain work into days by shifting the human role from line-by-line coding to occasional oversight and plan refinement. Durable execution underpins this: prefer a framework-native durable/resumable session primitive where one exists rather than hand-rolling a checkpoint file (see G3c Step 2 and G7 for the framework-default persistence treatment).

### Step 3: Govern Recurring Loops with a Loop Contract

A multi-day session has a start and an end; a *recurring* loop (a nightly triage, a CRM-lifecycle sweep, a documentation-drift check) runs indefinitely and needs a durable home for its own governance and memory. The production pattern is one living markdown file per loop that is simultaneously its constitution and its notebook, with three sections:

- **Contract** -- the loop's goal, its boundaries (what it may do unsupervised vs. what must escalate to a human), and its SOP. This is the always-loaded governance the loop reads on every wake.
- **State** -- deliberately small: current hypothesis, open backlog, and items shipped but needing follow-up. Kept small on purpose so it stays legible and cheap to load.
- **Log** -- append-only, one entry per run: what happened, what was decided, what failed.

This is loop-level self-tuning, distinct in altitude from a system-wide research scan or an engine-wide lesson store -- the contract governs *one* automation. A second cadence rides on top: every 5-10 runs, a dedicated **evolve session** hands the agent its own past contract, its state/log history, and raw run transcripts, and asks it to propose changes to its own contract, prune stale state, or convert a repetitive SOP step into a script. The evolve session is where a loop earns the right to shed a manual step (turn it into deterministic code, per G3c Step 1) or tighten its own boundaries. Governance caveat: proposed changes to a loop's *contract* -- especially its escalation boundaries -- are a human-gated decision, not an autonomous self-rewrite; the evolve session drafts, a human approves. Uncontrolled self-modification of a loop's own governance is exactly the failure mode Step 6's autonomy discipline guards against.

### Step 4: Track Workflow State for Unattended Pipelines

An autonomous orchestrator needs to know which work items are eligible, in-flight, or blocked -- without a human tracking it. For pipelines whose work items already live in an external system (GitHub issues, tickets), encode workflow state as labels on the work item itself rather than in a separate database. A production dark-factory label design:

| Label | State Meaning |
|-------|--------------|
| `factory-accepted` | Triage classified as in-scope |
| `factory-rejected` | Triage classified as out-of-scope |
| `in-progress` | Implementation workflow currently running |
| `needs-fixed` | Implementation failed; awaiting retry or human |
| `needs-human` | Failed 2+ times or flagged ambiguous; requires human review |
| `factory-rate-limit` | Daily spend limit reached; pause until reset |

The orchestrator reads labels before dispatching: no label means eligible for triage; `in-progress` means skip (already being processed); `needs-human` means skip until a human clears it. This solves the double-dispatch problem (two orchestrator cycles picking up the same item) without a separate state store, and provides free observability -- a human scanning the issue list sees the full pipeline state with no dashboard. Guard against orphaned `in-progress` labels: a workflow that crashes without cleanup strands its item forever unless a timeout mechanism auto-clears stale labels. (The general workflow-state-vs-conversation-state separation and idempotent-tool-call discipline this rests on is in G3c Step 2.)

### Step 5: Observe the Loop Portfolio

Per-run observability (streaming events, distributed tracing -- G3c Step 5) is necessary but not sufficient once agents run on schedules. Unattended operation needs two more layers: a dashboard over every scheduled task, and a meta-loop that watches the whole portfolio.

#### Scheduled-Task Dashboard (Management Layer)

Once agents run on schedules, per-run observability is not enough -- you need a single pane showing every scheduled task: active/inactive state, last-run status, next scheduled run, and links to output logs. Without it, scheduled tasks become invisible infrastructure whose failures surface only when someone happens to look. Anthropic ships this natively for cloud routines (grid view, calendar view, "Run Now" test button, per-run transcript with full tool-call trace); local schedulers need at minimum a status file per job (last-run timestamp, last-run outcome). Beware the false-green trap: a green status means the task ran without error, not that it produced correct output -- pair the dashboard with output spot-checks.

#### Portfolio Health: The Loop That Manages Loops

Every scheduled loop added to a system adds operational debt. As the portfolio grows, run a periodic meta-loop with three mechanisms:

1. **Shared run-log utility.** Every loop calls one shared `write-run-log` skill that writes results to a single folder. One place to update logging; one place to read health. Cross-referencing the logs shows which loops are silently broken or no longer earning their tokens -- most loop operators are burning tokens on loops worth killing, and this makes them visible enough to turn off.
2. **Convention-based discovery.** Name every loop `<name>-loop` and have the meta-loop glob for the pattern each run. New loops are picked up automatically; there is no registry file to maintain or drift.
3. **Composability scan.** Scan the loop library for logic repeated across loops (two loops both fetching the same data) and propose extracting it into a shared skill -- but only on clear recurrence (2-3+ repetitions), not first duplication.

Caveat: the meta-loop is itself a loop. It can fail silently, and nothing monitors the monitor -- keep its output on a surface a human actually sees.

### Step 6: Cap Costs for Unattended Runs

Scheduled runs burn tokens continuously; a misconfigured cron job is an unbounded liability. On top of the supervised-execution cost controls (per-step and global budgets, pre-turn projection, loop termination, caching, model routing, fast-fail -- G3c Step 6), unattended pipelines add controls that are existential rather than optional:

**Batch caps per cycle.** An autonomous pipeline triggered by external input (issue queues, webhooks) must cap work per cycle (e.g., 10 issues per orchestrator run) so an input spike cannot cause runaway spend.

**Explicit rate-limit state.** A pipeline needs a rate-limit state (e.g., a `factory-rate-limit` label, Step 4) that pauses all dispatch when the daily budget is hit -- not a soft warning, a hard pause.

**Cost-estimate gate before fan-out.** Multi-pass patterns multiply fast -- 5 review iterations × 7 sub-agents is 35 invocations per PR -- so add a cost-estimate gate before execution.

**Graceful degradation is the failure contract.** When any budget is exceeded, the pipeline enters a degradation mode rather than continuing to spend: retrieval-only fallback, clarification request (queued for a human), human escalation, or partial answer with uncertainty. (The four degradation modes and hard budget enforcement are detailed in G3c Step 7; they are shared substrate.)

**Escalation ladders.** In unattended operation, "human escalation" needs a concrete trigger: after N failed attempts (2 is a common production value) or an ambiguity flag from the classifier, mark the item `needs-human` and stop retrying. Without a retry ceiling, a failing item consumes budget indefinitely; without the explicit escalation state, it fails silently.

### Step 7: Run Autonomous Pipelines at the Right Autonomy Level

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

- **A cron orchestrator** that wakes on schedule, reads workflow state (labels, Step 4), and dispatches work -- with a batch cap per cycle (Step 6).
- **A small set of single-purpose workflows** (triage → implement → validate → fix), each a plan-execute-verify DAG (G3c Step 1), each mixing agentic decision nodes with deterministic action nodes.
- **A governance layer injected everywhere:** a mission file and a rules file included as shared context in every workflow, so autonomous decisions stay anchored to intent. **But intent-anchoring is not enforcement.** The strongest cross-vendor finding in the harness-landscape survey is that safety-critical guardrails must live *outside the model's reach* -- as a `PreToolUse`-equivalent hook or a deny-by-default permission rule that makes the disallowed action invisible -- never as prose in a rules file the model may correctly summarize and then stop applying a few turns later (`operations/plans/memory-spec-inputs/C-synthesis-harness-memory-harmonization.md` §4b, the enforcement-locus consensus, triangulated across three independent LLM-first vendors). For an unattended pipeline this is not optional: the mission/rules file steers judgment, but anything the pipeline *must not* do under any circumstance belongs in a structural gate the agent cannot argue its way past. A source-verified "hard" rule is still only evidence of what is *designed*, not what is *delivered* -- test the leak-prone paths (subagent delegation, resumed/background sessions, mode transitions) with a deliberately seeded violation, because those are exactly where enforcement empirically slips.
- **Blind validation:** the validating agent runs regression without knowing what was just implemented, preventing sycophantic confirmation of the implementer's choices (the holdout pattern -- see G4).
- **Human escalation states** built into the state machine (`needs-human` after 2 failures).

Evidence: StrongDM runs a production dark factory shipping AI-authored PRs continuously; Stripe Minion ships 1,300 AI-only harnessed PRs/week with human review. Between those two poles, pick the least autonomy that meets the need.

**The autonomous failure taxonomy** (from the same retrospective): cascading failures; agents stalled waiting on handoffs from crashed agents; evaluation gaming; agents veering off-spec into nonsense task fan-out; and a single spec error amplifying into dozens of shipped deployments -- all with low visibility *by design*, because the whole point is that no one is watching. Every mechanism in Steps 5-6 (and G3c's observability, cost, and degradation steps) exists to compensate for exactly this.

#### Single-Invocation Pipeline Automation

Below full autonomy, two mid-ladder patterns convert multi-hour human workflows into one invocation while keeping human gates:

- **Sequential end-to-end pipelines.** Chain every stage of a fixed process in strict order within one orchestrator thread (read ticket → reproduce → research → implement → review → verify → commit → deploy → QA). Stage N cannot start before N-1 completes; sub-agents appear *within* stages (research, review) but results return to the main thread before the next stage. The pipeline encodes institutional process -- you cannot skip verification, you cannot deploy without review. Add conditional halts (if reproduction fails, stop and notify) and human gates before irreversible stages.
- **Autonomous phase drivers.** A driver skill reads a phase-queue state file, dispatches each incomplete phase as a fresh headless subprocess, collects the summary, updates the state file, and loops until all phases complete -- breadth-first across a project (contrast with an iteration loop, which is depth-first on one task). The orchestrator session stays under ~10% context because it only manages dispatch. Known limits: no mid-run human gate (a bad phase poisons subsequent phases), exit-code-only completion checks miss quality failures, and sequential dispatch wastes time on independent phases.
- **Fresh-context multi-pass review.** Run N headless review passes over the same target, each with a fresh context window (no memory of prior passes), each internally fanning out sub-agent reviewers; aggregate all findings, weighting issues flagged by multiple passes. Fresh context eliminates implementation-aware reviewer bias. Budget-gate it first (Step 6) -- the invocation count multiplies quickly.

#### When Many Agents Write at Once: The Pre-Merge Reconciliation Queue (Emerging)

As autonomy scales, the unit of work shifts from the diff to the *intent*. A near-term production shape already in use: work starts from a written intent/plan rather than a PR diff, an agent harness checks out a well-known commit and self-validates against the repo's own build/test assets, and a lightweight human check-in ("continue" becomes the most common human utterance) gates progress before a conventional merge queue. The forward-looking extension -- framed as "weeks to months, not years" out by practitioners already living the volume -- is a genuine *reconciliation queue*: with many agent-authored changes in flight against the same codebase simultaneously, changes land in a "pre-merge" queue instead of going straight to the repository, where a reconciliation process resolves them against each other for serializability before the ledger write. The forcing function is volume: teams report PR-equivalent throughput already several times pre-agent levels, and the PR-as-unit-of-work model does not survive that concurrency. Treat this as a horizon signal, not a build-now item -- but if your autonomy climb is producing concurrent writes to one codebase, the merge queue is where contention will first surface, and intent-plus-self-validation (not diff review) is the shape to plan toward.

---

## Templates

### Scheduled Workflow Definition

```markdown
## Scheduled Workflow -- {{JOB_NAME}}

- Active: {{TRUE/FALSE}}                # file-based activation flag
- Surface: {{LOOP/DESKTOP/OS_CRON_HEADLESS/CLOUD_ROUTINE}}
- Trigger shape: {{CONTINUOUS/CRON/EVENT/COMBO}}   # combo = cheap pre-check gates the LLM wake
- External scheduler (if harness has no native cron): {{OS_CRON/LAUNCHD/ORCHESTRATOR/NATIVE}}
- Cheap pre-check before LLM wake (combo only): {{SCRIPT_OR_CHECK_THAT_SKIPS_NO-OP_RUNS}}
- Schedule or trigger: {{CRON_EXPRESSION_OR_WEBHOOK_EVENT}}
- Skill chain: {{ORDERED_LIST_OF_SKILLS}}
- Output destination: {{REVIEW_FOLDER_OR_REPORT_PATH}}
- Output verifiability: {{HOW_A_HUMAN_CHECKS_THE_RESULT_AFTER_THE_FACT}}
- Allowed tools: {{MINIMUM_TOOL_ENVELOPE}}
- Per-run budget: {{TOKENS_OR_DOLLARS}}
- Batch cap per cycle (if externally triggered): {{N_ITEMS}}
- Rate-limit pause state: {{STATE_OR_LABEL_THAT_HALTS_DISPATCH}}
- Failure alerting: {{NOTIFICATION_CHANNEL_OR_NONE}}
- Run log: {{SHARED_RUN_LOG_PATH}}
- Last run / status: {{TIMESTAMP}} / {{OK/FAILED}}   # maintained by the scheduler
- Autonomy level (0-5): {{LEVEL}}
- Oversight subtracted so far: {{LIST}}
- Trust evidence: {{RUNS_WITHOUT_INTERVENTION/QUALITY_METRICS}}
```

**Variable Reference:**

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `JOB_NAME` | string | Yes | Unique job identifier (use a `<name>-loop` convention for auto-discovery) |
| `CRON_EXPRESSION_OR_WEBHOOK_EVENT` | string | Yes | Time trigger (cron) or event trigger (webhook source) |
| `ORDERED_LIST_OF_SKILLS` | list | Yes | The chained skills; single-prompt jobs are a chain of one |
| `HOW_A_HUMAN_CHECKS_THE_RESULT` | string | Yes | The output-verifiability gate; if unanswerable, the job must not run headless |
| `MINIMUM_TOOL_ENVELOPE` | list | Yes | Allowed-tools constraint; start read-only, expand as trust is earned |
| `N_ITEMS` | number | If externally triggered | Max work items dispatched per orchestrator cycle |
| `LEVEL` | number (0-5) | Yes | Autonomy level per the five-level ladder (Step 7) |

### Loop Contract File

One living markdown file per recurring autonomous loop -- its constitution and its notebook (Step 3).

```markdown
# Loop Contract -- {{LOOP_NAME}}

## Contract
- Goal: {{WHAT_THIS_LOOP_EXISTS_TO_DO}}
- May do unsupervised: {{BOUNDED_LIST_OF_AUTONOMOUS_ACTIONS}}
- Must escalate to human: {{ACTIONS_REQUIRING_A_HUMAN_GATE}}
- SOP: {{STEP_BY_STEP_PROCEDURE_LOADED_ON_EVERY_WAKE}}

## State
- Current hypothesis: {{ONE_LINE}}
- Open backlog: {{SHORT_LIST}}
- Shipped, needs follow-up: {{SHORT_LIST}}

## Log
- {{YYYY-MM-DD}} -- {{WHAT_HAPPENED / WHAT_WAS_DECIDED / WHAT_FAILED}}
- (append-only; one entry per run)

<!-- Evolve session (every 5-10 runs): hand the agent this file + run transcripts;
     it drafts contract/state/SOP changes; a human approves boundary changes. -->
```

**Variable Reference:**

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `LOOP_NAME` | string | Yes | Loop identifier (use the `<name>-loop` convention) |
| `BOUNDED_LIST_OF_AUTONOMOUS_ACTIONS` | list | Yes | Exactly what the loop may do without asking; everything else escalates |
| `ACTIONS_REQUIRING_A_HUMAN_GATE` | list | Yes | The escalation boundary — changed only by human-approved evolve sessions |

---

## Worked Example: Scheduled Blog-Watch Run

A filled-in Scheduled Workflow Definition for running the engine's blog monitoring unattended.

```
Scheduled Workflow -- watch-blogs-loop

- Active: true
- Surface: OS_CRON_HEADLESS (launchd + claude -p)
- Trigger shape: CRON (could add a combo pre-check on feed etag to skip no-op weeks)
- External scheduler: LAUNCHD
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
- Autonomy level: 2-3 (triage autonomous; extraction still human-gated)
```

Note what makes this safe to run unattended: the run is read-only against the KB (triage only -- extraction still passes the human gate), the output is a single reviewable report (verifiability), the tool envelope is minimal, and failure is loud (run log + flag file) rather than silent.

---

## Pitfalls

### 1. Scheduling without failure alerting
A scheduled job that fails silently produces its bad output (or no output) every cycle until someone happens to notice -- a bad morning-report template makes bad reports every day. File-based activation flags fail silently on typos; laptops close; schedulers stop. Every scheduled job needs loud failure (notification, run-log FAILED row, flag file) and a dashboard row showing last-run status. Green status means "ran without error," not "output was correct" -- spot-check outputs too.

### 2. Leaping to the dark factory
Full autonomy (level 5) before per-workflow trust is earned produces the autonomous failure taxonomy at full blast: cascading failures, stalled handoffs, evaluation gaming, spec errors amplified into dozens of shipped deployments -- all invisible by design. The practitioner consensus, including from those who built one: stay at supervised level 3 and subtract oversight workflow-by-workflow. The orchestration layer of a high-autonomy pipeline is a separate engineering effort; budget for it or don't climb.

### 3. Loop sprawl without a portfolio monitor
Each scheduled loop added is standing operational debt. Without a shared run log and periodic portfolio review, broken and useless loops silently burn tokens indefinitely. Use convention-based discovery (no registry to drift) and remember the monitor is itself a loop -- its output must land where a human looks.

### 4. Enforcing mandatory constraints in prose instead of in a gate
A rule written into a mission or CLAUDE.md file is a hint the model can correctly summarize and then, a few turns later, stop applying -- production vendors document exactly this drift. Anything an autonomous pipeline *must not* do belongs in a `PreToolUse`-equivalent hook or a deny-by-default permission rule that removes the action from the model's option set entirely, never in prose. And a "hard" rule verified in source is not proof of *delivered* enforcement: test the leak-prone paths -- subagent delegation, resumed/background sessions, mode transitions -- with a deliberately seeded violation, because that is where enforcement empirically slips.

### 5. Assuming "scheduled" means native
Claude Code has no native cron -- neither timed nor event-based wake ships with the harness. A cadence you assume is built in is really an external scheduler you have not yet built (OS cron around `claude -p`, a native-scheduler harness, or an orchestrator wake layer), and event triggers need your own webhook daemon. The wake/dispatch layer fails independently of the work and needs its own observability; a "green" work run says nothing about whether the scheduler fired at all.

### 6. Chain propagation from a failed early step
A scheduled skill chain feeds each step's output to the next. A failed or garbage early step silently poisons everything downstream -- practitioners report ~20% failure rates in fully autonomous chains, much of it chain-propagation. Add per-step failure checks and alerting; do not let a chain run to completion on bad intermediate output.

---

## Related Guides

- **Supervised execution <-:** *Production Agent Execution* (G3c) is this guide's sibling — it covers plan/execute separation, workflow state, per-run observability, cost control, degradation modes, review bandwidth, and routing. The shared substrate (durable execution, cost caps, degradation modes, YAML DAGs) appears in both; this guide references G3c rather than duplicating it.
- **Architecture decisions ->:** The loop-anatomy and harness-composition patterns in *Agent Architecture Decisions* (G3) are the design-time view of the execution surfaces operated here.
- **Long-running state -> session persistence:** Multi-day autonomous execution (Step 2) and the loop contract (Step 3) build on the persistence patterns in *Session Persistence and Memory* (G7).
- **Autonomy levels -> safety and permissions:** The allowed-tools envelopes, permission escalation, and enforcement-locus discipline (Steps 2, 7) connect to *Agent Safety and Permissions* (G6).
- **Blind validation -> evaluation:** The holdout/blind-validation pattern in the dark-factory anatomy (Step 7) connects to *Building Agent Evaluation Suites* (G4).

---

## Contract

### Preconditions
- A supervised version of the workflow already runs reliably (see G3c) — you are removing the human, not building from scratch.
- The workflow runs unattended: on a schedule, as a background worker, headless, or fully autonomous.
- You can state how a human verifies the output after the fact (if you cannot, it must not run headless).

### Invariants
- Autonomy is earned per-workflow and raised one level at a time as trust is demonstrated, never assumed globally.
- Nothing runs headless whose output cannot be verified after the fact.
- Every scheduled job logs its runs to a shared, human-visible surface and fails loudly.
- Every externally-triggered pipeline has a batch cap and a rate-limit pause state.
- Anything the pipeline must not do lives in a structural gate (hook / deny-by-default permission), never in prose the model may stop applying.
- Recurring loops carry a loop contract; changes to a loop's escalation boundaries are human-gated, not autonomous self-rewrites.

### Governance
- Autonomy-level changes (subtracting oversight from a workflow) are deliberate, recorded decisions with trust evidence attached.
- The scheduling/wake layer is treated as a first-class component with its own observability, separate from the work.
- Loop contracts and their escalation boundaries are amended through human-approved evolve sessions, not ad hoc.
- Cost monitoring for continuous runs is reviewed periodically; a misconfigured cron job is treated as an unbounded liability until capped.
- This guide is owned by the IL knowledge layer and updated when new unattended-operation findings are integrated.

### Recovery
- If unattended runs misbehave: drop the workflow one autonomy level (Step 7), re-verify at supervised operation, and re-earn the subtracted oversight.
- If scheduled loops accumulate unmonitored: stand up the shared run-log and portfolio meta-loop (Step 5); kill loops that are not earning their tokens.
- If a scheduled job fails silently: add loud failure (run-log FAILED row, flag file, notification) and a dashboard row (Steps 5, Pitfall 1).
- If a must-not action leaks: move it from prose into a `PreToolUse` hook or deny-by-default permission (Step 7); seed a deliberate violation on the leak-prone paths to confirm enforcement.
- If costs run away on a continuous schedule: add a batch cap and a rate-limit pause state (Step 6); gate multi-pass fan-out on a cost estimate.
- If concurrent agent writes contend on one codebase: plan toward intent-plus-self-validation and a pre-merge reconciliation queue (Step 7), not diff-by-diff review.
