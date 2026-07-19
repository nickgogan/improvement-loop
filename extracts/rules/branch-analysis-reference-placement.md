---
title: "Branch-Analysis Reference Placement — Every-Branch Inline, Partial-Branch Externalized"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "branch-analysis-externalization-rule-skill-reference"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "structuring-agent-context.harvest-queue"
identification_report: "structuring-agent-context.harvest-queue.md::branch-analysis-externalization-rule-skill-reference::rule::branch-analysis-reference-placement"
deployed: false
deployed_to: null
context:
  applies_to:
    - "skill or command authors deciding whether a piece of reference material belongs inline in the main file or in a separate reference file"
    - "skill-audit or skill-design tooling checking procedure-plus-reference artifacts for progressive-disclosure structure"
    - "any procedure-plus-reference artifact (skill, playbook, runbook) that supports more than one distinct usage path"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — moving a reference block inline or externalizing it is a file-structure edit with no data loss; either direction is reversible by moving the content back"
  auditability: "high — branch enumeration and reference-block-to-branch tagging is a checklist any auditor can apply mechanically to a given artifact, without further judgment calls once the branches are enumerated"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Documented practice from a widely used, open-source skill-authoring guide, applied throughout its own large skill library. No formal adoption elsewhere recorded at extraction time."
contract:
  preconditions: "A procedure-plus-reference artifact (a skill, playbook, or similar SKILL.md-style file) exists or is being authored, and it has — or can be decomposed into — one or more reference blocks (templates, explainers, standards) supporting its procedure."
  invariants: "Every reference block is tagged with the set of branches (distinct, mutually exclusive usage paths) that need it. A reference block needed on every branch stays inline in the main file. A reference block needed on only some branches is moved to a separate, bundled reference file and replaced inline by a one-line context pointer naming when to read it. No reference block used on every branch is externalized, and no reference block used on only some branches is left inline."
  governance: "Owner: whoever authors or audits the skill/procedure artifact. Branch enumeration and reference-to-branch tagging happen at authoring time and are re-checked whenever branches are added, removed, or merged. Skill-audit tooling applies the same two-directional check — every-branch-externalized is a defect, partial-branch-inline is a defect."
  recovery: "If an every-branch reference block is found externalized: inline it — the pointer adds a read round-trip that fires on every use with no offsetting benefit. If a partial-branch reference block is found inline: externalize it behind a context pointer scoped to the branches that need it. If branches were miscounted (an input variation mistaken for a branch, or a genuinely exclusive mode missed): re-run the branch enumeration and re-tag affected reference blocks — over-externalizing and under-externalizing are both symptoms of the same miscount and get the same fix. If a model is found not following an external-reference pointer for material that turns out to be needed on every branch: treat this as a signal the material was mis-tagged as partial-branch, and move it inline rather than trying to force pointer-following."
tags:
  - "extracted-artifact"
  - "rule"
  - "skill-authoring"
  - "context-engineering"
  - "progressive-disclosure"
---

# Branch-Analysis Reference Placement — Every-Branch Inline, Partial-Branch Externalized

**Source:** [[branch-analysis-externalization-rule-skill-reference]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A procedure-plus-reference artifact (a skill, playbook, or similar) is being authored, restructured, or audited, and it contains — or can be decomposed into — a procedure plus one or more reference blocks (templates, explainers, standards).

## Action

**Required:** Enumerate the artifact's branches — the distinct, mutually exclusive ways it can be used or the different things it can do. Classify each reference block: used on every branch → keep inline in the main file; used on only some branches → move it to a separate, bundled reference file, replaced inline with a one-line context pointer ("if you need X, read `<file>`").

**Forbidden:** Externalizing a reference block that is used on every branch — this adds a guaranteed read round-trip on every single use with no offsetting benefit. Leaving a reference block that is used on only some branches inline — this pays the same always-loaded cost on branches that never need it and inflates the artifact's baseline size.

## Boundary

Enforced at two points: (1) authoring time, whenever a reference block is added or a new branch is introduced; (2) audit time, re-checking existing reference-block placement against the artifact's current branch structure, since branches can be added or merged after the original placement decision was made.

## Enforcement

- **Mechanism:** Per-reference-block classification against the artifact's enumerated branch set.
- **Check (deterministic):** `branches_using(block) == all_branches(artifact)` → block must be inline. `branches_using(block) ⊂ all_branches(artifact)` (a proper subset) → block must be externalized behind a pointer.
- **Violation response:** Misplaced blocks are moved to the correct location (inline ↔ externalized) and, if the misplacement traces to a miscounted branch set, the branch enumeration itself is redone before re-tagging.

## Rationale

General progressive-disclosure guidance says to keep the main file small and push reference material out — but that alone doesn't say *which* material to move. Branch analysis supplies the missing operative test: reference material used unconditionally, on every path through the artifact, gains nothing from externalization (the pointer is followed every time anyway, so it's a pure added round-trip); reference material used only on some paths gains from externalization, because the always-loaded cost of an unused block on the other paths disappears. This converts a fuzzy "keep it small" heuristic into a per-block, binary decision that an auditor can apply mechanically once the branches are enumerated — no separate judgment call needed for each reference block.

## Failure Modes

- **Branch miscounting.** Treating an input variation (not a genuinely distinct usage path) as a branch leads to over-externalizing; missing a genuinely exclusive mode leads to under-externalizing. Both trace back to the same root cause and are fixed by redoing the branch enumeration.
- **Pointer non-follow.** An externalized reference is reached via a context pointer, and models sometimes decline to follow such pointers. Critical every-branch material behind a pointer is therefore a reliability bug, not just an efficiency loss — which is exactly why the rule requires every-branch material to stay inline rather than relying on pointer-following for anything universally needed.
- **Drift across files.** Externalized reference material can version separately from the procedure steps that use it. Single-source-of-truth discipline has to span the whole artifact's folder, not just its main file, or the externalized copy silently goes stale relative to the procedure that depends on it.

## Contract

### Preconditions
A procedure-plus-reference artifact (a skill, playbook, or similar SKILL.md-style file) exists or is being authored, and it has — or can be decomposed into — one or more reference blocks (templates, explainers, standards) supporting its procedure.

### Invariants
Every reference block is tagged with the set of branches (distinct, mutually exclusive usage paths) that need it. A reference block needed on every branch stays inline in the main file. A reference block needed on only some branches is moved to a separate, bundled reference file and replaced inline by a one-line context pointer naming when to read it. No reference block used on every branch is externalized, and no reference block used on only some branches is left inline.

### Governance
Owner: whoever authors or audits the skill/procedure artifact. Branch enumeration and reference-to-branch tagging happen at authoring time and are re-checked whenever branches are added, removed, or merged. Skill-audit tooling applies the same two-directional check — every-branch-externalized is a defect, partial-branch-inline is a defect.

### Recovery
If an every-branch reference block is found externalized: inline it — the pointer adds a read round-trip that fires on every use with no offsetting benefit. If a partial-branch reference block is found inline: externalize it behind a context pointer scoped to the branches that need it. If branches were miscounted (an input variation mistaken for a branch, or a genuinely exclusive mode missed): re-run the branch enumeration and re-tag affected reference blocks — over-externalizing and under-externalizing are both symptoms of the same miscount and get the same fix. If a model is found not following an external-reference pointer for material that turns out to be needed on every branch: treat this as a signal the material was mis-tagged as partial-branch, and move it inline rather than trying to force pointer-following.
