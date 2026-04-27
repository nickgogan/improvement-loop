---
title: /re Fork-and-Trim Trajectory Procedure
type: extracted-artifact
assigned_form: skill
source_finding: trajectory-engineering-non-linear-session-forking
identification_report: "managing-agent-context.harvest-queue.md::trajectory-engineering-non-linear-session-forking::skill::re-fork-and-trim-trajectory-procedure"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
deployed: false
deployed_to: null
context:
  applies_to:
  - Claude Code sessions where the agent has accumulated dead-weight context (failed debug attempts, abandoned approaches, exploratory tangents) that is degrading response quality
  - architectural decision points where multiple solution approaches need to be explored from a common starting state without polluting one trajectory with another's context
  - long-running coding sessions where the practitioner wants to keep the trunk lean by trimming each branch back to stable reusable context after evaluation
  platform_coupling: claude-code
  autonomy: human-driven
  stage: execute
  reversibility: rewinds via /re or Esc+Esc are non-destructive within the active session — the prior trajectory remains accessible until the session ends; rewinds do not survive across sessions
  auditability: low — session-internal navigation produces no persistent log; if audit trail is required, the operator must externally summarize what was trimmed and why
  evidence_strength: Strong
  adoption:
    status: Not Yet Started
    notes: Anthropic's April 2026 "Session Management and 1M Context" guidance promotes /rewind from advanced practitioner technique to first-class default; shortcut Esc+Esc.
contract:
  preconditions: An active Claude Code session with at least one prior turn the operator can identify as a clean fork point ("trunk state"). The operator can articulate which parts of the current context are trunk (stable, reusable — repo info, current plan, accepted decisions) versus branch (ephemeral exploration — failed attempts, abandoned options, debug spelunking). The operator has a one-to-three-sentence summary of any learnings from the branch they want to preserve across the rewind.
  invariants: Rewinds happen only within a single Claude Code session — the procedure cannot restore context from a previous session. The operator names the chosen mode (trim-after-fix, fork-to-compare, or trim-back-to-trunk) before invoking /re, so the trim decision is explicit rather than reactive. After every rewind, the operator re-injects a brief learnings summary if any branch produced reusable insight; otherwise the rewind is a clean discard.
  governance: 'Owner: the human operator running the Claude Code session. The operator owns the trunk-vs-branch judgment — neither Claude nor the harness can determine what is load-bearing. The procedure must not be automated end-to-end while session boundaries remain the rewind ceiling. If the operator cannot confidently classify content as trunk or branch, the procedure halts and the operator either (a) defers the rewind, or (b) explicitly accepts the risk of trimming load-bearing context.'
  recovery: If a rewind discards context the operator later realizes was load-bearing, the prior trajectory is still reachable within the session — re-rewind forward or paste the missing summary into the new trajectory. If the session ends before the trimmed context can be recovered, the loss is permanent for that session; restart with a handoff document. If oscillation is detected (operator rewinding repeatedly without converging), halt the procedure and switch to a fresh session with a written handoff summary instead.
tags:
- extracted-artifact
- skill
- claude-code
- context-management
- trajectory-engineering
---

# /re Fork-and-Trim Trajectory Procedure

**Source:** [[trajectory-engineering-non-linear-session-forking]]
**Form:** skill
**Extraction date:** 2026-04-27

This skill turns a Claude Code session from a linear chat into a directed tree. The operator names a mode, picks a rewind target, trims dead-weight context, and re-injects only the learnings worth keeping. The result is a lean session whose trunk carries stable reusable context and whose branches are pruned after evaluation.

## Inputs

- **Active Claude Code session.** The procedure operates only within the current session. It cannot reach across session boundaries.
- **Identified trunk state.** A prior turn in the session that the operator can mark as the clean fork point. Typically: "the turn after I confirmed the plan, before I started the failed debug detour."
- **Mode selection (one of three).**
  - `trim-after-fix` — a bug was found and fixed; rewind to before the bug-spotting context, re-inject a one-sentence summary of the fix, continue.
  - `fork-to-compare` — multiple architectural options need exploration from a common starting point; run each option down its own branch, evaluate, keep the winner, trim the rest.
  - `trim-back-to-trunk` — an exploratory branch is complete; rewind to the trunk, re-inject any insight worth keeping, discard the rest.
- **Learnings summary (one to three sentences).** The compact form of any insight from the branch that should survive the rewind. May be empty if the branch produced nothing worth keeping.

## Procedure

1. **Name the mode.** Before touching /re, state which of the three modes applies. The mode determines what counts as trunk and what counts as branch for this rewind.

2. **Identify the rewind target.** Scroll back and locate the specific turn that represents the desired trunk state. For trim-after-fix, this is the turn just before bug-hunting context began. For fork-to-compare, this is the turn just before the first option was explored. For trim-back-to-trunk, this is the last turn that contained only stable reusable context (repo info, accepted plan, confirmed decisions).

