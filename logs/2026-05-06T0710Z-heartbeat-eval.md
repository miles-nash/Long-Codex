# Run Log: Heartbeat Eval

Date: 2026-05-06
Time: 00:10 America/Los_Angeles
Automation: `long-codex-hourly-continuation`

## Mode

`eval`

## Candidate Actions Considered

- Observe and score the first heartbeat wakeup: high learning, high durability, low cost.
- Add the first `codex exec --json` eval: high future value, but larger than the first observation cycle.
- Build a source ledger: useful, but less urgent than verifying the automation loop itself.

Chosen action: observe and score the first heartbeat wakeup.

## What Changed

- Added `state/useful_hour_scores.md`.
- Added this heartbeat run log.
- Updated `docs/operating_loop.md`, `docs/automation_steering.md`, `.agents/skills/long-codex-cycle/SKILL.md`, and `docs/automation_prompt.md` to identify the latest log by modification time.
- Updated `state/status.md` and `state/next_actions.md`.
- Updated `scripts/check_long_codex_repo.sh` to require the useful-hour ledger.
- Updated the live heartbeat automation with the same modification-time log rule.

## Observation

The heartbeat resumed from the expected durable state without asking Miles for help. A small ambiguity appeared during orientation: filename sorting can select the wrong "latest" log when filenames include descriptive suffixes. Modification time is the right local rule.

## Useful-Hour Score

11/12. Details are in `state/useful_hour_scores.md`.

## Verification

```sh
./scripts/check_long_codex_repo.sh
```

## Next

Add a tiny `codex exec --json` eval that checks whether the long-codex cycle updates durable state and leaves a log.
