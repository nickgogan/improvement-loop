---
type: "link-intake-triage-report"
topic: >-
  Run 2 of the link-intake triage protocol (session 130) — 7-link LINKS.md batch
  added by Nick after the pilot (Anthropic/Claude articles + one commands repo)
date: "2026-07-11"
protocol_spec: "operations/references/link-intake-protocol.md"
input: "systems/improvement-loop/LINKS.md (7 links, added 2026-07-11 after pilot batch cleared)"
verdict_set: ["ADD", "ENHANCE", "KB-ONLY", "REJECT"]
---

# Link-Intake Triage Report — 2026-07-11, run 2

Second run of the protocol (first post-pilot). Two tracks (roster/repo, KB), verdicts gated;
this report changes nothing by itself.

## Verdict summary

| # | Link | Class | Verdict | One-line disposition |
|---|------|-------|---------|----------------------|
| 1 | glittercowboy/taches-cc-resources `/commands` | REPO-SKILLBEARING | **KB-ONLY** (no-op) | Already a watched library, analyzed 2026-05-24 after upstream's last push; 0 ADDs from 27 commands; one marginal ENHANCE candidate flagged (`heal-skill`) |
| 2 | anthropics/claude-cookbooks `building_evals.ipynb` | ARTICLE | **REJECT** | Fully covered (grading-hierarchy + volume-over-quality findings, 2 sources); canonical runnable reference for a future evals-for-skills skill |
| 3 | Anthropic — Building Effective Agents | ARTICLE | **REJECT** | Exact URL already a KB source with 3 extracted findings; blog is tier-1 watched |
| 4 | Claude Code — prompt caching is everything | ARTICLE | **KB-ONLY** | Densest link in the batch: ~5 novel harness-layer patterns; queue extraction |
| 5 | Anthropic — harness design for long-running apps | ARTICLE | **REJECT** | Exact URL already a KB source with 4 extracted findings |
| 6 | Claude blog — sales leader runs 4,000-account book | ARTICLE | **REJECT** | Usage story; 1 marginal novel pattern, below the 2-novel bar |
| 7 | Claude blog — the founders' playbook | ARTICLE | **REJECT** | Marketing content; frameworks named but not operationalized |

