---
title: "Skills Reference Shared Context by Path, Not by Copy — Single-Source-of-Truth Rule for Skill Context"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "skills-as-pointers-to-second-brain-files"
identification_report: "managing-agent-context.harvest-queue.md::skills-as-pointers-to-second-brain-files::rule::skills-reference-shared-context-by-path"
extraction_date: "2026-04-27"
last_change_session: 82
last_change_sl: "session-82-codifier-extract-artifacts-harvest-promotion-batch"
deployed: false
deployed_to: null
context:
  applies_to:
    - "skill-based agent architectures (Claude Code skills, Cursor commands, equivalent SKILL.md-style artifacts) that consume context"
    - "deployments with multiple skills sharing common reference context (brand voice, ICP, project conventions, vocabulary, governance)"
    - "any second-brain or vault setup where context can be centralized and referenced from multiple consumer artifacts"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — converting from embedded copies to path references is a refactoring step; rolling back is also a refactoring step. The cost is in tooling-aware implementation, not migration"
  auditability: "high when a skill audit tool detects content duplication and flags embedded copies of shared context; medium when tracked via convention; low when relied on by author discipline"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Practitioner-documented at scale (Beni: 60+ skills across business processes; Agentic Academy's Five-Pillar Agentic OS video independently validates the same pattern). Anthropic's adapted skill-creator skill enforces a related discipline (SKILL.md ≤200 lines, reference context in separate files loaded on-demand)."
contract:
  preconditions: "A skill-based architecture exists (SKILL.md-style artifacts that the agent loads when invoked). A centralized context store (Obsidian vault, second-brain folder, repository convention, or equivalent) is available and accessible to the runtime where the skills execute. Multiple skills share at least one piece of common context — brand voice, ICP, project conventions, governance, vocabulary, or similar."
  invariants: "Each skill's SKILL.md (or equivalent definition) carries only (a) the workflow/SOP the agent should follow and (b) file path references to where shared context lives in the central store. Shared context is never embedded as a copy inside a skill's own reference folder. The same shared context is never copied into multiple skills' reference folders. Path references are validated — at skill creation time, at periodic audit, or both — to ensure they resolve to existing files at runtime."
  governance: "Owner: any policy or skill-authoring tool that defines or audits skills. The rule must be embedded in skill-authoring guidance and in skill-audit tooling. The audit reads each skill's reference folder, identifies content that duplicates content elsewhere in the skill set, and flags the duplication. Migration playbook (identify duplication → move to vault → replace with path) is the standard remediation. Exemptions: low-churn, skill-specific context that is genuinely unique to one skill may remain embedded."
  recovery: "If a skill is discovered with embedded shared context: identify the canonical home in the central store; if the canonical does not exist, create it (single source of truth); replace the skill's embedded copy with a path reference to the canonical; verify the path resolves at runtime. If multiple skills carry divergent copies of the same content (drift): pick the most-correct version, reconcile into the canonical, replace each skill's copy with the path reference; investigate which copies were stale and why. If runtime context lacks vault access (skill executes in an isolated environment without the central store): the skill's deployment context must include the referenced files, OR the rule's exemption applies if the context is genuinely skill-specific. Path references that fail to resolve at runtime are violations regardless of cause."
tags:
  - "extracted-artifact"
  - "rule"
  - "skill-authoring"
  - "context-engineering"
  - "single-source-of-truth"
  - "second-brain"
---

# Skills Reference Shared Context by Path, Not by Copy — Single-Source-of-Truth Rule for Skill Context

**Source:** [[skills-as-pointers-to-second-brain-files]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

A skill-based architecture exists where skills (SKILL.md-style artifacts, Cursor commands, or equivalent) carry their own definition and load on demand. A centralized context store — a vault, a second-brain folder, a repository-level shared-context directory, or similar — exists and is accessible to the runtime that executes the skills. Multiple skills share common context: brand voice, ICP, project conventions, governance documents, vocabulary, or other reference material.

A new skill is being authored, OR an existing skill is being audited or refactored.

Scope of application: any artifact where context could plausibly be either embedded or referenced. Out of scope: skill-specific context that is genuinely unique to one skill and never shared.

## Action

**Required:** Each skill's definition carries (a) the workflow or SOP the agent should follow and (b) path references to shared context in the central store. Shared context lives in the central store as the single source of truth; the skill's own reference folder contains only skill-specific material that is genuinely unique.

When a skill needs context that is or could be shared with other skills, place the canonical content in the central store and reference it by path from the skill. Periodic audit detects content duplication across skills and flags it for migration.

**Forbidden:** Embedding copies of shared context inside a skill's own reference folder when a central store exists. Maintaining multiple skills with their own copies of the same content. Path references that are not validated for runtime resolution. Treating "I'll keep them in sync manually" as a sustainable practice.

## Boundary

Enforced at skill authorship time (rule fires when a new skill is created or an existing skill is edited) and at periodic audit (a tool scans the skill set for content duplication). Applies to any context that is shared, or plausibly shareable, across skills.

Out of scope: context that is genuinely unique to one skill (no other skill consumes it, no other skill plausibly will). Such context may remain embedded; the rule does not require everything to move to the central store. Out of scope as well: deployment environments where central-store access is impossible (the deployment context must include the referenced files, or the rule's exemption applies for genuinely skill-specific content).

## Enforcement

- **Mechanism:** A skill audit tool reads each skill's reference folder, computes content fingerprints (hash, embedding similarity, or both), and identifies duplication across skills. Duplicates are surfaced for migration. Path references in skill definitions are validated at skill creation and at audit — references that don't resolve to existing files in the central store are violations.
- **Check (deterministic):** For every skill `S`: `for every reference file `R` in S's reference folder: NOT exists(R' in another skill's reference folder where content_matches(R, R'))` AND `for every path reference `P` in S's definition: resolves(P) at audit time`. Any branch false → violation.
- **Violation response:**
  - *Duplicated content across skills:* identify the canonical version, reconcile if there's drift, place in the central store, replace each skill's copy with a path reference; verify each path resolves.
  - *Path reference that doesn't resolve:* the skill is broken at runtime; either fix the path (the canonical may have moved) or restore the canonical if it was deleted.
  - *Skill embedded shared context that the central store doesn't have:* migrate to central store; replace embedding with reference; the canonical is now the central-store version.
  - *Multiple skills with divergent copies:* pick the most-correct version, reconcile, migrate; investigate which copies were stale and why (this is a process-improvement signal, not a one-time fix).
- **Cannot be silently exempted:** "I'll deal with it later when we have time" is the failure path. The rule does not require every skill to be migrated immediately on rule adoption — it requires that *new* skills are authored to the rule and that audits drive migration with bounded latency.

## Rationale

The rule exists because shared context drifts when copied. With 60+ skills (the Beni example) each carrying its own copy of common context (ICP, brand voice, audience persona), a single update to that shared truth requires touching every skill. In practice, the touches are skipped, missed, or applied inconsistently — and skills accumulate version drift where each operates on a slightly different shared truth.

The single-source-of-truth invariant collapses the maintenance surface to one. Updating the canonical once propagates to every consumer skill on the next invocation. Authors think about shared context as shared; skill files think about workflow.

The rule is symmetric to broader DRY discipline applied at the context-infrastructure layer. Where DRY in code prevents logic drift, this rule prevents context drift across skill files. The mechanisms are different (skills aren't compiled together), but the rationale is the same: duplicate stores diverge by default; single sources do not.

The rule respects skill-specific context. Genuine uniqueness — a skill that needs context no other skill will ever consume — is allowed to remain embedded. The rule's discipline applies to *shared* context; the central store is for content that has more than one consumer.

The rule is the positive-space restatement of the embedded-copies anti-pattern. Rather than enumerating ways drift accumulates (manual sync misses, partial updates, version-mismatched skills, "did I update all 60?"), the positive invariant is "shared context lives in one place; skills reference it by path." One rule, deterministic enforcement.

## Failure Modes

- **False-positive in duplication audit.** Two skills genuinely need similar-but-distinct context (e.g., LinkedIn-writer and Twitter-writer each have their own voice profile that share boilerplate). Audit flags as duplication. Mitigation: the audit produces candidates, not verdicts; humans rule on each flagged duplication; "similar but distinct" is allowed when the distinction is load-bearing.
- **Path-reference brittleness on vault restructure.** The canonical moves; every skill's path reference breaks. Mitigation: vault restructures include a sweep of consumer skills; reference-validation audit catches stragglers; a vault-aware redirect mechanism (similar to symlinks) can decouple references from physical paths.
- **Runtime without vault access.** A skill is invoked in an isolated environment that lacks the central store. Mitigation: deployment context includes the referenced files (the skill carries its dependencies); for genuinely-isolated environments, the rule's exemption applies and the skill embeds the necessary content with a stated rationale.
- **Premature migration.** A skill's context is flagged as shareable based on superficial similarity but is in fact distinct. Mitigation: migration is a deliberate decision per flagged duplication, not automatic; the audit surfaces candidates; humans confirm.
- **Central-store granularity drift.** The central store accumulates over-consolidated documents (one big "context" file) or under-consolidated fragments. Mitigation: central-store organization is its own concern with its own discipline; this rule does not prescribe the central store's internal structure, only that shared content lives there.
- **"I'll keep them in sync manually" theater.** An author opts out of the rule with a promise of manual sync. Mitigation: manual sync is the failure mode the rule prevents; opt-out without migration is a violation, not a deferral.

## Contract

### Preconditions
A skill-based architecture exists (SKILL.md-style artifacts that the agent loads when invoked). A centralized context store (Obsidian vault, second-brain folder, repository convention, or equivalent) is available and accessible to the runtime where the skills execute. Multiple skills share at least one piece of common context — brand voice, ICP, project conventions, governance, vocabulary, or similar.

### Invariants
Each skill's SKILL.md (or equivalent definition) carries only (a) the workflow/SOP the agent should follow and (b) file path references to where shared context lives in the central store. Shared context is never embedded as a copy inside a skill's own reference folder. The same shared context is never copied into multiple skills' reference folders. Path references are validated — at skill creation time, at periodic audit, or both — to ensure they resolve to existing files at runtime.

### Governance
Owner: any policy or skill-authoring tool that defines or audits skills. The rule must be embedded in skill-authoring guidance and in skill-audit tooling. The audit reads each skill's reference folder, identifies content that duplicates content elsewhere in the skill set, and flags the duplication. Migration playbook (identify duplication → move to vault → replace with path) is the standard remediation. Exemptions: low-churn, skill-specific context that is genuinely unique to one skill may remain embedded.

### Recovery
If a skill is discovered with embedded shared context: identify the canonical home in the central store; if the canonical does not exist, create it (single source of truth); replace the skill's embedded copy with a path reference to the canonical; verify the path resolves at runtime. If multiple skills carry divergent copies of the same content (drift): pick the most-correct version, reconcile into the canonical, replace each skill's copy with the path reference; investigate which copies were stale and why. If runtime context lacks vault access (skill executes in an isolated environment without the central store): the skill's deployment context must include the referenced files, OR the rule's exemption applies if the context is genuinely skill-specific. Path references that fail to resolve at runtime are violations regardless of cause.
