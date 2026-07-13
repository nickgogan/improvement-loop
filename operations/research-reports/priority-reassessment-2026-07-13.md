---
title: "Priority Reassessment Report — 2026-07-13"
type: "research-report"
category: "priority-reassessment"
created: "2026-07-13"
author: "improvement-loop"
findings_scanned: 176
candidates_flagged: 16
---

# Priority Reassessment Report — 2026-07-13

**Trigger:** today's KB currency sweep (wave-3 Pass 2 + Archon/pydantic-ai/BMAD/superpowers
promotions + corroboration-extension closeout) added 60 findings and modified 116 —
the largest single-day evidence growth since the skill was created.

**Scan scope:** the 176 findings touched by commits `401b836..9d2f5dd` (corpus: 966).
Untouched findings had no evidence change since their last priority assignment and were
not re-evaluated. Independence counted by author/org (Anthropic ×3 sources = 1 org);
repo-promoted findings counted by originating framework (BMAD, superpowers, Archon,
pydantic-ai are four independent orgs).

**Weighting context (PROGRESS.md):** IB-176 memory-system build is the next build unit —
memory findings carry a timing premium. Harness formalization is the North Star —
capability/harness-layering findings carry a strategic premium. Checkpoint #1 pending.

**This report is proposal-only. No finding was modified. Nick gates every change.**

> **Gate outcome (2026-07-13):** Nick accepted ALL proposals as-is. All changes applied
> 2026-07-13 (per-proposal Applied markers below). One gate-sourced addition rode along
> on proposal 1: a dated Nick gate note on `ralph-wiggum-execution-pattern.md` recording
> that the engine's corpus carries essentially the same shape as Ralph in the PIV loop
> (plan→implement→verify — Archon's shipped plan-to-PR workflow); Ralph and PIV are
> treated as sibling loop variants, with a symmetric same-problem crosslink added to
> `archon-yaml-defined-harness-workflows.md`. Section D judgment flags carry no file
> changes per acceptance of the report as-is.

## Summary

- Findings scanned: 176 (60 added, 116 modified today)
- Reassessment candidates: 16
- Proposed priority upgrades: 7
- Proposed priority downgrades: 1 (rule-4 exception — explicitly requested by the
  trigger context; documented cause: originator deprecated the pattern with eval data)
- Proposed caveats / status changes (no tier change): 4
- Flagged for review, no tier proposal (C5 clusters need human judgment): 4

---

## A. Priority upgrades

### 1. Ralph Wiggum Execution Pattern (`ralph-wiggum-execution-pattern.md`)
- **Current priority:** P2 · Strong (production-tested) · Partially Adopted
- **Proposed priority:** **P1 (Implement Now)**
- **Criteria triggered:** C1 (5+ independent w/ production), C4 (convergent implementation), C5 (8 inbound links)
- **Evidence summary:** 5 independent orgs now implement the loop: AI Automators
  (idiom source), Anthropic (C-compiler build + scientific-computing + harness guide —
  production), gstack/GSD (orchestrator), Archon v0.5.0 (schema-enforced `loop:` engine
  primitive — today's `loop-node-anatomy-schema-enforced-ralph-primitive` extension),
  plus today's `spec-frontmatter-state-machine-unattended-dev-loop` (same-problem).
  8 reverse links across the corpus.
- **Rationale:** the pattern crossed from prompt idiom to *shipped engine primitive with
  a checkable schema* — a qualitatively different evidence class. Directly feeds the
  North Star harness layer and the IB-176 self-improve loop.
- **Status: Applied 2026-07-13** (P1; body Priority Note + Nick gate note re Ralph/PIV
  sibling variants; symmetric same-problem crosslink with
  `archon-yaml-defined-harness-workflows.md`)

### 2. Append-Only Run Log as Working Memory (`append-only-run-log-as-working-memory.md`)
- **Current priority:** P2 (Design Required) · Medium · Partially Adopted
- **Proposed priority:** **P1 (Implement Now)**
- **Criteria triggered:** C4 (independent convergence: BMAD memlog.py + superpowers progress ledger), C5 (7 typed links), timing weight
- **Evidence summary:** two watched frameworks converged independently on the same
  primitive with the same invariants (append-only, blind-write, state-from-tail-on-resume);
  the engine already partially adopts it by convention (PROGRESS/HISTORY spine). 4
  same-problem siblings (`phase-queue-state-file`, `cross-session-learnings-jsonl`,
  `workflow-state-vs-conversation-state`, `append-only-lesson-store`).
- **Rationale:** timing-driven half of the bump — IB-176 (the memory build this finding
  is explicitly a "direct input" to) is the next unit of work after wave-3. P1 = Implement
  Now, and implementation is literally now. Flagged as a judgment call: on raw source
  count alone (2 frameworks + engine) it sits at the P2/P1 boundary.
- **Status: Applied 2026-07-13** (P1)

### 3. File-Mediated Subagent Handoff Workspace (`file-mediated-subagent-handoff-workspace.md`)
- **Current priority:** P3 (Monitor) · Medium · Partially Adopted
- **Proposed priority:** **P2 (Design Required)**
- **Criteria triggered:** C4 (3 independent frameworks), C3 (engine already adopted a variant)
- **Evidence summary:** superpowers v6.0.0 (scripted `.superpowers/sdd/` workspace —
  an explicit inversion of its own v5 paste-the-text doctrine), BMAD v6.10.0 (reviewers
  return verdict + path only; loop/worker modules communicate solely through spec
  files), and Archon's typed output sidecars (`typed-node-output-sidecars-by-type-artifact-discovery`,
  same-problem) — 3 independent implementations. The engine's own handoff-protocol.md
  and the session-137 "report path + 5-line summary" ruling are a live adopted variant.
- **Rationale:** P3 was assigned at promotion before the closeout crosslinks established
  the three-way convergence. The deltas the finding documents (scripted workspace
  creation, per-task brief extraction) are concrete upgrades to a protocol the engine
  already runs — design-required is the right tier.
- **Status: Applied 2026-07-13** (P2)

### 4. Plans That Carry Their Own Contract (`plans-that-carry-their-own-contract.md`)
- **Current priority:** P3 (Monitor) · Medium · Not Yet Started
- **Proposed priority:** **P2 (Design Required)**
- **Criteria triggered:** C4 (4 independent orgs on the same problem)
- **Evidence summary:** superpowers v6.0.0 (Global Constraints + per-task Interfaces,
  with upstream fix-round eval data), BMAD v6.10.0 (sealed SPEC.md file contracts),
  Nick Gupta's production playbook (`task-contract-pattern-schema-first-agent`, already
  P1), and the war-game plan format (`war-game-plan-format-for-executor-handoff`, P2) —
  four independent sources converging on "the artifact handed across a context boundary
  must carry its own binding contract."
