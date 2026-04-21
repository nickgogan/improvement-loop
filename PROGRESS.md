# Improvement Loop — Progress

**Last Updated:** 2026-04-21 (session 49)

**Note on tracking drift:** Sessions 17-21 were in the root PROGRESS.md. Sessions 22+ were supposed to be tracked here, but sessions 41-46 ended up in the root PROGRESS.md instead. Session 47 resumed correct tracking in this file. Per memory feedback, session-by-session narrative lives in `operations/system-log/`; this file carries current focus and pointers only.

## Current Focus

**Librarian reference layer is executable end-to-end. Next: design how the Librarian learns from use.**

Option α' (session 47) has been fully built out. Session 48 validated it empirically — four composition tests (3-guide agent slice, 7-guide agent audit, prompt audit, skill audit) all passed — and produced the first three exemplars (`harness.md`, `second-brain.md`, `audit.md`). Session 49 closed the substrate: 35 Librarian use cases canonicalized, a formal read-contract specified (10-step execution flow, 3-hop Tier-2 ceiling, Tier-3 consumer-request-gated), three more concept files (`agent.md`, `prompt.md`, `skill.md`), and three IL-scoped assessment skills (`assess-agent`, `assess-prompt`, `assess-skill` at `systems/improvement-loop/.claude/skills/`). `assess-prompt` is framed as an *extension over `/prompt-evaluator`* — not a parallel rubric — after mid-session Nick push-back on duplication.

**Session 50 focus (handoff prepared):** Owner persona. Primary task: design the Librarian boundary-case tracking mechanism — where encounter data (no concept match, ambiguous verb, hop-ceiling hit, KB gap, Tier-3 read) lives so Nick + Codifier can see patterns over time and prioritize next-wave authoring. Nick's session-49 annotation on read-contract §9 is the source question. Output lands in `governance/proposals/` (not `project-management/design-notes/`) per Nick's session-49-close decision that Owner-authored design artifacts belong in `governance/`; a companion DD proposal codifies that placement rule. Secondary stream: SL pattern-recognition on Nick's ad-hoc brief. Handoff at `operations/handoffs/handoff-prompt-session-50-owner-boundary-case-tracking.md`.

**Reference-layer authoring backlog (from use-case registry):**
- P2 concepts: `memory.md` (variants), `context-rot.md`. P2 operations: `diagnose.md`, `design.md`.
- P3 concepts: `agentic-systems.md`, `prompt-caching.md`, `mcp.md`. P3 operations: `decide.md`, `fetch.md`, `explain.md`, `whats-new.md`, `coverage.md`. P4: `plan.md`.
- Session 51+ Codifier scope after the boundary-case tracking design lands.

**Pipeline state unchanged from session 48:** `/research-loop` → `/identify-artifacts` → `/synthesize-guide` (absorbs non-pattern inlining per pipeline collapse proposal) → lift-and-deploy from `guide#anchor`. G7/G2/G9 re-syntheses remain gated on lifecycle-spec Phase-1 DDs.

---

## Watched Libraries State

| Library | Slug | Spectrum | Version | Analysis Status |
|---------|------|----------|---------|-----------------|
| GSD | `gsd` | wholesale | v1.33.0 | Done — `gsd-analysis.md` |
| Superpowers | `superpowers` | thin-wrapper | v5.0.7 | Done — `superpowers-analysis.md` |
| BMAD Method | `bmad-method` | cherry-pick | v6.2.2 | Done — `bmad-method-analysis.md` |
| OpenClaw | `openclaw` | cherry-pick | v2026.4.5 | Done — `openclaw-analysis.md` |
| Paperclip | `paperclip` | cherry-pick | v2026.403.0 | Done — `paperclip-analysis.md` |
| gstack | `gstack` | cherry-pick | v0.15.16.0 | Done — `gstack-analysis.md` |
| mem0 | `mem0` | evaluating | v1.0.11 | Done — `mem0-analysis.md` |

## What's Been Done

