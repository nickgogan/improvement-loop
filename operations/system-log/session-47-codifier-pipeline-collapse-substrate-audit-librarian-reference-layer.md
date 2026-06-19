---
notion_id: null
log_entry: "Session 47 — Codifier: Pipeline Collapse Proposal + Substrate Audit + Librarian Reference Layer Design"
actor: "Agent: Claude"
area: null
change_type: "Design"
milestone: null
rationale: "Two streams planned (collapse proposal + Librarian design), reframed mid-session into three streams after Nick's ultrathink challenge on whether the taxonomy chain actually supports Librarian use cases. Produced: (1) pipeline collapse proposal, (2) substrate audit with v2 synthesis introducing Option α' (composition registry + three-tier access) and the Librarian reference layer (concept files + operation files). Dimensions registry reframed to Researcher-specific scan scope (reframe-only, no re-categorization); Agentic OS renamed to Agentic Systems; Harness rejected as dimension (placed in Librarian reference layer as a cross-cutting concept). Stream B.1–B.3 (Librarian use-case registry, read-contract design, assessment skill drafts) deferred to session 48 — this session closed at minimum-coherent state to avoid handing off incoherent docs."
source_dd: "DD-29, DD-77, DD-78, DD-80, DD-81, DD-82, DD-86"
target_system: "improvement-loop"
timestamp: "2026-04-21T00:00:00.000Z"
---

# Session 47 — Codifier: Pipeline Collapse Proposal + Substrate Audit + Librarian Reference Layer Design

## What Changed

### Stream A — Pipeline Collapse Proposal

- Produced design note at `project-management/design-notes/2026-04-20-pipeline-collapse-proposal.md`. Third in the governance bundle alongside the session-46 lifecycle spec and acceptance rubric.
- **Core proposal:** collapse `extracts/rules/`, `extracts/skills/`, `extracts/templates/`, `extracts/agents/` as staging directories; non-pattern content migrates inline into guides as anchored sections. `/extract-artifacts` retires as user-invocable. DD-X9 (co-occurrence harvesting) obviated — absorbed into `/synthesize-guide`'s native handling of co-occurrence metadata.
- **Survives:** `extracts/guides/` (primary deliverable); `extracts/patterns/` tightened to cross-cutting only (≥2 guide citations or Librarian-outside-guide rationale); `/identify-artifacts` unchanged; `/synthesize-guide` absorbs full production responsibility.
- **Deploy mechanics post-collapse:** lift-and-deploy from `guide.md#anchor` to `.claude/rules/<name>.md` etc. per a per-guide section manifest in frontmatter. Manifest keyed by anchor IDs (not line numbers), with `kind + deploy_target` metadata per section.
- **Migration plan (sketch only, not executed):** Phase M1 audit → Phase M2 inline migration during next staleness-gated re-syntheses → Phase M3 directory retirement. ~5 sessions end-to-end.
- **DD bundle:** amend DD-80; tighten DD-81; obviate DD-X9; re-scope DD-X12; 4 new DDs (section manifest, deploy-by-anchor, anchor stability, `/extract-artifacts` deprecation).
- **Revised in v2 (2026-04-21):** "Librarian Read Contract" section trimmed. Original v1 evaluated three options for Librarian read shape; those deliberations moved to the substrate audit. This section now retains only the guide section manifest, scoped to anchor stability + deploy metadata.

### Stream B — Substrate Audit (added mid-session per Nick's ultrathink challenge)

- Produced diagnostic design note at `project-management/design-notes/2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md`.
- **Prompted by:** Nick's question — "Are research dimensions, patterns, and guides actually the right substrate for the Librarian's use cases?" Ultrathink audit followed.
- **Diagnostic finding:** Current substrate has a missing third layer. Dimensions (Researcher-side, aspect-topic intake) + Guides (practitioner-question product) are well-formed for what they do. But there's no consumer-query-indexed layer, so Librarian was implicitly expected to aggregate at runtime. For stable assess-* skills (Nick's top priority), runtime aggregation is expensive, inconsistent, and cache-hostile.
- **v1 recommendation:** Option α (view artifacts — standalone curated rubrics, symptom maps, catalogs pointing into guides). Nick's three inline notes challenged this.
- **v2 recommendation (post-interview):** Option α' — Librarian reference layer (small pointer artifacts: concept files + operation files) + three-tier access model (guides → patterns+findings graph → watched-library repos). No new artifact form; reference layer is a routing table, not a knowledge base. Lighter than α, preserves finding graph as Tier 2 substrate, promotes watched-libraries to Tier 3 consumer-accessible depth substrate.
- **Disambiguation surfaced:** "Rubric" is overloaded in our system. Three distinct senses (form-classification rubric / acceptance rubric / hypothetical assessment rubrics) plus a fourth thing that looks rubric-shaped (Contract sections per DD-78). v1 conflated them; v2 names each explicitly.
- **Untested empirical claim:** Contract invariants across `{G1, G2, G3, G5, G6, G9, G10}` compose into a coherent agent-audit rubric. Option α' depends on this. Spot-check deferred to session 48.

