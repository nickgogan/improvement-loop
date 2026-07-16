---
name: 'Structural Outline Before Read: Compact Code Summaries as Agent Navigation Maps'
summary: 'Instead of an agent reading whole files to learn a codebase''s shape, it first pulls a compact

  structural outline — functions, classes, imports, exports with line numbers — and uses it to

  decide what to actually read. ast-grep''s author-measured benchmarks on 7 real repos show

  35-55% cost reduction on large repos (VS Code, Django, OkHttp) at 100% of baseline answer

  coverage — but overhead on small repos (under ~1,000 files), so the pattern must be size-gated.

  Focused-extraction flags (--match for one symbol, --items imports/exports) act as progressive

  disclosure of the code surface: shape first, members on demand, full source last.'
implementation_notes: 'Already partially adopted: session 130''s ENHANCE verdict landed ast-grep outline in

  /repo-analyzer (structural-inventory and import-map dimensions), gated on repo size and tool

  availability — which is why adoption_status is Partially Adopted / Improvement Loop. Remaining

  design surface: the optional outline pass in /audit-artifacts, and generalizing the size gate

  (small repos: grep + direct reads already win; the benchmark''s break-even sits near ~1,000

  files). Feature is alpha (v0.44.0) — pin expectations accordingly.'
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: P2 (Design Required)
applicability:
- General
adopted_in:
- Improvement Loop
sources:
- ast-grep-outline-structural-summaries.md
related_findings: []
proposals: null
date_discovered: '2026-07-11'
last_updated: '2026-07-11'
consumed_by:
- structuring-agent-context.md
pipeline_status: synthesized
---

## What It Is

An agent navigation pattern built around `ast-grep outline` (alpha in v0.44.0): before opening source files, the agent requests a compact structural summary — function/class declarations with line numbers and first-line signatures, imports, exports, direct members, public/private flags. Three surfaces: single-file inspection (`ast-grep outline src/parser.ts`), directory export surfaces (`ast-grep outline src`), and symbol expansion (`--match Parser --view expanded`). The `--items imports` / `--items exports` and `--match` flags narrow output further — progressive disclosure of the code surface: outline first, focused symbol next, full read last, each step informing the next.

## Why It Matters

Broad file reads are the dominant token cost in agent codebase exploration, and most of what's read is never used. The outline gives the agent a map — "12: export function parseRule(source: string)" — that is enough to decide *what* to read and *where* (line numbers make the follow-up read surgical). Author-measured results across seven repositories with architecture-level questions: VS Code (11,370 files) 45% fewer tokens / 35% cheaper; Django (3,030 files) 67% fewer / 55% cheaper; OkHttp (640 files) 40% fewer / 40% cheaper — all at 100% of baseline answer coverage. The critical caveat: small repos inverted the result (Gin, 99 files: 11% *costlier*; Alamofire, 108 files: token increase, cost even) — "smaller repositories … were already cheap to explore with grep and direct reads, so outline sometimes added work instead of saving it." The pattern therefore ships with a size gate, not as a universal default.

## Why People Are Using It

Released by the ast-grep project explicitly for code agents, with published benchmarks; positioned on a stated spectrum between grep (fast, local, textual) and LSP/AST indexes (global, semantic, slow or stale) — "fast like local search, correct about syntax structure, and concise enough to guide the next read."

## Potential Alternatives

- grep + targeted reads (wins on small repos; no structural awareness).
- LSP document-symbol queries or ctags (similar shape data; LSP needs a running server per checkout, ctags needs generated tag files).
- Repo maps baked into context (e.g., Aider-style repo map) — precomputed rather than on-demand.

## Potential Improvements

- JSON output (planned upstream) would let harnesses post-process outlines instead of parsing text.
- Custom extraction rules per project (planned) — project-specific symbol kinds surfaced in outlines.
- Automatic size gating in skills: probe file count first, choose outline vs grep strategy accordingly.

## Potential Failure Modes

- Small-repo overhead: applied without a size gate, the pattern adds a step and costs more than it saves (measured on sub-1,000-file repos).
- Coverage gaps from incomplete extractor rules — outlines silently omit constructs the rules don't cover; by design the gap is in rules, not heuristics, but the agent can't tell from the output.
- Alpha-stage churn: flags and output format may change; hard-coding output parsing is brittle until JSON output lands.
