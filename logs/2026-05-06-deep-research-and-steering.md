# Run Log: Deep Research And Steering

Date: 2026-05-06

## Mode

`harvest` plus `automation` because the user explicitly asked for research followed by scheduling.

## What Changed

- Added deeper research synthesis in `docs/research/2026-05-06-deep-agent-memory.md`.
- Added `docs/automation_steering.md` to make hourly work selection explicit.
- Added `docs/useful_hour_scorecard.md` to evaluate whether a run was useful.
- Added `docs/decision_log.md`.
- Updated the repo skill and canonical automation prompt to use the steering policy.
- Updated state and next actions.
- Updated active heartbeat automation `long-codex-hourly-continuation` with the new steering prompt.

## Research Takeaways

- Durable memory should be layered: working state, episodic logs, semantic synthesis.
- Indexed evidence beats summary-only memory because future runs can dereference exact paths.
- Memory quality should be evaluated by changed future action, not just recall.
- The hourly automation should score candidate actions and pick one bounded artifact.

## Verification

Run:

```sh
./scripts/check_long_codex_repo.sh
```

## Next

Observe and score the next heartbeat wakeup with `docs/useful_hour_scorecard.md`.
