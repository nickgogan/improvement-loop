# History

Newest-first changelog of shipped sessions and milestones for the improvement-loop engine.
`PROGRESS.md` stays forward-only (current focus + queue) and points here for anything already shipped;
git is the atomic record of what changed, file by file (Conventional Commits from session 133 onward).
Entries carry dates and commit ranges where known; sessions 1–116 predate this file and are collapsed into era summaries.

## Session 146 — 2026-07-13 — Phase 4 interview prep + gate-clearance fully executed (2a2108b…8ffedc8)

**Outcome:** the Phase 4 interview structure is drafted, and gate-clearance is complete end-to-end under a standing delegated-judgment grant ("trusting your judgement") — every ruling made *and* every extraction executed. Promotions applied; all 18 harvest rows across 4 queues resolved; 11/11 drift re-extractions and 3 schematic re-evals done. A Fable-5 monthly spend limit aborted the first extraction wave mid-run; state was salvaged consistent, then the remainder was finished on Opus 4.8 in staggered 3-agent waves (no further limit hits). Five corpus-scan consolidation gates surfaced and were ruled inline — all two-way doors, itemized below for Nick's review/override.

- **Extraction execution (Opus, staggered waves).** 12 harvest artifacts written across the four post-sweep guide crops (templates, rules, skills); source findings back-annotated; queue rows written back to `extracted`/`merged`. Four mid-abort orphans (clean artifact, missing Step-4.8 write-back) were recovered by hand before the Opus waves resumed. All 11 drift-report `re-run` artifacts re-extracted via `--update` (lifecycle pointers set, no `last_change_sl` residue).
- **Five consolidation rulings (DD-97/DD-100, delegated grant — all git-reversible):** (1) `byte-stable-disclosure-catalog` → **extend** `never-mutate-cached-prompt-prefix` (Special Case section), per DD-97's extension-first thesis; (2) `static-first-prompt-layering-stack` → **DD-100 version-bump** to `seven-layer-prompt-assembly-with-cache-control-v2.md` (independent side-file, v1 untouched, `version: 2`); (3) `lesson-store-entry-schema` and (4) `pruning-is-status-change-never-deletion` → **create-new** (false-positive overrides — distinct object / opposite enforcement primitive from their flagged matches; the run-log rule explicitly scopes lesson stores out); (5) `derive-dont-edit` cross-queue twin → **merged** into the canonical `derived-artifacts-single-writer-rule`. Provenance in `operations/{extension,version-bump}-proposals/2026-07-13-*.md`.

- **Phase 4 interview structure** (`project-management/design-notes/2026-07-13-phase4-interview-structure.md`): adapts CareerBuddy `ops-vision-to-plan` v0.3.0 to the engine's kernel outputs — constitution → PRD → actors → generalize-first-vs-harness-first decision → checkpoint #2. Drops the upstream brief (opens with a pre-filled summary for confirmation instead, per reduce-Nick-bottleneck), keeps the per-section approval gates / binary-acceptance / cold-start-test mechanics; six blocks incl. the one-implicit-agent-vs-four-actors question and the two transcription clarifications ("attachés", "division to a degree") folded into Block 0. Awaits Nick's gate on its §5 questions.
- **Promotions L-1/L-2/L-4 applied** (proposal-log `P-1..P-3`, commits 4507084…fdb2fcf): each through the full pipeline — shadow-sandbox validate → fresh-context 4-verdict grade → apply. L-1 = G9.I6 write gates on `promote-findings`/`translate-governance`/`research-loop`/`watch-upstream` (1 revise cycle — the assessor caught an ungated Periodic Web Scan write path in research-loop); L-2 = gh-first repo-location in `/repo-analyzer`; L-4 = tallies-from-enumeration in `/identify-artifacts`. Source-finding carve-out in L-1: user-supplied URLs authorize their own source entries; agent-discovered URLs gate source creation too. Lessons flipped to `promoted`.
- **Harvest queues ruled + closed** (all 4 post-sweep guide crops): 16 rows nick-approved + 2 dismissed (memory-system-triad-scorecard, fail-open-routing-hook-invariants — both re-queueable). Final tally across all 18 rows: 14 extracted, 2 merged, 2 dismissed — every queue fully resolved.
- **Drift-report recommendations accepted + executed** (`operations/drift-reports/2026-07-13-source-drift.md`): 3 schematics re-evaluated and materially updated (autonomy maturity time-axis on project-coding-workcell + scheduled-operations-assistant; re-curation-destroys-signal failure mode on research-scanning-agent); all 11 `re-run` artifacts re-extracted via `--update`.
- **Orchestration note (not codified — first occurrence, external cause):** the initial 7-agent parallel extraction wave hit the account's Fable-5 monthly spend ceiling mid-run. No engine surface prevents an external process kill, so no lesson was filed; the recovery (hand-reconcile orphans, then resume on Opus in staggered 3-agent waves) is the pattern to repeat, and the judgment cost (fan-out size vs. spend headroom) is flagged to Nick rather than mechanized.

## Session 145 — 2026-07-13 — milestone shipped: KB codification + memory-system v1 build (0ed0ceb…0ec57a4)

**Outcome:** the post-sweep P1/P2 crop is codified into the four affected guides, and the engine's memory system v1 is live end-to-end — the CareerBuddy-style self-improvement loop with Nick's demand ledger (IB-176 ship steps 1–2), with the frozen System Log distilled into consumable artifacts and closed.

