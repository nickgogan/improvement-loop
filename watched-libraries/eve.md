---
name: "vercel/eve"
type: "watched-library"
repo_url: "https://github.com/vercel/eve"
description: |-
  Vercel's filesystem-first framework for durable AI agents ("The Framework for
  Building Agents"). An agent is a conventional folder — instructions.md (always-on
  system prompt), agent.ts (model/runtime config), tools/, skills/, channels/
  (HTTP, Slack, Discord), schedules/ (cron) — compiled into one manifest with no
  explicit wiring
spectrum_position: "study"
what_we_use: |-
  Nothing adopted as code — study target. Primary interest: the folder-as-compiled-
  manifest asset model as working prior art for the engine's portable JSON/YAML
  asset-description language (Nick-ruled queue item 3), plus durable/checkpointed
  sessions and evals-as-deploy-gate as framework defaults
local_derivations: []
last_evaluated_version: "main (2026-07-18, pre-1.0 npm releases)"
last_evaluated_date: "2026-07-18"
maintainer: "Vercel"
status: "active"
tags:
  - "agent-framework"
  - "typescript"
  - "session-management"
  - "skills"
  - "orchestration"
related_findings:
  - "agent-as-folder-compiled-to-manifest.md"
  - "durable-checkpointed-sessions-as-framework-default.md"
  - "evals-folder-as-first-class-deploy-gate.md"
related_sources:
  - "vercel-eve-file-system-agent-framework.md"
date_added: "2026-07-18"
---

## What It Does

Filesystem-first TypeScript framework for durable AI agents (Apache-2.0, ~3.9k stars
within a month of its 2026-06-16 creation, actively pushed). Core agent capabilities
live in conventional folder locations — `agent/instructions.md` (required always-on
system prompt), `agent.ts` (optional model/runtime config), `tools/` (typed callable
functions), `skills/` (on-demand markdown procedures), `channels/` (HTTP/Slack/Discord
message surfaces), `schedules/` (recurring cron jobs) — and a compile step traverses
the folder into a single manifest, so projects are inspectable and extensible without
explicit wiring. Durable/checkpointed sessions and eval gating ship as defaults rather
than bolt-ons. Docs: https://eve.dev/docs.

## What We Use From It

Study target — nothing adopted as code. Three interest axes: (1) the
folder-as-compiled-manifest asset model is the closest shipped analog to the engine's
queued portable asset-description language (a compiler over a described asset tree) and
to the engine's own agent-as-directory pattern (DD-82/DD-86); (2) always-on checkpointed
sessions as a default informs the E4 harness/session design space; (3) evals-as-a-
first-class-folder informs the /meta-skill-author eval-discipline upgrade. Findings
extracted from the launch walkthrough (Cole Medin, 2026-07-16, disclosed sponsorship)
carry the pattern detail.

## Spectrum Rationale

Study. The engine is harness-first on Claude Code and does not need a second agent
runtime; the value is Eve's asset model and compile step as design reference. Nick
flagged the repo for the watch list at the 2026-07-18 link intake ("pull it in as a
watched repo"). First diff target for a future /repo-analyzer pass: the manifest
compiler and the folder-primitive vocabulary vs. the engine's asset-description draft.

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-07-18 | main | Initial entry from the 2026-07-18 link-intake run (Nick-accepted verdict). Repo verified via GitHub API: 3,853 stars, Apache-2.0, TypeScript, created 2026-06-16. |
