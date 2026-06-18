---
title: "Core/Specialized Skill Pair Specification Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "core-specialized-skill-inheritance-pattern"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "skill systems shared across multiple repositories or deployment contexts where per-repo behavioral customization is needed"
    - "any agent skill being factored into a reusable core and a repo-specific or context-specific variant"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "low — splitting an existing monolithic skill into core/specialized requires refactoring skill files and updating references; future merges or reversions require equivalent effort"
  auditability: "high — the specializes field in frontmatter makes the inheritance relationship explicit and diffable; overridable categories are declared in the core skill and auditable independently"
  evidence_strength: "Strong (production-tested)"
  adoption:
    status: "Not Yet Started"
    notes: "Production evidence from Warp (warpdotdev/warp): 15 skills in .agents/skills/, multiple using specializes field. Core skills managed in separate common-skills repo with skills-lock.json versioning."
contract:
  preconditions: "At least one skill is being authored or refactored for use across more than one repository or deployment context. The customization needs of the different contexts are understood well enough to identify which categories of behavior should be overridable."
  invariants: "The core skill defines the full skill contract: output schema, safety rules, evidence rules, and the explicit list of overridable categories. Specialized skills declare specializes in frontmatter and override only the declared-overridable categories. Specialized skills cannot redefine the core contract (schema, safety rules, follow-up rules). The core skill is versioned independently; specialized skills declare which version of the core they target."
  governance: "Owner: the team or system that maintains the shared skill repository (equivalent of common-skills). Core skill contracts are not modified without a versioned change to the core skill file. Overridable category declarations in the core skill are explicit — omission means non-overridable. Specialized skill reviews verify that overrides stay within declared slots before merging."
  recovery: "If a specialized skill overrides a non-overridable category → reject the specialized skill; surface a conflict report specifying the unauthorized override. If the core skill changes a previously overridable category to non-overridable → audit all specialized skills that override that category; require re-review before the core version bump is accepted. If core and specialized conflict on non-overridable content → the core wins unconditionally; the conflict is surfaced as a diagnostic."
tags:
  - "extracted-artifact"
  - "template"
  - "agent-design"
  - "skill-architecture"
  - "inheritance"
---

# Core/Specialized Skill Pair Specification Template

**Source:** [[core-specialized-skill-inheritance-pattern]]
**Form:** template
**Extraction date:** 2026-05-25

A two-file template for the core/specialized skill architecture. Use this when factoring a skill into a shared core and one or more context-specific variants.

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{SKILL_NAME}}` | Canonical skill name (lowercase-hyphenated) | `triage-issue` |
| `{{SKILL_DESCRIPTION}}` | What the skill does in plain English | `Triage an incoming issue: assign labels, severity, and owner` |
| `{{OVERRIDABLE_CATEGORIES}}` | Comma-separated list of category names that specialized skills may override | `label-taxonomy, severity-scale, assignment-heuristics` |
| `{{CORE_VERSION}}` | Semver version of this core skill | `1.0.0` |
| `{{OUTPUT_SCHEMA_REF}}` | Path or inline schema defining the required output structure | `schemas/triage-output.json` |
| `{{SAFETY_RULES}}` | Non-overridable safety constraints | `Never assign to an owner who is on-call-exempt` |
| `{{SPECIALIZED_SKILL_NAME}}` | Repo-specific skill name (lowercase-hyphenated) | `triage-issue-local` |
| `{{TARGET_CORE_VERSION}}` | Core skill version this specialization targets | `1.0.0` |
| `{{REPO_CONTEXT}}` | Plain-English description of the repo's customization context | `Warp terminal repo — labels follow warp-specific taxonomy` |
| `{{OVERRIDDEN_CATEGORY}}` | One of the declared overridable categories being customized | `label-taxonomy` |
| `{{OVERRIDE_CONTENT}}` | The repo-specific content replacing the core default | `[ux-bug, perf, crash, feature-request, docs]` |

---

## Body

### File 1 — Core Skill (`common-skills/{{SKILL_NAME}}.md`)

```yaml
---
name: {{SKILL_NAME}}
version: {{CORE_VERSION}}
description: >
  {{SKILL_DESCRIPTION}}
  This is the core skill definition. Specialized skills may override only the
  categories listed in overridable_categories.
overridable_categories:
  - {{OVERRIDABLE_CATEGORIES}}
output_schema: {{OUTPUT_SCHEMA_REF}}
safety_rules:
  - "{{SAFETY_RULES}}"
  # Add additional non-overridable rules here. These apply in all specializations.
follow_up_rules:
  - "Always surface confidence level in output."
  # Non-overridable follow-up behavior goes here.
---
```

```markdown
# {{SKILL_NAME}} — Core Skill

## Purpose
{{SKILL_DESCRIPTION}}

## Output Contract
All implementations must produce output conforming to `{{OUTPUT_SCHEMA_REF}}`.
This contract is non-overridable.

## Overridable Categories

