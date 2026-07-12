---
name: "HKUDS DeepTutor Structural Analysis"
source_type: "Tool Release"
status: "Done"
key_takeaways: "24k-star agent-native tutoring platform. Key pattern: two-layer plugin model — Level 1 single-shot Tools (LLM picks on demand) and Level 2 multi-stage Capabilities (pipelines that own the turn, with named stages). ChatOrchestrator routes UnifiedContext. StreamBus for event fan-out. Context-gated vs user-toggleable tool visibility."
relevance: "Medium"
added_by: "Nick"
tags:
  - "orchestration"
  - "agent-design"
  - "tools"
url: "https://github.com/HKUDS/DeepTutor"
authority: []
findings:
  - "two-layer-plugin-model-tools-vs-capabilities.md"
date_added: "2026-05-24"
date_processed: "2026-05-24"
date_published: "2025-12-28"
---

# HKUDS DeepTutor Structural Analysis

Structural analysis of `HKUDS/DeepTutor` (24k stars, Python). Agent-native tutoring platform with a clean architectural separation between single-shot tools and multi-stage capability pipelines.
