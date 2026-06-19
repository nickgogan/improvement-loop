---
title: "BMAD Method -- Structural Analysis"
id: "bmad-method-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-08"
updated: "2026-04-08"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "bmad-method"
analyzed_version: "v6.2.2"
analyzed_date: "2026-04-08"
repo_url: "https://github.com/bmad-code-org/BMAD-METHOD"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
  - "research-dimension-mapping"
---

# BMAD Method -- Structural Analysis

- **Repo:** <https://github.com/bmad-code-org/BMAD-METHOD>
- **Version:** v6.2.2
- **Date:** 2026-04-08
- **Spectrum:** cherry-pick

---

## Structural Inventory

- **Total files:** 559
- **Total directories:** 144
- **Markdown files:** 418 (74.8%)
- **JS files:** 41 (7.3%)
- **YAML files:** 26
- **CSV files:** 18
- **JSON files:** 10
- **MJS files:** 7
- **PNG files:** 6
- **TOML files:** 5
- **MDX files:** 5
- **Other:** 3 (TS, SH, PY, HTML, etc.)
- **MD-to-code ratio:** 8.5:1 (extreme MD dominance)
- **Max directory depth:** 7

### Markdown Composition

| Purpose | Count | Directory |
|---------|-------|-----------|
| Skill definitions (SKILL.md entrypoints) | 41 | `src/bmm-skills/`, `src/core-skills/` |
| Step files (workflow steps) | 112 | `src/*/steps/`, `src/*/steps-*/` |
| Workflow orchestrators | 22 | `src/*/workflow.md` |
| Templates | ~15 | `src/*/templates/`, `src/*/*.template.md` |
| Agent sub-definitions | ~8 | `src/*/agents/` |
| Prompts/references | ~10 | `src/*/prompts/`, `src/*/references/`, `src/*/data/` |
| IDE templates (multi-platform) | 19 | `tools/installer/ide/templates/` |
| Human documentation (en) | ~20 | `docs/explanation/`, `docs/how-to/`, `docs/reference/`, `docs/tutorials/` |
| i18n docs (cs, fr, vi-vn, zh-cn) | ~150 | `docs/{locale}/` |
| Project/community files | ~15 | Root (README, CHANGELOG, CONTRIBUTING, SECURITY, etc.) |
| Test fixtures | ~6 | `test/` |
| **Total** | **~418** | |

**Key insight:** 418 markdown files with 112 step files + 41 SKILL.md + 22 workflows = 175 functional execution files. The framework IS its markdown. Code (41 JS + 7 MJS) is exclusively tooling: installer, CLI, validator, tests.

**Directory naming:** kebab-case throughout. Phase-numbered top-level (`1-analysis`, `2-plan-workflows`, `3-solutioning`, `4-implementation`).

### Top-Level Structure

```
.
├── .augment/           # Augment code review config
├── .claude-plugin/     # Claude marketplace manifest
├── .github/            # CI, issue/PR templates
├── .husky/             # Git hooks
├── .vscode/            # Editor config
├── docs/               # Human docs + i18n (cs, fr, vi-vn, zh-cn)
├── src/
│   ├── bmm-skills/     # 30 phase-organized skills (4 phases)
│   │   ├── 1-analysis/         # 8 skills: analyst, tech-writer, document-project, prfaq, product-brief, 3 research
│   │   ├── 2-plan-workflows/   # 6 skills: PM, UX designer, create/edit/validate PRD, create UX
│   │   ├── 3-solutioning/      # 5 skills: architect, create-architecture, create-epics, check-readiness, gen-project-context
│   │   └── 4-implementation/   # 11 skills: dev, checkpoint-preview, code-review, correct-course, create-story, dev-story, qa-e2e, quick-dev, retrospective, sprint-planning, sprint-status
│   └── core-skills/    # 11 cross-phase skills: brainstorming, distillator, elicitation, editorial reviews, help, index-docs, party-mode, adversarial review, edge-case hunter, shard-doc
├── test/               # Test files + fixtures
├── tools/              # Installer, validator, docs tools
└── website/            # Astro documentation site
```

### Notable Structural Patterns

1. **Everything-as-skill architecture**: Post-v6.2.2, ALL agents and workflows are SKILL.md-based. No separate agents directory -- agents are skills with persona definitions.
2. **Phase-numbered organization**: `bmm-skills/` uses numbered prefixes (1-4) matching the SDLC phases.
3. **Step-file micro-architecture**: Complex workflows decompose into numbered step files (`step-01-init.md` through `step-12-complete.md`). Just-in-time loading -- only current step in memory.
4. **CSV data tables**: Domain complexity, project types, brainstorming methods, and agent manifests stored as CSV for structured lookup.
5. **Multi-IDE installer**: Templates for Claude, OpenCode, Kiro, Windsurf, Trae, Rovodev, Antigravity -- same skills, different harness packaging.

