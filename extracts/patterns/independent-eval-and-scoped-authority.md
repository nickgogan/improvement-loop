---
title: "Independent Evaluation and Scoped Authority"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "independent-eval-and-scoped-authority-commandments"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "An AI agent is being deployed to perform tasks with real-world consequences (data modification, code changes, communications). The blast radius of agent failure has been assessed. Independent evaluation mechanisms (linters, tests, schema validators, human review) are available or can be built."
  invariants: "Agent self-reports are never the sole basis for evaluating agent output quality. Every agent operates under an explicit authority boundary that lists what it cannot do. Permission expansions are logged and reversible."
  governance: "Nick owns authority boundaries and evaluation gate definitions. No agent may expand its own permissions. Evaluation mechanisms are maintained independently of the agents they evaluate — the agent under test must not be able to modify its own evaluator."
  recovery: "If independent evaluation detects agent output failure, halt the agent and escalate to human review. If an authority boundary is breached (agent performs an action outside its scope), revert the action if possible, tighten the boundary, and conduct a post-incident review."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Independent Evaluation and Scoped Authority

**Source:** [[independent-eval-and-scoped-authority-commandments]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Deployed AI agents fail in two characteristic ways: (1) they appear to work because their only quality signal is their own self-report, and (2) they cause damage because their authority was never explicitly bounded. Both failure modes are silent — the operator discovers the problem only after significant damage has accumulated. The $14K voice agent case study exemplifies this: the agent functioned correctly for months while producing unusable data, because no independent evaluation existed.

## Forces

- **Trust vs. verification.** Agents that self-report success are convenient but unreliable. Building independent evaluation adds cost and complexity.
- **Autonomy vs. safety.** Agents need enough authority to be useful. Restricting authority too aggressively makes the agent useless. The balance point depends on the blast radius of failure.
- **Upfront investment vs. downstream cost.** Building observability and evaluation from day one feels expensive relative to just letting the agent run. But the cost of discovering a silent failure months later is far higher.
- **Negative space vs. positive space.** Defining what an agent *cannot* do (negative space) is harder to think about than defining what it *can* do (positive space), but it's the more important constraint.

## Solution

Apply two complementary deployment principles as a mandatory pair:

**Principle 1 — Independent Evaluation from Day One:**
Never rely on agent self-reports to assess quality. Instrument every agent deployment with logging, metrics, and automated quality checks that run independently of the agent. "Stop letting agents tell you whether they are doing a good job."

Key mechanics:
- Automated quality gates (linters, test suites, schema validators) that run on agent output.
- Output sampling with human review on a regular cadence.
- Metrics that track outcome quality, not just task completion (e.g., "data was usable downstream" not just "agent ran without errors").
- Evaluation infrastructure is maintained separately from the agent — the agent under test cannot modify its own evaluator.

**Principle 2 — Scoped Authority with Explicit Guardrails:**
Define the negative space first — what the agent explicitly cannot do. Start with minimal permissions and expand deliberately. Every permission expansion is a conscious decision, not a default.

Key mechanics:
- An explicit authority boundary document listing prohibited actions (e.g., "must not modify production data," "must not commit to main").
- Permission tiers that map to blast radius: low-risk actions are autonomous, medium-risk require logging, high-risk require human approval.
- Permission expansion requires a recorded decision (a Design Decision or equivalent), not a casual config change.
- Rollback capability for every permission-gated action.

## Consequences

**Positive:**
- Silent failures are caught early by independent evaluation, before they accumulate into costly problems.
- Explicit authority boundaries prevent the catastrophic failure modes (production database wipeout, unauthorized commits, data corruption).
- The pattern scales: adding a new agent requires defining its eval gates and authority boundary, which forces the operator to think about failure modes upfront.
- Maps directly to existing MetaSystem infrastructure: hooks provide independent evaluation, CLAUDE.md constraints provide authority scoping.

**Negative:**
- Over-constraining authority makes agents slow and frustrating to use — every action requires approval.
- Over-instrumenting evaluation adds latency, cost, and maintenance burden.
- Finding the right balance point requires iterating — the initial authority boundary is almost never right on the first try.
- Independent evaluation infrastructure must itself be maintained and tested, adding a recursive maintenance cost.

## Known Uses

- **Nate B Jones's Five Commandments** (Commandments 4 and 5): Derived from the $14K voice agent failure case study and the "Production Database Wipeout" incident.
- **MetaSystem human gates (DD-29):** Every stage boundary requires human approval — a direct implementation of scoped authority.
- **Claude Code permission system:** Tiered permissions (allow/deny/ask) that map to action risk levels.
- **MetaSystem CLAUDE.md constraints:** Explicit lists of prohibited actions ("Never run destructive commands without approval," "Never commit to main without review").

## Contract

### Preconditions

- An AI agent is being deployed to perform tasks with real-world consequences (data modification, code changes, external communications).
- The blast radius of agent failure has been assessed (what is the worst thing this agent could do?).
- Independent evaluation mechanisms (linters, tests, schema validators, human review) are available or can be built before deployment.

### Invariants

- Agent self-reports are never the sole basis for evaluating agent output quality.
- Every deployed agent operates under an explicit authority boundary that lists what it cannot do.
- Permission expansions are logged, justified by a recorded decision, and reversible.
- Evaluation infrastructure is maintained independently of the agents it evaluates.

### Governance

- Nick owns authority boundaries and evaluation gate definitions.
- No agent may expand its own permissions — permission changes require human approval.
- Evaluation mechanisms are owned and maintained separately from the agents they evaluate.
- Authority boundary changes are tracked as Design Decisions or equivalent governance records.

### Recovery

- If independent evaluation detects agent output failure, halt the agent and escalate to human review before resuming.
- If an authority boundary is breached (agent performs an action outside its scope), revert the action if possible, tighten the boundary, and conduct a post-incident review.
- If evaluation infrastructure itself fails (evaluator crashes, test suite breaks), pause agent operation until evaluation is restored — do not operate without independent evaluation.
