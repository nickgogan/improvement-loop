---
name: vision-to-plan
description: >-
  Turn a human's rough vision into approved planning artifacts — product brief →
  PRD → architecture doc → epics mapped into progress-doc milestones — through
  Socratic elicitation and section-by-section human approval. Use when asked to
  create a PRD, capture a project's vision or intent, write an architecture
  document, plan a project or subsystem, or turn an idea into an executable
  roadmap — trigger phrases: "create a PRD", "capture my vision", "plan this
  project", "write the architecture doc", "turn this idea into a roadmap".
  Distills the BMAD planning arc (brief → PRD → architecture → epics) and
  chunked-design-approval execution discipline; hands finished epics to the
  host's progress-reconciliation process. Not for end-of-session reconciliation
  or domain artifact production.
license: MIT
metadata:
  port-stage: "generic — stage-1 harness- and workspace-neutral canon (meta-skill-author §4.0)"
  source-skill: "ops-vision-to-plan v0.3.0"
  re-derive-when: "the source SKILL.md changes; the source is canonical, this file is derived"
  version: "1.0"
---

# Generic port — Vision to Plan

> Stage-1 Port deliverable (`meta-skill-author` §4.0). Harness- and workspace-neutral
> canon of `ops-vision-to-plan`. **Separability bar:** zero user-, workspace-, or
> platform-specific content. Stage-2 appliers map the **capability contract** below onto
> one platform via that platform's adapter profile; every contract row maps to a platform
> feature or is dropped-with-reason in the stage-2 manifest.

## Goal

Extract a human's product intent and encode it as durable planning artifacts that a
context-free agent can execute against. The artifact chain is **brief → PRD →
architecture → epics-as-milestones**; every artifact is approved by the human **section
by section** before the next begins. This skill produces vision-layer documents;
execution tracking stays in the project's progress/history documents, owned by the
host's progress-reconciliation process (e.g. the `session-handoff` generic) — this skill
proposes milestones in that vocabulary and never duplicates those conventions.

At completion the project's doc root contains:

1. **PRD** — vision, users, goals/non-goals, epics with binary acceptance criteria,
   risks, open questions.
2. **Architecture doc** — system boundaries, components, control surfaces, and an
   **agent operating contract** (what an agent must load, may decide alone, and must
   escalate).
3. **Milestone proposals** for the progress document — each epic mapped to a milestone
   with a testable definition-of-done and initial scopes, in the host PM vocabulary.

Success test (**cold-start test**): a fresh agent session, loading only the project's
standard entry points plus these artifacts, can state the system's purpose and the next
unit of work with zero guidance from the human.

## Invocation inputs (host-provided parameters)

| Input | What the host supplies |
|---|---|
| **Project identity** | Which project/subsystem is being planned |
| **Doc root** | Where the planning artifacts live (or should be created) |
| **Grounding sources** | The project's existing state documents: progress/history docs, any settled-facts ledger or standing guardrails, prior planning artifacts to amend |
| **PM vocabulary** | The host's milestone/scope/status conventions (defaults to the `session-handoff` generic's Vision → Milestone → Scope + hill model) |

## Capability contract (what any host must supply)

Derived from the skill's `capability-contract.yaml` (canonical, machine-readable —
meta-skill-author §4.0); the approval channel is **required**-tier (inert without it).
The progress-reconciliation row is a process-level dependency outside the
host-capability vocabulary — it names a downstream owner, not a platform feature.

| Capability | Contract | Degradation if absent |
|---|---|---|
| **Durable editable documents** | Persistent documents the agent can create and rewrite at the doc root | Agent outputs full artifact text per section for the human to save; never claims to have saved anything it didn't |
| **Section templates** | The three elicitation templates (brief, PRD, architecture) with per-section embedded instructions, available at invocation | Agent reconstructs each section's outline from the artifact definitions above and states that template fidelity is reduced |
| **Approval channel** | A way to present one section at a time and receive explicit approval/rejection before proceeding | None permitted — the section gate is the method; without an interactive channel this skill must not run |
| **Versioned checkpoints** | Change history with revert, so superseded artifact versions are recoverable | Amendments must quote the superseded text inline in a change note before rewriting it |
| **Progress-reconciliation process** | A downstream owner for milestone tracking (progress/history documents and their conventions) | Milestone proposals are delivered as a standalone section inside the PRD, marked as unowned |

