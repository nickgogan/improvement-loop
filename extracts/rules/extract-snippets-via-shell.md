---
title: "Extract Code Snippets via Shell Tools, Never from Model Memory"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "programmatic-snippet-extraction-via-shell-anti-hallucination"
extraction_date: "2026-05-25"
last_change_session: 103
last_change_sl: "session-103-codifier-complete-extract-artifacts-write-phase"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "coding agents producing outputs that quote code from a codebase (walkthrough docs, PR descriptions, annotated explanations, review comments)"
    - "skill authors defining any skill whose output contains code blocks drawn from source files"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — a single prompt instruction; removal is a deletion with no migration cost"
  auditability: "high when shell commands and their outputs are logged verbatim; low when only the final output document is retained"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "The agent is producing an output (document, description, explanation) that includes code blocks quoted from source files in the repository. A shell or file-read tool is available to the agent."
  invariants: "Every code block in the output that quotes code from a source file is extracted via a read-only source access path (shell command, file-read tool, or equivalent) — not typed from memory, not reconstructed from understanding, not copy-pasted from the model's working context. The extraction command or tool call is retained in the session log as evidence."
  governance: "Owner: any skill, CLAUDE.md section, or agent definition that instructs the agent to produce code-quoting output (walkthroughs, PR descriptions, documentation generation). The extraction mandate must be stated explicitly in the prompt layer as a positive instruction — not as a negative prohibition. Skills that produce code-quoting output must declare this rule in their SKILL.md. The mandate extends to all read-only access paths — sed, grep, cat, a file-read tool — any path that returns bytes from the filesystem rather than the model's memory."
  recovery: "If a shell extraction command fails (no output, error): do not fall back to memory; surface the failure, fix the command (path, line range, syntax), and re-run. If a code block was written from memory (caught in review): replace it with a shell-extracted block; diff against the source file to confirm accuracy. If the environment has no shell access: adapt to the available read-only file-access tool; if no such tool exists, flag the snippet as unverified rather than present it as accurate."
tags:
  - "extracted-artifact"
  - "rule"
  - "prompt-engineering"
  - "anti-hallucination"
  - "code-quality"
---

# Extract Code Snippets via Shell Tools, Never from Model Memory

