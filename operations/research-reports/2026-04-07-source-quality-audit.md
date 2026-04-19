# Source Quality Audit — 2026-04-07

## Summary

Audited all 74 research sources against their linked findings to identify extraction gaps. Cross-referenced with the calibration report's per-video data for the 16 already-calibrated videos. Spot-checked 10 zero-finding sources (5 blog posts, 5 papers/docs) to estimate expected finding counts.

| Metric | Value |
|--------|-------|
| **Total sources** | 74 |
| **Sources with 1+ findings linked** | 42 (57%) |
| **Sources with 0 findings linked** | 32 (43%) |
| **Total findings in KB** | ~220 |
| **High-relevance sources with 0 findings** | 20 |
| **Estimated missed findings (spot-checked sources)** | 41-55 |

---

## Structural Issue: Broken Bidirectional Linkage

Before interpreting the gap data, a critical structural issue: **source-to-finding and finding-to-source links are inconsistently maintained.**

- Source files use `findings: []` arrays to link forward to findings
- Finding files use `sources: []` arrays to link back to sources
- Many findings have `sources: []` (empty) despite clearly originating from a specific source
- Example: `tool-shaped-object-evaluation-lens.md` clearly derives from "Tool Shaped Objects" (Substack) but has `sources: []`
- Example: ACE findings exist in the KB but the ACE source file has `findings: []`

**Impact:** The 32 "zero-finding" sources include some that DO have findings — they're just not linked. The actual zero-extraction count is lower, but the linkage gap itself is a data quality problem that should be fixed.

**Recommendation:** A linkage repair pass should precede or accompany any backfill work. Match findings to sources by content/title/URL correlation.

---

## Gap Analysis by Source Type

### Videos (35 sources)

**Calibrated videos (16):** These received transcript-based extraction in the prior session. Current linked findings range from 3-13, against calibration-identified totals of 8-25 patterns per video. The backfill session created 34 new findings but did not achieve full coverage.

| Video | Current Findings | Calibrated Total | Remaining Gap | Miss Rate |
|-------|-----------------|------------------|---------------|-----------|
| Anthropic's $2.5B Leak (12 Critical Pieces) | 13 | 18 | 5 | 27.8% |
| BMad-Method Masterclass | 12 | 23 | 11 | 43.5% |
| 10 CLI Tools | 9 | — | Unknown | — |
| How to Make Claude Code Less Dumb | 8 | — | Unknown | — |
| Claude Code's Leak Changes Everything | 8 | 15 | 7 | 53.3% |
| Building AI Agents (Full Course) | 8 | — | Unknown | — |
| BMad V6 is Finally Here | 6 | 25 | 19 | 60.0% |
| Agent Produces 100x, Org Reviews 3x | 6 | 16 | 10 | 68.8% |
| Stop Using Claude Code in Terminal | 5 | 14 | 9 | 85.7% |
| Self-Evolving Claude Code Memory | 5 | 17 | 12 | 29.4% |
| Your Claude Limit Burns in 90 Minutes | 4 | 21 | 17 | 66.7% |
| Karpathy's Obsidian RAG + Claude Code | 4 | 13 | 9 | 38.5% |
| Building Agents on Layers That Won't Exist | 4 | 18 | 14 | 72.2% |
| Claude Code Works Better When You Do This | 3 | 8 | 5 | 12.5% |
| OpenClaw SOUL.md Explained | 3 | 17 | 14 | 41.2% |
| Anthropic Just Dropped Ultra Plan | 3 | 17 | 14 | 47.1% |
| These 3 Frameworks | 2 | 18 | 16 | 5.6% |
| Claude Code + RAG-Anything | 3 | 18 | 15 | 44.4% |
| Claude Code + SUPERPOWERS Tutorial | 1 | 19 | 18 | 42.1% |

**Non-calibrated videos (19):** These have NOT been calibrated. Based on the calibration data (avg 17.6 patterns per video, 46.5% miss rate), most are significantly under-extracted.

