---
name: Pointers over Copies in Context Files
summary: Instead of embedding code snippets or architectural descriptions in context files (which go stale), use pointers (file:line references) that direct the agent to the canonical source. The agent
  reads the live code rather than a potentially outdated copy. ETH Zurich found codebase overviews are redundant because agents discover structure themselves.
implementation_notes: 'Audit MetaSystem CLAUDE.md files for any embedded code patterns, directory trees, or architecture descriptions. Replace with file path references. Example: instead of describing the
  fractal pattern inline, point to ''systems/meta-system/governance/fractal-pattern.md''.'
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
proposer_priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- eth-zurich-context-files-paper-march-2026.md
related_findings:
- file: file-read-deduplication-pattern.md
  rel: same-problem
- file: tiered-context-injection-over-monolithic-files.md
  rel: same-problem
- file: claudemd-context-rot-from-indiscriminate-rule-accu.md
  rel: same-problem
- file: context-file-instruction-bloat-eth-zurich.md
  rel: same-problem
- file: ace-delta-updates-over-monolithic-rewrites.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: extended-by
- file: index-file-navigation-as-rag-replacement.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- managing-agent-context.md
---
## What It Is

A context file design principle from the ETH Zurich research community: use pointers (file paths, line references) instead of copying content into context files. Two supporting observations:

1. **Agents navigate codebases well**: The ETH Zurich study found that directory listings and codebase overviews in context files did not help agents find relevant files faster. Agents are "surprisingly good at discovering file structures on their own."
2. **Copies go stale**: Embedded code snippets in context files become outdated as the codebase evolves, creating contradictory signals between the context file and the actual code.

Practical format: instead of pasting a function signature, write `See the interface definition in src/types/agent.ts:42-58`. The agent reads the live file at task time.

## Why It Matters

Stale context is worse than no context -- it creates contradictions that the agent must resolve, consuming reasoning tokens and potentially producing incorrect output. Pointers ensure the agent always sees the current state while keeping the context file lightweight.

## Why People Are Using It

Multiple practitioners in the post-ETH-Zurich discussion converged on this pattern independently. The MarkTechPost analysis specifically recommends "pointers over copies" as a best practice for context file design.

## Potential Improvements

Tooling that validates pointer targets still exist (analogous to link checking). IDE integration that auto-updates line numbers when referenced code moves.

## Potential Failure Modes

Adds a file-read step before the agent can act on the information, increasing latency for frequently-needed references. Some information (project intent, trade-off philosophy) genuinely belongs inline because it has no canonical file location.
