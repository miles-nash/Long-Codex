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
  "docs/source_ledger.md"
  "evals/long_codex_cycle_smoke.md"
  "state/status.md"
  "state/next_actions.md"
  "state/useful_hour_scores.md"
  ".agents/skills/long-codex-cycle/SKILL.md"
  "scripts/eval_long_codex_cycle.py"
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

if ! grep -q "long-codex-hourly-continuation" state/useful_hour_scores.md; then
  echo "useful hour score ledger is missing heartbeat entry" >&2
  missing=1
fi

if ! grep -q "EVAL_SMOKE_MARKER" evals/long_codex_cycle_smoke.md; then
  echo "codex exec smoke eval prompt is missing status marker" >&2
  missing=1
fi

if ! grep -q "Keep the active heartbeat automation as-is" docs/heartbeat_synthesis.md; then
  echo "heartbeat synthesis is missing automation decision" >&2
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

if ! python3 - <<'PY'
import py_compile
import tempfile

with tempfile.NamedTemporaryFile(suffix=".pyc") as compiled:
    py_compile.compile("scripts/eval_long_codex_cycle.py", cfile=compiled.name, doraise=True)
PY
then
  echo "codex exec smoke eval script has a syntax error" >&2
  missing=1
fi

if [[ "$missing" -ne 0 ]]; then
  exit 1
fi

echo "long-codex repo structure ok"
