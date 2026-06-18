---
name: "Data-Permanent Software-Ephemeral Knowledge Architecture"
summary: "Treat domain knowledge artifacts (skills files, context documents, distilled summaries) as the durable, precious layer — never discard them. Treat generated software/dashboards/tooling as ephemeral and regenerable. As models improve, throw away generated code and regenerate from original instructions + preserved context. Inverts the typical engineering instinct to protect code and discard notes."
implementation_notes: "MetaSystem already follows this directionally: KB findings are permanent, tooling is versioned. The explicit framing — throw away the software, keep the instructions — could formalize this as a design principle when reviewing artifact preservation policies."
category: "Context Engineering"
evidence_strength: "Anecdotal"
adoption_status: "Partially Adopted"
priority: "P3 (Monitor)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "self-improving-company-yc-five-layer-loop.md"
proposals: null
date_discovered: "2026-05-24"
last_updated: "2026-05-25"
related_findings:
  - file: "agent-architecture-layer-impermanence.md"
    rel: "extends"
  - file: "self-improving-knowledge-artifact-living-document.md"
    rel: "extends"
  - file: "progressive-diorization-pipeline-raw-to-breadcrumb.md"
    rel: "enables"
  - file: "total-organizational-legibility-as-ai-prerequisite.md"
    rel: "enables"
pipeline_status: "raw"
tags:
  - "context-engineering"
  - "knowledge-management"
---

# Data-Permanent Software-Ephemeral Knowledge Architecture

## What It Is

A design principle: domain knowledge artifacts (skills, context documents, distilled summaries, business rules) are the precious, permanent layer. Generated software (dashboards, tooling, one-off scripts) is ephemeral and regenerable. When models improve, discard generated code and regenerate from preserved instructions — no migration cost if you never treated the code as the artifact.

## Why It Matters

YC partner demonstrates this with internal systems: all emails stored as markdown (permanent), dashboards generated on-demand (disposable). YC user manual regenerated from 2,000 hours of recorded office hours in one weekend; now auto-updates monthly. The pattern eliminates software migration costs and makes model upgrades free from a data perspective.

## How It Could Fail

Some generated software accumulates state that cannot be regenerated (user configurations, runtime data). The boundary between "regenerable code" and "stateful system" needs explicit classification. Also, "throw away and regenerate" only works if the instructions/context are complete enough to reproduce equivalent output.
