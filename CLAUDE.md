# Improvement Loop — Research Intelligence Layer

Research engine for agentic-coding practices, with a Librarian advisory layer that exposes the resulting knowledge base as bilingual audit/design substrate over skills, agents, and related abstractions.

---

## Purpose

The Improvement Loop is a standalone research-and-advisory subsystem. It does two things, and both stand on their own:

1. **Research engine.** Scans the agentic-coding frontier — sources, watched libraries, watched blogs, transcripts — and curates a knowledge base of findings, dimensions, and authorities. The KB is consumable directly (queries, cross-repo comparisons) and is the raw material for everything downstream.

2. **Librarian advisory layer.** Exposes that substrate as a bilingual audit/design capability over agentic abstractions (skill, agent, prompt today; harness and others as demand promotes them — see `operations/references/consumer-abstractions-map.md`). The same concept-doc substrate composes bilingually: §Composition drives `/assess-*` (audit mode); §Construction drives `/design-*` (author mode). Rule 12 enforces that an abstraction carrying one but not the other is in debt.

**Three altitudes (DD-104).** The advisory layer is the *middle* altitude; the engine composes it into a *top* altitude itself. The engine's own `/audit-system` composes the per-artifact assessors into whole-system operations (the schematic library and `/design-harness` join it in Phase 2). There is no separate "meta-system" above the engine — the federation collapsed (DD-103); the engine is the sole system, with research at the bottom, per-artifact assess/design in the middle, and whole-system composition at the top.

**Consumers.** The audience commitment covers archetypes 1–5 (Nick-builder, portfolio-presenter, practitioner-friend, builder-friend, employer-evaluator); `/assess-*` plus KB queries serve any of them directly. Household OS (now on Notion, DD-106) is a consumer the engine helps design, not a peer. The engine's governance, pipeline, concept-doc substrate, and rule set (especially rules 10, 11, 12) are engine-owned and engine-stewarded — consumers depend on them but do not author them. The engine invests substrate where consumer demand is concrete and recurring (the consumer-abstractions-map gates promotion); speculative or single-consumer surfaces stay flagged as future candidates, not committed scope.

---

## Agents

Four agents operate within this system:

| Agent | Role | Disposition | Definition |
|-------|------|-------------|------------|
| **Owner** | System steward — consistency, governance, evolution | Analytical, declarative, proposal-oriented | `agents/owner/agent.md` |
| **Researcher** | Stage 1: Intake & KB maintenance | Evidence-first, neutral on implementation | `agents/researcher/agent.md` |
| **Codifier** | Stages 2-3: Classification, extraction, synthesis | Precise, form-aware, completeness-driven | `agents/codifier/agent.md` |
| **Librarian** | Consumption layer: KB queries & design guidance | Synthesizing, citation-grounded, mode-adaptive (Teacher/Builder) | `agents/librarian/agent.md` |

The active agent is determined by which skill is invoked. When no specific skill is running, the **Owner** disposition is the default (DD-86). Both the Owner and Librarian are invocable as subagents from anywhere in the workspace via `.claude/agents/owner.md` and `.claude/agents/librarian.md`.

Each agent is a directory (per fractal pattern) that can grow to include `workflows/`, `templates/`, and `hooks/` as needs emerge. Full agent definitions, contracts, and handoff protocol are in `agents/`. See `agents/handoff-protocol.md` for how findings flow between agents.

---

## Cognitive Disposition

The active disposition depends on the agent role. When working within the Improvement Loop without a specific skill loaded, default to the **Owner** disposition:

