# Eval Summary Policy

Date: 2026-05-08

## Decision

Keep `usage` token fields in eval summary artifacts when `codex exec --json` emits them.

They are small, already available in `turn.completed` events, and they support future token-efficiency comparisons without keeping full JSONL traces. Treat them as optional telemetry, not as pass/fail evidence, unless a future eval is specifically testing token cost.

## Required Core Fields

Every committed eval summary should stay compact and include:

- `summary_version`
- `passed`
- `checks`
- `duration_seconds`
- `event_counts`
- `event_total`
- `prompt_path`
- `returncode`
- `timeout_seconds`
- `model`
- `parse_error`
- `usage`

Behavior-specific summaries may add narrow fields such as `trap_log` when the field explains what was tested.

## Usage Field Rules

- Keep `usage` as the raw object from the final `turn.completed` event when present.
- Use `null` if the event stream has no usage object.
- Do not fail an eval solely because `usage` is missing.
- Do not store full transcripts, raw JSONL traces, secrets, or unbounded stderr in committed summaries.
- Keep `stderr_tail` empty on success and bounded on failure.

## Why This Helps Long Codex

The useful-hour scorecard includes restraint and token efficiency as a future quality dimension. Compact usage data lets later sessions notice when a change makes evals slower or more expensive without expanding into a heavier observability system.

## Current Evidence

- `evals/last_long_codex_cycle_smoke_summary.json`
- `evals/last_dead_end_avoidance_summary.json`
- `scripts/eval_long_codex_cycle.py`
- `scripts/eval_dead_end_avoidance.py`
