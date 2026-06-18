---
title: "Session 101: LINKS.md Repo Intake — 6 repos, 22 findings, cross-repo refresh"
type: "system-log"
date: "2026-05-25"
session: 101
agent: "researcher"
scope: "improvement-loop"
tags:
  - "repo-intake"
  - "watched-libraries"
  - "findings-promotion"
  - "cross-repo-comparison"
---

## What Happened

Researcher session processing 6 GitHub repos from LINKS.md into the IL pipeline. Full intake cycle: watched-library entries → shallow clone → structural analysis (5 dimensions each) → findings dedup → promotion → cross-repo comparison refresh.

## Key Outcomes

- **6 watched-library entries** created: langflow (monitor), adk-python (cherry-pick), autogpt (cherry-pick), autogen (monitor, maintenance-mode), crewai (cherry-pick), letta (cherry-pick)
- **6 structural analyses** produced via parallel subagents (~5 min each)
- **22 new findings** promoted (18 from individual analyses + 4 from cross-repo comparison)
- **3 existing findings** updated with new evidence (triple-storage evidence→Strong, dual-enforcement + sleeptime with cross-repo corroboration)
- **2 standalone URLs** processed (arXiv Mem0 paper, Oracle memory blog)
- **Cross-repo comparison** regenerated: 29 repos (up from 15), 7 new cross-repo patterns identified (CR-24 through CR-30)
- **Dedup rate:** 69% (36/52 individual candidates overlapped with existing KB)

## Observations

- Letta (formerly MemGPT) was highest-yield (7 findings) — memory architecture deeply relevant to Dimension 1
- CrewAI yielded 0 net-new despite 10 candidates — KB already well-covered in orchestration/delegation patterns from earlier intakes
- SKILL.md convergence now at 20/29 repos (69%) — de facto standard
- Graph execution engines at 6/29 repos — converging on model, diverging on semantics
- Parallel subagent execution worked well (6 analyses + 3 promotion batches + 1 comparison = 10 subagents total)

## Delta Report

`operations/research-reports/2026-05-25-session-101-repo-intake-delta.md`
