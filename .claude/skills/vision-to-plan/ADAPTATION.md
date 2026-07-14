# Engine adaptation — vision-to-plan in MetaSystem

> **Downstream copy.** Upstream source: `nickgogan/CareerBuddy`
> `.github/skills/ops-vision-to-plan` @ **0.3.0** per its CHANGELOG (imported
> 2026-07-13, session 147, restructure-program Phase 4). Verdict locked in the program
> plan §4 (`Import + adapt`, Phase 4). Unlike `meta-skill-author` (imported intact), this
> is a **heavier adapt**: the design note
> `project-management/design-notes/2026-07-13-phase4-interview-structure.md` IS the
> adaptation spec for the templates and block ordering. Re-derive check: diff SKILL.md
> and `references/` against upstream `ops-vision-to-plan` before adopting upstream
> releases; `ports/generic.md` is the harness-neutral canon carried for that diff.

## What was changed at import (complete list)

1. **Renamed** `ops-vision-to-plan` → `vision-to-plan` (engine drops the `ops-` prefix,
   matching `/session-handoff`; also matches the upstream generic port's name).
2. **Artifact chain reordered** from upstream `brief → PRD → architecture → epics` to the
   engine's governance-first kernel set: **confirmation summary → constitution → PRD →
   actors → ordering decision → plan update**. Rationale (design note §2): the engine's
   direction note puts the constitution above the PRD, and the architecture doc's role is
   played by the kernel's "how it works" + actors layers.
3. **`references/brief-template.md` dropped** — no standalone brief. Its content
   (problem, who, outcome, constraints, out-of-scope, bet size) is already answered by
   the plan §1–2 and CHARTER.md, so the workflow opens with a **pre-filled confirmation
   summary** drafted from the corpus and corrected by the human (reduce-Nick-bottleneck
   posture). Upstream brief-template retained only via `ports/generic.md` for diff.
4. **`references/architecture-template.md` replaced by `references/actors-template.md`** —
   the engine kernel expresses architecture as actors + a "how it works" layer, not a
   standalone architecture doc. The new template leads with the actor-model decision
   (one implicit agent / N actors / one agent with N dispositions) and names the human's
   seat (human/AI seam, wave-3 ruling).
5. **`references/constitution-template.md` added (net-new)** — engine-original; no
   external exemplar generates the layer above the PRD (Phase 1 delta report, insight
   #2). Leads with the Charter-relationship decision.
6. **`references/prd-template.md` adapted** — Users section seeds the five locked engine
   archetypes; Epics section carries the checkpoint-#1 named inputs
   (capability-as-composition-unit; harness maintenance/fitness DoD); Non-goals probes
   the engine's named candidates. Structure otherwise upstream-diffable.
7. **Outputs relocated to `governance/`** as kernel content (`governance/constitution.md`
   or a CHARTER amendment set, `governance/prd.md`, `governance/actors.md`) — the kernel
   litmus (a downstream consumer would pull all three). Upstream wrote to repo root.
8. **Evidence/grounding sources rebound** to engine substrate (CHARTER.md, FOUNDATIONS.md,
   DD/IB registry, `agents/`) and supersession bound to DD-44.
9. `metadata.upstream` + `metadata.imported` provenance fields added; `version` set to
   `0.3.0-il.1`. This file.
10. **`distribution-scope` set `exportable` → `internal`** (Rule-10 finding #5). Upstream's
    "exportable" requires zero workspace-specific content in the body; this engine copy is
    saturated with engine bindings. `ports/generic.md` is the maintained exportable canon
    (its own `port-stage` metadata confirms), recorded now in a `metadata.exportable-canon`
    field. This dissolves the "missing README" symptom — an internal engine skill needs no
    distribution README. `allowed-tools` also gained `Edit` (finding #4) to support
    section-scoped amendments in the re-entry posture without full-file rewrites.

`capability-contract.yaml`, `CHANGELOG.md`, `SOURCES.md`, and `evals/trigger-eval.md` are
carried **as-is from upstream** for re-derive/diff; they describe the upstream skill, not
this adaptation. The BMAD/Superpowers method debts in SOURCES.md still hold.

## Engine-context overlay (how this skill runs here)

- **Home & registration:** engine-scoped at
  `systems/improvement-loop/.claude/skills/` (DD-109). Registered in the engine CLAUDE.md
  Owner-skills listing (structured-interview capability crosses agents; owner-stewarded).
- **Capability mapping (contract → this harness):** human-approval-channel = Nick inline
  (required — the section gate is DD-29/human-gate aligned by construction);
  durable-document-store = Write tool into `governance/`; reference-bundle-attachment =
  L3 progressive disclosure of `references/`; versioned-checkpoints = git.
- **SKILL vs run-spec:** this SKILL is the **reusable capability**; a per-engagement
  design note is the **run parameters**. The Phase 4 interview structure note pre-orders
  the blocks (0/A/B/C/D/E) and pre-loads evidence — the SKILL follows it when present.
  Phase 5's kernel-compiler arc re-invokes this SKILL to produce the same three kernel
  docs for downstream produced systems (why it landed as a skill, not a one-shot —
  program plan §4; Rule-11 recurrence is satisfied by that re-invocation, not by the
  single Phase 4 run).
- **Governance tier:** kernel docs are governance artifacts; §Constraints "Governance
  discipline" maps to the engine's Nick-gate + workspace Process Rule 3 (no volatile
  metrics). Local commits at section approvals are fine; push is Nick-gated.

## Known overlap (flagged — not resolved here)

`vision-to-plan` (Socratic vision → kernel docs) is adjacent to `/design-agent` (drafts a
single agent artifact) and `/translate-governance` (charter → engine governance docs). No
merge implied: this skill elicits *net intent* section-by-section and produces the
constitution/PRD/actors *set*; `/design-agent` drafts one already-scoped actor;
`/translate-governance` mechanically derives governance from an *existing* charter without
elicitation. If a future run shows real duplication, flag for a Nick-gated consolidation
call — do not merge speculatively (rule 11).

## Rule-10 assess pass

`/assess-skill` ran in a separate Librarian context after landing (2026-07-13; program
plan §4: every import gets a Rule-10 assess pass). Classification: **safety-critical**
(Write + governance writes → G9.I6 fires). The load-bearing gate — G9.I6, destructive/
irreversible actions always require human approval — **passed unconditionally**. DD-92
ContextSpec N/A (no `context:` block). Finding dispositions:

- **#5 exportable→internal + missing README** (Medium-High) — **fixed**: scope set
  `internal`, `exportable-canon` field points at `ports/generic.md`; README moot. See
  import-delta item 10.
- **#4 Write-only tool surface vs amendment behavior** (Medium) — **fixed**: `Edit` added
  to `allowed-tools`.
- **#1 constraints not split by enforcement layer; section-gate is prompt-only** (Medium)
  — **fixed (form) + accepted (residual)**: `§Constraints` now split Hard/Steering with an
  explicit enforcement note. The prompt-only residual risk is *accepted* for this
  interactive-only skill (inert without an approval channel; workspace push-gate + Nick's
  presence are the standing mitigations) — same disposition as the `meta-skill-author`
  import's finding #3. Structural backstop deferred until/unless the skill runs less-attended.
- **#2 stop-rules lack a labeled completion criterion** (Medium) — **fixed**: `§Stop Rules`
  now points at `§Acceptance criteria` as its completion criterion.
- **#3 no durable state tracking across sittings** (Medium) — **fixed**: `§Workflow` gained
  a "Progress tracking (resume across sittings)" note — approved-section-in-file + run-spec
  block list is the checkpoint.
- **#6 multi-sentence description** (Low) — **accepted, no change**: folded-scalar
  descriptions are the upstream convention (same disposition as `meta-skill-author` #6);
  G8 content quality is strong (consumer-phrased triggers + explicit boundary).
- **upstream-diffable carryovers** (`capability-contract.yaml`, `evals/trigger-eval.md`,
  `SOURCES.md` still naming `ops-vision-to-plan` / upstream artifact set) — **accepted as
  flagged**: they describe the upstream skill for re-derive; SKILL.md never routes an
  executing agent to read them for behavior.

**Open follow-ups (process-verifiable, not blocking):**

- **(b) adapted-trigger eval gap** — `evals/trigger-eval.md` tests upstream phrasing, not
  the adapted engine triggers (constitution/actors vocabulary; `/design-skill`,
  `/meta-skill-author`, `/research-loop` boundaries). The deployed trigger surface is
  untested. **IB candidate** — close before heavy reuse (Phase 5), not before the single
  Phase 4 run driven directly from SKILL.md + run-spec.
- **(a) cost/turn budget** — no stall circuit-breaker on a long multi-session engagement;
  upstream-inheritable gap (same as `meta-skill-author` #7). Candidate upstream contribution.
- **(f) Rule-11 recurrence** — the reusable-skill justification rests on the Phase 5
  kernel-compiler re-invocation, which has not occurred yet. Forward-looking; revisit if
  Phase 5 changes the ordering such that this skill is never re-invoked.
- **(e) `bypassPermissions` confirmed in effect** for `Write` (agent memory
  `feedback_no_permission_prompts`) — so #1's residual is live, hence the explicit accept.
