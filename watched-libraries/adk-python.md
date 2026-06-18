---
name: "ADK-Python"
type: "watched-library"
repo_url: "https://github.com/google/adk-python"
description: "Google's Agent Development Kit — code-first Python framework for building, evaluating, and deploying sophisticated AI agents with flexibility and control. Features agent composition, tool integration, built-in evaluation, and deployment abstractions."
spectrum_position: "cherry-pick"
what_we_use: "Agent evaluation framework patterns, tool integration abstractions, agent composition model, deployment and lifecycle patterns"
local_derivations: []
last_evaluated_version: "v2.0.0"
last_evaluated_date: "2026-05-25"
maintainer: "google"
status: "active"
tags:
  - "agent-framework"
  - "evaluation"
  - "tool-integration"
  - "orchestration"
  - "python"
  - "google"
related_findings: []
related_sources: []
date_added: "2026-05-25"
---

## What It Does

Google's open-source, code-first Python framework for building AI agents. Provides structured abstractions for agent composition, tool definition, evaluation suites, and deployment. Emphasizes flexibility and control — agents are Python objects with declarative configuration rather than visual graphs. Includes built-in evaluation primitives and deployment tooling.

## What We Use From It

Cherry-pick patterns:
1. **Agent evaluation framework** — Built-in eval primitives, test harness patterns, evaluation suite composition
2. **Tool integration abstractions** — How tools are defined, registered, and made available to agents
3. **Agent composition model** — How agents are composed, nested, and orchestrated
4. **Deployment and lifecycle patterns** — Agent packaging, versioning, and deployment abstractions

## Spectrum Rationale

**Cherry-pick** — ADK is a Python framework from Google targeting agent builders who want code-first control. While MetaSystem operates in the Claude Code / markdown context engineering space, ADK's evaluation framework patterns, tool definition abstractions, and agent composition model offer directly applicable concepts. The evaluation primitives are particularly relevant given IL's interest in agent quality gates.

## Change Signals

Watch for:
- Evaluation framework expansions (new eval types, metrics)
- Agent composition model changes (nesting, delegation)
- Tool definition pattern evolution
- Memory and state management primitives
- Multi-agent coordination features
- Context management patterns
