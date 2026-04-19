---
name: Watch Blogs Triage Report
date: "2026-04-09"
type: triage-report
---

# Watch Blogs Triage Report -- 2026-04-09

**Mode:** dry-run (no entries updated, no sources created)

## Summary

| Blog | Last Checked | New Posts | EXTRACT | SKIP | DEFER | Fetch Method |
|------|-------------|-----------|---------|------|-------|--------------|
| Anthropic Engineering | 2026-04-09 | 18 | 17 | 1 | 0 | webfetch |
| Anthropic Research | 2026-04-09 | 6 | 4 | 2 | 0 | perplexity + webfetch |
| **Total** | | **24** | **21** | **3** | **0** | |

---

## New Posts Detail

### Anthropic Engineering Blog
**Checked via:** webfetch (no RSS available)

| Post | Date | Patterns | Verdict | Dimensions | Reason |
|------|------|----------|---------|------------|--------|
| Writing effective tools for agents -- with agents | 2025-09-11 | 19 | EXTRACT | Tools, Prompt, Eval | Densest post. Tool consolidation, natural language identifiers, agent-driven optimization. 25-35% accuracy gains. |
| Demystifying evals for AI agents | 2026-01-09 | 15 | EXTRACT | Eval, Agent Design | pass@k vs pass^k, combined grader types, saturation monitoring. Comprehensive eval framework. |
| Claude Code: Best practices for agentic coding | 2025-04-18 | 14 | EXTRACT | Context, Orchestration, Agent Design | Writer/Reviewer pattern, fan-out, interview pattern, CLAUDE.md pruning heuristic. |
| Effective context engineering for AI agents | 2025-09-29 | 12 | EXTRACT | Context, Prompt, Agent Design | Canonical context engineering reference. JIT retrieval, progressive disclosure, message compaction. |
| Harness design for long-running application development | 2026-03-24 | 11 | EXTRACT | Orchestration, Eval, Agent Design | Generator-evaluator split, sprint contracts. 20x cost yielded working result vs broken solo. |
| Building effective agents | 2024-12-19 | 11 | EXTRACT | Agent Design, Orchestration, Tools | Foundational taxonomy: orchestrator-workers, evaluator-optimizer, ACI optimization. |
| Effective harnesses for long-running agents | 2025-11-26 | 8 | EXTRACT | Orchestration, Agent Design, Tools | Initializer agent, feature list JSON, git-based state management. |
| Scaling Managed Agents: Decoupling the brain from the hands | 2026-02-04 | 8 | EXTRACT | Orchestration, Agent Design, Sandboxing | Brain/hands decoupling, event-sourced sessions, lazy provisioning (60% p50 TTFT reduction). |
| Building a C compiler with a team of parallel Claudes | 2026-02-05 | 8 | EXTRACT | Orchestration, Agent Design, Tools | 2000 sessions, $20K, 100K-line compiler. Git-based task locking, oracle debugging. |
| How we built our multi-agent research system | 2025-06-13 | 8 | EXTRACT | Orchestration, Agent Design, Tools | Scaling rules by complexity, Claude-as-prompt-engineer (40% time reduction). |
| Claude Code auto mode: a safer way to skip permissions | 2026-03-25 | 7 | EXTRACT | Governance, Sandboxing, Agent Design | Two-stage classifier (8.5% to 0.4% false positives), transcript stripping, multi-agent handoff gating. |
| Introducing advanced tool use | 2025-11-24 | 7 | EXTRACT | Tools, Context | Deferred loading (85% token reduction), programmatic tool calling, tool use examples (72% to 90%). |
| Code execution with MCP | 2025-11-04 | 7 | EXTRACT | Tools, Context, Sandboxing | 98.7% token reduction via on-demand loading. PII tokenization at MCP layer, filesystem discovery. |
| Beyond permission prompts: Claude Code sandboxing | 2025-10-20 | 7 | EXTRACT | Sandboxing, Governance | OS-level isolation (bubblewrap/seatbelt), git proxy interception. 84% permission prompt reduction. |
| The "think" tool | 2025-03-20 | 7 | EXTRACT | Prompt, Tools, Eval | 54% improvement in complex policy domains. pass^k metric, selective implementation criteria. |
| Eval awareness in BrowseComp | 2026-03-06 | 7 | EXTRACT | Eval, Model, Governance | Multi-agent token amplification (3.7x contamination rate), URL slug exploitation. Critical for eval design. |
| Quantifying infrastructure noise in evals | 2026-02-03 | 6 | EXTRACT | Eval, Sandboxing | 6-point swings from config alone. 3x headroom calibration reducing infra errors 5.8% to 2.1%. |
| Designing AI-resistant technical evaluations | 2026-01-21 | 8 | SKIP | -- | About hiring eval design for human candidates, not agent systems. |

### Anthropic Research Blog
**Checked via:** perplexity + webfetch (no RSS available)