| Video | Current Findings | Expected (heuristic) | Estimated Gap |
|-------|-----------------|---------------------|---------------|
| Your AI Coding is BAD | 6 | 10-18 | 4-12 |
| Your AI Agent Fails 97.5% | 6 | 10-18 | 4-12 |
| Notion Custom Agents | 6 | 10-18 | 4-12 |
| ChatGPT Health / Respiratory Failure | 6 | 10-18 | 4-12 |
| Andrej Karpathy's Math | 6 | 10-18 | 4-12 |
| Anthropic Didn't Build a Browser | 5 | 8-15 | 3-10 |
| Stop Building AI Agents (Folder System) | 5 | 10-18 | 5-13 |
| GSD 2 vs Claude Code | 5 | 10-18 | 5-13 |
| Nate B. Jones Videos (Feb-Mar) | 4 | 15-25 (compilation) | 11-21 |
| Most People Build Skills Wrong | 4 | 10-18 | 6-14 |
| Why Your Coding Agent Gets DUMBER | 3 | 10-18 | 7-15 |
| Claude Skills vs Projects | 3 | 8-15 | 5-12 |
| Claude Code Paperclip | 3 | 8-15 | 5-12 |
| Karpathy Autoresearch | 1 | 10-18 | 9-17 |
| AI Agents in Enterprise Webinar | 0 | 3-8 (Low relevance) | 3-8 |

### Blog Posts (21 zero-finding sources)

Spot-checked 5. Results:

| Source | Relevance | Estimated Findings | Spot-Check Confidence |
|--------|-----------|-------------------|----------------------|
| **MCP: Everything Your Team Needs (WorkOS)** | High | **8-12** | High |
| **Multi-Agent Orchestration Playbook (Gupta)** | High | **8-10** | High |
| **Agent Orchestrators Are Bad** | High | **4-5** | High |
| **Every Layer of Review Makes 10x Slower** | High | **3-4** | Medium |
| **Tool Shaped Objects** | High | **1-2** (1 exists, unlinked) | High |
| OpenClaude (Hindsight) | High | 3-5 (estimated) | Low |
| Intent Engineering Framework (Product Compass) | High | 2-4 (estimated) | Low |
| Prompting After Feb 2026 | High | 2-4 (estimated) | Low |
| How to Build Self-Improving AI Skills | High | 2-4 (estimated) | Low |
| HITL Agentic AI (Strata.io) | High | 2-3 (estimated) | Low |
| 4-Layer Memory Stack (Alok Mishra) | High | 2-3 (estimated) | Low |
| AI Agent Prompt Engineering (Inflectra) | High | 2-3 (estimated) | Low |
| AI Agents in Production (Gupta) | High | 2-3 (estimated) | Low |
| Every AI Prompting Technique (Product w/ Attitude) | High | 2-4 (estimated) | Low |
| LLM Benchmark 2026: 38 Tasks | High | 2-3 (estimated) | Low |
| Gemini vs GPT vs Claude Benchmark (Lorka) | High | 1-2 (estimated) | Low |
| Google A2A Protocol Guide | Medium | 2-3 (estimated) | Low |
| Cursor AI MCP Server Config | Medium | 1-2 (estimated) | Low |
| Human-on-the-Loop AI (Torry Harris) | Medium | 1-2 (estimated) | Low |
| ARC-AGI-3 All Score 0% | Medium | 1-2 (estimated) | Low |
| March 2026 AI Roundup | Medium | 1-2 (estimated) | Low |

### Research Papers (4 zero-finding sources)

Spot-checked all 4:

| Source | Estimated Findings | Confidence | Notes |
|--------|-------------------|------------|-------|
| **ACE (ICLR 2026)** | **2-3 new** (+ 2 existing unlinked) | High | Bullet metadata format, reflector loops, offline warmup |
| **ARTIST (arXiv)** | **4-5** (+ 1 existing unlinked) | High | Loss masking, composite rewards, difficulty-adaptive tools |
| **ETH Zurich Context Files** | **3-4** | Medium | LLM-generated files hurt performance, under-300-line rule |
| **HyperAgents** | **3-4** | Medium | Task/meta agent separation, metacognitive self-modification |

### Documentation (5 zero-finding sources)

| Source | Estimated Findings | Notes |
|--------|-------------------|-------|
| **Anthropic Prompt Evaluation Framework** | **5-6** | SMART criteria, three-tier grading, LLM-as-judge pattern |
| **DeepEval MCP Evaluation Quickstart** | 2-3 | MCP-native eval patterns |
| **Prompting Best Practices (Nick Gogan)** | 1-2 | Internal doc, may already be reflected in practices |
| **Intent Engineering (Pathmode Glossary)** | 1-2 | Terminology reference |
| **OpenAI Self-Evolving Agents Cookbook** | 2-3 | Self-improvement patterns |

