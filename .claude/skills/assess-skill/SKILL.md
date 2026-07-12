---
name: assess-skill
description: >-
  Audit a consumer-submitted SKILL.md against Contract-derived criteria from
  IL guides G1, G3b, G5, G6, G8 — plus G9.I6 for safety-critical skills (any
  skill whose allowed-tools or procedure perform destructive actions). Also
  validates DD-92 ContextSpec conformance (presence, universal vocabulary,
  IL-meta leak) on artifacts that carry a `context:` frontmatter block.
  Composes audit.md × skill.md from the Librarian reference layer. Read-only;
  produces findings + follow-ups.
user-invocable: true
allowed-tools: Read Grep Glob Write
argument-hint: "<skill-file-path>"
---

# Assess Skill

Load-and-apply wrapper over `audit.md` (operation) × `skill.md` (concept).
IL-KB-grounded audit of a Claude Code skill, with mandatory G9.I6 enforcement
when destructive actions are in scope.

## When to Use This Skill

- Consumer wants an audit of a `SKILL.md` or similar skill-packaging artifact.
- Consumer is preparing a skill for deployment and wants governance coverage
  verified (particularly G9.I6 for destructive actions).

## Safety-Critical Classification

A skill is safety-critical if **any** of:
- `allowed-tools` includes Write, Edit, Bash (with destructive flags), or any
  MCP tool that mutates external state.
- Procedure steps include deployment, publication, cross-system writes, or
  credential handling.
- Output is consumed by a downstream automated action without human review.

For safety-critical skills, **G9.I6 always fires** regardless of whether the
skill's prose mentions governance. This is a non-negotiable audit-composition
rule from session 48 Test 4.

## What This Skill Does NOT Do

- Does not rewrite the skill. Read-only.
- Does not deploy or activate the skill.
- Does not audit generic workflows or playbooks — only skill-shaped
  artifacts (file with `name`, `description`, `allowed-tools`, procedure body).

## Cognitive Disposition

Librarian Audit — read-only, citation-grounded, safety-aware. The G9.I6 gate
is a forcing function for destructive-action skills; do not skip it even if
the skill prose doesn't raise the topic. The DD-92 ContextSpec audit is a
deploy-boundary check — it fires when the artifact carries a `context:`
frontmatter block, regardless of whether the skill prose mentions it.

## Paths

| Path | Purpose |
|------|---------|
| `systems/improvement-loop/operations/references/librarian/audit.md` | Operation file |
| `systems/improvement-loop/operations/references/librarian/skill.md` | Concept file |
| `systems/improvement-loop/extracts/guides/` | Substrate — Contract subsections for {G1, G3b, G5, G6, G8}, plus G9 for safety-critical |
| Consumer-provided path | Skill under audit |

## Procedure

### Step 0: Parse input