3. **Compose the learnings summary.** Before rewinding, write down (mentally or in a scratch buffer) the one to three sentences that capture what was learned in the branch. Examples: "The bug was in the auth middleware ordering — fixed by moving session validation before CSRF check." Or: "Option A (Postgres triggers) was rejected because it ties business logic to the DB layer; Option B (application-level events) was selected." If the branch produced nothing reusable, mark the summary as empty.

4. **Invoke the rewind.** Press Esc+Esc (or use /re) and select the target turn from step 2. Confirm the rewind. The session is now positioned at the trunk state.

5. **Re-inject the learnings summary.** If the summary from step 3 is non-empty, paste it as the next message — typically prefixed with "Context recovered from a trimmed branch:" or equivalent — so the agent has the compact form of the learning without the dead weight. If the summary is empty, skip this step.

6. **Continue work from the lean state.** The session now contains trunk context plus a one-to-three-sentence learnings summary. Resume normal work. Subsequent branches follow the same procedure.

7. **For fork-to-compare specifically:** repeat steps 1–6 for each option being explored. After all options have been evaluated, rewind one final time to the common trunk and re-inject the comparative result ("Option B was selected because X") rather than the full per-option exploration.

## Outputs

- **Lean session at the trunk state plus learnings summary.** The agent's working context is reduced to stable reusable content plus the compact form of any insight worth keeping.
- **Mental model of trunk vs branch for the session.** The operator now has an explicit category for each piece of context — trunk to keep, branch to trim — that informs future rewind decisions.
- **Optional — external summary record.** For sessions where audit trail matters, the operator records the rewind events and the learnings summaries to an external file (PROGRESS.md, session log, or similar).

## Boundary

- **Single-session ceiling.** Rewinds operate only within the active Claude Code session. Context lost when the session ends cannot be recovered by /re — only by handoff documents.
- **Operator-owned classification.** Neither Claude nor the harness can determine what is trunk versus branch. The trim decision belongs to the operator; the procedure does not automate it.
- **Not a substitute for fresh sessions.** When the operator cannot confidently classify content, or when the session has accumulated structural confusion (not just dead weight), starting a new session with a handoff document is preferable to repeated rewinding.

## Failure Modes

- **Trimmed load-bearing context.** The operator misclassifies trunk content as branch and rewinds past it. Symptom: the agent later asks about something that was previously established. Mitigation: re-rewind forward to recover the trajectory, or paste the missing context into the new trajectory.

- **Oscillation between branches.** The operator rewinds repeatedly without converging — fork to A, rewind, fork to B, rewind, fork back to A. Token cost accumulates without progress. Mitigation: halt the procedure; switch to a fresh session with a written handoff that names the decision criteria explicitly.

- **Learnings summary too verbose.** The operator pastes a multi-paragraph recap of the trimmed branch, defeating the trim. Mitigation: hold to one-to-three-sentence ceiling; if more nuance is needed, the branch was not actually finished and should not have been trimmed.

- **Cross-session rewind expectation.** The operator expects /re to recover context from a previous session. It cannot — rewinds are session-internal only. Mitigation: use a handoff document for cross-session continuity; reserve /re for within-session trajectory engineering.

- **Unmarked trunk pollution.** Without explicit trunk-vs-branch classification, the trunk gradually accumulates content that should have been trimmed. The session becomes linear by default again. Mitigation: name the mode at every rewind (step 1); refuse to rewind without an explicit mode.

- **Compaction-as-substitute.** The operator uses /compact instead of /re-and-trim. Compaction is lossy and gives no operator control over what is kept. Mitigation: prefer /re for context trimming; reserve /compact for end-of-session checkpoints where loss is acceptable.

## Contract

### Preconditions
An active Claude Code session with at least one prior turn the operator can identify as a clean fork point ("trunk state"). The operator can articulate which parts of the current context are trunk (stable, reusable — repo info, current plan, accepted decisions) versus branch (ephemeral exploration — failed attempts, abandoned options, debug spelunking). The operator has a one-to-three-sentence summary of any learnings from the branch they want to preserve across the rewind.

### Invariants
Rewinds happen only within a single Claude Code session — the procedure cannot restore context from a previous session. The operator names the chosen mode (trim-after-fix, fork-to-compare, or trim-back-to-trunk) before invoking /re, so the trim decision is explicit rather than reactive. After every rewind, the operator re-injects a brief learnings summary if any branch produced reusable insight; otherwise the rewind is a clean discard.

### Governance
Owner: the human operator running the Claude Code session. The operator owns the trunk-vs-branch judgment — neither Claude nor the harness can determine what is load-bearing. The procedure must not be automated end-to-end while session boundaries remain the rewind ceiling. If the operator cannot confidently classify content as trunk or branch, the procedure halts and the operator either (a) defers the rewind, or (b) explicitly accepts the risk of trimming load-bearing context.

### Recovery
If a rewind discards context the operator later realizes was load-bearing, the prior trajectory is still reachable within the session — re-rewind forward or paste the missing summary into the new trajectory. If the session ends before the trimmed context can be recovered, the loss is permanent for that session; restart with a handoff document. If oscillation is detected (operator rewinding repeatedly without converging), halt the procedure and switch to a fresh session with a written handoff summary instead.