### Session 10 (2026-04-08) — Repo analyzer skill + first analyses

1. **Built `/repo-analyzer` skill** — 6-dimension structural analysis: structural inventory (with markdown composition), context file map (Chain-loader, Hook-injected mechanisms, sampling strategy), workflow topology, governance model, cross-agent protocol, research dimension mapping. Clones to `/tmp/metasystem-repo-cache/`, writes to `watched-libraries/analysis/`.
2. **Analyzed GSD** — 600 files, 341 MD (56.8%), 24 agents, 70 commands, 10 workflows. Three-layer context chain (command→workflow→agent). Hub-and-spoke orchestration. Four-gate taxonomy. 7 High-relevance dimensions. 5 findings candidates.
3. **Analyzed Superpowers** — 142 files, 75 MD (52.8%), 14 skills, 1 agent. Persuasion-engineered constraints (Meincke et al. 2025). Pull-model context loading (hook-injected bootstrap). Brainstorming as mandatory design-first gate. 7 findings candidates.
4. **Built `/promote-findings` skill** — Bridges analysis candidates into formal Research Findings KB entries. Dedup check, user-gated selection, bidirectional linking.
5. **Iteratively improved `/repo-analyzer`** — Added Markdown Composition table, Chain-loader mechanism, Hook-injected mechanism, sampling strategy, Research Dimension Mapping (6th dimension).

**Key insight:** GSD uses push-model context (harness pre-assembles via @-reference chains), Superpowers uses pull-model (agent self-activates skills on demand). Superpowers applies academic persuasion research to constraint design. Distinct approaches to the same problem (making agents follow rules).

### Session 12 (2026-04-08) — Handoff generation

- Evaluated and abandoned GitHub org watching mechanism (not needed)
- Generated handoff prompt for remaining analyses at `handoff-prompts/handoff-prompt-repo-analyses.md`

### Session 13 (2026-04-08) — Remaining 5 repo analyses

1. **Analyzed BMAD Method** — 559 files, 418 MD, 41 skills (30 phase + 11 core), 112 step files, 22 workflows. Everything-as-skill architecture. Step-file micro-architecture with sequential enforcement. Named agent personas (Mary, John, Winston, Amelia). Deterministic skill validator (27 rules). 7 findings candidates.
2. **Analyzed OpenClaw** — 13,216 files, 636 MD, 53 skills + 8 maintainer skills, ~100 bundled plugins. 6-file workspace taxonomy (SOUL/USER/AGENTS/TOOLS/HEARTBEAT/MEMORY). Pluggable context engine. Dreaming memory consolidation (Light→Deep→REM). Distributed AGENTS.md/CLAUDE.md symlink pairs. 7 findings candidates.
3. **Analyzed Paperclip** — 1,462 files, 184 MD, 10 skills, 7 adapters, 53 SQL migrations. Hierarchical org-chart orchestration (CEO→CTO/CMO/UXDesigner). Budget governance with hard-stop. Heartbeat execution model. Atomic checkout with 409 exclusion. PARA-based file memory. 7 findings candidates.
4. **Analyzed gstack** — 413 files, 90 MD, 41 skills (38 templates), 8 host configs, headless browser daemon. Template-generated skills with multi-host variants. ETHOS.md as philosophical constitution. Review Army parallel specialist dispatch. Three-tier eval system. 7 findings candidates.
5. **Analyzed mem0** — 1,927 files, 441 MD+MDX, 78 providers (24 LLM + 30 vector + 15 embedding + 4 graph + 5 reranker). Triple storage architecture (vector+graph+SQLite). Scoped memory model (user/agent/run). Library/service, not agent framework. 5 findings candidates.
6. Generated handoff prompt for cross-repo comparison at `handoff-prompts/handoff-prompt-cross-repo-comparison.md`

**Key insight across all 7 repos:** Seven distinct context loading mechanisms, seven distinct orchestration patterns, and fundamentally different approaches to agent identity. The ecosystem has not converged on patterns yet — comparison will reveal which approaches are emerging conventions vs. unique innovations.

