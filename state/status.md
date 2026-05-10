# Status

Last updated: 2026-05-10

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
- `scripts/check_long_codex_repo.sh` now detects when `docs/source_ledger.md` is older than the latest dated `docs/research/*.md` note
- `scripts/eval_long_codex_cycle.py` now emits `evals/last_long_codex_cycle_smoke_summary.json` with duration, event counts, checks, and usage
- dead-end avoidance eval added and passed in `scripts/eval_dead_end_avoidance.py`
- stale-open-loop state added in `state/open_loops.md`, with active blockers, active follow-ups, parked ideas, and retired ideas
- eval summary field policy added in `docs/eval_summary_policy.md`
- faster-cadence heartbeat trend synthesis updated in `docs/heartbeat_synthesis.md`; prompt and cadence kept as-is, weekly synthesis automation deferred
- useful-hour score ledger consistency check added in `scripts/check_useful_hour_scores.py`
- cadence review added in `docs/cadence_review.md`; active heartbeat kept at `FREQ=MINUTELY;INTERVAL=30` with watchpoints
- current-practices harvest added in `docs/research/2026-05-08-agent-artifact-handoffs.md` and `docs/source_ledger.md`
- subagent artifact-handoff rule encoded in `docs/operating_loop.md` and `.agents/skills/long-codex-cycle/SKILL.md`
- cadence follow-up review added to `docs/cadence_review.md`; active heartbeat kept at `FREQ=MINUTELY;INTERVAL=30`
- cadence watchpoint review added to `docs/cadence_review.md`; active heartbeat kept at `FREQ=MINUTELY;INTERVAL=30` only because the next run has a concrete synthesis target
- next-experiment ladder added in `docs/next_experiment_ladder.md`; the next frontier is a queue-exhaustion behavior eval
- queue-exhaustion behavior eval added in `scripts/eval_queue_exhaustion.py` and passed; it verifies that a no-ready-work branch records rollback/no-work guidance instead of inventing busywork
- active heartbeat returned to hourly at `FREQ=HOURLY;INTERVAL=1` after the queue-exhaustion eval passed and the fast-cadence experiment ladder completed
- eval harness maintenance assessment added in `docs/eval_harness_maintenance.md`; helper extraction is deferred until a concrete trigger occurs
- canonical and live heartbeat prompts now include a no-ready-work negative-result branch so hourly runs can stop cleanly instead of inventing work
- first live no-ready-work negative-result run observed; no concrete trigger appeared and the run stopped after verification plus a log

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
- Keep `usage` token fields in compact eval summaries when available, but do not make missing usage a pass/fail condition unless an eval explicitly targets token cost.
- Faster cadence is still useful when each run closes a distinct open loop; defer weekly synthesis automation until logs become repetitive or hard to scan.
- Check the useful-hour score ledger's rubric shape before adding heavier model-graded useful-hour evaluation.
- Keep the temporary faster heartbeat cadence while runs remain distinct and high-scoring; return to hourly if cadence watchpoints trigger.
- Subagent work should hand back durable artifact paths plus short findings, not chat-only summaries.
- Use subagents only for independent branches where artifact-path handoffs reduce context pressure.
- Keep the 30-minute heartbeat while runs remain distinct and 10+/12; next test is a bounded synthesis pass that either names a concrete next experiment or recommends returning to hourly.
- Treat source-ledger freshness as a date contract: `docs/source_ledger.md` must be at least as new as the latest dated research note, but not every note needs a ledger row unless it materially changes the system.
- Keep the 30-minute heartbeat through one queue-exhaustion behavior eval because a concrete high-value next experiment now exists.
- Use the queue-exhaustion eval result as the next cadence input before adding more evals or automation.
- Use hourly cadence as the default again; fast cadence should return only when a concrete experiment ladder justifies the extra wakeups.
- Keep the three nested Codex eval scripts duplicated for now; extract `scripts/codex_eval_utils.py` only when adding a fourth eval or changing shared runtime behavior.
- If all candidate actions are conditional, blocked, or lower-value than waiting, record a verified no-ready-work negative result rather than manufacturing a new artifact.
- Treat repeated no-ready-work hourly runs as a cadence signal; if the next hourly wake also has no concrete trigger, consider pausing or slowing the heartbeat instead of logging indefinitely.

## Known Gaps

- The eval suite has a smoke test, a dead-end avoidance behavior test, and a queue-exhaustion behavior test; it does not yet measure useful-hour score.
- The useful-hour score ledger is now shape-checked, but the scores are still human/rubric judgments rather than model-graded quality measurements.
- Weekly synthesis automation is not yet justified by log volume or repetition.
- `state/open_loops.md` is now in use, but it still needs routine pruning as follow-ups resolve.
- The subagent artifact-handoff rule is encoded, but not yet exercised in a real multi-agent cycle.
- Source-ledger freshness is checked by date, but the repo does not yet check that every material research note appears as a ledger row.
- The eval harness helper boundary is documented, but the helper itself is intentionally deferred until a trigger occurs.
- The no-ready-work branch has been observed once in a live hourly run; it has not yet been tested for repeated no-trigger wakes.

## Recovery Instructions

If a future session is disoriented, do this:

1. Read `README.md` and `AGENTS.md`.
2. Run `./scripts/check_long_codex_repo.sh`.
3. Read this file and `state/next_actions.md`.
4. Pick the first not-done next action that is still relevant.
5. Leave a log before stopping.
