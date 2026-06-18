---
name: "Session 89 Delta Report — Researcher Link Intake"
session: 89
date: "2026-05-24"
agent: "Researcher"
disposition: "link intake from LINKS.md"
---

# Session 89 Delta Report — Researcher Link Intake

## Summary

Processed 18 links from LINKS.md through the IL intake workflow. 12 links processed (3 repos, 8 videos, 1 article), 6 skipped (4 off-dimension videos, 2 triaged-out videos). Produced 17 new findings, updated 3 existing findings, created 11 new source entries, and added 3 new watched-library entries.

## Links Processed vs Skipped

| # | Link | Type | Route | Verdict |
|---|------|------|-------|---------|
| 1 | glittercowboy/taches-cc-resources | GitHub repo | repo-analyzer (agent) | DONE — 2 new findings |
| 2 | nousresearch/hermes-agent | GitHub repo | repo-analyzer (agent) | DONE — 3 new findings |
| 3 | HKUDS/DeepTutor | GitHub repo | manual analysis | DONE — 1 new finding |
| 4 | z02Y-1OvWSM | YouTube | transcript-fetcher → extract | DONE — 1 new finding |
| 5 | wRDk9_JoIic | YouTube | transcript-fetcher → extract | DONE — 1 new + 1 update |
| 6 | FDkvRl1RlT0 | YouTube | — | SKIPPED (M&A news) |
| 7 | 647pSnX5H_Y | YouTube | transcript-fetcher → triage | SKIPPED (generic, already covered) |
| 8 | EpJ0CjTJSag | YouTube | transcript-fetcher → extract | DONE — 1 new + 1 update |
| 9 | jwtpMSRAPAQ | YouTube | transcript-fetcher → triage | SKIPPED (market analysis) |
| 10 | adNErrz2aA0 | YouTube | — | SKIPPED (SaaS pricing) |
| 11 | -iSLQe_imrE | YouTube | transcript-fetcher → extract | DONE — 1 new + 1 update |
| 12 | BlTpG51x94w | YouTube | transcript-fetcher → extract | DONE — 1 new finding |
| 13 | LIkYVsxMpS8 | YouTube | — | SKIPPED (business strategy) |
| 14 | 725QE_LNXT4 | YouTube | — | SKIPPED (marketing) |
| 15 | X_JsIHUfUjc | YouTube | transcript-fetcher → extract | DONE — 2 new findings |
| 16 | zP6TnEiueEc | YouTube | transcript-fetcher → extract | DONE — 2 new findings |
| 17 | ogTLWGBc3cE | YouTube | transcript-fetcher → extract | DONE — 1 new finding |
| 18 | foundanand.medium.com | Blog post | WebFetch → extract | DONE — 1 new finding |

## New Findings Created (17)

### P1 — Implement Now (3)

| Finding | Category | Source |
|---------|----------|--------|
| Screen-as-Permissions-Model Agent Bypass Failure | Governance | Lilly/McKinsey incident video |
| MCP Tool Descriptions as Prompt-Injection Attack Surface | Governance | Google I/O protocols video |
| Auxiliary Model Slot Architecture | Agent Design | hermes-agent repo |

### P2 — Design Required (6)

| Finding | Category | Source |
|---------|----------|--------|
| Write-Time vs Query-Time Synthesis: KB Poisoning | Context Engineering | Medium article |
| Orchestrator-Delegates-to-Headless for Context Isolation | Context Engineering | GStack+GSD video |
| Five-Layer Recursive AI Loop Architecture | Agentic Systems | YC self-improving company video |
| AGUI as Human Control Layer, Not UI Layer | Orchestration | Google I/O protocols video |
| Bounded Tiered Memory with Inference-Driven Curation | Context Engineering | hermes-agent repo |
| Two-Layer Plugin Model: Tools vs Capabilities | Agent Design | DeepTutor repo |
| Context Degradation at 40-50% Utilization Threshold | Context Engineering | taches-cc repo |
| Layered Prompt Assembly with Stable-Segment Caching | Prompt Craft | hermes-agent repo |

### P3 — Monitor (8)

