---
title: "HTML PR Explainer with Margin Annotations"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "html-pr-explainer-with-margin-annotations"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agents or developers producing pull requests with complex or multi-file changes that require reviewer comprehension support"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "trivial — the HTML file is an additive artifact; removing it from a PR leaves the diff unchanged"
  auditability: "high when the generated HTML is attached to the PR record and versioned with the branch; low when the explainer is generated but not attached or re-generated on push"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "Derrick (Anthropic/Claude Code team) attaches this to every PR he creates as a habitual practice. No MetaSystem adoption yet; /code-review and /ship skills currently produce Markdown outputs."
contract:
  preconditions: "A pull request is being prepared that contains changes spanning multiple files, or changes where the 'why' is not self-evident from the diff alone. The diff content is available to the agent generating the explainer."
  invariants: "The HTML explainer is a review companion — it exists alongside the standard diff, not instead of it. Every change annotated in the HTML must correspond to a real change in the diff; no annotations may be fabricated. Severity classifications (critical/cosmetic) are assigned based on code analysis — API surface changes, test coverage delta, security-sensitive file changes — not guessed. The explainer is regenerated on each new push to the branch; a stale explainer is worse than no explainer."
  governance: "Owner: the agent or developer creating the PR. The explainer is optional for single-file or trivial changes (under ~20 lines changed). For complex multi-file changes, attachment is the default. Severity misclassification (marking critical as cosmetic) is a quality failure — the template's severity criteria must be applied, not approximated. The HTML file is named `pr-explainer.html` and attached as a PR artifact or comment."
  recovery: "If the explainer becomes stale (new commits after generation) → regenerate before the reviewer reviews; mark stale explainers with a visible warning banner. If severity classification is contested by a reviewer → treat the disagreement as calibration feedback; adjust the severity criteria in the template variation. If the HTML file cannot be rendered in the review environment → fall back to a Markdown version with the same structure; do not omit the annotations."
tags:
  - "extracted-artifact"
  - "template"
  - "code-review"
  - "pr-workflow"
  - "html-output"
---

# HTML PR Explainer with Margin Annotations

**Source:** [[html-pr-explainer-with-margin-annotations]]
**Form:** template
**Extraction date:** 2026-05-25

## Variables

| Variable | Description |
|----------|-------------|
| `{{PR_TITLE}}` | Title of the pull request |
| `{{PR_BRANCH}}` | Branch name |
| `{{PR_AUTHOR}}` | Author of the PR |
| `{{GENERATED_AT}}` | Timestamp when the explainer was generated |
| `{{COMMIT_SHA}}` | Commit SHA this explainer was generated from |
| `{{DIFF_SECTIONS}}` | List of changed files and their diff sections (populated programmatically) |
| `{{ANNOTATIONS}}` | List of margin annotation objects: `{file, line_range, severity, why}` |

---

## Body

