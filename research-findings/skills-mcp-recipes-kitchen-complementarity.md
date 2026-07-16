---
name: Skills + MCP — Recipes + Kitchen Complementarity
summary: 'Anthropic frames Skills and MCP as complementary primitives, not competing ones. MCP provides connectivity (Claude reaches your service — Notion, Linear, etc.) — what Claude *can do*. Skills provide
  knowledge (Claude knows how to use your service for specific workflows) — how Claude *should do it*. Without a skill, users blame the connector for what''s actually a workflow guidance problem. Use cases
  divide into three categories: standalone skills, workflow-orchestration skills, and MCP-enhancement skills.'
implementation_notes: 'Three named use-case categories from the Complete Guide PDF: (1) Document & Asset Creation (frontend-design, docx, pptx, etc.) — output generation with consistent style/quality, no
  external tools required. (2) Workflow Automation (skill-creator) — multi-step processes with consistent methodology, may coordinate MCP servers. (3) MCP Enhancement (sentry-code-review) — workflow guidance
  on top of MCP tools. Without skills, MCP integrations suffer ''users connect your MCP but don''t know what to do next'' — support tickets, inconsistent results, blame on the connector when the issue is
  workflow guidance. Recommended pattern for MCP authors: ship MCP + skills together; link from MCP docs to skills repo.'
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-equipping-agents-with-agent-skills.md
- anthropic-complete-guide-building-skills-pdf.md
related_findings:
- file: mcp-as-code-api-progressive-tool-discovery.md
  rel: same-problem
- file: skill-as-directory-progressive-disclosure-three-levels.md
  rel: enabled-by
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: synthesized
consumed_by:
- designing-agent-tools.md
---

# Skills + MCP — Recipes + Kitchen Complementarity

## What It Is

Anthropic's framing of the relationship between Agent Skills and MCP (Model Context Protocol):

| | MCP (Connectivity) | Skills (Knowledge) |
|---|---|---|
| Role | Connects Claude to your service (Notion, Asana, Linear, etc.) | Teaches Claude how to use your service effectively |
| Provides | Real-time data access and tool invocation | Captures workflows and best practices |
| Frame | What Claude *can* do | How Claude *should* do it |

The kitchen analogy: MCP provides the professional kitchen (tools, ingredients, equipment); Skills provide the recipes (step-by-step instructions on how to make something valuable).

The Complete Guide PDF names three skill use-case categories that map to this framing:
1. **Document & Asset Creation** — output generation with consistent style/quality. Uses Claude's built-in capabilities; no MCP required. Examples: frontend-design, docx, pptx.
2. **Workflow Automation** — multi-step processes with consistent methodology. May or may not orchestrate MCP servers. Example: skill-creator.
3. **MCP Enhancement** — workflow guidance specifically on top of an MCP server's tools. Example: sentry-code-review (Sentry's MCP + workflow skill).

## Why It Matters

The framing answers a question Anthropic explicitly addresses: "MCP already exists — why do we need skills?" The answer is that the two primitives solve orthogonal problems. MCP without skills is a connector with no workflow guidance — users connect it but don't know what to do next. Skills without MCP are workflow guides with no service connectivity — they can orchestrate Claude's built-in capabilities but can't reach external services.

For builders of MCP integrations, the practical implication is concrete: ship MCP + skills together. The Complete Guide PDF spells out the cost of NOT shipping skills: "Users connect your MCP but don't know what to do next" → support tickets, inconsistent results, "Users blame your connector when the real issue is workflow guidance."

For Improvement Loop consumers, the framing helps decide which artifact to author for a given problem. Service connectivity gap → MCP. Workflow knowledge gap → skill. Both → both.

## Why People Are Using It

Universal framing across Anthropic's canonical skill sources. Documented adoption pattern: MCP authors at Sentry, Notion, Slack, and others ship companion skill libraries. The plugin marketplace pattern (`/plugin marketplace add ...`) supports bundling MCP + skill distributions together.

## Potential Alternatives

MCP-only integrations (status quo before skills — leaves workflow gap). Custom system prompts per use case (heavier; doesn't compose well). Documentation-only (workflow lives outside the agent — users have to find it). Skill-only without MCP (works for built-in capabilities; can't reach external services).

## Potential Improvements

Standard "MCP + skill" bundle distribution shape so users install both together. Cross-references between MCP server metadata and skill availability ("this MCP has 3 recommended skills"). Skill telemetry feeding back into MCP design — "users invoke this MCP tool sequence 80% of the time; that's a skill candidate."

## Potential Failure Modes

**Two-by-two confusion.** Skills + MCP works; skill-only without MCP works; MCP-only without skills works (poorly). Users sometimes try to install skill packs that assume an MCP server they don't have. Clear `compatibility` declarations help; conventional discipline is fragile.

**Skill drift from MCP version.** A skill encoding workflows on top of MCP server v1's tool surface will fail or misbehave when the MCP server ships v2 with renamed/changed tools.

**Wrong category framing.** Authors framing an MCP-enhancement use case as a standalone workflow-automation skill miss the connectivity layer and end up reimplementing what should be MCP. Or the inverse: framing a standalone workflow as MCP-enhancement requires connectivity that doesn't exist.

**"Skills make MCP optional" misread.** A reader of the framing might conclude that skills replace MCP. They complement; they don't substitute. A workflow needing external data access cannot ship as skill-only.