---

## Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `AGENTS.md` (root) | LLM | Global | Auto-loaded | Constraints/Rules | Project rules: conventional commits, quality checks |
| `src/bmm-skills/*/SKILL.md` (41 files) | LLM | Tool | Auto-loaded | Identity/Persona + Workflow | Skill entrypoints: frontmatter (name, description) + L2 instructions |
| `src/core-skills/*/SKILL.md` (11 files) | LLM | Tool | Auto-loaded | Identity/Persona + Workflow | Cross-phase skill entrypoints |
| `src/*/workflow.md` (22 files) | LLM | Task | Referenced | Workflow/Process | Orchestration logic: step sequencing, config loading, routing |
| `src/*/steps/step-*.md` (112 files) | LLM | Task | Referenced | Workflow/Process | Individual workflow steps: just-in-time loaded, sequential |
| `src/*/agents/*.md` (~8 files) | LLM | Task | Injected | Identity/Persona | Sub-agents within skills (distillator compressor, prfaq analyzers) |
| `src/*/prompts/*.md` (~4 files) | LLM | Task | Referenced | Workflow/Process | Contextual prompts for skill phases |
| `src/*/templates/*.md` (~15 files) | LLM | Tool | Referenced | Memory/State | Output templates for artifacts (PRD, architecture, stories, etc.) |
| `src/*/data/*.csv` (~18 files) | LLM | Tool | Referenced | Tool Usage | Structured data: domain complexity, project types, brainstorming methods |
| `tools/skill-validator.md` | LLM | Global | Referenced | Constraints/Rules | 27-rule validation spec for skill quality |
| `tools/installer/ide/templates/combined/*.md` (19 files) | LLM | Global | Auto-loaded | Identity/Persona + Workflow | IDE-specific agent/workflow templates |
| `docs/**/*.md` | Human | Global | Referenced | Workflow/Process | Human documentation with i18n |

**Sampling notes:** Read 6 SKILL.md exemplars in full (analyst, PM, architect, dev, brainstorming, distillator). Classified remaining 35 by structural pattern (identical activation protocol, capabilities table, persona format). Read 3 workflow.md and 2 step files in full. Classified remaining by pattern.

### Context Loading Strategy

**Three-level progressive disclosure with config-driven activation:**

1. **L1 -- Metadata** (~100 tokens per skill): SKILL.md frontmatter (`name`, `description`) loaded at startup into harness system prompt. Used for skill auto-discovery.
2. **L2 -- Instructions** (<5K tokens): SKILL.md body loaded when skill is triggered. Contains persona definition, capabilities table, and activation protocol.
3. **L3 -- Resources** (unlimited): workflow.md, step files, templates, CSV data loaded on demand. Step files loaded just-in-time -- only current step in memory, never forward-loading.

**Config-driven activation**: Every agent skill loads `{project-root}/_bmad/bmm/config.yaml` on activation to resolve: user_name, communication_language, document_output_language, planning_artifacts path, project_knowledge path. This externalizes user preferences from skill logic.

**Skill-as-agent pattern**: Agent personas (Mary the Analyst, John the PM, Winston the Architect, Amelia the Dev) are implemented as skills, not separate agent definitions. The SKILL.md IS the agent identity. When activated, the skill "becomes" the persona and stays in character.

**Step-file sequential loading**: Complex workflows use micro-file architecture -- each step is a self-contained file with explicit instructions. Steps are loaded one at a time in sequence. Forward-loading is forbidden (STEP-05 rule). This prevents context pollution from future steps.

---

## Workflow Topology

### Phases/Stages

| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| **1. Analysis** | Activate analyst/researcher skills | Product brief, research docs, PRFAQ created | Yes -- user reviews/accepts |
| **2. Plan** | Activate PM/UX designer skills | PRD, UX design, epics/stories created | Yes -- validation pass |
| **3. Solutioning** | Activate architect skill | Architecture doc, implementation readiness check | Yes -- readiness report |
| **4. Implementation** | Activate dev skill | Stories implemented with tests | Yes -- code review, sprint review |

### Flow Diagram