### Session 14 (2026-04-08) — Cross-repo comparison

1. **Produced cross-repo comparison** — `cross-repo-comparison.md` comparing all 7 repos across 6 dimensions. Key outputs:
   - Comparison matrices for structural scale, context loading, orchestration, governance, and agent design
   - Special focus: brainstorming/critical thinking skills across Superpowers vs BMAD vs GSD vs gstack
   - Orchestration spectrum from manual (BMAD) to autonomous (Paperclip)
   - Three governance philosophies: structural, psychological, economic
   - Push vs pull context loading tradeoff analysis
   - Pattern clusters: 10 shared patterns, 14 unique patterns, 9 contradictory approaches
   - 8 cross-repo findings candidates (CR-1 through CR-8)
2. Updated analysis index with cross-repo comparison entry

**Key insight:** The ecosystem has NOT converged on context loading, orchestration, or governance patterns. Seven repos, seven distinct approaches to each. The three deepest divergences: push vs pull context loading, structural vs psychological vs economic governance, and ephemeral vs persistent agent identity. These are genuine architectural tradeoffs, not immature ecosystem noise.

### Session 14 (continued) — Findings promotion + handoff

1. **Promoted 47 findings** into Research KB via `/promote-findings all` — 32 new, 15 partial matches with `related_findings` links, 4 duplicates skipped (Four-gate taxonomy, Deterministic skill validator, Org-chart orchestration, Review Army), 2 cross-repo candidates merged into individual findings (CR-6→anti-bias, CR-7→rationalization prevention).
2. **Updated findings index** with 47 new entries. KB now at ~370 findings.
3. **Added bidirectional links** — 48 promotion back-links across all 8 analysis docs.
4. **Filed SL entry** — `repo-analysis-pipeline-complete-47-findings-promoted.md`
5. **Generated handoff** for next session: research-loop final batch + crosslink pass.

### Session 15 (2026-04-09) — Final research batch + source processing

1. **Processed 12 unique videos** via `/research-loop` with transcript-based deep extraction (Pass 2). 3 already in KB (FtCdYhspm7w, 7huCP6RkcY4, OSZdFnQmgRw — corroboration only). 9 new source entries created.
2. **Extracted 13 new findings** across 7 categories: Prompt Craft (1), Orchestration (3), Evaluation (3), Tool Integration (3), Agent Design (1), Governance (1), Model Selection (1). Plus 1 update to existing Hybrid Retrieval Pattern finding.
3. **Updated 3 authorities** — Nate B Jones (source_count 5→6), Cole Medin (1→3), Chase AI (5→7).
4. **KB state:** 382 findings, 85 sources, 3 P1 findings (worktree isolation, ultra review, advisor-executor).
5. **Delta report** at `operations/loop-reports/2026-04-09-delta-report.md`.

**Key findings this session:**
- **Harness engineering maturation** — Archon (YAML workflow DAGs), Stripe Minion (1,300 AI PRs/week), 40% of Claude Code is harness code. PR acceptance: 6.7% raw → 70% harnessed.
- **Conway persistent agent** — Leaked always-on agent with extension format, triggers, behavioral context lock-in. Anthropic speedrunning the Microsoft 90s platform strategy.
- **Ultra Review verification pipeline** — Find→verify→dedup with independent verifier. Cross-model verification (Claude + Codex) catches model-specific blind spots.
- **Advisor-Executor API** — Opus advises, Sonnet executes. Better benchmarks at lower cost ($0.96 vs $1.89/task).
- **Brevity constraints** — Research paper shows forcing conciseness improves LLM accuracy by 26 percentage points on some problems.

### Session 16 (2026-04-09) — Crosslink pass + proposer review