The template below is the structural scaffold for the HTML PR explainer. Replace variables and populate diff sections and annotation objects programmatically from the diff.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>PR Explainer: {{PR_TITLE}}</title>
  <style>
    /* Layout */
    body { font-family: monospace; margin: 0; display: flex; flex-direction: column; }
    .header { padding: 1rem 2rem; background: #1a1a2e; color: #e0e0e0; }
    .header h1 { margin: 0; font-size: 1.1rem; }
    .meta { font-size: 0.8rem; color: #aaa; margin-top: 0.3rem; }
    .nav-bar { padding: 0.5rem 2rem; background: #16213e; display: flex; gap: 1rem; overflow-x: auto; }
    .nav-bar a { color: #4fc3f7; text-decoration: none; font-size: 0.85rem; white-space: nowrap; }
    .nav-bar a:hover { text-decoration: underline; }
    .content { display: grid; grid-template-columns: 1fr 320px; gap: 0; }

    /* Diff section */
    .diff-section { padding: 1.5rem 2rem; border-right: 1px solid #333; }
    .diff-section h2 { font-size: 0.95rem; color: #81d4fa; margin-top: 2rem; margin-bottom: 0.5rem; }
    .diff-section h2:first-child { margin-top: 0; }
    pre { background: #0d1117; border: 1px solid #30363d; border-radius: 4px; padding: 1rem;
          overflow-x: auto; font-size: 0.8rem; line-height: 1.5; }
    .line-added { color: #3fb950; }
    .line-removed { color: #f85149; }
    .line-context { color: #8b949e; }

    /* Margin annotations */
    .annotations { padding: 1.5rem 1rem; display: flex; flex-direction: column; gap: 1rem; }
    .annotation { border-left: 3px solid; border-radius: 4px; padding: 0.75rem; font-size: 0.82rem; line-height: 1.4; }
    .annotation.critical  { border-color: #f85149; background: #1c0a0a; }
    .annotation.important { border-color: #e3b341; background: #1a1400; }
    .annotation.cosmetic  { border-color: #58a6ff; background: #0a1628; }
    .annotation .tag { font-weight: bold; text-transform: uppercase; font-size: 0.7rem; letter-spacing: 0.05em; }
    .annotation.critical  .tag { color: #f85149; }
    .annotation.important .tag { color: #e3b341; }
    .annotation.cosmetic  .tag { color: #58a6ff; }
    .annotation .location { color: #8b949e; font-size: 0.75rem; margin: 0.2rem 0; }
    .annotation .why { color: #e0e0e0; }
    .related-link { color: #4fc3f7; font-size: 0.75rem; text-decoration: none; display: block; margin-top: 0.4rem; }
    .related-link:hover { text-decoration: underline; }

    /* Severity legend */
    .legend { padding: 0.5rem 2rem; background: #0d1117; font-size: 0.78rem; color: #8b949e;
              display: flex; gap: 1.5rem; border-top: 1px solid #333; }
    .legend span { display: flex; align-items: center; gap: 0.4rem; }
    .dot { width: 10px; height: 10px; border-radius: 50%; display: inline-block; }
    .dot.critical  { background: #f85149; }
    .dot.important { background: #e3b341; }
    .dot.cosmetic  { background: #58a6ff; }
  </style>
</head>
<body>

  <div class="header">
    <h1>PR Explainer: {{PR_TITLE}}</h1>
    <div class="meta">
      Branch: {{PR_BRANCH}} &nbsp;|&nbsp;
      Author: {{PR_AUTHOR}} &nbsp;|&nbsp;
      Generated: {{GENERATED_AT}} &nbsp;|&nbsp;
      Commit: <code>{{COMMIT_SHA}}</code>
    </div>
  </div>

  <!-- Jump links: one per changed file -->
  <nav class="nav-bar">
    {{DIFF_SECTIONS.forEach(section => `<a href="#${section.anchor}">${section.filename}</a>`)}}
  </nav>

  <div class="content">

    <!-- Left column: diff sections -->
    <div class="diff-section">
      {{DIFF_SECTIONS.forEach(section => `
      <h2 id="${section.anchor}">${section.filename}</h2>
      <pre>${section.rendered_diff}</pre>
      `)}}
    </div>

    <!-- Right column: margin annotations -->
    <div class="annotations">
      {{ANNOTATIONS.forEach(ann => `
      <div class="annotation ${ann.severity}">
        <div class="tag">${ann.severity}</div>
        <div class="location">${ann.file} &nbsp;L${ann.line_range}</div>
        <div class="why">${ann.why}</div>
        ${ann.related_anchor ? `<a class="related-link" href="#${ann.related_anchor}">→ Related: ${ann.related_label}</a>` : ''}
      </div>
      `)}}
    </div>

  </div>

  <div class="legend">
    <span><span class="dot critical"></span>Critical — API surface, security, data integrity</span>
    <span><span class="dot important"></span>Important — logic change, test coverage delta</span>
    <span><span class="dot cosmetic"></span>Cosmetic — style, rename, comment</span>
  </div>

</body>
</html>
```

---

## Usage

1. Run the explainer generator after the final commit on the branch (or hook it to a pre-push step).
2. Populate `{{DIFF_SECTIONS}}` by parsing the `git diff` output for the PR branch vs. base.
3. Populate `{{ANNOTATIONS}}` by running the agent over the diff — each annotation answers: what changed, why, and how critical.
4. Classify each annotation severity using the legend criteria:
   - **Critical:** API surface change, security-sensitive file, data schema change, removal of a public interface
   - **Important:** logic change, test coverage delta, dependency version bump, behavioral change
   - **Cosmetic:** rename, style, comment, whitespace, non-behavioral refactor
5. Add jump links (`related_anchor`) between annotations that refer to the same underlying change across files.
6. Save as `pr-explainer.html` and attach to the PR (as a comment attachment, linked artifact, or uploaded file).
7. If new commits are pushed → regenerate; do not leave a stale explainer without a staleness warning.

---

## Variation Axis

| Variation | Adjustment |
|-----------|-----------|
| Small PR (single file, <20 lines) | Skip the HTML; a plain PR description is sufficient; the overhead outweighs the benefit |
| Markdown-only environment | Replicate the structure as a fenced-code-block diff + annotation table; lose the jump links but retain the why/severity content |
| Severity auto-classification | Agent classifies severity via code analysis rules; reviewer can override; disagreements feed back to calibrate the severity criteria |
| Interactive review | Add JavaScript to allow inline reviewer comments on each annotation, creating a bidirectional review conversation in the HTML artifact |
| CI hook | Generate the explainer in CI on each push; post as a PR comment with a rendered preview link |

---

## Contract

### Preconditions
A pull request is being prepared that contains changes spanning multiple files, or changes where the "why" is not self-evident from the diff alone. The diff content is available to the agent generating the explainer.

### Invariants
The HTML explainer is a review companion — it exists alongside the standard diff, not instead of it. Every change annotated in the HTML must correspond to a real change in the diff; no annotations may be fabricated. Severity classifications are assigned based on code analysis, not guessed. The explainer is regenerated on each new push to the branch; a stale explainer is worse than no explainer.

### Governance
Owner: the agent or developer creating the PR. The explainer is optional for single-file or trivial changes. For complex multi-file changes, attachment is the default. Severity misclassification (marking critical as cosmetic) is a quality failure — the template's severity criteria must be applied, not approximated. The HTML file is named `pr-explainer.html` and attached as a PR artifact or comment.

### Recovery
If the explainer becomes stale (new commits after generation) → regenerate before the reviewer reviews; mark stale explainers with a visible warning banner. If severity classification is contested by a reviewer → treat the disagreement as calibration feedback; adjust the severity criteria in the template variation. If the HTML file cannot be rendered in the review environment → fall back to a Markdown version with the same structure; do not omit the annotations.
