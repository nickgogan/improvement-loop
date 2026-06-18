---
title: "IL Agent Handoff Protocol"
type: "extracted-artifact"
assigned_form: "template"
source_finding: null
confidence: "HIGH"
tier: "auto"
reason_codes: ["inter-agent-contract", "pipeline-mediation"]
co_occurrence: null
extraction_date: "2026-04-19"
updated: "2026-05-24"
identification_report: null
deployed: false
deployed_to: null
contract:
  preconditions: "All three pipeline-participating agents (Researcher, Codifier, Librarian) are defined. Owner is the fourth IL agent, out of scope for this protocol. Pipeline stages 1-4 are operational. pipeline_status and consumed_by fields exist on all findings."
  invariants: "Handoffs are file-mediated, never direct. Nick triggers every stage transition. pipeline_status transitions are unidirectional (raw → classified → extracted, or raw → synthesized). No agent modifies another agent's output files beyond metadata fields."
  governance: "Owner: Improvement Loop system. Protocol changes require DD-level review if they affect stage boundaries or human gates."
  recovery: "If pipeline_status is inconsistent: run audit query (grep for status values), reconcile against identification reports and guide reports."
tags:
  - "extracted-artifact"
  - "template"
  - "improvement-loop"
  - "handoff-protocol"
---

# IL Agent Handoff Protocol

How findings flow from Researcher to Codifier, what triggers Codifier work, and how the Librarian consumes the output. This document defines the inter-agent contracts for the three pipeline-participating IL agents (Researcher, Codifier, Librarian). The Owner agent is out of scope for this protocol — see `owner/agent.md` for stewardship contracts.

---

## Core Principle: File-Mediated Handoffs

IL agents never communicate directly. All handoffs are mediated by the filesystem:

```
Researcher                    Codifier                     Librarian
    |                             |                            |
    |--- writes findings -------->|                            |
    |    (pipeline_status: raw)   |                            |
    |                             |                            |
    |         [NICK TRIGGERS]     |                            |
    |                             |                            |
    |                     reads findings                       |
    |                     writes identification report         |
    |                             |                            |
    |              [NICK APPROVES/REJECTS]                     |
    |                             |                            |
    |                     reads approved report                |
    |                     writes staged artifacts              |
    |                     updates pipeline_status              |
    |                             |                            |
    |                      [NICK DEPLOYS]                      |
    |                             |                            |
    |                             |-------- reads KB --------->|
    |                             |    (findings + guides +    |
    |                             |     deployed artifacts)    |
```

Every arrow labeled `[NICK]` is a human gate (DD-29). No agent autonomously triggers another agent's work.

---

## Pipeline Status Transitions

The `pipeline_status` field on findings is the primary interface contract between Researcher and Codifier:

| Status | Set By | Meaning | Next Valid Transition |
|--------|--------|---------|----------------------|
| `raw` | Researcher | Finding created, not yet classified or consumed | `classified` (via `/identify-artifacts`) or `synthesized` (via `/synthesize-guide`) |
| `classified` | Codifier (`/identify-artifacts`) | Finding classified into a form (pattern / skill / rule / template / agent); awaits Gate 2 approval before extraction | `extracted` (via `/extract-artifacts` after Gate 2 approval) |
| `synthesized` | Codifier (`/synthesize-guide`) | Finding consumed by guide synthesis | Terminal (finding content lives in guide) |
| `extracted` | Codifier (`/extract-artifacts`) | Finding consumed by artifact extraction | Terminal (finding content lives in artifact) |

**Transition rules:**
- Transitions are unidirectional — a finding cannot go back to `raw` or to `classified`
- Only the Codifier sets `classified`, `synthesized`, or `extracted`
- The Researcher only ever sets `raw`
- When a finding is consumed (synthesized or extracted), the Codifier also sets the `consumed_by` field to the guide or artifact path
- **Precedence on dual consumption:** if a finding is already `synthesized` and `/extract-artifacts` is later run on it, the Codifier keeps `synthesized` and appends the artifact path to `consumed_by` rather than transitioning to `extracted` (per `extract-artifacts/SKILL.md:648`)

---

## Trigger Conditions

### What triggers Researcher work?

| Trigger | Source | Typical Cadence |
|---------|--------|-----------------|
| Nick provides URLs to process | Conversational | Ad hoc |
| Watch-list check reveals new content | `/watch-upstream`, `/watch-blogs` | Weekly |
| Research dimension scan | `/research-loop`, `/perplexity-research` | Bi-weekly |
| KB maintenance needed | Linkage issues, dimension changes | As needed |

The Researcher is invoked by Nick. It does not self-trigger.

### What triggers Codifier work?

