---
name: Code as Deterministic Tool Inside Skills (Script Execution Without Context Cost)
summary: Skills can bundle scripts in scripts/ that Claude runs via bash. The script's code never enters the context window — only the script's output (stdout/stderr) does. This makes scripts dramatically
  more efficient than having Claude regenerate equivalent logic, and provides deterministic reliability for operations LLMs are bad at (sorting, parsing, validation, network calls). Bundled scripts are
  part of the Level 3 progressive disclosure tier.
implementation_notes: 'Quote from the engineering post: ''Sorting a list via token generation is far more expensive than simply running a sorting algorithm.'' Example pattern: PDF skill bundles a Python
  script that extracts form fields — Claude executes it without loading either the script''s code or the PDF into context. Skills can also bundle scripts as documentation rather than executables (the author
  should make this clear in SKILL.md). Use ${CLAUDE_SKILL_DIR} in Claude Code skills to reference bundled scripts portably regardless of CWD.'
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-equipping-agents-with-agent-skills.md
- anthropic-agent-skills-overview-docs.md
- anthropic-claude-code-skills-docs.md
- anthropic-complete-guide-building-skills-pdf.md
related_findings:
- file: skill-as-directory-progressive-disclosure-three-levels.md
  rel: enabled-by
- file: mcp-as-code-api-progressive-tool-discovery.md
  rel: same-problem
- file: skill-dynamic-context-injection-shell-prerender.md
  rel: same-problem
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: synthesized
consumed_by:
- designing-agent-tools.md
---

# Code as Deterministic Tool Inside Skills

## What It Is

A skill can bundle executable scripts in a `scripts/` subdirectory. Claude executes them via bash from the SKILL.md instructions. The crucial property: **only the script's output enters the context window**. The script's code itself is never loaded into context — it lives on the filesystem and runs in the Claude environment.

This decouples three things that are normally bundled together:
1. **Behavior selection** (Claude decides to run the script — context cost: a line of SKILL.md guidance).
2. **Behavior execution** (the script runs deterministically — context cost: zero for the script body).
3. **Result integration** (Claude receives output — context cost: the output itself).

Compare to inline code generation: Claude writes equivalent logic in the conversation, pays full token cost for the code, and the result may not be deterministic across runs.

Anthropic's example: the PDF skill bundles a Python script that extracts form fields. Claude calls the script without loading either the script's code or the PDF into context.

## Why It Matters

Two distinct benefits that compose:

**Efficiency.** Long-form deterministic logic (sorting, parsing, validation, format conversion, schema enforcement) is grossly token-expensive when generated as LLM output. A 100-line script that runs in 50ms is dramatically cheaper than the equivalent tokens of Claude generating output that mimics the same logic — and the script result is the same every time.

**Determinism.** Many real workflows need bit-exact reproducibility — validating that a form has all required fields, parsing a specific file format, computing a hash, normalizing input. LLMs are unreliable at these. Code is reliable by construction.

The pattern reframes "what is a tool" — instead of an MCP-served capability or a hard-coded Claude Code tool, a tool can be a script the skill author chose to bundle for exactly this workflow.

## Why People Are Using It

Documented across all canonical Anthropic sources as a first-class design pattern. Anthropic's own production document skills (docx, pdf, pptx, xlsx) ship with bundled Python scripts for deterministic parts of the workflow. The skill-creator skill ships an `eval-viewer/generate_review.py` script that the skill executes rather than asking Claude to regenerate HTML. The Complete Guide PDF lists "scripts/ (optional): Executable code (Python, Bash, etc.)" as a canonical skill component.

## Potential Alternatives

MCP-served tools (heavier — requires a separate process and protocol). Inline LLM code generation (cheap to author but expensive per-invocation and non-deterministic). Tool definitions registered via the API (require external infrastructure). Sub-agents spawned for the deterministic step (overkill for pure compute).

## Potential Improvements

Standard script harness with structured output (JSON envelopes, error codes) so Claude can robustly interpret results. Per-skill script-level versioning. Sandboxing guidance for skill scripts in untrusted contexts. The Agent Skills open standard does not yet specify script execution semantics — currently each surface (Claude.ai, Claude Code, API) has its own runtime constraints.

## Potential Failure Modes

**Hidden dependencies.** Bundled scripts can have system dependencies (Python version, packages, OS tools) that aren't declared. On surfaces with `compatibility:` field guidance, authors are nudged to declare them; on others, the script fails at runtime with no clean recovery path.

**Path resolution from a different CWD.** Without `${CLAUDE_SKILL_DIR}` (Claude Code) or equivalent, bundled script paths can be wrong when the skill runs from a project subdirectory. Hard-coding `scripts/foo.py` breaks across surfaces.

**Script-as-documentation confusion.** A script bundled as reference (Claude should read it as documentation) vs. executable (Claude should run it) is ambiguous without clear SKILL.md guidance.

**Security surface expansion.** A bundled script can do anything the user environment permits — file deletion, network exfiltration, credential access. The "audit before trust" obligation falls on the user/admin, but the script body isn't in the system prompt where it would otherwise be visible.

**Network unavailability on surface mismatch.** Claude API runtime has no network; a skill whose bundled script makes HTTP calls works on Claude Code but fails on the API.
