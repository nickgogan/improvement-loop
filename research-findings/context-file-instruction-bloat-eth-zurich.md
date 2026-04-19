---
name: Context File Instruction Bloat (ETH Zurich Empirical)
summary: ETH Zurich 2026 study proves agents follow context file instructions precisely, but unnecessary instructions make tasks harder. LLM-generated files reduce success by 3% and increase cost by 20%.
  Human-written files gain only 4%. Agents explore more, test more, and take 3-4 extra steps per task -- following instructions faithfully but unproductively.
implementation_notes: 'Validate against MetaSystem''s own CLAUDE.md files. Apply the 60-line rule (community benchmark sweet spot). Remove codebase overviews, directory trees, and anything the agent can
  discover by reading the repo. Keep only non-inferable details: custom tooling, unusual build commands, project-specific constraints.'
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- General
adopted_in: []
sources:
- eth-zurich-context-files-paper-march-2026.md
related_findings:
- file: claudemd-context-rot-from-indiscriminate-rule-accu.md
  rel: same-problem
- file: claudemd-minimum-viable-rule-only-add-globally.md
  rel: same-problem
- file: context-curation-over-context-stuffing.md
  rel: same-problem
- file: three-tier-vault-architecture-global-shared-local.md
  rel: same-problem
- file: context-file-taxonomy-claudemd-soulmd-agentsmd.md
  rel: same-problem
- file: pointers-over-copies-in-context-files.md
  rel: same-problem
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: claudemd-as-signal-to-noise-problem-not-size-probl.md
  rel: same-problem
- file: tiered-context-injection-over-monolithic-files.md
  rel: enables
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- managing-agent-context.md
---
## What It Is

The first rigorous empirical study of context file effectiveness (ETH Zurich, February 2026, arXiv 2602.11988). Tested 4 coding agents (Claude Code/Sonnet-4.5, Codex/GPT-5.2, GPT-5.1 mini, Qwen Code) across 438 real-world tasks using AGENTbench (138 novel tasks from niche repos) and SWE-bench Lite.

Key findings:
- LLM-generated context files **reduce** success rates by ~3% vs. no context file
- LLM-generated files increase inference cost by 20-23%
- Human-written files improve success by ~4% but increase cost by up to 19%
- Context files add 2.45-3.92 extra steps per task on average
- Agents follow instructions precisely -- the problem is the instructions themselves
- When all repo documentation was removed, LLM-generated files improved by 2.7% (proving they duplicate existing docs)
- Tool mentions in context files increase tool usage 160x (e.g., `uv` mentioned -> used 1.6 vs 0.01 times per instance)
- Claude Code was the ONLY agent where even human-written files failed to improve performance

## Why It Matters

This is the strongest empirical evidence against the "more context is better" assumption. The failure mode has a name in systems design: **instruction bloat**. The agent's behavior space is constrained by context that doesn't reduce ambiguity -- it increases cognitive load without reducing the search space. Agents don't filter gracefully; they process and act on everything they're given.

## Why People Are Using It

Community response has been significant. Practitioners are replacing verbose CLAUDE.md files with minimal ones (60-80 lines). Some are replacing markdown guidance entirely with programmatic enforcement (linters, pre-commit hooks, AST validation). Anthropic's own internal usage converges on the 60-80 line sweet spot.

## Potential Improvements

Tiered instruction injection: categorize instructions by operation type (coding, testing, reviewing) and inject only the relevant subset per task. This reduces context by 60-80% while maintaining accuracy. Claude Code already performs partial context management; future tooling will likely automate this.

## Potential Failure Modes

Over-pruning removes safety constraints. The study is Python-centric and covers relatively niche repos. Context files may have cumulative benefits in repeated tasks that static evaluation misses. The "minimal requirements" guidance requires knowing which requirements are truly non-inferable -- a skill that itself requires domain expertise.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[instruction-bloat-minimal-context-files]] in `extracts/patterns/`