- **codifier-run** (first sitting, pre-handoff commit 0ed0ceb): `/identify-artifacts` over the 5-finding crop — all approved as pattern at Nick's gate; `/detect-drift` pre-step authorized and run (most hits cosmetic crosslink/priority metadata; re-run and schematic re-eval recommendations queued for ruling); 4 guide re-syntheses (G1 writing-agent-specifications, G2b defending-agent-context, G7 session-persistence-and-memory, G10 agent-design-patterns) with fresh harvest queues; findings back-annotated `synthesized`.
- **memory-system build, ship step 1** (226528a): `operations/self/` store (lessons / query-log / proposal-log / retro + gitignored capture buffer); `/self-improve` skill (capture/scan/promote/status, Owner-owned) — rule-10 audited via a fresh-context `/assess-skill` subagent, all high/medium findings fixed pre-commit (canonical contract headings, apply-on-`applied`-only clause, 2-cycle revise cap, assessor Consumes/Produces, tool tiering); `UserPromptSubmit` capture hook registered in tracked `.claude/settings.json` (first concrete harness-layer instance); `store_check.py` as pre-commit check 4; lessons-check step added to `/session-handoff`; `/process-feedback` retired into scan mode, rosters updated.
- **memory-system build, ship step 2** (0ec57a4): one-time SL distill over all 153 entries (3 parallel miners) — calibration numbers → `operations/references/calibration-registry.md` (consumer-keyed sections with read-moments; dated figures are priors, not truths); lesson residue → `lessons.md` L-1…L-9 after verifying each candidate against its owning surface (already-codified classes triaged out, audit trail in `retro-latest.md`); SL corpus closed read-only in place (DD-59 placement respected). First-run PROMOTE flags: L-1 (unconfirmed G9.I6 write-gate remediation across 4 skills, high), L-2 (gh-first repo location missing in `/repo-analyzer`, high), L-4 (tallies-from-enumeration, N=2).
- IB-176 marked Done; deferred pieces stay per design note §6/§9 (findings-search implementation parked; DD/IB audit waits on its converged reading list; docs/portability → Phase 4/5).

## Session 144 — 2026-07-13 — Phase 1 shipped: wave-3 triage→extraction, gap-check, checkpoint #1 + KB currency sweep (694fb06…7e2b253)

**Outcome:** Phase 1 (research grounding) is complete and checkpoint #1 is ruled — and the KB was brought fully current for the coming design work: every named dependency re-analyzed at today's upstream version, every candidate promotion dispositioned, linkage symmetric, priorities re-tiered under Nick's gate.

