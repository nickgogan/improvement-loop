# Co-occurrence Harvest Queue — Writing Agent Specifications

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

> Ruled 2026-07-13 (session 146) under Nick's delegated-judgment grant; per-row statuses set accordingly.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-13 | extracted | template | [[plans-that-carry-their-own-contract]] | "plan-carried-contract-blocks" | extracted to [[plan-carried-contract-blocks]] |
| 2026-07-13 | extracted | template | [[war-game-plan-format-for-executor-handoff]] | "war-game-plan-scaffold" | extracted to [[war-game-plan-scaffold]] |
| 2026-07-13 | extracted | skill | [[human-ai-seam-identification-three-question-rubric]] | "seam-map-delegation-rubric" | extracted to [[seam-map-delegation-rubric]] |
| 2026-07-13 | nick-dismissed | rule | [[role-registry-prompt-hook-routing-backstop]] | "fail-open-routing-hook-invariants" | dismissed |

## Per-row details

### plans-that-carry-their-own-contract::template::plan-carried-contract-blocks

- **Date queued:** 2026-07-13
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[plans-that-carry-their-own-contract]]
- **Source excerpt:**
  > "1. **Global Constraints header.** Project-wide requirements are copied *verbatim* from the spec into a mandatory plan header block...
  > 2. **Per-task Interfaces block.** Each task declares Consumes and Produces with exact signatures...
  > BMAD's sealed file contracts are the same move at the spec boundary: frontmatter `companions:`/`sources:` manifests declare what downstream must and must not read, with stable IDs (CAP-N, AD-n) that survive updates."
- **Codifier's reading:** The Global Constraints header, Interfaces block, and sealed-frontmatter manifest are structural scaffolds meant for rendering with fillable slots — template form per the rubric (structural form, placeholder fields). This is the exact co-occurrence flagged in the 2026-07-13 identification report (candidate #4).
- **Suggested headline:** plan-carried-contract-blocks
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[plan-carried-contract-blocks]]

Extracted 2026-07-13 — Session 146 — [[writing-agent-specifications.harvest-queue]] — to [[plan-carried-contract-blocks]].

### war-game-plan-format-for-executor-handoff::template::war-game-plan-scaffold

- **Date queued:** 2026-07-13
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[war-game-plan-format-for-executor-handoff]]
- **Source excerpt:**
  > "Required elements per move: expected observation if it worked, expected observation if it didn't, most-likely failure with its signals, and the countermove. Every fork carries a trigger condition. Unresolvable assumptions are flagged to a blocked-variables ledger... The document terminates with abort conditions... Demonstrated workflow: tasks/ + wargames/ folders, success.md criteria file, ledger.md"
- **Codifier's reading:** A fixed per-move field set plus mandatory ledger and abort-condition sections is a structural scaffold with named slots — template form. The finding's own Potential Improvements says "standardize the ledger/abort-condition sections as a template." (This guide's Plan Handoff Contract template absorbs a merged variant; a standalone war-game template with the authoring prompt is the residual candidate.)
- **Suggested headline:** war-game-plan-scaffold
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[war-game-plan-scaffold]]
### human-ai-seam-identification-three-question-rubric::skill::seam-map-delegation-rubric

- **Date queued:** 2026-07-13
- **Status:** extracted
- **Target form:** skill
- **Source finding:** [[human-ai-seam-identification-three-question-rubric]]
- **Source excerpt:**
  > "walk the three questions, and return a seam map — human-owned parts, AI-owned parts, joint parts — rather than a yes/no on automation... Ruled framing from the wave-3 gate: extract as a Librarian advisory capability... fold the three questions into the Librarian's design-mode intake and the Phase 4 interview script."
- **Codifier's reading:** Defined input (candidate workflow), ordered question procedure, defined output (seam map) — skill shape. The finding's implementation_notes carry Nick's ruled framing that this becomes a Librarian advisory capability, i.e., a procedure to fold into design-mode intake, not just guide prose.
- **Suggested headline:** seam-map-delegation-rubric
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[seam-map-delegation-rubric]]

Extracted 2026-07-13 — Session 146 — [[writing-agent-specifications.harvest-queue]] — to [[seam-map-delegation-rubric]].

### role-registry-prompt-hook-routing-backstop::rule::fail-open-routing-hook-invariants

- **Date queued:** 2026-07-13
- **Status:** nick-dismissed
- **Target form:** rule
- **Source finding:** [[role-registry-prompt-hook-routing-backstop]]
- **Source excerpt:**
  > "Design details worth keeping verbatim: whole-word matching over substring (substring fires on incidental hits and injects noise), gate-not-ranking semantics (inject only above threshold, never a best-effort guess), and always-exit-0 fail-open (a routing aid must never become an availability risk)."
- **Codifier's reading:** Three imperative, machine-enforceable directives ("always exit 0", "never block a prompt", "inject only above threshold") — rule shape. Recommended dismiss-as-inline because the invariants only bind once the engine adopts a routing hook (P2 Design Required; no enforcement surface exists yet); re-queue at adoption time.
- **Suggested headline:** fail-open-routing-hook-invariants
- **Recommendation:** dismiss as inline
- **Resolution:** dismissed
