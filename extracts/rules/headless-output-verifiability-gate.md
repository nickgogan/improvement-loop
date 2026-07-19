---
title: "Headless Output Verifiability Gate"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "headless-cron-composition-autonomous-scheduled-workflows"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "autonomous-scheduled-agent-operation.harvest-queue"
identification_report: "autonomous-scheduled-agent-operation.harvest-queue.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "engineers deciding whether a task is a fit for headless / unattended / scheduled agent execution at all — the go/no-go call made before any cron entry or background run is configured"
    - "teams composing background automations (morning report generators, transcript-to-post pipelines, overnight batch runners) where no human is present to catch an error at run time"
    - "anyone triaging a portfolio of candidate automations into 'safe to run unattended' vs. 'keep a human in the loop'"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — applying the gate is a design-time yes/no decision with no migration cost. Note the gate's entire criterion is the reversibility (and post-hoc verifiability) of the governed task's output: low-reversibility or hard-to-verify outputs are exactly what it keeps out of headless mode."
  auditability: "high — the go/no-go decision is checkable against a scheduled-job or headless-run config by asking two questions of the task's terminal output: is it easy to verify after the fact, and is it reversible if wrong? A task admitted to headless mode whose output fails either test is a visible violation."
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Practitioner-documented decision criterion from a survey of headless-mode (`claude -p` + cron/launchd) automation patterns; cited use cases (morning summary reports written to file, transcript-to-social-post pipelines saved to file) are exactly the post-hoc-verifiable, easily-reversible tasks the gate admits. Not yet formally adopted by the extracting system."
contract:
  preconditions: "A task is being considered for headless / unattended / scheduled execution — an agent run with no human watching each cycle (e.g. `claude -p` under cron/launchd, a background daemon, a routine engine). The task has an identifiable terminal output or side effect whose verifiability and reversibility can be assessed at design time."
  invariants: "A task is admitted to headless/unattended execution only if BOTH hold: (a) its output is easy to verify after the fact (a human or a deterministic check can confirm correctness post-hoc without re-running the whole task), and (b) its operations are reversible or low-cost-to-undo. Hard-to-undo operations MUST NOT run headless. Verifiability and reversibility are assessed for the task's actual output, not its common case."
  governance: "Owner: whoever configures the headless/scheduled job (skill author, orchestrator maintainer, the person writing the cron entry). The gate is a structural check on the job definition: does the admitted task's terminal output pass the verify-after-the-fact and reversible tests? This gate is the design-time go/no-go criterion for running unattended at all; it composes with — and does not replace — the runtime publish-boundary checkpoint of [[scheduled-workflows-require-human-checkpoint]]: a task may clear this gate to run headless and still require that rule's human checkpoint before any externally-visible publish step."
  recovery: "If a headless task is found to produce output that is hard to verify after the fact, or to perform hard-to-undo operations → remove it from headless mode: add a human-in-the-loop review step, narrow it to a reversible sub-output (e.g. write a draft to a private folder instead of publishing), or run it supervised. If a headless task's failures compound silently across scheduled runs (bad output produced every cycle until noticed), treat that as evidence the verify-after-the-fact test was not actually met and re-gate it."
tags:
  - "extracted-artifact"
  - "rule"
  - "headless-mode"
  - "unattended-automation"
  - "scheduled-workflows"
  - "autonomy-boundary"
  - "reliability"
---

# Headless Output Verifiability Gate