- **Rationale:** the cluster's older members already sit at P1/P2; this finding is the
  most complete statement of the pattern and extends `artifact-as-contract-pattern`
  (see D.12). Feeds harness-formalization dispatch design.
- **Status: Applied 2026-07-13** (P2)

### 5. Capability as the Single Agent-Composition Primitive (`capability-as-agent-composition-primitive.md`)
- **Current priority:** P3 (Monitor) · Medium · Not Yet Started
- **Proposed priority:** **P2 (Design Required)**
- **Criteria triggered:** C5 (9 typed links, 7 extends/enables — largest new cluster of the sweep), C4 (cross-framework convergence on capability/skill-as-unit), North Star weight
- **Evidence summary:** 5 of today's pydantic-ai findings are `extended-by` children of
  this one (`cache-stable-progressive-disclosure-catalog`, `capability-composition-declared-ordering-constraints`,
  `declarative-agent-spec-with-serialization-registry`, `disclosure-granularity-decision-rubric`,
  `guardrails-as-hook-lattice-capabilities`); converges with Archon's tiered capability
  registry (already P2) and Claude Code's everything-as-skill on "one composition unit
  above MCP."
- **Rationale:** the finding's own implementation note names it an industry-convergence
  datapoint for the portable-kernel / single-implicit-agent direction — the North Star.
  A P3 on the hub of a 9-link harness-relevant cluster understates it; its P2 children
  would outrank their own parent.
- **Status: Applied 2026-07-13** (P2)

