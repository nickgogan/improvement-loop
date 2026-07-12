---
name: "The Complete Guide to Building Skills for Claude (PDF)"
source_type: "Documentation"
status: "Done"
key_takeaways: "33-page (5,528-word) Anthropic narrative guide. Covers fundamentals → planning → testing → distribution → patterns → resources. Names three common skill use-case categories (Document & Asset Creation; Workflow Automation; MCP Enhancement) with named exemplars per category. Defines a 'critical rules' set: SKILL.md is case-sensitive exactly; kebab-case folder names only; NO README.md inside the skill folder (docs go in SKILL.md or references/); reserved-word ban on 'claude'/'anthropic' in names. Frames description quality with [What it does] + [When to use it] + [Key capabilities] structure and named good/bad examples. Documents three-level testing approach (triggering tests, functional tests, performance comparison) with concrete example test suites and baseline-vs-skill metric comparisons. Distribution model timestamped January 2026: GitHub host + zip + upload to Settings > Capabilities > Skills, or place in Claude Code skills directory; org-level skills shipped December 18, 2025. Positions skills as portable open standard parallel to MCP."
relevance: "High"
added_by: "Nick"
tags:
  - "skills"
  - "agent-design"
  - "prompt-engineering"
  - "evaluation"
  - "mcp"
  - "claude-code"
url: "https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf"
authority:
  - "anthropic.md"
findings:
  - "skill-as-directory-progressive-disclosure-three-levels.md"
  - "skill-md-frontmatter-as-discovery-trigger-primitive.md"
  - "skill-description-structure-what-when-capabilities.md"
  - "skill-testing-three-tier-trigger-functional-perf.md"
  - "iterate-on-single-task-then-extract-skill.md"
  - "skills-mcp-recipes-kitchen-complementarity.md"
  - "skill-authoring-four-guidelines.md"
  - "skills-as-open-portable-standard.md"
date_added: "2026-06-11"
date_processed: "2026-06-11"
date_published: "2026-01-26"
---

# The Complete Guide to Building Skills for Claude (PDF)

Long-form narrative guide complementing the engineering blog post and reference docs. Published by Anthropic, undated but referencing January 2026 distribution model. Available at resources.anthropic.com.

Notable additions beyond the docs:
- **Three use-case categories with exemplars:** Document & Asset Creation (`frontend-design`), Workflow Automation (`skill-creator`), MCP Enhancement (`sentry-code-review`).
- **Critical rules ledger:** SKILL.md name is exactly that string and case-sensitive; folder names are kebab-case only; NO README.md inside the skill folder.
- **"15-30 minutes to build and test your first working skill using the skill-creator"** as the target authoring cadence.
- **Three-tier testing approach** with worked examples, including a baseline-vs-skill performance comparison framing.
- **Iteration signals**: undertriggering, overtriggering, and execution issues each get a named fix pattern.
- **Positioning guidance**: "focus on outcomes, not features" + "highlight the MCP + skills story" for marketing the integration.

Local cache: `incubator/claude-build/app/pdf-to-markdown/output/The-Complete-Guide-to-Building-Skill-for-Claude.md` (read-only; not the canonical source).
