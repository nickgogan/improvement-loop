---
title: "Pipeline Collapse Proposal — Guides + Patterns Only"
type: "design-note"
target_system:
  - "improvement-loop"
created: "2026-04-20"
updated: "2026-04-21"
author: "claude"
stage: "draft"
source_dd:
  - "DD-29"
  - "DD-77"
  - "DD-78"
  - "DD-80"
  - "DD-81"
  - "DD-82"
  - "DD-86"
tags:
  - "design-note"
  - "pipeline"
  - "governance"
  - "proposal"
aliases:
  - "Pipeline collapse"
  - "Guides-plus-patterns-only"
  - "Extract-artifacts retirement"
---

# Pipeline Collapse Proposal — Guides + Patterns Only

**Status:** Design proposal. Not a decision. Nick gates any DD that would codify this. Third in a governance bundle alongside `2026-04-20-artifact-lifecycle-spec.md` and `2026-04-20-artifact-acceptance-rubric.md` — together they reshape the IL's production surface.

## Context

Two session-46 design notes converged on the same edge. The acceptance rubric said: *patterns should be inline in guides by default; rules/skills/templates/agents have low consumer value as standalone extracts; `extracts/` would shrink ~109 → ~30–40 post-audit*. The lifecycle spec said: *change-log discipline is only cost-effective for guides; non-pattern extracts can live on frontmatter pointers because they change rarely and read rarely*. Both converge: **the IL produces guides. Everything else is either inline inside a guide, or a rare cross-cutting reference.** Standalone rule / skill / template / agent extraction is no longer load-bearing on consumer value — it's residual machinery from a pipeline that hadn't yet identified its product.

Nick surfaced at the end of session 46 two moves he wanted formalized this session: *collapse the artifact staging surface to guides + patterns only*, and *design the Librarian as the primary consumer surface working backwards from use cases*. This note is the first; the Librarian design follows.

**Why now.** Session 46 classified 12 findings: 11 pattern, 1 rule, 0 template, 0 skill, 0 agent. The calibration baseline (session 22, 50 findings) is 92% pattern. After four identification runs, the non-pattern yield is ~8%. Session 25's first `/extract-artifacts` run produced 3 rules, 1 skill, 1 template — a total of 5 non-pattern artifacts, against 70+ pattern findings in the same batch. Session 44's run added 26 more non-pattern extracts across rules/skills/templates/agents. The count is small but the machinery is disproportionate: 4 staging directories, 1 skill (`/extract-artifacts`) dedicated to drafting, per-form `_index.md`, deployment paths per form, acceptance criteria per form, lifecycle semantics per form. The lifecycle spec added 9 proposed DDs and the acceptance rubric added 3 more — a total of 12 DDs to govern ~30 artifacts that mostly duplicate content already in guides.

The pipeline is over-built for what it produces. The collapse is the natural endpoint.

**What this note covers.** Seven questions:
1. What collapses, and why.
2. What survives.
3. Post-collapse deployment mechanics.
4. The Librarian read contract — how guides-bigger-than-they-used-to-be stay cheap to consume.
5. DDs to supersede or amend.
6. Migration plan for the ~26 existing non-guide/non-pattern extracts.
7. Tradeoffs to surface for Nick.

**What is out of scope.** Retroactive execution of the migration (analysis only this session). Deployment-to-live-location mechanics beyond the lift-and-deploy step (DD-29 still governs). The folder-to-agent structural hypothesis Nick raised (deferred to a later session).

---

## Current State Inventory

The staging surface as of 2026-04-20.

