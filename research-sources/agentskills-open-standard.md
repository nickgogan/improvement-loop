---
name: "Agent Skills Open Standard (agentskills.io)"
source_type: "Documentation"
status: "Done"
key_takeaways: "Anthropic-maintained, community-contributable open format for Agent Skills, published as an open standard in December 2025. Repository at github.com/agentskills/agentskills under Apache 2.0 (code) and CC-BY-4.0 (docs). The format-as-standard specifies six frontmatter fields: `name` (required, 1-64 chars, lowercase alphanumeric + hyphens, no consecutive hyphens, must match parent directory), `description` (required, 1-1024 chars), `license` (optional), `compatibility` (optional, 1-500 chars), `metadata` (optional key-value map), `allowed-tools` (optional space-separated string, experimental). Directory shape: SKILL.md (required) + optional scripts/, references/, assets/. Progressive disclosure documented as three-tier: metadata ~100 tokens always loaded; instructions <5000 tokens recommended on activation; resources unbounded on demand. SKILL.md target: under 500 lines, file references one level deep, no deeply nested chains. Validator: `skills-ref validate ./my-skill` from the skills-ref reference library."
relevance: "High"
added_by: "Nick"
tags:
  - "skills"
  - "agent-design"
  - "governance"
  - "claude-code"
url: "https://github.com/agentskills/agentskills"
authority:
  - "anthropic.md"
findings:
  - "skill-md-frontmatter-as-discovery-trigger-primitive.md"
  - "skill-frontmatter-validation-rules.md"
  - "skill-as-directory-progressive-disclosure-three-levels.md"
  - "skills-as-open-portable-standard.md"
date_added: "2026-06-11"
date_processed: "2026-06-11"
date_published: "2025-12-16"
---

# Agent Skills Open Standard

Cross-vendor open specification for the Agent Skills format. Establishes Anthropic-originated skills as a portable format rather than a Claude-only feature. Adopters listed in agentskills.io/clients. CONTRIBUTING.md exposes the standard to ecosystem contributions.

The standard is deliberately narrower than Claude Code's superset: only six frontmatter fields are first-class, with `allowed-tools` explicitly marked Experimental. Claude Code's `disable-model-invocation`, `user-invocable`, `context: fork`, `agent`, `paths`, `hooks`, `model`, `effort`, `arguments` are Claude Code extensions, not part of the open spec.

Validation is mechanical (frontmatter conformance + naming rules) rather than semantic (description quality, instruction structure). The standard does not codify the "description should include both what and when to use it" guidance that the engineering post and Claude Code docs emphasize — that quality bar lives in authoring guidance, not in the spec.
