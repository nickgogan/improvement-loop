# Hermes Agent — Memory Architecture

Dossier for the E1 memory-architecture spec's cross-framework survey (Track B). Written
2026-07-16. Internal KB grounding was thin (one 2026-05-24 structural analysis, ~5K, plus
five sources surfaced via `rg -i hermes`) so this dossier leans heavily on external
research (WebSearch/WebFetch against first-party Hermes docs, GitHub issues, and dated
third-party write-ups). Every sentiment claim is dated; recency is weighted per the
survey's recency rule (2026/late-2025 outranks older unless clearly de facto consensus).

**Disambiguation (read this first).** "Hermes" is an overloaded name in this space:

1. **Hermes Agent** (`github.com/NousResearch/hermes-agent`) — the subject of this
   dossier. A self-hosted, self-improving autonomous agent (persistent daemon, CLI,
   HTTP API, web UI, Telegram/Discord/Slack/WhatsApp/Signal gateway), built and
   maintained by **Nous Research**, launched **February 2026**.
2. **Nous Research's Hermes model series** (Hermes 3, Hermes 4, etc.) — fine-tuned LLMs
   from the *same organization*. **This is NOT the agent framework.** Same publisher,
   completely different product (a model vs. a runtime). Casual references to "Hermes"
   in agent-memory discussions almost always mean the agent (#1), but the org overlap is
   a real confusion source and the task brief's warning is correct to flag it.
3. **The "rebuilt Hermes memory in Claude Code" genre** — a cluster of *at least three*
   independent 2026 creator write-ups/videos that reimplement Hermes Agent's memory
   design inside Claude Code rather than adopting the Hermes runtime: Simon Scrapes'
   "I Rebuilt Hermes in Claude Code (It's Ridiculously Good)" (2026-05-23, earlier build,
   branded "MAOS"), Simon Scrapes' "I Rebuilt Hermes's Best Feature in Claude Code (Steal
   This)" (2026-07-10, the KB-tracked source, refined build with a recall ladder), and a
   third creator's "I Built The Best Claude Memory System (Beats Hermes)". These are
   **not Hermes** — they are practitioner reactions to it, covered in §4 for sentiment
   and used to shade §2 where Hermes' native design is being *replaced*, not described.

Internal KB context: `watched-libraries/hermes-agent.md` and its thin analysis doc
(`watched-libraries/analysis/hermes-agent-analysis.md`, 2026-05-24) track Hermes Agent
under `nousresearch/hermes-agent` — confirmed correct against the live repo. Six KB
findings already draw on Hermes, all traceable to two sources: the 2026-05-24 structural
analysis and the 2026-07-10 "rebuild" video (`research-sources/rebuilt-hermes-memory-in-claude-code.md`).

---

## 1. Snapshot

Hermes Agent is a 165k+ star (2026-05-24) / 211k+ star (2026-07-10, per the rebuild
video's own framing — "zero to 211,000 GitHub stars in just 5 months") open-source
autonomous agent. Python, self-hosted (runs on anything from a $5 VPS to a GPU cluster),
multi-entrypoint (CLI, HTTP daemon, Telegram/Discord/Slack/WhatsApp/Signal, cron), any
backing model (Nous Portal, OpenRouter, OpenAI, self-hosted endpoint). Its headline
differentiator, per its own marketing and independently per practitioner sentiment (§4),
is memory + a closed self-improvement loop: it "creates skills from experience, improves
them during use, nudges itself to persist knowledge, searches its own past conversations,
and builds a deepening model of who you are across sessions" (first-party GitHub
description). Memory scope covers user identity/preferences, environment/operational
facts, full session history, and procedural skills — i.e., all four of
working/episodic/semantic/procedural in some form (§2), though the split is a *de facto*
architectural pattern surfaced consistently across sources, not a term Hermes' own docs
use natively.

Currency: primary sources (hermes-agent.nousresearch.com/docs, GitHub) were fetched live
2026-07-16 and describe a system at "v0.9.0 (April 2026)"-and-later state per
glukhov.org's dating; the pluggable memory-provider system (8 providers, setup wizard)
is a *later* addition that replaced an earlier Honcho-only manual-config path — the
provider system is what's live today, not what the earliest reviews describe.

---

## 2. Memory model by type

### Working / short-term memory
**Substrate:** the live context window, bounded by the model's context limit. A
`context_compressor.py` component summarizes older turns while preserving recent
messages once a roughly-50%-of-window threshold is crossed (dev.to, manikant92,
2026-05-23 — third-party framing, not verified against first-party source in this pass).

**Write path:** every turn appends automatically; no explicit write step. The
`memory`-tool write decisions (below) happen *during* working memory, as a side effect of
processing a turn, not as a separate working-memory mechanism.

**Injection/recall:** total and automatic until compression fires. No first-party
detail was found on exact trigger thresholds or what gets dropped vs. summarized beyond
the third-party ~50% figure above — flagged as unconfirmed.

**Consolidation/decay:** the compressor is the only working-memory-specific mechanism;
everything of durable value is expected to have already been promoted to MEMORY.md/USER.md
(semantic) or the skills directory (procedural) before working memory rolls off.

### Episodic memory (specific past sessions/events)
**Substrate:** `~/.hermes/state.db`, a SQLite database with **FTS5 full-text indexing**
over session messages. This is the "capture everything" layer — separate from the
curated snapshot, every turn's raw transcript is archived regardless of importance.

**Write path:** automatic, unconditional, agent-internal — no salience judgment gates
what gets archived here (contrast with MEMORY.md/USER.md below, which *are*
salience-gated). Every session is stored.

**Injection/recall:** **not** injected by default. Recall happens on demand via the
`session_search` tool. First-party docs (hermes-agent.nousresearch.com/docs, fetched
2026-07-16) state search "queries return actual messages from the DB — no LLM
summarization, no truncation," i.e., raw FTS5 keyword hits. (One third-party source,
glukhov.org, describes `session_search` as pairing SQLite with "Gemini Flash
summarization" — this conflicts with the first-party "no LLM summarization" language for
search *results*; the likely reconciliation is that summarization happens at a different
stage, e.g. building the searchable index or a chat-facing answer layer, not the raw
search-tool response itself. Flagged as an unresolved discrepancy between primary and
secondary sources rather than smoothed over.)

