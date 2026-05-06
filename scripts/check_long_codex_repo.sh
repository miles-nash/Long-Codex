#!/usr/bin/env bash
set -euo pipefail

required_files=(
  "README.md"
  "AGENTS.md"
  "docs/spec.md"
  "docs/operating_loop.md"
  "docs/automation_prompt.md"
  "docs/research/2026-05-06-long-horizon-codex.md"
  "state/status.md"
  "state/next_actions.md"
  ".agents/skills/long-codex-cycle/SKILL.md"
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

if ! grep -q "long-codex-cycle" .agents/skills/long-codex-cycle/SKILL.md; then
  echo "skill metadata missing expected name" >&2
  missing=1
fi

if [[ "$missing" -ne 0 ]]; then
  exit 1
fi

echo "long-codex repo structure ok"
