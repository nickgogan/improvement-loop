---
title: "Priority Reassessment Report — 2026-04-23"
type: "research-report"
category: "priority-reassessment"
created: "2026-04-23"
author: "improvement-loop"
agent: "Codifier"
ib_item: "IB-149"
session: 62
findings_scanned: 27
candidates_flagged: 4
---

# Priority Reassessment Report — 2026-04-23

**Scope:** IB-149 retroactive priority re-evaluation. Primary scope: 4 session-57 candidates pre-flagged during `/promote-findings`. Extended scope: 17 session-58 findings + 6 session-59 findings (per IB-149 optional extension).

**Posture:** Conservative per skill rules. Thresholds are evaluated strictly — "3+ independent sources → P2; 5+ independent sources with production evidence → P1." Proposals, not changes. Nick gates before any frontmatter writes.

---

## Summary

| Metric | Count |
|---|---|
| Findings scanned (primary scope) | 4 |
| Findings scanned (extended scope) | 23 (17 session-58 + 6 session-59) |
| Reassessment candidates (Criteria 1–5 met) | 4 |
| Proposed priority bumps | 3 |
| Proposed hold (with rationale) | 1 |
| Proposed evidence_strength upgrades | 0 |
| Proposed adoption_status changes | 0 |
| Cluster-level flags (Criterion 5) | 1 |
| Scope-adjacent drift observations | 2 |

---

## Candidates

### 1. `cross-platform-context-file-strategy` → **PROPOSE P3 → P2**

- **Current priority:** P3
- **Proposed priority:** P2
- **Criteria triggered:** Criterion 4 (Convergent Implementation)
- **Evidence summary:**
  - **Independent repos exhibiting the pattern:** 4
    - Archon (coleam00) — platform-specific mirroring
    - n8n (n8n-io) — chain-loader indirection
    - LangGraph (langchain-ai) — content duplication
    - MemPalace (MemPalace) — symlink (via `extended-by` link to `universal-harness-context-via-symlink`)
  - **Independent orgs:** 4 (no shared ancestry)
  - **Production evidence:** All four are public releases with version tags
  - **Related findings:** 5 (three `extends`, one `same-problem`, one `extended-by`)
- **Rationale:** Criterion 4 threshold is 3+ independent implementations → bump one tier. 4 independent orgs, each with a materially different strategy, is textbook convergent interest in the problem. Session 57's addition of `universal-harness-context-via-symlink` as a 4th strategy confirms the design space is non-trivial. P3 → P2 is the skill-strict reading.
- **Skill compliance:** Conservative — proposes one tier, not two.

Nick: Agreed.

---

### 2. `specification-as-governance-fourth-enforcement-philosophy` → **PROPOSE HOLD at P2** *(tension with IB-149)*

- **Current priority:** P2
- **IB-149's stated candidacy:** P2 → P1
- **Proposed priority:** **P2 (hold)** — with flag for future P1 re-evaluation
- **Criteria triggered:** Criterion 1 (partial — evidence accumulated but below P1 threshold)
- **Evidence summary:**
  - **Independent repos exhibiting the pattern:** 3
    - LangGraph (langchain-ai) — `libs/checkpoint-conformance/` conformance test suite
    - n8n (n8n-io) — spec-driven development skill with bidirectional sync
    - MemPalace (MemPalace) — declared_transformations + conformance tests (via `extended-by` link to `declared-transformations-contract-conformance`)
  - **Independent orgs:** 3
  - **Production evidence:** Yes across all three (LangGraph checkpoint implementations shipped; n8n skill in active engineering use; MemPalace spec as loaded contract)
  - **Related findings:** 4 (two `extends`, one `same-problem`, one `extended-by`)
