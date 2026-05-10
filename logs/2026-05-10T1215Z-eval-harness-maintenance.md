# Run Log: Eval Harness Maintenance

Date: 2026-05-10
Time: 06:15 America/Denver
Automation: `long-codex-hourly-continuation`

## Mode

`structure`

## Candidate Actions Considered

- Record the eval-harness maintenance decision: score 8. Top queue item, low risk, and creates a durable rule before another eval is added.
- Extract `scripts/codex_eval_utils.py` now: score 6. Would reduce duplicated plumbing, but it would touch all three passing eval scripts without a concrete shared-behavior change.
- Ignore the duplication: score 3. The duplication is real enough that future sessions need an explicit trigger rule.

Chosen action: document the helper boundary and defer extraction until a concrete trigger occurs.

## What Changed

- Added `docs/eval_harness_maintenance.md`.
- Updated `scripts/check_long_codex_repo.sh` to require the maintenance note.
- Updated `state/status.md`, `state/next_actions.md`, `state/open_loops.md`, and `state/useful_hour_scores.md`.

## Verification

```sh
wc -l scripts/eval_long_codex_cycle.py scripts/eval_dead_end_avoidance.py scripts/eval_queue_exhaustion.py
rg -n "^def " scripts/eval_long_codex_cycle.py scripts/eval_dead_end_avoidance.py scripts/eval_queue_exhaustion.py
./scripts/check_long_codex_repo.sh
python3 scripts/check_useful_hour_scores.py
git diff --check
```

Result: passed.

## Useful-Hour Score

12/12. Details are in `state/useful_hour_scores.md`.

## Next

Let the hourly cadence run once more, then review `docs/cadence_review.md` only if the two hourly runs show drift, repetition, or a new concrete experiment ladder.
