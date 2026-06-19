---
name: design-agent
description: >-
  Draft a new agent specification (agent.md, CLAUDE.md, or system prompt for an
  agent) from designer intent using IL substrate. Walks the agent.md
  §Construction Decision sequence — variant selection (A prompt-based /
  B harness-based / C autonomous-vs-supervised) gates the rest, then identity →
  context → architecture → (variant B) harness surface → (variants B/C)
  workflow/termination → (variant C primarily) autonomy envelope → (variant C)
  session persistence → recovery → composition cross-check. Applies the
  common-core Template skeleton plus declared variant overlays. Then invokes
  /assess-agent as a separate subagent in fresh context (rule 10) and surfaces
  the audit findings alongside the draft. Does not deploy. Composes design.md
  × agent.md from the Librarian reference layer.
user-invocable: true
allowed-tools: Read Grep Glob Write Agent
argument-hint: "<intent-description> [--variant prompt-based|harness-based|autonomous] [--target-path <where-to-write>] [--partial <existing-draft-path>]"
---

# Design Agent

Load-and-apply wrapper over `design.md` (operation) × `agent.md` (concept).
Constructive peer of `/assess-agent` — same concept-doc substrate, read
bilingually per IL rule 12. Variant-aware: the variant selected at Decision
step 1 gates which overlays compose into the draft.

## When to Use This Skill

- Designer wants to draft a new agent artifact (`agent.md`, `CLAUDE.md`,
  system prompt for an agent) from intent.
- Designer has a partial agent spec and wants the missing sections — or the
  variant-specific overlays — filled in.
- Designer wants the draft graded against IL audit criteria before deploying.

## What This Skill Does NOT Do

- Does not deploy the draft. Default behavior is inline presentation;
  `--target-path` writes only on explicit per-invocation approval after
  audit findings.
- Does not internally assess the draft. Per IL rule 10, audit is delegated
  to `/assess-agent` invoked as a separate subagent in fresh context.
- Does not modify `agent.md`, `design.md`, or any other IL concept/operation
  file. Substrate gaps are reported as Librarian gap reports, not patched.
- Does not draft skills, prompts, or harness configs in isolation. Use
  `/design-skill` for SKILL.md; skills bundled with an agent are noted in
  the Skill Inventory section of the agent draft, not authored here.
- Does not pre-decide between variants A, B, C. If intent is ambiguous, ask
  one disambiguating question per agent.md §"Decision sequence" step 1.

## Cognitive Disposition

Librarian Builder mode — accessible, evidence-cited, substrate-grounded,
variant-aware. Variant selection (step 1) is consequential: it determines
which guides will fire at audit and which overlay sections the draft must
carry. A Variant A agent that silently embeds tool/permission directives is
the canonical authoring-time anti-pattern (variant drift); flag and re-route
to Variant B before continuing.

Hard gates:
- **Variant C autonomy-envelope sizing (step 7).** Trust thresholds, HITL
  gates, escalation paths must be concrete before drafting the Autonomy
  Table.
- **G9.I6 for any destructive-action path.** Analogous to skill safety-
  critical classification; fires unconditionally on destructive-action paths
  regardless of variant.

## Paths

| Path | Purpose |
|------|---------|
| `systems/improvement-loop/operations/references/librarian/design.md` | Operation file — 6-phase procedure |
| `systems/improvement-loop/operations/references/librarian/agent.md` | Concept file — §Construction (Decision sequence, Template skeleton with variant overlays, Scoping heuristics, Authoring-time anti-patterns) and §Composition (forward-reference to audit, variant-aware) |
| `systems/improvement-loop/.claude/skills/assess-agent/SKILL.md` | Subagent invoked at Phase 5 |
| Designer-provided path (optional) | Partial draft to complete; or target write location on explicit approval |

## Procedure

### Step 0: Parse the query

1. Confirm verb is `design` (or synonym) and noun is `agent`. If not, stop
   and redirect.
2. Capture designer intent inline. If `--partial` is supplied, `Read` the
   partial draft. If the partial exceeds ~500 lines, ask the designer for
   scoping clarification before proceeding (over-scoping signal).
3. Capture optional `--target-path` (no write happens at this phase) and
   optional `--variant` hint (used in step 2 alongside intent-based
   inference; designer flag wins on disagreement).

### Step 1: Load construction substrate

