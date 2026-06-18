---
name: "Two-Layer Plugin Model: Tools vs Capabilities"
summary: "Separate single-shot Tools (LLM picks on demand, one function call) from multi-stage Capabilities (pipelines that own the turn, with named stages like rephrasing → decomposing → researching → reporting). A unified orchestrator routes context to the selected capability. All capabilities converge on a shared output envelope and emit events on a shared bus. Context-gated tools are always-on; user-toggleable tools surface in settings."
implementation_notes: "MetaSystem's skill system blurs this distinction — skills range from single-shot (transcript-fetcher) to multi-stage (research-loop). The DeepTutor pattern suggests formalizing this as two distinct registries with different dispatch mechanisms. The stage-naming convention could improve observability of multi-step skills."
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "deep-tutor-hkuds-analysis.md"
proposals: null
date_discovered: "2026-05-24"
last_updated: "2026-05-24"
related_findings:
  - file: "skill-as-package-export-with-references.md"
    rel: "same-problem"
pipeline_status: "synthesized"
consumed_by:
  - "agent-design-patterns.md"
  - "templates/tool-vs-capability-classification-stage-map.md"
tags:
  - "agent-design"
  - "orchestration"
  - "tools"
---

# Two-Layer Plugin Model: Tools vs Capabilities

## What It Is

An architectural pattern separating agent extensions into two layers:

- **Level 1 — Tools:** Single-function invocations the LLM picks on demand. One call, one result. Examples: web_search, code_execution, rag retrieval.
- **Level 2 — Capabilities:** Multi-stage pipelines that own the entire turn. Named stages (e.g., deep_research: rephrasing → decomposing → researching → reporting). The capability controls the loop until it produces a final result.

A unified `ChatOrchestrator` routes `UnifiedContext` to the selected capability. All capabilities converge on `emit_capability_result()` producing the same output envelope.

## Why It Matters

Conflating tools and capabilities in a single registry obscures the execution model — is this invocation a single function call or a multi-step pipeline? The two-layer model makes this explicit: tools are LLM-directed, capabilities are system-directed. This affects error handling (tool errors retry once; capability errors may require stage rollback), observability (tools log one call; capabilities emit per-stage events), and cost estimation (tools have predictable cost; capabilities accumulate across stages).

## How It Could Fail

The boundary between "complex tool" and "simple capability" is fuzzy. A tool with retry logic behaves like a mini-capability. Over-engineering the distinction adds registry overhead without clear benefit for simple agent systems.
