---
title: "Correct Course: Structured Mid-Project Pivot Command"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "correct-course-mid-project-pivot-command"
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-4.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agentic software development workflows where story-based planning is in flight"
    - "Scrum Master or project manager agent personas handling mid-project scope changes"
    - "developers needing a structured pivot mechanism that preserves completed work"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "specify"
  reversibility: "low — revised backlog and updated artifact documents require developer review before taking effect; no code is changed by the skill itself"
  auditability: "high — every backlog change is tagged [PRESERVED], [MODIFIED], [NEW], or [REMOVED] and presented for explicit developer approval before any effect"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "Developer has wrapped the current in-progress story. All project artifacts are present and readable. Developer has provided a clear pivot description."
  invariants: "Completed stories marked [PRESERVED] are never modified. No backlog changes take effect without explicit developer approval. All artifact changes are declared atomically."
  governance: "Owner: BMad Scrum Master agent persona. Modifications require a DD. Human gate (Step 7 approval) is mandatory."
  recovery: "If preconditions not met: halt and return a checklist. If developer rejects recommendation: return to Step 3 with the objection as additional input."
tags:
  - "extracted-artifact"
  - "skill"
---

# Correct Course: Structured Mid-Project Pivot Command

**Source:** [[correct-course-mid-project-pivot-command]]
**Form:** skill
**Extraction date:** 2026-04-19

## Purpose

Handle mid-project pivots without discarding completed work or accumulating unstructured tech debt. Invoked when a developer needs to integrate a missed requirement, a new API/library, or a significant scope change after stories are already in flight.

## Inputs

- Current project artifact set: architecture doc, PRD, tech stack doc, story backlog
- List of completed stories (with acceptance criteria marked done)
- List of in-progress stories (partial completion state)
- Developer's pivot description: what changed, why, what the desired end state is

## Outputs

- Pivot assessment: revert / incremental adjustment / full restart recommendation with rationale
- Revised story backlog: modified, added, and removed stories identified explicitly
- Updated artifact list: which artifacts were modified and how
- Preserved completed work inventory

## Steps

1. **Wrap current story.** Developer completes or formally suspends the in-progress story before invoking.
2. **Read project state.** Agent reads completed story list, in-progress state, architecture doc, PRD, and tech stack doc in full.
3. **Classify pivot magnitude.** Determine whether the pivot affects: (a) a single epic, (b) cross-epic dependencies, or (c) foundational architecture.
4. **Select correction strategy.**
   - *Incremental:* Modify or add stories within the existing backlog. Use when pivot affects ≤1 epic.
   - *Staged revert:* Roll back to a prior stage milestone, regenerate stories forward. Use when completed stories conflict with the pivot.
   - *Full restart:* Archive all stories, regenerate from PRD. Use only when the pivot invalidates the architecture or core tech stack.
5. **Update artifacts.** If strategy requires it: revise architecture doc, PRD, or tech stack doc. Mark prior versions superseded.
6. **Produce revised backlog.** Output new story list with explicit tags: `[PRESERVED]`, `[MODIFIED]`, `[NEW]`, `[REMOVED]`.
7. **Present to developer for approval.** No backlog changes take effect until the developer confirms.

## Failure Modes

- **Overly conservative recommendation:** Agent defaults to full restart when incremental adjustment would suffice. Require agent to justify full restart with explicit list of completed stories that conflict.
- **Incomplete state read:** Agent misses tribal knowledge not encoded in artifacts. Developer reviews preserved work inventory before approving.
- **Artifact drift:** Architecture doc updated but PRD not, or vice versa. Step 5 requires agent to declare all artifact changes atomically.

## Contract

### Preconditions
Developer has wrapped the current in-progress story. All project artifacts are present and readable. Developer has provided a clear pivot description.

### Invariants
Completed stories marked [PRESERVED] are never modified. No backlog changes take effect without explicit developer approval. All artifact changes are declared atomically.

### Governance
Owner: BMad Scrum Master agent persona. Modifications require a DD. Human gate (Step 7 approval) is mandatory.

### Recovery
If preconditions not met: halt and return a checklist. If developer rejects recommendation: return to Step 3 with the objection as additional input.
