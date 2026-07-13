#!/usr/bin/env python3
"""Deterministic checker for the self-improvement store (IB-176, design note §2).

Validates `operations/self/` — schema validity blocks the commit; threshold and
growth signals are advisory (printed, never blocking):

  Blocking (exit 1):
    - lessons.md entry headers match
      `## L-<seq> · YYYY-MM-DD · high|normal · open|promoted|declined|pruned`
    - required lesson fields present (Lesson, Owning surface, Source, Occurrences)
    - L-<seq> unique and ascending (append-only sanity)
    - `Q-<seq>` references in lesson Sources exist in query-log.md
    - query-log.md rows match the 6-column contract with a valid outcome
    - proposal-log.md headers match
      `## P-<seq> · YYYY-MM-DD · L-<seq> · applied|declined`, and referenced
      L-<seq> entries exist

  Advisory (exit 0):
    - PROMOTE flags: open lessons at threshold (normal ≥2 occurrences, high ≥1)
    - growth bound: >50 open lessons → gated pruning pass due

Usage: python3 store_check.py            # full check
       python3 store_check.py --status   # counts + flags only (skill status mode)
"""
import re
import sys
from pathlib import Path

SELF = Path(__file__).resolve().parent.parent / "self"
LESSON_HDR = re.compile(
    r"^## L-(\d+) · (\d{4}-\d{2}-\d{2}) · (high|normal) · (open|promoted|declined|pruned)\s*$"
)
PROPOSAL_HDR = re.compile(
    r"^## P-(\d+) · (\d{4}-\d{2}-\d{2}) · L-(\d+) · (applied|declined)\s*$"
)
QUERY_ROW = re.compile(r"^\|\s*Q-(\d+)\s*\|")
REQUIRED_FIELDS = ("**Lesson:**", "**Owning surface:**", "**Source:**", "**Occurrences:**")
OPEN_GROWTH_BOUND = 50


def split_entries(text, hdr_re):
    """Return [(match, body_lines)] for each `## `-headed entry, plus malformed headers."""
    entries, malformed = [], []
    current = None
    for line in text.splitlines():
        if line.startswith("## "):
            m = hdr_re.match(line)
            if m:
                current = (m, [])
                entries.append(current)
            elif not line.startswith("## Entries"):
                malformed.append(line)
                current = None
        elif current is not None:
            current[1].append(line)
    return entries, malformed


def check(status_only=False):
    errors, notices = [], []

    lessons_text = (SELF / "lessons.md").read_text(encoding="utf-8")
    query_text = (SELF / "query-log.md").read_text(encoding="utf-8")
    proposal_text = (SELF / "proposal-log.md").read_text(encoding="utf-8")

    # --- lessons.md ---
    lessons, malformed = split_entries(lessons_text, LESSON_HDR)
    for line in malformed:
        errors.append(f"lessons.md: malformed entry header: {line!r}")

    seqs, open_count = [], 0
    known_queries = {m.group(1) for line in query_text.splitlines() if (m := QUERY_ROW.match(line))}

    for m, body in lessons:
        seq, date, severity, status = m.group(1), m.group(2), m.group(3), m.group(4)
        seqs.append(int(seq))
        body_text = "\n".join(body)
        for field in REQUIRED_FIELDS:
            if field not in body_text:
                errors.append(f"lessons.md L-{seq}: missing required field {field}")
        for qref in re.findall(r"\bQ-(\d+)\b", body_text):
            if qref not in known_queries:
                errors.append(f"lessons.md L-{seq}: references Q-{qref}, not found in query-log.md")
        occ = re.search(r"\*\*Occurrences:\*\*\s*(.+)", body_text)
        n_occ = len(re.findall(r"\d{4}-\d{2}-\d{2}", occ.group(1))) if occ else 0
        if status == "open":
            open_count += 1
            if (severity == "normal" and n_occ >= 2) or (severity == "high" and n_occ >= 1):
                notices.append(f"PROMOTE: L-{seq} ({severity}, {n_occ} occurrence(s)) is at threshold")

    if seqs != sorted(seqs) or len(seqs) != len(set(seqs)):
        errors.append("lessons.md: L-<seq> values must be unique and ascending (append-only)")
    if open_count > OPEN_GROWTH_BOUND:
        notices.append(f"GROWTH: {open_count} open lessons (> {OPEN_GROWTH_BOUND}) — gated pruning pass due")

    # --- query-log.md ---
    q_seqs = []
    for line in query_text.splitlines():
        if line.startswith("| Q-") or QUERY_ROW.match(line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) != 6:
                errors.append(f"query-log.md: row must have 6 columns: {line!r}")
                continue
            q_seqs.append(int(cells[0].removeprefix("Q-")))
            if cells[5] not in ("served", "partial", "unserved"):
                errors.append(f"query-log.md {cells[0]}: outcome must be served|partial|unserved, got {cells[5]!r}")
    if q_seqs != sorted(q_seqs) or len(q_seqs) != len(set(q_seqs)):
        errors.append("query-log.md: Q-<seq> values must be unique and ascending (append-only)")

    # --- proposal-log.md ---
    proposals, malformed = split_entries(proposal_text, PROPOSAL_HDR)
    for line in malformed:
        errors.append(f"proposal-log.md: malformed entry header: {line!r}")
    known_lessons = {str(s) for s in seqs}
    for m, _body in proposals:
        if m.group(3) not in known_lessons:
            errors.append(f"proposal-log.md P-{m.group(1)}: references L-{m.group(3)}, not found in lessons.md")

    # --- report ---
    if status_only:
        print(f"lessons: {len(lessons)} total, {open_count} open · queries: {len(q_seqs)} · proposals: {len(proposals)}")
    for n in notices:
        print(f"store_check: {n}")
    if errors:
        print("store_check FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  ✗ {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(check(status_only="--status" in sys.argv[1:]))
