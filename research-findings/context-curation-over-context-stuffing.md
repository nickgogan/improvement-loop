---
name: Context Curation Over Context Stuffing -- Less Is More for Agent Quality
summary: 'Loading everything available into the context window degrades output quality rather than improving it. The fix is deliberate context curation: summarize stable conventions into short high-signal
  rule files, move volatile details to retrieval, and curate what counts as authoritative. The prompt is a rounding error (200 tokens) vs. the context window (200k-1M tokens); the real leverage is in designing
  the information environment.'
implementation_notes: 'Directly applicable to MetaSystem CLAUDE.md and skills. Current skills load variable amounts of context. Pattern: audit each skill''s context for signal-to-noise ratio, move low-signal
  content to retrieval or remove it, keep rule files short and high-signal.'
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- prompting-after-feb-2026-prompt-craft-context-inten.md
related_findings:
- file: context-file-instruction-bloat-eth-zurich.md
  rel: same-problem
- file: ace-delta-updates-over-monolithic-rewrites.md
  rel: same-problem
- file: claudemd-minimum-viable-rule-only-add-globally.md
  rel: same-problem
- file: claudemd-context-rot-from-indiscriminate-rule-accu.md
  rel: extended-by
- file: notebooklm-as-external-knowledge-base-for-context.md
  rel: same-problem
- file: five-context-management-techniques-in-claude-code.md
  rel: same-problem
- file: bmad-outcome-based-skill-rewrite-pattern.md
  rel: same-problem
- file: gsd-execution-context-profiles-mode-switching.md
  rel: same-problem
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: context-engineering-supersedes-prompt-engineering.md
  rel: enabled-by
- file: catastrophic-context-collapse-risk-during-claudemd.md
  rel: same-problem
- file: spec-first-agent-briefs-prompt-craft-context-inten.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- managing-agent-context.md
---
## What It Is

The counterintuitive finding that loading more context into agent windows often makes output *worse*, not better. Context curation is the discipline of designing the information environment the agent runs inside:

**What to include:**
- System prompts / agent instructions (high-signal, stable)
- Tool definitions + permissions (scoped to task)
- Curated RAG sources (authoritative only)
- Memory (what persists across runs, not everything that happened)
- Conventions (how this org writes, builds, tests, ships)

**What to exclude or summarize:**
- Verbose documentation that can be retrieved on demand
- Historical context that is not relevant to the current task
- Redundant information already captured in conventions
- Low-confidence or contradictory sources

**The math:** Your prompt might be 200 tokens. Your context window might be 200k-1M. The prompt is a rounding error. Context engineering -- deciding what fills the other 99.98% -- is where the leverage lives.

## Why It Matters

"We loaded everything and quality got worse" is one of the five most common agent failure modes. The mechanism: irrelevant or contradictory context dilutes attention, creates conflicting signals, and forces the model to resolve ambiguities that should have been resolved by the human during curation. This is the context-level analogue of the Catastrophic Context Collapse finding.

## Why People Are Using It

Documented as a core failure mode fix in the post-Feb-2026 prompting framework. The recommendation is explicit: "curate context; summarize; move stable conventions into a short, high-signal rule file."

## Potential Failure Modes

- **Over-pruning:** Removing too much context leaves the agent without necessary information, producing hallucinations
- **Stale summaries:** Summarized conventions that are not updated become misleading context
- **Curation effort:** The upfront cost of curating context is higher than dumping everything in; teams may skip it under time pressure

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[context-curation-over-stuffing]] in `extracts/patterns/`
