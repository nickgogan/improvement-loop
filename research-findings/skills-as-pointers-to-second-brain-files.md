---
name: Skills as Pointers to Second Brain Files
summary: Once a centralized second brain exists, skills should contain only a SKILL.md with file path references pointing into the vault — not embedded context copies. Any update to a shared context document
  (e.g., ICP doc) propagates automatically to all skills that reference it, eliminating context duplication and per-skill update overhead.
implementation_notes: MetaSystem's current skills embed context directly in their reference folders. As the Obsidian vault matures, high-churn shared context (ICP, vocabulary, principles) should migrate to
  vault files with skills updated to point at them. Low-churn, skill-specific context can remain embedded. This is a direct upgrade path — no architectural change required, just refactoring skill reference files
  to paths rather than copied content.
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- seven-levels-context-infrastructure-ai-agents.md
- agentic-os-five-pillars-claude-code.md
proposals: []
date_discovered: '2026-04-19'
last_updated: '2026-04-20'
related_findings:
- file: claudemd-as-knowledge-base-traversal-guide.md
  rel: extends
- file: index-file-navigation-as-rag-replacement.md
  rel: same-problem
- file: context-infrastructure-seven-level-maturity-model.md
  rel: part-of
- file: compounding-knowledge-loop-internal-data.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- managing-agent-context.md
---
# Skills as Pointers to Second Brain Files

## What It Is
When a centralized second brain (Obsidian vault or equivalent) exists, skills should not embed copies of shared context documents inside their own reference folders. Instead, each skill's SKILL.md contains only:
1. The workflow/SOP the agent should follow
2. File path references to where it should read context from within the second brain

Example: Instead of a LinkedIn Writer skill embedding an ICP document inside `skills/linkedin-writer/references/icp.md`, the SKILL.md says "read ICP context from `/second-brain/business/icp.md`."

When the ICP document is updated in one place in the vault, every skill that references it picks up the change automatically on the next invocation. No per-skill update propagation required.

## Why It Matters
Skills with embedded context become stale independently. A team running 60 skills that each embed their own copy of shared context (ICP, brand voice, audience persona) must manually update each skill when that context changes. This creates version drift where different skills operate on different versions of shared truth. The pointer pattern collapses shared context into a single source of truth and eliminates this maintenance surface.

## Why People Are Using It
Beni (60+ skills across business processes) explicitly migrated to this pattern when his second brain reached sufficient maturity. The migration step is: identify which reference files in a skill are shared across multiple skills → move to vault → replace with path reference. Claude can perform this migration on request.

## Potential Improvements
A skill audit tool that detects duplicated content across skills and proposes vault consolidation. Automated path validation to catch references to moved or deleted vault files. Versioning strategy for when the vault file is intentionally branched (e.g., locale-specific variants).

## Potential Failure Modes
Skills become dependent on vault file structure — reorganizing the vault breaks skill path references. Vault files may not exist when a skill runs in a context without vault access. Path references in SKILL.md become stale if vault is restructured without updating all referencing skills. Requires the vault to be mounted or accessible in every context where the skill runs.

## Additional Evidence — 2026-04-20

Agentic Academy's "Five-Pillar Agentic OS" video independently validates this pattern as "business context" — pillar 5 (the foundation layer). Their implementation: a single `brand-context/` folder containing voice profile, ICP, positioning, and client details. Every skill references this folder. "Update the information once and every skill gets that update when it runs." They explicitly frame this as the #1 thing to build first: "Start with the business brain, not the agents. Every feature gets multiplied by having the solid context foundation layer underneath it."

The adapted Anthropic skill-creator skill enforces context hygiene: SKILL.md kept under 200 lines, all reference context in separate files loaded on-demand. This matches the "pointers over copies" principle — skills reference the brand context folder rather than embedding context.
