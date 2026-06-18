---
name: Skill Frontmatter Validation Rules (Open-Standard Constraints)
summary: The Agent Skills open standard validates frontmatter mechanically — name conforms to character class and length rules, description is bounded, reserved words are rejected, XML tags are forbidden. Validation is mechanical not semantic — naming conformance, not description quality. The agentskills/agentskills repo ships a `skills-ref validate` CLI for this check.
implementation_notes: "Six first-class frontmatter fields in the open standard: name (required), description (required), license (optional), compatibility (optional, ≤500 chars), metadata (optional key-value map), allowed-tools (optional, Experimental). Claude Code extends this with disable-model-invocation, user-invocable, when_to_use, argument-hint, arguments, disallowed-tools, model, effort, context, agent, hooks, paths, shell — but those are Claude Code-specific. A skill authored against the open standard runs everywhere; one authored against Claude Code extensions is non-portable. Validate with `skills-ref validate ./my-skill`."
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-agent-skills-overview-docs.md"
  - "agentskills-open-standard.md"
related_findings:
  - file: "skill-md-frontmatter-as-discovery-trigger-primitive.md"
    rel: "extends"
  - file: "skill-cross-surface-portability-with-constraints.md"
    rel: "same-problem"
  - file: "claude-code-skill-frontmatter-extensions.md"
    rel: "contradicts"
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: raw
consumed_by: []
---

# Skill Frontmatter Validation Rules

## What It Is

The Agent Skills open standard specifies six first-class frontmatter fields with mechanical validation:

| Field | Required | Rules |
|---|---|---|
| `name` | Yes | 1-64 chars; lowercase a-z, 0-9, and hyphens; no leading/trailing/consecutive hyphens; must match parent directory name |
| `description` | Yes | 1-1024 chars; non-empty; no XML tags |
| `license` | No | License name or reference to bundled LICENSE file |
| `compatibility` | No | 1-500 chars; environment requirements (intended product, packages, network needs) |
| `metadata` | No | Arbitrary key-value mapping for client-specific extension |
| `allowed-tools` | No | Space-separated tool list (Experimental — support varies by client) |

A reference validator (`skills-ref validate ./my-skill`) checks naming and frontmatter conformance.

## Why It Matters

The validation is mechanical, not semantic. It guarantees naming and structural correctness, not description quality or instruction effectiveness. This is the right scope for a cross-vendor standard: anything more would entangle the spec with specific Claude behavior.

The frontmatter cap also bounds the security surface. Because frontmatter enters the system prompt, character-class restrictions on names and XML-tag prohibition on descriptions limit prompt-injection vectors from third-party skills.

The reserved-word ban on `anthropic` and `claude` (documented in Anthropic's overview docs; not in the open-standard validation table) prevents impersonation skills from claiming system authority.

## Why People Are Using It

Open standard published December 2025. Validator library `skills-ref` shipped alongside. Anthropic itself enforces these rules on Claude.ai upload and on Claude API skill creation. Same constraints documented across all canonical sources (engineering post, overview docs, Claude Code docs, anthropics/skills README, Complete Guide PDF).

## Potential Alternatives

JSON Schema validation (more expressive but heavier; rejected in favor of mechanical YAML checks). Markdown-front-matter conventions used by other tools (Hugo, Jekyll) without prescriptive cross-vendor naming rules — too loose for triggering semantics. Programmatic skill registration via API only (loses portability). Validation embedded in the agent runtime (skills-ref makes it a separate lint step).

## Potential Improvements

A semantic description-quality lint ("does this description name a trigger context?") complementing the mechanical check. Spec-level versioning so skills can declare which version of the standard they target. Optional schema fields for trigger keywords as a separate field instead of inline in description. A standard `tests/` directory shape that validators could exercise. The current spec marks `allowed-tools` as Experimental — future versions may either promote it or differentiate per-client extensions more explicitly.

## Potential Failure Modes

**Skills validate but trigger poorly.** Mechanical conformance doesn't predict whether a skill loads at the right times. The validator can't catch description vagueness, missing trigger contexts, or overlap with other skills.

**Reserved-word collision.** Naming a skill `claude-fix-imports` is silently invalid; authors discover this only at registration time.

**Spec drift between vendors.** As Claude Code grows extensions (currently ~13 additional frontmatter fields), a skill written against Claude Code may not run elsewhere. The standard captures the floor; vendor extensions are the ceiling.

**XML-tag check is shallow.** The "no XML tags" rule rejects `<` and `>` characters but doesn't prevent text-based prompt injection. The frontmatter is still untrusted input in the system prompt.
