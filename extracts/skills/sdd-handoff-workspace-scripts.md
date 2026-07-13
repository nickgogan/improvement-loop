---
title: "SDD Handoff Workspace Scripts — File-Mediated Subagent Dispatch"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "file-mediated-subagent-handoff-workspace"
identification_report: "defending-agent-context.harvest-queue.md::file-mediated-subagent-handoff-workspace::skill::sdd-handoff-workspace-scripts"
extraction_date: "2026-07-13"
last_change_session: 146
last_change_report: "defending-agent-context.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "orchestrator/subagent workflows where dispatch prompts currently paste task text, reports, or diffs inline"
    - "multi-agent coding pipelines that need the orchestrator's context to hold routing state, not artifact bodies"
    - "plan-driven development flows where each subagent should see only its own task brief, never the whole plan"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — reverting to pasted-content dispatches requires no migration; the runtime workspace directory can simply be deleted"
  auditability: "high — every handoff artifact (task brief, implementer report, review package) is a plain-text file on disk; dispatch prompts can be mechanically checked for paths-not-bodies compliance and return messages for the line cap"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Partially Adopted"
    notes: "Two widely used open-source agent frameworks converged independently on file-mediated handoffs; one documented the reversal of its own paste-full-text doctrine with eval evidence (~2x faster, ~50% fewer tokens for the overall flow)."
contract:
  preconditions: "An orchestrating agent can run deterministic scripts (shell or equivalent) and spawn subagents that read and write files. A plan or task source exists from which per-task briefs can be extracted. A writable runtime workspace location outside the version-control metadata directory (harnesses often write-protect it) is available. The version-control history is intact (it is the recovery source if the workspace is destroyed)."
  invariants: "Dispatch prompts carry file paths plus a thin prose frame — never pasted task bodies, reports, or diffs. Each subagent reads only its own task brief; no subagent ever reads the whole plan. Subagent return messages stay under a small line cap (~15 lines) with all detail in the report file. Deterministic scripts, not orchestrator prose, assemble the handoff files. The workspace is self-ignoring (carries its own ignore file) and lives outside the version-control metadata directory."
  governance: "Owner: the orchestration layer that authors dispatch prompts and maintains the workspace scripts. The brief/report/review file-name and section contracts are versioned together with the scripts; a change to either side requires updating both. Separately installed components that share the file contracts must pin or verify the contract version they expect."
  recovery: "If a subagent executes without reading its brief file: make the read mandatory and verifiable in the dispatch (require the subagent to restate the brief's task header or acceptance checklist before acting). If the workspace is destroyed (e.g., an aggressive clean command): regenerate briefs from the plan and recover completed-work history from version-control log. If file contracts drift between separately versioned components: lint each dispatch to verify every referenced file exists and parses before spawning the subagent."
tags:
  - "extracted-artifact"
  - "skill"
  - "context-engineering"
  - "subagent-handoffs"
  - "orchestration"
---

# SDD Handoff Workspace Scripts — File-Mediated Subagent Dispatch

**Source:** [[file-mediated-subagent-handoff-workspace]]
**Form:** skill
**Extraction date:** 2026-07-13

The core inversion: everything pasted into a dispatch prompt stays resident in the orchestrator's context for the rest of the session. So scripts write the files, and dispatches carry paths. The observed anti-pattern this replaces: a 42k-character dispatch that was 99% pasted history.

## Inputs

- **Plan file:** The multi-task plan governing the work. Only the brief-extraction script reads it whole; no subagent ever does.
- **Task number(s):** Which task to extract into a brief for the next dispatch.
- **Base/head refs:** For review packaging — the commit range a reviewer subagent must assess.
- **Workspace root:** A runtime scratch location for handoff artifacts (e.g., a dot-directory in the working tree), deliberately outside the version-control metadata directory, self-ignoring via its own ignore file.
- **Report contract:** The file path and section structure each subagent must write its full output to.

## Outputs

- **A populated handoff workspace:** per-task brief files, implementer report files, review packages, and a progress ledger — all plain text, all inspectable.
- **Thin return messages:** each subagent's return is a compact summary (under ~15 lines) plus the path to its report file. The orchestrator's context accumulates routing state, not artifact bodies.

## Steps

1. **Create the workspace by script.** A setup script creates the workspace directory at runtime, writes its self-ignore file, and scopes it per-worktree. It lives outside the version-control metadata directory, which harnesses commonly write-protect.
2. **Extract a per-task brief.** A `task-brief PLAN N`-style script extracts exactly task N from the plan into `task-N-brief.md`. Deterministic extraction — not orchestrator prose — so the brief is reliable and cheap to produce, and the subagent's view is scoped by construction.
3. **Compose the dispatch prompt from paths.** One line of scene-setting; the brief path with an explicit instruction ("read this first — it is your requirements"); any interfaces produced by earlier tasks; the report-file path and its section contract. No pasted bodies.
4. **Run the implementer subagent.** It reads its brief, does the work, writes its full report to the report file, and returns a summary capped under ~15 lines plus the report path.
5. **Package the review by script.** A `review-package BASE HEAD`-style script emits the commit list, the diff stat, and a wide-context diff (e.g., `-U10`) into a single file readable in one call.
6. **Run the reviewer subagent.** It reads the review package, writes full findings to its own report file, and returns only a verdict, the top findings, and the path. The parent never holds full review text.
7. **Advance the ledger.** Record task completion and report locations in the workspace's progress ledger, then loop to step 2 for the next task.

## Failure Modes

- **Path-trust failure:** a subagent that skips reading its brief executes on vibes. The dispatch must make the read mandatory and verifiable (e.g., require the subagent to restate the acceptance criteria before acting).
- **Workspace destruction:** an aggressive clean command erases the scratch substrate. Version-control log is the recovery source; briefs regenerate from the plan.
- **Convention drift across components:** file-name and section contracts between separately installed modules version independently and can skew. Lint dispatches for referenced-file existence; version the contract with the scripts.
- **Ledger staleness:** the workspace survives compaction but also survives relevance — add retention/cleanup so stale briefs and reports don't masquerade as current state.

## Contract

### Preconditions
An orchestrating agent can run deterministic scripts (shell or equivalent) and spawn subagents that read and write files. A plan or task source exists from which per-task briefs can be extracted. A writable runtime workspace location outside the version-control metadata directory (harnesses often write-protect it) is available. The version-control history is intact (it is the recovery source if the workspace is destroyed).

### Invariants
Dispatch prompts carry file paths plus a thin prose frame — never pasted task bodies, reports, or diffs. Each subagent reads only its own task brief; no subagent ever reads the whole plan. Subagent return messages stay under a small line cap (~15 lines) with all detail in the report file. Deterministic scripts, not orchestrator prose, assemble the handoff files. The workspace is self-ignoring (carries its own ignore file) and lives outside the version-control metadata directory.

### Governance
Owner: the orchestration layer that authors dispatch prompts and maintains the workspace scripts. The brief/report/review file-name and section contracts are versioned together with the scripts; a change to either side requires updating both. Separately installed components that share the file contracts must pin or verify the contract version they expect.

### Recovery
If a subagent executes without reading its brief file: make the read mandatory and verifiable in the dispatch (require the subagent to restate the brief's task header or acceptance checklist before acting). If the workspace is destroyed (e.g., an aggressive clean command): regenerate briefs from the plan and recover completed-work history from version-control log. If file contracts drift between separately versioned components: lint each dispatch to verify every referenced file exists and parses before spawning the subagent.