| Directory | Count | Size | Consumer mode | Consumer value |
|-----------|-------|------|---------------|----------------|
| `extracts/guides/` | 11 | 13–38 KB each | Read (advice) | **High** — primary deliverable |
| `extracts/patterns/` | 72 | 5.8–8.5 KB each | Cite (rationale) | **Low standalone; high when inline in a guide** |
| `extracts/rules/` | 9 | 3.2–6.1 KB each | Grep + enforce | Mixed — most already reachable via target guide |
| `extracts/skills/` | 11 | 4.2–7.6 KB each | Adapt (reference) | Mixed — most tightly coupled to source author's harness |
| `extracts/templates/` | 4 | 5.1–6.9 KB each | Copy + edit | **Real** — but all 4 also fit naturally as guide sections |
| `extracts/agents/` | 2 | 4.9–5.3 KB each | Adapt (reference) | Low — reference examples, Nick-gated (DD-82) |
| **Total** | **109** | — | — | — |

**Form distribution across four classification runs:**

| Run | Findings | Pattern | Rule | Template | Skill | Agent |
|-----|----------|---------|------|----------|-------|-------|
| Session 22 calibration | 50 | 92% | 4% | 2% | 2% | 0% |
| Session 24 P1 batch | 13 | 92% | 8% | 0% | 0% | 0% |
| Session 42 batches | 28 | 92.9% | 3.6% | 0% | 3.6% | 0% |
| Session 45 (current) | 12 | 91.7% | 8.3% | 0% | 0% | 0% |
| **Mean** | — | **~92%** | **~6%** | **~0.5%** | **~1.5%** | **0%** |

**What the distribution tells us.** Rules show up ~every 15 findings. Templates show up ~every 200 findings. Agents have never shown up in Codifier output — all agents in the system are Owner-defined under DD-82. Skills show up rarely and are almost always source-author-specific (the acceptance rubric flagged ~5 of 11 existing skills as likely-reject under the "transferable" criterion).

**What produces the residual non-pattern extracts.** Almost every one is a finding whose center-of-gravity is a reusable *shape* (pattern) that co-occurs with an embedded *artifact* (rule / skill / template). DD-77's single-form classification resolves this at read time — the primary form determines pipeline routing, and secondary forms are noted as co-occurrences. Session 45 produced 4 co-occurrence flags on 11 pattern findings. The harvest queue we added to the identification report was the operational workaround. **DD-X9 in the lifecycle spec proposed formalizing this workaround as a mechanism. This collapse proposal argues the workaround itself is unnecessary** — co-occurring artifacts should live as anchored sections inside the target guide, not as standalone files.

---

## What Collapses

### 1. Standalone `extracts/rules/`, `extracts/skills/`, `extracts/templates/`, `extracts/agents/` directories

**Action:** retire as pipeline staging targets. Existing content migrates into guide bodies as anchored sections (see Migration Plan) or retires if it doesn't meet the acceptance rubric.

**Why:**
- **Most rule findings are already covered by a target guide.** `programmatic-snippet-extraction-via-shell-anti-hallucination` (session 45, the one rule) routes to G2 (Managing Agent Context) or G5 (Designing Agent Tools). Under the current pipeline, it would produce both a standalone rule file AND be absorbed into the guide — duplicate content. Collapsed: it becomes a section `## Rule: Programmatic Snippet Extraction` inside the guide, citable as `guide.md#rule-programmatic-snippet-extraction`.
- **Templates are rare and always fit as guide sections.** The 4 existing templates all describe scaffolds tied to a specific practitioner question (tech stack pinning, YAML with elicitation, execution-context profiles, one-shot PRD). Each has a natural guide home. Keeping them standalone creates a 1-file directory that Librarian has no reason to search separately.
- **Skills as standalone are mostly source-specific references.** The acceptance rubric's skill audit flagged ~5 of 11 existing skills as likely-reject under "transferable" — they describe how a specific practitioner built something in a specific harness. These belong as examples inside a guide (or in `watched-libraries/` as external references), not as IL deliverables.
- **Agents as standalone are system-level decisions (DD-82).** No Codifier run has ever produced one. The 2 existing agent extracts are historical; they stay as reference files but don't gate any pipeline step.

