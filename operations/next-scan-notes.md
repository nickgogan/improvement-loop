---
name: "Next Scan Notes"
last_updated: "2026-04-20"
---

# Next Scan Notes

Carry-forward from session 45 (final batch intake: Memongo + Claude Code session mgmt + 2 arXiv + Simon Willison).

## Specific Items to Investigate

### Memongo-related (highest priority for Nick's active work)

- **Mampalace and Supermemory leaderboard source** — Nick cited Memongo 92% raw, Mampalace #1 at 96.6% raw, Supermemory #3 at 70%. None of these comparison numbers appear in the Memongo README. Locate the external LongMemEval-S leaderboard or benchmark post, process it as a source, and cross-reference against Memongo's self-reported 98.1% R@5 to understand the methodology difference between "raw" and "LLM-aided" pipelines.
- **Memongo companion documentation** — `PRODUCTION-READY.md`, `docs/benchmarks/benchmark-operating-contract.md`, `docs/platform/self-host.md`, and the referenced `MAINTAINER-MAP.md` are referenced but not in the README body. Strong Pass 2 extraction candidates — run `/repo-analyzer` on `watched-libraries/memongo.md` to surface them.
- **Mampalace repo** — locate the repository, add to a future research-loop intake (not this cycle's scope). Likely P1 or P2 fit given leaderboard claim.
- **Supermemory repo** — same.

### Guide re-synthesis (for next Codifier run)

- **G7 Session Persistence and Memory** — now +11 findings since last synthesis (+4 from Batch 2 at session 44, +7 Memory Architecture from session 45). Staleness threshold (3+) significantly exceeded. **Overdue.**
- **G2 Managing Agent Context** — +3 findings from session 45 (decision matrix, proactive compaction, walkthrough). Approaching staleness threshold.
- **G9 Agent Governance and Trust** — still flagged from session 44; not touched this session.

### From session 45 sources

- **DAB benchmark repo** (github.com/ucbepic/DataAgentBench) — worth a `/repo-analyzer` run if MetaSystem builds any data-agent capability. Treat 38% pass@1 as the frontier baseline for expectation-setting.
- **Simon Willison "Agentic Engineering Patterns" guide series** — this session processed only the "Linear Walkthroughs" chapter. Full guide has chapters on Principles (5), Working with coding agents (3), Testing and QA (3), Understanding code (2, one processed), Annotated prompts (2), Appendix. Process remaining chapters in a future scan. Author is Tier 1 — high expected yield.
- **Claude Code Subagents blog** — cross-referenced from the session-management blog, not yet processed. Likely high-signal on the subagent decision-matrix cell.
- **New /usage slash command** — mentioned in session-management blog; find its canonical doc.

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

## Still Deferred (from prior sessions)

- **Playwright DOM selector update** (session 42) — not touched this session.
- **Batch 1 deferred video `ib2m9HVX7as`** — still deferred.
- **`/tmp/metasystem-repo-cache/` cleanup** — pending.
- **Dark Code channel identity** — no new evidence.
- **Agentic OS dimension registry update** — still at 3 findings; no new additions from session 45. Graduation trigger (5) not reached.
- **Nate B Jones agentic harness skill** — download and evaluate against current S2/S3 prompts.
- **Claude Code leaked source** — 18-module bash security architecture.
- **Token budget pre-turn projection implementations** — architectural evidence exists, no practitioner walkthroughs found.
- **Superpowers + GSD tension resolution** — mega-orchestrator vs. fresh-session-per-phase.
- **Garry Tan direct commentary** on gstack — find first-party source.
- **Stripe Projects for agent billing** — current state and API maturity.
- **E2B vs Daytona sandbox comparison** — direct comparison evidence.
- **Obsidian Web Clipper + Local Images Plus** — tool combination for research ingestion.
- **Video 4 misattribution** — `ide-first-claude-code-with-deterministic-hooks.md` does not match "Stop Using Claude Code in Terminal" (Simon Scrapes). Re-source.
