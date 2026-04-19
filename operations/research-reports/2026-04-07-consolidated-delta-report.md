# Consolidated Delta Report — 2026-04-07

All four sessions from 2026-04-07 consolidated into a single report.

---

## Scan Summary

| Metric | Session 1 (Eric Tech) | Session 2 (PC Calibration) | Session 3 (Transcript Re-Extraction) | Session 4 (Backfill) | **Total** |
|--------|----------------------|---------------------------|--------------------------------------|---------------------|-----------|
| **Sources reviewed** | 2 | 3 | 16 (re-extraction) | — | **16 unique + 5 re-processed** |
| **Dimensions covered** | Context Eng, Orchestration, Tool Integration | Memory Arch, Context Eng, Orchestration, Tool Integration, Prompt Craft, Intent Eng | All dimensions | — | **All 6 dimensions** |
| **New findings added** | 8 | 18 | 15 (backfill from calibration) | — | **41** |
| **Existing findings updated** | 0 | 0 | 9 (vague strengthened) | — | **9** |
| **New authorities added** | 2 | 5 | 0 | — | **5 unique** |

KB state at end of day: **~140 findings** in `_index.md`.

---

## Sources Processed

### Session 1 — Eric Tech Zip (2 videos)

| Source | Channel | Tags |
|--------|---------|------|
| These 3 Frameworks Make Claude Code Unstoppable | Eric Tech | `claude-code`, `orchestration`, `context-engineering`, `multi-agent` |
| Claude Code Works Better When You Do This | Eric Tech | `context-engineering`, `claude-code`, `tools`, `multi-agent`, `mcp` |

### Session 2 — Perplexity Computer Calibration (3 videos, deeper extraction)

| Source | Channel | Tags |
|--------|---------|------|
| Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases | Cole Medin | `memory`, `context-engineering`, `claude-code`, `vault-architecture` |
| I Broke Down Anthropic's $2.5 Billion Leak. Your Agent Is Missing 12 Critical Pieces. | Nate B Jones | `orchestration`, `tools`, `context-engineering`, `memory`, `claude-code` |
| The Official BMad-Method Masterclass | BMad Code | `orchestration`, `context-engineering`, `prompt-engineering`, `multi-agent` |

### Session 3 — Full Transcript Re-Extraction (all 16 videos)

| # | Video | Channel | Miss Rate |
|---|-------|---------|-----------|
| 1 | Your Claude Limit Burns In 90 Minutes | Nate B Jones | 66.7% |
| 2 | Claude Code's Leak Changes Everything | Agentic Lab | 53.3% |
| 3 | 12 Critical Pieces | Nate B Jones | 27.8% |
| 4 | Stop Using Claude Code in Terminal | Simon Scrapes | 85.7% |
| 5 | Karpathy's Obsidian RAG + Claude Code | Chase AI | 38.5% |
| 6 | These 3 Frameworks Make Claude Code Unstoppable | Eric Tech | 5.6% |
| 7 | Claude Code + RAG-Anything = LIMITLESS | Chase AI | 44.4% |
| 8 | Claude Code Works Better When You Do This | Eric Tech | 12.5% |
| 9 | Claude Code + SUPERPOWERS Tutorial | Eric Tech | 42.1% |
| 10 | BMad V6 is Finally Here | BMad Code | 60.0% |
| 11 | Anthropic Just Dropped Ultra Plan | Ray Amjad | 47.1% |
| 12 | OpenClaw SOUL.md Explained | Flowgrammers | 41.2% |
| 13 | Agent Produces at 100x, Org Reviews at 3x | Nate B Jones | 68.8% |
| 14 | Building Agents on Layers That Won't Exist | Nate B Jones | 72.2% |
| 15 | Self-Evolving Claude Code Memory | Cole Medin | 29.4% |
| 16 | BMad-Method Masterclass | BMad Code | 43.5% |

---

## New Findings (All Sessions Combined)

### Session 1 — Eric Tech (8 findings)

