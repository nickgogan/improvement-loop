---
name: "GStack + GSD + Superpowers Workflow Is Insane!"
source_type: "Video"
status: "Done"
key_takeaways: "Thin orchestrator session dispatches each phase as a separate claude -p headless subprocess. Each headless session gets a fresh context window, executes one phase, reports summary, exits. Orchestrator stays at <10% context utilization after 100+ headless sessions. 16-phase project completed overnight autonomously."
relevance: "High"
added_by: "Nick"
tags:
  - "context-engineering"
  - "orchestration"
  - "claude-code"
url: "https://www.youtube.com/watch?v=BlTpG51x94w"
authority: []
findings:
  - "build-loop-skill-autonomous-phase-driver.md"
  - "context-degradation-40-50-percent-threshold.md"
  - "framework-tension-taxonomy-superpowers-gsd-gstack.md"
  - "greenfield-brownfield-framework-selection-heuristic.md"
  - "gstack-specialist-role-architecture.md"
  - "lossy-compression-boundary-headless-return.md"
  - "multi-framework-orchestration-power-stack.md"
  - "orchestrator-headless-dispatch-context-isolation.md"
  - "phase-queue-state-file-as-orchestrator-memory.md"
  - "ralph-wiggum-execution-pattern.md"
  - "role-voting-for-autonomous-design-decisions.md"
  - "self-contained-phase-prompt-pattern.md"
  - "three-tier-orchestration-hierarchy-scheduler-worker-framework.md"
date_added: "2026-05-24"
date_processed: "2026-05-24"
date_published: "2026-05-01"
---

# GStack + GSD + Superpowers Workflow Is Insane!

Practitioner demo combining GStack, GSD plugin, and Superpowers workflow. Key pattern: orchestrator-delegates-to-headless-sessions for context isolation. 16/16 phases completed overnight with orchestrator at <10% context.