**Source:** [[programmatic-snippet-extraction-via-shell-anti-hallucination]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

A coding agent is producing an output that includes code blocks quoted from source files — walkthrough documents, PR descriptions, annotated explanations, review comments, or any other artifact where the agent reproduces code verbatim. The agent has access to a shell or file-read tool.

Scope: **code blocks quoted from source files.** This rule covers any case where the agent represents code as a quote from the codebase. It does not govern newly synthesized code (where the agent is authoring, not quoting), nor does it govern pseudocode or schematic examples.

## Action

**Required:** When producing output that includes a code block quoted from a source file, extract it via a read-only source access path — `sed`, `grep`, `cat`, a file-read tool, or any equivalent that reads bytes from the filesystem. Retain the extraction command or tool call in the session log as evidence. Verify that the extracted content matches the intended location (file path, line range) before including it.

**Forbidden:** Typing code from memory into an output document. Reconstructing a function signature, class definition, or snippet from the model's understanding of what the file contains. Treating an earlier in-session read of a file as sufficient basis for quoting its current content (the file may have been edited since).

Standard phrasing for prompt instructions: "Use `sed`, `grep`, `cat`, or a file-read tool to extract code snippets from source files; do not type code from memory or reconstruct it from understanding."

## Boundary

Enforced at the content-authoring step for any output containing code blocks that purport to quote source files. The rule fires when the agent is about to write a code block into its output. It does not apply to code the agent is synthesizing (writing for the first time) — only to code the agent is representing as already existing in the repository.

## Enforcement

- **Mechanism:** The agent must include the extraction command (or file-read tool call) in its response before the quoted block. The extracted content is what goes into the output. Downstream readers (human review, hook, audit) check that each quoted code block has a corresponding extraction artifact.
- **Check (deterministic):** For each code block in the output that quotes a source file: `(extraction_tool_called == true) AND (extracted_content == block_content)`. Either condition false → violation.
- **Violation response:**
  - *Block written from memory:* replace with shell-extracted version; diff against source to confirm accuracy.
  - *Extraction command failed silently:* surface the failure; do not fall back to memory; fix and re-run.
  - *No shell access in environment:* adapt to available file-read tools; if none exist, mark the snippet as unverified explicitly in the output.
- **Cannot be self-certified:** The extraction command's output must appear in the session log — not just the agent's assertion that it ran the command. For load-bearing outputs (PR descriptions that will be reviewed, walkthrough docs that will be shipped), hook-level enforcement (diff quoted snippets against source files) is more reliable than prompt-level instruction alone.

## Rationale

Two distinct failure modes are prevented by this rule:

1. **Direct hallucination.** The model writes a function signature that looks plausible but differs from what the file actually contains — a parameter renamed, a return type changed, a method that was deleted. The output looks right; reviewers check it against their mental model of the code rather than the file. The error ships.

2. **Stale mental model.** The model read the file earlier in the session, then an edit was made. The model quotes the pre-edit version because that is what it remembers. The file has changed; the quote has not.

Both produce plausible-looking output that is subtly wrong — exactly the class of error that review catches least reliably, because reviewers apply pattern-matching rather than byte-comparison.

The mitigation is cheap: one sentence of prompt instruction shifts the extraction from memory to filesystem. Shell-extracted snippets are byte-accurate by definition. The extraction command also creates an auditable artifact: if a reviewer questions a snippet, they can re-run the command and compare.

Simon Willison's formulation from the "Linear Walkthroughs" chapter of his Agentic Engineering Patterns guide: "By telling it to use sed or grep or cat or whatever you need to include snippets of code, I ensured that Claude Code would not manually copy snippets, since that could introduce risk."

**Distinction from `agent-self-reporting-unreliability-independent-eval`:** That rule governs task completion verification — whether an agent's claim of "done" should be independently confirmed. This rule governs code snippet extraction methodology — how code is physically obtained when quoting it in output. Different enforcement boundary: completion assessment vs. content authoring.

## Failure Modes

- **Agent ignores the instruction for small snippets.** Models may shortcut to memory-based copy for brief snippets, judging the extraction overhead disproportionate. Mitigation: state the rule without scope exceptions in the prompt; "small" is not a reliable self-assessment.
- **Extraction command fails silently.** A `sed` with an off-by-one line range returns empty output; the agent includes an empty block or falls back to memory. Mitigation: require the agent to verify the extracted content is non-empty before including it; treat empty extraction as a signal to fix the command, not to fall back.
- **Over-application adds unnecessary tool calls.** Forcing shell extraction for every reference (including trivial built-in function names or well-known API signatures) adds overhead with no accuracy benefit. Mitigation: scope the rule to code blocks that quote repository-specific content; general language constructs are exempt.
- **Harness has no shell access.** In sandboxed environments, `sed`/`grep`/`cat` may be unavailable. Mitigation: the rule generalizes to any read-only source access path — file-read tools, AST query tools, or equivalent. The key invariant is "read from filesystem, not from memory," not "use shell specifically."

## Contract

### Preconditions
The agent is producing an output (document, description, explanation) that includes code blocks quoted from source files in the repository. A shell or file-read tool is available to the agent.

### Invariants
Every code block in the output that quotes code from a source file is extracted via a read-only source access path (shell command, file-read tool, or equivalent) — not typed from memory, not reconstructed from understanding, not copy-pasted from the model's working context. The extraction command or tool call is retained in the session log as evidence.

### Governance
Owner: any skill, CLAUDE.md section, or agent definition that instructs the agent to produce code-quoting output (walkthroughs, PR descriptions, documentation generation). The extraction mandate must be stated explicitly in the prompt layer as a positive instruction — not as a negative prohibition. Skills that produce code-quoting output must declare this rule in their SKILL.md. The mandate extends to all read-only access paths — sed, grep, cat, a file-read tool — any path that returns bytes from the filesystem rather than the model's memory.

### Recovery
If a shell extraction command fails (no output, error): do not fall back to memory; surface the failure, fix the command (path, line range, syntax), and re-run. If a code block was written from memory (caught in review): replace it with a shell-extracted block; diff against the source file to confirm accuracy. If the environment has no shell access: adapt to the available read-only file-access tool; if no such tool exists, flag the snippet as unverified rather than present it as accurate.