1. Accept skill as file path (inline text is rare for skills). `Read` the file.
2. Extract frontmatter: `name`, `description`, `allowed-tools`, `argument-hint`.
3. Classify: is the skill safety-critical per §"Safety-Critical Classification"?
   Record the classification and the specific trigger (e.g., "allowed-tools
   includes Write").

### Step 1: Load composition

1. `Read` `operations/references/librarian/audit.md`.
2. `Read` `operations/references/librarian/skill.md`.
3. Compose the guide set: {G1, G3b, G5, G6, G8}. If safety-critical, add G9
   with G9.I6 specifically forced to fire.
4. `Read` the `### Contract` subsection of each guide in the set.

### Step 2: Build rubric

Per `audit.md` Phase 2. For safety-critical skills, G9.I6 appears in the
rubric as a non-latent invariant — precondition gating does not suppress it.

### Step 3: Apply rubric

File-verifiable checks on the skill body: trigger description quality (G8),
tool use discipline (G5), workflow termination (G3b), permissions (G6),
spec quality (G1). For safety-critical, G9.I6: does the skill's procedure
explicitly gate destructive actions on human approval?

System-verifiable follow-ups: e.g., "is the skill tested in dry-run mode
before being used against production?" — system-verifiable, becomes a
follow-up question.

### Step 3.5: DD-92 ContextSpec audit

Additive deploy-boundary check on artifact frontmatter. Composes with — does
not replace — the Contract-derived audit above.

**Applicability gate.** Inspect the artifact frontmatter for a `context:`
block. If absent, record one informational note in the working report:
"DD-92 ContextSpec audit skipped — no `context:` block in frontmatter.
DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts
without ContextSpec are not flagged here." Skip the three checks below.

If present, run all three checks. Findings emit into the same file-verifiable
table as Contract-derived findings; cite source as `DD-92` (literal, not
`<guide>.md#<anchor>`); tier 1; confidence High.

**Check 1 — Presence.** Verify all 8 required fields under `context:` are
present and non-null:

- `applies_to` (non-empty list)
- `platform_coupling`
- `autonomy`
- `stage`
- `reversibility`
- `auditability`
- `evidence_strength`
- `adoption.status`

(`adoption.notes` may be null.) For each missing or null field, emit one
finding: aspect="ContextSpec presence", outcome=Missing, evidence=field name.

**Check 2 — Universal-vocabulary scan.** Scan the values of `applies_to`
(each list entry), `platform_coupling`, `autonomy`, `stage`, `reversibility`,
`auditability`, and `adoption.notes` for forbidden tokens — same set as
`/extract-artifacts` Step 2.5:

- MetaSystem scope labels: `S2`, `S3`, `General` (when used as scope
  shorthand), `Perplexity Skills`
- IL-internal skill names: `/identify-artifacts`, `/extract-artifacts`,
  `/assess-skill`, `/assess-agent`, `/research-loop`, `/promote-findings`,
  `/synthesize-guide`, `/reassess-priorities`
- IL-specific path prefixes: `systems/improvement-loop/`, `extracts/`,
  `research-findings/`, `research-sources/`, `research-authorities/`

For each hit, emit one finding: aspect="ContextSpec universal vocabulary",
outcome=Violated, evidence=`<field>: '<offending token>'`.

**Check 3 — IL-meta leak.** Inspect top-level frontmatter (NOT inside the
`context:` block) for any of: `confidence`, `tier`, `reason_codes`,
`co_occurrence`. Per DD-92, IL classification metadata MUST be stripped at
the deploy boundary. For each present, emit one finding: aspect="IL
classification meta leak", outcome=Violated, evidence=`top-level frontmatter
contains '<key>'`.

### Step 4: Assemble report

Per `audit.md` §"Output shape". Read-contract elements (query restatement,
tier trace, confidence, citations). If safety-critical, open the Summary
with the G9.I6 outcome — it's the load-bearing finding for deployment
readiness.

### Step 5: Confidence + provenance pass

Per `audit.md` Phase 5.

## Output Shape

See `audit.md` §"Output shape". Add a one-line classification note at the
top: "Classification: safety-critical (trigger: <which>)." or
"Classification: non-safety-critical." DD-92 ContextSpec findings (if any)
interleave with Contract-derived findings in the same file-verifiable
findings table; source cited as `DD-92`. The applicability-gate note (when
ContextSpec is absent) appears in the Summary or as a one-line preamble to
the findings table.

## Boundaries

- If the submitted artifact doesn't have skill frontmatter (`name`,
  `description`, `allowed-tools`), reject — "this appears to be a workflow
  or playbook, not a SKILL.md — redirect to `/assess-agent` if it's an agent
  spec, or a playbook review (no IL skill yet)."
- If `allowed-tools` includes destructive tools but the procedure body does
  not describe the destructive operations, flag as a follow-up (the skill
  may be misconfigured).

## Boundary-Case Encounter Surfacing

On any deviation from the Tier-1 happy path (the 13-type encounter taxonomy — missing concept/operation, ambiguous verb/variant, cross-concept, verb-noun-mismatch, oversized-artifact, hop-ceiling-hit, tier-3-read, low-confidence, kb-gap, redirect, clarification-asked), surface the encounter in this run's report output: encounter type + one-line description.

Persistent encounter logging is **suspended**: the System Log is retired as a producer (DD-116; DD-59 scope note), and the durable destination for boundary-case records is Nick-gated via the Phase-2 second-brain proposal (substrate audit gate G9). Until that ruling, this skill writes no encounter records to disk.

- Taxonomy, per-encounter body shape, and feedback routing: `systems/improvement-loop/operations/references/librarian/boundary-cases.md`

## Cross-References

- Operation file: `systems/improvement-loop/operations/references/librarian/audit.md`
- Concept file: `systems/improvement-loop/operations/references/librarian/skill.md`
- Session-48 Test 4 (where the G9.I6 gate was validated):
  `systems/improvement-loop/project-management/design-notes/2026-04-21-contract-section-spotcheck-agent-audit.md`
- Read-contract: `systems/improvement-loop/project-management/design-notes/2026-04-21-librarian-read-contract.md`
- Boundary-case tracking: `systems/improvement-loop/project-management/design-notes/2026-04-22-librarian-boundary-case-tracking.md`
- Governing DDs: DD-78, DD-82, DD-89, DD-92
