# Run Log: Codex Exec Eval

Date: 2026-05-06
Time: 01:13 America/Los_Angeles
Automation: `long-codex-hourly-continuation`

## Mode

`eval`

## Candidate Actions Considered

- Add the first `codex exec --json` eval: high future unblock, high durability, moderate cost.
- Observe the second wakeup only: useful but lower artifact value because the first wakeup had already been scored.
- Build a source ledger: valuable, but less urgent than proving the eval loop can run.

Chosen action: add and run the `codex exec --json` smoke eval.

## What Changed

- Added `evals/long_codex_cycle_smoke.md`.
- Added `scripts/eval_long_codex_cycle.py`.
- Updated `scripts/check_long_codex_repo.sh` to require and syntax-check the eval harness.
- Updated `state/status.md`, `state/next_actions.md`, and `state/useful_hour_scores.md`.

## Evidence

Official Codex docs say `codex exec` is for scripted or CI-style runs and `--json` emits newline-delimited JSON events, including `thread.started`, `turn.completed`, `turn.failed`, item events, and errors: https://developers.openai.com/codex/cli/reference#codex-exec and https://developers.openai.com/codex/noninteractive#make-output-machine-readable.

The harness runs Codex in a temporary copy of this repo, asks it to make two tiny durable-state edits, then validates:

- JSONL event stream includes `thread.started` and `turn.completed`.
- JSONL event stream does not include `turn.failed` or `error`.
- `state/status.md` contains `EVAL_SMOKE_MARKER`.
- `logs/eval-smoke-run.md` exists and contains `EVAL_SMOKE_LOG`.
- final message contains `EVAL_SMOKE_DONE`.

## Verification

```sh
./scripts/check_long_codex_repo.sh
python3 scripts/eval_long_codex_cycle.py --dry-run
python3 scripts/eval_long_codex_cycle.py --timeout 600
```

Result: all passed.

## Useful-Hour Score

12/12. Details are in `state/useful_hour_scores.md`.

## Next

Synthesize the first two heartbeat runs and decide whether the steering prompt needs tightening.
