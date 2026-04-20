---
title: "OB1 (Open Brain) -- Structural Analysis"
id: "ob1-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "2026-04-20"
updated: "2026-04-20"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "ob1"
  - "agentic-os"
  - "personal-os"
analyzed_version: "latest"
analyzed_date: "2026-04-20"
repo_url: "https://github.com/NateBJones-Projects/OB1"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
---

# OB1 (Open Brain) -- Structural Analysis

## Metadata
- **Repo:** https://github.com/NateBJones-Projects/OB1
- **Version analyzed:** latest (as of 2026-04-20)
- **Date:** 2026-04-20
- **Spectrum position:** cherry-pick

---

## 1. Structural Inventory

### File Tree Statistics
| Metric | Value |
|--------|-------|
| Total files | 477 |
| Total directories | 155 |
| Markdown files | 142 |
| TypeScript files | 34 (ts) + 34 (tsx) |
| JSON files | 100 |
| SQL files | 18 |
| Python files | 8 |
| YAML files | 19 |
| Config/YAML/JSON files | 119 |
| MD-to-code ratio | 142 MD : ~76 code = 1.87:1 |
| Max directory depth | 8 |

### Markdown Composition
| Purpose | Count | Directory |
|---------|-------|-----------|
| Skill definitions (SKILL.md, *.skill.md) | ~25 | `skills/*/`, `recipes/*/`, `skills/*/variants/*/` |
| Recipe READMEs + docs | ~30 | `recipes/*/` |
| Extension READMEs + templates | ~10 | `extensions/*/`, `extensions/_template/` |
| Integration/primitive/schema READMEs | ~12 | `integrations/*/`, `primitives/*/`, `schemas/*/` |
| Reference docs (knowledge) | 11 | `skills/n-agentic-harnesses/references/`, `recipes/repo-learning-coach/` |
| Human documentation | 7 | `docs/`, root (`CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`) |
| Agent/context files | 2 | `CLAUDE.md`, `.claude/skills/review-pr.md` |
| Dashboard docs | 3 | `dashboards/*/` |

**Markdown IS the codebase.** 142 of 477 files (30%) are markdown. Skills, recipes, and extensions are defined primarily through markdown files. The code files (TS, SQL) are edge function implementations and database schemas that serve the markdown-defined behaviors.

### Directory Naming Conventions
- **kebab-case** throughout (e.g., `panning-for-gold`, `home-maintenance`, `n-agentic-harnesses`)
- **Role-based directories at top level**: `extensions/`, `recipes/`, `skills/`, `primitives/`, `integrations/`, `schemas/`, `dashboards/`
- **Every category has a `_template/` directory** containing scaffolding files
- **Flat contribution structure**: each contribution is a direct child of its category

### Top-Level Structure
```
.
├── .claude/skills/         — Claude Code admin skill (PR review)
├── .github/                — CI workflows, issue templates, PR template
├── dashboards/             — Frontend templates (SvelteKit, Next.js)
├── docs/                   — Setup guides, FAQ, companion prompts
├── extensions/             — Curated 6-build learning path
├── integrations/           — MCP extensions, capture sources
├── primitives/             — Reusable concept guides
├── recipes/                — Standalone capability builds (25+)
├── resources/              — Official companion files
├── schemas/                — Database table extensions
├── server/                 — Core MCP server reference
├── skills/                 — Reusable AI client skill packs (14)
├── CLAUDE.md               — Agent instructions
├── CONTRIBUTING.md         — Full contribution rules
└── README.md               — Project overview
```

### Notable Structural Patterns
1. **Template-driven contribution**: Every category has a `_template/` directory with scaffolding. Extensions have a full `AGENT_SPEC.md` generator spec that produces all 5 required files from a single AI prompt.
2. **metadata.json everywhere**: Every contribution subfolder has a `metadata.json` with structured metadata (name, description, category, author, version, requires, tags, difficulty, estimated_time). Validated by JSON Schema in CI.
3. **Canonical skill separation**: Reusable skills live in `skills/`. Recipes can depend on them via `requires_skills` in metadata.json. Recipe-local `.skill.md` files are allowed but discouraged for reusable behavior.
4. **No monorepo tooling**: Unlike most watched libraries, OB1 has no package manager workspace config. Contributions are self-contained directories, not linked packages.

