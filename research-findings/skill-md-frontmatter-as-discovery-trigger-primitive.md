---
name: SKILL.md Frontmatter as Discovery & Triggering Primitive
summary: A skill's YAML frontmatter — primarily `name` (≤64 chars, lowercase + hyphens + digits) and `description` (≤1024 chars, what + when) — is the only thing Claude sees at agent startup. It is simultaneously the discovery surface (Claude knows what skills exist) and the triggering primitive (Claude decides whether to load a skill based on description match). Authoring quality at this level dominates skill effectiveness — every other layer is downstream.
implementation_notes: "The description should include BOTH what the skill does AND when to use it; Anthropic's skill-creator guidance pushes authors toward 'a little bit pushy' description language to combat Claude's tendency to undertrigger. Validation rules: name max 64 chars, lowercase alphanumeric + hyphens only, no consecutive hyphens, no leading/trailing hyphens, must match parent directory; description max 1024 chars, non-empty, no XML tags. Reserved words 'anthropic' and 'claude' cannot appear in names. Frontmatter is what appears in Claude's system prompt — malicious content here could inject instructions, hence validation strictness."
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
priority: P1 (Implement Now)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in:
  - "Improvement Loop"
  - "General / Cross-System"
sources:
  - "anthropic-equipping-agents-with-agent-skills.md"
  - "anthropic-agent-skills-overview-docs.md"
  - "anthropic-claude-code-skills-docs.md"
  - "agentskills-open-standard.md"
  - "anthropic-complete-guide-building-skills-pdf.md"
related_findings:
  - file: "skill-as-directory-progressive-disclosure-three-levels.md"
    rel: "enabled-by"
  - file: "skill-frontmatter-validation-rules.md"
    rel: "extended-by"
  - file: "skill-description-structure-what-when-capabilities.md"
    rel: "extends"
  - file: "skill-description-optimization-loop-held-out-test.md"
    rel: "extended-by"
  - file: "agent-description-auto-dispatch-routing.md"
    rel: "same-problem"
  - file: "description-based-workflow-routing-lazy-dispatch.md"
    rel: "same-problem"
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: raw
consumed_by: []
---

# SKILL.md Frontmatter as Discovery & Triggering Primitive

## What It Is

The required YAML frontmatter at the top of every `SKILL.md` carries the only information Claude sees before deciding whether to load a skill. Two fields are required across all Anthropic surfaces:

- `name`: 1-64 characters, lowercase letters / digits / hyphens, no leading/trailing or consecutive hyphens, must match parent directory name, cannot contain reserved words `anthropic` or `claude`, no XML tags.
- `description`: 1-1024 characters, non-empty, no XML tags. Authoring guidance: include both "what the skill does" and "when to use it"; include trigger phrases / keywords; mention file types if relevant.

Frontmatter alone is what enters Claude's system prompt at startup. The body of SKILL.md is filesystem-resident until activation.

## Why It Matters

Skill triggering is description-matching, not keyword-extraction or hard rules. The description is the entire interface between user intent and skill activation. Authoring quality at this single layer dominates skill effectiveness more than anything in the body — a perfect SKILL.md body that never triggers is dead capability.

The structure also constrains the security model. Because frontmatter appears in the system prompt, validation strictness (no XML, no reserved words, character set limits) is a defense against prompt injection from untrusted skills. The reserved-word ban exists specifically to prevent skills from impersonating system or vendor authority.

## Why People Are Using It

Universal across Anthropic surfaces — Claude.ai, Claude Code, Claude API, Claude Agent SDK, claude Developer Platform. Codified in the open standard at agentskills.io as the only two required fields. Anthropic's own skill-creator skill devotes a substantial portion of its guidance — and a full description-optimization loop with held-out test set — to getting this layer right. Practitioner guidance ("be a little pushy in descriptions to combat undertriggering") has propagated from skill-creator to community-curated lists like awesome-agent-skills.

## Potential Alternatives

Hardcoded skill activation by filename or path glob (loses semantic match across paraphrased requests). Manual-only invocation (loses background-knowledge use case). Embedding skills in CLAUDE.md as static rules (loses progressive disclosure). LLM-classifier as a separate routing model (heavier, slower, additional failure mode). Tag-based or schema-based metadata (less expressive for natural-language matching than free-form description).

## Potential Improvements

Structured description fields ("triggers": [...], "non-triggers": [...]) for clearer eval. Per-skill description embeddings precomputed and matched at routing time instead of in-prompt match. Description versioning with A/B regression on triggering accuracy. Claude Code's `when_to_use` field — added alongside `description` — is an evolutionary step in this direction, but the field is appended to `description` and counts toward the same character cap.

## Potential Failure Modes

**Undertriggering.** Claude has documented bias toward not invoking skills when they would be useful. Common authoring trap: descriptions that are too modest or technical ("Implements the Project entity model with hierarchical relationships"). Skill-creator's countermeasure is to push for explicit trigger phrases and slightly pushy language.

**Overtriggering.** Descriptions that are too broad or too keyword-rich cause skills to load on irrelevant queries, wasting context. Remedy: more specific descriptions, named negative triggers, or `disable-model-invocation: true`.

**Description truncation under context pressure.** When many skills are installed, Claude Code budgets descriptions at 1% of context window (configurable) with a 1536-char hard cap per entry. Under pressure, descriptions for least-recently-used skills get dropped first. Keywords needed for matching can be stripped before Claude sees the description.

**Reserved-word and validation rejection.** Skills named `claude-helper` or `anthropic-fix` are silently invalid and won't load. Authors hit this when migrating named workflows.

**Description divergence from body.** Skills authored quickly may declare capabilities in the description that the body doesn't actually deliver — Claude triggers the skill, then fails to perform the promised work.
