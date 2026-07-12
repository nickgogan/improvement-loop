# Trigger eval — meta-skill-author

Distilled install-acceptance set (meta-skill-author §2.1/§6). Self-administer after
install: pose each query in a fresh context, record whether this skill activates,
compare against the expected verdict. Triggering is non-deterministic — re-run any
mismatch 3×; a persistent mismatch is a triggering-conformance failure (fix by
adapting the port's description via its platform profile, never by editing queries
to match observed behavior).

Generic by construction: phrasings are specific-but-fictional; no real user or
workspace facts. Verdicts: **trigger** (this skill must activate) · **abstain**
(it must not). Routing notes name the skill that should serve the query when the
receiving host has it installed.

## Should trigger (10)

| # | Query | Expected | Note |
|---|-------|----------|------|
| 1 | "Write a skill that formats SQL files on save" | trigger | canonical authoring ask |
| 2 | "Author a SKILL.md for our deploy-checklist workflow" | trigger | names the artifact |
| 3 | "Audit this skill — is the description going to trigger reliably?" | trigger | Eval mode |
| 4 | "Port the changelog-writer skill to Cursor" | trigger | Port mode, stage 2 |
| 5 | "Make this skill generic so it works outside our repo" | trigger | Port mode, stage 1 |
| 6 | "The summarizer skill never activates when I ask casually — optimize its description" | trigger | undertriggering complaint → §2.1 loop |
| 7 | "Evaluate this skill package against the four disciplines" | trigger | rubric vocabulary |
| 8 | "Create a new skill for triaging support tickets, spec first" | trigger | Design mode, spec-first |
| 9 | "Improve the report-builder skill — it keeps skipping its validation step" | trigger | Improve mode |
| 10 | "Package this skill so another team can install it" | trigger | §6 distribution |

## Should not trigger (10)

| # | Query | Expected | Note |
|---|-------|----------|------|
| 11 | "Improve my writing skills" | abstain | human skills, keyword-only overlap |
| 12 | "Which skills should I put on my resume?" | abstain | resume domain; routes to a resume skill where installed |
| 13 | "Make this email sound like me" | abstain | routes to profile-voice where installed |
| 14 | "Create a PRD for the plugin marketplace" | abstain | routes to ops-vision-to-plan where installed |
| 15 | "Why is the linter failing on this file?" | abstain | ordinary debugging |
| 16 | "Add a keyboard-shortcuts cheat sheet to the docs" | abstain | docs authoring |
| 17 | "Install the spreadsheet skill from the marketplace" | abstain | consumption/install, not authoring |
| 18 | "Do a handoff and note the skill work for next session" | abstain | routes to ops-session-handoff where installed |
| 19 | "What model are you running?" | abstain | trivia |
| 20 | "Skill issue lol — anyway, fix this null-pointer bug" | abstain | slang keyword, bug fix |