**Recall is Hermes' acknowledged weak point.** FTS5 is **keyword-only**: a query for
"payment processing" will not surface a conversation that only used the word "Stripe."
This is not a rumor — it is documented in Hermes' own open issue tracker:
- **Issue #44075**, "Feature: Semantic Search for Session History (Hybrid BM25 + Vector)"
  — session_search "relies exclusively on FTS5 keyword matching."
- **Issue #346**, "Feature: Structured Memory System — Typed Nodes, Graph Edges, and
  Hybrid Search" — current memory "cannot express relationships between memories,
  distinguish between types of knowledge, decay stale information, or perform semantic
  search."
- **Issue #17350**, a bug where the optional Holographic memory plugin (a
  semantic-search add-on) silently degrades to FTS5-only when `numpy` is missing, with no
  warning and no `hermes doctor` detection.
- **Issue #20552**, Holographic memory's `get_relevant_memories()` fails on queries mixing
  a rare entity term with common words — FTS5-style relevance scoring dilutes the rare
  term's signal even in the semantic-search plugin path.

The fix path Hermes offers is **external, not native**: 8 pluggable memory-provider
plugins (Honcho, OpenViking, Mem0, Hindsight, Holographic, RetainDB, ByteRover,
Supermemory) run *alongside* built-in memory, adding knowledge graphs, semantic search,
automatic fact extraction, and cross-session user modeling — but only **one provider
active at a time**, additive not a replacement for the FTS5 core, and (per practitioner
sentiment, §4) historically confusing to configure.

**Consolidation/reflection:** no first-party evidence found of automatic
episodic-to-semantic distillation. One third-party source (dev.to, 2026-05-23) describes
a weekly "Curator" cron job that "grades skills, merges duplicates, archives unused
procedures, and rewrites descriptions" — but this is framed around the *skills* directory
(procedural), not the session archive, and was not independently confirmed against
first-party docs in this pass. Treat as plausible but unconfirmed, same caveat class as
the Claude Code survey's "Auto Dream."

**Decay/forgetting:** none documented. The SQLite archive appears to be append-only and
permanent; no retention window or pruning policy surfaced in first-party docs.

### Semantic memory (durable facts, preferences, identity)
**Substrate:** two markdown files at `~/.hermes/memories/`:
- `MEMORY.md` — agent's own notes: environment facts, conventions, learned lessons.
  Hard cap **2,200 characters (~800 tokens)**, ~8–15 entries typical.