- **Rationale:** Skill threshold for P1 is explicit — "5+ independent sources with production evidence → propose P1." Current evidence is 3 independent sources with production evidence. This is the P2 threshold, not P1. Bumping to P1 on 3 sources would set a precedent that erodes the skill's conservatism rule.
- **Disagreement with IB-149's framing:** IB-149 asserts "3+ threshold reached; candidate for P2 → P1." The skill's 3+ threshold is for P3/null → P2, not P2 → P1. This is a rubric-vs-note discrepancy that benefits from Nick's call.
- **Recommendation:** Hold at P2. Revisit when a 4th–5th independent repo surfaces specification-based enforcement in production (e.g., a future watched-library analysis). Tracking lever: add this finding to a cross-link pass watching for new conformance-suite or spec-driven patterns.
- **Alternative if Nick overrides the skill threshold:** If Nick judges production-deployment weight > source count, apply P2 → P1.

Nick: Agreed.
---

### 3. `importance-based-decay-permanent-exemption` → **FLAG (Criterion 5 cluster)** — conditional bump to P2

- **Current priority:** P3
- **Proposed priority:** Conditional — **P3 → P2 if decay design-space is prioritized**; otherwise hold at P3
- **Criteria triggered:** Criterion 5 (Related Findings Cluster) — cluster of 3 same-problem decay strategies; skill rules explicitly require human judgment on cluster-level bumps
- **Cluster contents (decay design-space):**
  | Finding | Current priority | Repo | Org |
  |---|---|---|---|
  | `importance-based-decay-permanent-exemption` | **P3** | Memongo | romiluz13 |
  | `surprisal-novelty-as-memory-write-gate` | **P2** | Memongo | romiluz13 (same org) |
  | `content-derived-temporal-expiration-contradiction-resolution` | **null** | Supermemory | supermemoryai |
- **Independent orgs in cluster:** 2 (romiluz13 Memongo, supermemoryai Supermemory)
- **Evidence summary:** The three findings are framed as complementary, not competing — the Supermemory finding explicitly presents a three-row table mapping the decay design-space. Cluster coherence is high, but independent-source count is low (2 orgs, not 3+).
- **Rationale for conditional proposal:**
  - Skill Criterion 5 flags clusters for human judgment; does not auto-propose a bump.
  - If Nick prioritizes decay as a design-space MetaSystem needs to land (e.g., for Household OS memory), normalize cluster priorities to P2. This triggers three moves: `importance-based-decay` P3 → P2, `content-derived-temporal` null → P2, and `surprisal-novelty` stays at P2.
  - If decay design-space is not a current priority, hold all three at current values (cluster recognition is noted in the finding bodies already; no frontmatter change required to preserve the knowledge).
- **Sub-observation:** The `content-derived-temporal-expiration` finding has `priority: null` — unclassified. Independent of this cluster call, that finding should be priority-assigned via `/identify-artifacts` as a baseline (see Scope-Adjacent Drift §2 below).

Nick: Now this is an interesting proposal. As you know, I'm sure, the ironic characteristic essence of human memory is that it is extremely selective. In other words, forgetting is actually cited as far more important than remembering. We are going to need to figure out some sort of a reasonable compression, compaction, forgetting memory solution here, and this would be an interesting research dimension to evolve actually. I would like to keep an eye on this one.

---

### 4. `memory-bank-isolation-per-agent-per-project` → **PROPOSE P3 → P2**

- **Current priority:** P3 (Monitor)
- **Proposed priority:** P2
- **Criteria triggered:** Criterion 4 (Convergent Implementation)
- **Evidence summary:**
  - **Independent orgs addressing multi-tenancy/isolation at the memory layer:** 3
    - Hindsight (Okhlopkov) — `bankId`, `HINDSIGHT_CHANNEL_ID`, `HINDSIGHT_USER_ID` as first-class primitives
    - mem0 — typed three-dimensional scoping (`user_id`, `agent_id`, `run_id`) via `scoped-memory-model` (same-problem link)
    - Supermemory (supermemoryai) — `containerTag` hierarchy via `hierarchical-container-tag-multi-tenancy` (same-problem link)
  - **Related findings:** 9 `same-problem` links — one of the densest clusters in the KB
  - **Convergence quality:** Three distinct implementation styles (per-bank, typed-dimension, flat-tag-hierarchy) solving the same architectural problem