### Tool Releases (1 zero-finding source)

| Source | Estimated Findings | Notes |
|--------|-------------------|-------|
| Introducing GPT-5.4 (OpenAI) | 1-2 | Tool search/deferred loading pattern (1 finding exists, unlinked) |

---

## Prioritized Backfill Recommendations

### Tier 1: Highest ROI — Deep Extract (article re-read or transcript Pass 2)

These are high-relevance sources with large estimated gaps. Each should yield 4+ new findings.

| Priority | Source | Type | Action | Est. New Findings |
|----------|--------|------|--------|-------------------|
| 1 | MCP: Everything Your Team Needs (WorkOS) | Blog | Article re-read | 8-12 |
| 2 | Multi-Agent Orchestration Playbook (Gupta) | Blog | Article re-read | 8-10 |
| 3 | Anthropic Prompt Evaluation Framework | Doc | Article re-read | 5-6 |
| 4 | Agent Orchestrators Are Bad | Blog | Article re-read | 4-5 |
| 5 | ARTIST (arXiv) | Paper | Paper re-read | 4-5 |
| 6 | Claude Code + SUPERPOWERS Tutorial | Video | Transcript Pass 2 | ~18 |
| 7 | Your Claude Limit Burns in 90 Minutes | Video | Transcript Pass 2 | ~17 |
| 8 | BMad V6 is Finally Here | Video | Transcript Pass 2 | ~19 |
| 9 | Building Agents on Layers That Won't Exist | Video | Transcript Pass 2 | ~14 |
| 10 | OpenClaw SOUL.md Explained | Video | Transcript Pass 2 | ~14 |

**Estimated Tier 1 yield: 111-120 new findings**

### Tier 2: Moderate ROI — Standard Extract

These should yield 2-4 new findings each.

| Source | Type | Action | Est. New Findings |
|--------|------|--------|-------------------|
| Every Layer of Review Makes 10x Slower | Blog | Article re-read | 3-4 |
| ETH Zurich Context Files | Paper | Paper re-read | 3-4 |
| ACE (ICLR 2026) | Paper | Paper re-read + link existing | 2-3 new |
| HyperAgents | Paper | Paper re-read | 3-4 |
| Intent Engineering Framework (Product Compass) | Blog | Article re-read | 2-4 |
| How to Build Self-Improving AI Skills | Blog | Article re-read | 2-4 |
| OpenClaude (Hindsight) | Blog | Article re-read | 3-5 |
| Agent Produces 100x, Org Reviews 3x | Video | Transcript Pass 2 | ~10 |
| Self-Evolving Claude Code Memory | Video | Transcript Pass 2 | ~12 |
| Karpathy Autoresearch | Video | Transcript Pass 2 | 9-17 |

**Estimated Tier 2 yield: 49-67 new findings**

### Tier 3: Low ROI — Quick Triage

These are either low-relevance, duplicative of other sources, or thin content. Skim only.

- ARC-AGI-3 All Score 0% (benchmark result, not pattern)
- March 2026 AI Roundup (aggregator, patterns likely covered by primary sources)
- AI Agents in Enterprise Webinar (Low relevance)
- Google A2A Protocol Guide (informational, limited actionable patterns)
- Cursor MCP Config (tool-specific setup, narrow applicability)
- Human-on-the-Loop (Torry Harris) (conceptual, limited implementation detail)

### Tier 0: Linkage Repair (no extraction needed)

These sources have existing findings that aren't linked:

| Source | Existing Unlinked Findings |
|--------|---------------------------|
| Tool Shaped Objects | `tool-shaped-object-evaluation-lens.md` |
| ACE (ICLR 2026) | 2 ACE findings in _index.md |
| ARTIST | `rl-trained-autonomous-tool-selection.md` (verify name) |
| GPT-5.4 | `gpt-54-tool-search-deferred-tool-loading.md` |

---

## Aggregate Gap Estimate

| Category | Sources | Est. Missing Findings |
|----------|---------|----------------------|
| Calibrated videos (remaining gaps) | 16 | ~175 (from calibration: 282 total - 94 correct - ~13 backfilled) |
| Non-calibrated videos | 19 | ~95-190 (5-10 per video, heuristic) |
| Zero-finding blog posts (High relevance) | 14 | ~45-65 |
| Zero-finding blog posts (Medium relevance) | 7 | ~7-14 |
| Research papers | 4 | ~12-16 |
| Documentation | 5 | ~11-16 |
| Tool releases | 1 | ~1-2 |
| **Total estimated extraction gap** | **66** | **~345-478** |

