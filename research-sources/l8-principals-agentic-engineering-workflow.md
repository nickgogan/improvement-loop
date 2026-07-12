---
name: L8 Principal's Agentic Engineering Workflow
source_type: Video
status: Done
key_takeaways: 'Kun Chen (ex-Meta/Microsoft/Atlassian principal; builds coding agents at Atlassian;

  ships 40-50 tested production changes/day) walks his full harness-above-the-agent

  workflow. Extracted: dev-cost-estimation bias correction as a standing memory-file rule

  (models trained on human timelines overweight development cost and pick cheap designs);

  memory-file→skill migration to cut the always-loaded token tax (global memory held to

  ~27 lines; agent performs the extraction itself); the "no mistakes" post-implementation

  validation pipeline (worktree isolation → intent extraction from the agent session →

  rebase-first → adversarial fresh-context review → evidence artifacts attached to PR →

  risk-gated human review depth); popularity ≠ efficacy for skills (177k-star repo skill

  benchmarked at +5% tokens with worse results); Treehouse worktree lifecycle pooling

  (auto-provision, reclaim on tab close, reuse idle worktrees). Also demonstrated,

  already covered or off-lane: agent-agnostic harness discipline via CLAUDE.md↔AGENTS.md

  symlinks, "lavish" HTML plan-review artifacts (corroborates the throwaway-HTML-editor

  finding), agent-ergonomic tool design ("axi": GitHub MCP measured 3x token cost / 2x

  latency vs CLI; token-efficient output ~40% under JSON), overnight loop tool with

  token/iteration caps, and a "first mate" orchestrator over tmux sessions.'
relevance: High
added_by: Nick
tags:
- multi-agent
- claude-code
- skills
- memory
- evaluation
url: https://www.youtube.com/watch?v=iQyg-KypKAA
authority:
- kun-chen.md
findings:
- dev-cost-estimation-bias-correction.md
- memory-file-to-skill-migration.md
- no-mistakes-post-implementation-validation-pipeline.md
- skill-popularity-vs-measured-efficacy.md
- isolation-resolver-worktree-lifecycle-algorithm.md
- throwaway-html-editor-structured-input-surface.md
date_added: '2026-07-12'
date_processed: '2026-07-12'
date_published: '2026-06-20'
---

Session-136 Pass 2 deep extraction (link-intake triage 2026-07-12, KB-ONLY verdict;
densest item in the batch). Transcript:
`app/transcript-fetcher/transcripts/iQyg-KypKAA.md` (45:46, ~10k tokens).

Channel note: Kun Chen is a new channel with no authority entry — deliberately not
created here (orchestrator owns authorities); recorded in the session's channels-seen
list. His adversarial fresh-context review stage echoes the rule-10/generator-assessor
findings owned by another lane this session — recorded as one-way related_findings on the
new pipeline finding only; those findings were not edited.