### 2. `/extract-artifacts` as a user-invocable skill

**Action:** retire from the standard pipeline. Deprecate the skill file with a note pointing to `/synthesize-guide` for pattern absorption, and to manual extraction for the exceptional case. Not deleted — retained for reference like `/research-proposer` (DD-80 precedent).

**Why:**
- Post-collapse, 92% of findings are patterns that route to `/synthesize-guide`. The remaining 8% (rules and rare skills/templates) fold into guide sections during the same synthesis. `/extract-artifacts` has no distinct workflow left — it becomes an edge case wrapper.
- The lifecycle spec's DD-X9 (co-occurrence harvesting during synthesis) formalizes the "embed the rule/template/skill as a guide section" mechanism. Once DD-X9 is in `/synthesize-guide`, `/extract-artifacts` has nothing left to do.
- The acceptance rubric's DD-X12 (retroactive audit) can run as a one-shot migration against existing extracts without needing a standing skill.

### 3. DD-X9 as proposed in the lifecycle spec (co-occurrence harvesting as a separate mechanism)

**Action:** obviate. The harvest mechanism is absorbed into `/synthesize-guide`'s standard behavior — every pattern finding carrying a co-occurrence produces an inline guide section for the embedded artifact, with a named anchor. There's no separate queue, no separate artifact class, no separate extraction step.

**Why:** DD-X9 was a workaround for the seam between `/identify-artifacts` (which flags co-occurrences) and `/extract-artifacts` (which only handles primary forms). Collapsing `/extract-artifacts` collapses the seam. The harvesting becomes `/synthesize-guide`'s normal handling of `co_occurrence: [template | rule | skill]` metadata on pattern findings.

### 4. `extracts/_index.md` per-form rows for non-guide, non-pattern forms

**Action:** the form subdirectory sections in `extracts/_index.md` retire when their directories retire. Top-level `_index.md` retains `guides/` and `patterns/` sections only.

---

## What Survives

### 1. `extracts/guides/` — Primary Deliverable

Unchanged in purpose. Absorbs more content per guide (embedded rule / template / skill sections with named anchors). Stays the Librarian's primary read surface and Nick's primary deployment source.

### 2. `extracts/patterns/` — Cross-Cutting Rationale Only

Tightened per DD-X11 (acceptance rubric): standalone pattern extraction requires **either** ≥2 guide citations **or** explicit Librarian-side rationale citation outside any single guide's scope. Single-guide patterns always fold inline in that guide. Projected post-audit count: ~10–15 (down from 72).

**Example survivors:** `programmatic-tool-calling-code-orchestrated-tool-use` (cross-cuts tool design, skill architecture, walkthrough generation; cited by ≥3 guides). `context-rot-attention-budget-depletion` (cited by G2, G7, G8). These earn standalone status because Librarian cites them in multiple contexts.

### 3. `/identify-artifacts` — Classification Router

Unchanged in purpose. Still classifies every finding into a form. The form still determines *where* content lands — but "where" is now almost always "inside a guide" (either as a new pattern absorbed, or as a co-occurring artifact section). Classification reason codes keep their diagnostic value: a finding classified as `rule` still gets recorded as a rule for reporting, but the extraction path writes it as a guide section, not a standalone file.

**What `/identify-artifacts` reports change.** The identification report's routing table becomes `guide + section-type` rather than `form + directory`. Each row says "finding X → guide Y section Z (kind: rule | template | embedded-example)" instead of "finding X → form F → extracts/F/".

### 4. `/synthesize-guide` — Absorbs Full Production Responsibility

