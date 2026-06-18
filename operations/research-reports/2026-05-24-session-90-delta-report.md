---
name: "Session 90 Delta Report — Researcher Link Intake (Continued) + Repo Analysis Cleanup"
session: 90
date: "2026-05-24"
agent: "Researcher"
disposition: "link intake continued + repo analysis cleanup"
---

# Session 90 Delta Report — Researcher Link Intake (Continued) + Repo Analysis Cleanup

## Summary

Processed 6 new links from LINKS.md (lines 19-24). Created 3 new watched-library entries, 4 analysis docs (2 new repos + 2 backfill from session 89), 12 new findings via `/promote-findings` gate (Nick approved all candidates), and 3 new source entries. Updated 1 existing finding with corroborating evidence. Also wrote the 2 missing analysis docs from session 89 (hermes-agent and deep-tutor).

## Part 1: Links Processed

| # | Link | Type | Route | Verdict |
|---|------|------|-------|---------|
| 1 | earendil-works/pi | GitHub repo | watched-library + /repo-analyzer + /promote-findings | DONE — 6 findings promoted |
| 2 | Pragmatic Engineer newsletter (pi article) | Newsletter | source entry | DONE — philosophy only, no new findings |
| 3 | warpdotdev/warp | GitHub repo | watched-library + /repo-analyzer + /promote-findings | DONE — 6 findings promoted |
| 4 | warpdotdev/oz-workspace | GitHub repo | watched-library (cherry-pick, included in warp analysis) | DONE — no separate findings |
| 5 | arxiv.org/pdf/2603.20576 | arXiv PDF | source entry | DONE — DataAgentBench, low relevance, no findings |
| 6 | youtube.com/watch?v=pDoBe4qbFPE | YouTube | transcript-fetcher + source entry | DONE — corroborates existing findings, no new ones |

## Part 2: Repo Analysis Cleanup

### Missing analysis docs written:
- `watched-libraries/analysis/hermes-agent-analysis.md` — reconstructed from source entry, watched-library entry, and repo metadata
- `watched-libraries/analysis/deep-tutor-analysis.md` — written from /tmp/DeepTutor clone + AGENTS.md

### Session 89 findings that bypassed `/promote-findings` gate (flagged for Nick's retroactive review):

| # | Finding | Source Repo | Priority | Status |
|---|---------|-------------|----------|--------|
| 1 | auxiliary-model-slot-architecture.md | hermes-agent | P1 | `pipeline_status: raw` — **APPROVE or REJECT?** |
| 2 | bounded-tiered-memory-inference-driven-curation.md | hermes-agent | P2 | `pipeline_status: raw` — **APPROVE or REJECT?** |
| 3 | layered-prompt-assembly-stable-segment-caching.md | hermes-agent | P2 | `pipeline_status: raw` — **APPROVE or REJECT?** |
| 4 | two-layer-plugin-model-tools-vs-capabilities.md | DeepTutor | P2 | `pipeline_status: raw` — **APPROVE or REJECT?** |
| 5 | context-degradation-40-50-percent-threshold.md | taches-cc | P2 | `pipeline_status: raw` — **APPROVE or REJECT?** |
| 6 | domain-expertise-as-loadable-context-sub-skill.md | taches-cc | P3 | `pipeline_status: raw` — **APPROVE or REJECT?** |

These were created directly from repo analysis agent reports in session 89 without Nick's candidate selection. They are properly structured and at `pipeline_status: raw`. Nick should retroactively approve or reject.

## New Findings Created (12)

### P1 — Implement Now (2)

| Finding | Category | Source |
|---------|----------|--------|
| Runtime Self-Modification via Extension API | Agent Design | pi-agent repo |
| Core/Specialized Skill Inheritance Pattern | Agent Design | warp repo |

### P2 — Design Required (7)

| Finding | Category | Source |
|---------|----------|--------|
| Session Tree as First-Class Abstraction | Context Engineering | pi-agent repo |
| Tool Call Event Interception Pattern | Tool Integration | pi-agent repo |
| Supply-Chain Hardening for Agent Packages | Governance | pi-agent repo |
| Skills-Lock for Portable Agent Skills | Tool Integration | warp repo |
| Feature Flag Lifecycle as Deployment Governance | Governance | warp repo |
| Oz Multi-Agent Room Model | Orchestration | warp repo |

### P3 — Monitor (3)

| Finding | Category | Source |
|---------|----------|--------|
| Multi-Provider LLM Abstraction with Dynamic Registration | Model Selection | pi-agent repo |
| Concurrent Agent Session Safety Rules | Governance | pi-agent repo |
| Visual Evidence Gate for UI PRs | Evaluation | warp repo |
| Follow-Up Question Budget in Agent Triage | Agent Design | warp repo |

## Existing Findings Updated (1)

| Finding | Update | New Source |
|---------|--------|-----------|
| Context Degradation at 40-50% Utilization Threshold | Added corroborating source (AIABS video cites 70% as degradation point, recommends 75% auto-compact) | claude-code-hidden-settings-aiabs.md |

## New Sources Created (3)

| Source | Type | Relevance |
|--------|------|-----------|
| pragmatic-engineer-pi-self-modifying-agent.md | Newsletter | Medium |
| claude-code-hidden-settings-aiabs.md | Video | Medium |
| dataagentbench-arxiv-2603-20576.md | Paper | Low |

## New Watched Libraries (3)

| Library | Stars | Spectrum | Key Tracking Focus |
|---------|-------|----------|-------------------|
| pi-agent | ~5k | study | Extension API, session tree, supply-chain hardening |
| warp | ~25k | study | Core/specialized skills, skills-lock, feature flag lifecycle |
| oz-workspace | ~500 | cherry-pick | Multi-agent room model, SSE coordination |

## New Analysis Docs (4)

| Doc | Repo | Status |
|-----|------|--------|
| pi-agent-analysis.md | earendil-works/pi | New (session 90) |
| warp-analysis.md | warpdotdev/warp | New (session 90) |
| hermes-agent-analysis.md | nousresearch/hermes-agent | Backfill (session 89 gap) |
| deep-tutor-analysis.md | HKUDS/DeepTutor | Backfill (session 89 gap) |

## KB Statistics Delta

| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| Research Findings | 606 | 618 | +12 |
| Research Sources | 174 | 177 | +3 |
| Watched Libraries | 22 | 25 | +3 |
| Analysis Docs | 20 | 24 | +4 |

## Dimension Distribution of New Findings

| Dimension | Count |
|-----------|-------|
| Agent Design | 4 |
| Governance | 3 |
| Tool Integration | 2 |
| Context Engineering | 1 |
| Orchestration | 1 |
| Model Selection | 1 |
| Evaluation | 1 |

## Processing Notes

- Pi, Warp, and oz-workspace repos cloned to `watched-libraries/_tmp/repo-cache/`
- YouTube transcript fetched via playwright backend (API blocked, fallback worked)
- arXiv paper fetched via WebFetch — limited extraction from PDF binary; supplemented with AI summary
- Pragmatic Engineer article paywalled for deep content — only surface-level philosophy available
- DeepTutor clone still available at `/tmp/DeepTutor` from session 89
- All 12 findings went through `/promote-findings` gate (Nick approved all)