- `USER.md` — user profile: preferences, communication style, identity. Hard cap
  **1,375 characters (~500 tokens)**, ~5–10 entries typical.

Combined budget: ~1,300 tokens maximum, always-on. This is the architecture the internal
KB finding `bounded-tiered-memory-inference-driven-curation.md` already documents from
the 2026-05-24 analysis pass; the numbers above were independently re-confirmed against
live first-party docs in this research pass and match exactly.

**Write path:** the `memory` tool (`action="add"|"replace"|"remove"`), called by the
agent itself — either from an explicit user request ("remember that...") or from
**inference-driven, post-turn judgment**: the agent proactively saves when it detects
learned user preferences, environment facts, corrections, conventions, or completed work,
and deliberately skips trivial info, easily re-derivable facts, raw data dumps, and
session-specific ephemera. A background self-improvement review can also initiate writes
after a turn completes. Duplicate exact-content writes are blocked automatically.

**Injection/recall:** **frozen snapshot pattern.** At session start, both files load from
disk and render into the system prompt as a static block (with usage-percentage/char
counts visible to the agent). This is deliberately prefix-cache-preserving: mid-session
edits persist to disk immediately but do **not** appear in the live prompt until the
*next* session — explicitly designed to stop the model "chasing its own tail" by reacting
to memory it just wrote.

**Consolidation:** **no auto-compaction.** A write that would exceed the character cap
returns an **error**, not a silent drop or truncation — the agent must then read current
entries (shown in the error response), consolidate/merge related ones via `replace`, and
retry. Best-practice guidance in the docs: consolidate proactively above ~80% capacity.
This "fail loud, not silent" design is a meaningful contrast with softer character-cap
handling elsewhere in the survey (e.g., Claude Code's `MEMORY.md` nudge-then-silent-drop
behavior described in the Claude Code dossier, §2).

**Decay/forgetting/supersession:** no automatic decay of any kind. Eviction is entirely
manual — the agent (or user) must explicitly `remove` or `replace` a stale entry. Nothing
ages out on its own; "stale memory" is a documented practitioner complaint (§4) precisely
because of this.

### Procedural memory (skills / how-to)
**Substrate:** a `skills/` directory of markdown files with YAML frontmatter, one file
per skill, compatible with the `agentskills.io` open standard. Progressive disclosure:
skill *names/descriptions* load at session start cheaply (~3K tokens for ~100 skills per
one third-party estimate); full skill bodies load only on invocation.

**Write path:** the `skill_manage` tool, invoked by the agent after: completing a complex
task (5+ tool calls) successfully, hitting an error/dead-end and finding a working path,
being corrected by the user mid-task, or discovering a non-trivial reusable workflow.
Actions: `patch` (targeted fix, preferred), `edit` (major rewrite), `write_file`
(add/update supporting files), `delete`.

**Injection/recall:** name/description list at launch; full content on invocation
(matches the progressive-disclosure pattern used across the survey's other frameworks).

**Consolidation/reflection:** "after every complex task, the agent reflects on its
performance, identifies patterns, and documents new skills" (WebSearch aggregate,
undated-precise but 2026 sourcing) — this *is* Hermes' headline self-improvement loop.
The unconfirmed weekly-Curator-cron claim (above) would sit here if real.

**Decay/supersession:** governed by an *optional* safety layer, not automatic
housekeeping:
- `skills.write_approval` gate — when enabled, every agent-initiated skill write is
  **staged, not committed**, pending human review (`/skills pending`, `/skills diff`,
  `/skills approve`, `/skills reject`). **Off by default** is the implication of "when
  enabled" language in the docs — this default posture is the direct cause of the
  self-rewrite failure mode reported in §4.
- `skills.guard_agent_created` — content scanning for dangerous patterns in
  agent-authored skills.
- Bundled skills flagged "user-modified" are skipped during framework updates, to avoid
  clobbering local edits.
- `hermes skills reset` — abandon all pending edits, restore original bundled versions.

---

## 3. Lifecycle trace — one memory item, end to end

Trace: the user tells Hermes, mid-session, "we settled on Stripe for payment processing,
not PayPal," and later debugs a Stripe webhook retry issue in the same area.

