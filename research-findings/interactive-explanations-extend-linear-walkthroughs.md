---
name: "Interactive Explanations Extend Linear Walkthroughs for Spatial/Temporal Algorithms"
summary: "A linear walkthrough (`walkthrough.md`) documents code structure — what's where, how files relate. An interactive explanation (an animated HTML tool) documents code behavior — what actually happens when the algorithm runs. They're complementary, not substitutes. Use linear when organization is the question; use interactive when behavior in space or time is the question. Plain English: if reading the code doesn't make it click, have the agent build you a tool you can play with to SEE it click."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P2
applicability:
  - "General"
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "simon-willison-interactive-explanations.md"
  - "understanding-is-the-new-bottleneck.md"
related_findings:
  - file: agent-generated-codebase-walkthrough-for-onboarding.md
    rel: extends
  - file: programmatic-snippet-extraction-via-shell-anti-hallucination.md
    rel: same-problem
  - file: "microworlds-ephemeral-interactive-debuggers.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-07-18"
pipeline_status: "synthesized"
consumed_by:
  - "structuring-agent-context.md"
---

## What It Is

A documentation-generation pattern where the output is a runnable, interactive single-page HTML app rather than a prose document. The agent is given existing code or documentation plus a detailed prompt specifying interaction affordances — text input with URL-fragment persistence, animation controls, frame-by-frame stepping, PNG export — and produces a self-contained HTML file that lets readers explore the algorithm's behavior.

Distinct from linear walkthroughs ([[agent-generated-codebase-walkthrough-for-onboarding]]) on two axes:

| Axis | Linear walkthrough | Interactive explanation |
|---|---|---|
| Question answered | How is this code organized? | What does this code do when it runs? |
| Output artifact | Markdown doc | HTML app |
| Reader interaction | Scroll + follow links | Click, drag, step, replay |
| Best for | Structure, dependencies, cross-references | Spatial algorithms, temporal processes, state machines |

Not a replacement for linear walkthroughs — the two complement each other. Structure-first artifacts read well; behavior-first artifacts play well. For complex algorithms, pairing both gives readers both mental models.

## Why It Matters

For MetaSystem's own documentation needs:
- **Governance visualizations.** The governance-visualization-brainstorm Nick has flagged in memory (`project_governance_visualization_wanted.md`) is a strong match for interactive explanation rather than linear walkthrough — DDs have a topology and a dependency structure that's easier to see than to read.
- **Agent-flow diagrams.** The IL's 4-agent architecture (Owner, Researcher, Codifier, Librarian) and the research-to-codification pipeline would benefit from a step-through animation more than a static diagram.
- **Memory-architecture triangle.** The Memongo / MemPalace / Supermemory comparison across four architectural poles (multi-store, single-store, verbatim, agentic) could ship as an interactive design-space explorer.

For code understanding more broadly: when an algorithm's complexity lives in its execution trace rather than its static structure (spiral-packing, tree-traversal, retry-logic, state-machine transitions), reading the source is not the best path to understanding. An animated visualization is often faster than a walkthrough + static diagrams.

A second, independent practitioner corroborates the core claim from the opposite side
of the author/reader relationship. Geoffrey Litt (Notion) reports the same
prose-is-insufficient-for-behavior conclusion, but applied to a builder's own
understanding rather than an audience's: agent-built ephemeral debuggers ("microworlds")
that a developer inhabits mid-task, thrown away once the intuition lands rather than
published as a deliverable. See `microworlds-ephemeral-interactive-debuggers.md` — same
underlying claim (interactive beats prose for spatial/temporal/state behavior),
generation-side rather than reader-side.

## Why People Are Using It

Observed in [Simon Willison's Agentic Engineering Patterns, Interactive Explanations chapter](https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/) — see [[simon-willison-interactive-explanations]] for the source entry. Simon's canonical example: an animated word-cloud tool showing real-time placement attempts by the Archimedean-spiral packing algorithm. Text: *"After reading a technical description of Archimedean spiral placement, I still didn't have an intuitive understanding of how that...part actually worked."* The visualization — which displays "little boxes showing where the algorithm is attempting to place them; if those boxes overlap an existing word it tries again" — made the mechanism click.

Tools used: Claude Code for web + Claude Opus 4.6. Output is a single-page HTML app, self-contained, shareable as a file or via URL. Generation cost is low (single prompt + a few iterations); consumption cost is also low (open in browser, click around).

## Potential Alternatives

- **Static diagrams** (Mermaid, Graphviz, PlantUML). Shareable, text-searchable, version-controllable. Can't convey dynamic behavior. Good for structure; weak for process.
- **Video walkthroughs** (screen-recording the algorithm running). High fidelity; not interactive; expensive to re-record when code changes.
- **Jupyter notebooks / Observable notebooks.** Interactive + code-adjacent. Requires a runtime; heavier than single-page HTML.
- **Whiteboard sessions with humans.** Gold standard for conveying intuition; doesn't scale, doesn't archive.
- **Linear walkthrough alone** ([[agent-generated-codebase-walkthrough-for-onboarding]]). Structure-first; weak on behavior. Complementary, not substitute.

## Potential Improvements

- **Standardize affordances.** A small vocabulary of common affordances (step / play / reset / URL-share / PNG-export / inspect-state) reduces per-artifact design cost.
- **Pair with a linear walkthrough.** Publish both artifacts for complex code; let readers switch between them.
- **Embed in the codebase.** Commit `walkthrough.md` + `interactive.html` alongside the code; they stay in sync via the same generation prompts.
- **Prompt-as-asset.** The generation prompt itself becomes a reusable skill — point it at different algorithms, get analogous interactive explanations.
- **Accessibility baseline.** HTML apps should keyboard-navigate and screen-read by default; machine-generated UIs often don't.

## Potential Failure Modes

- **Maintenance burden.** When the code changes, both artifacts need to be regenerated. Without automation, they drift. Mitigation: commit the generation prompts too; regeneration becomes a single command.
- **Complexity creep.** Interactive explanations can grow into full simulation apps that are themselves harder to understand than the original algorithm. Mitigation: scope tightly — one mechanism per artifact.
- **Browser-specific bugs.** Single-page HTML apps depend on browser JS runtime; older browsers or restricted environments may not render them. Mitigation: include a static fallback (screenshot + text description).
- **Hidden-state bugs.** Visualization may look correct but the underlying algorithm simulation has a bug — readers believe a false mental model. Mitigation: verify the visualization against the actual code's outputs on test inputs.
- **Replacement pressure.** Maintainers may skip the linear walkthrough because "the interactive one is cooler." The pair-is-better-than-either property is lost. Mitigation: treat them as complementary in docs-generation skill contracts; both or neither.
