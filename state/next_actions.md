# Next Actions

Last updated: 2026-05-10

## Priority Queue

1. On the next hourly wake, check for a concrete trigger: drift, repetition, a new experiment ladder, user instruction, or a repo-check failure. If none exists again, review whether to pause or slow the heartbeat instead of logging another no-ready-work run.
2. Review `docs/cadence_review.md` only if hourly runs show drift, repetition, or a new concrete experiment ladder.
3. Add a subagent handoff drift check only if `docs/operating_loop.md` and `.agents/skills/long-codex-cycle/SKILL.md` diverge later.
4. Add a weekly synthesis automation only if hourly logs begin repeating or growing too long.
5. Add a broader useful-hour score behavior eval only if queue-exhaustion coverage is not enough.
6. Extract `scripts/codex_eval_utils.py` only if a fourth nested eval is added or shared eval runtime behavior changes.
7. If repeated runs score below 7, update the automation before doing more research.

## Parking Lot

- Explore whether a global user skill is useful after the repo skill proves itself.
- Consider a weekly synthesis automation that compresses logs into principles.
- Build a scorecard for "useful hour" quality: artifact, verification, novelty, handoff clarity, and token efficiency.
- Keep `state/open_loops.md` as the place for active blockers, parked ideas, and retired ideas.
- Revisit `docs/eval_summary_policy.md` only if summary artifacts become noisy or expensive.
- Revisit `scripts/check_useful_hour_scores.py` if future score entries need an explicit blocked-run exception.
- Return the heartbeat to hourly if `docs/cadence_review.md` watchpoints trigger.
- Return to 30-minute cadence only when a concrete experiment ladder justifies it.
- Use subagents only for independent branches where durable artifact handoffs will reduce context pressure.
- Add source-ledger row coverage checks only if date freshness proves too weak for material research notes.
