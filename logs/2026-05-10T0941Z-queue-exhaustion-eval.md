# Run Log: Queue-Exhaustion Eval

Date: 2026-05-10
Time: 03:41 America/Denver
Automation: `long-codex-hourly-continuation`

## Mode

`eval`

## Candidate Actions Considered

- Add a queue-exhaustion behavior eval: score 10. Top queue item, high risk reduction, and directly tests whether longer persistence avoids busywork when no ready work exists.
- Review cadence immediately: score 6. Important, but premature until the eval result exists.
- Refactor nested eval scripts: score 3. Possible future cleanup, but a third eval needed to prove the duplication is painful.

Chosen action: add and run the queue-exhaustion behavior eval.

## What Changed

- Added `evals/queue_exhaustion_prompt.md`.
- Added `scripts/eval_queue_exhaustion.py`.
- Added `evals/last_queue_exhaustion_summary.json` from a passing nested Codex run.
- Updated `scripts/check_long_codex_repo.sh` to require and validate the new eval artifacts.
- Updated `docs/next_experiment_ladder.md`, `state/status.md`, `state/next_actions.md`, `state/open_loops.md`, and `state/useful_hour_scores.md`.

## Verification

```sh
python3 scripts/eval_queue_exhaustion.py --dry-run
python3 -m py_compile scripts/eval_queue_exhaustion.py
python3 scripts/eval_queue_exhaustion.py --timeout 600
./scripts/check_long_codex_repo.sh
python3 scripts/check_useful_hour_scores.py
git diff --check
```

Result: passed. The first nested eval attempt failed under sandbox permissions because Codex could not access `~/.codex/sessions`; rerunning the same command with narrow elevated permission passed.

## Useful-Hour Score

12/12. Details are in `state/useful_hour_scores.md`.

## Next

Review `docs/cadence_review.md` using the passing queue-exhaustion eval result, then decide whether to keep the 30-minute heartbeat or return to hourly.
