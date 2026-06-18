---
name: "HTML PR Explainer with Margin Annotations"
summary: "Attaching a generated HTML code explainer to every PR — with the diff rendered alongside margin annotations, severity colors, and jump links — makes code review more navigable than the default GitHub diff view. The HTML artifact is a review companion, not a replacement for the diff."
implementation_notes: null
category: "Tool Integration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2"
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "markdown-vs-html-claude-code-derrick-anthropic.md"
related_findings:
  - file: "visual-evidence-gate-for-ui-prs.md"
    rel: "same-problem"
  - file: "two-layer-ci-plus-llm-review-gate.md"
    rel: "same-problem"
  - file: "headless-multi-pass-iterative-review.md"
    rel: "same-problem"
  - file: "html-output-as-human-in-the-loop-restorer.md"
    rel: "extends"
  - file: "compound-review-debt-from-deferred-inspection.md"
    rel: "same-problem"
  - file: "bun-hot-reload-interactive-html-artifact-feedback-loop.md"
    rel: "extends"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - "templates/html-pr-explainer-with-margin-annotations.md"
  - designing-agent-tools.md
tags:
  - "session-95-reextract"
---

# HTML PR Explainer with Margin Annotations

## What It Is

Derrick (Anthropic/Claude Code team) attaches a generated HTML code explainer to every pull request he creates. The HTML artifact renders the PR diff alongside:

- **Margin annotations** explaining why specific changes were made
- **Severity colors** distinguishing critical changes from cosmetic ones
- **Jump links** for navigating between related changes across files

Derrick reports this "works better than the default GitHub diff view" for reviewers. The HTML explainer is a review companion artifact — it exists alongside the standard PR diff, not instead of it. It contextualizes the changes in a format designed for reviewer comprehension.

## Why It Matters

Code review is one of the primary human gates in software development. The default GitHub diff view is a flat, file-by-file list of changes with minimal semantic context. The reviewer must reconstruct the "why" from the code changes themselves. An HTML explainer pre-answers the reviewer's questions: why was this changed, how critical is it, and what else is related.

This is a specific application of the HTML-as-review-restorer pattern: rather than relying on PR descriptions (which suffer the same "wall of text" problem as Markdown specs), the review artifact is navigable and visually structured.

For MetaSystem: the `/code-review` and `/ship` skills produce Markdown review outputs. If the review output were HTML with jump links and severity coloring, the human gate quality at PR review time could improve.

## Why People Are Using It

Derrick creates this for every PR he makes — "and he is on the team" (i.e., an Anthropic engineer using this on the Claude Code codebase itself). The practice is habitual, not experimental. It addresses the specific problem that PR descriptions are often skimmed, and diff views lack semantic context.

## Potential Improvements

- Auto-generation: a post-commit hook or skill that generates the HTML explainer from the diff + commit messages, reducing manual effort
- Interactive annotations: the reviewer could add their own annotations in the HTML (see bun-hot-reload pattern), creating a bidirectional review conversation
- Severity auto-classification: the agent classifies change severity based on code analysis (test coverage delta, API surface changes, security-sensitive files)

## Potential Failure Modes

- **Maintenance of the explainer.** If the PR is revised after the explainer is generated, the explainer becomes stale. It needs regeneration on each push.
- **Trust in severity classifications.** If the agent marks a critical change as low-severity, the reviewer may skip it based on the color coding. The severity colors must be calibrated to avoid false-negative classifications.
- **Overhead for small PRs.** A single-file, 10-line change doesn't need an HTML explainer with jump links. The pattern is most valuable for complex, multi-file changes.
- **GitHub integration friction.** HTML files attached to PRs must be downloaded and opened in a browser — they don't render inline in the GitHub UI. This adds a review step.
