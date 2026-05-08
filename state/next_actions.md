# Next Actions

Last updated: 2026-05-08

## Priority Queue

1. Add a lightweight useful-hour score ledger consistency check before adding a model-graded useful-hour eval.
2. After two more heartbeat runs, review whether the temporary faster cadence should remain or return to hourly.
3. Add a weekly synthesis automation only if hourly/half-hourly logs begin repeating or growing too long.
4. Add a useful-hour score behavior eval only if the ledger consistency check shows manual scoring is not enough.
5. Refactor shared code between `scripts/eval_long_codex_cycle.py` and `scripts/eval_dead_end_avoidance.py` only if a third eval is added.
6. If repeated runs score below 7, update the automation before doing more research.

## Parking Lot

- Explore whether a global user skill is useful after the repo skill proves itself.
- Consider a weekly synthesis automation that compresses logs into principles.
- Build a scorecard for "useful hour" quality: artifact, verification, novelty, handoff clarity, and token efficiency.
- Keep `state/open_loops.md` as the place for active blockers, parked ideas, and retired ideas.
- Revisit `docs/eval_summary_policy.md` only if summary artifacts become noisy or expensive.
