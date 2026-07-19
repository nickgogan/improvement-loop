---
name: "langchain-ai/openwiki"
type: "watched-library"
repo_url: "https://github.com/langchain-ai/openwiki"
description: |-
  LangChain's CLI that writes and maintains "agent wikis" — code mode builds and
  auto-updates repository documentation in openwiki/ (CI opens docs-update PRs on a
  schedule); personal mode builds a local "personal brain" wiki synthesized from
  ingested sources (local repos, Gmail, Notion, web search, Hacker News, X)
spectrum_position: "study"
what_we_use: |-
  Nothing adopted as code — study target. Primary interest: a shipped, CI-driven
  reflection loop that keeps a synthesized knowledge base current without a human
  re-deriving it — direct prior art for the E1 memory-layer reflection mechanism —
  plus its standardized concept format (Google's Open Knowledge Format) as a
  comparison target for the engine's frontmatter schema design
local_derivations: []
last_evaluated_version: "main (2026-07-18)"
last_evaluated_date: "2026-07-18"
maintainer: "langchain-ai"
status: "active"
tags:
  - "memory"
  - "knowledge-synthesis"
  - "documentation"
  - "typescript"
  - "claude-code"
related_findings: []
related_sources: []
date_added: "2026-07-18"
---

## What It Does

TypeScript CLI (MIT, ~12.3k stars within a month of its 2026-06-22 creation,
Trendshift-trending, actively pushed) that generates and maintains structured,
cross-linked wikis for agents. **Code mode** builds repository documentation into
`openwiki/` for the current codebase; running `--update` in CI (GitHub Actions /
GitLab / Bitbucket templates ship in-repo) auto-opens a docs-update PR so the wiki
tracks the code without human re-derivation. **Personal mode** builds a local
"personal brain" wiki at `~/.openwiki/wiki` from configured sources — local
repositories, Gmail, Notion, web search, Hacker News, X/Twitter. Provider-agnostic
model config. Emits concepts in Google's Open Knowledge Format (OKF).

## What We Use From It

Study target — nothing adopted as code yet. Three interest axes for the E1
memory-layer milestone: (1) the CI-triggered update loop is a working example of "one
reflection mechanism runs over an accumulation surface and keeps knowledge current" —
the exact shape E1's DoD names; (2) the OKF concept-doc schema is a comparison target
for the engine's own frontmatter/concept-doc design; (3) personal mode's
multi-source ingestion + synthesis is a reference implementation for
accumulation-surface design. Actual adoption (running openwiki over the engine) is a
separate Nick decision, not implied by this entry.

## Spectrum Rationale

Study. Registered from the 2026-07-18 link-intake run (Nick-accepted verdict). Notably
absent from the memory-spec 12-framework survey completed 2026-07-16 — this entry
closes that gap at the registry level; a /repo-analyzer pass and a memory-spec-corpus
addendum are separate follow-ups. First diff targets: the update-loop's change
detection (what triggers a wiki rewrite) and the OKF schema vs. `_schema.yaml`.

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-07-18 | main | Initial entry from the 2026-07-18 link-intake run (Nick-accepted verdict). Repo verified via GitHub API: 12,280 stars, MIT, TypeScript, created 2026-06-22. Flagged as a memory-spec survey gap. |
