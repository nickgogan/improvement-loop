---
name: "HTML-First Prototyping with Parameter Tuning and Cross-Platform Translation"
summary: "Claude sketches designs in HTML because HTML is the most expressive universal prototype language — even when the target surface is React, Swift, or another framework. The prototype includes interactive sliders and knobs for parameter tuning (animation timing, colors, spacing), and the tuned parameters are copied back into the prompt or code for the next step."
implementation_notes: null
category: "Tool Integration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3"
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "markdown-vs-html-claude-code-derrick-anthropic.md"
related_findings:
  - file: "html-artifact-as-skill-output-design-variations.md"
    rel: "extends"
  - file: "html-mockup-generation-as-brainstorm-artifact.md"
    rel: "same-problem"
  - file: "throwaway-html-editor-structured-input-surface.md"
    rel: "same-problem"
  - file: "bun-hot-reload-interactive-html-artifact-feedback-loop.md"
    rel: "extends"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "classified"
tags:
  - "session-95-reextract"
---

# HTML-First Prototyping with Parameter Tuning and Cross-Platform Translation

## What It Is

A prototyping workflow where the agent produces an interactive HTML prototype as the design exploration medium, regardless of the final target platform. The three-step pattern:

1. **Sketch in HTML.** Claude generates a self-contained HTML file with CSS and JavaScript that renders the design concept. HTML is chosen because it is "incredibly expressive for design" — more so than describing the design in prose or static mockups.

2. **Tune with sliders and knobs.** The prototype includes interactive controls — sliders for animation timing, color pickers, spacing adjusters. The human manipulates these controls until the design feels right. This captures design intent through interaction rather than specification.

3. **Copy parameters back.** The tuned parameter values are exported (copied back into a prompt, a config file, or the next agent session) and Claude translates the HTML prototype into the target framework (React, Swift, etc.).

Derrick (Anthropic/Claude Code): "Claude design is built on HTML for a reason. HTML is incredibly expressive for design. Even when your end surface is React or Swift or anything else."

## Why It Matters

Design intent is often embodied in specific parameter values (timing curves, spacing ratios, color relationships) that are difficult to specify in prose. "Make the animation faster" is ambiguous; setting a slider to 200ms is precise. The HTML prototype is a parameter-capture tool — its purpose is not to be the final artifact but to let the human discover and record their preferences through interaction.

The cross-platform translation step separates design exploration from implementation technology. The human evaluates the design in HTML (universally renderable, zero-setup) and the agent handles the translation to the target framework (which may have different constraints and idioms).

## Why People Are Using It

Observed in Claude Design (Anthropic's design-focused product) and recommended by Derrick for Claude Code workflows. The HTML-as-universal-prototype pattern is already the standard approach in Claude's product line — this finding documents the rationale and the parameter-tuning extension.

## Potential Improvements

- Parameter persistence: save tuned values to a JSON file alongside the HTML prototype so they survive across sessions
- Translation validation: after translating to the target framework, generate a side-by-side HTML comparison showing the prototype vs. the implementation to catch translation drift
- Template library: common prototype patterns (form layouts, data visualizations, navigation flows) with pre-wired parameter controls

## Potential Failure Modes

- **Translation fidelity.** The HTML prototype may use CSS features that don't map cleanly to the target framework (e.g., CSS grid to SwiftUI layouts). The human approves an HTML design that cannot be faithfully reproduced in the target platform.
- **Prototype as spec.** If the team treats the HTML prototype as a pixel-perfect specification, every deviation in the target framework becomes a "bug." The prototype should be explicitly framed as a parameter-capture tool, not a visual specification.
- **Token cost of interactive HTML.** Generating sliders, event handlers, and interactive controls costs more tokens than a static HTML mockup. For simple designs where parameter tuning is unnecessary, the interactive elements add overhead.