### 6. Framework Abstraction Tax for Agent Development (`framework-abstraction-tax-for-agents.md`)
- **Current priority:** P3 (Monitor) · Strong (production-tested) · Already Adopted
- **Proposed priority:** **P2 (Design Required)**
- **Criteria triggered:** C1 (3 independent orgs + Strong evidence + P3 — mechanical trigger), C5 (14 links, 5 extends/enables)
- **Evidence summary:** 3 independent source orgs (Anthropic, Agentic Academy,
  Claude Code architecture analysis); 14 total links after today's extensions
  (pydantic-ai's lean-core two-lane layering is fresh corroboration of the tax and of
  where frameworks are now putting the boundary).
- **Rationale:** Already Adopted means the bump buys codification, not implementation —
  this is the evidence spine for the engine's platform-native-harness stance and belongs
  in the harness-formalization argument at P2, not in the P3 monitor pool.
- **Status: Applied 2026-07-13** (P2)

### 7. Platform-Native Harness Over Agent Frameworks (`platform-native-harness-over-agent-frameworks.md`)
- **Current priority:** Not Flagged · Medium · Already Adopted
- **Proposed priority:** **P3 (Monitor)** (one-tier bump per C4 rule)
- **Criteria triggered:** C4 (Not Flagged → P3 on convergence), C5 (5 extends/enables links)
- **Evidence summary:** today's sweep linked it into the pydantic-ai two-lane layering
  and Archon harness findings; together with finding 6 it anchors the position the
  North Star is built on.
- **Rationale:** "Not Flagged" on a finding that states the engine's own architectural
  stance is a bookkeeping artifact of early intake. Minimum correction only — it is
  Already Adopted, so Monitor suffices.
- **Status: Applied 2026-07-13** (P3)

---

## B. Proposed downgrade (rule-4 exception — Nick-gated)

Skill rule 4 permits downgrades only on explicit request with documented cause. The
trigger context for this run explicitly requested evaluation of today's contradiction
pairs. One pair crosses the bar:

### 8. Two-Stage Sequential Review (`two-stage-sequential-review.md`)
- **Current priority:** P3 · Medium · Not Yet Started
- **Proposed priority:** **Not Flagged**
- **Documented cause:** pattern deprecated *by its own originator*. Superpowers v6.0.0
  collapsed the two sequential per-task reviewers into one dual-verdict reviewer
  (`unified-dual-verdict-reviewer.md`, `contradicts` pair created today) with upstream
  eval data: similar quality, ~2x faster, ~50% fewer tokens. This is not a rival
  opinion — it is the source repo abandoning the recorded architecture with
  measurements.
- **Note:** the finding stays in the KB as history; the contradicts link preserves the
  supersession trail. If preferred, an `implementation_notes` supersession caveat (as
  in section C) is the softer alternative to a tier drop.
- **Status: Applied 2026-07-13** (Not Flagged; documented cause recorded in
  `implementation_notes`)

---

## C. Caveats — no tier change proposed

Contradiction pairs where the old finding should carry a frontmatter caveat
(`implementation_notes` — currently null on all three; body content untouched per rule 7):

### 9. Step-File Micro-Architecture (`step-file-micro-architecture.md`)
- **Current:** Not Flagged (already floor — no downgrade possible)
- **Proposed:** add `implementation_notes` caveat — *partially superseded by
  `skill-flattening-outcome-prose-over-step-files` (2026-07-13): BMAD, the originating
  framework, retreated from step files for all judgment-heavy work (112→35 step files,
  22→1 orchestrators); the pattern's validated scope is now mechanical execution skills
  only.*
- **Rationale:** the finding as written presents step files as unqualified "principled
  context window management"; the originator's own boundary (mechanical vs judgment
  work) is the durable lesson.
- **Status: Applied 2026-07-13** (scope caveat in `implementation_notes`; priority
  unchanged)

### 10. Two-Axis Parallel Code Review (`two-axis-parallel-code-review-standards-vs-spec.md`)
- **Current:** P3 (Monitor) — keep
- **Proposed:** add `implementation_notes` caveat — *contradicted by
  `unified-dual-verdict-reviewer` (superpowers measured ~2x faster / ~50% cheaper for
  the unified shape); unlike two-stage-sequential-review, this is an independent live
  practice (Pocock v1.1) not deprecated by its originator, so the contradiction is an
  open trade (parallel-axis separation vs single-read economy), not a supersession.*
