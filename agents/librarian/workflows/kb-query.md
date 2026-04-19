---
title: "KB Query Workflow"
type: "workflow"
target_system:
  - "improvement-loop"
agent: "librarian"
created: "2026-04-19"
updated: "2026-04-19"
tags:
  - "workflow"
  - "librarian"
  - "query"
  - "consumption"
---

# KB Query

The Librarian's query resolution workflow. Receive a question, determine mode (Teacher/Builder), search the KB, synthesize a grounded answer.

## Trigger

- User asks a knowledge question ("What do we know about X?")
- User asks for design guidance ("Help me design Y", "What patterns apply?")
- Another agent spawns the Librarian as a subagent for KB consultation

## Flow

```
[1] Parse query
         │
         Determine mode from query intent
         │
         ├─ "What/Explain/Summarize" ──→ Teacher mode
         │
         └─ "Help me/Design/Build/How should I" ──→ Builder mode
         │
[2] Navigate KB
         │
         Read guide routing table
         Grep findings by topic, category, tags
         Glob for relevant guides and artifacts
         │
         Resolution order:
         1. Deployed artifacts (meta-system/knowledge/)
         2. Staged guides (extracts/guides/)
         3. Raw findings (research-findings/)
         │
[3] Synthesize answer
         │
         ├─ Teacher: narrative with inline citations,
         │    evidence strength, gap flags
         │
         └─ Builder: ordered recommendation set —
              guides → patterns → templates → pitfalls
              Sequenced for consumption order
         │
[4] Assess coverage
         │
         ├─ Full coverage ──→ Deliver answer
         │
         ├─ Partial coverage ──→ Deliver answer +
         │    flag thin areas explicitly
         │
         └─ No coverage ──→ State: "the KB does not
              have findings on this topic"
              │
              Optionally: suggest /research-query
              to fill the gap
```

## Decision Points

| Point | Question | Answer |
|-------|----------|--------|
| Step 1 | Which mode? | Determined by query phrasing. Ambiguous → default to Teacher. |
| Step 2 | Multiple sources at different processing stages? | Prefer most-processed form (deployed > staged > raw). |
| Step 4 | KB gap found? | Report honestly. Never fill with training data. Suggest research if gap is significant. |

## Human Gates

None. The Librarian is read-only and produces conversational output. No structural changes, no file writes, no pipeline modifications.

## Gap Reporting

When the Librarian encounters a gap, it doesn't fix it — it reports:
- **Missing finding**: "The KB doesn't cover [topic]. Consider `/research-query` to investigate."
- **Stale finding**: "Finding [name] was last updated [date] — evidence may be outdated."
- **Contradictory findings**: "Finding A says X, finding B says Y. A has stronger evidence (production-tested vs. theoretical)."

These gap reports are input to Nick, who may direct the Researcher or Codifier to address them.
