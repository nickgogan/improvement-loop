---
title: "Skill-Artifact Map"
type: "generated-docs"
subject: "improvement-loop"
generated: "2026-05-25"
generator: "Owner agent · session 100"
regen_trigger: "Skill roster change · agent boundary change · new artifact directory added"
sources:
  - "systems/improvement-loop/CLAUDE.md"
  - "systems/improvement-loop/agents/handoff-protocol.md"
  - "systems/improvement-loop/agents/researcher/agent.md"
  - "systems/improvement-loop/agents/codifier/agent.md"
  - "systems/improvement-loop/agents/owner/agent.md"
  - "systems/improvement-loop/agents/librarian/agent.md"
siblings:
  - "subagent-topology.md"
---

# Skill-Artifact Map — Improvement Loop

Which skills create, edit, or read which files. Complements the directory-level [ownership-map](../2026-05-24/ownership-map.md) with skill-level granularity.

## TL;DR

Each IL skill has a narrow write surface. This map shows exactly what each skill touches — use it to trace where an artifact came from, or to verify that a proposed skill change won't violate agent boundaries.

---

## How to Read

Inherits conventions from the [session 87 docs](../2026-05-24/agent-interaction-model.md#how-to-read). Additions:

| Convention | Meaning |
|---|---|
| **C** (Create) | Skill writes new files to this path |
| **E** (Edit) | Skill updates existing files (metadata or content) |
| **R** (Read) | Skill reads from this path as input |
| Italic path | Conditional — only with certain flags or modes |

---

## Researcher Skills

### /research-loop

| Op | Path | What |
|----|------|------|
| C | `research-findings/*.md` | New findings with frontmatter + evidence |
| C | `research-sources/*.md` | New source entries with metadata |
| C | `research-authorities/*.md` | New authority entries |
| C | `operations/research-reports/*.md` | Delta report at session end |
| E | `research-findings/*.md` | Dedup merges, evidence updates |
| E | `research-sources/*.md` | Tag updates, finding linkage |
| R | `research-findings/*.md` | Dedup check before creating |
| R | `research-sources/*.md` | Existing source lookup |
| R | `operations/references/research-dimensions.md` | Dimension scoping |

### /research-query

| Op | Path | What |
|----|------|------|
| C | `research-findings/*.md` | New findings (if user approves persistence) |
| C | `research-sources/*.md` | New source entries (if user approves) |
| R | `research-findings/*.md` | Dedup check |
| R | `operations/references/research-dimensions.md` | Dimension fit check |

### /source-triage

| Op | Path | What |
|----|------|------|
| R | `research-sources/*.md` | Source metadata for triage |
| R | `research-findings/*.md` | Existing coverage check |

### /watch-upstream

| Op | Path | What |
|----|------|------|
| E | `watched-libraries/*.md` | Changelog appends, version updates |
| R | `watched-libraries/*.md` | Current entry state |

### /watch-blogs

| Op | Path | What |
|----|------|------|
| C | `research-sources/*.md` | New source entries for EXTRACT-verdict posts |
| E | `watched-blogs/*.md` | Post log appends |
| R | `watched-blogs/*.md` | Current entry state |

### /repo-analyzer

| Op | Path | What |
|----|------|------|
| C | `watched-libraries/analysis/*.md` | New analysis docs |
| C | `watched-libraries/_tmp/repo-cache/*/` | Shallow git clones (gitignored) |
| E | `watched-libraries/analysis/*.md` | Re-analysis on version bump |
| E | `watched-libraries/analysis/_index.md` | Index updates |
| R | `watched-libraries/*.md` | Registry entries for repo URLs |

### /promote-findings

| Op | Path | What |
|----|------|------|
| C | `research-findings/*.md` | Promoted findings from analysis docs |
| R | `watched-libraries/analysis/*.md` | Candidate extraction |
| R | `research-findings/*.md` | Dedup check |

### /transcript-fetcher

| Op | Path | What |
|----|------|------|
| C | `incubator/claude-build/app/transcript-fetcher/transcripts/*.md` | Fetched transcripts |
| R | `research-sources/*.md` | Source URL lookup |

### /linkage-repair

| Op | Path | What |
|----|------|------|
| E | `research-findings/*.md` | Fix broken source links |
| E | `research-sources/*.md` | Fix broken finding links |
| R | `research-findings/*.md` | Scan for unlinked entries |
| R | `research-sources/*.md` | Scan for orphaned entries |

### /finding-crosslink

| Op | Path | What |
|----|------|------|
| E | `research-findings/*.md` | Add `related_findings` links |
| R | `research-findings/*.md` | All findings for pair evaluation |

### /dimension-rebalance

| Op | Path | What |
|----|------|------|
| E | `research-findings/*.md` | Reclassify dimension fields |
| R | `research-findings/*.md` | All findings for evaluation |
| R | `operations/references/research-dimensions.md` | New dimension definitions |

### /perplexity-research

| Op | Path | What |
|----|------|------|
| C | `operations/research-reports/*.md` | Standalone research reports |
| R | `research-findings/*.md` | Gap analysis against KB |

---

## Codifier Skills

### /identify-artifacts

| Op | Path | What |
|----|------|------|
| C | `operations/pattern-identification-reports/*.md` | Identification report with form classifications |
| E | `research-findings/*.md` | Set `pipeline_status: classified` |
| R | `research-findings/*.md` | P1/P2 findings with `pipeline_status: raw` |
| R | `operations/references/form-classification-rubric.md` | Form Router criteria |

### /extract-artifacts

| Op | Path | What |
|----|------|------|
| C | `extracts/{form}/*.md` | Staged artifacts (patterns, rules, skills, templates, agents) |
| E | `research-findings/*.md` | Set `pipeline_status: extracted`, add `consumed_by` |
| R | `operations/pattern-identification-reports/*.md` | Approved identification report |
| R | `research-findings/*.md` | Finding content for drafting |
| R | `extracts/{form}/*.md` | Dedup against existing extracts |

### /synthesize-guide

| Op | Path | What |
|----|------|------|
| C | `extracts/guides/*.md` | New or regenerated guide |
| C | `extracts/guides/changelog/*.md` | Guide changelog entries |
| C | `operations/guide-reports/*.md` | Synthesis report |
| E | `research-findings/*.md` | Set `pipeline_status: synthesized`, add `consumed_by` |
| E | `extracts/guides/*.md` | Guide content updates on resynthesis |
| E | `operations/references/guide-routing-table.md` | Update synthesis status, finding counts |
| R | `research-findings/*.md` | Findings in the guide's cluster |
| R | `operations/references/guide-routing-table.md` | Cluster membership |
| R | `extracts/guides/*.md` | Existing guide state |
| R | *`extracts/guides/*.harvest-queue.md`* | Harvest queue candidates |

### /reassess-priorities

| Op | Path | What |
|----|------|------|
| E | `research-findings/*.md` | Priority field updates |
| R | `research-findings/*.md` | Evidence base scan |

---

## Owner Skills

### /translate-governance

| Op | Path | What |
|----|------|------|
| C | `governance/*.md` | New system-specific governance docs |
| E | `governance/*.md` | Drift fixes |
| R | `../meta-system/governance/constitution.md` | Source governance |
| R | `../meta-system/governance/vocabulary.md` | Terminology |
| R | `governance/*.md` | Current translations |

### /maintain-docs

| Op | Path | What |
|----|------|------|
| E | `CLAUDE.md` | Documentation updates |
| E | `agents/*/agent.md` | Agent definition updates |
| E | `.claude/skills/*/SKILL.md` | Skill contract updates |
| R | All system state | Drift comparison |

### /system-health

| Op | Path | What |
|----|------|------|
| R | All system state | Read-only diagnostic |

### /system-audit

| Op | Path | What |
|----|------|------|
| C | `operations/audit-reports/*.md` | Audit report |
| R | All system state | Comprehensive consistency check |

### /process-feedback

| Op | Path | What |
|----|------|------|
| R | `feedback/*.md` | Pending feedback items |
| R | All system state | Root cause investigation |

### /solicit-proposals

| Op | Path | What |
|----|------|------|
| C | `agents/*/reflections/*.md` | Per-agent reflection notes |
| C | `governance/proposals/*.md` | Agent-drafted proposals |
| R | `agents/*/reflections/*.md` | Freshness check |

### /cleanup-cache

| Op | Path | What |
|----|------|------|
| R | `watched-libraries/_tmp/repo-cache/` | Size and age scan |
| R | `watched-libraries/*.md` | Cross-reference against registry |

---

## Librarian

No dedicated skills. Reads via direct tool access:

| Op | Path | What |
|----|------|------|
| R | `extracts/guides/*.md` | Preferred — most refined form |
| R | `extracts/{form}/*.md` | Staged artifacts by form |
| R | `research-findings/*.md` | Raw findings |
| R | `../meta-system/knowledge/` | Deployed artifacts (most authoritative) |
| R | `operations/references/guide-routing-table.md` | Navigation |

---

## Assessment Skills (cross-agent, read-only)

`/assess-agent`, `/assess-skill`, `/assess-prompt` are read-only audit skills. They consume guide extracts and KB findings but never write to the KB.

| Op | Path | What |
|----|------|------|
| R | `extracts/guides/*.md` | Contract-derived criteria |
| R | `research-findings/*.md` | Tier-2 finding evidence |

---

## Drift Detection Skills (read-only)

`/detect-drift` reads artifact `extraction_date` vs finding `last_updated` and emits a drift report. Never modifies artifacts.

| Op | Path | What |
|----|------|------|
| R | `extracts/{form}/*.md` | Artifact metadata |
| R | `research-findings/*.md` | Finding timestamps |

---

## Generation Notes

| Field | Value |
|---|---|
| **Source of truth** | Per-skill `SKILL.md` files + agent `agent.md` definitions + `handoff-protocol.md` |
| **Complements** | [`ownership-map.md`](../2026-05-24/ownership-map.md) (directory-level) · [`agent-interaction-model.md`](../2026-05-24/agent-interaction-model.md) (pipeline flow) |
| **Regen cadence** | On skill roster change, new artifact directory, or agent boundary amendment |
