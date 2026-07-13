---
title: "Phase 1 Research-Grounding Delta Report — plan checkpoint #1 input — 2026-07-13"
type: "research-report"
category: "operations"
target_system:
  - "improvement-loop"
created: "2026-07-13"
author: "researcher-owner-subagent"
tags:
  - "delta-report"
  - "restructure-program"
  - "phase-1"
  - "checkpoint-1"
  - "agentic-os"
notes: |-
  Final Phase 1 DoD artifact (restructure program §Phase 1): scorecard over the three
  plan items, thematic KB-gain summary organized around what Phases 2-5 consume, honest
  negative space, and the concrete plan-revision questions for checkpoint #1. Phase 1
  spanned sessions 139-144 (2026-07-12/13); link-intake waves 1-2 landed pre-phase in
  sessions 135-136. All counts measured on 2026-07-13; point-in-time by design.
---

# Phase 1 Research-Grounding Delta Report — 2026-07-13

**What this is, in plain English.** Phase 1's job was to ground the second-brain and
harness models in research *before* anything gets built. This report closes Phase 1: it
scores the three plan items, says what the KB actually gained (organized around what
Phases 2–5 will consume), says honestly what it did *not* find, and turns the evidence
into concrete questions for **plan checkpoint #1**. Nick can gate the checkpoint from
this report alone. Recommendations here are inputs, not decisions.

**Corpus point-in-time (measured today):** 934 findings, 247 sources.

---

## 1. Phase 1 scorecard

### Item 1 — Nick's YouTube links intake (LINKS.md → triage → extraction)

**DONE.** The full LINKS.md arc is closed and the queue is empty.

- Waves 1–2 (sessions 135–136, pre-phase): 83 videos triaged, 28 KB-ONLY extracted →
  65 findings + 24 updates (`2026-07-12-delta-report.md`); 20 videos blocked by a
  YouTube IP-level 429 rolled into wave 3.
- Wave 3 (sessions 142–144): all 28 unique videos (20 retries + 9 Nick-added, 1 dup)
  cached full-text via the kome.ai fallback lane after every direct route died under
  the IP block (session 143, HISTORY.md); triaged today — **0 ADD / 0 ENHANCE /
  10 KB-ONLY / 18 REJECT**, Nick accepted all verdicts same-session
  (`2026-07-13-link-intake-triage.md`, Gate outcome); Pass 2 extracted all 10 —
  **9 new sources, 27 new findings, 13 finding extensions, 1 new + 4 updated
  authorities** (commit `401b836`), plus the n8n changelog note routed through
  `/watch-upstream` per the gate ruling.
- **Residual (small):** the per-channel triage-priority notes from triage follow-up 5
  (Chase AI, Nate Herk, Austin Marchese) are not yet written into their authority
  entries — only the Jones/Simmons/Scrapes/builder-io/Medin updates landed. One short
  authority-hygiene pass.

### Item 2 — CareerBuddy as a primary source

**DONE** (session 139, five parallel Researcher passes; HISTORY.md).

- 5 source entries covering everything the plan enumerated: wiring canon
  (`careerbuddy-wiring-canon.md`), meta-skill-author references
  (`careerbuddy-meta-skill-author-references.md`), the ops-self-improve store model
  (`careerbuddy-ops-self-improve.md`), the C1–C16 deterministic audit battery
  (`careerbuddy-ops-doc-sync-audit-battery.md`), and the 5 queued corpus contributions
  (`careerbuddy-improve-backlog-corpus-contributions.md` — invariant column,
  receiver-relative tiers, card-over-manifest fusion, Pi trust-gate trio,
  prose-guard→policy-engine degradation, each now a named finding).
- 35 findings written in that session; dedup treated shared mechanics as production
  validation (both systems drew on this KB), extending rather than duplicating.
- Already consumed downstream: the session-142 memory-system design (IB-176) lifted
  the ops-self-improve store/promotion model directly — the intake has paid for
  itself once already.

### Item 3 — Named research dependencies (BMAD, superpowers, Archon, Jones, #8 repo)