1. `Read` `operations/references/librarian/design.md`.
2. `Read` `operations/references/librarian/agent.md`. Within it, read:
   - `### Decision sequence` (10 steps; step 1 gates the rest)
   - `### Template skeleton` (common core + variant overlay blocks)
   - `### Scoping heuristics`
   - `### Authoring-time anti-patterns`
   - `## Variants (stubs)`
   - `## Composition` (forward-reference only — for the Phase 5 audit
     surface; not design-time substrate)

Do not pre-load all variant overlays. The variant is selected in step 2;
load only the selected variant's overlay block at draft time.

### Step 2: Elicit designer intent (Decision sequence walk)

Walk agent.md §Construction Decision sequence step by step.

**Step 1 — Select the variant (GATES THE REST).** Apply the variant table
from agent.md verbatim:

| Authorial intent / consumer phrasing… | Variant | Why |
|---|---|---|
| "my `agent.md`," "the instructions I wrote for my agent," "my system prompt for the agent" | **A — Prompt-based** | The agent's behavior is carried by an authored spec the harness loads. |
| "my custom Claude Code agent," "my Cursor agent with these hooks," "my MCP-tool-enabled agent" | **B — Harness-based** | The agent's behavior is meaningfully carried by harness configuration (tools, hooks, permissions). |
| "my background agent," "my long-running agent," "my agent that does things without me watching" | **C — Autonomous-vs-supervised** | The agent's autonomy envelope matters — HITL gating, escalation, trust promotion are load-bearing. |

If intent matches more than one variant (B + C is most common), apply BOTH
overlays — the gates from each are non-substitutable. Do not pick "dominant
variant" per agent.md §Scoping heuristics §"Variant overlap resolution".

If `--variant` was supplied AND intent suggests a different variant,
surface the disagreement in the report (Phase 3 risk) but honor the flag —
designer override wins.

**Step 2 — State identity, intent, bounded class of tasks.** All variants.
Anchors every downstream constraint. (Loads G1 + G10 §Contract at audit.)

**Step 3 — Specify context structure.** All variants. Session-boot context
vs. on-demand context. For multi-session or long-context agents, also
specify defense against context degradation (G2b).

**Step 4 — Specify architecture.** Single agent vs. delegating to sub-agents.
If delegating, name the boundary and the coordination contract per
§Scoping heuristics §"Multi-agent decomposition without a coordination
contract". A multi-agent topology without a coordination contract is one
agent with extra startup cost — collapse or specify the contract.

**Step 5 — Enumerate harness surface — Variant B (and B+C).** Tools, hooks,
permission tiers, MCP servers, session-state mechanisms. SKIP for pure
Variant A unless the authoring intent surfaces tool/permission directives
(in which case promote to Variant B per agent.md §Authoring-time anti-
patterns §"Variant silently drifting").

**Step 6 — Specify workflow and termination — Variants B, C.** Durable
workflow state, termination conditions, recovery on error.

**Step 7 — Size the autonomy envelope — Variant C (HARD GATE); HITL-gated
Variant B.** Trust-promotion thresholds, HITL gates, escalation paths,
governance-audit cadence. The Autonomy Table lives here. Destructive-action
paths fire G9.I6 unconditionally — treat as hard gate analogous to skill
safety-critical classification. Variant C cannot proceed to step 8 without
a concrete sized envelope.

**Step 8 — Specify session persistence — Variant C, or any agent spanning
sessions.** Handoff protocol, memory mechanism, what persists vs. what's
re-derived.

**Step 9 — Specify recovery.** All variants. Inconsistent state, tool
failure, context corruption.

**Step 10 — Cross-check against §Composition.** Confirm the variant's
composed guide set matches the authored surface. Variant A that embeds tool
directives has silently become Variant B; an agent spanning sessions without
persistence treatment fails G7 at audit. Mismatches → Phase 3 risk.

Phase 2 produces the **Decision record**: one row per step, including
variant selection rationale, overlap flags, and any scoping decisions made.

### Step 3: Surface authoring-time risks

Compare the Decision record against agent.md §Authoring-time anti-patterns
(six listed: variant silently drifting; skipping autonomy-envelope sizing on
Variant C; borrowing identity from the harness; composing every guide "just
in case"; multi-agent decomposition without a coordination contract; re-
stating constitution invariants in every skill).

For each anti-pattern the in-progress posture could fall into, name it and
the mitigation in the draft. Forward-looking warnings only — not findings.