Biggest scope expansion. `/synthesize-guide` becomes the only skill that writes artifacts to `extracts/`. Its responsibilities grow:
- **Classify-time content placement.** For each finding in the cluster, determine whether it contributes to an existing section, warrants a new section, or is a co-occurring rule / template / skill that needs its own anchored section.
- **Anchor management.** Every guide section (especially rule / template / skill sections) gets a stable slug. `/synthesize-guide` maintains the anchor map across re-syntheses — anchors are additive-only; no rename without explicit migration.
- **Preserved-section discipline.** From lifecycle spec DD-X1. Untouched across re-syntheses.
- **Co-occurrence inlining.** Formerly DD-X9. When a pattern finding carries `co_occurrence: rule`, the synthesizer produces a section `## Rule: <slug>` with ContractSpec-lite (the rule needs a deterministic check + enforcement boundary). When it carries `co_occurrence: template`, a section `## Template: <slug>` with a fillable body. Etc.
- **Cross-cutting pattern promotion.** If a finding is cited by ≥2 guides (detected by overlapping `source_findings[]` or explicit cross-references), the synthesizer flags it for standalone promotion to `extracts/patterns/` in addition to inline placement.

### 5. Ownership of the 2 existing `extracts/agents/` files

**Action:** leave in place as reference. They are not pipeline output post-collapse; they're historical artifacts describing transferable agent dispositions. Treated the same way as `archive/improvement-proposals/` — retained, not pipeline-active.

---

## Deployment Mechanics Post-Collapse

### Current: file → file

Nick's current deployment workflow for a rule:
```
extracts/rules/programmatic-snippet-extraction.md  →  .claude/rules/programmatic-snippet-extraction.md
```
Straight copy. Live file is the extract file.

### Post-collapse: section-lift from guide

Post-collapse, the rule's authoritative content lives inside the guide at `extracts/guides/managing-agent-context.md#rule-programmatic-snippet-extraction`. Deployment becomes a lift step:

1. Nick (or a helper script) reads the anchored section from the guide.
2. The section body is extracted with the section title becoming the rule file's title.
3. The lifted content is written to `.claude/rules/programmatic-snippet-extraction.md` with a frontmatter note `source: systems/improvement-loop/extracts/guides/managing-agent-context.md#rule-programmatic-snippet-extraction`.
4. Re-deployment (when the guide re-synthesizes) is a re-lift — deterministic, auditable.

### Skill change

`/synthesize-guide` adds a post-synthesis deployment manifest — for each guide, a list of `(anchor, deploy_target)` pairs for sections that are intended as deploy-ready artifacts (rules, templates). Nick reviews the manifest and deploys selectively.

**Optional future skill (not this session):** `/lift-and-deploy <guide>#<anchor>` — reads an anchored section, writes to the deployment target per the manifest. Scripted replacement for manual copy. Can be authored later once the lift pattern is proved by hand.

### What breaks vs. what holds

- **Holds.** Human gate (DD-29). Stage-before-deploy (DD-39, DD-80). ContractSpec per deployable artifact (DD-78) — now carried in the section frontmatter or inline at the top of the section. Pull model (DD-46).
- **Breaks.** The "one extracted file per deployable artifact" invariant. Post-collapse, one guide contains many deployable artifacts, addressed by anchor.
- **Requires.** Anchor stability across re-syntheses. A rename of a rule's slug breaks every deploy manifest referencing it. `/synthesize-guide` must treat anchors as first-class stable identifiers — captured in each guide's frontmatter as an anchor manifest.

---

## Guide Section Manifest (Anchor Stability + Deploy Manifest)

**Note (2026-04-21):** This section was revised in v2. Original v1 draft evaluated three options for the Librarian's read contract against bigger guides. The full Librarian read contract — how the Librarian actually queries substrate — is resolved in the companion substrate audit (`2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md`) via the Librarian reference layer (concept + operation files) and three-tier access model, not in this note. This section retains only what the *collapse* specifically needs: the guide-level anchor manifest that makes deploy-by-anchor work.