1. **Crosslink pass on 60 new findings** (13 from session 15 + 47 from session 14 repo analyses). 800 candidate pairs evaluated via 16 parallel Sonnet subagent batches.
2. **71 crosslinks written** to 71 finding files after hub trimming (4 links) and post-write validation (12 removals/reclassifications).
3. **Post-write validation** — 2 Sonnet subagents with full-text reads checked all 16 enables/extends/contradicts links + 10 stratified same-problem samples. Error rates: enables 33%, extends 33%, same-problem 60% (consistent with calibration). All WRONG/BORDERLINE links fixed.
4. **Coverage impact:** Isolated findings 89→73 (-16). Total crosslinks 1078→1220 (+142). Evaluation category zero-link rate 15.7%→7.8%.
5. **Final type distribution:** 63 same-problem, 4 extends, 3 enables, 1 contradicts.
6. **Research-proposer skill** confirmed already built (348-line spec at `.claude/skills/research-proposer/SKILL.md`). No build work needed.
7. **Crosslink report** at `operations/loop-reports/2026-04-09-crosslink-report.md`.

**Key observations:**
- **Verification cluster emerged** — builder-validator, cross-model-verification, ultra-review, llm-as-judge, qa-agent, two-stage-review, and verification-7-patterns form a tightly interconnected verification/quality cluster spanning Evaluation and Orchestration categories.
- **Archon as orchestration hub** — 10 same-problem links connecting archon to GSD, BMAD, superpowers, planner-executor, phase-task, and other orchestration frameworks. Confirms the "everyone solving the same problem differently" insight from session 14.
- **Conway connected to persistent agent cluster** — links to KAIROS, IDE-first, scheduled-task-dashboard. But many proposed links were false positives (Conway→Playwright, Conway→Skill.md format) due to scope mismatch.

## What Still Needs Work

### Session 48 execution scope (Codifier — Librarian reference layer build)

Handoff at `operations/handoffs/handoff-prompt-session-48-codifier-librarian-reference-layer-build.md`. Six phases, gate at each:

1. **Phase 1 — Contract-section spot-check** on G1+G2+G10 to validate Option α' (invariants compose into agent-audit rubric?). Outcome gates the rest. If pass: α' holds. If fail: escalate to view artifacts for assessment use cases.
2. **Phase 2 — `research-dimensions.md` rewrite:** Researcher-specific preamble + Agentic OS → Agentic Systems rename. Update `guide-routing-table.md` Agentic OS references.
3. **Phase 3 — Three exemplar files** in `operations/references/librarian/`: `harness.md` (concept, no variants), `second-brain.md` (concept, three variants: human / AI / hybrid), `audit.md` (operation). Plus `_index.md`.
4. **Phase 4 — Librarian use-case registry** under (concept, operation) decomposition. Map 35 session-46 use cases onto file pairs.
5. **Phase 5 — Librarian read-contract design:** three-tier access formalization, confidence/provenance protocols, consumer input handling.
6. **Phase 6 — Three assessment skill SKILL.md drafts:** `/assess-prompt`, `/assess-agent`, `/assess-skill` as load-and-apply wrappers over (audit operation × concept file).

### Pending Nick decisions (carried)

- Review session-47 design notes at v2 state (substrate audit + collapse proposal).
- Session-45 identification Status fields — 4 guided-tier + 8 auto-tier entries still pending APPROVED/REJECTED/REDIRECTED.
- Session-46 Phase 1 lifecycle-spec DDs (DD-X1, DD-X3, DD-X4) — approval unblocks G7/G2/G9 re-syntheses.
- Terminology check: "curator" usage — confirmed as Codifier unless rename intended.

### Blocked / paused

- Re-synthesize G7 Memory (+11), G2 Context (+3), G9 Governance (+4) — blocked on lifecycle-spec Phase 1 DD approval.
- Deploy 11 guides from `extracts/guides/` to `meta-system/knowledge/guides/` — paused pending pipeline-collapse decision.
- Deploy non-pattern extracts — paused; under collapse proposal these become migration-into-guides candidates per Phase M1 audit.
- Retroactive migration/retirement of ~26 existing non-guide/non-pattern extracts + ~57–62 inline-candidate patterns — analysis-only in session 48 if scope allows.

