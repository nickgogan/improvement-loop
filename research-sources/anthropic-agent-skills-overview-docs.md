---
name: "Agent Skills — Claude API Docs Overview"
source_type: "Documentation"
status: "Done"
key_takeaways: "Canonical platform.claude.com docs page for Agent Skills. Documents the three-level progressive disclosure model with explicit token-cost framing (Level 1 ~100 tokens always loaded; Level 2 <5K when triggered; Level 3 unlimited bundled). Specifies SKILL.md frontmatter validation rules: name max 64 chars lowercase+hyphens+digits, no XML tags, reserved words 'anthropic' and 'claude'; description max 1024 chars non-empty. Maps cross-surface availability — claude.ai (individual upload), API (workspace shared), Claude Code (filesystem-based, custom-only). Documents runtime constraints (API: no network, no runtime installs; Claude Code: full network, local installs only). Reiterates security obligation to audit untrusted skills."
relevance: "High"
added_by: "Nick"
tags:
  - "skills"
  - "claude-code"
  - "context-engineering"
  - "agent-design"
  - "governance"
url: "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview"
authority:
  - "anthropic.md"
findings:
  - "skill-as-directory-progressive-disclosure-three-levels.md"
  - "skill-md-frontmatter-as-discovery-trigger-primitive.md"
  - "skill-frontmatter-validation-rules.md"
  - "skill-cross-surface-portability-with-constraints.md"
  - "skill-security-audit-obligation.md"
date_added: "2026-06-11"
date_processed: "2026-06-11"
date_published: null
---

# Agent Skills — Overview (Claude API Docs)

Canonical reference for the Agent Skills feature across Anthropic surfaces. Documents the file-system-based execution model, progressive disclosure with token costs, frontmatter validation rules, and per-surface availability and constraints.

Architecture diagram framing: "Skills exist as directories on a virtual machine, and Claude interacts with them using the same bash commands you'd use to navigate files on your computer." On-demand file access + efficient script execution + no practical limit on bundled content are the three derived properties of the filesystem model.

Cross-surface table:
- Claude API: workspace-shared, requires three beta headers (`code-execution-2025-08-25`, `skills-2025-10-02`, `files-api-2025-04-14`), no network access, no runtime package installs.
- Claude Code: custom only, filesystem-based, full network access, local installs only.
- claude.ai: per-user upload via Settings, varying network access by admin policy.
