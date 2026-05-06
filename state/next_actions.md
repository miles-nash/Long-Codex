# Next Actions

Last updated: 2026-05-06

## Priority Queue

1. Extend `scripts/eval_long_codex_cycle.py` to emit a small JSON summary artifact with duration, event counts, and pass/fail checks.
2. Add a second eval that checks whether the cycle avoids repeating a dead-end noted in a prior log.
3. Add a stale-open-loop list that separates active blockers, parked ideas, and retired ideas.
4. After two more heartbeat runs, update `docs/heartbeat_synthesis.md` with trend notes.
5. Add a weekly synthesis automation only if hourly/half-hourly logs begin repeating or growing too long.
6. If repeated runs score below 7, update the automation before doing more research.

## Parking Lot

- Explore whether a global user skill is useful after the repo skill proves itself.
- Consider a weekly synthesis automation that compresses logs into principles.
- Build a scorecard for "useful hour" quality: artifact, verification, novelty, handoff clarity, and token efficiency.