The collapse absorbs rule / template / skill content inline into guides as anchored sections. Two things hang off that:
1. **Anchor stability** — post-collapse, anchor IDs are load-bearing. Librarian reads reference them (see substrate audit §"The Librarian Reference Layer" composition tables). Deploy manifests reference them (lift-and-deploy from `guide.md#anchor` to `.claude/rules/<name>.md`).
2. **Deploy metadata per section** — rules and templates carry deploy targets; other sections don't. The guide needs a way to distinguish them.

Both are solved by a single mechanism: a **section manifest in each guide's frontmatter**, keyed by anchor ID.

### Shape

```yaml
sections:
  - anchor: "key-concepts"
    heading: "Key Concepts"
    kind: "concepts"
  - anchor: "step-1-audit"
    heading: "Step 1: Audit Your Current Context"
    kind: "step"
  - anchor: "rule-programmatic-snippet-extraction"
    heading: "Rule: Programmatic Snippet Extraction"
    kind: "rule"
    deploy_target: ".claude/rules/programmatic-snippet-extraction.md"
    source_findings: ["programmatic-snippet-extraction-via-shell-anti-hallucination"]
  - anchor: "template-context-budget-worksheet"
    heading: "Template: Context Budget Worksheet"
    kind: "template"
    deploy_target: null  # template is advice-surface, not a deploy target
```

### Why anchor IDs, not line numbers

Line numbers in frontmatter break on any body edit. Anchor IDs resolve to line ranges via `Grep -n "^## <heading>"` at read time — cheap, robust across re-syntheses. `/synthesize-guide` regenerates the manifest on every run; anchors are additive-only across re-syntheses (per DD-NEW-3 below).

### Relationship to the Librarian reference layer

- Concept files (`operations/references/librarian/harness.md` etc.) reference guide sections by `guide.md#anchor`. Stability of anchors is what lets those references not rot.
- Operation files (`audit.md`, `diagnose.md`) compose by pulling sections of a particular `kind` (Contract sections for audit; Pitfalls sections for diagnose; etc.). The `kind` field in the manifest is what enables kind-indexed composition.
- Deploy happens via lift from `guide.md#anchor` per the manifest's `deploy_target`. Future `/lift-and-deploy` helper skill (not this session) scripts the lift.

The manifest is the single artifact that both read (Librarian composition) and deploy (rule/template extraction) hang off of. It was originally one of three options considered in v1; v2 treats it as the agreed mechanism and stops deliberating.

---

## DDs to Supersede or Amend

Proposed titles only. Nick gates filing. These slot into the lifecycle-spec + acceptance-rubric bundle.

| # | DD | Action | One-line rationale |
|---|----|--------|--------------------|
| 1 | **DD-80 (Pipeline simplification)** | **Amend** | Pipeline shape becomes `Finding → /identify-artifacts → Report → /synthesize-guide → guide (+ inline deploy-ready sections) → deploy`. `/extract-artifacts` retires as user-invocable. |
| 2 | **DD-81 (Pattern filter)** | **Tighten** | Tightens to DD-X11's phrasing: patterns default to inline sections; standalone extraction requires ≥2 guide citations or cross-guide rationale. Already foreshadowed by acceptance rubric. |
| 3 | **DD-X9 (Co-occurrence harvesting)** | **Obviate** | Replaced by `/synthesize-guide`'s standard handling of co-occurrence metadata — no separate mechanism needed. |
| 4 | **DD-X12 (Retroactive audit)** | **Retain, re-scope** | Audit scope narrows: apply the acceptance rubric against rules/skills/templates/agents and produce a per-file disposition (migrate inline / retire / keep as pattern-crosscutting). |
| 5 | **Proposed DD-NEW-1: Guide section manifest** | **New** | Each guide carries a frontmatter `sections[]` manifest with anchor IDs, headings, kinds, and (optional) deploy targets. Schema change to `_schema.yaml`. `/synthesize-guide` maintains. |
| 6 | **Proposed DD-NEW-2: Deploy-by-anchor** | **New** | Deployment happens via section-lift from `guide.md#anchor` per the guide's deploy manifest. ContractSpec moves into the section frontmatter or inline section header. Manual deploy step for now; scripted later. |
| 7 | **Proposed DD-NEW-3: Anchor stability** | **New** | Anchor IDs are additive-only across re-syntheses. Renames require an explicit migration entry in the guide changelog. Enforced by `/synthesize-guide` regression check. |
| 8 | **Proposed DD-NEW-4: `/extract-artifacts` deprecation** | **New** | Skill retires as user-invocable; retained for reference (DD-80 precedent with `/research-proposer`). Non-pattern handling absorbed into `/synthesize-guide`. |

