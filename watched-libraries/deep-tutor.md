---
name: "deep-tutor"
repo: "HKUDS/DeepTutor"
url: "https://github.com/HKUDS/DeepTutor"
description: "Agent-native personalized tutoring platform with two-layer plugin model (tools + capabilities), multi-stage pipeline capabilities, and StreamBus event architecture."
language: "Python"
stars: 24266
spectrum_position: "study"
tracking_focus:
  - "Two-layer plugin model (tools vs capabilities)"
  - "Capability stage pipeline pattern"
  - "StreamBus event fan-out architecture"
version_tracked: "latest (2026-05-24)"
last_analyzed: "2026-05-24"
analysis_doc: "watched-libraries/analysis/deep-tutor-analysis.md"
tags:
  - "agent-framework"
  - "multi-agent"
  - "rag"
  - "orchestration"
---

# deep-tutor

HKUDS/DeepTutor — agent-native tutoring platform. Two-layer plugin model: Level 1 single-shot Tools (LLM picks on demand) and Level 2 multi-stage Capabilities (pipelines that own the turn). ChatOrchestrator routes UnifiedContext to selected capability. All capabilities emit on a shared StreamBus for observability. 7 built-in capabilities with named stages (e.g., deep_research: rephrasing → decomposing → researching → reporting).