---

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `CLAUDE.md` | LLM | Global | Auto-loaded | Constraints/Rules | Repo structure, guard rails, PR standards, key files |
| `.claude/skills/review-pr.md` | LLM | Task | Injected | Workflow/Process | PR admin review: security scan, mission fit, naming, output templates |
| `skills/*/SKILL.md` | LLM | Task | Referenced | Workflow/Process | Skill definitions with trigger conditions, process steps, output specs |
| `skills/*/variants/*/SKILL.md` | LLM | Task | Referenced | Workflow/Process | Platform-specific variants (Anthropic, Codex, Claude Desktop) |
| `recipes/*/*.skill.md` | LLM | Task | Referenced | Workflow/Process | Recipe-local skill files (tightly coupled to one recipe) |
| `extensions/_template/AGENT_SPEC.md` | LLM | Task | Referenced | Workflow/Process | Machine-readable generator spec for creating new extensions |
| `docs/02-companion-prompts.md` | Both | Global | Referenced | Workflow/Process | Five prompts for onboarding, migration, habit building |
| `docs/05-tool-audit.md` | Both | Global | Referenced | Tool Usage | MCP tool audit and optimization guide |

### Sampling Notes
Read in full: `CLAUDE.md`, `.claude/skills/review-pr.md`, `skills/auto-capture/SKILL.md`, `skills/panning-for-gold/SKILL.md`, `skills/world-model-diagnostic/SKILL.md`, `skills/n-agentic-harnesses/SKILL.md`, `extensions/_template/AGENT_SPEC.md`. Classified by pattern: remaining 20+ skills and recipe-local skill files (all follow the same frontmatter schema and section structure).

### Context Loading Strategy
**Minimal root, skill-on-demand.** The CLAUDE.md is compact (~50 lines) — repo structure, guard rails, PR standards only. No persona, no identity, no workflow orchestration. Individual skills are loaded on demand when triggered by user prompts. Each skill is self-contained with its own trigger conditions and process.

This is the **opposite** of the chain-loading pattern seen in GSD, n8n, or MetaSystem. OB1 has exactly one auto-loaded file (CLAUDE.md) and one injected admin skill. Everything else is pulled in by the AI client's skill/command system when invoked.

**Notable**: The `n-agentic-harnesses` skill uses a reference-loading pattern — Step 1 of the skill reads 2-3 reference files from `references/` depending on the classified mode. This is a form of conditional context assembly within a single skill, not at the root level.

---

## 3. Workflow Topology

### Phases/Stages
| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| Contribution creation | Developer writes code + README + metadata.json | Files pass local validation | No |
| PR submission | `git push` + PR creation | Branch pushed, PR opened | No |
| Automated CI review | PR opened/updated | 15 rules pass (structure, secrets, SQL safety, scope, links) | No |
| Admin review | CI passes | Admin verdict (approve/changes/reject) via Claude Code skill | Yes |
| Post-merge tasks | PR merged | README index updates, CONTRIBUTORS.md, Discord announcement | Yes (admin) |

### Flow Diagram (ASCII)
```
Developer writes contribution
        |
        v
[PR opened] --> [CI: 15 automated rules] --fail--> [Fix & re-push]
        |                                              |
     pass                                              |
        |                                              |
        v                                              |
[Admin review via Claude Code]  <----------------------+
        |
    approve / changes / reject
        |
     approve
        |
        v
[Merge] --> [Post-merge: update indexes, CONTRIBUTORS, Discord]
```

### Transition Mechanisms
- **CI trigger**: GitHub Actions workflow (`ob1-review.yml`) fires on PR open/update
- **Admin trigger**: Manual invocation of `/review-pr <number>` skill in Claude Code
- **Post-merge**: Checklist generated by the review skill's Section E output

### Parallelism
No parallel execution in the contribution workflow. Skills themselves can dispatch parallel background evaluator agents (Panning for Gold Phase 2 uses up to 5 background agents).

---

## 4. Governance Model

### Constraint Expression
| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| Guard rails in CLAUDE.md | `CLAUDE.md` | Soft (LLM compliance) | Never modify `thoughts` table, no credentials, no binary blobs, MCP must be remote |
| CI automated rules | `.github/workflows/ob1-review.yml` | Hard (PR blocks) | 15 rules: folder structure, metadata validation, secret scanning, SQL safety, scope check, link resolution |
| JSON Schema validation | `.github/metadata.schema.json` | Hard (CI validates) | metadata.json structure requirements |
| CONTRIBUTING.md rules | `CONTRIBUTING.md` | Soft (human review) | What goes where, PR format, README standards, visual formatting requirements |
| Category curation gates | README + CONTRIBUTING.md | Soft (admin enforced) | Extensions and primitives are curated — must discuss with maintainers first |
| License constraint | `LICENSE.md` | Legal | FSL-1.1-MIT — no commercial derivative works |