**Source:** [[headless-cron-composition-autonomous-scheduled-workflows]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A task is being considered for **headless / unattended / scheduled execution** — an agent run with no human present to catch an error while it runs. Concretely: a `claude -p` invocation wired into cron or launchd, a background daemon, a Ralph-loop chain, or any routine engine that fires the agent on a schedule and exits without an interactive session. The condition fires at the point the go/no-go decision is made — before the job is configured, and again whenever the task's scope changes.

## Action

**Required:** Admit a task to headless/unattended execution only when BOTH tests pass:

1. **Verify-after-the-fact.** The task's output is easy to verify after it runs — a human skim or a deterministic check can confirm correctness post-hoc, without re-running the whole task, because no one watched it happen.
2. **Reversible.** The task's operations are reversible or cheap to undo if the output turns out wrong.

**Forbidden:** Running a task headless when its terminal operation is hard to undo, or when confirming its output is correct would be as expensive as producing it. "Hard-to-undo operations should not run headless" is the load-bearing prohibition.

**Permitted:** Tasks whose output lands as an inspectable artifact and whose effects are reversible — morning summary reports written to a file, a transcript-to-social-post pipeline that saves drafts to disk, a private-KB reindex — are exactly the shape this gate admits.

## Boundary

Enforced at **design time**, when a task is selected for (or excluded from) headless/scheduled execution, and re-checked at any review of an existing job whose task scope has drifted. This is a *selection* criterion — whether a task belongs in unattended mode at all — not a runtime mechanism. It does not attach to the publish step of a running workflow (that boundary belongs to [[scheduled-workflows-require-human-checkpoint]]); it attaches to the prior question of whether the task should run without a human in the first place.

## Enforcement

- **Mechanism:** Structural review of the scheduled-job / headless-run definition. For each task admitted to headless mode, inspect its terminal output and side effects against the two tests.
- **Check (deterministic):** For each headless task `T`: `admitted_headless(T) → output_verifiable_post_hoc(T) AND output_reversible(T)`. Any task where the antecedent holds and either conjunct fails is a violation.
- **Violation response:** Remove the task from headless mode — insert a human-in-the-loop review, narrow the task to a reversible sub-output, or run it supervised — then re-admit only if both tests pass.
- **Constrain, don't just gate:** the `--allowed-tools` permission envelope (read-only for read-only tasks) is a complementary guardrail that lowers a borderline task's reversibility risk, but it does not substitute for the verifiability test — a read-constrained task with unverifiable output still fails the gate.

## Rationale

Headless mode is where an agent stops being "a tool you sit with" and becomes "a team member that works independently." That shift removes the one thing an interactive session provides for free: a human noticing an error the moment it happens. The source practitioner's decision criterion for crossing that line is **output verifiability** — only go headless for tasks whose output is easy to verify after the fact, because verification is now the only line of defense, and it happens after the operation has already run.

The two tests are asymmetric-cost logic. When no one is watching, an unverifiable-but-wrong output either goes undetected or costs as much to check as to redo — either way the automation's value is gone. And a hard-to-undo wrong output cannot be walked back once the scheduled run has fired. So the gate keeps both classes out of headless mode up front, rather than compensating for them with monitoring and retries after the fact.

**Composition with the publish-boundary checkpoint.** This gate and [[scheduled-workflows-require-human-checkpoint]] are complementary siblings in the "bounded autonomy for unattended agent work" family, and they compose cleanly rather than overlapping:

- **This rule** is the *design-time go/no-go criterion*: may this task run headless **at all**, judged by post-hoc verifiability and reversibility of its output? Its admitted cases are typically closed-loop, non-externally-visible outputs (a report written to a private file).
- **The checkpoint rule** is a *runtime mechanism*: any scheduled workflow with an externally-visible side effect (publish, send, broadcast) MUST have a blocking human-approval gate before that action — regardless of how verifiable the output is — and explicitly excludes the closed-loop workflows this gate admits.

A single automation can require both: it must clear this gate to be eligible for headless execution, and if its terminal step crosses an externally-visible boundary it must additionally carry the publish checkpoint. Neither rule subsumes the other; one selects the task for unattended running, the other gates a specific externally-visible action within it.

## Failure Modes

- **Verifiability overestimated.** A task is admitted as "easy to verify" but in practice its output is only cheaply checkable in the common case, while its rare failures are subtle and expensive to catch (an off-brand summary that reads plausibly). Mitigation: assess verifiability against the failure output, not the happy path; if a wrong result would read as correct on a skim, the test is not met.
- **Compounding silent errors.** Because no human reviews each run, a bad template or drifting prompt produces bad output every scheduled cycle until someone notices — the finding's own named failure mode. Mitigation: treat any compounding-error incident as retroactive evidence the verify-after-the-fact test failed, and re-gate.
- **Gate confused with the publish checkpoint.** Clearing this design-time gate is read as license to publish autonomously. Mitigation: they are independent — passing this gate makes a task *eligible to run headless*; it does not authorize any externally-visible publish, which still requires [[scheduled-workflows-require-human-checkpoint]].
- **Reversibility assumed from tooling.** `--allowed-tools` read-only constraints are treated as making any task safe for headless. Mitigation: permission-scoping reduces blast radius but does not make an unverifiable output verifiable; both tests must pass on their own terms.

## Contract

### Preconditions
A task is being considered for headless / unattended / scheduled execution — an agent run with no human watching each cycle (e.g. `claude -p` under cron/launchd, a background daemon, a routine engine). The task has an identifiable terminal output or side effect whose verifiability and reversibility can be assessed at design time.

### Invariants
A task is admitted to headless/unattended execution only if BOTH hold: (a) its output is easy to verify after the fact (a human or a deterministic check can confirm correctness post-hoc without re-running the whole task), and (b) its operations are reversible or low-cost-to-undo. Hard-to-undo operations MUST NOT run headless. Verifiability and reversibility are assessed for the task's actual output, not its common case.

### Governance
Owner: whoever configures the headless/scheduled job (skill author, orchestrator maintainer, the person writing the cron entry). The gate is a structural check on the job definition: does the admitted task's terminal output pass the verify-after-the-fact and reversible tests? This gate is the design-time go/no-go criterion for running unattended at all; it composes with — and does not replace — the runtime publish-boundary checkpoint of [[scheduled-workflows-require-human-checkpoint]]: a task may clear this gate to run headless and still require that rule's human checkpoint before any externally-visible publish step.

### Recovery
If a headless task is found to produce output that is hard to verify after the fact, or to perform hard-to-undo operations → remove it from headless mode: add a human-in-the-loop review step, narrow it to a reversible sub-output (e.g. write a draft to a private folder instead of publishing), or run it supervised. If a headless task's failures compound silently across scheduled runs (bad output produced every cycle until noticed), treat that as evidence the verify-after-the-fact test was not actually met and re-gate it.
