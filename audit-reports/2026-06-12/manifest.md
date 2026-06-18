---
title: "IL audit manifest"
audit_target: "systems/improvement-loop/"
audit_date: "2026-06-12"
audit_version: "v1"
discovery_mode: "auto-detect"
bin_count: 9
artifact_count: 43
audit_session: "115"
---

# Discovered artifacts

## Skills (32)

| Path | Bin | Footprint | Dispatched to | Outcome |
|---|---|---|---|---|
| `.claude/skills/maintain-docs/SKILL.md` | 7 | 44.6k | /assess-skill | Persisted; G9.I6 Partial; 1M 10P 6S |
| `.claude/skills/source-triage/SKILL.md` | 6 | 45.0k | /assess-skill | Persisted; 3V 4M 5P 4S |
| `.claude/skills/finding-crosslink/SKILL.md` | 4 | 46.8k | /assess-skill | Visible-digest; **G9.I6 Satisfied** (strongest-governance skill) |
| `.claude/skills/research-query/SKILL.md` | 6 | 45.0k | /assess-skill | Persisted; 1V 3M 7P 5S |
| `.claude/skills/identify-artifacts/SKILL.md` | 2 | 49.4k | /assess-skill | Visible-digest; F#1 Violated (allowed-tools missing Edit) |
| `.claude/skills/promote-findings/SKILL.md` | 5 | 45.5k | /assess-skill | Persisted; **G9.I6 VIOLATED** (--auto bypasses HITL); 8V 8P 8S |
| `.claude/skills/solicit-proposals/SKILL.md` | 7 | 44.7k | /assess-skill | Persisted; G9.I6 Partial; 0V 1M 9P 7S |
| `.claude/skills/ask-kb/SKILL.md` | 6 | 45.4k | /assess-skill | Persisted; 0V 1M 5P 7S |
| `.claude/skills/linkage-repair/SKILL.md` | 8 | 44.6k | /assess-skill | Persisted; 0V 2M 5P 6S |
| `.claude/skills/transcript-fetcher/SKILL.md` | 9 | 43.7k | /assess-skill | Visible-digest; G9.I6 Partial; safety-critical undeclared |
| `.claude/skills/translate-governance/SKILL.md` | 7 | 44.7k | /assess-skill | Persisted; **G9.I6 VIOLATED** (act-then-report); 3V 4M 6P 4S |
| `.claude/skills/dimension-rebalance/SKILL.md` | 9 | 44.4k | /assess-skill | Visible-digest; F#3 Violated (Write missing from allowed-tools) |
| `.claude/skills/system-audit/SKILL.md` | 6 | 44.8k | /assess-skill | Persisted; 3V 0M 8P 4S |
| `.claude/skills/assess-prompt/SKILL.md` | 7 | 44.7k | /assess-skill | Persisted; G9.I6 Partial (over-broad tool grant); 2V 1M 10P 4S |
| `.claude/skills/compare-repos/SKILL.md` | 5 | 45.6k | /assess-skill | Persisted; **G9.I6 Satisfied**; 2V 5P 15S |
| `.claude/skills/detect-drift/SKILL.md` | 5 | 45.8k | /assess-skill | Persisted; **G9.I6 Satisfied**; 2V 4P 16S |
| `.claude/skills/design-skill/SKILL.md` | 5 | 45.8k | /assess-skill | Persisted; G9.I6 Partial; 2V 8P 11S |
| `.claude/skills/repo-analyzer/SKILL.md` | 4 | 47.1k | /assess-skill | **report-missing** (bin 4 partial output) |
| `.claude/skills/system-health/SKILL.md` | 9 | 44.3k | /assess-skill | Visible-digest; non-safety-critical; F#3 Missing (boundary section) |
| `.claude/skills/reassess-priorities/SKILL.md` | 7 | 44.8k | /assess-skill | Persisted; G9.I6 Partial; 2V 3M 8P 4S |
| `.claude/skills/synthesize-guide/SKILL.md` | 2 | 52.6k | /assess-skill | **report-missing** (bin 2 partial output) |
| `.claude/skills/assess-skill/SKILL.md` | 8 | 44.5k | /assess-skill | Persisted (self-audit); 0V 1M 5P 7S |
| `.claude/skills/watch-blogs/SKILL.md` | 8 | 44.6k | /assess-skill | Persisted; 2V 3M 5P 3S |
| `.claude/skills/process-feedback/SKILL.md` | 8 | 44.6k | /assess-skill | Persisted; 0V 1M 4P 8S |
| `.claude/skills/cleanup-cache/SKILL.md` | 9 | 44.0k | /assess-skill | Visible-digest; **G9.I6 Satisfied** |
| `.claude/skills/design-agent/SKILL.md` | 5 | 46.3k | /assess-skill | Persisted; G9.I6 Partial; 2V 7P 11S |
| `.claude/skills/research-loop/SKILL.md` | 3 | 49.0k | /assess-skill | Visible-digest; **G9.I6 VIOLATED** (KB writes no HITL) |
| `.claude/skills/perplexity-research/SKILL.md` | 6 | 45.5k | /assess-skill | Persisted; 3V 4M 4P 4S |
| `.claude/skills/watch-upstream/SKILL.md` | 9 | 44.3k | /assess-skill | Visible-digest; **G9.I6 VIOLATED** (auto Edit after triage) |
| `.claude/skills/assess-agent/SKILL.md` | 8 | 44.6k | /assess-skill | Persisted (self-audit); 0V 1M 4P 8S |
| `.claude/skills/extract-artifacts/SKILL.md` | 2 | 56.7k | /assess-skill | **report-missing** (bin 2 partial output) |
| `.claude/skills/research-proposer/SKILL.md` | 3 | 47.3k | /assess-skill | Visible-digest; DEPRECATED (DD-80); F#25 Violated (incomplete deprecation) |

