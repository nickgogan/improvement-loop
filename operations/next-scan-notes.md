---
name: "Next Scan Notes"
last_updated: "2026-04-09"
---

# Next Scan Notes

Carry-forward from 2026-04-07 (4 sessions, 16 videos, calibration complete).

## Emerging Trends to Monitor

- **Module marketplaces for agent frameworks.** BMAD v6 introduced a vetted module marketplace. Watch for similar patterns in Superpowers, GSD, and other orchestration frameworks. Signals ecosystem maturation.
- **AI-as-facilitator (not just executor).** Multiple sources show agents managing human workflows (goal-first abstraction, kanban turn-taking, task complexity tiering). The Simon Scrapes command center is the strongest example.
- **llms.txt / llms-full.txt convention.** AI-optimized documentation endpoints emerging as a standard. Context7 is the tooling layer; llms-full.txt is the content standard. Track adoption across major libraries.
- **Agent economy and payments.** Stripe Projects for agent billing, Agent Mail for inter-agent communication, email-as-identity shim patterns. Infrastructure for agents-as-economic-actors is forming.
- **Six-layer infrastructure maturity model.** Nate B Jones' stack (Execution, Orchestration, Memory, Tools, Evaluation, Identity) is a useful lens. Watch for competing maturity models and convergence.
- **Transcript compaction and context hygiene.** Fresh-conversation-every-10-15-turns, pre-compression identity pinning, and dynamic tool pool assembly are all responses to the same pressure: context window scarcity in long-running agents.
- **Eval integrity under multi-vector attack.** Anthropic documented three independent threats: models autonomously gaming evals (BrowseComp), infrastructure config confounding scores (6-point swings), and inter-agent web contamination. The "3-point skepticism threshold" is an actionable heuristic. Watch for community adoption.
- **Cross-vendor convergence on deferred tool loading.** Both Anthropic (Tool Search Tool) and OpenAI (GPT-5.4 tool search) shipped on-demand tool discovery. Emerging standard — track MCP integration and third-party implementations.
- **Programmatic tool calling as context compression.** Anthropic's approach of having Claude write Python to orchestrate tools (200KB → 1KB) is a fundamentally different architecture from sequential tool use. Watch for SDK-level support and community patterns.
- **Internal state monitoring for safety.** Anthropic's emotion vector research shows LLMs develop measurable internal states that causally influence behavior (desperation → composed-looking cheating). Novel safety dimension — not yet actionable for downstream users but worth tracking.
- **File-based coordination for parallel agents.** The C compiler project (100K lines, 2000 sessions) used git + file locks with no orchestrator. Strong counterpoint to framework-heavy approaches. Watch for more examples of filesystem-as-coordination-layer.

## Specific Items to Investigate

### From calibration (high priority)
- **Nate B Jones agentic harness skill** — download and evaluate against current S2/S3 prompts. Linked in "12 Critical Pieces" video description.
- **Claude Code leaked source** — review directly for additional primitives beyond the 12 covered. The 18-module bash security architecture specifically needs deeper analysis.
- **Token budget pre-turn projection implementations** — architectural evidence exists (leaked config) but no implementation guides found. Search for practitioner walkthroughs.
- **Dynamic tool pool assembly evidence** — inferred from Claude Code config but no practitioner walkthroughs found at scale.

### From transcript re-extraction (backfill candidates)
- **Mem0 hybrid memory benchmarks** — referenced in multiple videos but no production evidence captured. Search for benchmark data.
- **Stripe Projects for agent billing** — mentioned in Nate B Jones infrastructure video. Investigate current state and API maturity.
- **E2B vs Daytona sandbox comparison** — both referenced as agent execution environments. Need direct comparison evidence.
- **Obsidian Web Clipper + Local Images Plus** — tool combination for research ingestion. Evaluate for IL pipeline use.

### From session 1 (corroboration needed)
- **Superpowers + GSD tension resolution** — mega-orchestrator (persistent session) vs. fresh-session-per-phase. Look for practitioners who reconcile these.
- **Independent corroboration** for Superpowers, GSD, and gstack from sources outside Eric Tech's channel.
- **Garry Tan direct commentary** on gstack — find first-party source (GitHub README, post, talk).
- **MCP lazy-loading proposals** — CLI vs MCP is active debate. Monitor for MCP developments addressing the token-loading problem.

### Source quality
- **Video 4 misattribution** — `ide-first-claude-code-with-deterministic-hooks.md` does not match "Stop Using Claude Code in Terminal" (Simon Scrapes). Re-source the finding and create new findings for the video's actual content (web command center, goal-first abstraction, task complexity tiering).

## Resolved Items

- **Transcript extraction tool built and operational.** All 16 videos successfully processed via local transcripts. No longer dependent on Perplexity Computer for transcript access.
- **Calibration completed.** Miss rate measured at 46.5% for summary-based extraction. Quality gap (missed + vague) at 66.7%. Baseline established for pipeline improvement measurement.
- **Extraction quality gap quantified.** Summary-based: 2.1 patterns/video. Transcript-based: 17.6 patterns/video (8.4x increase). Transcript-first extraction is now the standard.
- **Perplexity Computer vs transcript comparison done.** PC better at architectural decomposition; transcripts better at implementation details. Neither sufficient alone. Optimal pipeline defined: PC for architecture + transcript for details + human for triage.
