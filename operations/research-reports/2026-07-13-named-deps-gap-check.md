---
title: "Named-Deps Gap-Check — direction-note asks vs research KB — 2026-07-13"
type: "research-report"
category: "operations"
target_system:
  - "improvement-loop"
created: "2026-07-13"
author: "owner-subagent"
tags:
  - "gap-check"
  - "restructure-program"
  - "phase-1"
  - "agentic-os"
  - "task-queue"
notes: |-
  Phase 1 Definition-of-Done item (restructure program §Phase 1 item 3): verify the
  research KB grounds every ask the agentic-OS direction note attaches to its named
  external dependencies (BMAD, superpowers, Archon, Nate B Jones), plus other named
  references. Also collects dep material for the deferred DD/IB task-queue study
  (memory-system design note §6). Read-only verification; no KB writes.
---

# Named-Deps Gap-Check — 2026-07-13

**What this is, in plain English.** The 2026-06-22 agentic-OS direction note said:
before committing any of this architecture, go learn from four named outside sources.
This report checks, dependency by dependency, whether the research KB now actually
contains what the note asked for — so Nick can close Phase 1's "named-deps gap-check
verified" box (or see exactly what's missing) without re-reading any of the deps.

**Sources of the asks:** `project-management/design-notes/2026-06-22-agentic-os-direction.md`
(§Research dependencies, §Sharpening from the Databricks comparison) and
`operations/plans/2026-07-12-engine-restructure-program.md` (§Phase 1 item 3).

## Verdict tally

