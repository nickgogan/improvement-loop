---
name: "Don't build more AI agents until you watch this"
source_type: "Video"
status: "Done"
key_takeaways: |-
  The harness-maintenance thesis: agents break in two directions — the world drifts
  around them AND the model inside them improves — so harnesses need scheduled fitness
  reviews, not launch-and-forget. Measured anchor: Vercel made its SDR agent better by
  deleting 80% of its tools. Five durable patterns: bidirectional agent breakage
  (over-restriction traps better models); tool pruning as maintenance discipline; a
  five-point agent health checklist (inputs current / reach fits model / job drifted /
  proof linkable / value real); harness depth as a maintenance-ownership tradeoff; and
  build from the observed workflow, not the paper workflow. Frames Stewart Brand's
  "Maintenance of Everything" (agents as sailboats, not apps) and the frontier-lab bet
  that better models ship better harnesses faster.
relevance: "High"
added_by: "Nick"
tags:
  - "tools"
  - "evaluation"
  - "multi-agent"
url: "https://www.youtube.com/watch?v=BOXK2XFLA-E"
authority:
  - "nate-b-jones.md"
findings:
  - "bidirectional-agent-breakage-world-drift-model-improvement.md"
  - "tool-pruning-as-harness-maintenance.md"
  - "five-point-agent-health-checklist.md"
  - "harness-depth-as-maintenance-ownership.md"
  - "build-from-observed-workflow.md"
  - "frontier-model-as-harness-designer.md"
date_added: "2026-07-13"
date_processed: "2026-07-13"
date_published: "2026-06-17"
---

# Don't build more AI agents until you watch this

Nate B Jones (AI News & Strategy Daily), 18:25, uploaded 2026-06-17. Pass 2 deep
extraction completed 2026-07-13 from the full local transcript
(`app/transcript-fetcher/transcripts/BOXK2XFLA-E.md`).

Part of the three-source "Nate B Jones" leg of the pending named-deps gap-check. This
source anchors the **harness-fitness-review** side: what his framework asks of a
well-run agentic system is a scheduled review that checks both drift directions — the
exact trigger the engine's model-capability-registry refresh half-embodies.

Five new findings extracted; one existing finding
(`frontier-model-as-harness-designer.md`) extended with the frontier-lab
harness-flywheel strategy rather than duplicated.
