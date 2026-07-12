# Comparator subagent — blind A/B between two skill versions

Canonical Comparator role for §3.1. Decides **which of two skill versions is better** on
the same eval cases, blind to which is newer, to defeat positional and recency bias
[generator-assessor-separation-in-skill-iteration]. It reports the winner per criterion and
overall; it does **not** explain *why* — that is the Analyzer's job (`analyzer.md`), kept
separate so "which won" never contaminates "why."

## How to invoke

Before spawning, the caller randomizes which version is labelled **A** and which is **B**
and records the mapping privately (do not pass it to the comparator). Spawn a read-only
subagent in a fresh context and paste the prompt below.

## Comparator prompt (paste, fill placeholders)

```
You are an INDEPENDENT COMPARATOR. Two versions of the same skill are provided as A and B.
You do NOT know which is older or newer; do not guess or infer it. Evaluate only — do not
modify files. Thoroughness: thorough.

AUTHORITATIVE RUBRIC + EVAL CASES:
- <REPO>/systems/improvement-loop/.claude/skills/meta-skill-author/references/audit-rubric.md
- <EVAL_CASES_PATH>   (the binary capability assertions both versions must satisfy)

VERSION A:
- <PATH_TO_VERSION_A>   (SKILL.md + its templates/references)
VERSION B:
- <PATH_TO_VERSION_B>

PROCEDURE (defeat positional bias):
1. Judge each version against the SAME criteria: the four-discipline rubric dimensions and
   every binary assertion in the eval cases.
2. Evaluate the criteria in BOTH orders (A-first and B-first) and only keep judgments that
   are stable across order. Flag any criterion whose verdict flips when order flips.
3. For each criterion, mark winner: A / B / tie, with a one-line cited reason.

PRODUCE:
- A per-criterion table: criterion | A | B | winner | evidence.
- Counts: criteria won by A, by B, tied; and any order-sensitive (unstable) criteria.
- OVERALL WINNER: A | B | tie — by criteria won, breaking ties toward fewer minimum-
  threshold failures on the rubric. State confidence (high/medium/low).
- Do NOT speculate about which is newer, and do NOT explain root causes — only judge.

Return the full comparison as your final message. Do not modify files.
```

## Notes

- Keep the A/B label mapping out of the comparator's context; reveal it only to the caller
  when interpreting the result.
- Order-sensitive criteria are a signal the two versions are near-equivalent on that axis;
  treat them as ties unless an Analyzer pass finds a real difference.
- A blind comparator plus a separate Analyzer mirrors the generator-assessor split one
  level up: judging and explaining are different jobs and must not share a context.
