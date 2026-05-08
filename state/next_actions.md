# Next Actions

Last updated: 2026-05-06

## Priority Queue

1. Add a stale-open-loop list that separates active blockers, parked ideas, and retired ideas.
2. After two more heartbeat runs, update `docs/heartbeat_synthesis.md` with trend notes.
3. Add a weekly synthesis automation only if hourly/half-hourly logs begin repeating or growing too long.
4. Decide whether eval summary artifacts should keep usage/token fields once multiple runs exist.
5. Refactor shared code between `scripts/eval_long_codex_cycle.py` and `scripts/eval_dead_end_avoidance.py` only if a third eval is added.
6. If repeated runs score below 7, update the automation before doing more research.

## Parking Lot

- Explore whether a global user skill is useful after the repo skill proves itself.
- Consider a weekly synthesis automation that compresses logs into principles.
- Build a scorecard for "useful hour" quality: artifact, verification, novelty, handoff clarity, and token efficiency.
