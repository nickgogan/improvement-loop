# Improvement Loop — Generated Docs

Human- and agent-consumable visualizations and explainers for the IL system. Versioned by generation date.

## What Lives Here

`<YYYY-MM-DD>/<slug>.md` — one artifact per concept, in a folder dated by generation. Multiple artifacts in the same date folder are siblings (cross-link them).

## Hard Constraints

1. **No hardcoded counts.** Per `.claude/rules/governance.md` rule #3 ("Process"). If a count would be useful in the artifact, embed the query that produces it; never persist the number.
2. **Docs interpret canonical sources; they don't restate them.** Source of truth for system facts is `../CLAUDE.md`, `../agents/handoff-protocol.md`, agent definitions, DD frontmatter, and the constitution. Update those; let `docs/` regenerate against them.
3. **Owner-authored.** This folder is the Owner agent's surface. Other IL agents read only.

## Conventions

Each date folder's first-written artifact carries a "How to Read" section that subsequent siblings inherit (Mermaid format, color/shape vocabulary, click-target patterns, frontmatter shape). New artifacts document only their additions to the convention set, not the inherited parts.

## Adding a New Artifact

1. Pick the question it answers (structure / behavior / ownership / topology).
2. Pick the form — Mermaid for graphs / sequences / states; tables for matrix-shaped data.
3. Write to `<today's date>/<artifact-slug>.md` with frontmatter: `title`, `type: generated-docs`, `subject`, `generated`, `generator`, `regen_trigger`, `sources`.
4. Cross-link siblings in the same date folder.
5. Surface any drift discovered while compiling, in an "Observed Drift" section.