| Post | Date | Patterns | Verdict | Dimensions | Reason |
|------|------|----------|---------|------------|--------|
| Long-running Claude for scientific computing | 2026-03-23 | 6 | EXTRACT | Context, Orchestration, Eval, Agent Design | CHANGELOG.md as persistent memory, test oracle pattern, Ralph Loop plugin, git-as-checkpoint. |
| Trustworthy agents in practice | 2026-04-09 | 5 | EXTRACT | Orchestration, Governance, Agent Design, Tools | 4-component architecture, Plan Mode, managed agent virtualization (p50 TTFT -60%). |
| Emotion concepts and their function in an LLM | 2026-04-02 | 2 | EXTRACT | Model, Eval, Agent Design | Emotion vector steering (22% reward hacking increase), character-based persona design. |
| A "diff" tool for AI | 2026-03-13 | 2 | EXTRACT | Model, Eval | DFC model diffing for behavioral regression, steering validation technique. |
| Introducing our Science Blog | 2026-03-23 | 0 | SKIP | -- | Announcement post, no actionable patterns. |
| Partnering with Mozilla | 2026-03-06 | 1 | SKIP | -- | Security domain, not agent design. Below threshold. |

---

## Action Queue

### Create Research Sources (21 EXTRACT verdicts)

**Tier 1 — Highest density (10+ patterns, process first):**
1. Writing effective tools for agents (19 patterns) — https://www.anthropic.com/engineering/writing-tools-for-agents
2. Demystifying evals for AI agents (15) — https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
3. Claude Code: Best practices (14) — https://www.anthropic.com/engineering/claude-code-best-practices
4. Effective context engineering (12) — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
5. Harness design for long-running apps (11) — https://www.anthropic.com/engineering/harness-design-long-running-apps
6. Building effective agents (11) — https://www.anthropic.com/engineering/building-effective-agents

**Tier 2 — High density (7-8 patterns):**
7. Effective harnesses for long-running agents (8) — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
8. Scaling Managed Agents (8) — https://www.anthropic.com/engineering/managed-agents
9. Building a C compiler with parallel Claudes (8) — https://www.anthropic.com/engineering/building-c-compiler
10. How we built our multi-agent research system (8) — https://www.anthropic.com/engineering/multi-agent-research-system
11. Claude Code auto mode (7) — https://www.anthropic.com/engineering/claude-code-auto-mode
12. Advanced tool use (7) — https://www.anthropic.com/engineering/advanced-tool-use
13. Code execution with MCP (7) — https://www.anthropic.com/engineering/code-execution-with-mcp
14. Claude Code sandboxing (7) — https://www.anthropic.com/engineering/claude-code-sandboxing
15. The "think" tool (7) — https://www.anthropic.com/engineering/claude-think-tool
16. Eval awareness in BrowseComp (7) — https://www.anthropic.com/engineering/eval-awareness-browsecomp
17. Quantifying infrastructure noise (6) — https://www.anthropic.com/engineering/infrastructure-noise

**Tier 3 — Research blog (2-6 patterns):**
18. Long-running Claude for scientific computing (6) — https://www.anthropic.com/research/long-running-claude-scientific-computing
19. Trustworthy agents in practice (5) — https://www.anthropic.com/research/trustworthy-agents-in-practice
20. Emotion concepts and their function (2) — https://www.anthropic.com/research/emotion-concepts-function
21. A "diff" tool for AI (2) — https://www.anthropic.com/research/ai-diff-tool

### No Action (3 SKIP)
- Designing AI-resistant technical evaluations — hiring eval, not agent systems
- Introducing our Science Blog — announcement only
- Partnering with Mozilla — security domain, below threshold

---

## Dimension Coverage

| Dimension | Posts Covering |
|-----------|---------------|
| Dim 1: Context Engineering | 6 |
| Dim 2: Model | 3 |
| Dim 3: Prompt | 4 |
| Dim 4: Tools | 9 |
| Dim 5: Orchestration | 9 |
| Dim 6: Evaluation | 8 |
| Dim 7: Sandboxing | 5 |
| Dim 8: Governance | 5 |
| Dim 9: Intent | 0 |
| Dim 10: Agent Design | 13 |

**Total estimated patterns across all EXTRACT posts: ~175**

---

## Notes

- First run of `/watch-blogs` — all posts are new since Post Log was empty.
- The Anthropic engineering blog is an exceptionally high-density source. Nearly every post yields 7+ actionable patterns with quantified results.
- The research blog is more selective — most posts are alignment/safety focused. Only agent-relevant research posts pass the filter.
- Neither blog has RSS. Future runs will use Perplexity `site:` search with `last_checked_date` to discover only new posts.
- **Suggested next step:** Process Tier 1 posts (6 highest-density) through `/research-loop` first, then work through Tier 2.
