#!/usr/bin/env bash
set -euo pipefail

required_files=(
  "README.md"
  "AGENTS.md"
  "docs/spec.md"
  "docs/operating_loop.md"
  "docs/automation_steering.md"
  "docs/automation_prompt.md"
  "docs/research/2026-05-06-long-horizon-codex.md"
  "docs/research/2026-05-06-deep-agent-memory.md"
  "docs/useful_hour_scorecard.md"
  "docs/decision_log.md"
  "docs/heartbeat_synthesis.md"
  "docs/cadence_review.md"
  "docs/next_experiment_ladder.md"
  "docs/source_ledger.md"
  "docs/eval_summary_policy.md"
  "evals/long_codex_cycle_smoke.md"
  "evals/last_long_codex_cycle_smoke_summary.json"
  "evals/dead_end_avoidance_prompt.md"
  "evals/last_dead_end_avoidance_summary.json"
  "evals/queue_exhaustion_prompt.md"
  "evals/last_queue_exhaustion_summary.json"
  "state/status.md"
  "state/next_actions.md"
  "state/open_loops.md"
  "state/useful_hour_scores.md"
  ".agents/skills/long-codex-cycle/SKILL.md"
  "scripts/check_useful_hour_scores.py"
  "scripts/eval_long_codex_cycle.py"
  "scripts/eval_dead_end_avoidance.py"
  "scripts/eval_queue_exhaustion.py"
)

missing=0
for file in "${required_files[@]}"; do
  if [[ ! -s "$file" ]]; then
    echo "missing or empty: $file" >&2
    missing=1
  fi
done

if ! find logs -maxdepth 1 -type f -name '*.md' | grep -q .; then
  echo "missing run log under logs/" >&2
  missing=1
fi

if ! grep -q "https://developers.openai.com" docs/research/2026-05-06-long-horizon-codex.md; then
  echo "research note is missing OpenAI source links" >&2
  missing=1
fi

if ! grep -q "https://arxiv.org/abs/2603.04257" docs/research/2026-05-06-deep-agent-memory.md; then
  echo "deep research note is missing Memex source link" >&2
  missing=1
fi

if ! grep -q "long-codex-cycle" .agents/skills/long-codex-cycle/SKILL.md; then
  echo "skill metadata missing expected name" >&2
  missing=1
fi

if ! grep -q "Subagent Handoffs" docs/operating_loop.md; then
  echo "operating loop is missing subagent handoff rule" >&2
  missing=1
fi

if ! grep -q "artifact path" .agents/skills/long-codex-cycle/SKILL.md; then
  echo "long-codex-cycle skill is missing subagent artifact handoff rule" >&2
  missing=1
fi

if ! grep -q "long-codex-hourly-continuation" state/useful_hour_scores.md; then
  echo "useful hour score ledger is missing heartbeat entry" >&2
  missing=1
fi

if ! python3 scripts/check_useful_hour_scores.py >/dev/null; then
  echo "useful hour score ledger consistency check failed" >&2
  missing=1
fi

if ! grep -q "EVAL_SMOKE_MARKER" evals/long_codex_cycle_smoke.md; then
  echo "codex exec smoke eval prompt is missing status marker" >&2
  missing=1
fi

if ! grep -q "DEAD_END_AVOIDED_MARKER" evals/dead_end_avoidance_prompt.md; then
  echo "dead-end avoidance eval prompt is missing status marker" >&2
  missing=1
fi

if ! grep -q "QUEUE_EXHAUSTION_MARKER" evals/queue_exhaustion_prompt.md; then
  echo "queue-exhaustion eval prompt is missing status marker" >&2
  missing=1
fi

if ! python3 - <<'PY'
import json
from pathlib import Path

summary = json.loads(Path("evals/last_long_codex_cycle_smoke_summary.json").read_text())
assert summary.get("summary_version") == 1
assert summary.get("passed") is True
assert isinstance(summary.get("duration_seconds"), (int, float))
assert summary.get("event_counts", {}).get("thread.started", 0) >= 1
assert summary.get("event_counts", {}).get("turn.completed", 0) >= 1
assert all(summary.get("checks", {}).values())
PY
then
  echo "codex exec smoke eval summary is missing required pass data" >&2
  missing=1
fi

if ! python3 - <<'PY'
import json
from pathlib import Path

summary = json.loads(Path("evals/last_dead_end_avoidance_summary.json").read_text())
assert summary.get("summary_version") == 1
assert summary.get("passed") is True
assert isinstance(summary.get("duration_seconds"), (int, float))
assert summary.get("event_counts", {}).get("thread.started", 0) >= 1
assert summary.get("event_counts", {}).get("turn.completed", 0) >= 1
checks = summary.get("checks", {})
assert all(checks.values())
assert checks.get("forbidden_log_absent") is True
PY
then
  echo "dead-end avoidance eval summary is missing required pass data" >&2
  missing=1
fi

if ! python3 - <<'PY'
import json
from pathlib import Path

summary = json.loads(Path("evals/last_queue_exhaustion_summary.json").read_text())
assert summary.get("summary_version") == 1
assert summary.get("passed") is True
assert isinstance(summary.get("duration_seconds"), (int, float))
assert summary.get("event_counts", {}).get("thread.started", 0) >= 1
assert summary.get("event_counts", {}).get("turn.completed", 0) >= 1
checks = summary.get("checks", {})
assert all(checks.values())
assert checks.get("forbidden_log_absent") is True
assert checks.get("rollback_recommendation") is True
PY
then
  echo "queue-exhaustion eval summary is missing required pass data" >&2
  missing=1
fi

