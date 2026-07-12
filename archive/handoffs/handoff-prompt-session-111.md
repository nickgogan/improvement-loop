# Session 111 Handoff — Stream B Step E: Hoist Librarian to First-Class IL Skills (`/ask-kb`, `/compare-repos`)

## IDENTITY AND SOUL

You are operating in the **Improvement Loop** subsystem of MetaSystem, with the **Researcher** disposition as your default working stance and the **Owner** disposition activated for gate decisions (skill ownership, scope shape, governance edits). Read `systems/improvement-loop/agents/researcher/agent.md` and `systems/improvement-loop/agents/owner/agent.md` before starting; the disposition tables in IL `CLAUDE.md` tell you when to switch.

**Working relationship with Nick:** he gives strategic direction; you execute with high autonomy and present structured options with tradeoffs. Evidence-first. Source-grounded. Concise, no filler. You do not invent abstractions to fill symmetry; rule 11 ("abstractions must earn their keep") is the standing bar. You do not collapse generator and assessor in one context; rule 10 is the standing rule.

**Project context:** MetaSystem is an Obsidian-vault governing layer above two graduated systems — Improvement Loop (research engine + Librarian advisory layer for agentic abstractions) and Meta-System (harness builder consuming IL substrate). Session 110 closed cross-system roadmap step D: `/design-skill` and `/design-agent` authored under Librarian ownership, composing `design.md × <concept>.md` and delegating Phase 5 audit to `/assess-*` peers via fresh-context subagent invocation. Existing §Construction substrate sufficed — no concept-doc edits triggered. Step E is the next cross-system surface: hoisting the Librarian's conversational KB-consumption and cross-repo-comparison behaviors into first-class IL skills.

## YOUR TASK

Execute cross-system roadmap step E — build `/ask-kb` and `/compare-repos` as first-class IL skills, both under Librarian ownership (pre-decided per session 110 PROGRESS.md update and Librarian agent.md "Future skill candidates"). Build **both** in one session; persona is **same as session 110**; **strict step E focus** (no deferred items revisited).

**Two key open decisions** to propose with rationale, then gate with Nick:

1. **Concept-doc treatment.** `/design-skill` and `/design-agent` are bilingual readings of `skill.md` and `agent.md` concept docs. `/ask-kb` and `/compare-repos` have no concept-doc peer today. Propose whether they need new concept docs in `operations/references/librarian/` (e.g., `kb-query.md`, `repo-comparison.md`) or whether they operationalize the Librarian's existing conversational behavior without a substrate layer. Rule 11 is the gate: don't invent concept docs to fill symmetry. Lead with evidence from how the existing Librarian Teacher/Builder modes already cover the surface.

2. **Generator-assessor separation applicability (rule 10).** `/ask-kb` is read-only consumption — there is no "draft" to assess; rule 10 may not apply the same way it does for `/design-*`. `/compare-repos` likewise produces analytical reports, not constructed artifacts. Propose whether either skill needs an assessor peer at all, or whether rule 10 only fires on constructive operations. State the proposed answer before authoring.

After both decisions are gated, proceed with the skill authoring:

- `/ask-kb` operationalizes the Librarian's Teacher and Builder modes as a callable skill. Reads findings, guides, watched-libraries, authorities. Output is narrative/structured per query type (Teacher → synthesis; Builder → ordered recommendation set).
- `/compare-repos` operationalizes cross-repo comparison across watched libraries. Today `/repo-analyzer --compare` does some of this; `/compare-repos` is the dedicated first-class surface. Decide whether to deprecate `--compare` mode or keep both.

Leverage the existing assess-* and design-* skills as **structural reference** for shape (frontmatter, paths, procedure phases, boundary-case encounter logging, cross-references). Do not copy their bilingual concept-doc pattern blindly — see decision 1.

## RULES

- **Tier:** Standard-tier for the skills themselves once ownership is gated. New concept docs (if proposed) are Proposal-First tier per rule 11 — they need evidence justifying the abstraction.
- **Rule 11 (abstractions earn their keep).** Concept docs are abstractions. The bar for `kb-query.md` or `repo-comparison.md` is recurring concrete need observed 2–3+ times, not symmetry with `skill.md` and `agent.md`.
- **Rule 10 (generator-assessor separation).** Applies to constructive operations. If you propose an assessor peer for `/ask-kb` or `/compare-repos`, justify why the operation is constructive enough to need the epistemic gap.
- **Rule 12 (audit/design symmetry).** Only fires if you author or extend a concept doc. If `/ask-kb` and `/compare-repos` land without concept docs, rule 12 is non-applicable for this session.
- **Read-before-acting.** Read IL `CLAUDE.md`, both agent definitions (Researcher + Owner + Librarian), rules 10/11/12, the existing `/repo-analyzer` SKILL.md, and the librarian conversation patterns in `agents/librarian/agent.md` (Teacher/Builder modes) before drafting.
- **Out of scope (do not do):**
  - Step F (MetaSystem Owner instantiation IB-167) — pending step E.
  - Step G (MetaSystem capability builds `/audit-system`, `/design-harness`) — pending step F.
  - §Construction backfill for any concept doc — Nick gates per priority queue item 2.
  - `/identify-artifacts` or `/extract-artifacts` runs against session 109 findings — Nick gates separately.
  - Promotion of rules 10/11 to MetaSystem constitution — Nick deferred this session.
  - No DD creation unilaterally. If the design surfaces a DD candidate, draft for Nick to gate.

## KEY REFERENCES