```
┌──────────────────────┐
│  1. ANALYSIS         │
│  Mary (Analyst)      │──── User: reviews product brief
│  Tech Writer         │──── Brainstorming, research
│  PRFAQ               │
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│  2. PLAN             │
│  John (PM)           │──── User: reviews PRD
│  UX Designer         │──── Validation pass (13-step)
│  PRD creation        │
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│  3. SOLUTIONING      │
│  Winston (Architect) │──── Readiness check
│  Architecture docs   │──── User: reviews arch decisions
│  Epics & Stories     │
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│  4. IMPLEMENTATION   │
│  Amelia (Dev)        │──── Story execution
│  Code review         │──── Sprint planning/status
│  QA / E2E tests      │──── User: reviews code
└──────────────────────┘

Cross-phase skills available at all stages:
  • Brainstorming (100+ ideas before organizing)
  • Advanced Elicitation (Socratic, first principles, pre-mortem, red team)
  • Adversarial Review (cynical review, edge-case hunting)
  • Distillator (lossless compression for context handoff)
  • Party Mode (multi-agent roundtable discussions)
```

### Transition Mechanisms

- **User-initiated**: Users activate agent personas (Mary, John, Winston, Amelia) which provide capabilities menus. User selects a capability, which invokes the corresponding skill.
- **Skill invocation**: Agent skills invoke sub-skills via `skill:skill-name` syntax. The `invoke` verb is enforced (REF-03 rule).
- **Step sequencing**: Within a workflow, each step file references the next step file. Sequential enforcement is mandatory.
- **Config-driven routing**: Workflows load project config to resolve paths and preferences before executing.

### Parallelism

- **Party Mode**: Spawns 2-4 agent subagents in parallel for roundtable discussions. Each gets independent context and produces genuine independent perspective.
- **Distillator fan-out**: For large document sets, spawns parallel compressor subagents per semantic group, then a merge compressor.
- **No workflow-level parallelism**: Phases are sequential. Within a phase, skills are invoked one at a time.

---

## Governance Model

### Constraint Expression

| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| AGENTS.md project rules | Root `AGENTS.md` | Hard | Conventional commits, quality checks before push |
| Skill validator (27 rules) | `tools/skill-validator.md` + `validate-skills.js` | Hard (14 deterministic) + Soft (13 inference) | SKILL-01 through REF-03: naming, paths, step sequencing, no forward-loading |
| Step-file architecture rules | Workflow files (inline) | Hard | "NEVER load multiple step files simultaneously", "NEVER skip steps" |
| Persona persistence | Agent SKILL.md files (inline) | Soft | "You must fully embody this persona... must not break character until user dismisses" |
| Sequential enforcement | Workflow files + validator | Hard | SEQ-01: No skip instructions. STEP-05: No forward loading. |
| Menu halt requirements | Validator STEP-04 | Hard | Steps presenting menus must explicitly HALT and wait |
| Anti-bias protocol | Brainstorming workflow | Soft | "Consciously shift creative domain every 10 ideas" to combat LLM semantic clustering |
| Skill encapsulation | PATH-05 rule | Hard | No file path references into another skill's directory |

### Guardrail Patterns

1. **Deterministic skill validator**: `validate-skills.js` checks 14 rules automatically (naming, structure, paths). Remaining 13 rules require LLM inference. Part of the CI quality pipeline.
2. **Step-file isolation**: Just-in-time loading prevents context pollution. Each step is self-contained with explicit goal, next-step reference, and halt conditions.
3. **Persona lock-in**: Agent personas explicitly state "must not break character until user dismisses." Persona persists across skill invocations within the same session.
4. **Skill encapsulation boundary**: PATH-05 forbids reaching into another skill's internal files. Skills are units -- invoke, don't reach.
5. **Progressive disclosure budget**: L1 (~100 tokens), L2 (<5K tokens), L3 (unlimited on-demand). Prevents loading unnecessary context.

### Permission Model

- **No per-agent tool restrictions**: Unlike GSD, BMAD does not specify tool allowlists per agent. Skills assume full tool access.
- **Config-driven preferences**: User preferences (language, output paths, project knowledge paths) externalized to config.yaml.
- **No explicit filesystem permissions**: Any activated skill can read/write anywhere.

---

## Cross-Agent Protocol

### Agent Roster (as skills with personas)

