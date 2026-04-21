---
name: "Programmatic Snippet Extraction via Shell — Anti-Hallucination Rule"
summary: "An explicit prompt-level rule: when an agent needs to include code snippets in an output (walkthrough doc, PR description, explanation), instruct it to extract them programmatically via `sed`, `grep`, or `cat` rather than type/copy them by hand. Manual copy from memory introduces hallucination risk even on short snippets. Simon Willison's verbatim rule: 'By telling it to use sed or grep or cat or whatever you need to include snippets of code, I ensured that Claude Code would not manually copy snippets, since that could introduce risk.'"
implementation_notes: "Directly actionable prompt-engineering rule. Add to CLAUDE.md or skill definitions for any skill that produces outputs containing code — walkthroughs, PR descriptions, docs generation, /compare skills. Standard phrasing: 'Use `sed`, `grep`, `cat`, or similar to extract code snippets from source files; do not type code from memory or reconstruct it from understanding.' Cheap to adopt, measurable effect on output accuracy."
category: "Prompt Craft"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "simon-willison-linear-walkthroughs-agentic-patterns.md"
related_findings:
  - file: agent-generated-codebase-walkthrough-for-onboarding.md
    rel: enables
  - file: programmatic-tool-calling-code-orchestrated-tool-use.md
    rel: same-problem
  - file: work-disavowal-failure-mode-context-limit-cheating.md
    rel: same-problem
  - file: agent-self-reporting-unreliability-independent-eval.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: classified
consumed_by: []
---

## What It Is

A prompt-level rule: when an agent produces output that contains code snippets quoted from a codebase (e.g., walkthrough documents, PR descriptions, annotated explanations), instruct it to extract the snippets via shell tools — `sed`, `grep`, `cat`, or equivalent — rather than typing or reconstructing the code from its understanding.

Simon Willison's exact phrasing: **"By telling it to use sed or grep or cat or whatever you need to include snippets of code, I ensured that Claude Code would not manually copy snippets, since that could introduce risk."**

The mechanism is simple: shell-extracted snippets are byte-accurate; hand-typed snippets are reconstructed from the model's working understanding of the file, which may differ from the actual bytes in subtle ways.

## Why It Matters

Two distinct failure modes are prevented:

1. **Direct hallucination** — the model writes code that doesn't exist in the file (a function signature that looks right but isn't what the file contains).
2. **Stale mental model** — the model quotes code as it was earlier in the session (before an edit), not as it is now.

Both produce plausible-looking output that is subtly wrong, which is exactly the class of error that standard review catches least reliably. The mitigation is cheap: one sentence of prompt instruction shifts the extraction from memory to filesystem.

This is a close cousin of [[programmatic-tool-calling-code-orchestrated-tool-use.md]] — both move work from inference to execution — but operates at a much smaller scope (snippet extraction in documentation, not full workflow orchestration).

## Why People Are Using It

Simon Willison's "Agentic Engineering Patterns" guide, Linear Walkthroughs chapter. First-party author testimony from his SwiftUI "Present" project.

The rule generalizes beyond walkthroughs — any agent-produced output that quotes code is vulnerable to the same failure. PR descriptions that say "this change affects function `foo(x, y)`" while the actual signature is `foo(x, y, opts)` mislead reviewers exactly as much as a hallucinated walkthrough does.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Post-hoc verification | Generate snippets freely, then diff against source files | When the verification loop is cheap and automated |
| Structured tool output | Have the agent call a `get_code_snippet(file, line_range)` tool | For harnesses that support custom tools; more expensive but stricter |
| Accept the risk | Allow manual copy for small snippets where accuracy is less critical | For exploratory or draft outputs |

## Potential Improvements

- **Make it a hook rather than a prompt rule** — block agent outputs containing code blocks that don't correspond to actual file content. Automated enforcement beats prompt hope.
- **Generalize beyond shell tools** — any read-only extraction (AST query, file-read tool) satisfies the rule. Phrasing should be "use a read-only source access path, not your memory."
- **Detect at review time** — diff the quoted snippets in a walkthrough/PR-description against the source files. Fail CI if they don't match.

## Potential Failure Modes

- **Agent ignores the instruction** — models can still shortcut to memory-based copy for small snippets; the rule is prompt-level, not enforced.
- **sed/grep errors silently** — a failed command returns nothing, and if the agent doesn't check, the snippet is silently empty or wrong.
- **Over-application** — forcing shell-based extraction for every reference (including trivial ones like quoting a built-in function name) adds unnecessary tool calls.
- **Harness doesn't expose shell** — in sandboxed environments without shell access, the rule has to be adapted to whatever read-only access the harness provides.