**DONE, with two recorded non-blockers** (`2026-07-13-named-deps-gap-check.md`).

- Verdict tally over the direction note's 8 asks: **6 GROUNDED / 1 PARTIAL / 1 GAP**;
  the gap-check's closing verdict: the DoD is satisfiable now.
- The PARTIAL (BMAD's governance-layer generation) is a gap in BMAD itself, not in our
  coverage — the plan already covers it via the Phase 4 `ops-vision-to-plan` import.
- The GAP ("attachés") is an unconfirmable transcription artifact — resolution is a
  one-line Nick clarification in the Phase 4 interview, not research.
- Archon is the freshest dep: re-analyzed today at v0.5.0 for this gap-check
  (`watched-libraries/analysis/archon-analysis.md`), registry refreshed
  (`2026-07-13-watch-upstream-triage.md`). The #8 repo resolved to the enterprise
  context-hub, intaken session 139 (`research-sources/hub-and-spoke-context-hub.md`,
  primaries anonymized at `research-sources/raw/context-hub/`).
- **Residuals:** 10 Archon v0.5.0 findings candidates awaiting a gated
  `/promote-findings` run; BMAD + superpowers registries ~3 months stale (last
  evaluated 2026-04-07) — cheap `/watch-upstream` advisable before Phase 4/5 consumes
  them.

**Bottom line: all three items done; Phase 1's DoD is met with this report. Residuals
are hygiene-scale, none blocks checkpoint #1.**

---

## 2. What the KB gained, thematically

Organized by what Phases 2–5 actually need. "Load-bearing" = the engine would design
differently without it; "corroboration" = confirms a direction already ruled.

### (a) Harness-layer grounding (→ Phase 5)

The corpus can now describe a formal harness layer in someone else's production terms,
not just our own intentions:

- **Capability primitives — load-bearing.** Pydantic AI 2.0 ships a "capability"
  primitive (instructions + tools + lifecycle hooks + guardrails + model settings in
  one shareable unit, "the layer above MCP") and splits into a lean core vs a named
  harness lane — the industry converging on the engine's own vocabulary
  (`capability-as-agent-composition-primitive.md`,
  `lean-core-vs-harness-two-lane-framework-layering.md`).
- **A working harness exemplar at depth — load-bearing.** Archon v0.5.0
  (archon-analysis.md §"What Archon Now Demonstrates"): first-class Ralph-loop anatomy
  (`until`/`until_bash`/`max_iterations`/`fresh_context`/per-iteration gates), a
  **tiered, not boolean** provider-capability registry the engine branches on,
  governance escalated to product identity — and a **counter-signal**: Archon deleted
  its 11-file rules layer and consolidated into one 979-line CLAUDE.md (with observable
  drift against its AGENTS.md mirror). Both signals matter for Phase 5's layering
  decisions.
- **Loop engineering with numbers — load-bearing.** Stanford repeated-sampling data
  (15.9%→56% solve rate at 250 attempts; selection without a mechanical verifier stalls
  at ~100) plus Anthropic production data (token spend explains 80% of run-quality
  variance): **evals are the binding constraint on multi-agent scale**
  (`repeated-sampling-scaling-law-and-verifier-ceiling.md`).
- **Harness fitness and maintenance — load-bearing as a set.** The Jones
  harness-fitness leg: agents break bidirectionally (world drift AND model improvement
  — over-restriction traps better models), tool pruning as maintenance discipline
  (Vercel deleted 80% of tools, agent improved), harness depth = maintenance ownership,
  a five-point agent health checklist, build-from-observed-workflow
  (`bidirectional-agent-breakage-world-drift-model-improvement.md`,
  `tool-pruning-as-harness-maintenance.md`, `five-point-agent-health-checklist.md`,
  `harness-depth-as-maintenance-ownership.md`, `build-from-observed-workflow.md`).
  This says a Phase 5 harness is not ship-once — it needs a scheduled fitness loop,
  which the model-capability-registry refresh already half-embodies.
- **Reversibility as autonomy infrastructure** — Replit's three-layer reversible-state
  stack; reversible forks enable parallel sampling; capability-tax framing
  (`three-layer-reversible-state-single-undo-surface.md`,
  `reversible-forks-enable-parallel-sampling.md`,
  `capability-tax-permanent-operational-cost.md`). Secondhand teardown — medium
  evidence, verify against Replit primaries before leaning on it.
- Corroboration: the six-pattern harness-composition taxonomy (Strong, first-party,
  wave 2) and `harness-non-portability-across-model-families.md` remain the cluster
  anchors; nothing in wave 3 contradicted them.

### (b) Memory-system grounding (→ IB-176 build, Phase 2's successor work)

- **Point-for-point corroboration of the ruled design — corroboration with teeth.**
  A practitioner independently rebuilt Hermes-grade memory inside Claude Code as
  portable local markdown — the engine's exact stack — landing on post-turn hook
  capture, a size-capped curated snapshot separate from append-only transcripts, and
  gated promotion after Hermes' self-rewrite failure mode
  (`research-sources/rebuilt-hermes-memory-in-claude-code.md`,
  `memory-system-evaluation-triad-storage-injection-recall.md`,
  `memory-recall-ladder-staged-deepening-with-citation-and-abstention.md`).
- **Bootstrap validation — load-bearing for ship order.**
  `session-history-import-as-memory-bootstrap.md` independently validates the ruled
  SL distill-then-close plan (frozen System Log corpus as day-one memory feedstock).
- The CareerBuddy ops-self-improve intake (item 2) is the design's named source:
  `append-only-lesson-store-owning-surface-identity.md`,
  `recurrence-threshold-gates-autonomy-not-direction.md`,
  `per-proposal-human-gate-promotion-pipeline.md`,
  `deterministic-store-checker-runtime-threshold-flags.md`,
  `self-improvement-dispatch-table-route-never-reimplement.md`.
- Net: **no evidence surfaced that changes the IB-176 design; two sources de-risk it.**

### (c) Governance-as-portable-kernel grounding (→ Phases 4–5)

- **The wiring canon — load-bearing.** CareerBuddy's abstract-then-adapt doc structure,
  machine-readable system contract with wiring rows, manifest-hash drift detection,
  two-tree authoring-vs-generated model, superset-spec for cross-platform authoring,
  receiver-relative tier semantics, platform capability matrix with explicit unknowns
  (`wiring-canon-abstract-then-adapt-doc-structure.md`,
  `machine-readable-system-contract-with-wiring-rows.md`,
  `manifest-hash-drift-detection-for-derived-docs.md`,
  `two-tree-model-authoring-vs-canonical-generated-pack.md`,
  `superset-spec-for-cross-platform-skill-authoring.md`,
  `receiver-relative-tier-semantics.md`,
  `platform-capability-matrix-with-explicit-unknowns.md`). This is the concrete
  mechanics library for "kernel compiles to harness materializations."
- **The asset-catalog question answered — load-bearing.** The context-hub intake
  resolved the direction note's open question: directory + registry + generated views
  as **one generation pipeline**, not a choice among forms
  (`hub-and-spoke-context-hub.md`, `hub-and-spoke-two-tier-skill-taxonomy.md`).
- Convergence corroboration: Pydantic's capability unit is a portable
  composed-capability artifact in the same spirit; Archon's committed `direction.md`
  driving automated PR triage is governance-as-product-identity in the wild.

### (d) Delegation / agent-routing grounding (→ Phase 4 interview)

- **The Jones delegation legs — load-bearing for the interview.** Four-estimate agent
  routing test (size / independence / separation-of-concerns / checkability → chat /
  single agent / team / human); two-constraint decomposition theory (split for memory
  vs split for eval); chief-of-staff home-base thread (one persistent thread owns the
  queue, eliminating human-as-router); planning-thread vs execution-thread fleets;
  token-burn telemetry as delegation-adoption metric
  (`four-estimate-agent-routing-test.md`,
  `two-constraint-decomposition-memory-vs-eval.md`,
  `chief-of-staff-home-base-thread.md`,
  `planning-thread-vs-execution-thread-subagent-fleets.md`,
  `token-burn-telemetry-as-delegation-metric.md`).
- **Seam identification — Nick-upgraded at the gate.** The Zhao rubric was kept not as
  a workflow-selection checklist but as a **Librarian advisory capability**: helping an
  operator see which parts of a workflow belong to the *human*, not the AI system
  (`human-ai-seam-identification-three-question-rubric.md`; framing per the wave-3
  Gate outcome). Direct Phase 4 interview input.

### (e) Task-queue feedstock (→ deferred DD/IB task-queue study)

Collected, not designed: gap-check §6 assembles the full reading list — Archon's
loop-node-as-queue-iteration-contract and typed output sidecars, BMAD's epics→stories
sharding and dependency-ordered execution, superpowers/GSD state-file queues, and
Jones's five-element assignment contract as the strongest external candidate for what
a well-formed IB item should carry
(`work-ticket-contract-prompt-mode-vs-work-mode.md`). The study's planned convergence
point ("converge with the wave-3 named-deps gap-check") has now happened — it is
schedulable.

Also landed, cross-theme: the model-capability registry's GPT-5.6 line finally has KB
grounding (`gpt-56-soul-vs-fable-5-one-shot-head-to-head.md`, anecdotal/medium, n=1
per task) plus a portable rule — never trust harness cost readouts, use independent
log-based accounting (`harness-cost-readout-unreliability-independent-log-accounting.md`).
And the strongest input yet for IB-175 governance visualization:
`mdx-visual-plans-with-reusable-components.md`,
`plan-level-as-engineering-reasoning-abstraction.md`,
`visual-recap-post-execution-mirror-artifact.md` — a named answer to Nick's
"DDs are prose-heavy" complaint.

---

## 3. What Phase 1 did NOT find

Honest negative space, so checkpoint #1 doesn't over-credit the corpus:

1. **Multi-tenant agentic-system design is still thin.** The session-139 observation
   stands: single-operator exemplars dominate. Phase 1 added only datapoints —
   CareerBuddy's users-as-data answer (`skills-generic-users-are-data-invocation-context.md`),
   Simon Scrapes' asker-scoped team memory, Replit's borrow-the-strongest-isolation-
   boundary tenancy, Archon's new per-user identity/attribution layer. No exemplar of a
   *governance kernel* designed for multiple operators. Remains a named research-gap
   candidate (Backlog; Nick gates promotion).
2. **Governance-layer generation (constitution/vision/values) has no external
   exemplar.** BMAD starts at analysis/PRD; nothing in the corpus generates the layer
   above the PRD. The plan's answer (Phase 4 `ops-vision-to-plan` + the direction
   note's governance-first extension) is engine-original, not research-corroborated —
   worth knowing when Phase 4 runs.
3. **"Attachés" resolved to nothing.** The term appears nowhere outside the direction
   note; treated as a transcription artifact pending Nick's one-line clarification.
4. **No complete within-class demand-ledger implementation exists** (session-142 web
   sweep finding, reconfirmed by wave 3 adding nothing on it) — IB-176's query/intent
   log is a compose-known-parts build, not a copy of anyone.
5. **The intake channel is saturated.** Zero ADD / zero ENHANCE for two consecutive
   triage runs (wave 2 run-2 and wave 3); 11 of 16 wave-3 content rejections were
   dedup kills against the KB. The YouTube-practitioner lane now mostly corroborates.
   Marginal return on further bulk video intake is low; targeted `/research-query`
   and primary-source (repo/paper) intake are the higher-yield instruments now.
6. **Jones's Open Skills framework was examined and rejected, not skipped** — the
   wave-2 triage checked the launch video against the KB and found every constituent
   concept already present. No single KB source documents it *as a spec*; fetch the
   Substack post only if Nick overrides that call.

---

## 4. Checkpoint #1 inputs — plan-revision questions the evidence raises

Recommendations only; Nick gates each. Ordered by consequence.

1. **Phase 5 harness scope: adopt "capability" as a named design input, and add a
   fitness loop to the DoD.** Two independent signals converged on the engine's
   direction this week: Pydantic AI 2.0's capability primitive + lean-core-vs-harness
   split, and Archon v0.5.0's tiered provider-capability registry. Recommend: (a) name
   capability-as-composition-unit and tiered-capability declaration as explicit Phase 5
   design inputs in the plan; (b) extend Phase 5's DoD with a harness *maintenance*
   deliverable (scheduled fitness review — the Jones leg's evidence; the
   model-capability registry refresh and `/system-health` are the natural carriers).
   Counterweight to carry: Archon's rules-layer collapse is a warning against
   over-layering the kernel's materializations.
2. **IB-176 ship order: unchanged — proceed as ruled.** The strongest possible Phase 1
   outcome for the memory build is what happened: independent point-for-point
   corroboration (Hermes rebuild) plus validation of the SL distill-then-close
   bootstrap. No evidence suggests reordering steps 1–2 or reopening the design.
   Recommend the milestone's `memory-system-build` scope start next session.
3. **Schedule the residuals as a named pre-Phase-4/5 hygiene batch** rather than
   letting them float: (a) `/promote-findings` over the 10 Archon v0.5.0 candidates;
   (b) `/watch-upstream` refresh of BMAD + superpowers (both ~3 months stale) before
   Phase 4/5 consumes them; (c) `/finding-crosslink` + `/linkage-repair` pass over the
   wave-3 batch (27 new findings carry one-way links by design); (d) the leftover
   per-channel authority triage notes (Chase AI / Herk / Marchese). All four are
   mechanical, sub-session-scale, and two-way doors.
4. **Declare bulk video intake done as a Phase 1 instrument.** Given two consecutive
   zero-ADD/ENHANCE runs and a dedup-dominated reject profile, recommend the plan
   treat future LINKS.md batches as routine operations (the `/link-intake` skill owns
   them), not phase work — and steer new research spend toward targeted
   `/research-query` and primary sources. Watched-library candidate to rule on now:
   `pydantic/pydantic-ai` (+ its Monty sandbox) — the capability primitive is
   dependency-grade for Phase 5 if adopted (recommendation 1).
5. **Feed Phase 3/IB-175 with the visual-plan cluster.** The manual-as-kernel-layer
   question now has a concrete mechanism candidate (plans/DDs as MDX with reusable
   components + post-execution visual recap). Not an adoption recommendation (fails
   abstractions-earn-their-keep on one source) — but the parked governance-
   visualization session should not run without this cluster, and Phase 3's
   whether/when gate is better-informed by it.
6. **Schedule the DD/IB task-queue study** — its stated trigger (converge with the
   named-deps gap-check) has fired, and its feedstock is assembled in gap-check §6.
   Natural home: alongside or just after the IB-176 build, since Jones's five-element
   contract and Archon's queue-iteration semantics both touch IB item shape.

---

## 5. Open Nick items carried

From this phase's artifacts:

- **"Attachés" clarification** — one line: is it a real library/framework or a
  transcription artifact? (Gap-check §2; Phase 4 interview bucket, same as the
  "Division, to a degree" fragment already in PROGRESS Blockers.)
- **Pydantic AI watched-library add** — Nick's call (wave-3 follow-up 3; also
  checkpoint recommendation 4).
- **Jones Open Skills Substack fetch** — only if Nick overrides the wave-2 triage's
  "concepts all in KB" rejection (gap-check §4 residual).
- **Archon `/repo-analyzer` re-run** — the upstream-triage report recommended it; the
  structural re-analysis was in fact completed today (`788ec98`), so this item is
  **discharged**; only the findings promotion (checkpoint recommendation 3a) remains.

Phase-1-relevant blockers already in PROGRESS.md (unchanged by this phase, listed for
the checkpoint's completeness): Design-mode video-intake spec (still wanted?);
verbatim-storage finding null→P3; re-injection correction next step; "Division, to a
degree" fragment (Phase 4); `il-published` mirror question.

---

**Close.** Phase 1's DoD — findings in the KB; delta report — is met with this
document. The plan's next line is its own: **→ Plan checkpoint #1: revisit this plan.**