### Stream B interview — key decisions reached

- **Dimensions reframe: reframe-only.** Dimensions stay as aspect-topic scan scopes. Rename Agentic OS → Agentic Systems. Rewrite `research-dimensions.md` preamble to make Researcher-specificity explicit. No new Harness dimension — Harness is a consumer concept, not a scan topic.
- **Agentic Systems scope confirmed:** personal/team/business operational systems where multiple agents serve user workflows (second-brain, daily briefs, scheduled-task setups, vault-as-OS patterns).
- **Harness relocated.** Placed in Librarian reference layer as a cross-cutting concept file. No new dimension.
- **Consumer artifacts framing dropped.** Replaced by (concept, operation) decomposition — verb-keyed operation files × noun-keyed concept files.
- **Three-tier Librarian access adopted.** Tier 1 (guides, section-addressable, default). Tier 2 (patterns + findings graph using `related_findings` typed links, on escalation). Tier 3 (watched-library repos, on explicit consumer ask). Promotes watched-libraries from Researcher-monitoring-only to consumer-accessible.
- **Librarian reference layer confirmed.** Directory: `operations/references/librarian/`. Flat layout; two file types (concept / operation) distinguished by frontmatter `type:`.
- **Variants as first-class optional field** for concept files. Applies to Agent, Memory, Second Brain (three genuinely distinct referents each). Does not apply to Harness, MCP, Context Rot, Agentic Systems (single referent each).
- **Second Brain variants:** (a) Human second brain — mostly human-authored PKM, AI minimally involved; (b) AI second brain — agent's own accumulated KB (adjacent to Memory Architecture + Context Engineering + Intent); (c) Hybrid — shared surface with HITL gates, human curation for agent intent. MetaSystem itself is an instance of the hybrid variant.
- **Early entries confirmed:** concepts (harness, agentic-systems, second-brain [3 variants], context-rot, mcp); operations (audit, diagnose, design).

### Stream B.1–B.3 — Deferred

- Not executed this session. Original plan was Librarian use-case registry (B.1) → read-contract design (B.2) → assessment skill designs (B.3). Substrate audit reshaped their scope; executing them in fatigued context would risk incoherence.
- Deferred with full context to session 48 handoff.

### Minimum-Coherent Close (this session's final pass)

- Substrate audit updated in-place (v2): Nick's inline notes preserved with per-note resolutions; Options/Recommendation/DDs/Open-Questions sections replaced to reflect Option α' + reference layer + three-tier access + rubric disambiguation.
- Collapse proposal "Librarian Read Contract" section trimmed — three-option deliberation removed; section manifest retained as agreed mechanism, scoped to anchor stability + deploy metadata; read-contract questions pointed to substrate audit.
- Session 47 SL entry (this file) — captures what was produced and what's deferred.
- Session 48 handoff prompt — generates from this session's state.

## Counts

| Metric | Value |
|--------|-------|
| Design notes produced | 2 (collapse proposal, substrate audit) |
| Design notes revised in v2 | 2 (both above, updated post-interview) |
| Proposed DDs (collapse proposal) | 4 new + DD-80 amend + DD-81 tighten + DD-X9 obviate + DD-X12 re-scope |
| Proposed DDs (substrate audit) | 4 new (reference layer, three-tier access, reference file acceptance, dimension reframe) |
| Total DD bundle (session 46 + 47) | ~16 DDs across lifecycle spec + acceptance rubric + collapse + substrate audit |
| Streams executed | 1.5 (Stream A complete; Stream B partial — audit only; Streams B.1–B.3 deferred) |
| Nick's inline notes resolved | 3 (dimensions reframe, three-tier access, drop consumer-artifacts framing) |

## Design Decisions Applied

| DD | How Applied |
|----|-------------|
| DD-29 | Human gate honored — nothing deployed; all output in `project-management/design-notes/`. |
| DD-77 | Single-form classification unchanged. |
| DD-78 | ContractSpec per artifact unchanged. **Flagged:** Contract invariants now load-bearing as emergent audit criteria under Option α'; DD-78 framing may need amendment to reflect dual role. |
| DD-80 | Pipeline simplification — amended by collapse proposal (proposed, not filed). |
| DD-81 | Pattern filter — tightened by collapse proposal + DD-X11 from acceptance rubric. |
| DD-82 | IL 4-agent architecture preserved. **Flagged:** Librarian role expands under α' (reference-layer maintenance + three-tier access); may warrant DD amendment. |
| DD-86 | Owner responsibility unchanged. |

## Affected Items

