# Getting Started: Your First Skill in 30 Minutes

**Purpose:** The fastest correct path from "I have a task I keep doing with AI" to "I have a validated, triggering skill." This is the on-ramp; `SKILL.md` is the full reference. Follow the clock — each step has a budget and a single artifact you should have at the end of it. If you blow a budget, that step is telling you something (noted under each).

**Before you start, one 60-second check.** Open `SKILL.md` §0.5 ("Is a skill the right primitive?"). If your task is a one-shot the base model already nails, a fully deterministic transform, an autonomous agent, or just an external API call — stop here and use the simpler primitive [skill-as-new-employee-mental-model]. A skill is for *reusable, tacit, multi-step expertise that should trigger by description*. Still a skill? Continue.

---

## The clock

| Time | Step | You end with |
|------|------|--------------|
| 0–5 min | 1. Pick one real task | A task you've actually done with AI |
| 5–15 min | 2. Elicit the tacit knowledge | A short notes file of how you really do it |
| 15–25 min | 3. Draft `SKILL.md` from the skeleton | A frontmatter + body draft |
| 25–28 min | 4. Validate (structural) | `validate.sh` exit 0 |
| 28–30 min | 5. Trigger gate (the one you can't skip) | A 6-query trigger spot-check |

Total: 30 minutes to a draft you can iterate on. Promotion to "stable" comes later via the full sequence — this gets you a *real, validated draft*, not a toy.

---

## Step 1 — Pick one real task (5 min)

Choose **one** task you have already completed successfully with an AI and that took real effort — judgment, iteration, or knowledge the model didn't have by default. Not a hypothetical; a task with a known good outcome you can distill from. This single-task-first approach is the Anthropic-endorsed default, and it works because authors systematically guess wrong when they specify upfront [iterate-on-single-task-then-extract-skill].

**Budget warning:** If you can't name a concrete past task in 5 minutes, you don't yet have a skill — you have an idea. Go do the task once with AI first, *then* come back.

---

## Step 2 — Elicit the tacit knowledge (10 min)

Open a scratch file. Answer these five prompts about how you *actually* do the task — fast, bullet points, no polish. This surfaces the judgment that has compiled into automatic expertise you'd otherwise leave out [tacit-knowledge-as-agent-delegation-barrier]:

1. **Trigger** — When does this task run? What kicks it off?
2. **Recurring decisions** — What judgment calls do you make every time?
3. **Required inputs** — What must be present for it to succeed?
4. **Friction points** — Where does it break? What error recurs?
5. **Done** — How do you know it's correct?

> Expertise "compiles" from explicit steps into automatic judgment; even structured interviews can't fully surface it — so write down the friction points especially, those are the parts you'll forget to encode. [tacit-knowledge-as-agent-delegation-barrier]

**Budget warning:** Going over 10 minutes usually means the task is really two tasks. Split it; author the smaller one first.

---

## Step 3 — Draft `SKILL.md` from the skeleton (10 min)

Copy `templates/skill-md-skeleton.md` into your skill directory and fill it in. Two parts matter most:

**Frontmatter (do this carefully — it's the highest-leverage part):**
- `name`: 1–64 chars, lowercase `[a-z0-9-]`, matches the directory name [skill-frontmatter-validation-rules].
- `description`: ≤ 1024 chars, structured as **what it does + when to use it + what it can do**, with the key use case *first*. The description is the only thing the model sees before deciding to load the skill — a perfect body that never triggers is dead capability [skill-md-frontmatter-as-discovery-trigger-primitive][skill-description-structure-what-when-capabilities].

**Body (translate your Step 2 notes):**
- Keep it under 500 lines and put the critical content first [skill-as-directory-progressive-disclosure-three-levels].
- Reference long material with relative paths to `references/` — point, don't paste [pointers-over-copies-in-context-files].
- **Do not** add "think step by step," few-shot examples, or decomposition scaffolding — these degrade frontier reasoning models [reasoning-model-anti-pattern-prescribed-reasoning].
- When you write a rule, write *why* beside it — not a bare ALL-CAPS MUST [skill-authoring-explain-the-why-not-musts].
- If your task includes a deterministic step (parsing, math, formatting), put it in a script and call it — don't ask the model to simulate determinism [code-as-deterministic-tool-inside-skills].

New here? Read `examples/design-walkthrough.md` alongside this step — it shows exactly this draft happening end to end.

---

## Step 4 — Validate, structurally (3 min)

```bash
bash scripts/validate.sh ./your-skill-dir
```

Exit `0` = pass (advisory warnings are fine). Exit `1` = fix the listed structural errors and re-run [bmad-deterministic-skill-validator]. This is Level 1 only — it proves the skill is well-formed, not that it behaves well. Behavioral quality comes from the audit later, run in a separate context [generator-assessor-separation-in-skill-iteration].

Quick smell pass: skim `references/skill-smells.md` against your draft. Any Category E (safety) smell blocks shipping; three smells across categories means iterate before you trust it.

---

## Step 5 — The trigger gate you can't skip (2 min)

A skill that doesn't fire reliably is worthless no matter how good the body is. Do a fast spot-check now (the full 20-query loop in `templates/eval-query-set.md` comes later):

- Write **3 queries that should trigger** this skill (realistic, specific — real file names, real phrasing, not "do the thing").
- Write **3 near-misses that should NOT trigger** it (share keywords, but actually need something else).
- Run them. If a should-trigger query misses, or a near-miss fires, revise the **description** — not the body — and re-check [skill-description-optimization-loop-held-out-test].

> Realistic, specific queries are the whole game here. "Format this data" is a bad eval query; "reformat this Stripe payout CSV into our finance template" is a good one. [skill-description-optimization-loop-held-out-test]

---

## You now have

A validated, triggering skill **draft**. That's the milestone. To take it to stable:

| Next | Where |
|------|-------|
| Run the full description optimization loop (20 queries, 60/40 split, ≤5 iterations) | `templates/eval-query-set.md` + `references/decision-sequence.md` Step 5 |
| Audit across the four-discipline rubric in a separate context | `references/audit-rubric.md` (Eval mode, `SKILL.md` §2) |
| Add side-effect / autonomy gating if the skill commits, sends, or deletes | `references/safety-gates.md` |
| Put it under version control and into CI | `references/git-integration.md` |
| Port it to another platform | `SKILL.md` §4 + `adapters/` |

Two rules carry forward: **author never grades their own skill in the same context** [generator-assessor-separation-in-skill-iteration], and **one logical change at a time, eval after each** [claude-code-skills-20-four-mode-skill-lifecycle-wi].

---

*This on-ramp compresses the Design-mode sequence in `references/decision-sequence.md`. Every rule it states cites the same finding the full sequence does — nothing here is a shortcut around a gate, only a faster path to the first draft.*
