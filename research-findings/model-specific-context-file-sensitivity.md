---
name: Model-Specific Context File Sensitivity
summary: Different models respond dramatically differently to context files. Claude Code (Sonnet-4.5) was the ONLY agent where even human-written context files failed to improve performance. GPT-5.1 mini
  exhibited redundant context-reading behavior (re-reading context files despite already having them). One-size-fits-all context strategies are empirically wrong.
implementation_notes: MetaSystem uses Claude Code exclusively. The ETH Zurich finding that Claude Code uniquely doesn't benefit from human-written context files should inform our CLAUDE.md optimization
  — Claude may already be good enough at self-discovery that most guidance is overhead.
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- eth-zurich-context-files-paper-march-2026.md
- glm-5-2-is-free-and-beats-claude-on-most-work.md
related_findings:
- file: context-file-instruction-bloat-eth-zurich.md
  rel: extends
- file: pointers-over-copies-in-context-files.md
  rel: same-problem
- file: harness-non-portability-across-model-families.md
  rel: extended-by
- file: provider-adaptive-prompt-rendering.md
  rel: extended-by
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- structuring-agent-context.md
- artifact: test-context-strategies-against-actual-model
  type: extracted-artifact
  form: rule
  date: 2026-04-27
  session: 83
---
## What It Is

The ETH Zurich study tested 4 coding agents with identical context files and found dramatically different responses:

- **Claude Code (Sonnet-4.5):** The ONLY agent where developer-written context files produced NO improvement. LLM-generated files also hurt. Claude Code's built-in context management (task tool for sub-task delegation, internal file discovery) appears to make external context files redundant or counterproductive.
- **Codex (GPT-5.2):** Benefited from human-written context (+4% on AGENTbench), hurt by LLM-generated (-3%).
- **GPT-5.1 mini:** Exhibited a unique pathology — multiple commands to locate and re-read context files that were already in its context window. Redundant context-reading behavior only occurred when context files were present.
- **Qwen Code (Qwen3-30b-coder):** Chat compression at 60% context limit, shell output restricted to 2,000 tokens. Different architectural constraints produced different context sensitivity.

Additional model-specific details:
- Different prompts performed differently: Codex prompt performed better on GPT models across both benchmarks
- Temperature settings varied: 0 for most models, 0.7 for Qwen, top-p 0.8

## Why It Matters

Most context file guidance assumes model-agnostic effectiveness. This study proves that assumption is wrong — not just in degree, but in kind. Claude Code actively manages its own context, making external context files redundant at best and harmful at worst. For teams using Claude Code, the optimal context strategy may be radically more minimal than for teams using Codex or other agents.

## Why People Are Using It

This is one of the few studies that tests the same context files across multiple agent platforms with controlled methodology. The finding has direct implications for teams choosing between agent platforms or maintaining context files across multiple agents.

## Potential Improvements

Model-specific context profiles: maintain different context file strategies per agent platform. For Claude Code: minimal files focused on non-discoverable information only (custom tooling, unusual build commands, project intent). For Codex: slightly richer context with tool recommendations and testing patterns.

## Potential Failure Modes

Model-specific findings expire quickly as models are updated. Claude Code's context management may change with new releases, potentially making context files more or less effective. The study tested specific model versions — generalization to future versions is uncertain.

## Corroboration Note — 2026-07-12

Production-scale corroboration from the Lindy migration (Nate B Jones, GLM 5.2 video —
see harness-non-portability-across-model-families): moving from Claude to a DeepSeek
architecture required rewriting not just context files but the memory architecture,
prompts, and tool-call handling. The ETH Zurich lab result (context strategy is
model-specific in kind, not degree) now has its strongest practitioner counterpart at
whole-harness scope.

## Extraction Note — 2026-04-27

Extracted as **rule**: [[test-context-strategies-against-your-actual-model]] in `extracts/rules/`. Harvested from the G2 (managing-agent-context) queue per IB-164 / DD-101 promotion path.