| Agent/Persona | Phase | Defined In | Capabilities | Communicates With |
|---------------|-------|-----------|--------------|-------------------|
| Mary (Analyst) | 1-Analysis | `bmad-agent-analyst/SKILL.md` | Brainstorming, market/domain/technical research, product brief, PRFAQ, document-project | Users directly; invokes sub-skills |
| Tech Writer | 1-Analysis | `bmad-agent-tech-writer/SKILL.md` | Explain concepts, mermaid generation, validate docs, write documents | Users directly |
| John (PM) | 2-Plan | `bmad-agent-pm/SKILL.md` | Create/validate/edit PRD, create epics/stories, check implementation readiness, correct course | Users directly; invokes sub-skills |
| UX Designer | 2-Plan | `bmad-create-ux-design/SKILL.md` | 14-step UX design workflow | Users directly |
| Winston (Architect) | 3-Solutioning | `bmad-agent-architect/SKILL.md` | Create architecture, check implementation readiness | Users directly; invokes sub-skills |
| Amelia (Dev) | 4-Implementation | `bmad-agent-dev/SKILL.md` | Dev story, quick dev, QA E2E tests, code review, sprint planning, create story, retrospective | Users directly; invokes sub-skills |
| Distillator sub-agents | Cross-phase | `bmad-distillator/agents/` | Compressor, round-trip reconstructor | Distillator orchestrator |
| PRFAQ sub-agents | 1-Analysis | `bmad-prfaq/agents/` | Artifact analyzer, web researcher | PRFAQ orchestrator |
| Product Brief sub-agents | 1-Analysis | `bmad-product-brief/agents/` | Artifact analyzer, opportunity/skeptic reviewer, web researcher | Product Brief orchestrator |
| Party Mode orchestrator | Cross-phase | `bmad-party-mode/SKILL.md` | Multi-agent roundtable facilitation | Spawns any agent as subagent |

### Handoff Mechanisms

1. **Skill invocation chain**: Agent personas present capabilities menus. User selects a capability, which invokes a sub-skill. The persona persists across invocations -- "When you are in this persona and the user calls a skill, this persona must carry through."
2. **Artifact-based handoff**: Skills produce documents (PRD, architecture doc, stories). Downstream skills consume these: `bmad-check-implementation-readiness` reads PRD, UX design, architecture, and epics to validate alignment.
3. **Party Mode subagent spawning**: Orchestrator spawns 2-4 agent subagents in parallel via the Agent tool. Each gets a prompt assembled from the agent manifest CSV + conversation context. Agents never communicate directly -- all routing through orchestrator.
4. **Distillator fan-out**: Orchestrator spawns compressor subagents per semantic group, then a merge compressor. Subagents return structured JSON results.
5. **Config-driven context passing**: `{project-root}/_bmad/bmm/config.yaml` provides shared configuration. `project-context.md` provides shared project context loaded by all agent skills on activation.

### Shared State

- **`_bmad/` directory**: Project-level config, agent manifest CSV, installed skills
- **`{planning_artifacts}/` directory**: Output documents (PRD, architecture, stories, sprint plans)
- **`project-context.md`**: Shared project context loaded by all agent skills
- **Config variables**: User preferences, output paths, language settings
- **No global state file**: Unlike GSD's STATE.md, BMAD has no central state tracker. State is implicit in produced artifacts.

### Coordination Patterns

**User-mediated hub with skill invocation chains.** The user is the explicit orchestrator -- they activate agent personas, select capabilities from menus, and decide when to move between phases. Within a phase, skills invoke sub-skills via `skill:skill-name`. Party Mode is the one exception: it spawns true subagents for parallel independent perspectives.

This is a fundamentally different model from GSD's automated hub-and-spoke: BMAD puts the human at the center of orchestration, while GSD automates the orchestration with human gates at phase boundaries.

---

## Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | **High** | Three-level progressive disclosure (L1 metadata, L2 instructions, L3 resources). Config-driven activation with externalized user preferences. Step-file just-in-time loading prevents context pollution. CSV data tables for structured lookup. Distillator for lossless document compression (verified by round-trip reconstruction). |
| Model | Low | No model selection or tier system. Party Mode has `--model` flag for subagent model override. |
| Prompt | **High** | Agent personas with names, communication styles, and principles. Menu-driven interaction patterns (capabilities tables). Step-file micro-architecture with sequential enforcement. CSV-backed elicitation method registry. Anti-bias protocol for brainstorming (shift domains every 10 ideas). |
| Tools | Medium | Skill validator (14 deterministic + 13 inference rules). Multi-IDE installer (Claude, OpenCode, Kiro, Windsurf, Trae, Rovodev, Antigravity). CSV data tables as structured tool inputs. Marketplace manifest (`.claude-plugin/`). |
| Intent | **High** | User-as-orchestrator model -- human explicitly selects agents, capabilities, and transitions. Menu halt requirements enforce wait-for-input. No autonomous phase transitions. Persona lock-in ensures consistent behavior within sessions. |
| Orchestration | **High** | Everything-as-skill architecture -- agents ARE skills. Four-phase SDLC (Analysis->Plan->Solutioning->Implementation). Skill invocation chains (agent->sub-skill). Party Mode for parallel multi-agent roundtables. User-mediated orchestration vs automated orchestration. |
| Evaluation | **High** | PRD validation (13-step process with density, measurability, traceability, leakage, compliance checks). Implementation readiness check (cross-artifact alignment). Adversarial review (cynical skepticism, minimum 10 issues). Edge-case hunter. Code review skill. Distillator round-trip validation (lossless verification). Deterministic skill validator with 27 rules. |
| Sandboxing | Low | No isolation mechanisms. Skills run in the host environment. |
| Governance | **High** | 27-rule skill validator (deterministic + inference). Skill encapsulation boundary (PATH-05). Sequential enforcement (no skipping, no forward-loading). Persona persistence across skill invocations. Agent Skills open standard compliance. |
| Agent Design | **High** | Named personas (Mary, John, Winston, Amelia) with identity, communication style, and principles. Skill-as-agent pattern -- agent identity IS the skill definition. Capabilities tables map codes to sub-skills. Activation protocol: load config -> load project context -> greet user -> present menu -> HALT. Cross-phase skills (brainstorming, elicitation, adversarial review) available to all personas. |

### Findings Candidates

1. **Everything-as-skill architecture** (Agent Design, Orchestration) -- Post-v6.2.2, BMAD merged agents and workflows into a unified SKILL.md-based architecture. Agent personas are skills, not separate definitions. This eliminates the agent/skill/workflow distinction that repos like GSD maintain. Compare to GSD's separate agents/ directory.
→ Promoted to [[everything-as-skill-architecture]] on 2026-04-08

2. **Step-file micro-architecture with sequential enforcement** (Context Engineering, Governance) -- Complex workflows decompose into numbered step files loaded one at a time. Just-in-time loading is enforced by validator rules (STEP-05: no forward-loading, SEQ-01: no skip instructions). This is a principled approach to context window management that prevents pollution from future steps.
→ Promoted to [[step-file-micro-architecture]] on 2026-04-08

3. **Deterministic skill validator** (Evaluation, Governance) -- 27-rule validation system with 14 deterministic checks (automated via `validate-skills.js`) and 13 inference-based checks (LLM-evaluated). Covers naming, paths, encapsulation, step structure, and cross-references. Integrated into CI quality pipeline. Novel pattern: using code to validate markdown skill definitions.
→ Skipped: duplicate of [[bmad-deterministic-skill-validator]] on 2026-04-19

4. **Named agent personas with session-locked identity** (Agent Design, Prompt) -- Agents have personal names (Mary, Winston, etc.), distinct communication styles, and explicit personality traits. Persona persistence is enforced: "must not break character until user dismisses." The persona carries through across sub-skill invocations. This is more than persona engineering -- it's session-level identity consistency.
→ Promoted to [[named-agent-personas-with-session-lock]] on 2026-04-08

5. **Anti-bias protocol for brainstorming** (Prompt, Evaluation) -- Explicit instruction to combat LLM sequential bias: "consciously shift creative domain every 10 ideas" and "aim for 100+ ideas before organization." Acknowledges LLM semantic clustering as a known failure mode and provides a concrete mitigation. Compare to Superpowers' brainstorming skill.
→ Promoted to [[anti-bias-protocol-for-llm-ideation]] on 2026-04-08

6. **Distillator with round-trip validation** (Context Engineering, Evaluation) -- Lossless document compression that distinguishes itself from summarization: "Summaries are lossy. Distillates are lossless compression optimized for LLM consumption." Verified by spawning a reconstruction subagent that rebuilds the source from the distillate alone, then diffing for semantic gaps and hallucinations. Novel verification methodology.
→ Promoted to [[distillator-with-round-trip-validation]] on 2026-04-08

7. **Multi-IDE portability via installer templates** (Tools, Agent Design) -- Same skills packaged for 7+ IDE platforms (Claude, OpenCode, Kiro, Windsurf, Trae, Rovodev, Antigravity) via installer templates. Demonstrates that SKILL.md-based architecture is genuinely platform-agnostic. The Agent Skills open standard enables this portability.
→ Promoted to [[multi-ide-portability-via-installer-templates]] on 2026-04-08

---

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-04-08 | v6.2.2 | all | Initial analysis. 559 files, 418 MD, 41 skills (30 phase + 11 core), 112 step files, 22 workflows. Everything-as-skill architecture. |