If `--variant` and intent disagreed in step 2, this is the place to surface
the mismatch as a documented Phase 3 risk (variant-drift candidate).

### Step 4: Draft the artifact

Apply agent.md §Template skeleton — common core for every agent, plus the
declared variant's overlay(s). The common core requires:

```markdown
---
title: "<Agent Name>"
type: "agent"
target_system:
  - "<system>"
created: "<date>"
updated: "<date>"
---

# <Agent Name>

## Constitution

### Core Truths
<3–6 bullets. The agent's anchoring beliefs.>

### Boundaries
<NEVER / MAY rules. Explicit out-of-bounds.>

### Vibe
<How the agent communicates. Concision, tone, action bias.>

### Continuity
<Session boot, memory model, state persistence.>

## Disposition

### When Active
### Cognitive Approach

## Scope

### In Scope
### Out of Scope

## Autonomy Table

| Action | Tier | Notes |
|---|---|---|
| <action> | <Full Autonomy / Guarded / Proposal-First / Human-Required> | <notes> |

## Skill Inventory

<Per-skill row: name, purpose, status.>

## Communication

### Input Artifacts Consumed
### Output Artifacts Produced
### Relationship to Other Agents

## Contract

### Preconditions
### Invariants
### Recovery
### Governance
```

Apply overlays per declared variant:

**Variant B overlay (additions):**
- Constitution → add a **Harness surface** subsection: tools, hooks,
  permission tiers, MCP servers.
- Communication → "Input Artifacts Consumed" must include the tool registry
  / hook definitions / harness config.
- Contract → Invariants reference G5/G6 invariants explicitly.

**Variant C overlay (additions):**
- Constitution → expand **Continuity** to cover handoff protocol and
  persistence mechanism in concrete terms (which file, which channel).
- Insert an **Autonomy Envelope** section between Scope and Autonomy Table:
  HITL gates, escalation thresholds, trust-promotion criteria.
- Contract → Invariants reference G7 + G9 invariants. G9.I6 fires for any
  destructive-action path.

For B+C overlap, apply both overlays — gates are non-substitutable.

The draft must be complete: frontmatter populated, common-core sections
present, declared variant's overlay sections present, no `<placeholder>`
text remaining for required fields.

Do not write to a file at this phase. Inline presentation only.

### Step 5: Delegate audit (rule 10 — non-negotiable)

Invoke `/assess-agent` as a separate subagent in fresh context. Use the
`Agent` tool with `subagent_type: general-purpose` and a self-contained
prompt that:

1. Names the draft (inline text OR a temp path written to
   `/tmp/design-agent-draft-<timestamp>.md` for the subagent to read — the
   temp file is for audit input, not a deployment).
2. Passes the variant selection so `/assess-agent` composes the correct
   guide set (Variant A → {G1, G2a, G2b, G3, G10}; Variant B → adds {G3b,
   G5, G6}; Variant C → adds {G7, G9}; overlaps → union).
3. Instructs the subagent to invoke `/assess-agent --variant <selected>`
   against the draft and return the full audit report.

Do not inspect the draft against G1/G2a/G2b/G3/G3b/G5/G6/G7/G9/G10 invariants
inside this skill's context. The fresh-context subagent invocation preserves
the epistemic gap rule 10 protects.

Collect the assess-* report.

### Step 6: Assemble report

Produce the design report per `design.md` §"Output shape". Include all
four deliverables: Decision record, Authoring-time risk surface, Draft
artifact, Audit findings (embedded /assess-agent output).

If `--target-path` was supplied AND the audit findings do not include any
HARD-blocking issues (Missing on G1.I1 Contract presence; Violated on G9.I6
for any destructive-action path; missing autonomy envelope on Variant C),
present the write option: "Approve writing the draft to `<target-path>`?
(y/N)". Write only on explicit `y`. Default is inline-only.

If `--target-path` was supplied AND the audit findings include HARD-blocking
issues, do NOT offer the write. State why and which step of the Decision
record to revise.

## Output Shape

Per `design.md` §"Output shape":

