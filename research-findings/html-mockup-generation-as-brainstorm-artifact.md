---
name: "HTML Mockup Generation as Brainstorm Decision Artifact"
summary: "During the brainstorm phase, the agent generates local HTML pages served on localhost that present UI options for the human to compare visually — transforming abstract design questions ('how should the sync button look?') into concrete visual choices. The mockup is a decision artifact: it exists to elicit a human choice, not to serve as implementation reference."
implementation_notes: null
category: "Intent Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P3
applicability:
  - "S3 (Claude Code Build)"
sources:
  - "claude-code-plus-superpowers-tutorial.md"
related_findings:
  - file: "brainstorming-as-mandatory-design-gate.md"
    rel: "extends"
  - file: "superpowers-plugin-spec-driven-sub-agent-orchestra.md"
    rel: "extends"
  - file: "agent-proof-of-work-ui-trust-building.md"
    rel: "same-problem"
adopted_in: []
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "classified"
consumed_by: []
tags:
  - "session-95-reextract"
---

# HTML Mockup Generation as Brainstorm Decision Artifact

## What It Is

During the brainstorm phase of a spec-driven development workflow, the agent generates a local HTML page served on localhost that presents multiple UI design options side by side for the human to compare visually. The human reviews the mockups in a browser and selects their preferred option (e.g., "option C — dropdown split button"). The selected option is then recorded in the spec document that flows downstream to planning and execution.

In the observed Superpowers workflow (Eric Tech tutorial, BookZero.ai):
1. The brainstorm skill identified that a UI decision was needed for the sync button placement
2. It generated an HTML page with three options: separate button, icon-only, dropdown split
3. The HTML was served on a local port and the user opened it in a browser
4. The user chose option C (dropdown split)
5. That decision was incorporated into the spec document

The mockup is a **decision artifact** — its purpose is to elicit a specific human choice, not to serve as a pixel-perfect implementation reference. The HTML is disposable; the decision it captures is durable.

## Why It Matters

Abstract design questions ("how should the sync button look?") produce abstract answers in text-only conversations ("maybe a dropdown?"). Visual mockups convert abstract preferences into concrete selections. The human is choosing between rendered options, not imagining options from prose descriptions.

This is a specific instance of a broader pattern: **using the agent's tool capabilities to generate artifacts that improve human decision quality.** The agent can write HTML, serve it locally, and let the human see rather than imagine. The composition insight is that brainstorm skills should not be limited to text Q&A — they should use whatever medium best supports the decision being made.

For MetaSystem: the IL pipeline does not have a visual decision artifact equivalent, but the pattern generalizes. Any phase that requires a human choice between options could benefit from generating a comparison artifact (table, diagram, mockup) rather than listing options in prose.

## Why People Are Using It

Demonstrated in Superpowers' brainstorm skill (Eric Tech tutorial). The HTML mockup generation is described as a feature of the brainstorm phase, not a separate tool. The skill decides when a visual comparison would help and generates the mockup autonomously.

The agent-proof-of-work finding documents a related pattern: agents generating visual previews to build trust. The difference here is purpose — this is about decision quality, not trust-building.

## Potential Improvements

- Interactive mockups rather than static HTML: let the user click through flows, not just see static layouts
- Mockup annotations: label each option with tradeoffs (e.g., "option A: simplest but less discoverable; option C: most flexible but more complex UI")
- Mockup-to-spec automation: when the user selects an option, automatically extract the relevant UI constraints into the spec document
- Template library of common mockup patterns (button placement, modal layouts, list views) to reduce generation time and improve consistency

## Potential Failure Modes

- **Mockup fidelity misleads.** If the mockup is too polished, the human may expect the final UI to match exactly. If too rough, the human may reject a good option because it looks bad. The mockup's visual quality should be calibrated to "good enough for the decision, not good enough for production."
- **Token cost for visual generation.** Generating HTML with CSS for multiple options is token-intensive relative to listing options in text. For decisions where text comparison suffices (e.g., naming conventions, API design), mockups add overhead without improving decision quality.
- **Decision captured but rationale lost.** The spec records "user chose option C" but not "because the dropdown accommodates future sync actions without new buttons." The decision artifact captures WHAT was chosen but not WHY.
- **Browser context-switch friction.** The user must leave the terminal, open a browser, navigate to localhost, review the mockup, then return to the terminal to respond. For rapid brainstorming, this context switch slows the conversation.
