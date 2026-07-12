---
name: 'Skills Are Generic, Users Are Data — Invocation-Time Context Injection'
summary: 'A hard decoupling rule for reusable skills: skill packages carry zero user/instance-specific content; the specifics (identity constraints, current targets, timelines, voice) live in one predictable per-user folder — users/{user-id}/agent-context/ — loaded at invocation time before any drafting. Containment is bidirectional: user context never gets copied into shared layers (pointer-only references), and one user''s context is never read into another user''s work. Skill packages are self-contained directories with description-triggered discovery and mandatory self-administrable trigger evals.'
implementation_notes: 'The engine''s equivalent split is engine-generic skills vs. consumer/system-specific context — the same invariant the /assess-* skills check as ContextSpec IL-meta leak. Adoptable: (1) formalize "where do instance specifics enter?" as a named invocation-context surface per consumer system rather than ad-hoc; (2) the mandatory per-skill trigger-eval file (evals/trigger-eval.md, coverage audit-enforced) is a concrete packaging bar the engine''s /design-skill could emit and /assess-skill could check; (3) the leak-risk stance — example contents deliberately omitted from install docs — is a documentation discipline worth copying for any tenant-shaped data.'
category: Agent Design
evidence_strength: Medium (practitioner-documented, single production system)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-wiring-canon.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: raw
consumed_by: []
tags:
- skill-decoupling
- invocation-context
- tenant-isolation
- skill-packaging
---
# Skills Are Generic, Users Are Data — Invocation-Time Context Injection

## What It Is

The core separation that makes a skill library reusable across users (or instances,
tenants, consumer systems): skills carry method only; everything user-shaped enters at
invocation time from one predictable per-user place — `users/{user-id}/agent-context/`
— holding a README (what loads when), hard identity constraints, the active target set
(volatile — never trusted from any other surface), timelines, and a writing-voice
guide. Skill packages themselves are self-contained directories (SKILL.md plus optional
references/, scripts/, assets/) discovered by description match.

## Why It Matters

Plain English: the moment a user fact lands inside a skill body, that skill stops being
reusable and starts being a leak vector — it will surface that fact for the wrong user
or ship it in an export. Keeping the split absolute means every skill runs for any user,
the whole method layer exports cleanly, and privacy review reduces to auditing one
folder boundary instead of reading every skill. The same logic applies wherever a system
serves multiple instances: consumer systems, projects, tenants.

## How It Works

- **Load rule:** agents load the user's agent-context (with their profile) *before
  drafting anything* for that user; the guardrails in it are hard constraints, not
  suggestions.
- **Containment rule (bidirectional):** contents never get copied into shared layers —
  method KB, skills, always-on file, root control surfaces — only pointer-form
  references exist elsewhere. And tenant isolation: one user's context is never read
  into another user's work.
- **Single-surface volatility:** the active target set lives only here; any other
  surface claiming to know the user's current targets is by definition stale.
- **Package shape enforcing the split:** one directory per skill, name matching the
  skill name; open-standard frontmatter fields only (name, description, license,
  metadata, allowed-tools, compatibility); description carries what + when + trigger
  phrases (the description *is* the runtime interface — "a skill that never triggers
  is dead capability"). Every package ships a mandatory `evals/trigger-eval.md` —
  a self-administrable trigger-eval set, coverage enforced by audit. Exportable skills
  add a machine-readable `capability-contract.yaml` sidecar, ports/, and package meta.
- **Eval decoupling:** shipped eval sets carry zero references to the meta-tooling that
  authored them — evals travel with every package but never couple a product skill to
  its authoring toolchain.
- **Leak-risk documentation stance:** the canon doc for this folder deliberately carries
  no example contents — "any concrete guardrail, target, or timeline in an install doc
  is a violation of the separability bar, not a helpful illustration."

## How It Could Fail

The split dies by convenience: inlining "just this one" user fact into a skill during a
deadline. It needs the edit-time path-scoped guardrail and the export audit as backstops.
Invocation-time loading adds a failure mode of its own — a skill invoked without the
context loaded produces generic output that looks plausible; the load rule must be
checkable (e.g. the skill's procedure names the context files it requires).
