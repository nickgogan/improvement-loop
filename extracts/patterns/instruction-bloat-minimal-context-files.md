---
title: "Instruction Bloat and Minimal Context Files"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "context-file-instruction-bloat-eth-zurich"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "The agent reads a context file (CLAUDE.md, rules, or equivalent) before task execution; the file's content influences agent behavior."
  invariants: "Context files contain only non-inferable information -- constraints the agent cannot discover by reading the codebase itself; file length stays within the empirical sweet spot (60-80 lines)."
  governance: "Context files are audited periodically against the non-inferable test; additions require justification; removals are the default."
  recovery: "If minimal context causes task failures, add back the specific missing instruction and document why it is non-inferable; do not revert to a verbose file."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Instruction Bloat and Minimal Context Files

**Source:** [[context-file-instruction-bloat-eth-zurich]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Context files (CLAUDE.md, .cursorrules, agents.md, etc.) grow unboundedly as teams add instructions for every new convention, tool, and edge case. Agents follow these instructions faithfully -- but faithfully following unnecessary instructions makes tasks harder, not easier. The agent explores more, tests more, and takes extra steps, following instructions precisely but unproductively.

## Forces

- **Accretion bias:** Instructions are easy to add and psychologically hard to remove. Teams default to "add a rule" whenever something goes wrong.
- **Faithful compliance:** Unlike humans who filter irrelevant instructions, agents process and act on everything they are given. Unnecessary instructions are not ignored -- they increase the agent's behavior space.
- **Discoverability asymmetry:** Some information (project structure, file locations, standard tooling) is discoverable by the agent through repo exploration. Other information (custom build commands, non-standard conventions, project-specific constraints) is not. Context files that include both waste capacity on the former.
- **Cost amplification:** Each unnecessary instruction adds 2.45-3.92 extra steps per task on average, increasing inference cost by 19-23% without improving success rates.
- **Tool mention sensitivity:** Mentioning a tool by name in context files increases its usage 160x, even when the tool is not the right choice for the task.

## Solution

Apply the **non-inferable test** to every line in a context file: could the agent discover this by reading the codebase itself? If yes, remove it. Keep only what the agent genuinely cannot infer:

**Keep (non-inferable):**
- Custom or non-standard build, test, and deploy commands
- Project-specific constraints and conventions that deviate from language/framework defaults
- Safety boundaries (what the agent must NOT do)
- Architectural decisions that are not visible in the code structure
- Team-specific workflow requirements

**Remove (inferable or counterproductive):**
- Codebase overviews and directory trees (the agent can `ls` and `find`)
- Standard tooling documentation (the agent knows common tools)
- Verbose explanations of framework conventions (the agent has training data)
- "Helpful" context that duplicates what the repo's own docs provide

**Operational benchmarks:**
- Target 60-80 lines for the primary context file (empirical sweet spot from ETH Zurich study and Anthropic internal usage).
- Prefer programmatic enforcement (linters, pre-commit hooks, AST validation) over prose instructions for code style and formatting rules.
- When a context file instruction can be replaced by a tool configuration or CI check, replace it.

## Consequences

**Positive:**
- Reduced inference cost (19-23% savings from removing unnecessary instructions).
- Fewer unproductive exploration steps (2.45-3.92 fewer steps per task).
- Agents focus on the task rather than complying with irrelevant instructions.
- Programmatic enforcement is more reliable than prose instructions -- linters do not have off days.

**Negative:**
- **Over-pruning risk:** Removing a safety constraint that appeared verbose but was load-bearing. The non-inferable test requires domain expertise to apply correctly.
- **Python-centric evidence:** The ETH Zurich study covers Python repos; results may not generalize perfectly to other languages or frameworks.
- **Cumulative benefits missed:** Static evaluation may undercount benefits of context files in repeated-task scenarios where conventions compound over many sessions.
- **Expertise requirement:** Knowing which instructions are truly non-inferable requires understanding what the agent can and cannot discover on its own -- a skill that itself takes experience to develop.

## Known Uses

- **ETH Zurich empirical study (arXiv 2602.11988, Feb 2026)** -- Tested 4 coding agents across 438 real-world tasks. LLM-generated context files reduced success by 3% and increased cost by 20%. Human-written files improved success by only 4% while increasing cost by 19%. Claude Code was the only agent where even human-written files failed to improve performance.
- **Community CLAUDE.md minimization movement** -- Practitioners replacing verbose files (200+ lines) with minimal ones (60-80 lines) after the study's publication, reporting quality improvements.
- **Anthropic internal usage** -- Internal context files converge on the 60-80 line sweet spot, corroborating the study's findings.

## Contract

### Preconditions
- The agent reads a context file before task execution and its content influences agent behavior.
- The codebase is accessible to the agent for exploration (the agent can read files, list directories, run tools).
- Someone with domain expertise can apply the non-inferable test to distinguish necessary from redundant instructions.

### Invariants
- Context files contain only non-inferable information -- constraints the agent cannot discover by reading the codebase itself.
- File length stays within the empirical sweet spot (60-80 lines for the primary file). Growth beyond this threshold triggers an audit.
- Tool mentions are deliberate -- naming a tool in context files is an explicit behavioral directive, not casual documentation.

### Governance
- Context files are audited periodically against the non-inferable test. The default action is removal; additions require justification.
- A diff-based review process tracks what was added, removed, or changed, and why.
- The audit cadence increases after periods of rapid instruction accretion (e.g., after onboarding new team members or tools).

### Recovery
- If minimal context causes task failures, add back the specific missing instruction and document why it is non-inferable. Do not revert to the previous verbose file.
- If the non-inferable test is applied incorrectly (something removed that was actually needed), the failure mode is visible in task results and the instruction can be restored surgically.
- Maintain a "removed instructions" log so that restored instructions are not re-removed in the next audit cycle.