- **Rationale:** distinguishes it from finding 8; P3 remains correct while the trade is
  unresolved.
- **Status: Applied 2026-07-13** (caveat in `implementation_notes`; P3 kept)

### 11. Memory-File-to-Skill Migration (`memory-file-to-skill-migration.md`)
- **Current:** P2 (Design Required) — **keep P2, no drop**
- **Proposed:** add `implementation_notes` caveat sentence — *Archon v0.5.0's rules-layer
  collapse (`rules-layer-collapse-monolithic-context-counter-signal`) is a live
  counter-signal; note however that its two monolithic mirror files have already
  observably drifted, which is evidence for, not against, this finding's discipline.*
- **Rationale:** the counter-example partially undermines itself (the drift it exhibits
  is the failure mode migration-to-skills avoids), and the finding feeds the IB-176
  memory build now — dropping P2 would be wrong on both counts.
- **Status: Applied 2026-07-13** (caveat appended to `implementation_notes`; P2 kept)

### 12. Artifact-as-Contract Pattern (`artifact-as-contract-pattern.md`)
- **Current:** P3 · adoption_status "Not Yet Started"
- **Proposed:** `adoption_status` → **"Partially Adopted"** (C3), plus priority-review flag
- **Evidence summary:** the engine ships ContractSpec on every staged extract (DD-78)
  and ContextSpec (DD-92) — a live variant of exactly this pattern; today
  `plans-that-carry-their-own-contract` extended it, bringing it to 15 total links
  (10 inbound).
- **Rationale:** C3 is the mechanical trigger (codebase now uses a variant); tier is
  left to Nick — if proposal 4 is accepted, parent and child would reasonably both be P2.
- **Status: Applied 2026-07-13** (`adoption_status` → Partially Adopted; DD-78
  ContractSpec + DD-92 ContextSpec recorded as the live variant; priority-review flag
  noted in `implementation_notes`, tier left at P3)

---

## D. Flagged for review — C5 clusters, no automatic tier proposal

Per criterion 5, link clusters get human judgment, not automatic bumps. All four were
*created today* with priorities set at intake, so retroactive machinery has weaker
standing — listed because their clusters formed within hours of triage:

**Status: No action (2026-07-13)** — judgment flags only; Nick's acceptance of the
report as-is means no file changes for this section.

| Finding | Priority | Cluster signal | Why it might matter now |
|---|---|---|---|
| `cache-stable-progressive-disclosure-catalog.md` | P3 | 8 links, 4 extends/enables | Harness/capability layering (North Star); child of proposal 5 |
| `no-single-memory-architecture-workload-alignment.md` | P3 | 6 links, 4 extends/enables | Design caution directly applicable to the IB-176 build window |
| `controller-deauthorization-reviewer-independence.md` | P3 | 8 links, 3 extends/enables | Review-independence cluster around proposals 8/10 |
| `claude-5-family-retiers-claude-line.md` | null | 7 links, 4 extends/enables | Model-registry currency; null priority on a 7-link node is likely an intake gap (cf. the open "verbatim-storage null→P3" blocker) |

---

## No Change (Confirmed)

160 of the 176 scanned findings were reviewed against all five criteria and not flagged
(list omitted — grep the KB for current priorities if needed). Notables confirmed
as-is: `loop-node-anatomy-schema-enforced-ralph-primitive` (P2, set correctly at
today's intake), `tiered-capability-registry-engine-behavior-branching` (P2, correct),
`unified-dual-verdict-reviewer` (P3 pending engine relevance),
`memory-system-evaluation-triad` and `session-history-import-as-memory-bootstrap`
(both P2 at intake, already aligned with the IB-176 timing premium),
`incremental-one-feature-per-session-pattern` (already P1),
`rules-layer-collapse-monolithic-context-counter-signal` (P3 correct for a
counter-signal), `superpowers-plugin-spec-driven-sub-agent-orchestra` and
`model-tier-routing-expensive-orchestrator-cheap-s` (already P1 despite the sweep's
largest link growth).
