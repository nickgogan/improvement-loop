---
title: "Memory-File-to-Skill Migration Pass"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "memory-file-to-skill-migration"
identification_report: "defending-agent-context.harvest-queue.md::memory-file-to-skill-migration::skill::memory-file-to-skill-migration-pass"
extraction_date: "2026-07-13"
last_change_session: 146
last_change_report: "defending-agent-context.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent operators whose always-loaded memory file (a project or global instruction file loaded into every session) has accumulated sections only some session types need"
    - "teams running a correct-and-remember discipline where the project memory file bloats by design and needs periodic relief"
    - "anyone paying a standing per-session token tax for conditionally-useful content that could load on demand instead"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "low — reversal is a copy-back of the skill's content into the memory file with no data loss, but any invocation wiring must also be unwound and the token tax returns"
  auditability: "high — the migration is a reviewable diff (the memory file shrinks; one or more skills are created); the per-section conditionality test is a binary check any reviewer can re-run; session-startup context size is an observable proxy for whether the tax actually dropped"
  evidence_strength: "Medium"
  adoption:
    status: "Partially Adopted"
    notes: "A practitioner runs this across all projects with a harness-agnostic setup (one memory file symlinked to serve several harnesses); a first-party skill-authoring helper exists to make the extraction step delegable on harnesses that do not natively author skills."
contract:
  preconditions: "An always-loaded memory file (a project or global instruction file, or equivalent) exists and has grown to include sections only some session types need. The harness supports skills — a pull-loaded capability with progressive disclosure — or a skill-authoring helper is available for harnesses that do not. The agent can rewrite the memory file and create a skill in one step."
  invariants: "Only conditionally-useful sections migrate; content needed by (nearly) every session stays in the memory file. Each migrated section becomes a skill whose progressive disclosure loads only a one-line description until the skill is actually invoked. The migration is a reviewed change — the diff is inspected before acceptance. Migration provenance is recorded (the skill notes which memory-file learnings it absorbed) so future corrections keep flowing to the right home."
  governance: "Owner: whoever maintains the memory file and the skill set. The conditionality test is applied per section before any migration. The agent may perform the migration, but the resulting diff is human-reviewed like any other change. Over-migration — hiding content the agent needs every session behind a skill it fails to invoke — is the primary failure to guard against."
  recovery: "Under-invoked migrated skill (the agent needed it but did not load it) → the migration over-reached; fold that content back into the memory file. Skill sprawl with overlapping descriptions degrading selection → consolidate or sharpen the descriptions. Migration dropped nuance from a learning → recover the original from version control and re-migrate with the nuance preserved."
tags:
  - "extracted-artifact"
  - "skill"
  - "context-engineering"
  - "memory-files"
  - "progressive-disclosure"
  - "token-economy"
---

# Memory-File-to-Skill Migration Pass

**Source:** [[memory-file-to-skill-migration]]
**Form:** skill
**Extraction date:** 2026-07-13

A periodic maintenance pass that relieves memory-file bloat by moving *conditionally-useful* sections out of the always-loaded memory file and into skills, whose progressive disclosure loads only a description line until the skill is invoked. It reframes push-loaded memory and pull-loaded skills not as an architectural either/or but as two lifecycle stages of the same content: knowledge enters cheaply through the memory file and graduates to a skill once its conditionality is clear.

## Inputs

- An always-loaded memory file (a project or global instruction file loaded into every session) that has accumulated content.
- The conditionality test as the sorting key: **"is this section needed by (nearly) every session, or only conditionally?"** Conditional content is anything needed only for some session types — e.g., end-to-end testing instructions needed only when the agent changes code, or deployment steps needed only when shipping.
- A harness that supports skills (progressive disclosure), or a skill-authoring helper for harnesses that lack the concept.

## Outputs

- A slimmed memory file: conditional sections removed, always-needed content retained.
- One or more new skills, each carrying a one-line description (loaded at startup) plus the full extracted content (loaded only on invocation).
- A migration-provenance note in each skill recording which memory-file learnings it absorbed.

## Steps

1. **Trigger the pass.** Run it periodically, or when the memory file crosses a size threshold / the always-loaded token cost becomes felt. A concrete trigger ("memory file exceeds N lines → run a migration pass") beats waiting for felt pain.
2. **Enumerate sections** of the memory file.
3. **Apply the conditionality test to each section.** Needed every session → keep in place. Needed only by some session types → mark for migration.
4. **Delegate each migration to the agent, one section at a time.** Instruct it to (a) extract the section into a project-level skill — a description line plus the full content body — (b) remove the section from the memory file, and (c) record in the skill which memory-file learnings it absorbed. The agent rewrites the memory file and creates the skill in a single step.
5. **Leave always-needed content untouched.** Do not migrate content the agent relies on every session — that is the inverse-tax trap.
6. **Review the diff.** Inspect the change like any other: verify the memory file shrank, the new skill(s) carry a crisp description, and no always-needed content was hidden. Confirm session-startup context dropped.

## Failure Modes

- **Over-migration.** Content the agent actually needs every session gets hidden behind a skill description it fails to invoke; the resulting missed-context tax is worse than the token tax it removed. Guard with the conditionality test and post-migration review.
- **Skill sprawl.** Many micro-skills with overlapping descriptions degrade the harness's skill selection. Consolidate related migrations and keep descriptions distinct.
- **Nuance drop.** The agent-performed migration can drop nuance from the original learning; the migration diff needs review like any other change, and provenance notes help the original intent survive.

## Contract

### Preconditions
An always-loaded memory file exists and has grown to include sections only some session types need. The harness supports skills (progressive disclosure), or a skill-authoring helper is available. The agent can rewrite the memory file and create a skill in one step.

### Invariants
Only conditionally-useful sections migrate; content needed by (nearly) every session stays in the memory file. Each migrated section becomes a skill whose progressive disclosure loads only a one-line description until invoked. The migration is a reviewed change. Migration provenance is recorded so corrections keep flowing to the right home.

### Governance
Owner: whoever maintains the memory file and skill set. The conditionality test is applied per section before migrating. The agent may perform the migration, but the diff is human-reviewed. Over-migration is the primary failure to guard against.

### Recovery
Under-invoked migrated skill → fold that content back into the memory file. Skill sprawl with overlapping descriptions → consolidate or sharpen descriptions. Migration dropped nuance → recover the original from version control and re-migrate with the nuance preserved.