- **Wave-3 triage** (`/link-intake`, 4 read-only topical subagents over the 28 cached videos): 0 ADD / 0 ENHANCE / 10 KB-ONLY / 18 REJECT, Nick-accepted. Second consecutive zero-ADD/ENHANCE run → bulk video intake **closed as a phase instrument** at checkpoint #1; future spend = targeted `/research-query` + primary sources. Gate ruling captured: the Zhao keep was affirmed for **human/AI seam identification** — the Librarian should help an operator see what stays *human* (also in agent memory as a standing steer).
- **Pass 2 extraction** (3 parallel subagents): 9 sources, 27 findings, 13 extensions; Pat Simmons authority created; Jones trio extracted as the three legs of the named-deps gap-check (eval-ceiling / delegation-contract / harness-fitness).
- **Named-deps gap-check** (`operations/research-reports/2026-07-13-named-deps-gap-check.md`): 6 grounded / 1 partial (BMAD governance layer — covered by the Phase 4 CareerBuddy import) / 1 gap ("attachés" — Nick one-liner, now plan open-question 7); §6 collects task-queue feedstock for the deferred DD/IB study. **Delta report** (`…phase1-research-grounding-delta.md`) closed the Phase 1 DoD; checkpoint #1 outcome recorded in the plan of record (Phase 5 gains capability-as-composition-unit as named input + a maintenance/fitness DoD; IB-176 ship order unchanged).
- **KB currency sweep** (Nick: "brainstorm from a fully-up-to-date KB"): Archon re-analyzed at v0.5.0 (loops now a first-class engine primitive), BMAD at v6.10.0 (skill flattening 112→35 step files; memlog governance runtime; critical-thinking layer now exists — it didn't at v6.2.2), superpowers at v6.1.1 (unified dual-verdict reviewer supersedes the two-stage review our KB/DD-62 cite — stale finding annotated; brainstorming HARD-GATE verbatim unchanged, ask still grounded), **pydantic-ai onboarded** as a watched library at v2.9.0 (Nick-accepted; Monty tracked inside; capability primitive = 31-file hook lattice; core-vs-harness split is inter-repo with a graduation path). 49 candidates dispositioned → 33 promoted (Archon 7, pydantic-ai 8, BMAD 11, superpowers 7; 1 genuine cross-repo merge: append-only-run-log ← BMAD memlog + superpowers ledger).
- **Hygiene closeout:** builder-io orphan root-caused (Notion-era gap) and repaired 3-way; 100 deferred reverse links + 24 new typed links, all symmetric; 7 corroboration extensions applied; 3 authority triage notes; GPT-5.6 registry profile added with evidence caveats (fills the registry's declared grounding hole).
- **Priority reassessment applied** (Nick-accepted, `…priority-reassessment-2026-07-13.md`): ralph-wiggum → **P1** (5-org corroboration; Nick's gate note: engine treats Ralph and Archon's PIV plan-to-PR loop as sibling variants — linked), append-only-run-log → **P1** (IB-176 input), 4 new P2s, two-stage-review → Not Flagged (originator deprecation), 4 caveats incl. memory-file-to-skill-migration kept at P2 (the Archon counter-signal self-undermines via its own mirror drift).

## Session 143 — 2026-07-13 — wave-3 transcripts resolved 28/28 via fallback lane (bac87bb…724bb52)

**Outcome:** the wave-3 transcript backlog is fully resolved — all 28 unique videos (20 retries + 9 Nick-added, 1 dup) cached as full-text markdown, LINKS.md emptied — clearing the path to `/link-intake` triage and the rest of the Phase 1 wrap.

- **Browser rung verified, then defeated:** three real bugs fixed in `fetch.py`'s browser backend with Nick debugging alongside (fixed-sleep captured the transcript panel's spinner → wait on segment selectors; JS `.click()` is untrusted and silently no-ops on YouTube's components → real Playwright clicks + hard error when the button is missing; Chapters→Transcript chip toggle added for YouTube's stuck-spinner bug). Two clean end-to-end fetches proved the rung — then ~26 rapid sequential fetches tripped a hard IP block on caption endpoints (even previously-working videos began failing; page HTML kept serving).
- **Every direct lane confirmed dead under the block:** transcript API, playwright scrape, persistent-profile browser pull, yt-dlp with and without real-Chrome cookies (429 is IP-level, not account-level), in-page player-session fetch (the player's own caption URL 429s), Invidious mirrors (caption-dead ecosystem-wide), and cloud egress (YouTube blocks datacenter IPs wholesale; probed via remote agent).
- **Winning lane (Nick's "whatever it takes" mandate, change-nothing constraint):** kome.ai's server-side transcript API — their infra fetches YouTube; our IP never touches a caption endpoint — plus watch-page `ytInitialPlayerResponse` for metadata. Scratchpad script only; technique preserved in agent memory (`kome-transcript-fallback`); codification as a fetch.py backend left as a Backlog trigger item. 23-video batch ran 23/23 with 6–12s pacing.
- **Transcript format ruled full-text-only:** the Timestamped Segments section dropped from the writer and stripped from all 133 pre-existing cached files (6.9 MB → 3.0 MB, 57%) — zero findings or sources ever cited a video timestamp; SKILL.md contract updated to match. Coarse anchors can return if a citation need ever materializes.

## Session 142 — 2026-07-13 — memory-system design ruled; Phase 2 shipped (b277a4d…cc15e92)

**Outcome:** Phase 2's remaining half is done — the memory-system design was brainstormed and ruled inline with Nick: a CareerBuddy-lift self-improvement loop plus a Nick-originated demand ledger (query/intent log). Build filed as IB-176 (Approved, P1); IB-172 closed as delivered.

- **Design note** `project-management/design-notes/2026-07-13-memory-system-design.md`: `operations/self/` store (lessons + query-log + proposal-log + retro), one 4-mode skill (capture/scan/promote/status), N=2 normal / N=1 high thresholds ("threshold gates autonomy, never direction"), five-stage promotion pipeline (draft → shadow sandbox → separate-context grade → per-proposal Nick gate → append-only log), dispatch table (DD-116 routing generalized), deterministic `store_check.py` in pre-commit. Capture split: hooks for determinism (UserPromptSubmit query capture, store validation), agent for judgment (inline lesson capture + a lessons-check step in `/session-handoff`).
- **Demand ledger** (Nick's addition, researched this session): per-intent rows `Q-<seq> · query gist · route · why · served/partial/unserved`; unserved themes at threshold become IB proposals through the same promotion gate; the ledger doubles as the future implicit-routing harness's eval corpus. Lessons may cite Q-rows via the existing Source field (one-directional, optional, checker-verified). Web sweep persisted as the fifth deliberation report (`operations/research-reports/2026-07-13-query-intent-logging-web.md`): Rasa CDD / Dialogflow fallback analytics / zero-result-query mining as lineage; Datadog `/agent-observability-session-classify` + LangSmith Engine at org scale; claude-mem-lite hooks→SQLite as within-class persistence precedent; **no complete within-class implementation found** — compose-known-parts build, KB-finding candidate.
- **Rulings:** lesson capture = both inline + session-close sweep; `feedback/` folds into scan mode (`/process-feedback` retires with the build); frozen SL = one-time distill on first scan run (calibration numbers → `operations/references/calibration-registry.md` with named consumers; lesson residue → store) then closed archive; no `eval-candidates.md` v1 (ledger carries eval material); findings hybrid-search **implementation parked** (the component stays designed-in per session 141); DD/IB cruft audit + task-queue study wait to converge with the wave-3 named-deps gap-check.
- Archiving policy set per layer (design note §7): three new rules — done IBs → `archive/` at milestone close, ~50-open-lessons gated pruning trigger, run reports → `archive/` when their consuming phase closes; HISTORY/git classified as governance memory (append-only correct).
- Nick extended LINKS.md with 9 new links (one dup) for the wave-3 intake.

## Session 141 — 2026-07-13 — gate-execution closed (G8) + memory-system direction set (13947b1…39a91df)

**Outcome:** the substrate-audit gate program is fully executed (G1–G8 + follow-ups), and the second-brain question got its real answer: Nick rejected the residue-triage minimal proposal and set the direction — build an actual memory system (full IB-172 pulled forward), with four persisted research reports as the design input.

- **G8 guides dissolution:** pipeline guide marked DD-cache (DD-121) with its drift-magnet "Current State" table dropped (the DD-111 two-bodies framing kept as content); `knowledge/guides/_index.md` trimmed to a Dataview-only live view with a dissolution-bound scope note; `archive/guides/` created — 10 resolved harvest-queue files (97 rows verified all terminal before the move) + deprecated G2 `managing-agent-context.md`; `system-log-template.md` → `archive/templates/`; live pointers (routing table, read-contract example, consumer-abstractions-map) rewritten before the moves; `extracts/guides/CLAUDE.md` deployment-target fiction corrected to the DD-111 live-substrate framing.
- **No-gate follow-ups:** `knowledge/reference/_index.md` Household-OS framing fixed + its Dataview WHERE clause repaired (filtered on a `type` no file carries — the "live view" rendered empty); DD-66 got its missing `title`.
- **Second-brain proposal arc:** residue-triage version drafted (calibration registry + G9 defer + overflow-resolved; Librarian consult + 18-question web sweep as grounding) → **Nick rejected the minimal scoping** and ruled: an actual memory system — Hermes-style external memory + self-improvement loop; OpenClaw/GBrain references; IL-as-one-big-agent; must answer existing-corpus disposition + archiving policy; CareerBuddy `ops-self-improve` named the best self-improvement exemplar. Ruling recorded atop the design note; its residue evidence and question table remain design input; P1–P3 not adopted.
- **Research corpus persisted** to `operations/research-reports/` (four reports): Librarian residue consult, Librarian full architecture consult (layer mapping, transitions, retirement gaps, self-improvement wiring — run-report telemetry and the skills roster flagged as the two write-only layers), web 18-question design checklist + failure stories, web deep-dive (OKF v0.1 = ~50-line export transform, zero non-Google adopters; Obsidian dual-interface pattern; grep beats vectors empirically at our scale with FTS5/BM25 as first upgrade; lifecycle mechanics incl. OpenClaw's 3 promotion gates + only-system-with-numeric-decay).
- **Scale correction with teeth:** findings corpus measured at **907 files** (first consult was fed "~150") — at the KB's own ~1000-doc file-traversal ceiling; the KB's prescribed first move is hierarchical index-layer reinforcement, not RAG.

## Session 140 — 2026-07-12 — substrate-audit gate execution, G1–G7 (309b4b7…d5473e2)

**Outcome:** seven of the eight sanctioned gates executed under the door-type delegation — the broken pipeline stage repaired, the DD corpus cleaned (5 new DDs; 12 stale DDs formally superseded), the design-notes folder reduced to genuine deliberation, IB hygiene done. G8 (guides dissolution) + the no-gate `/maintain-docs` follow-ups remain.

- **G5 first (urgent):** DD-117 supersedes DD-95 — the lifecycle pointer re-anchors from the retired SL (`last_change_sl`) to the run's authorizing input (`last_change_report`: identification-report / harvest-queue stem, derived not passed; `--sl` argument and its abort paths deleted). `/extract-artifacts` non-guide writes work again; `_schema.yaml` updated; legacy pointers stay frozen-valid, no backfill.
- **G4 + second-order SL sweep:** DD-59 carries the scope note verbatim. Seven Librarian skills' encounter logging suspended pending G9 (encounters surface in run reports instead); the 13-type taxonomy/schema/routing distilled to `operations/references/librarian/boundary-cases.md`; `/solicit-proposals` round record re-routed to `governance/proposals/`; `/system-audit` + `/system-health` recency reads re-pointed to HISTORY + git; `librarian-reads.md` re-homed out of the frozen folder; Owner path maps annotated read-only.
- **G1:** DD-118 closes DD-31/38/40/42/50/58/90 in one consolidating supersession with per-DD successor pointers; pipeline-rules rules 6–7 re-sourced to DD-116 (telemetry rule retired); engine CLAUDE.md drops the DD-31 hard constraint.
- **G2:** DD-119 (foundational) restates the stage-before-deploy, workspace-shape, and milestone-gate invariants post-collapse; DD-39/47/61 superseded; FOUNDATIONS regenerated (DD-47 out, DD-119 in).
- **G3:** DD-120 re-homes DD-60/DD-62 as `knowledge/patterns/composable-agent-teams.md` + `explore-then-harden.md`; patterns `_index` hardcoded catalog trimmed to the Dataview view.
- **G6:** `archive/design-notes/` created — 10 ratified notes + 2 distilled sources archived, filenames preserved, no stubs; read-contract + use-case-registry re-homed to `operations/references/librarian/` with live pointers in 22 files rewritten *before* the move; DD-121 files the DD-wisdom caching policy (was live law anchored to a draft note); design-notes `_index` scope now excludes living reference material.
- **G7:** IB-148 cancelled (mooted by Phase 0), IB-102 cancelled (superseded by harness-materialization), IB-103 merged into IB-173 with its track-record prerequisites carried; IB-174 (meta-skill-author follow-ups A/D/E) and IB-175 (governance visualization) filed.
- Session cut by Nick after G7; G8 + no-gate follow-ups roll to the next session inside the same scope.

## Session 139 — 2026-07-12 — Phase 1 intakes + Phase 2 substrate audit (91d7bd2…dd32524)

**Outcome:** the KB gained both same-class agentic-OS exemplars (CareerBuddy + the anonymized enterprise context-hub), and Phase 2 opened with a full six-class substrate audit awaiting gate execution.

- **CareerBuddy intaken as primary source** (plan §Phase 1 item 2, five parallel Researcher passes): wiring canon, meta-skill-author references, ops-self-improve store model, C1–C16 deterministic battery, and the 5 queued corpus contributions — 5 source entries; dedup treated shared mechanics as production validation (both systems drew on this KB), extending rather than duplicating.
- **#8 taxonomy/clustering dependency resolved**: the private enterprise context-hub (an agentic Work OS built by one technical account manager, shared org-wide), intaken from an author-shared writeup + role-routing hook. Everything anonymized before write (vault going public — Nick directive); primary materials preserved at `research-sources/raw/context-hub/`; zero identifying strings verified vault-wide. Key yields: the asset-catalog form answer (directory + registry + generated views as one generation pipeline, not a choice), and the prompt-time role-routing hook Nick flagged worth keeping for front-door-less multi-agent systems.
- **Phase 2 substrate audit filed** (`project-management/design-notes/2026-07-12-substrate-audit.md`, six parallel Owner-disposition auditors, propose-only): DDs split 26 kernel / 59 state; 7 functionally-dead Binding DDs → one consolidating supersession (G1); ~230KB of April design notes fully ratified → archive (G6); `knowledge/guides/` confirmed too shallow, dissolves (G8); IB and concept-doc classes essentially clean; DD-112 survives the kernel model. **Urgent find:** `/extract-artifacts` functionally broken — DD-95 provenance anchor demands a retired SL entry (G5).
- **Nick rulings this session:** named-deps gap-check skipped for now; Phase 2 opened before Phase 1 close; **door-type delegation** granted (execute two-way doors on best judgment, surface only true tensions/one-way doors) → gates G1–G8 sanctioned for execution, G5 anchor = identification report, G9 folded into the Nick-gated second-brain proposal.
- Multi-tenancy observation recorded (single-operator exemplars dominate; users-as-data is CareerBuddy's answer) → backlog research-gap candidate.

## Session 138 — 2026-07-12 — restructure-program Phase 0 shipped (614102c…743499c)

**Outcome:** the engine's session ops run on the three-artifact spine — forward-only PROGRESS.md (the sole cold-start artifact) + this HISTORY.md + Conventional Commits (DD-116).

- This file created and backfilled (sessions 117–137 detailed, earlier eras collapsed); PROGRESS.md restructured to the control-surface shape, well under the 150-line soft cap.
- `/session-handoff` rewritten reconcile-in-place (first CareerBuddy import: `ops-session-handoff` @0.9.0; dual-scope/ledger apparatus dropped; ADAPTATION.md records provenance). Fresh-context Rule-10 `/assess-skill`: PASS — 3 Low findings fixed pre-commit. This close was its first end-to-end run.
- All dated handoffs archived to `archive/handoffs/`; wake-up idiom + Session Ops section registered in engine CLAUDE.md; PROGRESS line-budget check (warn >150 / block >250) added to the pre-commit hook beside the DD-114/DD-115 checks.
- **System Log retired as producer** (Nick ruling — stronger than the plan's option (a)), grounded in a Librarian KB pass over Omnigent/Hermes/OpenClaw session models: none routes learnings through a session store; all distill into a curated layer. Learnings now route decision→DD, pattern→`knowledge/`, work→IB; historical corpus kept as IB-172 feedstock. Recorded as DD-116; producer surfaces (`/sl`, `/track`, `/governance-audit`) carry retirement notes.
- Nick's **single-implicit-agent** vision refinement captured in plan §2 (one agent = the system itself; the kernel is that agent's full description) — Phase 4 interview input.
- Wave-3 retry correctly rolled forward untouched (same-day-plus as wave-2's IP block; window opens 2026-07-13).

## Session 137 — 2026-07-12 — gate rulings + hygiene + commit clearance (f88cfd2…6c44ea9)

- All session-136 checkpoint items ruled and executed: 3 watched libraries added (gbrain, mattpocock-skills, ponytail — Ponytail flagged by Nick as future Reviewer/Gate agent), 3 authorities created (Nate Herk, Tonbi's AI Garage, Austin Marchese), model-capability registry refreshed (GPT-5.6 skipped — no KB grounding).
- Playwright `--backend browser` rung built into `/transcript-fetcher` (Rule-10 `/assess-skill` PASS; 3 findings fixed pre-commit; live verification deferred to wave-3).
- Reassessment applied: `scale-threshold-heuristic-obsidian-vs-rag` P3→P2; `frontier-model-as-harness-designer` P3→P2; `trust-calibration-progressive-autonomy-ramp` → Strong.
- Hygiene: 193 session-136 one-way links reciprocated + 30 linkage repairs; karpathy duplicate-source and Nate B Jones duplicate-authority pairs merged; corpus-wide pre-existing link debt parked as IB-171.
- Two design directions approved: IB-172 layered memory architecture (semantic index + graph, OKF as curated layer; Hermes/OpenClaw inspiration) and IB-173 three-bucket gate tiering (DD-29 refinement).
- The 129–137 commit/push gate cleared — sessions 134–137 landed as the batch f88cfd2…6c44ea9; origin/main current, tree clean. Wave-3 correctly not attempted (same calendar day as wave-2's failure).
- Standing rule added: skill/corpus passes run as subagents; main thread gets report paths + short summaries.

## Session 136 — 2026-07-12 — Pass 2 extraction sweep (committed in session 137's clearance batch)

- All 28 Nick-accepted KB-ONLY sources extracted via 8 topical subagent clusters: 65 new findings (33 P2, 0 P1), 24 existing findings updated, pairing instructions honored, corpus-wide linter clean.
- Anthropic primaries ingested: `frontier-model-as-harness-designer` + six-pattern taxonomy upgraded to Strong (Bun Zig→Rust case study; "adversarial verification" naming correction); Fable field guide landed as the phase-anchored unknowns-reduction technique set.
- Authority pass: 5 entries updated, 8 new.
- Wave-2 retry of the 20 blocked videos failed same-day (0/20): IP-level 429 outlasts an hours-scale cooldown — retry guidance revised to ≥1 calendar day.
- `/link-intake` first skill run: no transcription defects. Batched Nick-gate checkpoint presented at close.
- Reports: `operations/research-reports/2026-07-12-delta-report.md`, `2026-07-12-link-intake-triage-wave2.md`.

## Session 135 — 2026-07-12 — LINKS.md triage sweep + /link-intake promotion (committed in session 137's clearance batch)

- Full 83-video sweep triaged: 28 KB-ONLY / 33 content-REJECT / 2 already-ingested / 20 defer-blocked on a YouTube 429; Nick accepted all verdicts same-session; LINKS.md reduced to the 20-video retry backlog.
- Fired promotion trigger ruled option 1: the protocol became the `/link-intake` orchestrator skill (via `/design-skill` + Rule-10 audit); protocol reference doc superseded.
- Global `bypassPermissions` ruled and set in `~/.claude/settings.json`.

## Session 134 — 2026-07-12 — video-intake tooling rebuilt inline (committed in session 137's clearance batch)

- `fetch.py` gained `--probe` (title/duration/upload-date/token-estimate), automatic video-ID dedup, and metadata-enriched headers; yt-dlp bot-check fragility fixed (Homebrew build preferred).
- transcript-fetcher SKILL.md gained the 6-step fallback chain + `status: "Blocked"` retry-backlog convention; research-loop SKILL.md gained the Video Batch Gate, transcript-first rule, and recency-weighting rule.
- `date_published` added to the source schema and backfilled across all sources via 6-subagent fan-out; all transcript headers enriched with zero probe failures.
- Both modified skills passed independent Rule-10 `/assess-skill` audits. Open residue: whether a formal `/meta-skill-author` Design-mode spec is still wanted.

## Session 133 — 2026-07-12 — restructure pivot + plan of record (7c253d0…33cdc18)

- User manual parked mid-contract (audience/altitude locked); Nick redirected to the engine restructure & harness program — plan of record `operations/plans/2026-07-12-engine-restructure-program.md` (6 phases; Phase 0 greenlit, not executed).
- Inputs: full CareerBuddy ops-model analysis (forward-only PROGRESS + HISTORY + reconcile-in-place handoff) and Nick's governance-as-portable-kernel vision.
- `meta-skill-author` imported from CareerBuddy @1.15.0 (adapted, Level-1 PASS, Rule-10 assessed; 2 upstream bugs found).
- 3-video KB intake kept on Nick's ruling; the ~70-link LINKS.md batch landed but parked (61 transcripts cached untracked).

## Session 132 — 2026-07-12 — promotion gate execution + sweep follow-ups (06baab9…a87292b)

- Pre-decided promotion gate executed in full: 10 findings promoted (7 New, O2-as-extends, C13-with-contradicts, and the `permission-channel-as-escalation-steering-bus` cross-repo synthesis); C4/C5/C7/C8 folded as corroboration; all 31 candidates annotated in both analysis docs.
- Batch reciprocity clean; 14 pre-existing one-way links repaired, 1 misnamed ref fixed.
- Scoped `/reassess-priorities`: no threshold crossings; one gate left for Nick (verbatim-storage null→P3).
- Triage run 3 didn't fire (LINKS.md empty); re-injection premise correction delivered in-chat.

## Session 131 — 2026-07-11 — research sweep (9f7dd6d…26bf5cd)

- omnigent + opencode structural analyses (omnigent verified as governance-without-constitution — the gap the agentic-OS model occupies).
- 8-source extraction pass: 23 new findings, incl. the first-party prompt-caching playbook and the skill-library-drift cluster.
- Model-capability-registry refresh (KB-grounded via narrow RSI-essay intake); linkage repair (32 reciprocal links).
- Attention-closure paper refutes the periodic-re-injection remedy (Appendix H negative result) — flagged for Nick.
- Promotion-candidates report (31 dedup-checked; `operations/research-reports/2026-07-11-promotion-candidates.md`); gate later resolved 2026-07-12 as adopt-as-is.

## Session 130 — 2026-07-11 — link-intake triage protocol (769ea22…a168491)

- Protocol designed, Nick-gated, piloted on the 13-link batch, then run again same-day on a fresh 7-link batch (20 links total: 0 ADD / 1 ENHANCE / 11 KB-ONLY / 8 REJECT).
- Landed as a reference doc (`operations/references/link-intake-protocol.md`) per Rule 11; skill promotion trigger set at a third stable-shape batch.
- The one ENHANCE (`ast-grep outline` → `/repo-analyzer`) applied, Rule-10 re-audited, and defect-fixed same session.
- omnigent confirmed as the Databricks meta-harness; five of run-2's seven links resolved by dedup alone.

## Session 129 — 2026-06-22 — model-capability research + agentic-OS direction (e471499…02d5e76, committed 2026-07-11)

- Model capability research: registry created, 5 findings, 6 sources, 3 new sub-dimensions.
- The agent-vs-skill thread opened into the agentic-OS thesis: formalize the engine toward a harness layer that audits, specifies, and creates whole agentic systems, governance-first. Captured in `project-management/design-notes/2026-06-22-agentic-os-direction.md`.
- Logged-for-future #1 (put the engine on a real harness) promoted to the active spine; the narrow DD-109 fold put on hold.

## Session 128 — 2026-06-22 — upstream YAML prevention + FOUNDATIONS spine + PROGRESS consolidation (4ce12d9…dafd313)

- DD-114: block-scalar authoring convention added to the 7 frontmatter producers; new `validate_frontmatter.py` + git pre-commit hook; `kb_parser` verified load-bearing.
- DD-115: `governance/FOUNDATIONS.md` generated spine map of ~20 foundational DDs — `foundational: true` tags, `generate_foundations.py` (+`--check`), CLAUDE.md pointers, pre-commit staleness check, inclusion/exclusion criteria codified.
- The ~2-months-stale `il-published` subtree mirror (DD-84) refreshed via `git subtree push`.
- Vestigial root PROGRESS.md reduced to a pointer; the IL file made the single canonical PROGRESS; `/session-handoff` patched to target it.

## Session 127 — 2026-06-21 — sweep residuals + frontmatter/YAML hygiene sweep (011fa8c…a58a55b)

- DD-113: DD↔IB linkage made forward-only via `source_dd` — uniform YAML list across 63 IBs, 4 non-lossy reconciliations, `ib_items` removed from 81 DDs, schema + `/dd`/`/track`/`/governance-audit` repointed.
- Harness whole-system invariants confirmed deferred per Rule 11 (evidence test unmet; dated note in `harness.md`).
- Full-corpus PyYAML scan found 40 parse failures (3 classes); a field-aware fixer rewrote only the offending field per file; 0 failures remain; 4 findings backfilled `pipeline_status: raw`.

## Session 126 — 2026-06-21 — knowledge-architecture sweep (867e2a7…7394329)

- DD-37's five principles cached into `governance/agent-rules.md`; `principles.md` → `dbdo-pipeline.md` (re-anchored DD-45→DD-103, de-federated).
- DD-111: `extracts/guides` + `extracts/patterns` recognized as Librarian substrate; the residue (~123 files) designated an explicit harvest archive (no moves/deletes).
- DD-112 + IB-170 resolved: concept-doc home rule (`knowledge/reference/` = self-knowledge; `operations/references/` = operational reference); `harness.md` relocated; runtime-sense → `runtime-environment.md`.
- `ib_items` normalized (YAML list; DD-43's 9 dead URLs → real back-refs).

## Session 125 — 2026-06-21 — governance health + DD-wisdom caching policy (b113c8d…68839f1)

- Phase 1: DD/IB corpus verified structurally sound — no contradictions, all 9 supersessions machine-traceable, live-era DDs commit-backed; four gated hygiene fixes applied.
- Phase 2 (propose-only): the caching question resolved — ~88% of DD wisdom correctly not separately cached; four-part selection test + exclusion rules + anti-redundancy invariant delivered; no cache-every-DD mechanism (Rule 11).
- Reports: `operations/system-audits/2026-06-21-governance-health-audit.md`, `project-management/design-notes/2026-06-21-dd-wisdom-caching-policy.md`.

## Session 124 — 2026-06-20 — concept-doc reorg + drift fixes (d19eb1b…bee26da)

- household-os reference subtree archived post-collapse (DD-103/DD-106).
- Drift fixed in the research-to-codification-pipeline guide; skill-authoring-guide slimmed to a SKILL.md mechanics reference.
- Design note: `extracts/` ↔ `knowledge/` reconciliation (live-vs-orphaned audit).

## Session 123 — 2026-06-19 — governance hygiene + audit-home disambiguation (2dd1b2f…024db67)

- Stale-IB sweep cleared 15 post-collapse items; open backlog left small and engine-relevant.
- DD-110 (resolves IB-169): the two audits disambiguated, not consolidated — `/audit-artifacts` (renamed from `/audit-system`) vs `/system-audit`, both homes moved under `operations/`.
- Post-collapse "MetaSystem vs IL" framing reconciled to the one-engine three-altitude model; the two consumer-abstractions maps merged; IB-170 filed.

## Session 122 — 2026-06-18 — Phase 2 items 2–3 + first post-collapse /system-audit (72af64c…b1e7585)

- Phase 2 item 2: Dimension 7/9 → schematic re-evaluation wiring made explicit; schematics added as a `/solicit-proposals` reflection input.
- Phase 2 item 3: two consumer-facing seed schematics (`project-coding-workcell`, `scheduled-operations-assistant`) — library at 4 seeds, `/detect-drift` clean.
- First full `/system-audit` post-collapse: 0 Critical, structurally sound; all findings remediated same session — DD-108 (Owner files DDs as mechanics; Nick gates content), DD-109 (re-home skills governance), agent + skill contract fixes, 148 system-log entries normalized to canonical `date:`.
- Report: `operations/audit-reports/2026-06-18-system-audit.md`. IB-169 filed.

## Session 121 — 2026-06-18 — schematics into drift detection; collapse merged to main (9416655…33139fc)

- Phase 2 Slice 2: schematics brought into `/detect-drift`.
- `engine-collapse-phase-1` merged `--no-ff` (199a6ee), pushed to origin/main, branch deleted — main became the live line.

## Session 120 — 2026-06-18 — post-Phase-1 cleanup + schematic form (dafc99d…068681d)

- Step 9: research-to-codification guide reframed to in-engine reality; `target_system` vocabulary collapsed to improvement-loop; post-collapse priority queue seeded.
- Phase 2 Slice 1: schematic artifact form defined (DD-107); first two seed schematics (`research-scanning-agent`, `codebase-audit-workcell`).

## Session 119 — 2026-06-18 — engine collapse Phase 1 finish (7443d17…e81248f)

- Steps 6–8: the two Owners merged (symlink deleted); the `meta-system` shell dissolved into `archive/`; governance reset — DD-103 architecture reset + DD-104/105/106.
- Phase-1 verification: residual moved-path references and relative-path/identity drift cleared from live config.

## Session 118 — 2026-06-18 — engine collapse Steps 4–5 (feb130f…eda5962)

- `CHARTER.md` authored; design-wisdom demoted to engine knowledge.
- PM data merged into the engine + Semantic Rewrite #2 (routing).

## Session 117 — 2026-06-18 — engine collapse Steps 1–3 (2aec0c2…be2337c)

- Accumulated sessions 106–116 work committed as the pre-restructure baseline (2aec0c2).
- Steps 1–3: transcript-fetcher + pdf-to-markdown relocated into the engine; dormant systems archived (Household OS Notion substrate lifted into engine knowledge); knowledge moved into the engine + Semantic Rewrite #1 (deploy target).

## Sessions 87–116 — May–Jun 2026 — Owner stewardship & pre-collapse era (802b77d…aa7bf1d; sessions 106–116 landed via baseline 2aec0c2)

- Owner-led maintenance: visualization brainstorm artifacts, handoff-protocol drift cleanup, no-hardcoded-counts sweep, DD navigability backfill, guide cross-refs.
- Link intake from LINKS.md (session 89 handoff); logged-for-future resolutions; Codifier artifact batches + Owner health check; Owner agent skill build.
- Sessions 106–116 accumulated uncommitted and were committed wholesale as the 2026-06-18 baseline immediately before the engine-collapse restructure.

## Sessions 45–86 — Apr–May 2026 — Librarian layer & lifecycle era (26d627b…7162382)

- Librarian reference layer + four-zone architecture; IL reflections architecture; `_index.md` cleanup sweep (49 → 22 files).
- DD-92 ContextSpec + `/extract-artifacts`; lifecycle-spec DDs 93–101 ratified and executed (IB-154 → IB-164); `/detect-drift` shipped and smoke-tested.
- Guide re-syntheses under live validation: G7 (14→27 findings), G2 (26→44), G9 (10→16); G11 initial synthesis (Agentic Systems theme graduation, 29 findings absorbed).
- IB-153 dimension rebalance (Memory Architecture retired, 41→0); 38 harvest-queue rows ruled; 28 artifacts extracted across rules/skills/templates; subagent queue-mutation discipline ruling; Codifier calibration reflection.

## Sessions 33–44 — Apr 2026 — KB pipeline & triage era (597433d…ff4390f)

- Batch repo analyses (beads, OpenViking, sandbox, deer-flow, OB1); cross-repo comparison grown to 15 repos.
- KB health cleanup: YAML normalization across 457 findings; null-priority triage of 192 findings across 12 categories; isolate crosslinking (88 → 48).
- Research-loop batches 1–2 over YouTube sources (transcript fetcher gained Playwright + yt-dlp backends); DD-87 added Agentic OS as Dimension 11.
- Codifier identification/extraction cycles began; `proposer_priority` → `priority` rename (DD-80 drift cleanup); DD-88 superseded DD-72.

## Sessions 1–32 — Apr 2026 — founding & federation era (a6e278b…7a87347)

- MetaSystem vault initialized as a three-system federation: meta-system governance layer, Improvement Loop core (agents, skills, research KB, operations), incubator systems (Household OS, Claude Build), cross-system Claude Code config.
- Owner agent pattern established + 5 Owner skills built; IL governance translations made self-sufficient (`_governance/` snapshot removed).
- PROGRESS.md compressed 620 → 161 lines; session detail moved to handoffs.
