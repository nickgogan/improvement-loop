# Improvement Loop — Progress

**Last Updated:** 2026-04-20 (session 40)

## Current Focus

**Batch 2 extraction in progress. 2 new videos processed (session 40). OB1 repo analysis + 13 remaining Batch 2 sources next.**

**Pipeline state:**
```
/research-loop (intake)  →  /identify-artifacts  →  /extract-artifacts  →  /synthesize-guide  →  [deploy]
     done (sessions 15-16)    done (sessions 24,27)   done (sessions 25,28)   partial (G1-G8 done, G9-G10 next)
```

**Note:** Sessions 17-21 were recorded in the root PROGRESS.md. From session 22 onward, IL session updates are tracked here.

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

1. **OB1 repo analysis** — New watched library (`https://github.com/NateBJones-Projects/OB1`). Analyze + promote findings.
2. **Batch 2 extraction** — 13 sources approved, not yet extracted. Process in parallel waves.
3. **P2 guide synthesis** — Check G1-G8 staleness from P2 deltas, synthesize G9 (Governance) and G10 (Agent Design)
4. **Deploy staged artifacts** — 8 guides + 5 P1 non-patterns + 19 P2 non-patterns in `extracts/`
5. **Design IL agents** — Researcher and Codifier agent definitions using the guides (deferred until guides complete)
6. **P3 identification** — 63 findings at Monitor priority per DD-72
7. **feedback/ taxonomy** — Structure for the new IL feedback directory
8. **Unified processed-findings tracking** — Current dedup mechanisms work but have gaps
9. **Temp directory cleanup** — Design cleanup for `/tmp/metasystem-repo-cache/` (repo-analyzer) and transcript fetcher temp files. Consider automated cleanup, TTL pruning, or manual skill.

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

## KB Totals (as of session 40)

~499 findings, 121 sources, 11 research dimensions. 7 watched libraries (OB1 pending as 8th). P1 (75) and P2 (120) fully classified. 94 artifacts staged in `extracts/` (75 P1 + 19 P2). 8 guides synthesized (G1-G8), 2 pending (G9-G10).

## Key Files

| Entity | Path |
|--------|------|
| Staged extracts | `extracts/` |
| Guide routing table | `operations/references/guide-routing-table.md` |
| Research dimensions | `operations/references/research-dimensions.md` |
| Form classification rubric | `operations/references/form-classification-rubric.md` |
| P2 identification report | `operations/pattern-identification-reports/2026-04-19-identification-report-4.md` |
| Research findings | `research-findings/` |
| Watched libraries registry | `watched-libraries/_index.md` |
| Next session handoff | `operations/handoffs/handoff-prompt-p2-guide-synthesis.md` |
