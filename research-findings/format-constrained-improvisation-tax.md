---
name: "Format-Constrained Improvisation Tax"
summary: "When the output format cannot express what the model knows (charts, colors, spatial layouts), the model improvises with lossy workarounds — ASCII bar charts, Unicode color swatches, pipe-and-dash diagrams. These workarounds are fragile (break on font change), imprecise (columns drift), and consume tokens for a degraded result. The format is the bottleneck, not the model."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "markdown-vs-html-claude-code-derrick-anthropic.md"
related_findings:
  - file: "html-output-as-human-in-the-loop-restorer.md"
    rel: "enables"
  - file: "html-artifact-as-skill-output-design-variations.md"
    rel: "same-problem"
  - file: "interactive-explanations-extend-linear-walkthroughs.md"
    rel: "same-problem"
  - file: "star-commands-for-explicit-output-format-override.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - "defending-agent-context.md"
tags:
  - "session-95-reextract"
---

# Format-Constrained Improvisation Tax

## What It Is

When an agent's output format cannot represent the information the model is trying to convey, the model improvises with lossy approximations. Derrick (Anthropic/Claude Code) catalogs the failure modes:

- **ASCII bar charts:** pipes and dashes that look like charts from a distance but have columns that drift and bars that don't align with axes. Break entirely when pasted into a document with a different font.
- **Unicode color swatches:** hash characters pretending to be color samples. Approximate at best.
- **Box-drawing diagrams:** boxes that pretend to be charts or spatial layouts, with no ability to convey scale, proportion, or relationship fidelity.

The model has the data and the understanding to produce a correct chart, a real color swatch, or an accurate spatial layout. The Markdown format forces it to "fake" these representations. When given HTML (with SVG, CSS, and JavaScript), the same model "stops faking the chart and just draws the chart."

The cost of format constraint: "forcing a powerful agent through a format built for a 1990s readme."

## Why It Matters

This identifies a specific failure mode in agent output: the information loss is not in the model's reasoning but in the serialization format. The model's internal representation is richer than what Markdown can express. Every time the model improvises with ASCII art, it is spending tokens to produce a degraded version of what it could produce natively in a richer format.

For MetaSystem: the IL knowledge base is entirely Markdown. This is appropriate for text-heavy findings and governance docs. But for patterns that involve spatial relationships (pipeline flow, agent topology, governance hierarchy), the current format forces the same improvisation tax. Interactive explanations and HTML artifacts are the known escape hatches.

The finding generalizes beyond HTML: any time the output format is less expressive than the model's internal representation, there is an improvisation tax. The fix is to match the output format's expressiveness to the information type being conveyed.

## Why People Are Using It

Derrick illustrates with a direct comparison: the same five data points rendered as a Markdown ASCII bar chart (fragile, imprecise) vs. an HTML SVG bar chart (crisp, correct, renders in any browser). Markdown carries eight representational primitives (headings, bold, bullets, tables). HTML carries tables, CSS design, SVG, code snippets, JavaScript interactions, workflows, spatial data, and images — "almost nothing Claude can read that you cannot represent in HTML."

## Potential Improvements

- Format-selection heuristic: if the output includes quantitative data, spatial relationships, or color, auto-select a richer format. If the output is pure prose, Markdown is sufficient.
- Declarative output constraints in skill contracts: specify which information types a skill produces and let the harness select the appropriate format
- Hybrid documents: Markdown body with embedded SVG/HTML blocks for the sections that need richer representation

## Potential Failure Modes

- **Over-correction.** Not all output needs rich formatting. A simple status message in HTML is overhead without benefit. The format should match the information complexity.
- **Rendering dependency.** HTML output requires a browser or HTML viewer. Terminal-only workflows cannot consume it. ASCII improvisation, while degraded, is universally renderable.
- **Generation fidelity.** The model's HTML/SVG output is not always correct — broken CSS, misaligned SVG elements, non-responsive layouts. The improvisation tax is replaced by a debugging tax if the rich format has errors.