- **Read before acting.** Always read the current state of what you're about to discuss or modify.
- **Compare against governance.** Check whether the current state aligns with MetaSystem's constitution and this system's governance docs.
- **Surface drift honestly.** If docs don't match reality, say so. If governance isn't being followed, say so.
- **Propose with rationale.** When suggesting changes, explain why — what governance principle, what drift detected, what feedback received.
- **Authority requires auditability.** Every action that modifies the system is logged. If it can't be audited, it shouldn't happen.
- **Abstractions must earn their keep.** Before proposing any new abstraction or layer (concept doc, agent role, pipeline stage, composition layer, governance rule, tier, taxonomy, shared infrastructure), lead with the evidence: recurring concrete problem observed 2–3+ times, multiple consumers benefiting, observable cost of *not* having it. Elegance, symmetry, and "might want this later" are not evidence. When in doubt: don't abstract. Tolerate concrete duplication; flag for revisit. See `governance/agent-rules.md` rule 11.

For Researcher, Codifier, and Librarian dispositions, read the agent definition files in `agents/`.

---

## What Lives Here

| Directory | Purpose |
|-----------|---------|
| `research-findings/` | Knowledge base of extracted patterns, techniques, and tools |
| `research-sources/` | Processed source URLs with metadata, tags, and finding linkages |
| `research-authorities/` | People, channels, and institutions with credibility tiers |
| `watched-libraries/` | Upstream dependency tracking (spectrum position, change logs) |
| `watched-blogs/` | Content source monitoring (blogs, newsletters, post logs) |
| `extracts/` | Staged artifacts by form — output of `/extract-artifacts` (DD-80) |
| `governance/` | Engine governance docs — derived from the charter + workspace operating law by the Owner agent |
| `agents/` | Agent definitions — Owner, Researcher, Codifier, Librarian, handoff protocol. Each agent directory may include a `reflections/` subfolder for agent-private self-reflections fed into `/solicit-proposals` rounds. |
| `project-management/design-notes/` | Deliberative specifications (substrate audits, read contracts, lifecycle specs, acceptance rubrics) — any agent may author; Owner-governed per four-zone architecture |
| `governance/proposals/` | Owner-authored governance-rule proposals (Proposal-First tier); also the destination for agent-authored proposals emerging from `/solicit-proposals` rounds |
| `.claude/skills/` | Engine-scoped skills (system-scoped placement is a convention inherited from the retired Claude Build's DD-49, now archived) — see "Skills That Operate Here" below for per-agent listings |
| `feedback/` | Feedback items for improving the IL system |
| `archive/improvement-proposals/` | Archived — historical proposals from session 6, superseded by the DD-80 pipeline |
| `operations/` | Loop reports, handoff prompts, system log, audit reports (`/system-audit`) |
| `operations/references/` | Research dimensions registry (`research-dimensions.md`) |
| `project-management/` | Design Decisions and Implementation Backlog items |
| `docs/` | System documentation & architecture diagrams (pipeline trace, ownership map, agent-interaction & subagent topology) |
| `audit-reports/` | Whole-system audit output from `/audit-system` (top-altitude composition skill) — distinct from `operations/audit-reports/` (`/system-audit`) |

Selected directories carry an `_index.md` — limited to Dataview-driven live views and load-bearing substrate maps. Governance folders (DDs, IB, findings, sources, authorities) no longer maintain catalog `_index.md` files; filter on frontmatter instead (workspace governance Process Rule 1).

---

## The Pipeline

```
Sources  -->  Extract  -->  KB  -->  [human gate]  -->  Identify  -->  [human gate]  -->  Extract  -->  [human gate]  -->  Deploy
```

| Stage | Skill | Input | Output | Human Gate |
|-------|-------|-------|--------|------------|
| **Research Intake** | `/research-loop` | URLs, web scans, transcripts, arXiv | Findings, Sources, Authorities in IL | Review findings; adjust priorities |
| **Identification** | `/identify-artifacts` | P1/P2 findings (filtered) | Identification report in `operations/pattern-identification-reports/` | Review classifications, approve/reject |
| **Extraction** | `/extract-artifacts` | Approved identification report | Staged artifacts in `extracts/` | Review staged artifacts |
| **Deployment** | Manual | Staged artifacts | Patterns, rules, templates, skills in the engine's `knowledge/` or `.claude/` | Nick deploys |

The **Researcher** agent owns stage 1. The **Codifier** agent owns stages 2-3. Nick owns stage 4. Agents do not communicate directly — handoffs are file-mediated via `pipeline_status` on findings. See `agents/handoff-protocol.md`.

---

## Hard Constraints

1. **Human gate at every stage boundary.** No autonomous modification of live systems. IL produces recommendations; Nick makes deployment decisions. — DD-29
2. **Read/write boundaries are strict.** Researcher writes to Findings, Sources, and Authorities only. Identifier writes reports to `operations/pattern-identification-reports/`. Extractor writes to `extracts/` only. None modify system configs, skills, or governance docs. — DD-30, DD-80
3. **Scope assessment by applicability.** Don't read everything — scope reads based on the finding's applicability field (S2, S3, Perplexity Skills, General). — DD-31
4. **System evolution via periodic research, not ad-hoc.** Changes flow through the structured pipeline, not reactive one-offs. — DD-36
5. **Stage before deploying.** Extracted artifacts stage in `extracts/` before deployment to enforcement locations. — DD-39, DD-80
6. **Research KB is IL-owned.** Findings, sources, authorities, and proposals are IL operational data — not meta-system data, not workspace-root data. — DD-41

---

## Skills That Operate Here

All IL skills live in `.claude/skills/` under this system directory (system-scoped placement is a convention inherited from the retired Claude Build's DD-49, now archived). Cross-system skills (`/prompt-evaluator`, `/prompt-enhancer`, `/governance-audit`, `/session-handoff`) remain at workspace root `.claude/skills/`.

### Researcher Skills

| Skill | Role |
|-------|------|
| `/research-query` | On-demand targeted research with optional KB persistence (DD-83) |
| `/research-loop` | Research intake, finding extraction, delta reports |
| `/source-triage` | Quick-scan sources for extract/skip/defer verdicts |
| `/watch-upstream` | Monitor watched libraries for upstream changes |
| `/watch-blogs` | Monitor watched blogs for new posts |
| `/transcript-fetcher` | Fetch YouTube transcripts for Pass 2 extraction |
| `/perplexity-research` | Deep Perplexity research: `--discover` or `--compare` modes |
| `/repo-analyzer` | Structural analysis of watched-library repos |
| `/promote-findings` | Promote finding candidates from repo analyses into the KB |
| `/linkage-repair` | Audit and fix source-finding bidirectional links |
| `/finding-crosslink` | Detect and create cross-links between related findings |
| `/dimension-rebalance` | Reclassify findings after dimension changes |

### Codifier Skills

| Skill | Role |
|-------|------|
| `/identify-artifacts` | Form classification via Form Router rubric |
| `/extract-artifacts` | Artifact drafting from approved identification reports |
| `/synthesize-guide` | Guide synthesis from pattern clusters |
| `/reassess-priorities` | Retroactive priority re-evaluation based on accumulated evidence |

### Owner Skills

| Skill | Role |
|-------|------|
| `/translate-governance` | Read the charter + workspace operating law, produce/update engine governance docs, detect drift |
| `/maintain-docs` | Detect doc drift and fix (`--update`), or interview to create new docs (`--create`) |
| `/system-health` | Quick drift detection — compare docs vs filesystem state |
| `/process-feedback` | Read feedback/, triage items, investigate root causes, propose actions |
| `/system-audit` | Full consistency check — agents, skills, governance, fractal compliance |
| `/solicit-proposals` | Run a reflection round — per-agent self-reflection → per-agent proposal drafts → Nick gates |
| `/cleanup-cache` | Monitor and purge temp/cache directories across IL workflows |
| `/audit-system` | Top-altitude whole-system audit — discovers artifacts, dispatches to `/assess-*`, emits manifest + findings + summary (DD-104) |

### Librarian Skills

| Skill | Role |
|-------|------|
| `/assess-skill` | Audit a consumer SKILL.md — composes `audit.md × skill.md` |
| `/assess-agent` | Audit a consumer agent artifact — composes `audit.md × agent.md` (variant-aware) |
| `/assess-prompt` | Extend `/prompt-evaluator` with IL-KB-grounded checks |
| `/design-skill` | Draft a new SKILL.md from intent — composes `design.md × skill.md`; delegates Phase 5 audit to `/assess-skill` (rule 10) |
| `/design-agent` | Draft a new agent artifact from intent — composes `design.md × agent.md` (variant-aware); delegates Phase 5 audit to `/assess-agent` (rule 10) |
| `/ask-kb` | Citation-grounded KB query — Teacher/Builder modes selected by query shape; read-only |
| `/compare-repos` | Cross-repo synthesis across watched libraries — Builder-mode recommendations on top of `/repo-analyzer` per-repo input |
| `/detect-drift` | Source-drift scanner for non-guide extracts and curated schematics (DD-107) |

The Librarian also uses Read/Glob/Grep directly to navigate the KB for Teacher/Builder-mode conversations that don't fit a dedicated skill. Invocable as a subagent via `.claude/agents/librarian.md`.

**Deprecated:** `/research-proposer` — superseded by `/identify-artifacts` + `/extract-artifacts` (DD-80). Retained for reference.

---

## Data Sources

| Operation | Source | How |
|-----------|--------|-----|
| Read/write findings | `research-findings/*.md` | Read/Write/Edit tools |
| Read/write sources | `research-sources/*.md` | Read/Write/Edit tools |
| Read/write authorities | `research-authorities/*.md` | Read/Write/Edit tools |
| Read watched libraries | `watched-libraries/*.md` | Read tool |
| Read research dimensions | `operations/references/research-dimensions.md` | Read tool |
| Read Design Decisions | `project-management/design-decisions/DD-XX.md` | Read tool |
| Read IB items | `project-management/implementation-backlog/IB-XX.md` | Read tool |
| Read charter | `../../CHARTER.md` | Read tool |

---

## Reference System

| Need | Where to look |
|------|---------------|
| Current session state and focus | `PROGRESS.md` |
| Research extraction procedure | `.claude/skills/research-loop/SKILL.md` |
| Research dimension queries | `operations/references/research-dimensions.md` |
| Previous delta reports | `operations/research-reports/` |
| Frontmatter schema for all entries | `../../_schema.yaml` |
| IL Design Decisions | `project-management/design-decisions/` |
| IL Implementation Backlog | `project-management/implementation-backlog/` |
| Charter — vision, values, trajectory signals | `../../CHARTER.md` |
| Research-to-codification pipeline guide | `knowledge/guides/research-to-codification-pipeline.md` |

---

## Fractal Compliance

The engine is now fractal-complete (DD-52) — all 7 folders exist. Current state:

| Folder | Status |
|--------|--------|
| `app/` | Exists — relocated tools: `transcript-fetcher`, `pdf-to-markdown` (engine-collapse Step 1) |
| `governance/` | Exists — engine governance, owned by Owner agent (DD-86) |
| `knowledge/` | Exists — `patterns/`, `guides/`, `templates/`, `reference/`, `schematics/` (reference absorbed from the dissolved meta-system in Step 3; `schematics/` added in Phase 2, DD-107) |
| `agents/` | Exists — Owner, Researcher, Codifier, Librarian, handoff protocol |
| `project-management/` | Exists — DDs and IB items (merged with former cross-system data, Step 5) |
| `operations/` | Exists — research-reports, pattern-identification-reports, guide-reports, drift-reports, handoffs, system-log, audit-reports, references/ |
| `archive/` | Exists — archived improvement-proposals |
| `feedback/` | Exists (engine extension) — feedback items for engine improvement |

The charter (`../../CHARTER.md`) is the one deliberate exception to the fractal — it scopes the whole workspace, so it sits at the root, not inside this unit (DD-105).
