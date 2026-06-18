---
title: "End-to-End Sequential Bug-Fix Pipeline"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "end-to-end-sequential-bug-fix-pipeline"
extraction_date: "2026-05-25"
last_change_session: 94
last_change_sl: "session-94-codifier-extract-non-pattern-artifacts"
identification_report: "2026-05-24-identification-report-2.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "Development teams that want to reduce context-switching overhead across ticket reading, reproduction, coding, review, and deployment for routine bug fixes"
    - "Agentic coding environments where a single orchestrator should take a bug ticket from open to deployed without manual coordination at each stage"
    - "Teams with existing end-to-end test infrastructure and a connected issue tracker who want to encode their bug-fix process as an enforceable, auditable skill"
    - "Projects where skipping steps — deploying without verification, committing without review — is a known process risk that needs to be structurally prevented"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "operate"
  reversibility: "medium — changes are committed and deployed; rollback requires a revert commit and re-deploy; pre-commit stages are fully reversible"
  auditability: "High — every stage produces a concrete artifact (Playwright log, review summary, commit ref, deploy status); the full pipeline trace is reconstructible from these outputs"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "Valid, accessible ticket ID with reproduction steps and acceptance criteria. Playwright installed and configured. Issue tracker MCP connected. Git available in the repo."
  invariants: "Stages execute in strict order 1-9; no stage is skipped. Bug must be reproducible before implementation. Fix must pass Playwright verification before commit. Blocking review concerns must be resolved before verify."
  governance: "Owner: team operating the pipeline. Stage 8 (deploy) may require human gate per environment. Maximum 2 implement-verify retries before human escalation."
  recovery: "Non-reproducible bug: halt at Stage 2. Unresolved blocking review: return to Stage 4. Implement-verify cycle exceeds 2: halt and escalate. MCP failure: halt at the failing stage and surface to human."
tags:
  - "extracted-artifact"
  - "skill"
---

# End-to-End Sequential Bug-Fix Pipeline

**Source:** [[end-to-end-sequential-bug-fix-pipeline]]
**Form:** skill
**Extraction date:** 2026-05-25

A fully automated skill that chains all stages of a software bug-fix workflow in strict sequential order within a single orchestrator thread: ticket read → reproduce → research → implement → review → verify → commit → deploy → QA push. Sub-agents may be used within individual stages to contain context growth, but each stage must complete and return results to the orchestrator before the next stage begins.

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `ticket_id` | string | Yes | Issue tracker ticket ID (e.g., Jira issue key). The orchestrator fetches description and acceptance criteria from this. |
| `repo_root` | string | Yes | Local path to the repository root. |
| `playwright_config` | string | No | Path to Playwright config. Required if reproduction/verification steps use Playwright. |
| `deploy_target` | string | No | Deployment environment identifier (e.g., `staging`, `qa`). Required for Stage 8. |
| `review_roles` | array[string] | No | Specialist sub-agent roles to invoke at review (e.g., `frontend`, `backend`, `testing`). Defaults to `[backend, testing]`. |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| `fix_commit` | git ref | The commit SHA containing the implemented fix. |
| `verification_report` | markdown | Playwright output confirming the bug was resolved, with before/after comparison. |
| `review_summary` | markdown | Aggregated output from all specialist review sub-agents. |
| `deploy_status` | string | Deployment confirmation or failure reason. |

## Steps

### Stage 1: Read Ticket
- Fetch the bug description, reproduction steps, and acceptance criteria from the issue tracker via MCP (e.g., Jira MCP).
- Fail explicitly if the ticket is not found or lacks reproduction steps. Do not proceed to Stage 2 on ambiguous input.

### Stage 2: Reproduce
- Run the reproduction steps against the codebase using Playwright CLI.
- **Gate:** If the bug is not reproducible, halt the pipeline and return a non-reproducible finding to the ticket. Do not proceed to research or implement.
- **Output:** Playwright run log confirming the failure.

### Stage 3: Research
- Dispatch a sub-agent to gather context: relevant source files, prior related fixes (git log), and any referenced documentation.
- Sub-agent output is summarized and returned to the orchestrator thread before Stage 4 begins.

### Stage 4: Implement
- Write the fix using the research context.
- Scope strictly to the acceptance criteria from Stage 1. Do not fix tangential issues in the same change.

### Stage 5: Review
- Dispatch specialist review sub-agents per `review_roles`.
- Each sub-agent reviews the diff from Stage 4 against its domain criteria.
- **Gate:** If any reviewer raises a blocking concern, return to Stage 4 with the concern attached. Do not proceed to verify with unresolved blocking reviews.

### Stage 6: Verify
- Re-run the Playwright test from Stage 2.
- **Gate:** The test must pass. If it fails, return to Stage 4. Maximum 2 implement-verify cycles; escalate to human after second failure.

### Stage 7: Commit
- Commit the fix to version control with a message referencing the ticket ID.
- Do not amend prior commits.

### Stage 8: Deploy
- Deploy to `deploy_target`. If no target is specified, emit a deploy-skipped status and continue.

### Stage 9: QA Push
- Promote the change to QA session (may dispatch a sub-agent for QA handoff if the environment requires it).
- Record the QA session reference in the final output.

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Context accumulation exhausts context window | Orchestrator context grows too large to continue | Use sub-agents for research and review stages; summarize stage outputs before feeding to orchestrator |
| Bug not reproducible at Stage 2 | Playwright reports no failure | Halt and notify; do not proceed — fixing an unreproducible bug risks shipping unverified changes |
| Silent stage success (false positive) | Stage N reports success but state is incorrect | Each stage must produce a concrete artifact (log, diff, ref); reject empty or unverifiable success signals |
| Playwright environment drift | Playwright fails due to config mismatch, not a bug | Validate Playwright setup independently before invoking; flag as environment failure, not bug failure |
| Issue tracker MCP failure | Stage 1 cannot fetch the ticket | Fail at Stage 1; do not guess ticket contents; escalate to human |
| Implement-verify cycle exceeds 2 retries | Second Playwright run still fails | Halt; produce partial-progress report with all artifacts generated so far; escalate to human |

## Contract

### Preconditions
A valid, accessible ticket ID is provided with reproduction steps and acceptance criteria. Playwright is installed and configured in the repo. The issue tracker MCP is connected and reachable. Version control (git) is available in the repo.

### Invariants
Stages execute in strict order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9. No stage is skipped. The bug must be reproducible (Stage 2) before implementation begins. The fix must pass Playwright verification (Stage 6) before it is committed. Blocking review concerns from Stage 5 must be resolved before Stage 6.

### Governance
Owner: the team operating the pipeline. Stage 8 (deploy) may require a human gate depending on the environment; configure `deploy_target` accordingly. Maximum 2 implement-verify retries before human escalation.

### Recovery
Non-reproducible bug: halt at Stage 2, return non-reproducible status to ticket. Unresolved blocking review: return to Stage 4 with review feedback; do not skip review. Implement-verify cycle exceeds 2 retries: halt, produce partial-progress report, escalate. MCP failure: halt at the stage of failure, log the error, surface to human.