**Total DD bundle after the collapse:** lifecycle spec's DD-X1..X8 (X9 obviated) + acceptance rubric's DD-X10..X12 (X12 re-scoped) + this note's 4 new DDs = ~14 DDs. Comparable to the 12 the lifecycle spec + rubric already proposed, trading DD-X9 for 4 new DDs that replace a pipeline mechanism with a read-and-deploy mechanism.

---

## Migration Plan

### Scope

26 existing non-guide/non-pattern extracts:
- 9 rules (`extracts/rules/`)
- 11 skills (`extracts/skills/`)
- 4 templates (`extracts/templates/`)
- 2 agents (`extracts/agents/`)

Plus ~57–62 pattern extracts (72 current minus the ~10–15 cross-cutting survivors) that fold inline into their routed guides during the next `/synthesize-guide` run.

### Procedure (sketch, not executed this session)

**Phase M1 — Audit (analysis only).**
1. Read each non-guide/non-pattern extract against the acceptance rubric.
2. For each file, produce a disposition:
   - **Migrate inline:** content moves into a guide section under the next re-synthesis. Record target guide + anchor ID.
   - **Retire:** content fails acceptance rubric (tightly coupled to source harness, not transferable, duplicate of guide content). Mark `stage: retired` in frontmatter; move to `archive/extracts/<form>/`.
   - **Keep standalone:** rare. Only if the artifact has cross-guide rationale value AND passes the acceptance rubric. This shouldn't happen for rules/templates/skills/agents — if it does, the form classification was wrong.
3. Output a migration manifest: one table, 26 rows, per-file disposition + target guide anchor (for migrate-inline).

**Phase M2 — Inline migration (execute per-guide).**
1. For each affected guide, run `/synthesize-guide` with the migration manifest.
2. The synthesizer incorporates each migrate-inline row as a new `## Rule:` / `## Template:` / `## Skill (example):` section with ContractSpec and anchor ID.
3. Produce a guide changelog entry per lifecycle spec DD-X3.
4. Delete the migrated source file from `extracts/<form>/` after the anchor is stable in the guide.

**Phase M3 — Directory retirement.**
1. Once all content in `extracts/rules/`, `extracts/skills/`, `extracts/templates/`, `extracts/agents/` is migrated or archived, move each directory wholesale to `archive/extracts/<form>/`.
2. Update `extracts/_index.md` to remove the retired-form sections.
3. Update IL `CLAUDE.md` to reflect guides + patterns as the only active staging directories.

### Estimated cost

- **Phase M1:** 1 Codifier session. Analysis-only. Outputs a manifest.
- **Phase M2:** 3–4 guide re-syntheses (staleness-gated on lifecycle-spec DDs). Each re-synthesis absorbs the migrating rows for its target guide.
- **Phase M3:** 1 session to execute directory moves and index updates.
- **Total:** ~5 sessions from approval to complete migration.

### What this migration does NOT do

- Touch the 72 pattern extracts beyond what `/synthesize-guide` does naturally (inline absorption into target guide; standalone retention if cross-guide criterion fires). The acceptance rubric's DD-X12 retroactive audit covers that scope.
- Modify any deployed content in `.claude/` or `meta-system/knowledge/`. Deployment is Nick's, governed by DD-29.
- Auto-retire any file without Nick's per-file approval. Every disposition is presented in the manifest; nothing deletes without gating.