### Guardrail Patterns
1. **Two-layer review**: CI handles mechanical checks (15 rules); Claude Code admin skill handles judgment (security deep scan, mission fit, naming consistency). Neither alone is sufficient.
2. **SQL safety guards**: No `DROP TABLE`, `TRUNCATE`, or unqualified `DELETE FROM`. No modifications to core `thoughts` table columns.
3. **Secret scanning**: CI checks for API keys, tokens, passwords. Admin skill does a deeper scan (base64-encoded values, connection strings, prompt injection).
4. **Remote MCP enforcement**: Must deploy as Supabase Edge Functions, not local servers. CI checks for `claude_desktop_config.json` and `StdioServerTransport` patterns.
5. **Prompt injection scanning**: Admin review skill checks skill files for `ignore previous`, `disregard`, `you are now`, `jailbreak`, `bypass`.

### Permission Model
- **Category-based**: Extensions and primitives are curated (maintainer approval required). Recipes, schemas, dashboards, integrations, and skills are open.
- **Contributor ladder**: Community Member → Contributor → Regular → Maintainer. Non-code contributions count at every level.
- **No RBAC in code**: No programmatic permission boundaries between agents. Guard rails are expressed as LLM instructions and CI rules.

---

## 5. Cross-Agent Protocol

### Agent Roster
| Agent/Role | Defined In | Capabilities | Communicates With |
|------------|-----------|--------------|-------------------|
| User's AI client | External (Claude, ChatGPT, Cursor, etc.) | Read/write Open Brain via MCP, invoke skills | Open Brain DB via MCP |
| CI review bot | `.github/workflows/ob1-review.yml` | 15 automated checks on PRs | GitHub PR comments |
| Admin reviewer | `.claude/skills/review-pr.md` | Security scan, mission fit, naming check | PR comments, Discord |
| Life Engine | `recipes/life-engine/life-engine-skill.md` | Proactive scheduled briefings, habit tracking | Telegram/Discord via channel tools |
| Background evaluators | Dispatched by skills (e.g., Panning for Gold) | Per-idea evaluation, write to permanent files | File-based output |

### Handoff Mechanisms
**No multi-agent orchestration.** OB1 is fundamentally a single-agent system — the user's AI client interacts with Open Brain via MCP tools. There is no agent-to-agent communication protocol.

The closest to multi-agent patterns:
1. **Background evaluator dispatch**: Panning for Gold dispatches up to 5 background agents for idea evaluation. Coordination is file-based — each evaluator writes to a permanent file, and the main skill reads those files for synthesis.
2. **CI → Admin handoff**: The CI bot produces a structured output (pass/fail per rule + post-merge tasks), which the admin review skill consumes as input context.
3. **Canonical skill dependencies**: The `requires_skills` field in metadata.json creates a loose coupling between recipes and skills, but this is a build-time dependency, not a runtime handoff.

### Shared State
- **Supabase database**: The primary shared state. All extensions, recipes, and skills read/write the same database.
- **Open Brain `thoughts` table**: The core shared data model. All data ingestion flows into a single table with vector embeddings.
- **File system (contributions)**: Each contribution is self-contained in its directory. No shared runtime state between contributions.

