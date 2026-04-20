---
title: "Finding-to-Artifact Workflow"
type: "workflow"
target_system:
  - "improvement-loop"
agent: "codifier"
created: "2026-04-19"
updated: "2026-04-19"
tags:
  - "workflow"
  - "codifier"
  - "pipeline"
  - "extraction"
---

# Finding-to-Artifact

The Codifier's end-to-end pipeline: classify research findings into forms, draft artifacts, and stage for deployment. Covers Stages 2-3 of the IL pipeline.

## Trigger

- P1/P2 findings have accumulated in the KB (pipeline_status: raw)
- Nick requests artifact identification or extraction
- A guide cluster has new findings since last synthesis

## Flow

```
[1] /identify-artifacts
         │
         Read P1/P2 findings
         Apply Form Router rubric
         Classify each: pattern / skill / rule / template / agent
         │
         Produces: identification report in
         operations/pattern-identification-reports/
         │
    ─── HUMAN GATE: Nick reviews identification report ───
         │
         Nick approves/rejects per finding
         │
[2] /extract-artifacts
         │
         Read approved identification report
         Draft form-appropriate artifacts
         Apply ContractSpec (DD-78) to each
         │
         Produces: staged artifacts in extracts/{form}/
         Updates: pipeline_status on processed findings
         │
    ─── HUMAN GATE: Nick reviews staged artifacts ───
         │
         ├─ Pattern-classified findings with 3+ in a cluster?
         │        │
         │   [3] /synthesize-guide
         │        │
         │        Read finding cluster + guide routing table
         │        Draft end-directed guide
         │        │
         │        Produces: staged guide in extracts/guides/
         │        Updates: guide routing table
         │        │
         │   ─── HUMAN GATE: Nick reviews guide ───
         │
         └─ No guide synthesis needed
                  │
         [4] Deployment (Nick's manual action)
              │
              Move approved artifacts from extracts/
              to meta-system/knowledge/ or .claude/
```

## Decision Points

| Point | Question | Answer |
|-------|----------|--------|
| Step 1 | Which findings to classify? | Filter by: `priority` P1/P2, `pipeline_status: raw`. |
| Step 1 | Form ambiguous (co-occurrence)? | Classify conservatively (pattern > skill). Flag for Nick. |
| After Step 2 | Guide synthesis warranted? | Check guide routing table. If a cluster has 3+ new findings → yes. |
| Step 4 | Who deploys? | Nick only. Codifier stages; never deploys to enforcement locations. |

## Human Gates

- **After identification**: Nick approves/rejects form classifications per finding
- **After extraction**: Nick reviews staged artifacts for quality and accuracy
- **After guide synthesis**: Nick reviews guide for completeness and actionability
- **Deployment**: Nick moves artifacts to enforcement locations manually

## Pipeline Status Transitions

```
raw ──[identify]──→ raw (unchanged, just classified)
raw ──[extract]──→ extracted (consumed by an artifact)
raw ──[synthesize]──→ synthesized (consumed by a guide)
```

The Codifier manages these transitions. The Researcher never sets `extracted` or `synthesized`.
