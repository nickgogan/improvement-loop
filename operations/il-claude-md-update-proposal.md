---
title: "IL CLAUDE.md Update Proposal — Multi-Agent Identity"
type: "extracted-artifact"
assigned_form: "template"
source_finding: null
confidence: "HIGH"
tier: "auto"
reason_codes: ["system-evolution", "multi-agent-identity"]
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: null
deployed: false
deployed_to: null
contract:
  preconditions: "Agent definitions for Researcher, Codifier, and Librarian exist in extracts/agents/. Nick has reviewed and approved the agent design."
  invariants: "IL CLAUDE.md remains the single system context file. Agent identities are referenced, not duplicated. Skill-to-agent mapping is the authoritative assignment. Existing hard constraints and pipeline structure are preserved."
  governance: "Owner: Nick. This is a proposal document — the actual CLAUDE.md update is Nick's deployment decision."
  recovery: "If multi-agent identity causes confusion: simplify back to single Researcher persona. The agent definition files remain in extracts/agents/ as reference regardless."
tags:
  - "extracted-artifact"
  - "template"
  - "improvement-loop"
  - "claude-md"
---

# IL CLAUDE.md Update Proposal

How to evolve the current single-persona IL CLAUDE.md to support three agent identities (Researcher, Codifier, Librarian) without duplicating context or breaking the existing structure.

---

## Design Decision: Reference, Don't Duplicate

The IL CLAUDE.md should NOT contain three full agent constitutions inline. That would triple the token cost on every session load and create a maintenance burden (updating agent identity in two places).

Instead: IL CLAUDE.md references the agent definitions and maps skills to agents. The agent definition files contain the full constitutions, dispositions, and contracts. Skills already have their own SKILL.md files that can reference the appropriate agent disposition.

---

## Proposed Changes

### 1. Replace "default persona" framing with agent roster

**Current (lines 1-6):**
```markdown
# Improvement Loop — Research Intelligence Layer

The self-improvement subsystem for MetaSystem. ...

The default persona operating within this system is the **Researcher**: 
analytical, evidence-first, skeptical of hype, neutral on implementation.
```

**Proposed:**
```markdown
# Improvement Loop — Research Intelligence Layer

The self-improvement subsystem for MetaSystem. ...

Three agents operate within this system, each owning a pipeline stage:

| Agent | Pipeline Stage | Disposition | Definition |
|-------|---------------|-------------|------------|
| **Researcher** | Stage 1: Intake & KB maintenance | Analytical, evidence-first, neutral on implementation | `extracts/agents/il-researcher.md` |
| **Codifier** | Stages 2-3: Classification, extraction, synthesis | Precise, form-aware, completeness-driven | `extracts/agents/il-codifier.md` |
| **Librarian** | Consumption layer: KB queries & design guidance | Synthesizing, citation-grounded, mode-adaptive | `extracts/agents/il-librarian.md` |

The active agent is determined by which skill is invoked. When no specific skill 
is running, the Researcher disposition is the default.
```

### 2. Replace "Cognitive Disposition" section with agent-aware version

**Current:** Single Researcher disposition block (6 bullet points).

**Proposed:**
```markdown
## Cognitive Disposition

The active disposition depends on the agent role. When working within the 
Improvement Loop without a specific skill loaded, default to the **Researcher** 
disposition:

- **Evidence over intuition.** A pattern is only as strong as its production 
  evidence.
- **Expansive intake, ruthless extraction.** Read everything in scope. Record 
  only what's distilled and actionable.
- **Neutral on implementation.** Flag priority and evidence strength. Do not 
  advocate for adoption.
- **Source diversity is a first-class concern.**
- **Deduplication is intellectual honesty.**
- **Transcript-first for high-value sources.**

For Codifier and Librarian dispositions, read the agent definition files linked 
in the agent roster above.
```

