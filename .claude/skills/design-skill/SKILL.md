---
name: design-skill
description: >-
  Draft a new SKILL.md from designer intent using IL substrate. Walks the
  skill.md §Construction Decision sequence (name → trigger → tools → safety-
  critical classification → procedure/state/termination → output shape →
  composition cross-check), applies the Template skeleton, and produces a
  complete draft. Then invokes /assess-skill as a separate subagent in fresh
  context (rule 10) and surfaces the audit findings alongside the draft. Does
  not deploy. Composes design.md × skill.md from the Librarian reference layer.
user-invocable: true
allowed-tools: Read Grep Glob Write Agent
argument-hint: "<intent-description> [--target-path <where-to-write>] [--partial <existing-draft-path>]"
---

# Design Skill

Load-and-apply wrapper over `design.md` (operation) × `skill.md` (concept).
Constructive peer of `/assess-skill` — same concept-doc substrate, read
bilingually per IL rule 12.

## When to Use This Skill

- Designer wants to draft a new SKILL.md from intent (verb-phrase scope,
  trigger conditions, output shape).
- Designer has a partial SKILL.md and wants the missing sections filled in.
- Designer wants the draft graded against IL audit criteria before deploying.

## What This Skill Does NOT Do

- Does not deploy the draft. Writing to an enforcement location is the
  designer's decision (see Output shape — `--target-path` writes only on
  explicit approval; default is inline presentation).
- Does not internally assess the draft. Per IL rule 10, audit is delegated
  to `/assess-skill` invoked as a separate subagent in fresh context.
- Does not modify `skill.md`, `design.md`, or any other IL concept/operation
  file. If a Decision-sequence step exposes a substrate gap, report it as a
  Librarian gap report — do not fix it inline.
- Does not draft agents, prompts, or harness configs. Use `/design-agent`
  for agents; prompt design has no dedicated skill yet (designer should use
  `/prompt-enhancer` workspace skill).

## Cognitive Disposition

Librarian Builder mode — accessible, evidence-cited, substrate-grounded. The
design operation is the constructive peer of audit; both compose the same
concept doc bilingually. Construction substrate (Decision sequence, Template
skeleton, Scoping heuristics, Authoring-time anti-patterns) is load-bearing;
§Composition is read here only as a forward-reference to what `/assess-skill`
will fire on at Phase 5.

The safety-critical classification at Decision-sequence step 4 is a hard gate
— do not defer it, do not draft the procedure first. Authoring a safety-
critical skill without HITL gating produces a draft that will fail audit on
first inspection.

## Paths

| Path | Purpose |
|------|---------|
| `systems/improvement-loop/operations/references/librarian/design.md` | Operation file — 6-phase procedure |
| `systems/improvement-loop/operations/references/librarian/skill.md` | Concept file — §Construction (Decision sequence, Template skeleton, Scoping heuristics, Authoring-time anti-patterns) and §Composition (forward-reference to audit) |
| `systems/improvement-loop/.claude/skills/assess-skill/SKILL.md` | Subagent invoked at Phase 5 |
| Designer-provided path (optional) | Partial draft to complete; or target write location on explicit approval |

## Procedure

### Step 0: Parse the query

1. Confirm verb is `design` (or synonym: construct, author, create, draft,
   build) and noun is `skill`. If not, stop and redirect.
2. Capture designer intent inline. If `--partial` is supplied, `Read` the
   partial draft. If the partial exceeds ~500 lines, ask the designer for
   scoping clarification before proceeding (over-scoping signal per
   `design.md`).
3. Capture optional `--target-path`. Do not write to it yet; presence only
   means the designer pre-authorizes a write at Phase 6 if approved.

### Step 1: Load construction substrate

1. `Read` `operations/references/librarian/design.md`.
2. `Read` `operations/references/librarian/skill.md`. Within it, read:
   - `### Decision sequence` (7 steps; step 4 is a hard gate)
   - `### Template skeleton`
   - `### Scoping heuristics`
   - `### Authoring-time anti-patterns`
   - `## Composition` (forward-reference only — for the Phase 5 audit surface
     the draft will face, NOT design-time substrate)

Do not pre-load full IL guide bodies. §Composition is consulted only to set
expectations for the assess-* subagent's coverage; the substrate driving
authoring choices is §Construction.

### Step 2: Elicit designer intent (Decision sequence walk)

Walk skill.md §Construction Decision sequence step by step. For each step,
state the step in one line, ask the designer the questions it requires,
record the answer in the Decision record.

**Step 1 — Name the single bounded operation.** Verb-phrase. Reject "and";
if the operation cannot be stated without conjunction, consult §Scoping
heuristics §"Split when". A SKILL.md whose Procedure section has one step
is almost always over-extracted (§Scoping heuristics §"Collapse when").