- **Rationale:** Criterion 4 threshold is 3+ independent implementations → bump one tier. The pattern appears independently in 3 unrelated orgs with three distinct technical approaches — genuine convergent implementation, not copy-paste. P3 → P2 is skill-strict.
- **Adjacent consideration:** The MetaSystem application is direct (per-system memory boundaries map to DD-55/DD-56/DD-59 system scope). Criterion 3 (Adoption Signal) is **not** triggered — MetaSystem has not yet adopted a memory-isolation pattern. No `adoption_status` change proposed.

Nick: Agreed.
---

## Scope-Adjacent Drift Observations

*IB-149 instructed: "If reassess surfaces drift in other areas, flag it in the report but don't fix it in this session."*

### Drift §1: 17 session-58 findings at `priority: null, pipeline_status: raw`

All 17 findings promoted during session 58 (Buckets A + B) have `priority: null`. The `/promote-findings` skill wrote them as `raw`, with no priority assignment. Per `/reassess-priorities` scope rules, these are **not** reassessment candidates — they need initial classification via `/identify-artifacts`, which is a separate Codifier skill.

**Affected findings (17):**
`external-benchmark-hosting-as-trust-mechanism`, `benchmark-dataset-deprecation-lifecycle`, `experimental-sandbox-labeling-discipline`, `ensemble-eval-majority-required-for-success`, `production-configuration-baseline-discipline`, `agentic-search-memory-retrieval-architecture`, `confirm-failure-first-tdd-agent-discipline`, `personal-knowledge-hoard-as-agent-substrate`, `interactive-explanations-extend-linear-walkthroughs`, `subagent-scope-priority-ladder`, `inline-scoped-mcp-servers-per-subagent`, `subagent-persistent-memory-directory`, `capability-restricted-agent-spawning-via-allowlist`, `subagent-isolation-contract`, `foreground-vs-background-subagent-permission-models`, `five-durable-verticals-ai-cannot-replace`, `agent-native-app-store-emerging-category`.

**Recommended follow-up:** Dedicated `/identify-artifacts` run over this batch to assign priority + form classification before they're candidates for any reassessment pass. Filed as a pointer for a future session, not fixed in-session.
- Nick: Agreed.

### Drift §2: `content-derived-temporal-expiration-contradiction-resolution` has `priority: null`

This session-57 finding participates in the decay cluster (see Candidate 3) but was never priority-assigned. Baseline expectation is P3 given standalone evidence (1 repo: Supermemory) and single-org sourcing. Out-of-session fix: `/identify-artifacts` pass covering this finding.
- Nick: Agreed. 

---

## Extended-Scope Observations — Session 58 & 59 Findings

- **Session 58 (17 findings):** Out of scope for this skill — see Drift §1.
- **Session 59 (6 findings):** Priority-assigned at promote-time (4 × P2, 2 × P3). All are single-repo-sourced and 1 day old — no evidence-accumulation signal per Criterion 1 (3+ sources required). None surface as reassessment candidates this session.
  | Finding | Priority | Sources | Verdict |
  |---|---|---|---|
  | `stripe-machine-payments-protocol-agent-economy` | P3 | 1 | No bump — single source |
  | `sandbox-architecture-by-threat-model-microvm-vs-container` | P2 | 1 | Already P2 — no Criterion 1 trigger |
  | `model-native-context-window-awareness` | P2 | 1 | Already P2 |
  | `shell-injection-vector-taxonomy-agent-bash-security` | P2 | 1 | Already P2 |
  | `framework-tension-taxonomy-superpowers-gsd-gstack` | P2 | 1 | Already P2 |
  | `audit-skill-as-expert-harness-distribution-channel` | P3 | 1 | No bump — single source |