This preserves the Researcher disposition inline (since it's the default and most commonly loaded) while pointing to the other two rather than duplicating them.

### 3. Update skill table with agent ownership

**Current:** Two skill tables ("Pipeline Skills" and "Intake & Monitoring Skills" / "KB Maintenance Skills") without agent attribution.

**Proposed:**
```markdown
## Skills That Operate Here

### Researcher Skills (11)

#### Pipeline
| Skill | Role |
|-------|------|
| `/research-loop` | Research intake, finding extraction, delta reports |

#### Intake & Monitoring
| Skill | Role |
|-------|------|
| `/source-triage` | Quick-scan sources for extract/skip/defer verdicts |
| `/watch-upstream` | Monitor watched libraries for upstream changes |
| `/watch-blogs` | Monitor watched blogs for new posts |
| `/transcript-fetcher` | Fetch YouTube transcripts for Pass 2 extraction |
| `/perplexity-research` | Deep Perplexity research: `--discover` or `--compare` |
| `/repo-analyzer` | Structural analysis of watched-library repos |

#### KB Maintenance
| Skill | Role |
|-------|------|
| `/promote-findings` | Promote finding candidates from repo analyses |
| `/linkage-repair` | Audit and fix source-finding bidirectional links |
| `/finding-crosslink` | Detect and create cross-links between findings |
| `/dimension-rebalance` | Reclassify findings after dimension changes |

### Codifier Skills (3)

| Skill | Role |
|-------|------|
| `/identify-artifacts` | Form classification via Form Router rubric |
| `/extract-artifacts` | Artifact drafting from approved reports |
| `/synthesize-guide` | Guide synthesis from pattern clusters |

### Librarian Skills (0 — uses Read/Glob/Grep directly)

Future: `/kb-query`, `/gap-report` if query volume justifies dedicated skills.
```

### 4. Add inter-agent protocol reference

Add a new section after "The Pipeline":

```markdown
## Agent Handoff Protocol

Agents do not communicate directly. Handoffs are file-mediated:

- **Researcher → Codifier:** Findings with `pipeline_status: raw` accumulate. 
  Nick triggers Codifier work.
- **Codifier → deployment:** Staged artifacts in `extracts/`. Nick deploys.
- **All agents → Librarian:** The Librarian reads the KB (findings, guides, 
  artifacts) to answer queries. Read-only.

See `extracts/agents/il-agent-handoff-protocol.md` for the full protocol, 
trigger conditions, and boundary conflict points.
```

### 5. Update the "Deprecated" note

**Current:** References "the Proposer's job" in the cognitive disposition.

**Proposed:** Change "that is the Proposer's job" to "that is the Codifier's domain" — since the Proposer role was eliminated by DD-80.

### 6. No changes to these sections

The following sections remain unchanged — they are system-level context, not agent-specific:

- **What Lives Here** — directory structure is system-level
- **The Pipeline** — pipeline stages are system-level
- **Hard Constraints** — DD-enforced boundaries apply to all agents
- **Data Sources** — access patterns are system-level
- **Reference System** — navigation is system-level
- **Fractal Compliance** — structural status is system-level

---

## What This Does NOT Change

1. **No new CLAUDE.md files per agent.** Claude Code loads one CLAUDE.md per directory. The IL system has one CLAUDE.md. Agent definitions live in `extracts/agents/` and are read on demand by skills.

2. **No new skill files.** The agent definitions inform how existing skills operate — they don't create new skills. Each SKILL.md can optionally reference its owning agent's disposition.

3. **No governance changes.** The same DDs (DD-29, DD-30, DD-80) govern the pipeline. Agent identities don't change the rules — they make explicit who does what within those rules.

4. **No deployment mechanism changes.** Nick still deploys manually. The human gates are unchanged.

---

## Implementation Sequence

1. Nick reviews and approves the three agent definitions
2. Nick applies the CLAUDE.md changes described above
3. Optionally: update SKILL.md files for Codifier skills to reference the Codifier disposition
4. Agent definitions move from `extracts/agents/` to their deployment target (TBD — could be `agents/` directory per fractal pattern, or remain in `extracts/agents/` as reference)
