---
name: "Omnigent"
type: "watched-library"
repo_url: "https://github.com/omnigent-ai/omnigent"
description: "Databricks-built open-source meta-harness — orchestrates coding-agent harnesses (Claude Code, Codex, Cursor, OpenCode, Hermes, Pi) with a policy layer and sandboxing"
spectrum_position: "study"
what_we_use: "Nothing adopted yet — study target. Policy layer (approval gates, spend caps, tool limits), harness-abstraction seams, YAML-defined custom agents, sandbox backend architecture"
local_derivations: []
last_evaluated_version: "alpha (2026-07-11 HEAD)"
last_evaluated_date: "2026-07-11"
maintainer: "omnigent-ai (Databricks, Inc. per NOTICE)"
status: "active"
tags:
  - "harness"
  - "orchestration"
  - "governance"
  - "sandboxing"
  - "agentic-os"
related_findings: []
related_sources: []
date_added: "2026-07-11"
---

## What It Does

Open-source (Apache-2.0, Python) meta-harness that runs your agents *above* the harnesses you
already use: one orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and
YAML-defined custom agents. Ships a policy layer (approval gates, spend caps, tool limits),
OS-level sandboxing (bwrap/seatbelt) with cloud sandbox backends (Modal, Daytona, E2B, K8s,
Databricks), real-time multi-user session sharing, and cross-device session continuity. Alpha
status but fast-growing (~7k stars in its first month; org created 2026-06-09). NOTICE file:
"Copyright (2026) Databricks, Inc." — shipped under a neutral org rather than the Databricks
brand. This is the "Omnigent" referenced in the session-129 agentic-OS direction note.

## What We Use From It

Study target — nothing adopted. It is a shipped instance of exactly the harness-layer +
governance-first architecture the agentic-OS direction is formalizing (design note
`project-management/design-notes/2026-06-22-agentic-os-direction.md`). The parts to mine: the
policy model (how access governance is expressed and enforced per agent), the seams of the
harness abstraction (what it must know about each underlying harness), YAML agent definitions
(a data-driven actors model), and the sandbox backend interface.

## Spectrum Rationale

Study. We don't run it (the engine operates inside Claude Code, not above it), but its
architecture answers open questions in our agentic-OS model — especially where orchestration
ends and intent governance begins (it ships access governance without a constitution layer,
which is the gap our model occupies). Resolves the design note's "Databricks has zero KB
coverage" flag. Prioritized `/repo-analyzer` pass queued (link-intake triage 2026-07-11).

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-07-11 | alpha HEAD | Initial entry from link-intake triage pilot. Provenance confirmed (Databricks NOTICE). /repo-analyzer pass queued, high priority. |
