---
title: "Deterministic Nodes for Non-Reasoning Workflow Steps"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "dark-factory-ai-only-codebase-management"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "autonomous-scheduled-agent-operation.harvest-queue"
identification_report: "autonomous-scheduled-agent-operation.harvest-queue.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "engineers designing multi-step automated agent workflows, harnesses, or orchestrator pipelines"
    - "unattended or scheduled pipelines where no human reviews each intermediate step before the next one fires"
    - "teams debugging an unreliable agent workflow and hunting for the source of stochastic failure"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "low — note: converting an LLM-driven step to deterministic code requires rewriting that step's logic; if the LLM step was silently doing more than the nominal task (e.g., also normalizing edge cases), the workflow's behavior may shift and needs re-validation after conversion"
  auditability: "high — each workflow node's implementation (LLM call vs. plain code) is visible in the harness/workflow definition and can be reviewed node-by-node against the question 'does this step require reasoning over ambiguous or novel input?'"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Surfaced as a lesson from a practitioner's retrospective after running a production fully-autonomous ('dark factory') pipeline for real work; not yet formally adopted by the extracting system."
contract:
  preconditions: "A multi-step automated or agentic workflow exists (harness, orchestrator DAG, scheduled pipeline) composed of discrete nodes, where at least one node currently routes through an LLM/agent call."
  invariants: "Every workflow node that does not require reasoning or judgment over ambiguous or novel input — formatting, linting, running a fixed test command, triggering a deploy, applying a label, computing a diff, moving a file — is implemented as deterministic code (script, CLI invocation, API call with fixed logic), never an LLM call. Nodes that genuinely require synthesis, classification of ambiguous input, or open-ended judgment retain an LLM/agent call."
  governance: "Owner: whoever designs or maintains the workflow's step graph (harness author, orchestrator maintainer). Each node in the graph should be reviewable against the single audit question — does this step need reasoning? — with the answer visible from the node's implementation, not just its intent."
  recovery: "If a step implemented as an LLM call is found to require no reasoning (its outputs are fully determined by its inputs), replace it with equivalent deterministic code. When debugging an unreliable multi-step workflow, prioritize converting reasoning-free steps to deterministic code before adding more monitoring or retries around them — removing the stochastic surface is cheaper than compensating for it."
tags:
  - "extracted-artifact"
  - "rule"
---

# Deterministic Nodes for Non-Reasoning Workflow Steps

