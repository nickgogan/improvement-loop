---
name: "HTML Information Density: Eight Primitives vs. Markdown's Four"
summary: "Markdown carries four representational primitives (headings, bold, bullets, tables). HTML carries eight in a single file: tables, CSS-driven design, SVG illustrations, code snippets, live JavaScript interactions, SVG/HTML workflows, spatial data via absolute positioning, and embedded images. The format's expressiveness ceiling determines what the agent can communicate in a single artifact."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "markdown-vs-html-claude-code-derrick-anthropic.md"
related_findings:
  - file: "format-constrained-improvisation-tax.md"
    rel: "enables"
  - file: "html-output-as-human-in-the-loop-restorer.md"
    rel: "enables"
  - file: "html-artifact-as-skill-output-design-variations.md"
    rel: "enables"
  - file: "interactive-explanations-extend-linear-walkthroughs.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "classified"
tags:
  - "session-95-reextract"
---

# HTML Information Density: Eight Primitives vs. Markdown's Four

## What It Is

A comparative framework for evaluating output format expressiveness based on the number of representational primitives available in a single file.

**Markdown primitives (~4):**
1. Headings (hierarchy)
2. Bold/italic (emphasis)
3. Bullet/numbered lists (sequence)
4. Tables (tabular data, "if you squint at it")

**HTML primitives (~8):**
1. Tables (proper tabular data)
2. CSS-driven design (typography, color, layout, spacing)
3. SVG illustrations (charts, diagrams, icons)
4. Code snippets inside script tags (executable examples)
5. Live interactions via JavaScript and CSS (buttons, sliders, toggles)
6. Workflows drawn with SVG + HTML side by side (process diagrams)
7. Spatial data via absolute positioning (anything placeable on a canvas)
8. Embedded images via img tags (photos, screenshots, generated visuals)

Derrick (Anthropic/Claude Code): "There is almost nothing Claude can read that you cannot represent in HTML."

The 2x primitive count is the structural reason HTML documents are "easier to read, easier to organize visually, easier to navigate." More primitives means more channels for conveying information simultaneously — visual hierarchy, color-coded severity, spatial relationships, and interactive exploration can all coexist in one document.

## Why It Matters

The expressiveness ceiling of the output format bounds what the agent can communicate without resorting to workarounds (see: format-constrained-improvisation-tax). Markdown's four primitives are sufficient for linear prose documents — research findings, governance docs, session notes. But for artifacts that need to convey spatial relationships (architecture diagrams), quantitative comparisons (benchmark charts), or interactive decisions (parameter tuning), Markdown forces the model to either omit the information or improvise with ASCII art.

The practical implication: output format should be selected based on the information types the artifact needs to carry, not as a blanket default. Markdown is the right choice for prose; HTML is the right choice when the information includes any of the four HTML-only primitives (SVG, interactions, spatial data, embedded images).

## Why People Are Using It

Derrick presents this as the foundational argument for the HTML-over-Markdown thesis. The eight-primitive catalog is not theoretical — each primitive is demonstrated in Derrick's gallery of example artifacts. The comparison is made concrete with side-by-side rendering: same five data points as a Markdown ASCII bar chart (fragile, imprecise) vs. an HTML SVG bar chart (crisp, portable, correct).

## Potential Improvements

- Format-selection rubric: if the artifact needs to carry information types 5-8 (interactions, workflows, spatial data, images), auto-select HTML. If it only needs types 1-4, Markdown is sufficient.
- Markdown extensions: some Markdown renderers support Mermaid diagrams, LaTeX, and embedded HTML blocks. These partially bridge the expressiveness gap without requiring full HTML authoring.
- Hybrid format: Markdown body with HTML islands for sections that need richer primitives. Obsidian already supports this to some degree.

## Potential Failure Modes

- **Expressiveness without purpose.** Having eight primitives available doesn't mean every document should use all eight. Over-designed HTML documents become as hard to navigate as under-designed Markdown walls of text.
- **Rendering environment dependency.** HTML's full expressiveness requires a modern browser. Terminal tools, Obsidian's renderer, and GitHub's Markdown preview all have limited HTML support. The eight-primitive advantage only holds in unrestricted browser rendering.
- **Generation complexity.** Correct HTML with CSS layout, SVG charts, and JavaScript interactions is harder for the model to generate than Markdown. The error rate on complex HTML output may negate the expressiveness advantage.
