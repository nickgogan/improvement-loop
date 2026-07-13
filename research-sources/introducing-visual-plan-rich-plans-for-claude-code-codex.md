---
name: "Introducing /visual-plan — rich plans for Claude Code + Codex"
source_type: "Video"
status: "Done"
key_takeaways: |-
  Steve (Builder.io) open-sources /visual-plan and /visual-recap: plans and
  post-execution recaps rendered as MDX from reusable interactive components
  (pan/zoomable wireframes, commentable API specs, diagrams, schema views, annotated
  code), plus a CLI and a GitHub Action that posts a recap on every PR. Thesis: the
  plan level is becoming the abstraction engineers reason at, the way C displaced
  assembly — so plan artifacts must be consumable enough that the human gate actually
  functions. Best pattern-density-per-minute in the wave-3 batch (4:26 runtime).
  Flagged input for the parked governance-visualization work (IB-175) — extract before
  that session runs; the /visual-plan repo is a watched-library candidate (Nick's
  call, not actioned).
relevance: "High"
added_by: "Nick"
tags:
  - "claude-code"
  - "skills"
  - "tools"
url: "https://www.youtube.com/watch?v=NE0aBuQF0HA"
authority:
  - "builder-io.md"
findings:
  - "plan-level-as-engineering-reasoning-abstraction.md"
  - "mdx-visual-plans-with-reusable-components.md"
  - "visual-recap-post-execution-mirror-artifact.md"
date_added: "2026-07-13"
date_processed: "2026-07-13"
date_published: "2026-06-16"
---

Session-144 Pass 2 deep extraction (link-intake triage 2026-07-13, KB-ONLY verdict,
Nick-accepted). Transcript: `app/transcript-fetcher/transcripts/NE0aBuQF0HA.md`.

Triage estimated 4 novel patterns; extracted as 3 findings — the fourth (plan/recap as
CI artifact on every PR) is folded into the visual-recap finding per the group-related-
patterns rule. The video explicitly builds on Derrick's (Anthropic) markdown-vs-HTML
post, so the MDX and recap findings extend the existing HTML-output finding cluster
rather than duplicating it.

Follow-up flags carried from the accepted triage report:
- **IB-175 (governance visualization):** this source is the strongest input yet for
  that parked session — prose-heavy DDs/plans reviewed via bounded visual components.
- **Watched-library candidate:** Builder.io's open-source /visual-plan repo (skills +
  MDX generation app + CLI + GitHub Action) — Nick's call; no entry created here.