| Trigger | Condition | Skill Invoked |
|---------|-----------|---------------|
| Accumulated raw findings | 10+ findings with `pipeline_status: raw` at P1/P2 priority | `/identify-artifacts` |
| Approved identification report | Nick has set Status to APPROVED on report entries | `/extract-artifacts` |
| Guide staleness | Guide cluster finding count exceeds "Findings at Synthesis" by 3+ (per guide routing table) | `/synthesize-guide` |

Nick decides when these conditions are met. The Codifier does not monitor for them.

### What triggers Librarian work?

| Trigger | Source |
|---------|--------|
| Nick asks a question about KB content | Conversational — Teacher mode |
| Nick is designing something and wants KB input | Conversational — Builder mode |

The Librarian is purely reactive — it responds to questions, never proactively scans.

---

## Skill-to-Agent Mapping

### Researcher Skills

| Skill | Category | Boundary Rule |
|-------|----------|---------------|
| `/research-query` | Intake (on-demand) | Targeted research with gated persistence per DD-83; writes findings/sources only if user approves |
| `/research-loop` | Intake | Writes to findings/sources/authorities only |
| `/source-triage` | Intake | Produces verdicts, no KB writes |
| `/transcript-fetcher` | Intake | Mechanical fetch, no KB writes |
| `/watch-upstream` | Monitoring | Reads watched-libraries, produces triage report |
| `/watch-blogs` | Monitoring | Reads watched-blogs, produces triage report |
| `/perplexity-research` | Monitoring | Produces research reports in operations/ |
| `/repo-analyzer` | Monitoring | Produces analysis docs, candidates for /promote-findings |
| `/promote-findings` | KB Maintenance | Creates findings from analysis doc candidates |
| `/linkage-repair` | KB Maintenance | Fixes bidirectional links, no content changes |
| `/finding-crosslink` | KB Maintenance | Adds cross-links, no content changes |
| `/dimension-rebalance` | KB Maintenance | Reclassifies findings by dimension |

### Codifier Skills

| Skill | Category | Boundary Rule |
|-------|----------|---------------|
| `/identify-artifacts` | Classification | Reads findings, writes report to operations/; sets `pipeline_status: classified` on listed findings |
| `/extract-artifacts` | Extraction | Reads approved report + findings, writes to extracts/; sets `pipeline_status: extracted` (precedence rule applies if already `synthesized`) |
| `/synthesize-guide` | Synthesis | Reads findings + routing table, writes to extracts/guides/; sets `pipeline_status: synthesized` |
| `/reassess-priorities` | Re-evaluation | Reads findings, proposes priority changes based on accumulated evidence; produces report only — no `pipeline_status` writes |

### Librarian Skills

The Librarian uses Read/Glob/Grep tools directly. No dedicated skills currently.

### Boundary Conflict Points

Two skills touch both agents' domains and need explicit boundary rules:

1. **`/promote-findings` (Researcher)** creates new findings that the Codifier will later consume. The Researcher sets `pipeline_status: raw` and the finding enters the normal pipeline. The Codifier does NOT get notified — it discovers new findings on its next invocation.

2. **Finding metadata updates (Codifier)** — when `/identify-artifacts`, `/extract-artifacts`, or `/synthesize-guide` consume findings, they update `pipeline_status` and `consumed_by` on files in `research-findings/`. This is the ONLY case where the Codifier writes to a Researcher-owned directory, and it is restricted to metadata field updates — never content modifications.

---

## Librarian Consumption Model

The Librarian reads from three sources:

| Source | What It Contains | Freshness |
|--------|-----------------|-----------|
| `research-findings/` | Raw research — individual patterns with evidence | Updated by Researcher |
| `extracts/guides/` | Synthesized guides — aggregated pattern playbooks | Updated by Codifier |
| `knowledge/` | Deployed artifacts — production patterns, templates | Updated by Nick |

**Resolution order:** When the Librarian encounters information in multiple sources (e.g., a finding AND a guide covering the same topic), it prefers the most processed form:
1. Deployed artifact (most authoritative — Nick-approved)
2. Staged guide (synthesized — Codifier-processed)
3. Raw finding (least processed — Researcher-created)

This ensures the Librarian presents the most refined version of the knowledge, while still being able to cite the underlying evidence.

---

## Anti-Patterns

### 1. Researcher classifying its own findings
If the Researcher starts making form decisions ("this finding should be a rule"), it has crossed into Codifier territory. The Researcher sets `priority` and `evidence_strength` — not form assignments.

### 2. Codifier doing intake
If the Codifier discovers new patterns while synthesizing guides, it does NOT create findings. It notes the gap in the guide report and surfaces it to Nick, who may direct the Researcher to investigate.

### 3. Librarian fixing gaps
If the Librarian discovers a broken link or stale guide while answering a question, it reports the issue — it does NOT run `/linkage-repair` or modify any files. Gap reports flow to Nick → Researcher or Codifier.

### 4. Direct agent-to-agent triggers
No agent should invoke another agent's skills. Nick is the orchestrator for all stage transitions. This prevents cascading autonomous actions across pipeline stages.
