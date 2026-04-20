---
title: Priority Reassessment Report — 2026-04-20
type: research-report
category: priority-reassessment
created: 2026-04-20
author: improvement-loop
findings_scanned: 21
candidates_flagged: 2
---

# Priority Reassessment Report — 2026-04-20

## Summary

- **Scope:** Retroactive re-evaluation targeted at the 21 findings updated during session 42 Batch 2 extraction, plus a broader Criterion-5 crosslink-cluster scan across the full KB (533 findings).
- **Findings scanned (targeted):** 21
- **Crosslink-cluster scan (full KB):** ~533 (filtered to 49 with 3+ strong relationships)
- **Reassessment candidates:** 2
- **Proposed priority bumps:** 1 (bundle: evidence_strength + priority)
- **Proposed evidence_strength upgrades:** 2
- **Proposed adoption_status changes:** 0
- **Cluster-only flags (no proposal):** 6

Conservative run. Most Batch 2 updates were "second-source corroboration" which reinforced findings already sitting at an appropriate priority — not threshold-crossing evidence.

## Trigger

Session 42 Batch 2 extraction added 26 new findings, updated 21, and wrote 28 crosslinks across 13 sources. Three interim changes were already applied mid-Batch (see "Already Applied" section). This reassessment catches anything else the Batch 2 evidence pushed across a threshold.

---

## Already Applied (Confirmed)

These three changes were committed during Batch 2 and are verified correct in frontmatter:

| Finding | Change Applied | Verified |
|---------|----------------|----------|
| `autoplan-auto-decision-pipeline` | Not Flagged → P2 (Design Required) | Yes — frontmatter matches |
| `scheduled-task-dashboard-observability-layer` | P3 → P2 (Design Required) | Yes — frontmatter matches |
| `scheduled-tasks-for-real-time-context-maintenance` | P3 → P2 (Design Required) | Yes — priority matches. **Evidence_strength conflict: delta report says Medium→Strong, but frontmatter still shows Medium. See Evidence Conflicts below.** |

---

## Candidates

### Candidate 1: `dark-factory-ai-only-codebase-management`

- **Current priority:** P3
- **Proposed priority:** P2 (Design Required)
- **Current evidence_strength:** Low (theory + early experiment)
- **Proposed evidence_strength:** Medium (practitioner-documented)
- **Criteria triggered:** Criterion 2 (Evidence Strength Upgrade), Criterion 5 (Related Findings Cluster — 5 `enabled-by` links)
- **Evidence summary:** 2 independent sources (Cole Medin live stream + Dan Shapiro "Dark Code" framing). Adds StrongDM as a named production reference (shipping AI-authored PRs continuously with no human review). Adds Dan Shapiro's 5-level framework (Jan 2026 blog). Cole Medin's VPS+Archon implementation is a public, live experiment — not theoretical.
- **Rationale:** Crosses the Weak→Medium threshold for Criterion 2: finding now has a named production deployment (StrongDM) and a public live experiment (Medin VPS), plus 5 `enabled-by` strong-rel links from Batch 2 crosslinks (archon-yaml-defined, specialized-harness, holdout-validation, github-label-as-workflow-state, worktree-isolation). Priority bump is modest (P3→P2) and reflects that it is no longer pure theory — though not yet enough independent production evidence for P1.

### Candidate 2: `scheduled-tasks-for-real-time-context-maintenance`

- **Current priority:** P2 (Design Required) — already applied in Batch 2
- **Current evidence_strength:** Medium (practitioner-documented) — **NOT yet applied**
- **Proposed evidence_strength:** Strong (practitioner-documented → production-tested)
- **Criteria triggered:** Criterion 2 (Evidence Strength Upgrade) — per delta report intent that was only partially applied
- **Evidence summary:** 2 independent practitioner sources (Beni/Firefly 7-levels + Claude-Code-for-life daily brief). Both demonstrate live, running implementations. The delta report `2026-04-20-batch-2-delta-report.md` explicitly claims "evidence upgraded Medium→Strong" but the frontmatter still reads `Medium (practitioner-documented)`.
- **Rationale:** This is a documentation-hygiene correction, not a new proposal. Apply the evidence_strength upgrade to match the delta report's stated intent.

---

## Cluster Flags (Criterion 5 — No Auto-Proposal)

The following findings have 3+ `extends`/`enables`/`enabled-by`/`part-of`/`feeds-into` links but insufficient independent-source count to propose a tier bump. Per Criterion 5, these are flagged for human judgment. None triggered other criteria.