if ! grep -q "Keep the active heartbeat automation as-is" docs/heartbeat_synthesis.md; then
  echo "heartbeat synthesis is missing automation decision" >&2
  missing=1
fi

if ! grep -q "FREQ=MINUTELY;INTERVAL=30" docs/cadence_review.md; then
  echo "cadence review is missing active 30-minute schedule decision" >&2
  missing=1
fi

if ! grep -q "OpenAI, Codex best practices" docs/source_ledger.md; then
  echo "source ledger is missing OpenAI Codex best-practices row" >&2
  missing=1
fi

if ! grep -q "Memex(RL)" docs/source_ledger.md; then
  echo "source ledger is missing indexed-memory row" >&2
  missing=1
fi

if ! grep -q "MemoryArena" docs/source_ledger.md; then
  echo "source ledger is missing memory-action eval row" >&2
  missing=1
fi

if ! grep -q 'Keep `usage`' docs/eval_summary_policy.md; then
  echo "eval summary policy is missing usage-field decision" >&2
  missing=1
fi

if ! grep -q 'summary_version' docs/eval_summary_policy.md; then
  echo "eval summary policy is missing summary_version guidance" >&2
  missing=1
fi

for heading in "## Active Blockers" "## Active Follow-Ups" "## Parked Ideas" "## Retired Ideas"; do
  if ! grep -q "$heading" state/open_loops.md; then
    echo "open loops file is missing heading: $heading" >&2
    missing=1
  fi
done

if ! python3 - <<'PY'
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

errors: list[str] = []
date_re = re.compile(r"^\s*(?:Last updated|Date):\s*(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)
url_re = re.compile(r"https?://[^\s)]+")


def note(message: str) -> None:
    errors.append(message)


def first_date(path: Path) -> date | None:
    match = date_re.search(path.read_text())
    if not match:
        return None
    return date.fromisoformat(match.group(1))


logs = sorted(Path("logs").glob("*.md"), key=lambda path: path.stat().st_mtime, reverse=True)
if logs:
    latest_log = logs[0]
    latest_log_date = first_date(latest_log)
    if latest_log_date is None:
        note(f"{latest_log} is missing a Date: YYYY-MM-DD line")
    else:
        for state_path in (Path("state/status.md"), Path("state/next_actions.md")):
            state_date = first_date(state_path)
            if state_date is None:
                note(f"{state_path} is missing Last updated: YYYY-MM-DD")
            elif state_date < latest_log_date:
                note(f"{state_path} is stale: {state_date} is older than latest log {latest_log_date}")

latest_research_date: date | None = None
for research_path in sorted(Path("docs/research").glob("*.md")):
    text = research_path.read_text()
    research_date = first_date(research_path)
    if research_date is None:
        note(f"{research_path} is missing Date: YYYY-MM-DD")
    elif latest_research_date is None or research_date > latest_research_date:
        latest_research_date = research_date
    if "## Sources" not in text:
        note(f"{research_path} is missing a ## Sources section")
    if not url_re.search(text):
        note(f"{research_path} is missing source links")

ledger = Path("docs/source_ledger.md")
ledger_text = ledger.read_text()
ledger_date = first_date(ledger)
if ledger_date is None:
    note("source ledger is missing Last updated: YYYY-MM-DD")
elif latest_research_date is not None and ledger_date < latest_research_date:
    note(
        f"source ledger is stale: {ledger_date} is older than latest research note {latest_research_date}"
    )
rows = [
    line
    for line in ledger_text.splitlines()
    if line.startswith("| ") and not line.startswith("| ---") and not line.startswith("| Source")
]
if not rows:
    note("source ledger has no data rows")
for index, row in enumerate(rows, start=1):
    cells = [cell.strip() for cell in row.strip("|").split("|")]
    if len(cells) != 5:
        note(f"source ledger row {index} should have 5 columns")
        continue
    source, _claim, evidence, _implication, _next_use = cells
    if not url_re.search(source):
        note(f"source ledger row {index} source cell is missing a URL")
    evidence_paths = re.findall(r"`([^`]+)`", evidence)
    if not evidence_paths:
        note(f"source ledger row {index} evidence cell is missing local path references")
    for raw_path in evidence_paths:
        if raw_path == "this ledger":
            continue
        candidate = Path(raw_path)
        if not candidate.exists():
            note(f"source ledger row {index} references missing evidence path: {raw_path}")

if errors:
    for error in errors:
        print(error, file=sys.stderr)
    raise SystemExit(1)
PY
then
  echo "metadata freshness/source checks failed" >&2
  missing=1
fi

if ! python3 - <<'PY'
import py_compile
import tempfile

with tempfile.NamedTemporaryFile(suffix=".pyc") as compiled:
    py_compile.compile("scripts/check_useful_hour_scores.py", cfile=compiled.name, doraise=True)
with tempfile.NamedTemporaryFile(suffix=".pyc") as compiled:
    py_compile.compile("scripts/eval_long_codex_cycle.py", cfile=compiled.name, doraise=True)
with tempfile.NamedTemporaryFile(suffix=".pyc") as compiled:
    py_compile.compile("scripts/eval_dead_end_avoidance.py", cfile=compiled.name, doraise=True)
with tempfile.NamedTemporaryFile(suffix=".pyc") as compiled:
    py_compile.compile("scripts/eval_queue_exhaustion.py", cfile=compiled.name, doraise=True)
PY
then
  echo "codex exec eval script has a syntax error" >&2
  missing=1
fi

if [[ "$missing" -ne 0 ]]; then
  exit 1
fi

echo "long-codex repo structure ok"