- `project-management/design-notes/2026-04-20-pipeline-collapse-proposal.md` — created (v1); revised in v2 (Librarian Read Contract section trimmed)
- `project-management/design-notes/2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md` — created (v1 with Option α); revised in v2 with Nick's inline notes + Option α' + reference layer + three-tier access + rubric disambiguation
- `operations/system-log/session-47-codifier-pipeline-collapse-substrate-audit-librarian-reference-layer.md` — created (this file)
- `operations/handoffs/handoff-prompt-session-48-codifier-librarian-reference-layer-build.md` — created (handoff to session 48)

## Deferred to Session 48

### Primary scope

1. **Rewrite `research-dimensions.md`** — preamble rewrite (Researcher-specificity explicit) + rename Agentic OS → Agentic Systems entry.
2. **Write exemplar concept/operation files** — `harness.md` (concept, no variants), `second-brain.md` (concept, three variants), `audit.md` (operation). These lock the template shape and prove the reference layer works.
3. **Spot-check Contract sections** on `{G1, G2, G10}` — empirical test of Option α''s central claim. Read the three Contract sections; test composition against a sample agent.md audit query; assess whether invariants compose into a coherent audit rubric. If pass → proceed with α'. If fail → escalate to view artifacts (α) for the assessment use case.
4. **Stream B.1 use-case registry** — map 35 session-46 use cases onto (concept, operation) pairs; prioritize by frequency weighting.
5. **Stream B.2 read-contract design** — formalize three-tier escalation rules, confidence disclosure, provenance surfacing, consumer-input handling.
6. **Stream B.3 assessment skill designs** — assess-prompt, assess-agent, assess-skill as load-and-apply wrappers over (audit operation × concept-file) composition.

### Secondary scope

7. **References-by-agent reorg IB item.** Current `operations/references/` mixes files owned by different agents. Propose moves: `researcher/research-dimensions.md`, `codifier/form-classification-rubric.md`, `codifier/guide-routing-table.md`, `librarian/` (already scoped). Plus skill path updates (`/identify-artifacts`, `/synthesize-guide`, `/research-loop` have path refs).
8. **DD-78 amendment proposal** — reflect Contract sections' dual role (artifact governance + emergent audit criteria). Defer until spot-check outcome is in.
9. **DD-82 amendment proposal** — reflect Librarian's expanded role (reference-layer maintenance + three-tier access). Defer until reference layer is exercised.

### Deferred items from prior sessions (carried forward)

- **Session 45 identification Status fields** — Nick has not yet edited APPROVED/REJECTED/REDIRECTED for 4 guided-tier + 8 auto-tier entries. Still pending.
- **Lifecycle spec Phase 1 DDs** (DD-X1, DD-X3, DD-X4) — awaiting Nick's decision. Blocks G7/G2/G9 re-syntheses.
- **G7 / G2 / G9 re-syntheses** — still blocked on Phase 1 DDs.
- **Memongo improvement surfaces (6 items)** — Nick-direct or Researcher scope.
- **Session 44 non-pattern deployment** — artifacts in `extracts/rules/` and `extracts/skills/` pending Nick's deployment to enforcement locations. Post-collapse, these become migration-into-guides candidates per Phase M1 audit rather than deploy candidates.

## Next Steps (Nick's Decisions)

1. **Review both design notes at their v2 state.** Specifically: does Option α' (reference layer + three-tier access) match what you intended after the interview, or does it need further refinement before session 48 executes on it?
2. **Review collapse proposal's section manifest shape.** Confirm anchor-ID scheme + `kind + deploy_target` fields match your expectations.
3. **Confirm session-48 scope order.** Suggested sequence: rewrite `research-dimensions.md` first (5 min) → spot-check Contract sections (20 min, validates α') → write exemplar concept/operation files (45 min) → Stream B.1 use-case registry (then B.2, B.3 as context allows). Alternative: push spot-check to the front to de-risk α' before any authoring. Your call.
4. **Terminology check.** Session-47 conversation used "curator" informally in one message; confirmed interpretation is "Codifier" per DD-82. Flag if rename is intended.

## Cross-References

- Session 46 SL entry: `operations/system-log/session-46-codifier-session-45-identification-and-lifecycle-spec.md`
- Session 46 lifecycle spec: `project-management/design-notes/2026-04-20-artifact-lifecycle-spec.md`
- Session 46 acceptance rubric: `project-management/design-notes/2026-04-20-artifact-acceptance-rubric.md`
- Session 47 pipeline collapse proposal: `project-management/design-notes/2026-04-20-pipeline-collapse-proposal.md`
- Session 47 substrate audit: `project-management/design-notes/2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md`
- Session 48 handoff: `operations/handoffs/handoff-prompt-session-48-codifier-librarian-reference-layer-build.md`
- Identification report (session 45): `operations/pattern-identification-reports/2026-04-20-session-45-identification-report.md`
- Guide routing table: `operations/references/guide-routing-table.md`
- Research dimensions registry: `operations/references/research-dimensions.md`
- Codifier agent definition: `agents/codifier/agent.md`
- Librarian agent definition: `agents/librarian/agent.md`
