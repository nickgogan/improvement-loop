---
name: "Next Scan Notes"
last_updated: "2026-04-23 (session 59 close)"
---

# Next Scan Notes

Carry-forward from session 45 (final batch intake: Memongo + Claude Code session mgmt + 2 arXiv + Simon Willison). Updated session 56 (2026-04-22→23): Memongo Pass 2 analysis landed; LongMemEval leaderboard source located (name corrected MemPalace ≠ Mampalace). Locate-pass intel captured as prose bullet here rather than as a `status: "Queued"` research-source entry, per create-when-processed convention.

## Specific Items to Investigate

### Memongo-related (highest priority for Nick's active work)

- ~~**Memongo companion documentation** — `PRODUCTION-READY.md`, `docs/benchmarks/benchmark-operating-contract.md`, `docs/platform/self-host.md`, and the referenced `MAINTAINER-MAP.md` are referenced but not in the README body. Strong Pass 2 extraction candidates — run `/repo-analyzer` on `watched-libraries/memongo.md` to surface them.~~ — **RESOLVED session 56 (2026-04-22).** Pass 2 analysis landed at `watched-libraries/analysis/memongo-analysis.md`. Six finding candidates surfaced (not promoted); strongest is the Benchmark Operating Contract pattern. `/promote-findings` pending Nick review of the analysis.

- ~~**LongMemEval leaderboard source cluster**~~ **RESOLVED session 58 (2026-04-23).** All 6 URLs processed as research-sources; UCSB LongMemEval team, REM Labs, and Vectorize added as authorities. 6 new findings promoted: external-benchmark-hosting-as-trust-mechanism, benchmark-dataset-deprecation-lifecycle, experimental-sandbox-labeling-discipline, ensemble-eval-majority-required-for-success, production-configuration-baseline-discipline, agentic-search-memory-retrieval-architecture. mempalace.tech skipped as confirmed scam domain per session 57. Notable observation from session 58: REM Labs leaderboard composition has shifted materially in ~3 weeks since session 56 snapshot (MemPalace no longer listed; AgentMemory and Chronos are new entries). Dataset deprecation (xiaowu0162/longmemeval → longmemeval-cleaned) now documented as a governance finding. Original data retained below for historical reference:

**LongMemEval leaderboard source cluster — original capture (session 56):**
  - **Entity name correction:** MemPalace, not Mampalace. Domain: `mempalace.tech`.
  - **No official leaderboard exists.** REM Labs' aggregator states this explicitly: *"LongMemEval has no official leaderboard."* All rankings are self-reported or third-party compiled.
  - **Authoritative source cluster (process together on scan):**
    - `https://remlabs.ai/benchmarks` — most complete comparative table; REM Labs is itself a ranked system (mild conflict-of-interest).
    - `https://www.mempalace.tech/benchmarks` — MemPalace's own benchmark page; primary source for the 96.6% raw / 100% hybrid / 98.4% held-out numbers.
    - `https://supermemory.ai/research/` — Supermemory's ~85% on gpt-4o run.
    - `https://supermemory.ai/blog/we-broke-the-frontier-in-agent-memory-introducing-99-sota-memory-system/` — Supermemory's later ~99% SOTA claim (2026-03-22).
    - `https://vectorize.io/articles/mempalace-benchmarks` — third-party adjudication; documents the methodology divergence (see below).
    - `https://arxiv.org/html/2410.10813v1` — UC Santa Barbara LongMemEval paper (dataset + metric primary source).
    - `https://huggingface.co/datasets/xiaowu0162/longmemeval` — dataset distribution.
  - **Leaderboard snapshot (REM Labs aggregation, 2026-04-22), scores non-uniform across rows:** #1 MemPalace 96.6% (recall_any@5, raw), #2 Hindsight 94.6% (end-to-end QA), #3 REM Labs 94.6% (self-reported), #4 Supermemory 81.6% (later ~99% claim), #5 Zep/Graphiti 63.8%, #6 GPT-4 native 52.9%, #7 Mem0 66.9%.
  - **Methodology divergence is material.** MemPalace reports `recall_any@5` (did the right chunk appear in top-5?); Hindsight / Supermemory / Zep report end-to-end QA accuracy (did the system answer correctly?). Retrieval recall is structurally higher than end-to-end QA. Direct numeric comparison without metric labeling is the non-equivalent-comparison anti-pattern Memongo's own `benchmark-operating-contract.md` prohibits.
  - **MemPalace 100% hybrid score has disclosed methodology issues.** Engineered by identifying 3 failing questions, patching specifically for them, retesting on the same set. Held-out score (test on non-tuned 450): 98.4%. MemPalace maintainers disclose this openly.
  - **Likely finding candidates on future scan** (for Codifier to assess post-processing): "no official leaderboard" anti-pattern; verbatim-memory vs extraction-memory architectural dimension; MemPalace's layered always-loaded retrieval (L0/L1/L2/L3: identity / critical-facts / topical / on-demand); held-out test discipline as positive governance pattern.
  - **Add UC Santa Barbara LongMemEval team** to `research-authorities/` on scan if not already present.

