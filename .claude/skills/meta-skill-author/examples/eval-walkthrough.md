# Worked Example — Eval Mode

> End-to-end demonstration of §2 Eval Mode: take a deliberately weak skill, run
> the four-discipline rubric in dependency order, and produce the enhancement
> handoff block the Improve mode acts on. Read `references/audit-rubric.md` alongside.

Illustrative, not authoritative. If this conflicts with `SKILL.md` or
`references/audit-rubric.md`, those win.

---

## The skill under audit (deliberately weak)

```yaml
---
name: pr-helper
description: Helps with PRs.
---
```

```markdown
## PR Helper

You MUST always write a great PR description. ALWAYS think step by step about
the changes. First, list every file. Then, for each file, explain it. Here is an
example: "This PR adds a button. The button is blue." Be thorough and never miss
anything. Always be helpful.
```

This skill has problems at every layer. We score in **dependency order** so a
context problem is not misdiagnosed as a craft problem
`[the-four-discipline-prompting-stack-nate-b-jones]`.

---

## Level 1 first — deterministic structural validation

Before any LLM review, run the deterministic validator
`[bmad-deterministic-skill-validator]`:

```bash
bash scripts/validate.sh ./pr-helper
```

Findings:
- **PASS** — `name` is valid (`pr-helper`, lowercase, no reserved words).
- **WARN** — description is 14 chars; far below useful, no trigger phrases, no
  "when to use." Structurally legal, semantically empty.
- **PASS** — file is `SKILL.md`, no absolute paths, no reserved words in body.

Level 1 passing is necessary but not sufficient — it cannot catch the semantic
problems below `[bmad-deterministic-skill-validator]`. Proceed to Level 2 with a
**separate Grader context**, never the author's `[generator-assessor-separation-in-skill-iteration]`.

---

## Four-discipline rubric (scored in order)

### 1. Prompt Craft — word-level instruction quality → **WEAK**

- Stacked ALL-CAPS MUST/ALWAYS without reasoning — a documented yellow flag;
  reframe with the WHY `[skill-authoring-explain-the-why-not-musts]`.
- Positive aspirations ("be thorough," "be helpful") instead of negative
  constraints, which collapse the output distribution more reliably
  `[negative-constraints-as-probabilistic-output-collapse]`.

### 2. Context Engineering — what the model can access → **WEAK**

- No declaration of authoritative inputs (the diff? the issue? the commit log?).
- Embeds an inline example ("blue button") instead of pointing to `references/`
  — pointers over copies `[skill-as-package-export-with-references]`. The inline
  example also adds context bloat that reduces success ~3% `[context-file-instruction-bloat-eth-zurich]`.

### 3. Intent Engineering — goals, identity, stop rules → **MISSING**

- No objective, no desired outcomes, no **Stop Rules** — the single most commonly
  omitted and most consequential intent component
  `[intent-engineering-framework-seven-part-agent-inten]`.
- No reversibility classification and no HITL tier; posting a PR comment is a
  side effect that needs an autonomy tier `[autonomy-gradient-not-binary-delegation]`.

### 4. Specification Engineering — structured constraints → **WEAK**

- "Think step by step" and the few-shot example are reasoning-model
  anti-patterns that degrade GPT-5.4 / Claude 4.6 / Gemini 3.1
  `[reasoning-model-anti-pattern-prescribed-reasoning]`.
- No verifiable acceptance criteria; "great PR description" is not testable.

Scoring in order is for **diagnosis**; the fix cycles back across layers — a
Specification change here will require revisiting Prompt Craft
`[four-discipline-prompt-evaluator]`.

---

## Enhancement Handoff Block (output of Eval, input to Improve)

> Hand this block to Improve mode (§3). The Grader produces it; the author does not
> self-grade `[generator-assessor-separation-in-skill-iteration]`.

```
SKILL: pr-helper
LEVEL 1: PASS (description WARN — empty)

PRIORITY FIXES (dependency order):
[Intent]   Add objective, 2–4 desired outcomes, and explicit Stop Rules.
           Classify "post PR comment" as Proposal-first HITL.
[Spec]     Remove "think step by step" + inline few-shot example
           (reasoning-model anti-patterns). Add verifiable acceptance
           criteria: "every changed file referenced; risk section present."
[Context]  Declare authoritative inputs (diff + linked issue). Move any
           example into references/ as a pointer, not inline.
[Craft]    Replace ALL-CAPS MUSTs with reasoned constraints; convert
           "be thorough" into negative constraints.

DESCRIPTION: rebuild via the 20-query optimization loop
           (templates/eval-query-set.md), select by TEST score.

RE-VALIDATE: Level 1 must re-pass; then re-score all four disciplines
           in a fresh Grader context.
```

---

## What this example demonstrates

- Level 1 deterministic checks run **before** any LLM scoring.
- The four disciplines are scored in dependency order to prevent misdiagnosis.
- A high rubric score never substitutes for empirical eval cases
  `[four-discipline-prompt-evaluator]`.
- Eval's deliverable is a structured handoff block, not prose feedback.