### Coordination Patterns
**Hub-and-spoke with the database as hub.** The Supabase database (especially the `thoughts` table with pgvector) is the central coordination point. Every AI client, extension, and recipe connects to it independently. There is no orchestrator — each component is autonomous and self-contained.

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | Medium | Minimal CLAUDE.md + on-demand skill loading; conditional reference loading in n-agentic-harnesses; companion prompts for onboarding |
| Model | Low | Model selection delegated to user's AI client; Panning for Gold recommends Opus for strategic ideas, Sonnet for research, Haiku for feasibility |
| Prompt | Medium | Skill trigger conditions as prompt routing; companion prompts for habit building; classifier prompts for adaptive capture |
| Tools | High | Remote MCP as the only tool integration pattern; Supabase Edge Functions as MCP servers; tool audit guide for managing tool surface area |
| Intent | Medium | Guard rails as behavioral constraints in CLAUDE.md; skill trigger conditions define when behaviors fire; non-negotiable rules in skills |
| Orchestration | Low | Single-agent architecture; background evaluator dispatch is the only multi-agent pattern |
| Evaluation | Medium | Two-layer PR review (CI + admin skill); 15 automated CI rules; tool audit for post-deployment quality |
| Sandboxing | Low | RLS (Row Level Security) primitive for multi-user data isolation; service_role key bypasses RLS |
| Governance | High | Two-layer review gate (CI + human); curated vs. open categories; contributor ladder; SQL safety rules; prompt injection scanning; FSL-1.1-MIT license |
| Agent Design | High | Skill template pattern (frontmatter + Problem/Trigger/Process/Output/Notes); self-improving skills with lessons logs; AGENT_SPEC.md as machine-readable generator spec; extension progressive learning path |
| Agentic OS | High | Full personal/business OS domain coverage (household, maintenance, calendar, meals, CRM, career); Life Engine proactive assistant; daily digest; data import recipes (ChatGPT, Gmail, Twitter, Obsidian); "one brain, all AI clients" architecture |

### Findings Candidates

1. **Self-improving skill architecture** (Agent Design) — Skills include a Phase 4 "self-improvement" step and a Lessons Log table. After every use, the skill checks for lost work, token waste, and user corrections, then updates itself. This creates a production-tested feedback loop within individual skills without requiring a separate eval framework. Panning for Gold has 6 documented lessons from real sessions.
→ Promoted to [[self-improving-skill-lessons-log]] on 2026-04-20

2. **Two-layer review gate pattern** (Governance) — CI handles 15 mechanical rules (structure, secrets, SQL safety, scope, links); a Claude Code admin skill handles judgment (security deep scan, mission fit, naming consistency). Neither layer alone is sufficient. The CI layer blocks PRs; the admin layer produces structured output (checklist, verdict, Discord draft, post-merge tasks). This separates deterministic checks from LLM-judgment checks in a way that's auditable.
→ Promoted to [[two-layer-ci-plus-llm-review-gate]] on 2026-04-20

3. **Template-driven contribution scaffolding** (Agent Design) — Every category has a `_template/` directory. The extension template includes a full `AGENT_SPEC.md` — a machine-readable spec that lets an AI agent generate all 5 required files (README.md, metadata.json, schema.sql, index.ts, deno.json) from a single prompt. This is a concrete implementation of the "spec-as-generator" pattern.
→ Promoted to [[spec-as-generator-agent-spec-pattern]] on 2026-04-20

4. **Canonical skill separation with dependency declaration** (Orchestration) — Reusable skills live in `skills/`. Recipes declare `requires_skills` in metadata.json. Recipe-local `.skill.md` files are allowed but discouraged for reusable behavior. This creates a loose dependency graph without runtime orchestration — a build-time composition pattern.
→ Skipped: incremental variant of [[skill-chaining-composing-workflows-from-modular-s]] on 2026-04-20

5. **Personal OS progressive learning path** (Agentic OS) — 6 curated extensions that compound. Extensions build on each other: CRM knows about captured thoughts, meal planner checks who's home, job hunt contacts become professional network contacts. This demonstrates how to design a progressive adoption path for an agentic personal OS, moving users from single-domain to cross-domain agent capabilities.
→ Promoted to [[progressive-adoption-path-compounding-extensions]] on 2026-04-20

6. **Proactive scheduled agent pattern** (Agentic OS) — Life Engine implements a time-aware personal assistant loop: date anchor → duplicate check → time window decision → external pull (calendar) → internal enrich (Open Brain search) → deliver via channel tools → log. Includes 7 briefing types, habit tracking with streak management, and weekly self-improvement reviews. Runs on Telegram/Discord via channel tools.
→ Promoted to [[time-window-proactive-agent-loop]] on 2026-04-20

7. **Hub-and-spoke memory architecture** (Context Engineering) — One Supabase database (pgvector) as the central brain, any AI client connects via MCP. No middleware, no sync protocol. Extensions, recipes, and skills all read/write the same `thoughts` table. This contrasts with file-first approaches (MetaSystem, OpenClaw) and structured ontology approaches (Paperclip).
→ Skipped: covered by multiple existing memory architecture findings on 2026-04-20

---

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-04-20 | latest | All 5 + research mapping | Initial analysis |
