# Next Actions

Last updated: 2026-05-06

## Priority Queue

1. Observe the first `long-codex-hourly-continuation` wakeup under the new steering prompt and score it with `docs/useful_hour_scorecard.md`.
2. Add a tiny `codex exec --json` eval that verifies `$long-codex-cycle` produces a log and updates `state/status.md`.
3. Improve `scripts/check_long_codex_repo.sh` to detect stale status files and missing source links across all research notes.
4. Turn the memory architecture into a ledger: add `docs/source_ledger.md` with source, claim, evidence path, and implication columns.
5. After two heartbeat runs, synthesize what the automation actually did versus what the steering policy asked for.
6. If repeated runs score below 7, update the automation before doing more research.

## Parking Lot

- Explore whether a global user skill is useful after the repo skill proves itself.
- Consider a weekly synthesis automation that compresses logs into principles.
- Build a scorecard for "useful hour" quality: artifact, verification, novelty, handoff clarity, and token efficiency.
