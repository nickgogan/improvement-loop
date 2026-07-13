#!/usr/bin/env python3
"""UserPromptSubmit capture hook — demand-ledger raw buffer (IB-176).

Appends one JSON line {ts, session_id, prompt} to the gitignored capture buffer
`operations/self/.query-capture.jsonl`. `/self-improve` scan mode distills the
buffer into `operations/self/query-log.md` rows and truncates it.

Harness contract: mechanical append, no LLM, no judgment — the first concrete
instance of the North-Star harness layer (harness-enforced, not agent-remembers).
Must never block or fail the prompt: every path exits 0.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

BUFFER = Path(__file__).resolve().parents[2] / "self" / ".query-capture.jsonl"

try:
    payload = json.load(sys.stdin)
    prompt = payload.get("prompt", "")
    if prompt.strip():
        line = {
            "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "session_id": payload.get("session_id", "unknown"),
            "prompt": prompt,
        }
        BUFFER.parent.mkdir(parents=True, exist_ok=True)
        with BUFFER.open("a", encoding="utf-8") as f:
            f.write(json.dumps(line, ensure_ascii=False) + "\n")
except Exception:
    pass  # capture must never interfere with the session

sys.exit(0)
