---
name: "One-Shot PRD Prompt for Full System Bootstrap"
summary: "A single declarative PRD prompt pasted into Claude Code with zero other context scaffolds an entire system (folders, scripts, hooks, agents.md, index.md). Karpathy published a gist; Cole Medin's repo has an equivalent."
implementation_notes: "MetaSystem's /bootstrap could be enhanced to support PRD-as-prompt scaffolding rather than requiring manifest.json or interactive interview."
category: "Context Engineering"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
proposer_priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "self-evolving-claude-code-memory.md"
proposals: null
date_discovered: "2026-04-07"
last_updated: "2026-04-07"
pipeline_status: "synthesized"
consumed_by:
  - "managing-agent-context.md"
  - "templates/one-shot-prd-prompt-for-system-bootstrap.md"
---

# One-Shot PRD Prompt for Full System Bootstrap

## What It Is
A declarative bootstrap pattern where a single PRD document defines what a system should look like -- folder structure, index conventions, compilation rules, hook configuration -- and an agent one-shots the entire implementation. Karpathy's published gist is a PRD for an LLM KB system. Cole Medin has an equivalent working implementation.

## Why It Matters
This is distinct from imperative scaffolding (running install scripts) because the agent understands the design intent and can adapt. The PRD captures the "why" alongside the "what," enabling the agent to make intelligent decisions about implementation details that a script would need to hardcode.

## Why People Are Using It
Zero-context bootstrap: paste one document, get a fully scaffolded system. No prior setup, no manifest files, no interactive interview. The agent reads the PRD and builds everything in a single pass. Both Karpathy and Cole Medin have independently validated this pattern with working implementations.

## Potential Improvements
MetaSystem's /bootstrap skill currently uses manifest.json or interactive interview. A PRD-as-prompt mode would allow users to describe their desired system declaratively and let the agent handle structural decisions within the fractal pattern constraints.

## Potential Failure Modes
PRD ambiguity leads to inconsistent implementations across different sessions or agents. Without explicit constraints, two agents reading the same PRD may produce structurally different results. The PRD must be precise enough to be reproducible while remaining readable as a design document.

## Extraction Note — 2026-04-19
Extracted as **template**: [[one-shot-prd-prompt-for-system-bootstrap]] in `extracts/templates/`