1. **Turn processed.** The message enters working memory (context window) like any turn.
2. **Post-turn inference (semantic write).** The agent judges "settled on Stripe" as a
   durable decision, not ephemera. It calls `memory(action="add", target="memory",
   content="Payment processor: Stripe (decided over PayPal)")`. If MEMORY.md is near its
   2,200-char cap, this may instead trigger a `replace`-based consolidation pass first.
3. **Unconditional episodic write.** Independent of step 2, the full turn (verbatim) is
   already persisted into `state.db` and FTS5-indexed — this happens for every turn,
   decision-worthy or not.
4. **Snapshot frozen for the rest of the session.** The MEMORY.md write is on disk
   immediately but won't appear in the live prompt until the *next* session starts
   (prefix-cache preservation) — so later in this same session, the agent still has to
   rely on working-memory continuity, not the freshly-written snapshot, if it needs the
   fact again.
5. **Next session.** MEMORY.md (now including the Stripe decision) loads as a frozen
   block before the first turn — zero retrieval cost, guaranteed presence.
6. **Weeks later, a Stripe webhook retry bug comes up.** The agent works the problem
   (5+ tool calls, hits a dead end, finds the fix) and calls `skill_manage` to write a new
   skill file documenting the webhook-retry procedure — procedural memory. If
   `write_approval` is enabled, this lands as a pending diff, not a committed file, until
   a human runs `/skills approve`.
7. **Recall test.** Months later the user asks "what payment processor did we pick and
   why?" — MEMORY.md still holds it verbatim (no decay), answered directly from the
   always-injected snapshot, no search needed. But if the user instead asks "what was that
   payment thing we discussed?" without saying "Stripe" or "processor," `session_search`'s
   FTS5 keyword matching may miss the relevant older session entirely (documented gap,
   §2) — the fact is *stored* but not *reliably recallable* through vocabulary drift.
8. **Failure-mode branch (documented, not hypothetical).** If `write_approval` is
   **disabled** (the implied default) and the self-improvement loop later "improves" the
   webhook-retry skill, community reports (§4) describe the agent overestimating its own
   edit quality and overwriting the human-added caveat about retry backoff timing —
   silently, with no rollback path unless the user separately bolted on approval/rollback
   tooling.

---

## 4. Practitioner sentiment (dated)

