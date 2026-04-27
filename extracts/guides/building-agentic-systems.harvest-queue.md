# Co-occurrence Harvest Queue — Building Agentic Systems

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-04-27 | queued | rule | [[compounding-knowledge-loop-internal-data]] | "Compounding loops must encode outcomes, not just events" | extract via /extract-artifacts |
| 2026-04-27 | queued | rule | [[ai-managed-vault-separate-from-human-vault]] | "AI vault and human vault must be strictly separated" | extract via /extract-artifacts |
| 2026-04-27 | queued | rule | [[signal-capture-as-byproduct-of-work]] | "Knowledge capture must be a byproduct of work, not a separate act" | extract via /extract-artifacts |
| 2026-04-27 | queued | rule | [[five-pillar-agentic-os-framework]] | "Scheduled agent workflows require human checkpoint before publish" | extract via /extract-artifacts |
| 2026-04-27 | queued | rule | [[context-infrastructure-seven-level-maturity-model]] | "Reach L6 personally before attempting L7 (team OS)" | extract via /extract-artifacts |
| 2026-04-27 | queued | skill | [[time-window-proactive-agent-loop]] | "Time-window proactive agent loop" | extract via /extract-artifacts |
| 2026-04-27 | queued | template | [[obsidian-experiment-notes-personal-health-tracking]] | "Experiment note frontmatter schema" | extract via /extract-artifacts |

## Per-row details

### compounding-knowledge-loop-internal-data::rule::compounding-loops-must-encode-outcomes

- **Date queued:** 2026-04-27
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[compounding-knowledge-loop-internal-data]]
- **Source excerpt:**
  > "the loop only compounds when it encodes **outcomes**, not just events. A knowledge base records what happened. A world model — and by extension this pattern — must record: (1) what happened, (2) what was done about it, and (3) what resulted. Without element 3, month six looks like month one."
- **Codifier's reading:** Imperative directive, machine-enforceable as a structural check on session-log content (does each entry carry an `outcome` field?). Three-element invariant (event / action / result) is the rule body. Fits rule artifact form per the form-classification rubric — clear must-have, falsifiable invariant, applies as a precondition to any compounding-loop implementation.
- **Suggested headline:** compounding-loops-must-encode-outcomes
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### ai-managed-vault-separate-from-human-vault::rule::ai-and-human-vaults-must-be-separate

- **Date queued:** 2026-04-27
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[ai-managed-vault-separate-from-human-vault]]
- **Source excerpt:**
  > "**Human vault** — personal notes, hand-written thinking, curated knowledge. Never touched by the AI.
  > **AI vault** — all AI-generated content: content summaries, entity pages, project documentation, meeting notes, daily briefs. The human uses this vault read-only.
  > The separation enforces clean ownership: anything in the AI vault was written by the AI, and anything in the human vault was written by a human. No mixed provenance."
- **Codifier's reading:** Two-direction prohibition ("AI never writes human vault; human never writes AI vault") with explicit ownership invariant. Machine-enforceable via per-vault write-access controls or git pre-commit hooks. Fits rule artifact form; applies wherever AI-generated content accumulates alongside human-authored content.
- **Suggested headline:** ai-and-human-vaults-must-be-separate
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### signal-capture-as-byproduct-of-work::rule::capture-must-be-byproduct-of-work

- **Date queued:** 2026-04-27
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[signal-capture-as-byproduct-of-work]]
- **Source excerpt:**
  > "the system must capture signal as a natural byproduct of doing work, not as a separate documentation effort. If contributing to the knowledge system requires a distinct, extra step, the system will fail to accumulate the most valuable knowledge"
- **Codifier's reading:** Design-time directive applying to any tool/workflow choice in an agentic system. Falsifiable: for each capture path, ask "is this a byproduct of work or a separate act?" Reject the latter. Fits rule artifact form — applies as a precondition to ingestion-pattern adoption per Section 4 of the guide.
- **Suggested headline:** capture-must-be-byproduct-of-work
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### five-pillar-agentic-os-framework::rule::scheduled-workflows-require-human-checkpoint