The KB currently has ~220 findings. Full extraction could roughly triple it. However, not all gaps are equal — Tier 1 sources contain the highest-density, most actionable patterns.

---

## Process Recommendations

1. **Fix linkage before backfill.** Run a linkage repair pass matching existing findings to their sources. This will clarify the true gap before investing in extraction.

2. **Prioritize blog posts over remaining video gaps.** Blog posts are cheaper to re-read (no transcript fetching needed) and the spot-checked articles (MCP WorkOS, Orchestration Playbook) are extremely dense. Better ROI per token spent.

3. **For videos, prioritize the 5 with largest calibrated gaps** (SUPERPOWERS, Claude Limit Burns, BMad V6, Layers Won't Exist, SOUL.md Explained). These have known, calibrated gaps — no estimation uncertainty.

4. **For non-calibrated videos, run calibration first** before committing to full extraction. The calibration step is much cheaper than full extraction and identifies whether a video is worth the investment.

5. **Research papers yield fewer but higher-rigor findings.** Prioritize ARTIST and ETH Zurich — both have concrete, implementable patterns with academic evidence backing.

---

## Appendix: Complete Source Inventory

| # | Source | Type | Relevance | Linked Findings | Gap Tier |
|---|--------|------|-----------|----------------|----------|
| 1 | Anthropic's $2.5B Leak (12 Critical Pieces) | Video | High | 13 | Calibrated |
| 2 | BMad-Method Masterclass | Video | High | 12 | Calibrated |
| 3 | 10 CLI Tools That Make Claude Code Unstoppable | Video | High | 9 | Not calibrated |
| 4 | How to Make Claude Code Less Dumb | Video | High | 8 | Not calibrated |
| 5 | Claude Code's Leak Changes Everything | Video | High | 8 | Calibrated |
| 6 | Building AI Agents That Actually Work | Video | High | 8 | Not calibrated |
| 7 | Your AI Coding is BAD | Video | High | 6 | Not calibrated |
| 8 | Your AI Agent Fails 97.5% | Video | High | 6 | Not calibrated |
| 9 | Notion Custom Agents | Video | High | 6 | Not calibrated |
| 10 | ChatGPT Health / Respiratory Failure | Video | High | 6 | Not calibrated |
| 11 | BMad V6 is Finally Here | Video | High | 6 | Calibrated |
| 12 | Andrej Karpathy's Math | Video | High | 6 | Not calibrated |
| 13 | Agent Produces 100x, Org Reviews 3x | Video | High | 6 | Calibrated |
| 14 | Anthropic Didn't Build a Browser | Video | Medium | 5 | Not calibrated |
| 15 | Stop Using Claude Code in Terminal | Video | High | 5 | Calibrated |
| 16 | Stop Building AI Agents (Folder System) | Video | High | 5 | Not calibrated |
| 17 | Self-Evolving Claude Code Memory | Video | High | 5 | Calibrated |
| 18 | GSD 2 vs Claude Code | Video | High | 5 | Not calibrated |
| 19 | Your Claude Limit Burns in 90 Minutes | Video | High | 4 | Calibrated |
| 20 | Nate B. Jones Videos (Feb-Mar) | Video | High | 4 | Not calibrated |
| 21 | Most People Build Claude Skills Wrong | Video | High | 4 | Not calibrated |
| 22 | Karpathy's Obsidian RAG + Claude Code | Video | High | 4 | Calibrated |
| 23 | Building Agents on Layers That Won't Exist | Video | High | 4 | Calibrated |
| 24 | Why Your Coding Agent Gets DUMBER | Video | High | 3 | Not calibrated |
| 25 | OpenClaw SOUL.md Explained | Video | High | 3 | Calibrated |
| 26 | Claude Code Works Better | Video | High | 3 | Calibrated |
| 27 | Anthropic Just Dropped Ultra Plan | Video | High | 3 | Calibrated |
| 28 | Claude Skills vs Projects | Video | Medium | 3 | Not calibrated |
| 29 | Claude Code + RAG-Anything | Video | Medium | 3 | Calibrated |
| 30 | Claude Code Paperclip | Video | Medium | 3 | Not calibrated |
| 31 | TACHES Claude Code Resources | Tool Release | High | 3 | Not calibrated |
| 32 | These 3 Frameworks | Video | Medium | 2 | Calibrated |
| 33 | GWS CLI | Tool Release | High | 2 | N/A |
| 34 | March 18 Agent Memory Architecture Research | Documentation | High | 2 | N/A |
| 35 | Four-System Separation Session Research | Documentation | High | 2 | N/A |
| 36 | Karpathy Autoresearch | Video | High | 1 | Not calibrated |
| 37 | Claude Code + SUPERPOWERS Tutorial | Video | High | 1 | Calibrated |
| 38 | OpenSpec (YCombinator) | Tool Release | Medium | 1 | N/A |
| 39 | Obra/Superpowers Framework | Tool Release | High | 1 | N/A |
| 40 | NotebookLM-py | Tool Release | High | 1 | N/A |
| 41 | Anthropic PSM Research / Context Eng Guide | Documentation | High | 1 | N/A |
| 42 | MCP: Everything Your Team Needs (WorkOS) | Blog | High | 0 | **Tier 1** |
| 43 | Multi-Agent Orchestration Playbook (Gupta) | Blog | High | 0 | **Tier 1** |
| 44 | Anthropic Prompt Evaluation Framework | Documentation | High | 0 | **Tier 1** |
| 45 | Agent Orchestrators Are Bad | Blog | High | 0 | **Tier 1** |
| 46 | ARTIST (arXiv) | Research Paper | High | 0 | **Tier 1** |
| 47 | ACE (ICLR 2026) | Research Paper | High | 0 | **Tier 2** (has unlinked findings) |
| 48 | Every Layer of Review Makes 10x Slower | Blog | High | 0 | **Tier 2** |
| 49 | ETH Zurich Context Files Paper | Research Paper | Medium | 0 | **Tier 2** |
| 50 | OpenClaude (Hindsight) | Blog | High | 0 | **Tier 2** |
| 51 | Intent Engineering Framework (Product Compass) | Blog | High | 0 | **Tier 2** |
| 52 | How to Build Self-Improving AI Skills | Blog | High | 0 | **Tier 2** |
| 53 | Every AI Prompting Technique | Blog | High | 0 | **Tier 2** |
| 54 | Prompting After Feb 2026 | Blog | High | 0 | **Tier 2** |
| 55 | 4-Layer Memory Stack (Alok Mishra) | Blog | High | 0 | **Tier 2** |
| 56 | AI Agent Prompt Engineering (Inflectra) | Blog | High | 0 | **Tier 2** |
| 57 | AI Agents in Production (Gupta) | Blog | High | 0 | **Tier 2** |
| 58 | LLM Benchmark 2026: 38 Tasks | Blog | High | 0 | **Tier 2** |
| 59 | HITL Agentic AI (Strata.io) | Blog | High | 0 | **Tier 2** |
| 60 | Gemini vs GPT vs Claude Benchmark (Lorka) | Blog | High | 0 | **Tier 2** |
| 61 | DeepEval MCP Evaluation Quickstart | Documentation | High | 0 | **Tier 2** |
| 62 | HyperAgents (arXiv) | Research Paper | Medium | 0 | **Tier 3** |
| 63 | Tool Shaped Objects | Blog | High | 0 | **Tier 0** (linkage only) |
| 64 | Introducing GPT-5.4 (OpenAI) | Tool Release | High | 0 | **Tier 0** (linkage only) |
| 65 | Google A2A Protocol Guide | Blog | Medium | 0 | **Tier 3** |
| 66 | Cursor AI MCP Config | Blog | Medium | 0 | **Tier 3** |
| 67 | Human-on-the-Loop (Torry Harris) | Blog | Medium | 0 | **Tier 3** |
| 68 | ARC-AGI-3 All Score 0% | Blog | Medium | 0 | **Tier 3** |
| 69 | March 2026 AI Roundup | Blog | Medium | 0 | **Tier 3** |
| 70 | Prompting Best Practices (Nick Gogan) | Documentation | High | 0 | **Tier 3** (internal) |
| 71 | Intent Engineering (Pathmode Glossary) | Documentation | Medium | 0 | **Tier 3** |
| 72 | OpenAI Self-Evolving Agents Cookbook | Documentation | Medium | 0 | **Tier 3** |
| 73 | AI Agents in Enterprise Webinar | Video | Low | 0 | **Tier 3** |
