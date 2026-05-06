# Next Actions

Last updated: 2026-05-06

## Priority Queue

1. Turn the memory architecture into a ledger: add `docs/source_ledger.md` with source, claim, evidence path, and implication columns.
2. Improve `scripts/check_long_codex_repo.sh` to detect stale status files and missing source links across all research notes.
3. Extend `scripts/eval_long_codex_cycle.py` to emit a small JSON summary artifact with duration, event counts, and pass/fail checks.
4. Add a second eval that checks whether the cycle avoids repeating a dead-end noted in a prior log.
5. After two more heartbeat runs, update `docs/heartbeat_synthesis.md` with trend notes.
6. If repeated runs score below 7, update the automation before doing more research.

## Parking Lot

- Explore whether a global user skill is useful after the repo skill proves itself.
- Consider a weekly synthesis automation that compresses logs into principles.
- Build a scorecard for "useful hour" quality: artifact, verification, novelty, handoff clarity, and token efficiency.
