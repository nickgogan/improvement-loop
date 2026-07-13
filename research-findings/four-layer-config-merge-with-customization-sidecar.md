---
name: "Four-Layer Config Merge with Per-Skill Customization Sidecar"
summary: |-
  Plain English: let users extend and re-tune shipped skills without forking their
  prose, by giving every skill a customization sidecar file and resolving configuration
  through four layers (installer-owned vs human-authored × team vs personal) with typed
  merge rules. BMAD v6.10.0 merges `_bmad/config.toml` → `config.user.toml` →
  `custom/config.toml` → `custom/config.user.toml` via a stdlib-only script with
  structural semantics: scalars override, tables deep-merge, `code`/`id`-keyed arrays
  merge by key, other arrays append. Every one of its 47 skills carries a
  `customize.toml` exposing activation hooks (prepend/append steps), persistent_facts
  (user-injectable standing context), reviewer rosters, and on_complete actions.
  Installer-owned files are regenerated on update ("# DO NOT EDIT"); human overrides
  live in committed `custom/` (team) and gitignored `*.user.toml` (personal). A
  documented in-prose fallback (the skill re-derives the merge manually if the script
  is missing) makes the mechanism degradation-tolerant.
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "everything-as-skill-architecture.md"
    rel: "extends"
  - file: "core-specialized-skill-inheritance-pattern.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "governance"
  - "configuration"
  - "skill-customization"
---

# Four-Layer Config Merge with Per-Skill Customization Sidecar

## What It Is

A governed override surface for a shipped skill framework, built from three pieces:

1. **Four config layers** crossing two axes — installer-owned vs human-authored, and
   team-shared vs personal: `_bmad/config.toml` (installer, regenerated on update) →
   `config.user.toml` (personal) → `custom/config.toml` (team, committed) →
   `custom/config.user.toml` (personal, gitignored).
2. **Typed structural merge** (`resolve_config.py`, stdlib-only): scalars override,
   tables deep-merge, arrays keyed by `code`/`id` merge by key, other arrays append —
   so a user can add one reviewer to a roster without restating the roster.
3. **Per-skill sidecar** — every skill ships a `customize.toml` (agent skills an
   `[agent]` table, workflow skills a `[workflow]` table) declaring
   `activation_steps_prepend/append`, `persistent_facts` (literal facts, `file:` globs,
   `skill:` pointers held for the whole run), `on_complete`, output paths, and reviewer
   rosters. The skill reads its own merged config as activation step 1, with a
   documented manual-merge prose fallback if the script is unavailable.

## Why It Matters

The standard failure of shipped prompt frameworks is the fork: users edit skill prose
to change behavior, then every upstream update is a merge conflict. This design gives
behavior extension a *governed* home — user context injection becomes a config field
(`persistent_facts`) instead of prompt editing, and the installer/human file partition
means updates regenerate what they own without touching what users own. The typed merge
semantics matter more than they look: keyed-array merge is what makes small overrides
composable instead of clobbering.

## Why People Are Using It

Uniform across all 47 BMAD skills; the file partition and merge script are what let the
installer update 42 platform targets without destroying user customization. Source:
Observed in [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) v6.10.0 — see
[[bmad-method-analysis]] for structural details.

## Potential Alternatives

- **Fork-and-edit** — the default everywhere else; upstream updates become manual
  merges.
- **Inheritance-based skill layering** (core + specialized skills) — extension by
  new files rather than config; expressive but no typed merge or ownership partition.
- **Environment variables / CLI flags** — fine for scalars, unusable for rosters,
  hooks, and standing context.

## Potential Improvements

- Schema validation of sidecar contents so bad overrides fail at resolve time, not
  mid-run.
- Effective-config introspection ("show me the merged result and which layer each
  value came from").

## Potential Failure Modes

- **Merge-rule opacity** — four layers with per-type semantics is hard to reason about
  when a value surprises; debugging needs the provenance view it lacks.
- **Prose fallback drift** — the documented manual merge duplicates the script's rules
  in prose; the two can diverge.
- **Override sprawl** — persistent_facts and activation hooks are unbounded context
  injection; user layers can quietly rebuild the monolithic prompt the framework
  avoided.