- **Date queued:** 2026-04-27
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[five-pillar-agentic-os-framework]]
- **Source excerpt:**
  > "Critical learning: started fully autonomous but hit ~20% failure rate. Shifted to '80% automated + human checkpoint before publish.' File-based activation: active/inactive flags control which scheduled jobs run."
- **Codifier's reading:** Practitioner-validated threshold expressed as an imperative ("scheduled workflows must include a human checkpoint before publish"). Machine-enforceable as a structural check on scheduled-task definitions: does the task include an explicit human-gate step before any externally-visible side effect? Fits rule artifact form; aligns with DD-29's human-gate-at-every-stage invariant in MetaSystem.
- **Suggested headline:** scheduled-workflows-require-human-checkpoint
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### context-infrastructure-seven-level-maturity-model::rule::reach-l6-before-l7

- **Date queued:** 2026-04-27
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[context-infrastructure-seven-level-maturity-model]]
- **Source excerpt:**
  > "The business recommendation is to reach L6 personally before attempting L7."
- **Codifier's reading:** Sequencing rule for system maturity progression; falsifiable check at any L7 (team OS) rollout — was the operator's personal L6 cadence working before team sync was enabled? Failure mode (L7 before L6 → synchronization complexity multiplies before context quality is established) is documented in the same finding. Fits rule artifact form; applies as a precondition to L7 adoption decisions.
- **Suggested headline:** reach-l6-before-l7
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### time-window-proactive-agent-loop::skill::time-window-proactive-loop

- **Date queued:** 2026-04-27
- **Status:** queued
- **Target form:** skill
- **Source finding:** [[time-window-proactive-agent-loop]]
- **Source excerpt:**
  > "0. Date anchor — Establish exact date/time via `date` command or API response. Store as `anchor_date` and `anchor_time`. All date arithmetic is calculated from this anchor — never use vague terms like 'recently.'
  > 1. Time check — Classify current time into a window (early morning, pre-meeting, midday, late afternoon, evening).
  > 2. Duplicate check — Query the briefings table for entries already sent on `anchor_date`. Don't repeat.
  > 3. Decide — Based on time window, what should be delivered?
  > 4. External pull — Fetch live data (calendar events, weather, attendee lists).
  > 5. Internal enrich — Search the knowledge base for context on what was just found...
  > 6. Deliver — Send via channel tools (Telegram/Discord). Concise, mobile-friendly, bullet points. Silence is better than noise.
  > 7. Log — Record what was sent so the next cycle knows what's been covered."
- **Codifier's reading:** Fully-formed 8-step procedure with input/output contract (cron-driven invocation; output is a delivered briefing + log entry). Step structure, named state (anchor_date, briefings table), and a closed enum of briefing types (7 types) and time windows (5 windows) are all skill-shaped per the form-classification rubric. Could be extracted as a parameterized skill template installable per-domain (life-engine, work-engine, etc.).
- **Suggested headline:** time-window-proactive-loop
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### obsidian-experiment-notes-personal-health-tracking::template::experiment-note-frontmatter-schema

- **Date queued:** 2026-04-27
- **Status:** queued
- **Target form:** template
- **Source finding:** [[obsidian-experiment-notes-personal-health-tracking]]
- **Source excerpt:**
  > "**Frontmatter fields:** `type: experiment`, `status: in_progress/proposed/complete`, links to a health dashboard note
  > **Body sections:** Hypothesis (explicitly stated), Protocol (step-by-step...), Success Criteria (measurable...), Observations (filled daily)
  > **Data fields:** Numeric tracking (gym volume, sessions per week, mood 1-10, energy 1-10, sleep quality)..."
- **Codifier's reading:** Structural scaffold with named frontmatter fields, body section headings, and typed data fields — exactly template-shaped per the form-classification rubric. Could be extracted as `experiment.md` template with placeholders for {{HYPOTHESIS}}, {{PROTOCOL}}, {{SUCCESS_CRITERION}}, {{OBSERVATIONS}}, {{NUMERIC_TRACKED_FIELDS}}. Reusable across health, productivity, behavior-change, or any longitudinal-tracking domain.
- **Suggested headline:** experiment-note-frontmatter-schema
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**