---

## Tradeoffs to Surface for Nick

### 1. Guide completeness becomes load-bearing

Post-collapse, the guide is the canonical location for every deploy-ready rule, template, and skill section. If a guide omits a section it was supposed to carry (authoring slip, synthesis skip), nothing else captures it — the extract directory that used to be a backup doesn't exist anymore. Mitigation: the identification-report → synthesis-manifest → guide-section chain is audit-traceable; a dropped finding is visible in the delta between `source_findings[]` pre-syn and post-syn. `/synthesize-guide` can regress-check this. Still, the author's attention to completeness matters more than before.

### 2. Deployment mechanic shifts to section-lift

Currently Nick copies `extracts/rules/X.md` to `.claude/rules/X.md`. Post-collapse, Nick lifts `guide.md#anchor` to `.claude/rules/X.md`. The lift is slightly more manual without a helper script. Mitigation: the deploy manifest in the guide's frontmatter (Option B for read-contract) tells Nick exactly where each section lands. The helper script can come later. For the 2026-04-20 state (~26 deployable sections post-migration), manual lift is tractable.

### 3. Retroactive migration work

26 non-pattern extracts plus 57–62 pattern extracts (that weren't already cross-cutting) need disposition. This is work. Mitigation: the work is bounded (Phase M1 is one session of analysis; Phase M2 happens naturally on the next staleness-gated re-synthesis of each guide). The alternative — leaving the directories in place — creates ongoing lifecycle tax (drift detection, acceptance-rubric re-audits) that the collapse eliminates.

### 4. Anchor stability discipline

Post-collapse, anchor IDs become load-bearing. A rename breaks Librarian's read contract and Nick's deploy manifest. Mitigation: additive-only convention (DD-NEW-3) + `/synthesize-guide` regression check. The discipline is real but narrow — anchors change only when sections retire or split, and both cases warrant explicit migration entries anyway.

### 5. The collapse bets on patterns staying ~92%

If the form distribution shifts (e.g., we start processing dimensions where rules or skills dominate), the collapsed pipeline may under-serve the new distribution. Mitigation: the pipeline shape is not irreversible. If the mix shifts materially, reintroducing `/extract-artifacts` is a re-expansion from a smaller base. For now, four runs at ~92% pattern is strong evidence the collapse is right-sized.

### 6. Rubric fidelity under pressure

With `/synthesize-guide` now absorbing rule/template/skill content inline, there's a risk the synthesizer misclassifies or under-processes embedded artifacts (e.g., treats a rule as a generic section without an enforcement boundary). Mitigation: identification-report's co-occurrence metadata is the authoritative input; synthesizer just renders what identification classified. The fidelity contract is preserved — classification still happens in `/identify-artifacts` against the form rubric, which doesn't change.

---

## Open Questions for Nick

1. **Lift helper script timing.** Manual lift is fine for now. Is it worth planning a `/lift-and-deploy` skill as a follow-up task in IB, or defer until migration experience tells us whether manual is painful?
2. **Retire skills' extract directory with its agents counterpart (`extracts/agents/`), or keep agents as a pure historical directory?** Agents don't get actively extracted. They could live in `archive/extracts/agents/` cleanly, or stay under `extracts/agents/` as a reminder that agent classifications flag for Nick review (per DD-82).
3. **Migration phasing against the G7/G2/G9 re-synthesis block.** Phase M2 folds naturally into the next re-syntheses of G7 / G2 / G9, which are blocked on Phase-1 lifecycle-spec DDs. Should migration kick off at the same time the lifecycle-spec DDs file, or on a separate gate? Coupling them is efficient; separating them is auditable.
4. **Section-kind vocabulary for the manifest.** The current sketch uses `step`, `rule`, `template`, `example`, `concepts`, `pitfalls`. Is this the right vocabulary, or should it mirror the form-classification rubric's vocab exactly?
5. **Cross-cutting pattern survivors.** DD-X11 + this collapse leaves a pattern in `extracts/patterns/` only if cited by ≥2 guides OR by Librarian outside any guide. Do you want a minimum threshold (e.g., only pattern citations with >N Librarian references survive), or is the two-guide criterion enough?
6. **Agents in `extracts/agents/` — migration destination.** The 2 existing agent extracts (Quinn, initializer) describe transferable dispositions. Do they fit inside a guide (G10 Agent Design Patterns has them as reference candidates), or stay as a standalone `archive/extracts/agents/` for completeness?
7. **Folder-to-agent structural hypothesis.** Explicitly deferred from this session, but does this collapse change your thinking about it? Post-collapse, the IL has fewer directories (9 → 7 for `extracts/`; no change elsewhere), which reduces the "each folder becomes an agent" surface.

---

## Relationship to the Lifecycle Spec and Acceptance Rubric

The three design notes compose as:

| Design note | Answers | Primary scope |
|---|---|---|
| **Acceptance rubric** | *Which artifacts should exist at all?* | Write-time gate. Per-form acceptance criteria. |
| **Pipeline collapse** (this note) | *What's the production surface?* | Structural. Which skills run, which directories stage, what Librarian reads. |
| **Lifecycle spec** | *What happens to artifacts that exist?* | Post-write mechanics. Merge, create, change-log. |

Post-collapse, the three bound the IL's production surface:
- **Acceptance rubric** → determines if a finding becomes a guide section, a standalone pattern, or retires.
- **Pipeline collapse** → determines how that determination is implemented (one skill, one directory per form).
- **Lifecycle spec** → determines what happens when guides change, findings update, and artifacts need revising.

The lifecycle spec's 9 DDs shrink to 8 (DD-X9 obviated). The acceptance rubric's 3 DDs retain, with DD-X12 re-scoped to cover the narrower migration surface. This note adds 4 new DDs. Net: ~15 DDs to codify the full production surface — a reasonable one-milestone effort.

---

## Cross-References

- Lifecycle spec (obviated DD-X9; preserved section discipline from DD-X1; changelog mechanism from DD-X3): `project-management/design-notes/2026-04-20-artifact-lifecycle-spec.md`
- Acceptance rubric (DD-X11 tightens DD-81; audit headline ~109 → ~30–40): `project-management/design-notes/2026-04-20-artifact-acceptance-rubric.md`
- Identification report (co-occurrence harvest queue as the operational workaround this proposal obviates): `operations/pattern-identification-reports/2026-04-20-session-45-identification-report.md`
- Guide routing table (primary input for `/identify-artifacts`'s routing changes): `operations/references/guide-routing-table.md`
- Form classification rubric (unchanged — still runs at identification time): `operations/references/form-classification-rubric.md`
- `/synthesize-guide` skill contract (target of the scope expansion): `.claude/skills/synthesize-guide/SKILL.md`
- `/extract-artifacts` skill contract (target of retirement): `.claude/skills/extract-artifacts/SKILL.md`
- `/identify-artifacts` skill contract (reports format changes post-collapse): `.claude/skills/identify-artifacts/SKILL.md`
- Governing DDs:
  - DD-29 (human gate at stage boundaries) — unchanged
  - DD-77 (single-form classification) — unchanged
  - DD-78 (ContractSpec) — extended; now carried in guide section frontmatter or inline section header
  - DD-80 (pipeline simplification) — **amended** by this proposal
  - DD-81 (pattern filter) — **tightened** by this proposal + DD-X11
  - DD-82 (IL 4-agent architecture) — unchanged
  - DD-86 (Owner responsibility) — unchanged
- Frontmatter schema: `_schema.yaml` (will need `sections[]` field addition if DD-NEW-1 accepted)
