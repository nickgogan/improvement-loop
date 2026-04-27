---
title: "PROGRESS.md Session Bridge Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "progress-md-session-bridge"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
version: 1
identification_report: "managing-agent-context.harvest-queue.md::progress-md-session-bridge::template::progressmd-session-bridge-template"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent session continuity across multiple discrete sessions where the agent has no native cross-session memory"
    - "multi-session project tracking where decision rationale and in-flight work must survive session boundaries"
    - "handoff documentation systems coordinating work between sequential agent runs or between agent and human reviewer"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — the bridge file is a single markdown document; adoption, removal, or replacement carries no downstream migration cost"
  auditability: "high — the file is human-readable and version-controlled; any observer can read the most recent entry to see what was claimed completed, in-progress, blocked, or next; drift against actual filesystem state is independently verifiable"
  evidence_strength: "Strong"
  adoption:
    status: "Partially Adopted"
    notes: "Pattern recurs across 12 of 14 practitioner videos reviewed and is used by Anthropic's long-running scientific-computing workflow (CHANGELOG.md variant). The MetaSystem vault uses PROGRESS.md at workspace and per-system roots."
contract:
  preconditions: "A persistent, version-controlled, human-readable location exists for the bridge file. The agent has read access at session start and write access at session end. The session has clearly definable start and end boundaries. If the agent will run as a Cloud Scheduled Task, the bridge file lives in a cloud-accessible location (git repo, Notion page) rather than only on a local machine."
  invariants: "The bridge file is read at session start before substantive work begins. The bridge file is written at session end before context is discarded. Each entry timestamps its session. Status sections (Completed, In Progress, Blocked, Next) are present and non-empty for any session that produced output. Updates are delta — new entries are appended; prior session entries are not rewritten by an LLM (per ace-delta-updates-over-monolithic-rewrites rule). The file's claims are verifiable against actual filesystem or system state."
  governance: "Owner: the project operator (human or designated agent). Schema changes (adding/removing top-level sections) require operator approval. Section content within an established schema may be written by the agent at session end without per-session approval. The file must not be compacted or rewritten in full by an LLM (catastrophic-context-collapse risk applies to long-lived context documents)."
  recovery: "If the file is missing at session start: the agent reports the gap and either creates a fresh skeleton from this template or requests operator guidance before proceeding. If the file's claims diverge from filesystem reality: the agent flags the drift in a Drift Notes block at the top of the next session entry rather than silently overwriting. If the agent is interrupted before writing the closing entry: the next session's first action is a reconstruction entry summarizing observable state and noting the gap. If the file grows beyond a comfortable read budget: archive prior sessions to a sibling file (e.g., PROGRESS-archive-YYYY-QN.md) rather than LLM-summarizing in place."
tags:
  - "extracted-artifact"
  - "template"
  - "context-engineering"
  - "session-continuity"
---

# PROGRESS.md Session Bridge Template

**Source:** [[progress-md-session-bridge]]
**Form:** template
**Extraction date:** 2026-04-27

## Frontmatter Schema

| Field | Type | Description |
|-------|------|-------------|
| `title` | string | Human-readable title — typically `"{{PROJECT_NAME}} — Progress"` |
| `last_session` | ISO date | Date of the most recent session entry; used for staleness detection |
| `last_session_id` | string | Unique identifier for the last session (e.g., `session-83`) — pairs with the System Log entry if one exists |
| `active_milestone` | string \| null | Current milestone or focus area, if the project uses milestones; null otherwise |
| `cloud_task_aware` | boolean | True if this file is read by Cloud Scheduled Tasks; gates the Cloud Task Context section |
| `archive_pointer` | string \| null | Relative path to the most recent archive file once sessions have been archived out |

## Body Sections

| Section | Purpose | Content shape |
|---------|---------|---------------|
| `# {{PROJECT_NAME}} — Progress` | Title heading | One line; matches frontmatter title |
| `## Current Focus` | One-paragraph orientation for the agent reading at session start | Plain prose; what the project is doing right now and why |
| `## Session {{SESSION_ID}} — {{SESSION_DATE}}` | Per-session entry, appended each session end | Five subsections (below); newest at the top of session list |
| `### Completed` | What this session finished | Bulleted list with file links or commit refs where applicable |
| `### In Progress` | Work started but not finished, with enough state to resume | Bulleted list; each item names the artifact and the next concrete action |
| `### Blocked` | Items awaiting external input, decision, or unblocking | Bulleted list; each item names the blocker and who/what unblocks it |
| `### Next` | Ordered list of next concrete actions | Numbered list; first item is the immediate next action |
| `### Decisions` (optional) | Decisions made during the session that aren't already in DDs or commit messages | Bulleted; one line per decision with rationale |
| `### Assumptions` (optional) | Assumptions in play that future sessions should verify or revisit | Bulleted; flagged for verification |
| `### Risks` (optional) | Known risks or fragility surfaces introduced or discovered | Bulleted; pair each risk with a mitigation if known |
| `### Drift Notes` (optional) | Discrepancies between prior claims and observable state, surfaced before writing this session's claims | Bulleted; only appears when drift was detected |
| `## Cloud Task Context` (optional) | Context block read by Cloud Scheduled Tasks running while the local machine is off | Plain prose; only present when `cloud_task_aware: true` |
| `## Archive` (optional) | Pointer to archived prior sessions once the file is split | Single link to `archive_pointer` |

## Variables / Placeholders