## Workflow

1. **Elicit.** Interview the human as a product analyst. Cover five layers: operating
   rhythms, recurring decisions, required inputs, recurring frictions, success criteria —
   plus vision-specific probes (who is this for, what does "done and working" look like,
   what must never happen). Summarize what was heard; confirm before drafting.
2. **Brief.** One-page product brief from its template → human gate. The brief is a
   working file; it may live next to the PRD or be folded into it once approved.
3. **PRD.** Draft from its template, one section at a time with approval between
   sections. Every epic gets ≥1 binary acceptance criterion.
4. **Architecture.** Draft from its template, same chunked approval. The agent operating
   contract section is mandatory.
5. **Handoff.** Propose the epic → milestone mapping (milestone name, definition-of-done,
   initial scopes with status) → human gate. On approval, milestone entries are written
   by the host's normal progress-doc editing flow; future reconciliation belongs to the
   progress-reconciliation process.

Re-entry: when artifacts already exist, diff the human's new intent against the current
PRD/architecture, propose amendments section by section, and record superseded decisions
rather than silently rewriting them.

## Constraints (and why)

- **Human gates are mandatory.** Draft one section at a time; present it short enough to
  actually read; wait for explicit approval before the next section. Two rejections of
  the same section → stop drafting and re-elicit (the misunderstanding is upstream of
  the prose).
- **Elicit, don't dump.** Vision is extracted through questions, never invented. One
  focused question set at a time; prefer options with trade-offs over open-ended prompts
  when the human seems undecided.
- **Evidence-grounded.** Claims about users, facts, or history must trace to the
  provided grounding sources — never to training-data assumptions. Conflicts with a
  settled-facts ledger or standing guardrails are escalated, not resolved silently.
- **Context-free executability.** Every epic and milestone proposal must be actionable
  by an agent with no access to this conversation: name the inputs, the outputs, and a
  binary definition-of-done.
- **Governance discipline.** Root planning docs are governance artifacts: create or
  modify them only with in-turn human approval. No volatile metrics (counts that go
  stale) in any artifact — durable rules only.
- **Pointers over copies.** Reference the host's existing docs and processes; never
  restate the progress-doc or commit conventions owned downstream.
- **Template hygiene.** Follow each template section's embedded instruction, then delete
  the instruction comments from the final artifact.

## Stop rules — halt and ask, never resolve silently

- The same artifact section is rejected twice.
- Elicited intent contradicts a grounding source (ledger, guardrail, approved artifact).
- An epic cannot be given a binary acceptance criterion or a milestone
  definition-of-done.
- The engagement would write to any governance file without explicit approval given in
  the current turn.
- The scope grows beyond planning artifacts into implementation — hand off instead of
  drifting.

## Reversibility & HITL tiers

| Action | Reversibility | Tier |
|---|---|---|
| Elicitation questions, drafts shown in conversation | Fully reversible | Full autonomy |
| Creating/editing the brief, PRD, architecture doc | Reversible (with checkpoints) but governance | Proposal-first (approve each section) |
| Progress-doc milestone entries | Reversible | Proposal-first |
| Deleting or superseding an approved artifact | Reversible with effort | Human-required |
| Publishing or sharing artifacts externally | Practically irreversible | Human-required |

## Acceptance criteria (per engagement, binary)

- PRD and architecture doc exist, every section human-approved.
- Each epic has ≥1 binary acceptance criterion; each proposed milestone has a testable
  definition-of-done.
- No template instruction comments remain in final artifacts.
- No volatile metrics in any artifact.
- Cold-start test passes.

## Bundled-file manifest (fate of every file in the source skill)

| Source file | Platform-neutral fate |
|---|---|
| `SKILL.md` | Distilled into this generic; the source remains canonical — re-derive on change |
| `evals/trigger-eval.md` | **Ships with every port** — the §6 install-acceptance set (queries + expected verdicts, generic by construction); the receiving agent self-administers it post-install. Triggering conformance only |
| `references/brief-template.md` | Abstracted into the **section templates** contract row — attach/bundle on hosts that carry resources; degrade per the contract otherwise |
| `references/prd-template.md` | Same as above |
| `references/architecture-template.md` | Same as above |
