# Run Log: Cadence Review

Date: 2026-05-08
Time: 12:24 America/Los_Angeles
Automation: `long-codex-hourly-continuation`

## Mode

`automation`

## Candidate Actions Considered

- Review faster cadence and decide whether to keep or return hourly: score 9. Top queue item, enough evidence, and directly about the live automation.
- Add weekly synthesis automation: score 3. Premature because logs are compact and non-repetitive.
- Add useful-hour behavior eval: score 4. Still premature because the deterministic score-ledger check now covers the cheaper failure mode.

Chosen action: document the cadence review and keep the live heartbeat unchanged.

## What Changed

- Added `docs/cadence_review.md`.
- Updated `scripts/check_long_codex_repo.sh` to require the cadence review and check the active schedule decision.
- Updated `state/status.md`, `state/next_actions.md`, `state/open_loops.md`, and `state/useful_hour_scores.md`.

## Verification

```sh
sed -n '1,220p' /Users/milesnash/.codex/automations/long-codex-hourly-continuation/automation.toml
./scripts/check_long_codex_repo.sh
```

Result: passed. The live automation config still shows `FREQ=MINUTELY;INTERVAL=30`.

## Useful-Hour Score

12/12. Details are in `state/useful_hour_scores.md`.

## Next

Harvest one current source-backed practice for long-horizon agents and add it to `docs/source_ledger.md`.