---

## Proposed Changes (Frontmatter Edits, Pending Approval)

If approved by Nick, these edits will be applied with `last_updated: "2026-04-23"`. No body content will be modified.

| # | Finding | Field | Current | Proposed |
|---|---|---|---|---|
| 1 | `cross-platform-context-file-strategy` | `priority` | `P3` | `P2` |
| 2 | `memory-bank-isolation-per-agent-per-project` | `priority` | `"P3 (Monitor)"` | `P2` |
| 3 | `specification-as-governance-fourth-enforcement-philosophy` | `priority` | `P2` | `P2` *(hold)* |
| 4a | `importance-based-decay-permanent-exemption` | `priority` | `P3` | `P2` *(conditional on Nick)* |
| 4b | `content-derived-temporal-expiration-contradiction-resolution` | `priority` | `null` | `P2` *(conditional on Nick; cluster normalization)* |
| 4c | `surprisal-novelty-as-memory-write-gate` | `priority` | `P2` | `P2` *(no change; already at cluster level)* |

---

## Open Questions for Nick

1. **On Candidate 2** (`specification-as-governance-fourth-enforcement-philosophy`): the skill rubric says P2 hold at 3 sources; IB-149 says P2 → P1. Which governs — skill rubric or the IB-149 note's read? Recommendation: hold at P2 per rubric; re-evaluate when 4th–5th independent repo surfaces.

2. **On Candidate 3 cluster** (decay design-space): is memory decay a MetaSystem design-space priority right now (e.g., for Household OS)? If yes, normalize cluster priorities to P2. If no, hold and track. Nick: Not a huge priority right now 
- Nick: Not a huge priority right now, but I want this as a research sub-dimension of some kind. Can you write the taxonomy of our research dimensions please? 

3. **On Drift §1** (17 null-priority session-58 findings): should a `/identify-artifacts` run over these be queued as its own IB item? Not fixing in this session; flagging as next-up Codifier work after IB-149 closes.
- Nick: Nah, lets try to do the work in the same session.
---

## Methodology Notes

- **Sources counted by org, not by file.** Three findings all sourced from the same author's repos count as one independent source.
- **Production evidence** defined as: public release with version tag, documented production usage, or active team/engineering use.
- **Reciprocal links in session 58** added relatedness among findings but not new independent repo sources — reciprocal links are re-indexing existing evidence, not adding corroboration.
- **Cluster definition** (Criterion 5): 3+ `extends`/`enables` relationship types. `same-problem` links were counted leniently in this report (Candidate 4) where the convergence is on the architectural problem, not a hierarchical relationship — noted explicitly for Nick.

---

## Next Actions on Approval

1. Apply approved frontmatter edits via `Edit` tool — `priority` (and cluster members per Candidate 3 decision) + `last_updated: "2026-04-23"`.
2. Update `IB-149` frontmatter: `status: Done`.
3. File SL entry at `systems/improvement-loop/operations/system-log/session-62-codifier-ib-149-reassess.md` logging the reassessment, decisions taken, and open follow-ups (Drift §1 especially).
4. If Drift §1 is formalized as a new IB, create the IB file under `systems/improvement-loop/project-management/implementation-backlog/`.

---

## Report Provenance

- **Scanned:** `systems/improvement-loop/research-findings/*.md` (targeted subset per IB-149 scope)
- **Evidence sources cross-checked:** IB-149 assertions, finding frontmatter (`sources`, `related_findings`), finding body evidence claims
- **Analysis docs:** Not re-read in this pass — IB-149 provides explicit repo attribution for the primary candidates; analysis-doc corroboration deferred unless Nick requests deeper grounding.
- **Skill contract:** `systems/improvement-loop/.claude/skills/reassess-priorities/SKILL.md`
- **Session:** 62 — Codifier role (per handoff-prompt-session-62)