| Dep | Asks | Grounded | Partial | Gap |
|---|---|---|---|---|
| BMAD | 2 | 1 | 1 | 0 |
| superpowers (+ "attachés") | 2 | 1 | 0 | 1 |
| Archon | 1 | 1 | 0 | 0 |
| Nate B Jones | 1 | 1 | 0 | 0 |
| Other named refs (#8 repo, Databricks) | 2 | 2 | 0 | 0 |
| **Total** | **8** | **6** | **1** | **1** |

Neither the PARTIAL nor the GAP blocks the DoD — see Closing verdict.

---

## 1. BMAD

### Ask A — "BMAD high-level skills" (§Research dependencies)

The note wants the KB to capture how BMAD packages its top-of-SDLC capability as
skills, so the engine can learn the form.

**Verdict: GROUNDED.** Plain English: we have a full structural teardown of BMAD's
skill system plus a dozen promoted findings on exactly the mechanics that make its
high-level skills work.

- `watched-libraries/analysis/bmad-method-analysis.md` (v6.2.2, all 5 dimensions) —
  maps the 41 skills including the 2-plan-workflows set (PM, UX designer,
  create/edit/validate PRD) and 3-solutioning set (architect, create-architecture,
  create-epics, check-readiness, gen-project-context).
- Findings: `bmad-method-v6-multi-agent-sdlc.md`, `everything-as-skill-architecture.md`
  (agents are skills with personas), `skills-as-markdown-sop-files-encode-processes.md`,
  `bmad-outcome-based-skill-rewrite-pattern.md`, `bmad-deterministic-skill-validator.md`,
  `step-file-micro-architecture.md`, `yaml-templates-with-embedded-elicitation-instructions.md`,
  `bmad-dependency-graph-module-ordering.md`, `business-analyst-upstream-quality-gate.md`,
  `scrum-master-story-contextualization.md`.

### Ask B — "critical-thinking skills for generating high-level agentic-system *governance* and *product* layers (PRD, architecture); may need modification to fit our needs"

**Verdict: PARTIAL.** Plain English: the *product*-layer half (how BMAD generates PRDs
and architecture docs, and the critical-thinking mechanics under it) is well grounded.
The *governance*-layer half (generating vision/mission/values/principles) is not — and
that is a gap in BMAD itself, not in our coverage of BMAD: BMAD's pipeline starts at
analysis/PRD and has no constitution-generation stage.

- Covered: the 4-phase Analysis→Planning→Solutioning flow with human gates
  (bmad-method-analysis.md §3), elicitation-driven document generation
  (`yaml-templates-with-embedded-elicitation-instructions.md`,
  `yaml-template-dual-structure.md`), and the critical-thinking mechanics
  (`thinking-partner-philosophy.md`, `anti-bias-protocol-for-llm-ideation.md`,
  `brainstorming-as-mandatory-design-gate.md`).
- Missing: no external material on generating the governance layer above the PRD. The
  note itself anticipated this ("may need modification to fit our needs").
- **Cheapest closing move:** none needed from BMAD — the CareerBuddy
  `ops-vision-to-plan` import (Phase 4, already locked in the program plan §4) is the
  structured-interviewing engine for exactly the constitution/PRD layer; the direction
  note's governance-first creation model extends it downward. If Nick wants external
  corroboration for constitution-generation specifically, a scoped `/research-query`
  is the tool; nothing in BMAD to fetch.

### Staleness note (no fetch performed)

Registry `watched-libraries/bmad-method.md`: last evaluated **v6.2.2 on 2026-04-07**
(~3 months). The wave-3 `/watch-upstream` pass (2026-07-13) was scoped to Archon + n8n
only, so BMAD had no refresh. BMAD is a high-velocity project; a cheap `/watch-upstream`
check is advisable before Phase 4/5 consumes the material, but the asks above are about
its *pattern shapes*, which do not churn at patch cadence.

---

## 2. superpowers (obra/superpowers)

### Ask — "possibly augmented with superpowers" (augmenting BMAD's high-level / critical-thinking skill set)

**Verdict: GROUNDED.** Plain English: the KB documents exactly the superpowers pieces
that would augment BMAD — and the analysis explicitly tags the piece Nick flagged.

- `watched-libraries/analysis/superpowers-analysis.md` (v5.0.7, all dimensions) —
  its findings-candidate #4 states outright: brainstorming as a mandatory
  design-first `<HARD-GATE>` "is the thinking/critical-thinking skill Nick flagged."
- Findings: `brainstorming-as-mandatory-design-gate.md`,
  `superpowers-plugin-spec-driven-sub-agent-orchestra.md`,
  `persuasion-engineered-skill-design.md`,
  `framework-tension-taxonomy-superpowers-gsd-gstack.md` (who thinks / stabilizes /
  executes — the augmentation-fit question answered directly).

### Ask — "and attachés"

**Verdict: GAP (ambiguous term).** Plain English: the word "attachés" appears nowhere
in the KB, the registries, or any analysis — only in the direction note itself. The
note is a transcribed brain-dump that already flags one garbled fragment ("Division,
to a degree"); "attachés" is likely a second transcription artifact, or a niche
artifact name we never captured.

- **Cheapest closing move:** a one-line clarification from Nick (this is a Phase 4
  interview question, same bucket as the "Division" fragment). Only if it names a real
  library/framework does a `/research-query` or registry add follow. Do not research
  a word we can't confirm is a thing.

### Staleness note (no fetch performed)

Registry `watched-libraries/superpowers.md`: last evaluated **v5.0.7 on 2026-04-07**
(~3 months); no wave-3 refresh scoped. obra iterates quickly; same advisory as BMAD —
cheap `/watch-upstream` before Phase 4/5 consumption, not blocking.

---

## 3. Archon

### Ask — "The agentic system should always have a workflow similar to Archon" (workflow shape)

**Verdict: GROUNDED — the freshest dep of the four.** Plain English: as of today the
KB holds a v0.5.0 re-analysis written *for this gap-check*, on top of promoted findings
from the v0.3.2 era. If the engine wants "a workflow similar to Archon," the KB can now
state precisely what that means, down to schema fields.

- `watched-libraries/analysis/archon-analysis.md` (v0.5.0, re-analyzed 2026-07-13) —
  opens with "What Archon Now Demonstrates That It Didn't at v0.3.2," written for the
  named-deps gap-check: first-class Ralph loop anatomy, the 20-workflow default
  library, tiered provider-capability registry, governance escalated to product
  identity, and the rules-layer-collapse counter-signal.
- `watched-libraries/archon.md` — registry refreshed to v0.5.0 today (wave-3 gate
  follow-up 2) with the full upstream delta.
- Promoted findings already in the KB: `durable-workflow-engine-for-agent-systems.md`,
  `dag-vs-bsp-two-graph-based-orchestration-models.md`,
  `archon-yaml-defined-harness-workflows.md`, `intent-based-meta-routing-skill.md`,
  `isolation-resolver-worktree-lifecycle-algorithm.md`,
  `hook-based-enforcement-for-agent-outputs.md`,
  `meta-workflow-builder-self-extending-harness.md`.
- **Residual (mechanical, non-blocking):** the v0.5.0 analysis lists 10 new findings
  candidates not yet promoted; promotion is a separate gated `/promote-findings` step.
  The ask is grounded by the analysis + registry regardless.

---

## 4. Nate B Jones

### Ask — "'open skills framework' (newly released) — introduces the same abstraction we'd be learning from"

**Verdict: GROUNDED (by decomposition, with a recorded triage decision).** Plain
English: the KB covers every constituent idea of Jones's framework — skill anatomy,
portability, delegation contracts, skill self-improvement — and the wave-3 triage
*explicitly examined* his "Open Skills" launch video and rejected it as adding nothing
new: "'Open Skills' launch promo; concepts all in KB and engine substrate"
(`operations/research-reports/2026-07-12-link-intake-triage.md`, video 9PUaEj0pMYE).
That rejection is itself the grounding verdict: the abstraction was checked against
the KB and found already present.

- Authority corpus: `research-authorities/nate-b-jones.md` — 20 sources, with a
  2026-07-13 specialty note naming harness maintenance + delegation loops his
  strongest lane.
- Today's three Pass 2 legs (all fully extracted from local transcripts, 2026-07-13):
  - **Eval-ceiling leg** — `research-sources/1-6m-agents-registered-for-openclaw-and-did-nothing.md`
    → `repeated-sampling-scaling-law-and-verifier-ceiling.md`,
    `four-estimate-agent-routing-test.md`,
    `two-constraint-decomposition-memory-vs-eval.md`, + extended
    `model-tier-routing-expensive-orchestrator-cheap-s.md`.
  - **Delegation-contract leg** — `research-sources/codex-your-first-personal-ai-agent-delegation-loop.md`
    → `chief-of-staff-home-base-thread.md`,
    `planning-thread-vs-execution-thread-subagent-fleets.md`,
    `token-burn-telemetry-as-delegation-metric.md`, + extended
    `work-ticket-contract-prompt-mode-vs-work-mode.md` and
    `skill-self-improvement-three-approaches.md`.
  - **Harness-fitness leg** — `research-sources/dont-build-more-ai-agents-until-you-watch-this.md`
    → `bidirectional-agent-breakage-world-drift-model-improvement.md`,
    `tool-pruning-as-harness-maintenance.md`, `five-point-agent-health-checklist.md`,
    `harness-depth-as-maintenance-ownership.md`, `build-from-observed-workflow.md`,
    + extended `frontier-model-as-harness-designer.md`.
- Skill-abstraction coverage the framework maps onto:
  `skills-as-open-portable-standard.md` (agentskills.io open standard),
  `skill-anatomy-convergence-20-of-29-repos.md`,
  `nine-primitive-document-agent-skeleton.md` (notes his "two open skills" published
  on Substack), `harness-non-portability-across-model-families.md`.
- **Residual (only if Nick overrides the triage call):** no single KB source documents
  the Open Skills framework *as a spec document*. Cheapest move if wanted: fetch the
  Substack framework post via `/research-query` — one source, one pass.

---

## 5. Other named external references in the direction note

### "#8 taxonomy/clustering repo" ([NEED REPO NAME from Nick])

**Verdict: GROUNDED — resolved.** Nick supplied the name; it was the private
enterprise context-hub, intaken session 143 (HISTORY.md): anonymized primaries at
`research-sources/raw/context-hub/`, key yield = the asset-catalog form answer
(directory + registry + generated views as one generation pipeline, not a choice) —
which answers the direction note's open assets-catalog question directly.

### Databricks / Agent Bricks / Omnigent ("zero KB coverage as of this note")

**Verdict: GROUNDED.** The note's flag is discharged: `watched-libraries/omnigent.md`
(2026-07-11; Databricks provenance confirmed via NOTICE) + the 52k
`watched-libraries/analysis/omnigent-analysis.md` (2026-07-12) — the registry entry
says explicitly "Resolves the design note's 'Databricks has zero KB coverage' flag."
The proprietary Agent Bricks web sources listed in the note were superseded by the
open-source Omnigent repo, which is the better study object for the same architecture
(meta-harness above harnesses, access governance without a constitution layer — the
exact gap the engine's model occupies). No further intake needed.

### Deps named with no asks attached

The note names Letta/mem0 and GSD/Agent Bricks comparatively (in the
unit-of-governance table) without attaching research asks; per the brief, no asks are
invented for them. All four are watched libraries with analyses regardless.

---

## 6. Task-queue study feedstock (memory-system design note §6)

The deferred DD/IB task-queue study ("cruft audit + DD↔IB coupling map +
queue-structure study — converge with the wave-3 named-deps gap-check") shares this
reading list. Collected here, no design work done:

**Archon — loop/queue semantics (freshest, richest):**
- Loop-node anatomy as a complete queue-iteration contract: `until` signal +
  `until_bash` deterministic check + `max_iterations` budget + `fresh_context` +
  per-iteration human gates (`interactive`/`gate_message`) + `$LOOP_PREV_OUTPUT`
  bridging + pause/resume persisting the iteration counter (archon-analysis.md §3).
- Ralph-as-DAG: PRD → `prd.json` → fresh-context loop implementing **one story per
  iteration** — the story file is the queue item; the PRD is the queue.
- Typed output sidecars (`output_type` → `$ARTIFACTS_DIR/nodes/<id>.md` +
  `.meta.json`): downstream steps find work products by declared type, not filename
  convention — a queue-handoff contract.
- `persist_session` keyed `(workflow, node, scope, provider)`: cross-run memory as an
  engine feature; resume skips completed nodes.
- Approval nodes with `capture_response` (human verdict becomes queue data) and the
  no-autonomous-lifecycle-mutation principle (never mark ambiguous work failed on a
  staleness heuristic — directly relevant to stale-IB handling).

**BMAD — project/queue structure:**
- Epics→stories decomposition with story files as sharded, self-contained work units:
  `document-sharding-for-context-efficiency.md`,
  `scrum-master-story-contextualization.md` (a dedicated role whose whole job is
  packaging the next queue item's context).
- `step-file-micro-architecture.md` — numbered step files, forward-loading forbidden:
  queue discipline expressed as context rules.
- Dependency-ordered execution: `bmad-dependency-graph-module-ordering.md`,
  `governed-dependency-chain-build-order.md` — the DD↔IB coupling-map analog.
- 4-phase pipeline with per-phase human validation gates (bmad-method-analysis.md §3).

**superpowers / GSD — task queues:**
- `phase-queue-state-file-as-orchestrator-memory.md` — the queue lives in a state
  file, not in the orchestrator's context.
- GSD (gsd-analysis.md): `STATE.md` tracks current phase/status/last-operation; every
  transition reads/writes it; artifact-based handoff (CONTEXT→RESEARCH→PLAN→SUMMARY→
  VERIFICATION) — each queue stage produces the next stage's input document.
- `framework-tension-taxonomy-superpowers-gsd-gstack.md` — who owns sequencing when
  frameworks compose.

**Jones — delegation contracts (the queue-item schema):**
- Five-element assignment contract (goal, sources, standard, permission boundary,
  proof of done) — `work-ticket-contract-prompt-mode-vs-work-mode.md`. This is the
  strongest external candidate for what a well-formed IB item should carry.
- `chief-of-staff-home-base-thread.md` — one persistent thread owns the queue and
  routes sub-jobs (eliminates human-as-router).
- `planning-thread-vs-execution-thread-subagent-fleets.md` — queue planning and queue
  execution get separate contexts and separate fleets.
- `four-estimate-agent-routing-test.md` + `two-constraint-decomposition-memory-vs-eval.md`
  — when to split a task at all (split for memory vs split for eval), the intake-side
  question of queue design.

---

## 7. Closing verdict

**Phase 1's "named-deps gap-check verified" DoD is satisfiable now.** All four named
dependencies are grounded for the asks the direction note actually attaches to them;
the two non-GROUNDED verdicts do not block:

1. **BMAD Ask B (PARTIAL)** — the ungrounded half (governance-layer generation) is
   absent from BMAD itself; the engine's plan already covers it via the CareerBuddy
   `ops-vision-to-plan` Phase 4 import. Nothing to fetch.
2. **"attachés" (GAP)** — an unconfirmable term from a transcribed note; resolution is
   a one-line Nick clarification (Phase 4 interview bucket, alongside the "Division, to
   a degree" fragment), not research.

Non-blocking residuals to carry:
- Promote the 10 Archon v0.5.0 findings candidates (`/promote-findings`, gated).
- BMAD + superpowers registries are ~3 months stale (2026-04-07); cheap
  `/watch-upstream` pass before Phase 4/5 consumes them.
- Optional: fetch Jones's Open Skills Substack post only if Nick overrides the wave-3
  triage's "concepts all in KB" rejection.

Remaining Phase 1 DoD item after this check: the **delta report** → plan checkpoint #1.
