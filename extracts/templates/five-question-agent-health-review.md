---
title: "Five-Question Agent Health Review"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "five-point-agent-health-checklist"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "verifying-agent-output.harvest-queue"
identification_report: "verifying-agent-output.harvest-queue.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "operators or teams periodically reviewing a deployed agent that has been in production for a while"
    - "post-model-upgrade or post-workflow-change health checks on an existing agent's permissions, job scope, and output value"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "operate"
  reversibility: "trivial — a review instrument; running it changes nothing on its own, though its recommended actions (retool, retire) carry their own reversibility"
  auditability: "high when each answer cites a linkable trail (tickets, quoted source text, permission diffs) rather than the reviewer's own assertion"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "An agent has been deployed long enough, or its environment or underlying model has changed enough, that a periodic fitness check is warranted. The reviewer has access to the agent's source list, permission set, stated job, and a sample of recent output plus its readers."
  invariants: "All five questions are answered, not a subset. Each answer is backed by a linkable trail (ticket references, quoted source text, permission diffs, usage data) rather than the agent's or the reviewer's own self-report. A 'job drift' finding (question 3) is either reverted or explicitly re-authorized — never left as an unacknowledged silent change. Retirement (question 5) is treated as a first-class, non-failure outcome."
  governance: "Owner: whoever is accountable for the agent's continued operation (the deploying team or individual). The completed review is filed alongside the agent's other operational documentation. A 'retool' or 'retire' verdict routes to whatever change-approval process governs that agent's deployment."
  recovery: "If an answer cannot be backed by evidence (self-report only), treat that question as unanswered and gather the evidence before concluding the review. If the review surfaces silent job drift, pause the agent's expanded scope until the job change is either reverted or explicitly re-authorized. If value is uncertain (question 5), default to a shortened re-review interval rather than an indefinite pass."
tags:
  - "extracted-artifact"
  - "template"
  - "agent-health"
  - "operate"
  - "evaluation"
---

# Five-Question Agent Health Review

**Source:** [[five-point-agent-health-checklist]]
**Form:** template
**Extraction date:** 2026-07-19

## Variables

| Variable | Description |
|----------|-------------|
| `{{AGENT_NAME}}` | Name or identifier of the agent under review |
| `{{REVIEW_DATE}}` | Date this review is conducted |
| `{{REVIEWER}}` | Person conducting the review |
| `{{LAST_REVIEW_DATE}}` | Date of the previous health review, or "first review" |
| `{{MODEL_VERSION}}` | Model currently powering the agent |
| `{{STATED_JOB}}` | The agent's job as documented at its last review or at deployment |
| `{{SOURCE_LIST}}` | The inputs the agent depends on (data sources, workflows, upstream systems) |
| `{{PERMISSION_LIST}}` | What the agent can currently touch (read, draft, create, post, update, spend, publish) |
| `{{OUTPUT_CONSUMERS}}` | Who reads or acts on the agent's output |

---

## Body

# Agent Health Review: {{AGENT_NAME}}

**Review date:** {{REVIEW_DATE}} · **Reviewer:** {{REVIEWER}} · **Last reviewed:** {{LAST_REVIEW_DATE}} · **Model:** {{MODEL_VERSION}}

### 1. Inputs — What's it eating?

- Are the sources in `{{SOURCE_LIST}}` still current?
- Did an upstream workflow move since the last review?
- Did an old source become misleading, or a new one become important enough to add?

**Finding:** _______________
**Evidence (links, diffs, dates):** _______________

### 2. Reach — Test its permissions.

- Current permissions: `{{PERMISSION_LIST}}`.
- Does each permission still fit `{{MODEL_VERSION}}`'s current strength — not too broad for a weaker model, not too narrow for an improved one?

**Finding:** _______________
**Evidence (permission diff, incident log, or "no change"):** _______________

### 3. Job — Check for silent drift.

- Stated job: `{{STATED_JOB}}`.
- Is the agent still doing that job, or has it quietly expanded (e.g., a summary agent now effectively planning)?
- If drift is found: was it authorized on purpose, or did it happen silently?

**Finding:** _______________
**Evidence (sample outputs showing scope):** _______________
**Action if drifted:** revert to stated job ▢ / explicitly re-authorize new job ▢

### 4. Proof — Check the evidence trail.

- For the agent's recent consequential claims, is there a linkable trail (tickets, quoted source language, a record of which sources were checked and which were inaccessible) — not the agent's own assertion?

**Finding:** _______________
**Evidence (links):** _______________

### 5. Value — Check whether anyone benefits.

- Does `{{OUTPUT_CONSUMERS}}` actually read the output?
- Does it save time after review, or create another unread pile?
- Has `{{MODEL_VERSION}}` improved enough that the agent should be rebuilt, or has the business need changed enough that it should be retired?

**Finding:** _______________
**Verdict:** keep as-is ▢ / rebuild ▢ / retire ▢

---

**Overall verdict:** _______________
**Next review date:** _______________

---

## Usage

Run this review periodically for any agent that has been in production long enough to have accumulated drift risk, and on-demand after a triggering event. Fill every section — a review that skips a question is incomplete, not a shorter pass.

**Cadence guidance (per-question triggers, not a single fixed interval):**

| Question | Trigger |
|---|---|
| 1. Inputs | Time-based cadence (e.g., quarterly) |
| 2. Reach | Every model upgrade for this agent |
| 3. Job | Time-based cadence |
| 4. Proof | Every gated or consequential output, not just at review time |
| 5. Value | Every model upgrade, and time-based cadence |

## Variation Axis

The instrument is domain-agnostic, but two things vary by deployment:

- **Permission vocabulary (question 2).** The read/draft/create/post/update/spend/publish list should be replaced with whatever permission taxonomy the agent's platform actually uses.
- **Evidence shape (question 4).** What counts as a "linkable trail" differs by domain — ticket references for support agents, cited passages for research agents, diff links for coding agents. Define the evidence shape once per agent class so reviewers aren't inventing it each time.