- ~~**MemPalace repo** — locate the repository, add to a future research-loop intake (not this cycle's scope). Likely P1 or P2 fit given leaderboard claim. Verbatim-memory thesis is the architectural counter-stance to Memongo and Mem0 — worth processing alongside the leaderboard source cluster above.~~ **RESOLVED session 57 (2026-04-23).** Canonical repo: `github.com/MemPalace/mempalace` (49k stars, MIT, v3.3.2). Scam-domain correction logged: `mempalace.tech` is an impostor per the project's own `docs/HISTORY.md` 2026-04-11 entry; official surfaces are `github.com/MemPalace/mempalace`, `pypi.org/project/mempalace`, and `mempalaceofficial.com`. Watched-library entry + full 5-dimension analysis landed; 9 of 10 finding candidates promoted.
- ~~**Supermemory repo** — same. Multiple scoring generations (~85% → ~99%) make methodology disclosure the primary extraction target.~~ **RESOLVED session 57 (2026-04-23).** Canonical repo: `github.com/supermemoryai/supermemory` (~22k stars, MIT, Turborepo/Bun monorepo deployed on Cloudflare Workers). Watched-library entry + full 5-dimension analysis landed; all 7 finding candidates promoted. MemoryBench (their cross-provider benchmarking framework) captured as a distinct finding and a noteworthy distribution channel (skill-based).

### Guide re-synthesis (for next Codifier run)

- **G7 Session Persistence and Memory** — now +11 findings since last synthesis (+4 from Batch 2 at session 44, +7 Memory Architecture from session 45). Staleness threshold (3+) significantly exceeded. **Overdue.**
- **G2 Managing Agent Context** — +3 findings from session 45 (decision matrix, proactive compaction, walkthrough). Approaching staleness threshold.
- **G9 Agent Governance and Trust** — still flagged from session 44; not touched this session.

### From session 45 sources

- ~~**DAB benchmark repo** (github.com/ucbepic/DataAgentBench) — worth a `/repo-analyzer` run if MetaSystem builds any data-agent capability. Treat 38% pass@1 as the frontier baseline for expectation-setting.~~ **DEFERRED session 58 (2026-04-23).** Conditional trigger ("if MetaSystem builds any data-agent capability") not yet met — existing DAB finding + source is sufficient baseline reference. Re-evaluate when MetaSystem starts building S2/S3 data-agent features.
- ~~**Simon Willison "Agentic Engineering Patterns" guide series**~~ **RESOLVED session 58 (2026-04-23).** Processed 6 of 9 remaining chapters: Subagents, Anti-patterns, Hoard things, Red/green TDD, First run the tests, Interactive explanations. Yielded 3 new findings (confirm-failure-first-tdd-agent-discipline, personal-knowledge-hoard-as-agent-substrate, interactive-explanations-extend-linear-walkthroughs). Lower-yield chapters (What is agentic engineering, Writing code is cheap, AI should help us produce better code, How coding agents work, Using Git with coding agents, GIF optimization annotated prompt, Adding new content type annotated prompt, Appendix prompts) SKIPPED with reason: definitional / opinion-essay / project-specific-prompt content; core transferable patterns captured from the 6 high-yield chapters above.
- ~~**Claude Code Subagents blog** — cross-referenced from the session-management blog, not yet processed. Likely high-signal on the subagent decision-matrix cell.~~ **RESOLVED session 58 (2026-04-23).** Processed via Anthropic's canonical subagent docs at code.claude.com/docs/en/sub-agents (formerly docs.anthropic.com/en/docs/claude-code/sub-agents). Yielded 6 new findings (subagent-scope-priority-ladder, inline-scoped-mcp-servers-per-subagent, subagent-persistent-memory-directory, capability-restricted-agent-spawning-via-allowlist, subagent-isolation-contract, foreground-vs-background-subagent-permission-models). Simon Willison's own subagents chapter also processed as a supporting source.
- ~~**New /usage slash command** — mentioned in session-management blog; find its canonical doc.~~ **SESSION-58 DEFERRED (2026-04-23).** Searched code.claude.com/docs/en/slash-commands and adjacent pages — /usage does not have a standalone documentation page as of 2026-04-23 despite being mentioned in the session-management blog. Either (a) it's a newer/unreleased command not yet documented, or (b) it's documented only in release notes. Low priority — skip unless it surfaces in a future scan with a canonical doc URL.

## Emerging Trends (carried from prior scans, still active)

- **Module marketplaces for agent frameworks** — BMAD v6 introduced. Watch for similar patterns in Superpowers, GSD.
- **AI-as-facilitator (not just executor)** — Simon Scrapes command center is the strongest example.
- **llms.txt / llms-full.txt convention** — Context7 is tooling; llms-full.txt is content standard.
- **Agent economy and payments** — Stripe Projects, Agent Mail, email-as-identity shims.
- **Six-layer infrastructure maturity model (Nate B Jones)** — Execution, Orchestration, Memory, Tools, Evaluation, Identity.
- **Transcript compaction and context hygiene** — fresh-conversation-every-10-15-turns; session 45 strengthens this theme with Anthropic's canonical decision matrix.
- **Eval integrity under multi-vector attack** — 3-point skepticism threshold. Session 45 adds DAB's 38% pass@1 ceiling as a reality-check anchor.
- **Cross-vendor convergence on deferred tool loading** — Tool Search Tool (Anthropic) and GPT-5.4 tool search (OpenAI).
- **Programmatic tool calling as context compression** — session 45 strengthens this via programmatic-snippet-extraction (Simon Willison) and query-decomposition (Memongo).
- **Internal state monitoring for safety** — Anthropic emotion vector research.
- **File-based coordination for parallel agents** — C compiler project.

## Newly Emerging Themes (session 45)

- **Single-store vs. multi-store agent memory architectural debate** — Memongo's one-DB claim directly contradicts mem0's triple-store framing. Watch for a third position (hybrid? tiered?) and for benchmark-level adjudication on the same test set.
- **Interpretable rerankers over neural rerankers** — Memongo's weighted-signal composition is cheap and auditable. Watch whether this style spreads as debuggability pressure grows.
- **Importance-based memory decay (not TTL)** — Memongo and OpenClaw/Dreaming both use importance rather than wall-clock. Emerging convention.
- **Proactive vs. reactive compaction** — Anthropic's "compact while model is sharp" reframes a reactive tool as a proactive one. Watch for harnesses that schedule proactive compact at stable-state triggers.
- **Benchmark discipline: exact-vector-search during eval** — Memongo's `$vectorSearch exact:true` for zero ANN noise is a transferable practice for any retrieval benchmark.

## Resolved Items (session 45)

- **Final research batch for this cycle closed.** 5 sources processed, 12 new findings at `pipeline_status: raw`, handoff to future Codifier session.
- **Memongo added to watched-libraries** per Nick's explicit request (override on session scope).

## New from session 57 — Priority Re-Evaluation Candidates

Flagged per `/promote-findings` step 5b. Not acted on — reassessment is Codifier scope (`/reassess-priorities`, out of session 57). Nick reviews and directs.

- **`cross-platform-context-file-strategy`** (currently P3) — now corroborated across 4 repos (Archon, n8n, LangGraph, MemPalace). Extended-by link added to [[universal-harness-context-via-symlink]] (a 4th distinct strategy). Candidate for P3 → P2 reassessment.
- **`specification-as-governance-fourth-enforcement-philosophy`** (currently P2) — now corroborated across 3 repos (LangGraph, n8n, MemPalace). Extended-by link added to [[declared-transformations-contract-conformance]]. 3+ threshold reached; candidate for P2 → P1 reassessment.
- **`importance-based-decay-permanent-exemption`** (currently P3) — now part of a 3-strategy decay cluster with [[surprisal-novelty-as-memory-write-gate]] and [[content-derived-temporal-expiration-contradiction-resolution]]. Cluster-level reassessment: all three could move up to P2 if the decay design-space is prioritized.
- **`memory-bank-isolation-per-agent-per-project`** (currently P3) — now linked with [[hierarchical-container-tag-multi-tenancy]]. Both are same-problem findings for multi-tenant memory scoping; cross-repo evidence now spans Hindsight, mem0, and Supermemory.

## Still Deferred (from prior sessions)

- ~~**OB1 stale prioritization-list item** — session 56 flagged that OB1 was already fully promoted (5 findings, 2 skipped on 2026-04-20). PROGRESS.md prioritization list still carried the stale bullet at session 56 close.~~ **RESOLVED session 57 close (2026-04-23).** PROGRESS.md will be updated at session close; this note records that the stale bullet was struck at the carry-forward layer.
- ~~**Batch 1 deferred video `ib2m9HVX7as`** — still deferred.~~ **RESOLVED session 58 (2026-04-23).** Transcript existed at `incubator/claude-build/app/transcript-fetcher/transcripts/ib2m9HVX7as.md` (69KB, 776 segments). Content identified as Nate B. Jones' "The 5 Layers AI Cannot Replace" video. Processed as research-source; yielded 2 findings (five-durable-verticals-ai-cannot-replace, agent-native-app-store-emerging-category).
- ~~**`/tmp/metasystem-repo-cache/` cleanup** — pending.~~ **RESOLVED session 57 (2026-04-23).** Directory existed but was empty (no user files); confirmed unreferenced by any active code path (all 18 grep hits were historical docs/handoffs/SL entries, not consumers). `rmdir /tmp/metasystem-repo-cache/` succeeded. Active `/repo-analyzer` cache at `systems/improvement-loop/watched-libraries/_tmp/repo-cache/` untouched and correct.

### Still Deferred — carry forward to session 59 (Bucket C not completed in session 58)

Session 58 completed Buckets A and B but did not sweep Bucket C; context budget was prioritized for higher-yield Bucket A/B intake. **Session 59 (2026-04-23) swept all 13 items — disposition below. Each line prefixed with its session-59 action: PROMOTED, AMENDED, NO-FIX-NEEDED, or SKIP-WITH-REASON.**

- ~~**Playwright DOM selector update** (session 42)~~ — **SKIP-WITH-REASON (session 59).** Selectors in `incubator/claude-build/app/transcript-fetcher/fetch.py` (`ytd-transcript-segment-renderer`, `button[aria-label="Show transcript"]`, `.segment-timestamp`, `.segment-text`) are currently functional — session 58 processed `ib2m9HVX7as.md` via this exact code path successfully. No update needed until selectors break.
- ~~**Dark Code channel identity**~~ — **SKIP-WITH-REASON (session 59).** Second targeted locate (after session 57's first attempt) returned no identifying evidence. Authority entry at `research-authorities/dark-code-channel-youtube.md` remains minimal; final skip recommended unless new primary evidence emerges.
- ~~**Agentic OS dimension registry update**~~ — **NO-FIX-NEEDED (session 59).** Registry check shows 19 findings currently tagged `category: Agentic OS`/`Agentic Systems`. Dimension 11 "Agentic Systems" was formally registered in `operations/references/research-dimensions.md` on 2026-04-21 (renamed from "Agentic OS"). Graduation trigger (5) long since exceeded. Backlog item was stale bookkeeping.
- ~~**Nate B Jones agentic harness skill**~~ — **PROMOTED (session 59).** Locate found: (a) Nate's Substack "Your Agent Is 80% Plumbing" (Substack post) with a free installable Claude Code/Codex audit skill delivering a gap-analysis against his 12-primitive framework; (b) `affaan-m/everything-claude-code` GitHub repo (38 agents, 156 skills, 72 legacy shims) as a parallel example of skills-as-distribution. Finding promoted: `audit-skill-as-expert-harness-distribution-channel.md` (P3 Monitor). **Download/eval of Nate's skill against MetaSystem S2/S3 prompts remains out of Researcher scope — that is Nick-or-Codifier scope if/when MetaSystem chooses to adopt.**
- ~~**Claude Code leaked source** — 18-module bash security architecture~~ — **PROMOTED + AMENDED (session 59).** Canonical writeup located at `claudefa.st/blog/guide/mechanics/claude-code-source-leak`. Clarification: bashSecurity.ts runs **23 numbered checks**, of which **18 specifically block Zsh builtins** (not "18 modules" as the original backlog phrased). New finding promoted: `shell-injection-vector-taxonomy-agent-bash-security.md` (P2) — enumerating named vectors (Zsh equals expansion, unicode zero-width-space, IFS null-byte, HackerOne-originated malformed-token bypass). Existing finding `tiered-permission-system-bash-safety.md` amended to the 23-check/18-Zsh-builtin framing and cross-linked as extended-by.
- ~~**Token budget pre-turn projection implementations** — architectural evidence exists, no practitioner walkthroughs found~~ — **PROMOTED (session 59).** Anthropic's canonical context-windows doc (`platform.claude.com/docs/en/build-with-claude/context-windows`) documents that Claude Sonnet 4.5+, Haiku 4.5+ track remaining context-window headroom natively inside the model. ACL 2025 Findings paper "Token-Budget-Aware LLM Reasoning" (arXiv 2412.18547) provides academic grounding. Finding promoted: `model-native-context-window-awareness.md` (P2 Design Required) — model-side self-pacing distinct from harness-side pre-turn projection; layered defense.
- ~~**Superpowers + GSD tension resolution**~~ — **PROMOTED (session 59).** Pulumi blog and Ewan Mak Medium comparison establish a clean three-way taxonomy: "gstack thinks, GSD stabilizes, Superpowers executes." Finding promoted: `framework-tension-taxonomy-superpowers-gsd-gstack.md` (P2) documenting the primary constraint each framework enforces (role separation / context stability / execution discipline), the canonical failure mode per framework (orchestrator context exhaustion / explicit-handoff tax / chain rigidity), and composability guidance.
- ~~**Garry Tan direct commentary** on gstack — find first-party source~~ — **LOCATED, NO-NEW-FINDING (session 59).** First-party voice located at `github.com/garrytan/gstack` (canonical repo, 23 opinionated tools across CEO/Designer/Eng Manager/Release Manager/Doc Engineer/QA roles). Authority entry at `research-authorities/garry-tan.md` already exists. KB already carries 7+ gstack findings from prior repo analysis. Tan's "cognitive gearing" framing is already baked into the new `framework-tension-taxonomy-superpowers-gsd-gstack.md` finding. No separate finding-grade net-new.
- ~~**Stripe Projects for agent billing** — current state and API maturity~~ — **PROMOTED (session 59).** Major Stripe launches in 2026: Machine Payments Protocol (MPP, co-authored with Tempo), Agentic Commerce Suite, Stripe Projects (agent permissioning/provisioning), Shared Payment Tokens, plus x402-on-Base (Coinbase) announcement. Finding promoted: `stripe-machine-payments-protocol-agent-economy.md` (P3 Monitor) — cross-vendor convergence on agent-payment rails.
- ~~**E2B vs Daytona sandbox comparison** — direct comparison evidence~~ — **PROMOTED (session 59).** Multiple practitioner comparisons (Northflank, ZenML) converge on threat-model framing rather than pricing. Finding promoted: `sandbox-architecture-by-threat-model-microvm-vs-container.md` (P2 Design Required) — Firecracker microVM (hardware isolation, ~150ms cold start, untrusted-code) vs Docker container (shared kernel, 27-90ms cold start, stateful workspaces) as architectural choice mapped to workload type. Extends `three-sandbox-architectures-comparison.md`.
- ~~**Obsidian Web Clipper + Local Images Plus** — tool combination for research ingestion~~ — **SKIP-WITH-REASON (session 59).** Tool combo located (Obsidian Web Clipper is first-party, open-source, by Steph Ango; Local Images plugin is a separate community plugin). Architectural pattern (web-clip + AI template → vault) is already subsumed by existing `personal-knowledge-hoard-as-agent-substrate.md` and vault-as-OS findings. Operational Nick-workflow detail, not transferable finding-grade material.
- ~~**Video 4 misattribution** — `ide-first-claude-code-with-deterministic-hooks.md` does not match "Stop Using Claude Code in Terminal" (Simon Scrapes). Re-source.~~ — **NO-FIX-NEEDED (session 59).** On inspection both sides are already correctly attributed: (a) Simon Scrapes' "Stop Using Claude Code in Terminal" video (URL `youtube.com/watch?v=uhMCy25NBfw`) is already a processed source at `research-sources/stop-using-claude-code-in-terminal.md` with its own 7 findings (goal-first-agent-management, kanban, task-complexity-tiering, etc.) — all unrelated to the IDE-first-hooks finding; (b) `ide-first-claude-code-with-deterministic-hooks.md` is correctly sourced from `nate-b-jones-videos-feb-mar-2026.md` + `anthropic-claude-code-best-practices.md`, not from the Simon Scrapes video. Backlog item was based on a mistaken memory of misattribution that never actually occurred.
- ~~**`/usage` slash command canonical doc**~~ — **SKIP-WITH-REASON (session 59).** Second targeted locate (after session 58's first attempt) surfaces that `/usage` displays subscription-plan consumption (billing-view), distinct from `/context` (context-window-view) which is already covered by existing finding `context-usage-status-line-visual-budget-tracking.md`. `/usage` is a billing-inspection surface, not an architectural pattern — final skip.

### Bucket D — MemoryBench evaluation run (still deferred — session 60 standalone)

- **MemoryBench head-to-head evaluation** — Supermemory's MemoryBench framework (`npx skills add supermemoryai/memorybench` → `/benchmark-context`) against Memongo / Supermemory / mem0 / Zep on LongMemEval. Requires environment setup (bun, clone of framework repo). **Session 59 did not start this — Bucket C consumed the session budget and `feedback_sweep_over_piecemeal.md` guidance prefers one dedicated MemoryBench session to a half-completed one.** Handoff for session 60 at `operations/handoffs/handoff-prompt-session-60-researcher-memorybench-evaluation.md`.

### Session-58 self-deferred — low-yield Simon Willison chapters

The following Simon Willison "Agentic Engineering Patterns" chapters were deprioritized in session 58 and may be worth a later scan if capacity permits:

- **What is agentic engineering** — definitional chapter; captured by adjacent framings.
- **Writing code is cheap now** — opinion essay; not pattern-dense.
- **AI should help us produce better code** — opinion essay; not pattern-dense.
- **How coding agents work** — technical overview; likely overlaps with existing KB coverage of LLM/tool-calling/reasoning-loops.
- **Using Git with coding agents** — likely well-trodden ground in the KB.
- **GIF optimization annotated prompt** — project-specific example; low transferability.
- **Adding new content type annotated prompt** — project-specific example; low transferability.
- **Appendix prompts** — loose prompt collection; survey-once if Nick wants breadth.
