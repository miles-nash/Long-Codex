# Useful Hour Scores

## 2026-05-06 00:10 America/Los_Angeles

Automation: `long-codex-hourly-continuation`

Mode chosen: `eval`

Score: 11/12

- Artifact: 2 - added this score ledger plus a heartbeat run log.
- Verification: 2 - ran `./scripts/check_long_codex_repo.sh` before and after edits.
- Learning: 2 - discovered that "latest log" must be resolved by modification time, not filename sort, because descriptive filenames can misorder logs.
- Steering: 2 - followed the top next action and avoided new broad research.
- Handoff: 2 - updated status, next actions, and log.
- Restraint: 1 - touched the prompt, skill, and loop docs to fix one concrete ambiguity; useful but broader than a pure observation.

Result: useful hour. The automation resumed from durable state, chose a narrow eval cycle, and improved the next run's orientation.