| Placeholder | Type | Description |
|-------------|------|-------------|
| `{{PROJECT_NAME}}` | string | Human-readable project or system name used in the title |
| `{{SESSION_ID}}` | string | Identifier for this session (e.g., `session-83`); align with System Log id if SL is in use |
| `{{SESSION_DATE}}` | ISO date | Date the session ran |
| `{{COMPLETED_ITEMS}}` | bulleted list | What got finished this session |
| `{{IN_PROGRESS_ITEMS}}` | bulleted list | Work started but not finished, each with a resume hint |
| `{{BLOCKED_ITEMS}}` | bulleted list | Items waiting on external input |
| `{{NEXT_ITEMS}}` | numbered list | Ordered next actions; first item is the immediate next step |
| `{{DECISIONS}}` | bulleted list \| empty | Decisions made this session, when any |
| `{{ASSUMPTIONS}}` | bulleted list \| empty | Assumptions in play, when any |
| `{{RISKS}}` | bulleted list \| empty | Risks, when any |
| `{{DRIFT_NOTES}}` | bulleted list \| empty | Drift between prior claims and observed state, when any |
| `{{CLOUD_TASK_CONTEXT}}` | prose \| empty | Block read by cloud-scheduled runs, when applicable |

## Body Skeleton

```markdown
---
title: "{{PROJECT_NAME}} — Progress"
last_session: "{{SESSION_DATE}}"
last_session_id: "{{SESSION_ID}}"
active_milestone: null
cloud_task_aware: false
archive_pointer: null
---

# {{PROJECT_NAME}} — Progress

## Current Focus

<one-paragraph orientation: what the project is doing now, why>

## Session {{SESSION_ID}} — {{SESSION_DATE}}

### Drift Notes
{{DRIFT_NOTES}}

### Completed
{{COMPLETED_ITEMS}}

### In Progress
{{IN_PROGRESS_ITEMS}}

### Blocked
{{BLOCKED_ITEMS}}

### Next
{{NEXT_ITEMS}}

### Decisions
{{DECISIONS}}

### Assumptions
{{ASSUMPTIONS}}

### Risks
{{RISKS}}

<!-- Older session entries appended below in reverse chronological order -->

## Cloud Task Context

{{CLOUD_TASK_CONTEXT}}

## Archive

<!-- Populate when archive_pointer is set -->
```

## Usage Notes

**When to use:**
- Any project where the agent runs across multiple discrete sessions and lacks native cross-session memory.
- Workflows where decision rationale and in-flight state must survive a session boundary, not just the code state.
- Projects coordinated by sequential agent runs or alternating agent and human reviewers.

**When to update:**
- Read at session start, before any substantive work begins.
- Write a new session block at session end, before context is discarded. Append; do not rewrite prior sessions.
- If the agent detects drift between prior claims and observable state, add a Drift Notes block at the top of the new session entry rather than silently editing past sessions.
- When the file becomes uncomfortably long, archive prior sessions to `PROGRESS-archive-YYYY-QN.md` and set `archive_pointer`. Do not LLM-compact in place.

**Integration with the agent loop:**
- Pair with the System Log if the system has one — the SL entry id and PROGRESS session id should match for a session that produced governance-relevant changes.
- For Cloud Scheduled Tasks, set `cloud_task_aware: true` and host the file in a cloud-accessible location (git repo or shared note system) so off-machine runs can read it.
- The closely-related CHANGELOG.md "lab notes" pattern (Anthropic scientific-computing workflow) is a sibling variant — same scaffold, different naming for engineering/research contexts. Pick one per project; do not run both unless the dual-file CLAUDE.md (plan) + CHANGELOG.md (history) split is intentional.

**Do not use when:**
- The work is a single-session task with no continuation expected — the bridge has no consumer.
- The project already has a stronger handoff substrate (e.g., a structured task store the agent reads natively) and PROGRESS.md would duplicate it.

## Contract

### Preconditions
A persistent, version-controlled, human-readable location exists for the bridge file. The agent has read access at session start and write access at session end. The session has clearly definable start and end boundaries. If the agent will run as a Cloud Scheduled Task, the bridge file lives in a cloud-accessible location (git repo, Notion page) rather than only on a local machine.

### Invariants
The bridge file is read at session start before substantive work begins. The bridge file is written at session end before context is discarded. Each entry timestamps its session. Status sections (Completed, In Progress, Blocked, Next) are present and non-empty for any session that produced output. Updates are delta — new entries are appended; prior session entries are not rewritten by an LLM (per ace-delta-updates-over-monolithic-rewrites rule). The file's claims are verifiable against actual filesystem or system state.

### Governance
Owner: the project operator (human or designated agent). Schema changes (adding/removing top-level sections) require operator approval. Section content within an established schema may be written by the agent at session end without per-session approval. The file must not be compacted or rewritten in full by an LLM (catastrophic-context-collapse risk applies to long-lived context documents).

### Recovery
If the file is missing at session start: the agent reports the gap and either creates a fresh skeleton from this template or requests operator guidance before proceeding. If the file's claims diverge from filesystem reality: the agent flags the drift in a Drift Notes block at the top of the next session entry rather than silently overwriting. If the agent is interrupted before writing the closing entry: the next session's first action is a reconstruction entry summarizing observable state and noting the gap. If the file grows beyond a comfortable read budget: archive prior sessions to a sibling file (e.g., PROGRESS-archive-YYYY-QN.md) rather than LLM-summarizing in place.