| Finding | Category | Evidence | Priority |
|---------|----------|----------|----------|
| Superpowers Framework — TDD + Mega Orchestrator | Orchestration | Medium | P2 |
| GSD Context Window Management — Sub-50% Rule | Context Engineering | Medium | P1 |
| gstack Specialist Role Architecture + 5-Layer Governance | Orchestration | Medium | P2 |
| Multi-Framework Orchestration Power Stack | Orchestration | Weak | P3 |
| Agent Teams — Shared Communication Channel | Orchestration | Medium | P2 |
| Context7 — On-Demand Version-Specific Doc Grounding | Tool Integration | Medium | P1 |
| NotebookLM as External Knowledge Base | Context Engineering | Medium | P2 |
| CLI + Skills vs MCP — Token Efficiency | Tool Integration | Medium | P1 |

### Session 2 — PC Calibration (18 findings)

| Finding | Category | Evidence | Priority |
|---------|----------|----------|----------|
| LLM Knowledge Base Compiler Pattern (Karpathy) | Memory Architecture | Medium | P2 |
| Claude Code Hooks for Automatic Session Memory | Memory Architecture | Medium | P1 |
| Index-File Navigation as RAG Replacement | Context Engineering | Medium | P2 |
| Compounding Knowledge Loop (Internal Data) | Memory Architecture | Medium | P1 |
| Tool Registry with Metadata-First Design | Tool Integration | Strong | P1 |
| Tiered Permission System with Destructive-Command Safety | Tool Integration | Strong | P1 |
| Session Persistence as Recoverable State | Orchestration | Strong | P1 |
| Workflow State vs. Conversation State Separation | Orchestration | Strong | P1 |
| Token Budget Tracking with Pre-Turn Projection Checks | Orchestration | Strong | P2 |
| Structured Streaming Events for System Observability | Orchestration | Strong | P2 |
| System Event Logging (Actions, Not Just Words) | Evaluation | Strong | P1 |
| Agent Type System (Six Built-In Roles) | Orchestration | Strong | P2 |
| Dynamic Tool Pool Assembly + Transcript Compaction | Context Engineering | Strong | P2 |
| Structured Multi-Agent Role Separation (BMad) | Orchestration | Medium | P2 |
| Document Sharding for Context Efficiency | Context Engineering | Medium | P1 |
| Advanced Elicitation Techniques (18-Technique Library) | Prompt Craft | Medium | P2 |
| New-Chat-Per-Agent-Step as Context Hygiene Discipline | Context Engineering | Medium | P2 |
| Business Analyst as Upstream Quality Gate | Intent Engineering | Medium | P3 |

### Session 3 — Transcript Calibration Backfill (15 new findings)

| Finding | Category | Evidence | Priority |
|---------|----------|----------|----------|
| Prompt Caching for Stable Agent Context | Context Engineering | Strong | P1 |
| Verification Agent: Seven Prompt Patterns | Evaluation | Strong | P1 |
| File Read Deduplication (18% / 2.6% Fleet Savings) | Context Engineering | Strong | P2 |
| Fix Data and Schema Before Automating | Intent Engineering | Strong | P2 |
| Negative Constraints as Probabilistic Output Collapse | Prompt Craft | Medium | P2 |
| Goal-First Agent Management Abstraction | Orchestration | Medium | P3 |
| Skill vs. Process Distinction (Deterministic Rails) | Orchestration | Strong | P2 |
| One-Shot PRD Prompt for System Bootstrap | Context Engineering | Strong | P2 |
| YAML Template Dual Structure (Schema + Coaching) | Prompt Craft | Strong | P2 |
| Tech Stack Pinning Table for Drift Prevention | Context Engineering | Strong | P1 |
| Pre-Compression Identity Pinning | Context Engineering | Medium | P2 |
| Extract Deep Plan Prompt as Custom Skill | Prompt Craft | Strong | P1 |
| llms-full.txt: AI-Optimized Documentation Endpoint | Context Engineering | Medium | P3 |
| BMAD Module Marketplace with Vetting | Orchestration | Medium | P3 |
| Six-Layer Agent Infrastructure Stack | Orchestration | Medium | P2 |