```
## Design — agent

**Artifact:** <intended path or summary>
**Concept:** agent.md
**Variant:** <A / B / C / A+B / A+C / B+C / A+B+C>

### Decision record (Phase 2)

| Step | Decision | Source / scoping note |
|---|---|---|
| 1 — Variant selection | <variant>; rationale: <intent quote / flag> | GATES THE REST |
| 2 — Identity, intent, bounded task class | … | … |
| 3 — Context structure | … | … |
| 4 — Architecture (single vs multi-agent) | … | … |
| 5 — Harness surface (Variant B/B+C) | … or N/A | … |
| 6 — Workflow + termination (Variant B/C) | … or N/A | … |
| 7 — Autonomy envelope (Variant C) | … or N/A | HARD GATE for Variant C |
| 8 — Session persistence (Variant C / multi-session) | … or N/A | … |
| 9 — Recovery | … | … |
| 10 — Composition cross-check | … | … |

### Authoring-time risks surfaced (Phase 3)

| # | Risk (from agent.md §Authoring-time anti-patterns) | Why it applies here | Mitigation in draft |
|---|---|---|---|
| 1 | … | … | … |

### Draft artifact (Phase 4)

<full agent.md draft, inline; common core + declared variant overlays>

### Audit findings (Phase 5 — delegated to /assess-agent)

<embedded /assess-agent report: Findings table, Follow-ups table, Aspects-out-of-scope table, Summary>

### Summary

<1–3 sentences: variant choice rationale, what the draft does well, what risks remain, what the audit flagged, what the designer should decide next. If destructive-action path is in scope, lead with the G9.I6 outcome.>
```

## Boundaries

- **Read-only on the KB and on concept docs.** This skill never modifies
  `agent.md`, `design.md`, IL guides, findings, or sources. Substrate gaps
  surface as Librarian gap reports in the Summary; do not patch the
  substrate.
- **No deploy.** Default is inline. Writing to `--target-path` requires
  explicit per-invocation approval AND clean audit findings on hard gates.
- **No self-assessment (rule 10).** Phase 5 delegates to `/assess-agent` in
  fresh subagent context. The skill must not internally inspect the draft
  against G1/G2a/G2b/G3/G3b/G5/G6/G7/G9/G10 — that is the assessor's
  epistemic role.
- **Variant selection is not optional.** If intent is ambiguous and
  `--variant` was not supplied, ask one disambiguating question before
  proceeding to step 2.
- **Partial drafts >500 lines.** Request scoping clarification before
  proceeding.
- **If the artifact isn't an agent.** If the designer's intent describes a
  SKILL.md (single bounded operation, allowed-tools, procedure body),
  redirect to `/design-skill`. If it describes a harness configuration (not
  an agent spec), state that harness design has no dedicated skill yet —
  `harness.md` concept doc has §Composition only; §Construction is debt
  flagged session 109.

## Boundary-Case Encounter Logging

On any deviation from the Tier-1 happy path (the 13-type encounter
taxonomy — missing concept/operation, ambiguous verb/variant, cross-concept,
verb-noun-mismatch, oversized-artifact, hop-ceiling-hit, tier-3-read,
low-confidence, kb-gap, redirect, clarification-asked), append a structured
record to `operations/system-log/session-<N>-librarian-encounters.md` per
the entry schema. Create the file on the session's first encounter; append
thereafter. `<N>` matches the session's SL entry number (infer from most
recent `session-<N>-*.md` in the folder).

Ambiguous-variant cases (step 1 disambiguating-question fires) are an
expected encounter type in `/design-agent` — log them so the variant-routing
hit rate becomes observable over time.

- Schema, controlled vocabulary, per-encounter body shape, feedback routing:
  `systems/improvement-loop/project-management/design-notes/2026-04-22-librarian-boundary-case-tracking.md`
- Write scope is narrowed to `operations/system-log/` only.

## Cross-References

- Operation file: `systems/improvement-loop/operations/references/librarian/design.md`
- Concept file: `systems/improvement-loop/operations/references/librarian/agent.md`
- Symmetric audit skill: `systems/improvement-loop/.claude/skills/assess-agent/SKILL.md`
- Sibling design skill: `systems/improvement-loop/.claude/skills/design-skill/SKILL.md`
- Read-contract: `systems/improvement-loop/project-management/design-notes/2026-04-21-librarian-read-contract.md`
- Boundary-case tracking: `systems/improvement-loop/project-management/design-notes/2026-04-22-librarian-boundary-case-tracking.md`
- Librarian agent definition: `systems/improvement-loop/agents/librarian/agent.md`
- Governing rules: IL `agent-rules.md` rule 10 (generator-assessor separation), rule 11 (abstractions must earn their keep), rule 12 (audit/design symmetry)
- Governing DDs: DD-78, DD-82, DD-89, DD-92