**Source:** [[dark-factory-ai-only-codebase-management]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

Any multi-step automated or agentic workflow — a harness, an orchestrator DAG, a scheduled/unattended pipeline — where the step graph is being designed, reviewed, or debugged. Applies node-by-node: the condition fires per workflow node, not once per workflow.

## Action

**Required:** For each node in the workflow, ask "does this step require reasoning or judgment over ambiguous or novel input?" If the answer is no — the step is formatting, linting, running a fixed test suite, triggering a deploy, applying a label, computing a diff, moving or renaming a file, or any other operation whose output is fully determined by its input — implement it as plain deterministic code (a script, a CLI call, an API call with fixed logic), not an LLM/agent call.

**Permitted:** LLM/agent calls remain appropriate for nodes that genuinely require synthesis, classification of ambiguous input, open-ended judgment, or natural-language understanding — triage of an incoming issue's intent, code review commentary, drafting a summary.

**Forbidden:** Routing a reasoning-free step through an LLM call "for consistency" or because the workflow already has an agent in the loop for an adjacent step. Each node's implementation choice is made independently on its own reasoning requirement, not inherited from its neighbors.

## Boundary

Enforced at workflow/harness design time and at any subsequent review of the step graph. Applies to any pipeline where a node's implementation could plausibly be either an LLM call or deterministic code — it does not apply to nodes with only one possible implementation (e.g., a step whose entire job is drafting prose has no deterministic equivalent).

## Enforcement

- **Mechanism:** Review of the workflow/harness definition. For each declared node, inspect its implementation: is it a deterministic call (script/CLI/fixed-logic API) or an LLM/agent call?
- **Check:** For each node `N`: `requires_reasoning(N) == false → implementation(N) is deterministic`. Any node where the antecedent holds and the consequent fails is a violation.
- **Violation response:** Rewrite the node as deterministic code; re-run the workflow's existing test/validation suite to confirm equivalent behavior before merging the change.

## Rationale

Sourced from a practitioner's retrospective after running a production "dark factory" — a codebase where AI agent workflows are the sole authors of all code changes, unattended end-to-end. The retrospective's stated principle: "reliability by subtraction" — steps that don't need reasoning (formatting, lint, triggering deploys) should be plain code, not LLM calls.

The mechanism: every LLM call in a chain introduces a stochastic failure surface (nondeterministic output, occasional hallucination, prompt-sensitivity) that a deterministic call does not have. In an unattended pipeline — the retrospective's context is explicitly a workflow with "low visibility by design, because the whole point is that no one is watching" — each unnecessary LLM call is pure downside: it cannot make a reasoning-free step more correct, only occasionally less correct, and its failures are harder to reproduce and debug than a deterministic bug. Subtracting reasoning calls from steps that don't need them shrinks the workflow's total failure surface without giving up any capability the workflow actually needs.

## Special Case: The Trigger/Wake Node

The first node of any scheduled or event-driven loop — the check that decides whether to invoke the reasoning agent at all this cycle — is itself covered by this rule. A cron-interval ticker should run a cheap deterministic pre-check (compare a feed's last-modified/etag, query an API's "updates since" endpoint, diff a known state) and skip the run entirely — no agent invocation, no token spend — when the check finds no new work. Only a positive pre-check result should wake the expensive LLM-driven step. This is the "combo trigger" pattern: cron/schedule (trigger type 2) composed with a cheap deterministic gate before the actual agentic work fires. The trigger/wake check is a node under this rule's Condition ("per workflow node, not once per workflow"), and "is there new work?" is exactly the boolean, fully-input-determined check the Action already names as deterministic-eligible — the rule's general invariant applied to the specific node that starts the workflow.

**Source:** [[loop-trigger-taxonomy-poll-then-wake-combo]] (Strong / production-tested — a support-inbox triage loop polling Intercom every 30 minutes, arrived at via a self-proposed evolve-session optimization after running for a while, not the loop's original design).

## Failure Modes

- **Reasoning creep.** A step starts genuinely ambiguous (needs an LLM) but stabilizes into a fixed decision procedure over time (e.g., a triage step that in practice always follows the same few branches). Mitigation: periodically re-ask the audit question for long-running workflow nodes, not just at initial design.
- **False economy.** Converting a step that has a small amount of genuine judgment (edge-case handling, borderline classification) into rigid deterministic code, causing silent misclassification of edge cases that used to be caught by the LLM's judgment. Mitigation: the audit question is about the step's actual input distribution, not its common case — if ambiguous inputs are rare but real, the step still needs reasoning.
- **Local optimization losing sight of the workflow.** Converting individual nodes to deterministic code without re-validating the workflow end-to-end can miss interaction effects between nodes. Mitigation: the recovery guidance requires re-running the existing validation suite after each conversion, not just eyeballing the changed node.

## Contract

### Preconditions
A multi-step automated or agentic workflow exists (harness, orchestrator DAG, scheduled pipeline) composed of discrete nodes, where at least one node currently routes through an LLM/agent call.

### Invariants
Every workflow node that does not require reasoning or judgment over ambiguous or novel input — formatting, linting, running a fixed test command, triggering a deploy, applying a label, computing a diff, moving a file — is implemented as deterministic code (script, CLI invocation, API call with fixed logic), never an LLM call. Nodes that genuinely require synthesis, classification of ambiguous input, or open-ended judgment retain an LLM/agent call.

### Governance
Owner: whoever designs or maintains the workflow's step graph (harness author, orchestrator maintainer). Each node in the graph should be reviewable against the single audit question — does this step need reasoning? — with the answer visible from the node's implementation, not just its intent.

### Recovery
If a step implemented as an LLM call is found to require no reasoning (its outputs are fully determined by its inputs), replace it with equivalent deterministic code. When debugging an unreliable multi-step workflow, prioritize converting reasoning-free steps to deterministic code before adding more monitoring or retries around them — removing the stochastic surface is cheaper than compensating for it.