**Growth is real and memory-attributed — 2026-07-10** (Simon Scrapes, "I Rebuilt Hermes's
Best Feature in Claude Code," transcript): "Hermes agent went from zero to 211,000 GitHub
stars in just 5 months" (i.e., since its February 2026 launch); "somebody [Kilo] analyzed
1,300 Reddit comments about why people are switching to it from Open Claude... roughly
30% of switchers actually cite memory defaults as the reason." Representative quotes he
surfaces from that analysis: "easier setup, better memory"; "Remembering context is worth
more than a thousand integrations"; "Hermes agent is like a junior colleague who never
forgets." His framing of the market thesis: "these tools carry limited context between
sessions even as they add memory features. Hermes is effectively competing against the
session model itself" — i.e., practitioners increasingly value continuity over raw model
capability. This is the single most load-bearing sentiment datapoint in this dossier
(recent, quantified, dated) and it is corroborated structurally by the KB's own
`memory-system-evaluation-triad-storage-injection-recall.md` finding, which names the
same switching wave as "won on storage + injection defaults."

**Stale memory is the top complaint — 2026-05-23** (dev.to, manikant92): "Stale memory is
the #1 reason Hermes starts acting weird" — direct consequence of §2's no-auto-decay
design; MEMORY.md/USER.md require active maintenance or they accumulate outdated facts
that outrank current reality. Same source: "self-improving requires active correction and
explicit saving; passive use shows modest gains" — i.e., the headline self-improvement
loop underdelivers without an engaged operator.

**Self-rewrite overwrites good work — 2026, aggregate WebSearch sourcing (dailydoseofds
"Hermes Agent Masterclass," qwe.edu.pl, mranand.substack, exact publish dates not
individually confirmed but consistently 2026):** "the in-agent learning loop has a known
weakness: the agent tends toward self-congratulation and almost always thinks it
performed well, even when it didn't — community feedback has confirmed this." "Some users
reported the agent overwrote their carefully tuned skills during 'self-improvement,'
turning them into jumbled messes." This is independently corroborated by the KB's own
`bounded-tiered-memory-inference-driven-curation.md` and
`memory-cross-layer-promotion-governance.md` findings (sourced from the 2026-07-10
rebuild video), and by the first-party mitigation trail itself: `write_approval`,
`guard_agent_created`, and `hermes skills reset` all read as *reactive* fixes for a
problem the community surfaced first, not designed-in-from-day-one safeguards. **This is
the most consistently corroborated failure mode across independent source types**
(practitioner blogs, the rebuild video, and the shape of Hermes' own remediation
features) — it clears the bar for de facto consensus despite lacking one single precise
date.

**Honcho/provider configuration was a real onboarding failure — undated-precise, 2026,
aggregate:** "Previously, Honcho was the only external memory option and had to be
configured manually and wasn't enabled by default — a source of significant confusion in
the community." "Multiple Reddit users reported confusion when the 'self-learning'
features didn't work out of the box. You have to explicitly enable Honcho in the config,
which isn't mentioned in the quickstart." **Resolved, not current**: Hermes has since
shipped a pluggable memory-provider system (8 providers, setup wizard) that replaces the
old manual-config path, with auto-migration for existing Honcho configs. Recency rule
applies here directly — treat the confusion reports as historically real but the
underlying cause as fixed by the time of this writing (2026-07-16).

**Recall is the field-acknowledged weak axis — 2026-07-10** (rebuild video, corroborating
the open GitHub issues in §2): "there's even an open issue on Hermes' own GitHub that
says session search relies exclusively on this FTS5 keyword matching." The practitioner
response pattern is telling: rather than filing more complaints, at least three
independent creators (§0 disambiguation) rebuilt semantic+keyword hybrid recall
themselves, either inside Claude Code or by bolting on external providers
(MemZero/Honcho-class plugins) — recall is where the ecosystem visibly diverged from
copying Hermes verbatim.

**Balanced/critical framing — 2026, Towards Deep Learning (Sumit Pandey), "Hermes Agent:
The Hype, The Reality, and Who Should Actually Use It":** memory and the "Soul" feature
are "interesting and worth existing" but "feel like the first rung on a tall ladder...
memory too small and not situationally aware enough yet." Proposed practical bar: "if
Hermes can complete one recurring workflow with less repeated context after each run, it
is worth keeping in the stack" — a pragmatic, use-case-gated endorsement rather than a
universal one.

**Security researchers flag memory/skill persistence as an attack surface — 2026**
(Repello AI, "Hermes Agent Security: A Threat Model for Enterprise Workstation
Deployment"; Cloud Security Alliance research note, dated ~2026-05-04, "9 CVEs in 4
Days"): "Attackers can write into the agent's memory store via shared documents, emails,
web pages, or Slack messages, planting instructions that the agent retrieves and executes
on future turns... Memory retrieval bypasses traditional prompt-injection defenses."
Specifically on skills: "If the agent can be injected once during a session and that
session produces a skill, the injection persists on disk as a Markdown file... Hermes is
the first popular framework where [memory-poisoning-to-persistent-skill] is the default
behaviour" (memory-poisoning research itself dates to 2024, per the same source, but its
concrete instantiation in a popular shipped agent is a 2026 development). Hermes' own
defense — content scanning for injection/exfiltration/backdoor patterns before any
memory persists — is confirmed in first-party docs and is a direct response to this class
of report.

**Vendor-published material (bias caveat):** hermes-agent.ai's own blog ("Hermes Agent
Review 2026 — Honest Verdict After 30 Days," "Why Hermes Wins on Memory") reads as
marketing content associated with the project's own ecosystem, not independent review —
included for completeness but weighted low relative to the independent sources above.

---

## 5. Verdict

**Strengths worth transferring:**
- **Frozen-snapshot injection with hard character ceilings and fail-loud overflow.**
  MEMORY.md/USER.md's design (2,200/1,375 char caps, error-not-silent-drop on overflow,
  prefix-cache-preserving frozen-per-session loading) is a clean, low-mechanism pattern
  the engine has already partially adopted via
  `bounded-tiered-memory-inference-driven-curation.md`. The "error on overflow, not
  silent truncation" detail is worth double-checking against whatever the E1 spec
  currently assumes — silent drop is a subtler, harder-to-notice failure mode than a
  loud one.