**Step 2 — Identify the trigger shape.** Capture consumer phrasings ("when
the user asks to X", "when Y condition occurs"). The `description`
frontmatter derives from this. Reject feature-label descriptions per
§Authoring-time anti-patterns §"Description that won't trigger" — consumer
phrasing wins.

**Step 3 — Enumerate the tool surface.** Minimal list. Reject over-granting
per §Authoring-time anti-patterns §"Tool over-granting"; each unused tool
widens the safety envelope at step 4 and adds deferred-loading cost.

**Step 4 — Safety-critical classification (HARD GATE).** Apply skill.md's
classification criteria verbatim:

> A skill is safety-critical if **any** of:
> - `allowed-tools` include Write, Edit, Bash (destructive flags), or any
>   MCP tool that mutates external state.
> - Procedure steps include deployment, publication, cross-system writes,
>   or credential manipulation.
> - Output is consumed by a downstream automated action without human review.

If safety-critical, the designer MUST state the HITL gate the procedure will
encode (confirm-before-act, dry-run mode, or explicit human-approval step).
Do not proceed to step 5 without a concrete HITL gate decision.

**Step 5 — Specify procedure, state, and termination.** Steps as ordered
list, naming the tool used and what's read/written. State explicitly what
ends the skill (success criterion + abort criterion).

**Step 6 — Specify output shape.** File path, report structure, conversation
message, or state change. Name it so the consumer can verify against it.

**Step 7 — Cross-check against §Composition.** Confirm authored surface
matches the audit surface. If no embedded context → G2a/G2b will not fire
at audit. If no tools → G5 will not fire. Mismatches mean over-scoping or
under-specification — flag in Phase 3.

Phase 2 produces the **Decision record**: one row per step, including any
scoping decisions made and why.

### Step 3: Surface authoring-time risks

Compare the Decision record against skill.md §Authoring-time anti-patterns
(six listed: tool over-granting; description that won't trigger; embedded
workflow; skipping safety-critical classification; conflating skill with
playbook; re-stating guide content in the procedure).

For each anti-pattern the in-progress posture could fall into, name it
explicitly and the mitigation that will appear in the draft. This produces
*forward-looking warnings* — not findings. Findings come from the Phase 5
audit. Do not assign tier/confidence here; do not substitute this for the
audit.

### Step 4: Draft the artifact

Apply skill.md §Template skeleton verbatim, filling placeholders from the
Decision record:

```markdown
---
name: <kebab-case-name>
description: <one-line description used for trigger matching — phrase it the way a consumer would ask>
allowed-tools: <minimal list>
argument-hint: <optional — what the user passes after the slash command>
---

# <Skill Display Name>

## When to use

<Concrete trigger conditions. Mirror the description in fuller prose; name the consumer questions that should invoke this skill and the ones that should not.>

## Procedure

1. <Step — name the tool used and what's read/written>
2. <Step>
3. <Step>

## Output shape

<Describe the produced artifact — file path, report structure, conversation message, etc.>

## Boundary conditions

- **Termination:** <When the skill ends. Success criterion. Abort criterion.>
- **Out of scope:** <Adjacent operations this skill does NOT do — point to the skill that does.>
- **Safety-critical?** <Yes / No, per §Construction Decision sequence step 4. If yes, name the HITL gate.>
```

The draft must be complete — frontmatter populated, all required sections
present, no `<placeholder>` text remaining for required fields. Optional
fields may be left empty with an explicit `# optional, omit if unused`
comment.

Do not write the draft to a file at this phase. The draft is presented
inline in the Phase 6 report. Writing happens at Phase 6 only if
`--target-path` was supplied AND the designer explicitly approves after
seeing the audit findings.

### Step 5: Delegate audit (rule 10 — non-negotiable)

Invoke `/assess-skill` as a separate subagent in fresh context. Use the
`Agent` tool with `subagent_type: general-purpose` and a self-contained
prompt that:

1. Names the draft (inline text OR a temp path — do not require the
   designer to have approved a target-path write at this phase).
2. Instructs the subagent to invoke `/assess-skill` against the draft and
   return the full audit report.

If the draft has not been written to a path, write it to a temp scratch
file under `/tmp/design-skill-draft-<timestamp>.md` so the subagent has a
readable path; the temp file is for audit input only and is not a
deployment.

Do not inspect the draft against rubric criteria inside this skill's
context. The epistemic gap rule 10 protects is exactly the boundary the
fresh-context subagent invocation preserves.

Collect the assess-* report.

### Step 6: Assemble report

Produce the design report per `design.md` §"Output shape". Include all
four deliverables: Decision record, Authoring-time risk surface, Draft
artifact, Audit findings (embedded /assess-skill output).

If `--target-path` was supplied AND the audit findings do not include any
HARD-blocking issues (Missing on G1.I1 Contract presence; Violated on G9.I6
for safety-critical with no HITL gate), present the write option:
"Approve writing the draft to `<target-path>`? (y/N)". Write only on
explicit `y`. Default is inline-only.

If `--target-path` was supplied AND the audit findings include HARD-blocking
issues, do NOT offer the write. State why ("audit flagged G9.I6 violation —
revise the HITL gate in step 4 of the Decision record and re-run").

## Output Shape

Per `design.md` §"Output shape":

```
## Design — skill

**Artifact:** <intended path or summary>
**Concept:** skill.md
**Safety-critical classification:** <Yes (trigger: <which>) / No>

### Decision record (Phase 2)

| Step | Decision | Source / scoping note |
|---|---|---|
| 1 — Name single bounded operation | … | … |
| 2 — Trigger shape | … | … |
| 3 — Tool surface | … | … |
| 4 — Safety-critical classification | <Yes/No>; HITL gate: <if Yes> | HARD GATE |
| 5 — Procedure, state, termination | … | … |
| 6 — Output shape | … | … |
| 7 — Composition cross-check | … | … |

### Authoring-time risks surfaced (Phase 3)

| # | Risk (from skill.md §Authoring-time anti-patterns) | Why it applies here | Mitigation in draft |
|---|---|---|---|
| 1 | … | … | … |

### Draft artifact (Phase 4)

<full SKILL.md draft, inline>

### Audit findings (Phase 5 — delegated to /assess-skill)

<embedded /assess-skill report: Findings table, Follow-ups table, Aspects-out-of-scope table, Summary>

### Summary

<1–3 sentences: what the draft does well, what risks remain, what the audit flagged, what the designer should decide next. If safety-critical, lead with the G9.I6 outcome.>
```

## Boundaries

- **Read-only on the KB and on concept docs.** This skill never modifies
  `skill.md`, `design.md`, IL guides, findings, or sources. If the designer's
  intent surfaces a substrate gap (a Decision-sequence step has no guidance
  for an emerging case), report it as a Librarian gap report in the Summary
  — do not patch the substrate.
- **No deploy.** Default behavior is inline presentation. Writing to a
  target path requires explicit per-invocation designer approval AND clean
  audit findings on hard gates.
- **No self-assessment (rule 10).** Phase 5 delegates to `/assess-skill` in
  fresh subagent context. The skill must not internally inspect the draft
  against G1/G3b/G5/G6/G8/G9.I6 — that is the assessor's epistemic role.
- **Partial drafts >500 lines.** Request scoping clarification before
  proceeding. Mirrors `audit.md` and `design.md`'s ~500-line threshold.
- **If the artifact isn't a skill.** If the designer's intent describes an
  agent (model-plus-context assembly under a stated intent), redirect to
  `/design-agent`. If it describes a workflow with explicit phase gates,
  recommend extracting phases into separate skills per skill.md §Scoping
  heuristics §"Embedded workflow".

## Boundary-Case Encounter Logging

On any deviation from the Tier-1 happy path (the 13-type encounter
taxonomy — missing concept/operation, ambiguous verb/variant, cross-concept,
verb-noun-mismatch, oversized-artifact, hop-ceiling-hit, tier-3-read,
low-confidence, kb-gap, redirect, clarification-asked), append a structured
record to `operations/system-log/session-<N>-librarian-encounters.md` per
the entry schema. Create the file on the session's first encounter; append
thereafter. `<N>` matches the session's SL entry number (infer from most
recent `session-<N>-*.md` in the folder).

- Schema, controlled vocabulary of 13 encounter types, per-encounter body
  shape, and feedback routing:
  `systems/improvement-loop/project-management/design-notes/2026-04-22-librarian-boundary-case-tracking.md`
- Write scope is narrowed to `operations/system-log/` only — do not write
  elsewhere from this hook.

## Cross-References

- Operation file: `systems/improvement-loop/operations/references/librarian/design.md`
- Concept file: `systems/improvement-loop/operations/references/librarian/skill.md`
- Symmetric audit skill: `systems/improvement-loop/.claude/skills/assess-skill/SKILL.md`
- Read-contract: `systems/improvement-loop/project-management/design-notes/2026-04-21-librarian-read-contract.md`
- Boundary-case tracking: `systems/improvement-loop/project-management/design-notes/2026-04-22-librarian-boundary-case-tracking.md`
- Librarian agent definition: `systems/improvement-loop/agents/librarian/agent.md`
- Governing rules: IL `agent-rules.md` rule 10 (generator-assessor separation), rule 11 (abstractions must earn their keep), rule 12 (audit/design symmetry)
- Governing DDs: DD-78, DD-82, DD-89, DD-92