Tally: 0 ADD · 0 ENHANCE (one flagged candidate inside #1) · 2 KB-ONLY · 5 REJECT.

## Per-link rationales

### 1. taches-cc-resources /commands — KB-ONLY (no-op; self-dedup case)
We already track and have mined this repo: registry entry
`watched-libraries/taches-cc-resources.md` (cherry-pick), full analysis doc
(`analysis/taches-cc-resources-analysis.md`, analyzed 2026-05-24 — after upstream's last push
2026-04-01, so no re-analysis triggered), and its signature patterns already extracted as
findings (meta-prompting separation, thinking-model commands, context-degradation threshold,
loadable domain-expertise sub-skills). Mining all 27 commands against the roster produced **no
ADDs** — nearly everything is subsumed by the gsd-* suite, `/session-handoff`,
`/prompt-enhancer`/`/prompt-evaluator`, `/assess-*`/`/design-*`, `/research-query`, or existing
findings. One **marginal ENHANCE candidate, Nick-gated**: `heal-skill`'s in-session repair loop
(detect which skill just misbehaved from conversation context → root-cause reflection →
before/after diff → 4-option approval gate → apply + cross-file consistency check) as an
immediate "heal now" fast path for `/process-feedback`, whose current path is file-mediated and
deferred. Timely for the skill-evals thread (an eval loop needs a repair half) but marginal per
Rule 11 — recommendation below. Quality skim: portable, plain Claude Code assumptions, sound
structure; auditor agents pin `model: sonnet`.

### 2. claude-cookbooks building_evals.ipynb — REJECT (covered)
Everything the notebook teaches is already in the KB: code/model/human grading hierarchy
(`three-tier-grading-hierarchy.md`), volume-over-curated-sets
(`volume-over-quality-eval-principle.md`), binary assertion design, balanced eval sets, input
coverage — plus the same doctrine as two sources. The only delta is that it's *runnable*.
**Flag:** when the engine designs its evals-for-skills capability, this notebook is the
canonical reference implementation — record it in that skill's design inputs; don't re-triage.

### 3. Building Effective Agents — REJECT (covered)
Exact URL already in the KB as `anthropic-building-effective-agents.md` with three findings
extracted (framework-abstraction tax, poka-yoke tool interfaces, ground-truth feedback loops).
The Anthropic engineering blog is a tier-1 watched blog; its post log recorded this post as
source-created 2026-04-09. Anything missing flows through `/watch-blogs` or `/linkage-repair`,
not re-intake.

### 4. Lessons from building Claude Code: prompt caching — KB-ONLY (queue extraction)
The batch's gem, squarely on the harness-layer mission: the Claude Code team's production
playbook for treating prompt-cache **prefix stability as a first-class design constraint**. KB
has the basic idea (stable-context caching; byte-identical prefixes via OpenClaw) but not these
operational mechanics: (1) append `system-reminder` messages instead of mutating the prompt;
(2) never switch models mid-session — hand off to a subagent instead; (3) keep the tool set
static and make mode changes callable tools (plan mode as Enter/ExitPlanMode); (4) cache-safe
compaction by forking with an identical prefix + reserved compaction buffer; (5) cache hit rate
monitored like uptime with SEV-grade alerting. ~5 novel patterns. **Roster note:** the
never-switch-models mechanic feeds skill↔model-coupling guidance (model-capability-registry,
`/design-agent` variant B); the deferred-tool-stub pattern cross-corroborates the existing
GPT-5.4 tool-search finding (evidence-strength upgrade candidate at extraction time).

### 5. Harness design for long-running apps — REJECT (covered)
Exact URL already in the KB as `anthropic-harness-design-long-running-apps.md` with four
findings (builder-validator chains, sprint contracts, cost concentration in generation,
harness simplification as models improve). Post log: source-created 2026-04-09.

### 6. Sales leader / 4,000-account book — REJECT
Usage story, not engineering. Real but generic workflows (scheduled skills, multi-source report
assembly, human-in-the-loop approval); the one distinctive move (overnight rubric-scored batch
run with natural-language weight tuning) is Cowork scheduling + LLM-as-judge, both covered.
1 marginal novel pattern — below the 2-novel bar.

### 7. The founders' playbook — REJECT
Marketing content for startup founders: stage-level business advice (problem validation, PMF,
product-selection matrix) without techniques, configs, or quantified results. Zero novel
actionable patterns.

## Follow-up queue (each item separately gated)

1. **Prompt-caching post** → research-source entry + `/research-loop` extraction (joins the
   run-1 extraction queue).
2. **`heal-skill` ENHANCE candidate** → **Ruled: hold** (Nick, 2026-07-11) per Rule 11 —
   in-session repair is a mechanism addition on first occurrence; revisit when the
   evals-for-skills thread lands, where a repair half will have concrete recurrence.
3. **LINKS.md clearance** once verdicts are accepted.
4. No registry/analysis action for taches-cc-resources (coverage already current; registry
   star-count trivially stale — 1931 vs live 1975; not worth an edit).

## Protocol observations (run 2)

- **Self-dedup earned its keep twice**: the registry check caught an already-tracked repo
  (taches) and exact-URL dedup caught two already-mined sources (#3, #5) — five of seven links
  resolved without any extraction cost. The dedup-against-live-corpus rule (pilot lesson)
  worked as designed.
- **Watched-blogs overlap**: two links were posts from an already-watched tier-1 blog. A future
  refinement candidate (not proposed yet, Rule 11): classify-step check against the
  watched-blogs post log before dispatching to a track.
- Protocol recurrence count now 2. Promotion trigger (reference doc → skill) fires at a third
  batch with stable shape.