The following categories may be customized by specialized skills.
All other behavior is fixed by this core definition.

### {{OVERRIDABLE_CATEGORIES}} (overridable)
[Default behavior for each overridable category goes here.]

## Non-Overridable Behavior

### Safety Rules
{{SAFETY_RULES}}

### Follow-Up Rules
Always surface confidence level in output.
[Additional non-overridable follow-up rules here.]
```

---

### File 2 — Specialized Skill (`.agents/skills/{{SPECIALIZED_SKILL_NAME}}.md`)

```yaml
---
name: {{SPECIALIZED_SKILL_NAME}}
specializes: {{SKILL_NAME}}
core_version: {{TARGET_CORE_VERSION}}
description: >
  {{REPO_CONTEXT}}. Only the categories declared overridable by the core
  {{SKILL_NAME}} skill (v{{TARGET_CORE_VERSION}}) may be specialized here.
---
```

```markdown
# {{SPECIALIZED_SKILL_NAME}} — Specialized Skill

**Specializes:** [[{{SKILL_NAME}}]] v{{TARGET_CORE_VERSION}}
**Context:** {{REPO_CONTEXT}}

## Overrides

Only categories declared overridable in `{{SKILL_NAME}}` v{{TARGET_CORE_VERSION}} are
customized here. All other behavior is inherited from the core skill unchanged.

### {{OVERRIDDEN_CATEGORY}}
{{OVERRIDE_CONTENT}}

<!-- Repeat for each overridable category being customized. -->
<!-- Do not include sections for categories not being overridden. -->
<!-- Do not include sections for non-overridable categories. -->
```

---

## Usage

**When to use this template:**
- A skill serves multiple repositories with differing heuristics, taxonomies, or style patterns but the same core contract.
- You want customization to be auditable: reviewers can check specialized skills against the declared overridable categories in the core.
- You want to prevent divergence: the core contract (schema, safety, follow-up rules) stays shared; only declared slots can differ.

**Authoring sequence:**
1. Identify the full skill contract: output schema, safety rules, evidence rules, follow-up rules. These go in the core and are non-overridable.
2. Identify the categories that legitimately differ by repo context (taxonomies, heuristics, style). Declare these as `overridable_categories` in the core frontmatter.
3. Write the core skill to `common-skills/` (or equivalent shared directory). Version it.
4. For each repo needing a specialization, create a specialized skill in `.agents/skills/`. Declare `specializes` and `core_version`. Override only the declared-overridable categories.
5. During skill review, verify that the specialized skill's overrides are all within the declared `overridable_categories` of the targeted core version.

**Design checklist before authoring:**
- [ ] Core contract (output schema, safety rules, follow-up rules) is fully defined and non-overridable.
- [ ] Overridable categories are explicitly listed in the core frontmatter — omission means non-overridable.
- [ ] Core skill is versioned; specialized skills declare which version they target.
- [ ] Specialized skill contains overrides for declared-overridable categories only — no unauthorized redefinitions.

---

## Variation Axis

| Axis | Core Side | Specialized Side |
|------|-----------|-----------------|
| Output schema | Defined, non-overridable | Must conform |
| Safety rules | Defined, non-overridable | Inherited unchanged |
| Follow-up rules | Defined, non-overridable | Inherited unchanged |
| Label / tag taxonomies | Default provided | Overridable — replace with repo-specific taxonomy |
| Severity scales | Default provided | Overridable — replace with repo-specific scale |
| Assignment heuristics | Default provided | Overridable — replace with repo-specific heuristics |
| Style / tone guidance | Default provided | Overridable — replace with repo-specific style |

The core author controls what is overridable. If a specialization needs to override something not on the list, the request goes back to the core author — who decides whether to expand the overridable set or keep it fixed.

---

## Contract

### Preconditions
At least one skill is being authored or refactored for use across more than one repository or deployment context. The customization needs of the different contexts are understood well enough to identify which categories of behavior should be overridable.

### Invariants
The core skill defines the full skill contract: output schema, safety rules, evidence rules, and the explicit list of overridable categories. Specialized skills declare `specializes` in frontmatter and override only the declared-overridable categories. Specialized skills cannot redefine the core contract (schema, safety rules, follow-up rules). The core skill is versioned independently; specialized skills declare which version of the core they target.

### Governance
Owner: the team or system that maintains the shared skill repository (equivalent of common-skills). Core skill contracts are not modified without a versioned change to the core skill file. Overridable category declarations in the core skill are explicit — omission means non-overridable. Specialized skill reviews verify that overrides stay within declared slots before merging.

### Recovery
If a specialized skill overrides a non-overridable category → reject the specialized skill; surface a conflict report specifying the unauthorized override. If the core skill changes a previously overridable category to non-overridable → audit all specialized skills that override that category; require re-review before the core version bump is accepted. If core and specialized conflict on non-overridable content → the core wins unconditionally; the conflict is surfaced as a diagnostic.
