---
name: "Equipping agents for the real world with Agent Skills"
source_type: "Blog Post"
status: "Done"
key_takeaways: "Anthropic's canonical engineering post introducing Agent Skills (Oct 2025). Frames skills as 'organized folders of instructions, scripts, and resources that agents can discover and load dynamically.' Establishes progressive disclosure as the core design principle (3 levels: metadata always loaded → SKILL.md on trigger → bundled files on demand). Provides four authoring guidelines (start with eval, structure for scale, think from Claude's perspective, iterate with Claude). Calls out security audit obligations, code-as-deterministic-tool pattern, and complementarity with MCP. December 2025 update notes Agent Skills published as open standard (agentskills.io)."
relevance: "High"
added_by: "Nick"
tags:
  - "skills"
  - "context-engineering"
  - "claude-code"
  - "agent-design"
  - "mcp"
url: "https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills"
authority:
  - "anthropic.md"
findings:
  - "skill-as-directory-progressive-disclosure-three-levels.md"
  - "skill-md-frontmatter-as-discovery-trigger-primitive.md"
  - "code-as-deterministic-tool-inside-skills.md"
  - "skills-mcp-recipes-kitchen-complementarity.md"
  - "skill-authoring-four-guidelines.md"
  - "skill-security-audit-obligation.md"
  - "skills-as-open-portable-standard.md"
  - "meta-skill-for-skill-authorship.md"
date_added: "2026-06-11"
date_processed: "2026-06-11"
date_published: "2025-10-16"
---

# Equipping agents for the real world with Agent Skills

Anthropic engineering post, October 16, 2025. Authors: Barry Zhang, Keith Lazuka, Mahesh Murag.

Establishes Agent Skills as a first-class capability for Claude across Claude.ai, Claude Code, Claude Agent SDK, and the Claude Developer Platform. Documents the three-level progressive disclosure model, SKILL.md frontmatter contract, four authoring guidelines, and the relationship between skills and MCP. Notes the December 2025 release of Agent Skills as an open standard at agentskills.io.

Closing aspiration: "we hope to enable agents to create, edit, and evaluate Skills on their own, letting them codify their own patterns of behavior into reusable capabilities" — frames meta-skill authorship as the forward trajectory.
