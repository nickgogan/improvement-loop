---
name: Skills as Open Portable Standard (agentskills.io)
summary: Anthropic published Agent Skills as an open standard at agentskills.io on December 18, 2025, with the goal of cross-platform skill portability — the same skill folder works whether you're using Claude or another AI platform. The spec lives at github.com/agentskills/agentskills (Apache 2.0 code, CC-BY-4.0 docs), is open to community contributions, and is adopted by a growing list of clients (see agentskills.io/clients). Skills that target a specific platform's capabilities can declare so in the `compatibility` field.
implementation_notes: "Standard-track frontmatter is intentionally minimal: name, description, license, compatibility, metadata, allowed-tools (experimental). All other Claude Code frontmatter fields (disable-model-invocation, user-invocable, context: fork, agent, paths, hooks, etc.) are Claude Code extensions. The compatibility field is the spec-level escape hatch for skills that need a specific surface. Practitioner guidance from the Complete Guide: 'authors can note this in the skill's compatibility field.' Validator: skills-ref CLI from github.com/agentskills/agentskills/tree/main/skills-ref."
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-equipping-agents-with-agent-skills.md"
  - "agentskills-open-standard.md"
  - "anthropic-complete-guide-building-skills-pdf.md"
related_findings:
  - file: "skill-as-directory-progressive-disclosure-three-levels.md"
    rel: "enabled-by"
  - file: "skill-frontmatter-validation-rules.md"
    rel: "extends"
  - file: "skill-cross-surface-portability-with-constraints.md"
    rel: "extends"
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: raw
consumed_by: []
---

# Skills as Open Portable Standard (agentskills.io)

## What It Is

Agent Skills, originally developed by Anthropic, were released as an open standard on December 18, 2025. The format-as-standard lives at agentskills.io with the canonical repository at github.com/agentskills/agentskills (Apache 2.0 code, CC-BY-4.0 docs). The standard is open to ecosystem contributions; adopters are listed at agentskills.io/clients.

The portability promise: "the same skill should work whether you're using Claude or another AI platform." The standard-track frontmatter is deliberately minimal — six fields, with `allowed-tools` marked Experimental:

| Field | Required | Notes |
|---|---|---|
| `name` | Yes | 1-64 chars; lowercase alphanumeric + hyphens |
| `description` | Yes | 1-1024 chars |
| `license` | No | License name or reference |
| `compatibility` | No | 1-500 chars; declares surface requirements |
| `metadata` | No | Arbitrary key-value extension |
| `allowed-tools` | No | Experimental; space-separated pre-approved tools |

Skills targeting a specific platform's capabilities (e.g., Claude Code's `context: fork`, `paths`, `disable-model-invocation`) declare so in the `compatibility` field. The standard doesn't prohibit extensions; it just doesn't promise they'll be honored across clients.

## Why It Matters

The open-standard publication establishes Agent Skills as ecosystem infrastructure, not a Claude-only feature. Two implications:

1. **Skill authoring against the standard is portable.** Authors can publish skills that work across Anthropic, Cursor, Cline, Codex, Gemini CLI, and other adopters. Distribution platforms (skills.sh, plugin marketplaces, GitHub) can serve them.

2. **Vendor extensions are a tier above the floor.** Claude Code's extension set is rich and useful, but skills using extensions are silently Claude Code-only. The `compatibility` field is the spec-level mechanism for declaring this honestly.

Parallel to MCP, the standard makes a deliberate bet on broad adoption. The MCP analogy is explicit in Anthropic's framing: "Like MCP, we believe skills should be portable across tools and platforms."

For Improvement Loop substrate, the standard matters because the floor (six required+optional fields) is what cross-vendor skill authoring substrate should target. Claude Code-specific guidance can live on top of, not in place of, the open-standard substrate.

## Why People Are Using It

Anthropic-led with community contribution surface. The agentskills/agentskills repo CONTRIBUTING.md documents the contribution path. The "Client Showcase" at agentskills.io/clients lists adopters. Curated community lists (heilcheng/awesome-agent-skills, VoltAgent/awesome-agent-skills, ComposioHQ/awesome-claude-skills) link to skills from Anthropic, Google Labs, Vercel, Stripe, Cloudflare, Netlify, Trail of Bits, Sentry, Expo, Hugging Face, Figma, and more — substantial cross-vendor traction within ~6 months of the standard's release.

## Potential Alternatives

Claude-only skill format (faster iteration, vendor lock-in). Cross-vendor skill format owned by a foundation (slower governance, harder to evolve). Per-vendor formats with conversion tooling (translation overhead, semantic drift). No standard, just SKILL.md as convention (current state outside the spec; works but no validation).

## Potential Improvements

Spec-level versioning so skills can declare which version they target. Promotion path for high-utility Claude Code extensions into the open standard (e.g., `paths` for activation-gating, `disable-model-invocation` for invocation-control). Formal conformance suite — a skill can claim "passes agentskills-spec v1 conformance." Adopter feature matrix at agentskills.io/clients/comparison.

## Potential Failure Modes

**Vendor extensions become the de-facto standard.** If most skill authors target Claude Code extensions, the cross-vendor standard becomes nominal. Adopters that don't support extensions get a degraded experience.

**Spec drift from Claude Code's lead.** Claude Code ships features ahead of the standard. The standard catches up; in the gap, skills written against Claude Code aren't portable. This is the same problem MCP had early on.

**Compatibility field underused.** Authors who don't declare `compatibility` ship non-portable skills as if they're portable. Validators can't catch this — the field is optional and the extensions are silent.

**Adopter behavior divergence.** Two adopters may both claim spec compliance but interpret edge cases differently (description matching, validation strictness). Skills work on one and fail on the other.

**Open-standard governance friction.** Standards open to contributions move slower than vendor-owned formats. Anthropic's lead role mitigates this for now; longer-term governance shape is unclear.