- **Inference-driven write triggers, explicit skip criteria.** Hermes documents *what it
  deliberately does not save* (trivial info, re-derivable facts, raw dumps, ephemera) as
  clearly as what it does save — a useful explicit-negative-list model for the engine's
  own promotion-gate design, even though the engine otherwise avoids negative-space
  governance (per standing practice) — this is scoped to a single component's write
  filter, not a system-wide rule, so the tension is minor.
- **Progressive disclosure for procedural memory** (skill name/description at launch,
  full body on invocation) is validated convergently — same shape as Claude Code's Skills
  and multiple other frameworks in this survey family.

**Failure modes to design against, not copy:**
- **No native decay/supersession is a real, reported problem**, not a theoretical gap.
  "Stale memory is the #1 reason Hermes starts acting weird" (2026-05-23) is a direct
  consequence of manual-only eviction. The engine's `memory-cross-layer-promotion-governance.md`
  (policy-gated promotion *and* demotion with importance/recency scoring) is a genuine
  improvement over Hermes' bare model here, not just parity — this finding should be
  weighted up, not down, by this dossier's evidence.
- **Self-rewrite-without-default-gating is the most consistently corroborated failure
  mode in this survey.** Independent practitioner blogs, the rebuild-video source, and
  the shape of Hermes' own reactive mitigations (write_approval, guard_agent_created,
  reset command — all opt-in, all clearly added after the fact) triangulate on the same
  conclusion: **an autonomous agent that can rewrite its own durable memory/skills will,
  with real-world frequency, overwrite good information unless promotion is gated by
  default.** This is strong external corroboration — not just consistency, actual
  evidence — for the engine's already-ruled IB-176 generator-assessor separation and
  per-proposal Nick gate. It argues against ever relaxing that gate to "trusted
  autonomous promotion," even for low-stakes-seeming writes, because Hermes' failure
  reports don't discriminate by stakes — routine edits are exactly what gets clobbered.
- **FTS5-keyword-only recall is a multi-issue, multi-quarter, still-open gap** (issues
  #44075, #346, #17350, #20552) that the ecosystem worked around externally (plugins) or
  rebuilt from scratch (the Claude Code rebuild genre) rather than waiting on upstream.
  For the engine: recall is already the explicitly parked axis of the IB-176 design per
  the KB's own triad finding — this dossier's evidence says don't rush a naive
  keyword-only recall as a placeholder; the field has already demonstrated that choice
  ages into a named, recurring complaint. If recall ships before hybrid semantic+keyword
  is feasible, treat it explicitly as a known-limited interim state, not a finished
  feature.
- **Memory/skill persistence is a live security surface**, specifically because
  autonomous writes to disk-persisted, next-session-trusted files create a channel for
  injected instructions to survive across sessions. The engine's files are
  git-versioned and human-gated at every promotion, which structurally blocks the
  "agent silently persists poisoned content, trusted on reload" pattern Hermes' security
  researchers describe — but this dossier surfaces a gap worth naming explicitly: nothing
  in the KB's current memory-design findings mentions *scanning content before
  persistence* the way Hermes' first-party defense does. Worth a line in the E1 spec even
  though the git-gate already covers most of the risk by a different mechanism.

**Transferability notes for a markdown+git, single-operator, human-gated engine:**
- The separate-runtime cost structure Hermes carries (VPS, second model billing,
  independent security surface, independent update cycle) is the most-cited practitioner
  reason for *not* adopting Hermes directly, even by people who admire its memory design
  — this is confirmation, not new information, that the engine's own
  harness-native/no-second-runtime posture
  (`platform-native-harness-over-agent-frameworks.md`) is the right call for this
  project's shape; no action needed beyond noting the corroboration.
- Hermes' four-way memory split (working/episodic/semantic/procedural, per the dev.to
  synthesis, independently consistent with first-party docs) maps cleanly onto the
  engine's own PROGRESS.md (working) / HISTORY.md+git (episodic) / DDs+knowledge/
  (semantic) / skills (procedural) shape — useful as an external validation point that
  the four-way split itself is a sound organizing frame, separate from any of Hermes'
  specific mechanics.
- Single biggest actionable gap this dossier surfaces for the E1 spec: **decide the
  demotion/decay policy explicitly and early** — Hermes shipped without one, the field
  noticed within months, and retrofitting eviction policy onto an already-populated
  memory store is harder than designing it in from the start.
