# Status

Last updated: 2026-05-08

## Current State

The repo now has an initial long-horizon Codex scaffold:

- mission and constraints in `docs/spec.md`
- repeatable operating loop in `docs/operating_loop.md`
- first research distillation in `docs/research/2026-05-06-long-horizon-codex.md`
- canonical hourly automation prompt in `docs/automation_prompt.md`
- steering policy in `docs/automation_steering.md`
- useful-hour scorecard in `docs/useful_hour_scorecard.md`
- decision log in `docs/decision_log.md`
- repo-scoped skill in `.agents/skills/long-codex-cycle/SKILL.md`
- lightweight structural check in `scripts/check_long_codex_repo.sh`
- active thread heartbeat automation `long-codex-hourly-continuation`
- GitHub remote `origin` set to `https://github.com/miles-nash/Long-Codex.git`
- initial scaffold and handoff commits pushed to `origin/main`; use `git log --oneline -3` for exact history
- heartbeat prompt updated to read `docs/automation_steering.md` and report a useful-hour score
- first heartbeat wakeup observed and scored in `state/useful_hour_scores.md`
- "latest log" instructions now use modification time, not filename sort
- live heartbeat automation updated with the modification-time log rule
- `codex exec --json` smoke eval added and passed in `scripts/eval_long_codex_cycle.py`
- first two heartbeat runs synthesized in `docs/heartbeat_synthesis.md`; prompt kept as-is
- source ledger added in `docs/source_ledger.md` to map claims to evidence paths and implications
- active heartbeat cadence temporarily increased from 60 minutes to 30 minutes after Miles said to work more than hourly for now
- `scripts/check_long_codex_repo.sh` now detects stale state dates, research notes without sources, and missing source-ledger evidence paths
- `scripts/eval_long_codex_cycle.py` now emits `evals/last_long_codex_cycle_smoke_summary.json` with duration, event counts, checks, and usage
- dead-end avoidance eval added and passed in `scripts/eval_dead_end_avoidance.py`
- stale-open-loop state added in `state/open_loops.md`, with active blockers, active follow-ups, parked ideas, and retired ideas

## Decisions

- Use markdown files as the source of truth, with Codex memories as a secondary recall layer.
- Use a thread heartbeat for continuity when the same conversation should keep waking up.
- Keep cycles bounded by artifact, verification, and handoff rather than by ambition.
- Treat evals as part of the system, starting with cheap deterministic structure checks.
- Enable Codex memories in `~/.codex/config.toml`, but keep required guidance in repo files.
- Make the heartbeat choose work by a lightweight value score, not by recency alone.
- Preserve exact evidence paths and source URLs; summaries should point back to dereferenceable evidence.
- Resolve "latest log" by modification time because descriptive filenames are not reliable chronological keys.
- Run nested Codex evals in a temporary repo copy with `approval_policy="never"` and `workspace-write`, never against the live project.
- Keep the active heartbeat prompt unchanged after two successful observed runs; improve memory structure next.
- Use `docs/source_ledger.md` as the first stop for source-backed claims before reopening full research notes.
- Keep the same steering prompt while increasing cadence; faster cycles should still be bounded by artifact, verification, and handoff.
- Treat freshness and source-link checks as part of the minimum durable-state contract.
- Keep eval summary artifacts compact enough to commit; omit successful-run stderr noise.
- Behavior evals should plant controlled traps in temporary repo copies, then verify the agent avoids repeating the trap.
- Keep stale-open-loop state separate from the priority queue so future sessions can distinguish active work from parked or retired ideas.

## Known Gaps

- The eval suite has a smoke test and a dead-end avoidance behavior test; it does not yet measure useful-hour score.
- The repo has enough heartbeat logs for initial synthesis, but not yet for weekly trend analysis.
- `state/open_loops.md` exists, but it has not yet been exercised across multiple future runs.

## Recovery Instructions

If a future session is disoriented, do this:

1. Read `README.md` and `AGENTS.md`.
2. Run `./scripts/check_long_codex_repo.sh`.
3. Read this file and `state/next_actions.md`.
4. Pick the first not-done next action that is still relevant.
5. Leave a log before stopping.