| Entity | Path |
|---|---|
| IL CLAUDE.md (Purpose + agents + dispositions + Librarian skills) | `systems/improvement-loop/CLAUDE.md` |
| Workspace PROGRESS.md (cross-system roadmap) | `PROGRESS.md` |
| IL PROGRESS.md | `systems/improvement-loop/PROGRESS.md` |
| IL governance rules 10, 11, 12 | `systems/improvement-loop/governance/agent-rules.md` |
| Researcher agent definition | `systems/improvement-loop/agents/researcher/agent.md` |
| Owner agent definition | `systems/improvement-loop/agents/owner/agent.md` |
| Librarian agent definition (Teacher/Builder modes; updated session 110) | `systems/improvement-loop/agents/librarian/agent.md` |
| Existing `/design-skill` (structural reference) | `systems/improvement-loop/.claude/skills/design-skill/SKILL.md` |
| Existing `/design-agent` (structural reference) | `systems/improvement-loop/.claude/skills/design-agent/SKILL.md` |
| Existing `/assess-skill` (structural reference) | `systems/improvement-loop/.claude/skills/assess-skill/SKILL.md` |
| Existing `/repo-analyzer` (incumbent that may overlap with `/compare-repos`) | `systems/improvement-loop/.claude/skills/repo-analyzer/SKILL.md` |
| Existing Librarian reference layer | `systems/improvement-loop/operations/references/librarian/` (audit.md, design.md, skill.md, agent.md, harness.md, memory.md, context-rot.md, agentic-systems.md, second-brain.md, prompt.md) |
| Consumer abstractions map (demand-gated promotion) | `systems/improvement-loop/operations/references/consumer-abstractions-map.md` |
| Session 110 SL entry | `systems/improvement-loop/operations/system-log/il-stream-0-step-d-design-skill-design-agent-authored.md` |
| Watched libraries (input to `/compare-repos`) | `systems/improvement-loop/watched-libraries/` |
| Research dimensions registry | `systems/improvement-loop/operations/references/research-dimensions.md` |

## CONTEXT FROM PRIOR SESSION

### Resolved (session 110)

- `/design-skill` and `/design-agent` authored under Librarian ownership (Nick gated). Both compose `design.md × <concept>.md`. Phase 5 delegates audit to `/assess-skill` and `/assess-agent` via fresh-context Agent subagent invocation. Hard gates honored: safety-critical classification (`/design-skill` step 4); variant selection + autonomy-envelope sizing + G9.I6 (`/design-agent`).
- §Construction backfill deferred (Nick gated): existing skill.md and agent.md §Construction from session 107 sufficed; no rule-12 symmetric review triggered. Validates rule-11 stance on the deferred backfill candidates.
- Librarian skill-inventory drift fixed in IL `CLAUDE.md` and `agents/librarian/agent.md` — both now list the actual deployed skills.
- Workspace + IL PROGRESS.md updated: step D → Done, step E → In progress (next session 111).
- SL entry filed: `il-stream-0-step-d-design-skill-design-agent-authored.md`.

### Unresolved (for session 111)

1. **Concept-doc treatment for `/ask-kb` and `/compare-repos`** — propose with rule 11 evidence; Nick gates.
2. **Rule 10 applicability** — propose whether either skill needs an assessor peer; Nick gates.
3. **`/compare-repos` vs `/repo-analyzer --compare`** — propose whether to deprecate the `--compare` mode or keep both; Nick gates.

### Deferred (do not act on)

- Step F (MetaSystem Owner instantiation IB-167) and step G (MetaSystem capability builds) — pending step E.
- §Construction backfill for `skill.md`, `harness.md`, `prompt.md`, `context-rot.md`, `agent.md`, `memory.md`, `agentic-systems.md`, `second-brain.md` — Nick gates per priority queue item 2.
- Rules 10 and 11 promotion to MetaSystem constitution — waiting on Nick's trigger condition.
- `/identify-artifacts` and `/extract-artifacts` against session 109 findings.

### Nick's standing constraints (do not relitigate)

- **Occam's razor** — minimum viable abstraction; ship smaller first.
- **Rule 11** — abstractions must earn their keep; recurring concrete problem (2-3+) required.
- **Rule 10** — generator-assessor separation for constructive skills with quality checks.
- **Plain English first** — lead with "why it matters for us"; jargon second.
- **Positive-space governance** — don't codify rejection lists.

## SESSION 110 TELEMETRY

```yaml
model: claude-opus-4-7[1m]
tokens_consumed: unknown
context_window_size: 1000000
context_window_pct_peak: unknown
turns: ~7
tool_calls: ~25
subagents: 0
capture_quality: estimated
harness: claude-code-cli-cursor-macos
```

## OUTPUT REQUIREMENTS

At end of session 111:

- Concept-doc-treatment decision proposed, gated with Nick, and recorded in PROGRESS.md.
- Rule 10 applicability decision proposed, gated with Nick, and recorded in PROGRESS.md.
- `/compare-repos` vs `/repo-analyzer --compare` disposition proposed, gated, and recorded.
- `/ask-kb` and `/compare-repos` skills authored under `systems/improvement-loop/.claude/skills/` per Librarian ownership.
- If new concept docs proposed and accepted, written to `operations/references/librarian/` with §Composition (and §Construction if rule 12 fires).
- Workspace `PROGRESS.md`: step E → "Done"; step F → "In progress (next session 112)".
- IL `PROGRESS.md`: Current Focus updated to step F.
- IL `CLAUDE.md` Librarian Skills table updated to list `/ask-kb` and `/compare-repos` (drift-prevention from session 110 pattern).
- `agents/librarian/agent.md` Skill Inventory updated (same drift-prevention).
- SL entry recording step E completion (skills authored, decisions made, concept-doc treatment, rule-10 disposition, /repo-analyzer disposition).
- Invoke `/session-handoff` for session 112 (target: roadmap step F — MetaSystem Owner instantiation IB-167).
