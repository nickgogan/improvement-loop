---
name: Skill Plugin Marketplace Distribution Model
summary: Claude Code supports a plugin marketplace pattern for skill distribution. A GitHub repo registers as a marketplace via `/plugin marketplace add <owner>/<repo>`, exposing plugin bundles for install. Each plugin can ship multiple skills + agents + hooks + MCP servers as a coherent unit. Direct install: `/plugin install <plugin>@<marketplace>`. Anthropic's anthropics/skills repo is the canonical example, shipping `document-skills` (docx, pdf, pptx, xlsx) and `example-skills` (creative, design, dev, enterprise) plugins.
implementation_notes: "Distribution pattern combines: (1) GitHub repo with public README for humans (separate from per-skill READMEs which are forbidden inside skill folders). (2) Plugin manifest registering the repo as a Claude Code marketplace. (3) Individual plugin definitions inside the marketplace, each bundling related skills. (4) Optional `<plugin>/SKILL.md` plugin-root skill where frontmatter `name` becomes the invocation namespace. Authentication model: workspace trust dialog gates project-level skill `allowed-tools`. Plugins inherit this trust model. Updates: plugin updates flow through marketplace pull; auto-update vs. manual is a marketplace policy."
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-skills-repo.md"
  - "anthropic-claude-code-skills-docs.md"
related_findings:
  - file: "skill-hierarchy-enterprise-personal-project-plugin.md"
    rel: "extends"
  - file: "skill-security-audit-obligation.md"
    rel: "same-problem"
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: raw
consumed_by: []
---

# Skill Plugin Marketplace Distribution Model

## What It Is

Claude Code supports a plugin marketplace pattern for skill distribution:

1. **Register a marketplace**: `/plugin marketplace add <owner>/<repo>` adds a GitHub repo as a marketplace.
2. **Browse and install**: `/plugin install <plugin>@<marketplace>` installs a specific plugin bundle.
3. **Skill resolution**: installed plugin skills get a `plugin-name:skill-name` namespace, never colliding with personal or project skills.

A plugin bundle can ship multiple skills, agents, hooks, MCP server configs, output styles — all as a coherent unit. A plugin-root SKILL.md (using its `name` frontmatter for invocation) is the one place where the frontmatter `name` field sets the command name (instead of the directory name).

Anthropic's canonical example: the `anthropics/skills` repo is registerable via `/plugin marketplace add anthropics/skills`, exposing two plugin bundles:
- `document-skills@anthropic-agent-skills` — docx, pdf, pptx, xlsx (source-available, the document capabilities powering Claude.ai's create-files feature).
- `example-skills@anthropic-agent-skills` — creative (algorithmic-art, canvas-design, frontend-design, slack-gif-creator, theme-factory), technical (mcp-builder, web-artifacts-builder, webapp-testing), enterprise (brand-guidelines, internal-comms), and skill-creator.

## Why It Matters

The marketplace pattern solves a distribution problem skills hit at scale:
- **Discovery**: how do users find skills they don't know exist? A marketplace catalog beats GitHub search.
- **Coherent bundling**: related skills ship together with their supporting hooks, agents, and MCP configs.
- **Update channel**: plugin updates flow through marketplace pull rather than re-cloning.
- **Trust model**: marketplaces inherit GitHub identity; users trust `anthropics/*` differently than random forks.

The plugin-root SKILL.md exception (frontmatter `name` sets the invocation) is the one case where authorship needs to be deliberate about naming. Otherwise the consistent rule is "directory name is the command name."

For Improvement Loop substrate, the marketplace pattern is the consumer-facing distribution channel that skill authoring substrate eventually needs to target. Authors don't ship one-off skills; they ship plugin bundles.

## Why People Are Using It

Built into Claude Code's `/plugin` subcommand. Anthropic's anthropics/skills marketplace is officially supported. Plugin marketplaces from community sources are documented in awesome-agent-skills and similar curated lists. Partner skills (Notion, others noted as "Partner Skills" in anthropics/skills README) suggest a vendor distribution pattern beyond Anthropic-only marketplaces.

## Potential Alternatives

Direct GitHub clone (works but loses update channel, lacks discovery, no namespace isolation). Per-skill upload to claude.ai (per-user, per-skill, doesn't scale). Centralized Anthropic-only catalog (curation cost; community contribution surface limited). Vendor-specific marketplaces inside MCP server distributions (works for MCP-paired skills only).

## Potential Improvements

Marketplace search/discovery UI inside Claude Code. Per-plugin telemetry: which skills in the plugin actually get invoked vs. dead weight. Auto-update policy per marketplace ("pin to latest" vs. "manual approve updates"). Plugin signing for trust verification. A formal "marketplace listing" file that registers plugin metadata centrally (rather than relying on README conventions).

## Potential Failure Modes

**Untrusted marketplace registration.** `/plugin marketplace add malicious/repo` adds a marketplace whose plugins can ship skills, hooks, MCP configs — privileged surface area. The trust boundary is repo-level; users need to verify provenance before adding.

**Plugin sub-resource hot-reload gap.** SKILL.md hot-reloads in plugin skills; `hooks/`, `.mcp.json`, `agents/`, `output-styles/` need `/reload-plugins`. Updates to plugin bundles may leave half-loaded state.

**Marketplace governance unclear.** No documented policy for "what happens if a marketplace publisher pushes a malicious update to a previously-trusted plugin." The standing audit obligation transfers to update events but the tooling for that doesn't exist.

**Namespace overlap.** Two plugins with the same skill name don't collide (different plugin namespaces), but the user typing the unnamespaced `/skill-name` may not see both. Cross-plugin discovery is limited.

**Plugin install scope.** Plugin installs are session-level configurations; they affect all subsequent Claude Code sessions for that user. No per-project install isolation without committing to `.claude/skills/` instead.