---

## Updated Findings

| Finding | What Was Updated |
|---------|-----------------|
| Token Waste Taxonomy | Added cost breakdowns, fresh-every-10-15-turns cadence from transcripts |
| Claude Code Hooks | Added post-session git push use case, daily flush mechanics |
| Karpathy LLM KB | Added two-tier index system, wiki folder conventions, linting stage |
| BMAD Method v6 | Added party mode detail, scope expansion beyond SDLC, marketplace |
| Superpowers Plugin | Added two execution modes, HTML mockup generation, plan 3-level hierarchy |
| Claude Code Ultra Plan | Added 2x benchmark, dual execution path, A/B testing infrastructure |
| SOUL.md Agent Constitution | Added four-section anatomy names, boot sequence mechanics |
| gstack/Power Stack | Added role analogies, milestone calculation detail |
| IDE-First Claude Code with Deterministic Hooks | Flagged misattribution — Video 4 content does not match linked finding |

---

## Calibration Results (Summary)

| Metric | Value |
|--------|-------|
| Transcripts processed | 16 |
| Total distinct patterns identified | 282 |
| Correct (in KB, accurately captured) | 94 (33.3%) |
| Vague (in KB, missing specifics) | 57 (20.2%) |
| Missed (not in KB at all) | 131 (46.5%) |
| **Effective miss rate** | **46.5%** |
| **Quality gap rate (Missed + Vague)** | **66.7%** |
| Pattern density: summary-based | 2.1 per video |
| Pattern density: transcript-based | 17.6 per video (8.4x increase) |

**Key finding:** Transcript-first extraction is mandatory for high-value sources. Summary-based extraction should be reserved for initial triage only. Implementation details (31% of misses) are the highest-value miss category.

**Perplexity Computer vs. Transcript comparison:** PC found 18 gaps across 3 calibration videos; transcript re-extraction found 35 gaps from the same 3 videos. PC excels at architectural decomposition; transcripts excel at implementation details and tool discovery. Neither alone is sufficient.

---

## Recommendations

### Priority 1 — Immediate

1. **Transcript-first extraction is now mandatory** for any source worth more than a triage pass. Build this into the `/research-loop` skill pipeline.
2. **Run `/research-proposer`** on the current KB. There are 41 new findings (many P1) that have never been through proposal generation.
3. **Source linkage audit:** Video 4 misattribution confirmed. Audit other single-finding-per-video linkages for similar issues.

### Priority 2 — Design Required

4. **Two-pass extraction process:** First pass = summary triage (1-3 findings). Second pass = transcript extraction (10-20 additional patterns). Codify this as the standard operating procedure.
5. **Backfill the 57 vague findings** with transcript-derived specifics (configs, numbers, file paths). These are directionally correct but not yet actionable.
6. **Optimal pipeline design:** PC for architectural decomposition + transcript for implementation details + human review for priority triage.

### Priority 3 — Monitor

7. **131 missed patterns** remain as backfill candidates. Tier 1 (15 high-value) should be created; Tier 2 (9 vague updates) should strengthen existing entries; Tier 3 can be deferred.

---

## Evaluation Handoff

**Prompts to evaluate (via `/prompt-evaluator`):**
- S3 Claude Code system prompt — against F-005 (tool registry), F-006 (permission tiers), F-008 (workflow state), F-011 (action logging)
- S2 Notion Operations agent prompt — against F-007 (session persistence), F-008 (workflow state)
- Perplexity Skills (research-loop, research-proposer) — against F-015 (sharding), F-016 (elicitation techniques)

**Pipeline next step:** `/research-proposer` on the full P1/P2 findings set.

---

## Next Scan Notes

See `operations/next-scan-notes.md` for carry-forward items.