| Finding | Strong-Rel Links | Current Priority | Sources | Note |
|---------|------------------|------------------|---------|------|
| `context-infrastructure-seven-level-maturity-model` | 6 | P3 (Monitor) | 1 | Hub finding. `adoption_status: Already Adopted`. Single-source origin (seven-levels-context video) but 6 findings extend it. Consider P2 for its architectural importance if Nick views it as a load-bearing framework. |
| `rl-trained-autonomous-tool-selection-artist-pattern` | 5 | P3 (Monitor) | 1 | Single-paper finding with rich internal cluster (ARTIST paper findings). Cluster is genuine but single-origin — not convergent. |
| `mcp-n-plus-m-integration-economics` | 4 | P3 (Monitor) | 1 | Already `Adoption: Partially Adopted` by MetaSystem (MCP servers in use). Single source, but MCP is validated independently elsewhere in the KB. Consider P2 review. |
| `meta-improvement-convergence-and-transfer-rates` | 4 | P3 (Monitor) | 1 | Single-paper (HyperAgents arXiv). |
| `metacognitive-self-modification-hyperagents` | 4 | P3 (Monitor) | 2 | HyperAgents + OpenAI cookbook. Close to criterion 1 threshold. `evidence_strength: Weak (theoretical)` — no production evidence yet. |
| `cross-platform-context-file-strategy` | 3 | P3 | 0 (sources field empty) | Cluster forming but sources field is empty — should be backfilled before re-evaluating. |
| `dag-vs-bsp-two-graph-based-orchestration-models` | 3 | P3 | 0 (sources field empty) | Same pattern — empty sources field. |

---

## Evidence Conflicts

One conflict worth Nick's attention:

- **`scheduled-tasks-for-real-time-context-maintenance`** — Delta report `2026-04-20-batch-2-delta-report.md` (line 127) states evidence_strength was upgraded Medium→Strong, but finding frontmatter still shows `Medium (practitioner-documented)`. Either the delta report is wrong about the intended change, or the change was dropped during Batch 2 commits. Candidate 2 above proposes fixing this by applying the upgrade.

No other conflicts detected.

---

## No-Change Review (19 of 21)

The following 19 Batch 2–updated findings were reviewed and confirmed at their current priority/evidence level. Most saw "second-source corroboration" — adding a second independent practitioner reference to a finding already well-positioned in the tier system.

| Finding | Current | Reason No Change |
|---------|---------|------------------|
| `agent-onboarding-via-interview-style-context` | P3, Medium | 2 sources, 4 related. 5-layer elicitation adds depth, not threshold-crossing independence. |
| `context-gap-task-vs-job` | P2, Strong | Already at strongest evidence and P2. New link added. |
| `agent-clarification-over-assumption-pattern` | P2, Strong | 2 independent sources (Anthropic + RoboNuggets/Karpathy). Already P2. |
| `agent-context-kiss-commandments-minimum-viable` | P1, Strong | Already at top priority. |
| `file-over-app-philosophy-for-knowledge-permanence` | P3, Strong | Still 1 source. Second-practitioner article cited inline but not added to sources list. |
| `spec-as-source-of-truth-for-agent-construction` | P3, Medium | 1 source. Amazon Kira reference adds color but not independent evidence. |
| `eval-driven-development-autonomous-quality` | P2, Medium | Already P2. "Spec→eval" mechanism is a clarification, not a new source class. |
| `archon-yaml-defined-harness-workflows` | P2, Medium | Already P2. 3 sources mostly same author (Cole Medin) = ~1 independent. |
| `anthropic-managed-agents-platform` | P2, Strong | Already P2 with Strong. 3 sources but largely Anthropic-origin. |
| `five-persistent-human-skills-agent-era-framework` | P3, Medium | 2 sources, both Nate B Jones = 1 independent author. |
| `org-redesign-for-agentic-throughput-high-speed-rail` | P3, Medium | 3 sources all Nate B Jones = 1 independent. No bump. |
| `planning-session-bias-separate-context-windows` | P2, Medium | Already P2. 2 independent sources (Archon + GStack). |
| `compounding-knowledge-loop-internal-data` | P1, Medium | Already P1. |
| `programmatic-tool-calling-code-orchestrated-tool-use` | P1, Strong | Already P1. |
| `mcp-as-code-api-progressive-tool-discovery` | P1, Strong | Already P1. |
| `claude-code-channels-telegramdiscord-as-agent-inte` | P2, Strong | Already P2. |
| `memory-decay-compaction-convergence` | P2, Medium | Already upgraded in 2026-04-19. Batch 2 correction was a misattribution fix, not evidence addition. |
| (already-applied findings) | | See "Already Applied" section |

---

## Distribution of Proposed Changes

| Tier | Count |
|------|-------|
| P2 (Design Required) bumps | 1 (`dark-factory-ai-only-codebase-management` from P3) |
| Evidence upgrades (Low→Medium) | 1 (`dark-factory-ai-only-codebase-management`) |
| Evidence upgrades (Medium→Strong) | 1 (`scheduled-tasks-for-real-time-context-maintenance` — correction) |
| Adoption status changes | 0 |
| Cluster-only flags | 6 |

---

## Notes for Next Scan

- **Single-author clusters:** Nate B Jones appears as sole author across multiple "org design" and "five skills" findings. These cluster naturally but cannot independently corroborate each other. Watch for a second-author source in this space before bumping.
- **Empty `sources:` fields:** `cross-platform-context-file-strategy` and `dag-vs-bsp-two-graph-based-orchestration-models` have empty sources lists. Backfill during next hygiene pass before they can be scored on Criterion 1.
- **`context-infrastructure-seven-level-maturity-model`:** This is the strongest-looking cluster flag — 6 extending findings. Nick should decide whether a hub finding with a single origin source warrants P2 purely on its architectural centrality.