| Finding | Category | Source |
|---------|----------|--------|
| Typed-Edge Knowledge Graph for Token Reduction | Context Engineering | Karpathy alt video |
| Agent Proof-of-Work UI Builds User Trust | Evaluation | Utori interview video |
| Data-Permanent Software-Ephemeral Architecture | Context Engineering | YC video |
| Thesis-Anchored Multi-Question Prompting | Prompt Craft | Prompting style video |
| Throwaway HTML Editor as Structured Input Surface | Tool Integration | Markdown vs HTML video |
| Domain Expertise as Loadable Context Sub-Skill | Context Engineering | taches-cc repo |

## Existing Findings Updated (3)

| Finding | Update | New Source |
|---------|--------|-----------|
| March of Nines: Compounding Reliability Math | Added corroborating source from Utori interview | problem-with-ai-agents-utori-compound-errors.md |
| Agent Identity Governance as HITL Enforcement | Added Lilly incident as production case evidence | lilly-incident-agent-security-permissions.md |
| HTML Artifact as Rich Skill Output | Added human-re-engagement framing from Anthropic team | markdown-vs-html-claude-code-derrick-anthropic.md |

## New Sources Created (11)

| Source | Type | Relevance |
|--------|------|-----------|
| hidden-flaw-karpathy-llm-wiki.md | Blog Post | High |
| karpathy-second-brain-typed-edge-alternative.md | Video | High |
| problem-with-ai-agents-utori-compound-errors.md | Video | High |
| lilly-incident-agent-security-permissions.md | Video | High |
| markdown-vs-html-claude-code-derrick-anthropic.md | Video | High |
| gstack-gsd-superpowers-orchestrator-headless.md | Video | High |
| self-improving-company-yc-five-layer-loop.md | Video | High |
| google-io-mcp-a2a-agui-protocol-stack.md | Video | High |
| opus-4-7-prompting-style-obsolete.md | Video | Medium |
| hermes-agent-nousresearch-analysis.md | Tool Release | High |
| deep-tutor-hkuds-analysis.md | Tool Release | Medium |

## New Watched Libraries (3)

| Library | Stars | Spectrum | Key Tracking Focus |
|---------|-------|----------|-------------------|
| hermes-agent | 165k | study | Aux model slots, bounded tiered memory, prompt caching |
| taches-cc-resources | 1.9k | cherry-pick | Context degradation model, domain expertise sub-skills |
| deep-tutor | 24k | study | Two-layer plugin model, capability stages |

## KB Statistics Delta

| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| Research Findings | 589 | 606 | +17 |
| Research Sources | 163 | 174 | +11 |
| Watched Libraries | 19 | 22 | +3 |
| Analysis Docs | — | +1 | taches-cc-resources-analysis.md (by subagent) |

## Processing Notes

- All 14 YouTube transcripts fetched successfully via `transcript-fetcher` (batch mode). Transcripts cached at `incubator/claude-build/app/transcript-fetcher/transcripts/`.
- 5 parallel Sonnet agents used for transcript analysis; 3 parallel agents for repo analysis (1 failed on DeepTutor due to permissions — analyzed manually).
- Taches-cc-resources already had a source entry from session 28 (2026-03-28); analysis was an update pass. Agent wrote analysis doc to `watched-libraries/analysis/`.
- 2 video transcripts triaged as SKIP by analysis agents: 647pSnX5H_Y (generic scaffolding taxonomy) and jwtpMSRAPAQ (market analysis).
- 4 additional videos skipped by Nick's triage decision: FDkvRl1RlT0 (M&A), adNErrz2aA0 (SaaS pricing), LIkYVsxMpS8 (business strategy), 725QE_LNXT4 (marketing).

## Dimension Distribution of New Findings

| Dimension | Count |
|-----------|-------|
| Context Engineering | 7 |
| Governance | 3 |
| Agent Design | 3 |
| Orchestration | 2 |
| Prompt Craft | 2 |
| Tool Integration | 2 |
| Evaluation | 1 |
| Agentic Systems | 1 |

Note: some findings span multiple dimensions; counted by primary category.
