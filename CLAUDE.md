# Improvement Loop — Research Intelligence Layer

The self-improvement subsystem for MetaSystem. Researches frontier practices in agentic coding and AI agent systems, extracts actionable findings into a structured knowledge base, and produces staged artifacts for human review before deployment. Everything downstream — codified patterns, agent templates, system upgrades — starts here.

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
| `governance/` | System-specific governance docs — derived from MetaSystem constitution by the Owner agent |
| `agents/` | Agent definitions — Owner, Researcher, Codifier, Librarian, handoff protocol |
| `.claude/skills/` | IL-scoped skills (per DD-49) — Researcher (12), Codifier (3), Owner (5) |
| `feedback/` | Feedback items for improving the IL system |
| `archive/improvement-proposals/` | Archived — 5 historical proposals from session 6, superseded by DD-80 pipeline |
| `operations/` | Loop reports, handoff prompts, next-scan-notes, system log |
| `operations/references/` | Research dimensions registry (`research-dimensions.md`) |
| `project-management/` | Design Decisions and Implementation Backlog items |

Each directory contains an `_index.md` catalog for Obsidian navigation and agent discovery.

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
| **Deployment** | Manual | Staged artifacts | Patterns, rules, templates, skills in `meta-system/knowledge/` or `.claude/` | Nick deploys |

The **Researcher** agent owns stage 1. The **Codifier** agent owns stages 2-3. Nick owns stage 4. Agents do not communicate directly — handoffs are file-mediated via `pipeline_status` on findings. See `agents/il-agent-handoff-protocol.md`.

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

All IL skills live in `.claude/skills/` under this system directory (per DD-49). Cross-system skills (`/prompt-evaluator`, `/prompt-enhancer`, `/governance-audit`, `/session-handoff`) remain at workspace root `.claude/skills/`.

### Researcher Skills (12)

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

### Codifier Skills (3)

| Skill | Role |
|-------|------|
| `/identify-artifacts` | Form classification via Form Router rubric |
| `/extract-artifacts` | Artifact drafting from approved identification reports |
| `/synthesize-guide` | Guide synthesis from pattern clusters |

### Owner Skills (5)

| Skill | Role |
|-------|------|
| `/translate-governance` | Read MetaSystem constitution, produce/update IL governance docs, detect drift |
| `/maintain-docs` | Detect doc drift and fix (`--update`), or interview to create new docs (`--create`) |
| `/system-health` | Quick drift detection — compare docs vs filesystem state |
| `/process-feedback` | Read feedback/, triage items, investigate root causes, propose actions |
| `/system-audit` | Full consistency check — agents, skills, governance, fractal compliance |

### Librarian Skills (0)

The Librarian uses Read/Glob/Grep tools directly to navigate the KB. No dedicated skills currently. Invocable as a subagent via `.claude/agents/librarian.md`.

**Deprecated:** `/research-proposer` — superseded by `/identify-artifacts` + `/extract-artifacts` (DD-80). Retained for reference.

---

## Data Sources

| Operation | Source | How |
|-----------|--------|-----|
| Read/write findings | `research-findings/*.md` | Read/Write/Edit tools |
| Read/write sources | `research-sources/*.md` | Read/Write/Edit tools |
| Read/write authorities | `research-authorities/*.md` | Read/Write/Edit tools |
| Read watched libraries | `watched-libraries/*.md` | Read tool |
| Read proposals (Researcher) | `improvement-proposals/*.md` | Read tool only |
| Read research dimensions | `operations/references/research-dimensions.md` | Read tool |
| Read next-scan-notes | `operations/next-scan-notes.md` | Read tool |
| Read IL Design Decisions | `project-management/design-decisions/DD-XX.md` | Read tool |
| Read IL IB items | `project-management/implementation-backlog/IB-XX.md` | Read tool |
| Read cross-system DDs | `../meta-system/project-management/design-decisions/` | Read tool |
| Read constitution | `../meta-system/governance/constitution.md` | Read tool |

---

## Reference System

| Need | Where to look |
|------|---------------|
| Current session state and focus | `PROGRESS.md` |
| Research extraction procedure | `.claude/skills/research-loop/SKILL.md` |
| Research dimension queries | `operations/references/research-dimensions.md` |
| Scan carry-forward notes | `operations/next-scan-notes.md` |
| Previous delta reports | `operations/research-reports/` |
| Frontmatter schema for all entries | `../../_schema.yaml` |
| IL Design Decisions | `project-management/design-decisions/` |
| IL Implementation Backlog | `project-management/implementation-backlog/` |
| Constitution and system boundaries | `../meta-system/governance/constitution.md` |
| Research-to-codification pipeline guide | `../meta-system/knowledge/guides/research-to-codification-pipeline.md` |

---

## Fractal Compliance

This system follows the fractal unit pattern (DD-52) partially. Current state:

| Folder | Status |
|--------|--------|
| `operations/` | Exists — research-reports, pattern-identification-reports, guide-reports, handoff-prompts, system-log, references/ |
| `project-management/` | Exists — DDs and IB items |
| `feedback/` | Exists — feedback items for IL system improvement |
| `agents/` | Exists — Owner, Researcher, Codifier, Librarian, handoff protocol |
| `governance/` | Exists — system-specific governance, owned by Owner agent (DD-86) |
| `app/` | Not yet created |
| `archive/` | Not yet created |

See IB-138 and IB-139 for fractal completion work items.
