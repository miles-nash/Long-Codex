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

## 2026-05-06 01:13 America/Los_Angeles

Automation: `long-codex-hourly-continuation`

Mode chosen: `eval`

Score: 12/12

- Artifact: 2 - added `scripts/eval_long_codex_cycle.py` and `evals/long_codex_cycle_smoke.md`.
- Verification: 2 - ran `./scripts/check_long_codex_repo.sh`, `python3 scripts/eval_long_codex_cycle.py --dry-run`, and the full nested smoke eval.
- Learning: 2 - confirmed `codex exec --json` can be used as a machine-readable eval harness in a temporary repo copy.
- Steering: 2 - followed the highest-priority next action and avoided broader research.
- Handoff: 2 - updated status, next actions, score ledger, and run log.
- Restraint: 2 - kept the nested eval local, temporary, and non-publishing.

Result: excellent hour. The repo now has a working empirical smoke eval for the long-codex cycle.

## 2026-05-06 02:19 America/Los_Angeles

Automation: `long-codex-hourly-continuation`

Mode chosen: `synthesis`

Score: 11/12

- Artifact: 2 - added `docs/heartbeat_synthesis.md`.
- Verification: 2 - ran `./scripts/check_long_codex_repo.sh` before and after edits.
- Learning: 2 - concluded the prompt is working and the next bottleneck is memory structure, not automation wording.
- Steering: 2 - followed the top next action and changed mode after two eval cycles.
- Handoff: 2 - updated status, next actions, score ledger, and run log.
- Restraint: 1 - updated the structural check to require the synthesis artifact, which is useful but slightly expands the maintenance surface.

Result: useful hour. The automation should remain active unchanged; next work should build the source ledger.

## 2026-05-06 03:34 America/Los_Angeles

Automation: `long-codex-hourly-continuation`

Mode chosen: `structure`

Score: 12/12

- Artifact: 2 - added `docs/source_ledger.md`.
- Verification: 2 - ran `./scripts/check_long_codex_repo.sh` before and after edits.
- Learning: 2 - turned scattered research claims into a dereferenceable ledger organized by future use.
- Steering: 2 - followed the highest-priority next action and shifted from synthesis to memory structure.
- Handoff: 2 - updated status, next actions, score ledger, and run log.
- Restraint: 2 - kept the cycle to one durable memory artifact and a small structural check update.

Result: excellent hour. The next bottleneck is automated freshness/link checking and richer eval summaries.

## 2026-05-06 Continuing Work

Automation: manual continuation after Miles said "keep working"

Mode chosen: `eval`

Score: 12/12

- Artifact: 2 - improved `scripts/check_long_codex_repo.sh` with freshness, source-link, and ledger-evidence checks.
- Verification: 2 - ran `./scripts/check_long_codex_repo.sh` after the change.
- Learning: 2 - made the repo's implicit freshness/source contract executable.
- Steering: 2 - followed the highest-priority next action without expanding scope.
- Handoff: 2 - updated status, next actions, score ledger, and run log.
- Restraint: 2 - kept the cycle to one verification artifact.

Result: excellent continuation. The next best step is adding JSON summary output to the nested Codex eval harness.

## 2026-05-06 08:05 America/Los_Angeles

Automation: `long-codex-hourly-continuation`

Mode chosen: `eval`

Score: 12/12

- Artifact: 2 - extended `scripts/eval_long_codex_cycle.py` and added `evals/last_long_codex_cycle_smoke_summary.json`.
- Verification: 2 - ran dry-run, full nested eval, and `./scripts/check_long_codex_repo.sh`.
- Learning: 2 - captured duration, event counts, checks, and token usage for the smoke eval.
- Steering: 2 - followed the top next action and kept the eval focused.
- Handoff: 2 - updated status, next actions, score ledger, and run log.
- Restraint: 2 - kept summary output compact and omitted successful-run stderr noise.

Result: excellent hour. The next best step is a behavior eval for avoiding a logged dead end.
