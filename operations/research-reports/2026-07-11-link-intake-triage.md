---
type: "link-intake-triage-report"
topic: >-
  Pilot run of the link-intake triage protocol (session 130) over the 13-link
  LINKS.md batch — roster-fit + KB-fit verdicts per link
date: "2026-07-11"
protocol_spec: "session-130 inline spec (Nick-approved 2026-07-11); landing form proposed separately"
input: "systems/improvement-loop/LINKS.md (13 links, batch replaced by Nick at session-129 close)"
verdict_set: ["ADD", "ENHANCE", "KB-ONLY", "REJECT"]
---

# Link-Intake Triage Report — 2026-07-11 (pilot run)

Pilot of the link-intake triage protocol on the current LINKS.md batch. Three parallel triage
tracks (roster / repo / KB), one verdict per link. **This report changes nothing by itself** —
every ADD/ENHANCE execution and every KB-ONLY routing is separately Nick-gated; LINKS.md is
cleared only after verdicts are accepted.

## Verdict summary

| # | Link | Class | Verdict | One-line disposition |
|---|------|-------|---------|----------------------|
| 1 | Medium — semantic/episodic/procedural memory | ARTICLE | **REJECT** | Paywalled; taxonomy already covered in 1.C |
| 2 | arXiv 2605.19576 — skill-library drift | PAPER | **KB-ONLY** | 4 novel patterns; queue `/research-loop` |
| 3 | arXiv 2606.24775 — agent-memory systems survey | PAPER | **KB-ONLY** | 3 novel patterns; queue `/research-loop` |
| 4 | arXiv 2605.12922 — attention closure / goal loss | PAPER | **KB-ONLY** | Extends context-rot findings; queue `/research-loop` |
| 5 | ast-grep outline | ARTICLE | **ENHANCE** | Adopt in `/repo-analyzer` (+ optional `/audit-artifacts`); also extract as pattern |
| 6 | Anthropic — recursive self-improvement | ARTICLE | **REJECT** | Strategy essay, not builder patterns; stats flagged for model-capability-registry refresh |
| 7 | Kaggle whitepaper — new SDLC with vibe coding | PAPER | **KB-ONLY** | Same content as #8; one source entry, blog canonical |
| 8 | addyosmani.com — new SDLC vibe coding | ARTICLE | **KB-ONLY** | 3 novel patterns; queue `/research-loop` (covers #7) |
| 9 | cursor-team-kit `deslop` SKILL.md | SKILL | **REJECT** | Fully subsumed by harness `/simplify` + `/code-review` |
| 10 | cursor-team-kit `thermo-nuclear-code-quality-review` SKILL.md | SKILL | **KB-ONLY** | Not roster material; dense skill-design exemplar → research-source |
| 11 | anomalyco/opencode | REPO-FRAMEWORK | **KB-ONLY** | Watched-library entry + `/repo-analyzer` |
| 12 | TJSlattery/MemoryDemo | REPO-DEMO | **KB-ONLY** | Research-source only (zero-star demo; 1 citable pattern) |
| 13 | omnigent-ai/omnigent | REPO-FRAMEWORK | **KB-ONLY** | Watched-library entry + `/repo-analyzer`, **high priority** (confirmed Databricks meta-harness) |

Tally: 0 ADD · 1 ENHANCE · 9 KB-ONLY · 3 REJECT.

## Per-link rationales

### 1. Medium — semantic vs episodic vs procedural memory — REJECT
Inaccessible: Medium member paywall exposes only the intro and section outline; the promised
implementation blueprints are behind the wall. Novelty is doubtful even if retrieved — the
three-type taxonomy is already represented in 1.C Memory Systems coverage
(`converged-memory-substrate-vs-patchwork.md` enumerates working/semantic/episodic/procedural;
`four-tier-agent-memory-model-with-write-policy.md` covers tiered memory with write policies).
Re-triage only if a non-paywalled mirror surfaces and delivers the concrete implementation.

### 2. arXiv 2605.19576 — skill-library drift — KB-ONLY
Directly on-mission for a self-evolving engine that maintains its own skill library: the paper
names and reproduces the failure mode we are exposed to — unbounded skill accumulation degrading
retrieval and stagnating performance ("library drift") — and ships a verified fix. Headline
warning for us: human-curated skills gave +16.2pp while ungoverned LLM-authored skills gave
+0.0pp. The KB has self-improvement-loop findings but nothing on skill-lifecycle governance,
retirement thresholds, or per-skill attribution. Four distinct quantified patterns, all novel
after dedup (fix lifted pass@1 0.258 → 0.584; the meta-skill authoring prior alone accounts for
57% of the gain; costs 43% more LLM calls). **Roster note:** the Ratchet Recipe
(outcome-driven skill retirement with evidence floor, bounded active-skill cap) is a candidate
governance rule for the engine's own roster; feeds the "evals for skills" + assets-catalog
direction.

### 3. arXiv 2606.24775 — "Are We Ready For An Agent-Native Memory System?" — KB-ONLY
Fills a 1.C gap: existing KB memory findings are individual architecture patterns; we have no
systematic comparison saying which architecture fits which workload. Evaluates 12 memory systems
+ 2 baselines across 5 workloads/11 datasets from a data-management perspective; concludes no
single architecture dominates — effectiveness depends on aligning memory structure to the
workload bottleneck. Three novel decision-relevant patterns, including a maintenance-cost result
(localized maintenance beats global reorganization) that maps onto our KB-curation practice.

### 4. arXiv 2605.12922 — "When Attention Closes" — KB-ONLY
Gives mechanistic grounding and predictive power to a phenomenon we track behaviorally (context
rot / instruction drift): goal tokens become attention-inaccessible while persisting in residual
representations — instructions are not gone, they are unreachable, so periodic re-injection
restores them; failure timing is parametrically predictable for windowed attention. Introduces
the Goal Accessibility Ratio diagnostic (linear probes predict recall at AUC up to 0.99 across
four architectures). Extends `context-rot-attention-budget-depletion.md` (crosslink as
`extends`); 2–3 novel patterns.

### 5. ast-grep outline — ENHANCE
A tool the engine's analysis skills should adopt, not just record: `ast-grep outline` generates
compact structural summaries (functions/classes/imports/exports with line numbers) on demand, no
index, with measured 35–55% token-cost reduction on large repos at 100% baseline coverage in the
authors' testing. **Targets:** `/repo-analyzer` — use `ast-grep outline <dir>` (+ `--items
imports`) for the structural-inventory and context-file/dependency-map dimensions instead of
broad file reads; gate on repo size (minimal benefit on small repos). `/audit-artifacts` —
optional outline pass before per-artifact reads. Also KB-worthy as a pattern
(structural-outline-before-read); queue for extraction alongside the skill delta. URL
301-redirects to astgrep.com — record the canonical URL in the source entry.

### 6. Anthropic — "When AI Builds Itself" (recursive self-improvement) — REJECT
On-mission topic, wrong content type: a strategic essay/forecast, not builder-applicable
patterns. Its contributions are capability-trend evidence (task-horizon doubling every 4 months;
80% of Anthropic's merged code Claude-authored as of May 2026), a three-scenario RSI
preparedness framing, and lab-level governance proposals — none implementable by an agent
builder. The one adjacent design insight (humans retain research taste/judgment; AI executes) is
already covered (`brain-boundary-architecture-humans-at-periphery.md`). **Flag:** the
first-party capability stats are suitable citations for the next
`operations/references/model-capability-registry.md` refresh.

### 7 + 8. Kaggle whitepaper / addyosmani.com — new SDLC with vibe coding — KB-ONLY (one extraction)
Confirmed same content: the Kaggle page hosts the Google whitepaper co-authored by Addy Osmani;
the blog post is his own extraction of it (and the Kaggle page returns only a JS shell to
WebFetch — the blog is the accessible source of record; if full-whitepaper depth is wanted
later, the PDF needs `/pdf-to-markdown`). Of six named patterns, three survive dedup: (1)
static/dynamic context partition documented as a **versioned architectural decision** — we have
push-vs-pull loading but not the partition-as-ADR governance move; (2) **dual verification** —
trajectory (reasoning-path soundness) as a distinct eval axis from output correctness, absent
from `four-layer-agent-evaluation-architecture.md`; (3) **conductor-vs-orchestrator** operating
modes (interactive IDE exploration vs async delegation for well-specified tasks) — no KB
coverage. One source entry covering both URLs, canonical = the blog.

### 9. cursor-team-kit `deslop` — REJECT
Fully subsumed: a 20-line checklist for stripping AI-generation artifacts from a code diff
(extra comments, defensive try/catch, any-casts, deep nesting), every item covered by the
harness-provided `/simplify` and `/code-review` (+ `gsd-code-review`). Targets application-code
diffs, which the engine does not produce. Too thin (bullet list; no procedure/state/output
contract) to justify KB intake as a pattern source.

### 10. cursor-team-kit `thermo-nuclear-code-quality-review` — KB-ONLY
As a roster skill it overlaps harness `/code-review` (which already has escalating effort up to
ultra) and reviews app-code diffs we don't produce — don't install. But it is unusually
pattern-dense as a **skill-design exemplar**, which is exactly what the assess-skill/design-skill
substrate feeds on: full strictness-escalation architecture (core prompt → numbered
non-negotiable standards → per-change review questions → aggressive-flag list → preferred
remedies → tone calibration via literal example phrases → prioritized output ordering →
explicit approval bar with "presumptive blockers"), hard quantitative blockers (file pushed past
1000 lines = presumptive rejection), and `disable-model-invocation: true` (explicit-invocation-
only pattern for intentionally harsh modes — itself KB-worthy). Several rules echo standing
engine principles ("is this abstraction actually earning its keep"). Fully portable prompt-only
skill, no model coupling. → research-source entry.

### 11. anomalyco/opencode — KB-ONLY
The canonical opencode — leading open-source terminal coding agent (184k stars, MIT, pushed
2026-07-11) — under its current home after the SST org renamed to Anomaly Co (the archived
13.4k-star `opencode-ai/opencode` is the unrelated pre-dispute project; provenance clean).
Primary reference harness for tool/harness-design and loop-engineering dimensions and a
comparison point for the agentic-OS harness layer; its repo carries AGENTS.md, CONTEXT.md,
`.opencode/`, specs/ — exactly the surface `/repo-analyzer` mines. Framework, not a skills
collection → watched-libraries intake + `/repo-analyzer`.

### 12. TJSlattery/MemoryDemo — KB-ONLY (research-source only)
A compact working reference implementation of the five-memory-type taxonomy (working/episodic/
semantic/procedural/shared) in one LangGraph + MongoDB Atlas + Chainlit stack, with one genuinely
useful pattern: **typed shared-memory slots** (plan/findings/disambiguation/handoff_payload) for
coordinator↔sub-agent handoff that avoid paraphrase loss. But zero-star, single-author,
no-license demo — evidence strength weak; not watched-library material. Research-source entry
for 1.C; cite the shared-memory-slot pattern if corroborated elsewhere.

### 13. omnigent-ai/omnigent — KB-ONLY (high priority)
**Confirmed as the Databricks Omnigent from the session-129 design note** (NOTICE: "Copyright
(2026) Databricks, Inc."; shipped under a neutral org). The most agenda-relevant repo in the
batch: an Apache-2.0 meta-harness orchestrating Claude Code, Codex, Cursor, OpenCode, Hermes,
Pi, and YAML-defined custom agents *above* the harnesses you already use — with a policy layer
(approval gates, spend caps, tool limits), OS-level sandboxing (bwrap/seatbelt; Modal/Daytona/
E2B/K8s/Databricks cloud backends), and cross-device session continuity. A shipped instance of
exactly the "harness layer + governance-first" architecture the agentic-OS direction is
formalizing. 7k stars in one month; alpha status. → watched-libraries entry + prioritized
`/repo-analyzer` pass; mine the policy model and harness-abstraction seams against the
skill↔model-coupling and governance dimensions. Also resolves the design note's "Databricks has
zero KB coverage" gap.

## Follow-up queue (each item separately gated)

1. **ENHANCE — ast-grep outline** into `/repo-analyzer` (and optionally `/audit-artifacts`);
   modified skills re-audited via `/assess-skill` (Rule 10).
2. **Watched-libraries intake:** registry entries for `opencode` and `omnigent` (+ `/repo-analyzer`
   runs; omnigent first).
3. **Research-source entries:** thermo-nuclear skill (exemplar), MemoryDemo, vibe-coding SDLC
   (one entry, two URLs), three arXiv papers → then `/research-loop` extraction pass over the
   four KB-ONLY extraction targets (#2, #3, #4, #7/8).
4. **Model-capability-registry refresh flag:** Anthropic RSI essay stats as first-party citations.
5. **LINKS.md clearance** once verdicts are accepted (this report is the audit trail).

## Protocol observations (input to the landing proposal)

- The classify step earned its place: three tracks needed genuinely different evidence (full
  SKILL.md read vs README+API metadata vs content skim), and the repo track caught two
  provenance questions (opencode org rename; omnigent = Databricks) that a KB-only skim would
  have missed.
- The roster track fired weakly on this batch (0 ADD, 1 ENHANCE — and the ENHANCE came from the
  KB track's escalation question, not from a SKILL-class link). The dominant flow was routing
  into existing intake paths.
- Dedup-index handoff bug: the orchestrator passed a truncated findings index (200 of ~770
  lines); the KB-track agent detected it and grepped the corpus directly. Lesson: agents should
  dedup against the live corpus, not a snapshot index.
- Both literal-SKILL.md links resolved without needing full `/assess-skill` runs — the
  lightweight quality/portability skim was sufficient for a triage verdict.
