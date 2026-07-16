---
name: Bun Hot-Reload Interactive HTML Artifact Feedback Loop
summary: Running a Claude Code-generated HTML artifact through a local Bun server enables in-place annotation (click to pin comments) and hot-reload on file save, creating a tight visual feedback loop where
  users annotate decisions directly in the rendered UI and export them as structured JSON for Claude Code to action.
implementation_notes: null
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Strong / needs design)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- interactive-html-artifacts-claude-code-bun.md
related_findings:
- file: html-artifact-as-skill-output-design-variations.md
  rel: enables
- file: claude-code-channels-telegramdiscord-as-agent-inte.md
  rel: same-problem
- file: throwaway-html-editor-structured-input-surface.md
  rel: extended-by
proposals: null
date_discovered: '2026-04-20'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- designing-agent-tools.md
---
# Bun Hot-Reload Interactive HTML Artifact Feedback Loop

## What It Is
After generating an HTML artifact (see [[html-artifact-as-skill-output-design-variations]]), instead of viewing it as a static file, Claude Code spins up a lightweight Bun server that:
1. Serves the HTML on a local port
2. Watches the file for changes and hot-reloads in the browser
3. Overlays a comment/annotation UI — click anywhere to pin a comment bubble
4. Adds an "Export to JSON" button that copies all pinned comments to the clipboard

Workflow: view artifact in browser → click on areas of interest → leave natural-language comments ("make this 10 avatars", "add country flags here") → press Export to JSON → paste JSON into Claude Code → Claude implements changes → file saves → browser hot-reloads automatically. No manual page refresh needed.

The Bun server is set up by asking Claude Code to convert a static HTML artifact to an interactive one: "Make this a Bun interactive HTML artifact running on a local server; add click-to-comment UI with an Export to JSON button."

Use cases beyond design review: interactive concept explainers (ask Claude Code to generate an animated diagram explaining a technical concept at 3 levels of depth — the artifact becomes a clickable learning tool).

## Why It Matters
The friction in iterating on visual output is the feedback path: see a problem → describe it in text → wait for regeneration. Bun hot-reload collapses the visual iteration loop: the rendered artifact becomes the annotation canvas, and the export gives Claude Code a structured, spatially-grounded set of changes rather than a text description that loses context. Hot-reload eliminates the "refresh and re-scroll to where I was" overhead for each iteration.

## Why People Are Using It
Practitioners use this for UI component iteration, content layout decisions, and technical concept learning. The annotation-in-context pattern is especially valuable because clicking on the exact element that needs changing is more precise than describing it. Spatial annotation avoids the ambiguity of text references ("the second card from the left in the third row").

## Potential Improvements
Comments could include element metadata (CSS selector, DOM path) automatically, making Claude Code's targeting more deterministic. A "diff mode" in the hot-reload could highlight what changed between iterations. Integration with a screenshot tool could capture the pre-change state for A/B comparison.

## Potential Failure Modes
Bun must be installed on the developer machine — adds a setup prerequisite. If the HTML artifact becomes very large (many animated components), Bun's file-watching overhead may introduce latency. The JSON export is clipboard-based; if the clipboard is overwritten before pasting, annotations are lost. The human must still manually paste the JSON into Claude Code — Layer 3 (Claude Code Channels) eliminates this step but adds setup complexity.
