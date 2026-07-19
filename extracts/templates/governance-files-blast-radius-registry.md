---
title: "Governance-Files Blast-Radius Registry"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "governance-registry-blast-radius-classification"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-governance-and-trust.harvest-queue"
identification_report: "agent-governance-and-trust.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "workspaces with autonomous or semi-autonomous agents that edit files, where some files should only change under deliberate human review"
    - "teams that have stated an edit-autonomy rule in prose (\"don't touch governance files without approval\") but have no enumerated list an agent can actually check"
    - "audits that need a completeness target for 'is every behavior-shaping file accounted for'"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — a registry file; adding, editing, or reclassifying an entry has no migration cost beyond the registry itself"
  auditability: "high — the registry is a human-readable, single-file lookup; a completeness script can verify every behavior-shaping file in the tree has a classification entry"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Documented from a single production system's wiring canon; approximated implicitly (not as a single lookup file) in at least one adopting workspace via immutable-decision records and generated-file conventions."
contract:
  preconditions: "The workspace has a stated (even if only prose) rule distinguishing files that require human-in-the-loop edits from files agents may edit autonomously. The set of behavior-shaping files is enumerable — new ones are created rarely enough that a registry can keep pace."
  invariants: "Every behavior-shaping file in the workspace has exactly one classification entry: governance (human-in-the-loop only) or working/notes (autonomous edits fine), with reasoning attached. The registry itself is classified as governance — its own tiering rules cannot be loosened by an autonomous edit. An agent consults the registry before an autonomous edit rather than inferring risk from the file's name or content."
  governance: "Owner: the workspace's human steward. Additions or reclassifications go through the same human-in-the-loop gate the registry itself enforces on governance files — this is the self-referential guard. A completeness audit (script or periodic check) verifies every root/behavior-shaping doc is classified; unclassified files fail the audit rather than defaulting to either tier."
  recovery: "If an agent finds a behavior-shaping file with no registry entry, treat it as governance-tier (fail closed) until classified — do not default to autonomous-edit-allowed. If the registry itself falls out of sync with the tree (new files added, none registered), the completeness audit catches it; the registry is dead weight if nothing consults or enforces it, so the pre-edit lookup must be wired into an actual guard or hook, not left as documentation only."
tags:
  - "extracted-artifact"
  - "template"
  - "governance"
  - "autonomy-tiers"
  - "audit"
---

# Governance-Files Blast-Radius Registry

**Source:** [[governance-registry-blast-radius-classification]]
**Form:** template
**Extraction date:** 2026-07-19

## Variables

| Variable | Type | Description |
|---|---|---|
| `{{FILE_PATH_OR_PATTERN}}` | string | The behavior-shaping file or path pattern being classified. |
| `{{TIER}}` | enum: `governance` \| `working` | Two tiers only — resist adding more until recurrence demands it. |
| `{{REASONING}}` | string | Why this file sits in this tier — what breaks if an agent edits it autonomously, or why autonomous edits are safe. |
| `{{REGISTRY_OWNER}}` | string | The human steward accountable for the registry's own governance-tier reclassifications. |

## Body

```markdown
## Governance Registry — {{WORKSPACE_NAME}}

Classifies every behavior-shaping file into exactly two tiers. This registry is itself
classified as **governance** — its own rows cannot be loosened without human review.

| File / Pattern | Tier | Reasoning |
|---|---|---|
| {{FILE_PATH_OR_PATTERN_1}} | governance | {{REASONING_1}} |
| {{FILE_PATH_OR_PATTERN_2}} | governance | {{REASONING_2}} |
| {{FILE_PATH_OR_PATTERN_3}} | working | {{REASONING_3}} |
<!-- one row per behavior-shaping file or path pattern; every root doc must appear -->

**Owner:** {{REGISTRY_OWNER}}
**Completeness check:** {{AUDIT_MECHANISM}} — new behavior-shaping files that skip registration fail this check.
```

## Usage

Seed the governance tier with, at minimum: the always-on entry context file, path-scoped rules, skill/agent definitions, planning and vision documents, durable decision ledgers, and the registry itself. Seed the working tier with session control surfaces, draft artifacts, and session-scoped memory — anything an agent should be free to update as a byproduct of its normal work.

Wire the registry into an actual pre-edit check — an always-on guard instruction, a PreToolUse-style hook, or equivalent — so an agent looks up a target file's tier before editing rather than guessing from the filename. A registry that nothing consults is documentation, not enforcement.

Run (or write) a completeness audit that walks the workspace tree and flags any behavior-shaping file with no registry entry. Without this audit the registry silently falls behind as new files are added — the audit is load-bearing, not optional.

## Variation Axis

- **Two-tier (default):** governance / working, binary. Preferred starting point — resist a third tier ("autonomous but reviewed") until recurrence, not hypothetical edge cases, demands it.
- **Path-pattern entries:** for workspaces with many similarly-shaped files (e.g., all files under a `drafts/` directory), a single pattern row replaces N individual entries — trades granularity for lower maintenance.
- **Placeholder discipline for portable registries:** if the registry travels across environments or users, express user- or environment-scoped paths as placeholders (e.g., `{{user-id}}`) rather than hardcoded values, so the registry itself stays exportable.
- **Wiring-canon integration:** in systems with a broader "required capabilities" contract, this registry is a required row — the human-approval channel it depends on has no fallback, so its absence should block the contract rather than degrade silently.

## Contract

### Preconditions
The workspace has a stated (even if only prose) rule distinguishing files that require human-in-the-loop edits from files agents may edit autonomously. The set of behavior-shaping files is enumerable — new ones are created rarely enough that a registry can keep pace.

### Invariants
Every behavior-shaping file in the workspace has exactly one classification entry: governance (human-in-the-loop only) or working/notes (autonomous edits fine), with reasoning attached. The registry itself is classified as governance — its own tiering rules cannot be loosened by an autonomous edit. An agent consults the registry before an autonomous edit rather than inferring risk from the file's name or content.

### Governance
Owner: the workspace's human steward. Additions or reclassifications go through the same human-in-the-loop gate the registry itself enforces on governance files — this is the self-referential guard. A completeness audit (script or periodic check) verifies every root/behavior-shaping doc is classified; unclassified files fail the audit rather than defaulting to either tier.

### Recovery
If an agent finds a behavior-shaping file with no registry entry, treat it as governance-tier (fail closed) until classified — do not default to autonomous-edit-allowed. If the registry itself falls out of sync with the tree (new files added, none registered), the completeness audit catches it; the registry is dead weight if nothing consults or enforces it, so the pre-edit lookup must be wired into an actual guard or hook, not left as documentation only.