## Agents (4 fractal)

| Path | Variant inferred | Bin | Footprint | Outcome |
|---|---|---|---|---|
| `agents/librarian/agent.md` | A (prompt-based) | 1 | 59.1k | Persisted; 0V 6M 7P 4S |
| `agents/codifier/agent.md` | A+B (prompt + harness) | 1 | 58.9k | Persisted; 0V 8M 10P 7S |
| `agents/owner/agent.md` | A+C (prompt + autonomous-vs-supervised) | 1 | 58.8k | Persisted; 0V 5M 11P 10S |
| `agents/researcher/agent.md` | A+B (prompt + harness) | 1 | 58.8k | Persisted; 0V 8M 6P 11S |

## CLAUDE.md files (7)

| Path | Bin | Footprint | Outcome |
|---|---|---|---|
| `CLAUDE.md` (root) | 2 | 49.6k | **report-missing** (bin 2 partial). Word count 1957 → likely substantive (not MOC). |
| `docs/CLAUDE.md` | 3 | 47.3k | **Shape mismatch — MOC.** Folder-level directory README. 232 words. |
| `governance/proposals/CLAUDE.md` | 3 | 47.3k | **Shape mismatch — MOC.** Frontmatter `type: "index"`. 256 words. |
| `operations/references/CLAUDE.md` | 3 | 47.2k | **Shape mismatch — MOC.** Plain folder README. 145 words. |
| `extracts/CLAUDE.md` | 4 | 47.1k | **report-missing** (bin 4 partial). 78 words → almost certainly MOC. |
| `extracts/patterns/CLAUDE.md` | 4 | 47.1k | **report-missing** (bin 4 partial). 73 words → almost certainly MOC. |
| `extracts/guides/CLAUDE.md` | 4 | 47.1k | **report-missing** (bin 4 partial). 55 words → almost certainly MOC. |

## Prompts (0)

None discovered (no `prompts/` or `system-prompts/` directories in IL).

## Subagent files (0)

`.claude/agents/` is empty in IL. The Librarian engine subagent lives at workspace root `.claude/agents/librarian.md` per DD-82; the audit (correctly) does not cross system boundaries to discover it.

# Not discovered (structural gaps)

- IL has no `.claude/agents/` content — engine subagent for Librarian is referenced from workspace root, outside `<target>`. Per design contract, this is correct: single-target audit only.
- Owner and Codifier engine subagents are also absent from `systems/improvement-loop/.claude/agents/`; the four fractal `agents/*/agent.md` files are the only deployed agent-shape artifacts.
- No `prompts/` or `system-prompts/` directories — IL does not author standalone prompts as artifacts.

# Ambiguous classifications

- All 7 CLAUDE.md files were dispatched to `/assess-agent --variant prompt-based` per v1 default. **3 of the 4 audited came back as shape-mismatch MOC latents** (docs/, governance/proposals/, operations/references/). 3 of the 7 are unaudited due to bin 4 partial output but their word counts (55–78) and locations strongly suggest MOC shape. **Cumulative MOC recurrence with session 114 MetaSystem (3 confirmed MOCs) = ≥6 across 2 systems.** Rule-11 trigger met — see summary §"MOC-CLAUDE.md classifier decision".

# Sizing summary

- Total artifacts: 43
- Total estimated subagent footprint: ~1.99M tokens across 9 bins (ceiling: 250k each)
- Bin assignments: Bin 1 (235.6k, 4 agents), Bin 2 (208.3k, 4 artifacts), Bin 3 (238.1k, 5), Bin 4 (235.2k, 5), Bin 5 (229.0k, 5), Bin 6 (225.7k, 5), Bin 7 (223.5k, 5), Bin 8 (222.9k, 5), Bin 9 (220.7k, 5).
- Largest artifact: `agents/librarian/agent.md` at 59.1k.
- Oversized bins: none.

# Default excludes applied

`archive/`, `_tmp/`, `_cache/`, `node_modules/`, `.git/`, `reflections/` — codified in v1 SKILL.md §"Default exclusions" (added session 114).

# Coverage gaps (bin 2 and bin 4 partial output)

Bins 2 and 4 each returned only 1 of N expected sentinel-delimited reports — a v1 format-compliance regression. 7 of 43 artifacts are unassessed in this run (extract-artifacts, synthesize-guide, IL CLAUDE.md root, repo-analyzer, extracts/CLAUDE.md, extracts/patterns/CLAUDE.md, extracts/guides/CLAUDE.md). See summary §"Design contract refinement candidates from this run".