### Secondary / IB candidates

- DD-78 amendment (Contract sections' dual role under α') — defer until Phase 1 spot-check outcome.
- DD-82 amendment (Librarian's expanded role) — defer until reference layer is exercised.
- References-by-agent reorg IB — mirror `librarian/` with `researcher/` and `codifier/` subfolders; update skill path refs in `/identify-artifacts`, `/synthesize-guide`, `/research-loop`. Author IB in session 48; execute in session 49+.

### Long-tail carry-forward (pre-session-41)

- OB1 repo analysis (watched library queued as 8th).
- P3 identification — 63 findings at Monitor priority per DD-72.
- `feedback/` taxonomy — structure for IL feedback directory.
- Unified processed-findings tracking — current dedup has gaps.
- Temp directory cleanup — `/tmp/metasystem-repo-cache/`.

## What Changed Sessions 22-28

Sessions 17-21 are in the root PROGRESS.md. Summary of sessions 22-28:

- **Session 22** — Router calibration complete (50 findings). 5 DDs filed (DD-75-79). ContractSpec universal layer (DD-78).
- **Session 23** — Pipeline simplified (DD-80). `/research-proposer` deprecated. `/identify-artifacts` and `/extract-artifacts` built. `extracts/` staging area created.
- **Session 24** — Subagent prompt improved via `/prompt-evaluator` + `/prompt-enhancer`. Validation: 14/14 (100%). Full P1 identification: 75 findings classified.
- **Session 25** — Full P1 extraction: 75 artifacts. Pipeline redesigned (DD-81): patterns → `/synthesize-guide`, non-patterns → `/extract-artifacts`. Guide routing table created with 8 clusters (G1-G8).
- **Session 26** — All 8 guide clusters synthesized (G1-G8). 70 findings consumed, ~18,600 words. Cross-reference pass: 27 inter-guide references added.
- **Session 27** — P2 identification complete: 120 findings classified. G9 (Governance) and G10 (Agent Design) candidate clusters detected. Operations directories restructured.
- **Session 28** — P2 non-pattern extraction: 19 artifacts staged. `extracted-artifacts/` → `extracts/`, `knowledge/` → `operations/references/`. 2-headed agent architecture proposed (Researcher + Codifier), deferred.

### Sessions 37-40 (Batch 1 & 2 research loop)

- **Session 37** — Batch 1: 14 YouTube videos processed via Pass 2 deep extraction. 38 new findings across 11 dimensions (including new Agentic OS dimension, DD-87). Delta report + SL entry.
- **Session 38** — Batch 2 transcript acquisition. Built Playwright + yt-dlp backends for transcript fetcher.
- **Session 39** — Batch 2 triage: 15 sources evaluated, 13 approved for extraction, 2 skipped (#17 product demo, #21 model release news). All 13 transcripts committed.
- **Session 40** — 2 new YouTube videos processed. 1 new finding (`five-pillar-agentic-os-framework.md`, P2, Agentic OS), 4 existing findings updated. Transcript fetcher enhanced with `parse_transcript_html()` for manual HTML fallback. OB1 repo queued as 8th watched library.

### Sessions 41-46 (tracked in root PROGRESS.md — backfill from SL entries when needed)

High-level summary derived from `operations/system-log/` and root PROGRESS.md. For detail, consult SL entries and handoff prompts.

- **Session 41** — Batch 2 extraction handoff prep.
- **Sessions 42-44** — Batch 2 extraction and subsequent identification runs. Session 44 staged 26 non-pattern extracts across rules/skills/templates/agents.
- **Session 45** — Researcher final-batch intake: 12 new findings (Memongo cluster, Anthropic session-management blog, UC Berkeley papers, Simon Willison walkthroughs).
- **Session 46 (Codifier)** — Session-45 identification (91.7% pattern rate). Produced artifact **lifecycle spec** (9 proposed DDs) + artifact **acceptance rubric** (3 more DDs). Librarian use-case registry draft (35 use cases / 9 categories). G7 / G2 / G9 re-syntheses gated on lifecycle-spec Phase 1 DDs.
- **DD-82** (IL 4-agent architecture) and **DD-86** (Owner responsibility) filed somewhere in this window. 4-agent team (Owner / Researcher / Codifier / Librarian) operational.
- **KB growth during gap:** ~499 → 545 findings; 7 → 16 watched libraries; 8 → 11 guides (G9 Governance and G10 Agent Design synthesized; G3b Workflow added).

### Session 47 (Codifier — Pipeline Collapse + Substrate Audit)

- Produced **pipeline collapse proposal** (`project-management/design-notes/2026-04-20-pipeline-collapse-proposal.md`). Retire standalone non-pattern extract directories. `/extract-artifacts` retires as user-invocable. `/synthesize-guide` absorbs full responsibility. DD-X9 obviated. 4 new proposed DDs (section manifest, deploy-by-anchor, anchor stability, `/extract-artifacts` deprecation).
- Produced **substrate audit** (`project-management/design-notes/2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md`) in response to Nick's ultrathink challenge on whether the taxonomy chain supports Librarian use cases. v1 recommended Option α (view artifacts). v2 (post-interview) replaced with Option α' — **Librarian reference layer** (concept files + operation files as pointer artifacts) + **three-tier access** (guides → patterns+findings graph → watched-library repos).
- **Interview-resolved:** dimensions reframe-only (Agentic OS → Agentic Systems, no Harness dimension); "consumer artifacts" framing dropped in favor of (concept, operation) decomposition; variants as first-class optional field for Agent, Memory, Second Brain (three variants: human / AI / hybrid).
- Collapse proposal's Librarian Read Contract section trimmed (v2) to point to the substrate audit; section manifest retained as agreed mechanism for anchor stability + deploy metadata.
- Session 47 SL entry + session 48 handoff prompt written.
- **Deferred to session 48:** Contract-section spot-check to validate Option α', `research-dimensions.md` rewrite, three exemplar reference files (harness, second-brain, audit), Librarian use-case registry under new decomposition, read-contract design, three assessment skill drafts.

## KB Totals (as of session 47)

545 findings, 136 sources, 70 authorities, 11 research dimensions, 16 watched libraries. 11 guides synthesized (G1-G10 + G3b). ~109 artifacts staged in `extracts/` (11 guides + 72 patterns + 9 rules + 11 skills + 4 templates + 2 agents). Under collapse proposal, `extracts/` would shrink to ~30-40 (guides + ~10-15 cross-cutting patterns) post-migration.

## Key Files

| Entity | Path |
|--------|------|
| Next session handoff | `operations/handoffs/handoff-prompt-session-48-codifier-librarian-reference-layer-build.md` |
| Session 47 SL entry | `operations/system-log/session-47-codifier-pipeline-collapse-substrate-audit-librarian-reference-layer.md` |
| Pipeline collapse proposal | `project-management/design-notes/2026-04-20-pipeline-collapse-proposal.md` |
| Substrate audit | `project-management/design-notes/2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md` |
| Artifact lifecycle spec (session 46) | `project-management/design-notes/2026-04-20-artifact-lifecycle-spec.md` |
| Artifact acceptance rubric (session 46) | `project-management/design-notes/2026-04-20-artifact-acceptance-rubric.md` |
| Session 45 identification report | `operations/pattern-identification-reports/2026-04-20-session-45-identification-report.md` |
| Guide routing table | `operations/references/guide-routing-table.md` |
| Research dimensions | `operations/references/research-dimensions.md` |
| Form classification rubric | `operations/references/form-classification-rubric.md` |
| Staged extracts | `extracts/` |
| Research findings | `research-findings/` |
| Watched libraries registry | `watched-libraries/_index.md` |
| IL agent definitions | `agents/{owner,researcher,codifier,librarian}/agent.md` |
| IL CLAUDE.md | `CLAUDE.md` (at system root) |
