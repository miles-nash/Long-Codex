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

## 2026-05-06 09:10 America/Los_Angeles

Automation: `long-codex-hourly-continuation`

Mode chosen: `eval`

Score: 12/12

- Artifact: 2 - added `scripts/eval_dead_end_avoidance.py`, `evals/dead_end_avoidance_prompt.md`, and `evals/last_dead_end_avoidance_summary.json`.
- Verification: 2 - ran dry-run, full nested dead-end eval, and `./scripts/check_long_codex_repo.sh`.
- Learning: 2 - proved the eval harness can test a behavior property, not just smoke completion.
- Steering: 2 - followed the top next action and kept the test in a temporary repo copy.
- Handoff: 2 - updated status, next actions, score ledger, and run log.
- Restraint: 2 - avoided refactoring shared eval code until there is a third eval.

Result: excellent hour. The next best step is adding a stale-open-loop list for blockers, parked ideas, and retired ideas.

## 2026-05-08 00:15 America/Los_Angeles

Automation: `long-codex-hourly-continuation`

Mode chosen: `structure`

Score: 12/12

- Artifact: 2 - added `state/open_loops.md` and wired it into the repo check.
- Verification: 2 - ran `./scripts/check_long_codex_repo.sh` before and after edits.
- Learning: 2 - separated blockers, active follow-ups, parked ideas, and retired ideas so future runs can steer without rereading every log.
- Steering: 2 - followed the top next action and avoided adding premature automation.
- Handoff: 2 - updated status, next actions, score ledger, open-loop state, and run log.
- Restraint: 2 - kept the cycle to one memory artifact plus a minimal shape check.

Result: excellent hour. The next best step is heartbeat trend synthesis after two more runs, unless a concrete blocker appears first.

## 2026-05-08 00:49 America/Los_Angeles

Automation: `long-codex-hourly-continuation`

Mode chosen: `synthesis`

Score: 12/12

- Artifact: 2 - added `docs/eval_summary_policy.md` and wired it into the repo check.
- Verification: 2 - ran `./scripts/check_long_codex_repo.sh` before and after edits.
- Learning: 2 - resolved the usage/token-field ambiguity by keeping compact telemetry while making it non-fatal unless token cost is the test.
- Steering: 2 - skipped premature heartbeat trend synthesis and chose the highest-value ready item.
- Handoff: 2 - updated status, next actions, open loops, score ledger, and run log.
- Restraint: 2 - did not refactor eval scripts or add a third eval before the policy was needed.

Result: excellent hour. The next best step remains heartbeat trend synthesis after one more heartbeat run.

## 2026-05-08 01:27 America/Los_Angeles

Automation: `long-codex-hourly-continuation`

Mode chosen: `synthesis`

Score: 12/12

- Artifact: 2 - updated `docs/heartbeat_synthesis.md` with faster-cadence trend notes.
- Verification: 2 - ran `./scripts/check_long_codex_repo.sh` before and after edits.
- Learning: 2 - found that the faster cadence is still producing distinct artifacts, while weekly synthesis automation remains premature.
- Steering: 2 - followed the top ready synthesis action and reconciled it with `state/open_loops.md`.
- Handoff: 2 - updated status, next actions, open loops, score ledger, and run log.
- Restraint: 2 - kept the heartbeat prompt and automation unchanged.

Result: excellent hour. The next best step is a lightweight consistency check for useful-hour score ledger entries.

## 2026-05-08 02:12 America/Los_Angeles

Automation: `long-codex-hourly-continuation`

Mode chosen: `eval`

Score: 12/12

- Artifact: 2 - added `scripts/check_useful_hour_scores.py` and wired it into `scripts/check_long_codex_repo.sh`.
- Verification: 2 - ran the new ledger check and `./scripts/check_long_codex_repo.sh`.
- Learning: 2 - made the useful-hour score ledger's implicit rubric contract executable before adding heavier quality evaluation.
- Steering: 2 - followed the top next action and avoided a premature model-graded eval.
- Handoff: 2 - updated status, next actions, open loops, score ledger, and run log.
- Restraint: 2 - kept the check deterministic and limited to ledger shape and score arithmetic.

Result: excellent hour. The next best step is reviewing the temporary faster cadence after one more heartbeat run.

## 2026-05-08 12:24 America/Los_Angeles

Automation: `long-codex-hourly-continuation`

Mode chosen: `automation`

Score: 12/12

- Artifact: 2 - added `docs/cadence_review.md` and wired it into `scripts/check_long_codex_repo.sh`.
- Verification: 2 - verified the live automation config and ran `./scripts/check_long_codex_repo.sh`.
- Learning: 2 - confirmed the active schedule is still 30 minutes and that faster-cadence runs remain distinct and high-scoring.
- Steering: 2 - followed the top next action and avoided changing a working automation without evidence of churn.
- Handoff: 2 - updated status, next actions, open loops, score ledger, and run log.
- Restraint: 2 - kept the live automation unchanged and deferred weekly synthesis automation.

Result: excellent hour. The next best step is a current-practices harvest for the source ledger.

## 2026-05-08 15:48 America/Los_Angeles

Automation: `long-codex-hourly-continuation`

Mode chosen: `harvest`

Score: 12/12

- Artifact: 2 - added `docs/research/2026-05-08-agent-artifact-handoffs.md` and a source-ledger row.
- Verification: 2 - ran `./scripts/check_long_codex_repo.sh`, including source-link and ledger-evidence checks.
- Learning: 2 - harvested the artifact-handoff practice for subagent work from a current agent-system source.
- Steering: 2 - followed the top next action and kept the harvest to one practice.
- Handoff: 2 - updated status, next actions, open loops, score ledger, and run log.
- Restraint: 2 - did not add subagents or new automation before encoding the practice.

Result: excellent hour. The next best step is adding a short subagent artifact-handoff rule to the operating loop and repo skill.

## 2026-05-10 00:38 America/Denver

Automation: `long-codex-hourly-continuation`

Mode chosen: `structure`

Score: 12/12

- Artifact: 2 - encoded the subagent artifact-handoff rule in `docs/operating_loop.md` and `.agents/skills/long-codex-cycle/SKILL.md`.
- Verification: 2 - ran `./scripts/check_long_codex_repo.sh`, including the new rule checks.
- Learning: 2 - converted the harvested source-backed practice into a lightweight operating rule.
- Steering: 2 - followed the top next action and avoided adding premature subagent machinery.
- Handoff: 2 - updated status, next actions, open loops, score ledger, and run log.
- Restraint: 2 - kept the rule conditional and did not spawn subagents without an independent-branch need.

Result: excellent hour. The next best step is cadence watchpoint review now that two post-review heartbeat runs exist.

## 2026-05-10 01:40 America/Denver

Automation: `long-codex-hourly-continuation`

Mode chosen: `automation`

Score: 12/12

- Artifact: 2 - updated `docs/cadence_review.md` with the post-review cadence decision.
- Verification: 2 - checked the live automation config and ran `./scripts/check_long_codex_repo.sh`.
- Learning: 2 - confirmed two post-review runs were both distinct 12/12 artifacts, so no cadence watchpoint triggered.
- Steering: 2 - followed the top next action and avoided changing a working heartbeat schedule.
- Handoff: 2 - updated status, next actions, open loops, score ledger, and run log.
- Restraint: 2 - kept the automation unchanged and deferred weekly synthesis automation.

Result: excellent hour. The next best step is a lightweight source-ledger freshness check.

## 2026-05-10 02:10 America/Denver

Automation: `long-codex-hourly-continuation`

Mode chosen: `eval`

Score: 12/12

- Artifact: 2 - added a source-ledger freshness check to `scripts/check_long_codex_repo.sh`.
- Verification: 2 - ran `./scripts/check_long_codex_repo.sh` and `python3 scripts/check_useful_hour_scores.py`.
- Learning: 2 - converted the implicit source-ledger freshness rule into an executable date check.
- Steering: 2 - followed the top next action and kept the check limited to the lowest-cost failure mode.
- Handoff: 2 - updated status, next actions, open loops, score ledger, and run log.
- Restraint: 2 - did not require every research note to have a ledger row unless future drift proves that stronger rule is needed.

Result: excellent hour. The next best step is cadence watchpoint review after one more heartbeat run, unless a watchpoint triggers first.

## 2026-05-10 02:40 America/Denver

Automation: `long-codex-hourly-continuation`

Mode chosen: `automation`

Score: 12/12

- Artifact: 2 - updated `docs/cadence_review.md` with the queue-health cadence decision.
- Verification: 2 - checked the live automation config and ran `./scripts/check_long_codex_repo.sh`.
- Learning: 2 - found that faster cadence is still productive, but the next-action queue needs a synthesis target before it becomes conditional-only.
- Steering: 2 - followed the top next action and avoided changing a working heartbeat schedule without a triggered watchpoint.
- Handoff: 2 - updated status, next actions, open loops, score ledger, and run log.
- Restraint: 2 - kept the live automation unchanged and deferred weekly synthesis automation.

Result: excellent hour. The next best step is a bounded synthesis over recent heartbeat logs that produces a next-experiment ladder or recommends returning to hourly.

## 2026-05-10 03:11 America/Denver

Automation: `long-codex-hourly-continuation`

Mode chosen: `synthesis`

Score: 12/12

- Artifact: 2 - added `docs/next_experiment_ladder.md` with a concrete experiment ladder.
- Verification: 2 - ran `./scripts/check_long_codex_repo.sh`, `python3 scripts/check_useful_hour_scores.py`, and a ladder content check.
- Learning: 2 - identified queue-exhaustion behavior as the next frontier for useful persistence.
- Steering: 2 - followed the top next action and avoided returning to hourly while a high-value bounded eval exists.
- Handoff: 2 - updated status, next actions, open loops, score ledger, and run log.
- Restraint: 2 - did not add weekly synthesis automation or refactor evals before the next eval exists.

Result: excellent hour. The next best step is adding the queue-exhaustion behavior eval.

## 2026-05-10 03:41 America/Denver

Automation: `long-codex-hourly-continuation`

Mode chosen: `eval`

Score: 12/12

- Artifact: 2 - added `scripts/eval_queue_exhaustion.py`, `evals/queue_exhaustion_prompt.md`, and `evals/last_queue_exhaustion_summary.json`.
- Verification: 2 - ran the queue-exhaustion eval, `./scripts/check_long_codex_repo.sh`, `python3 scripts/check_useful_hour_scores.py`, and `git diff --check`.
- Learning: 2 - verified the agent can take the no-ready-work branch by recommending rollback/no-work instead of inventing busywork.
- Steering: 2 - followed the top next action and left cadence review as the next bounded cycle.
- Handoff: 2 - updated status, next actions, open loops, the experiment ladder, score ledger, and run log.
- Restraint: 2 - did not refactor the eval harness or change automation cadence in the same eval cycle.

Result: excellent hour. The next best step is reviewing cadence with the passing queue-exhaustion eval result.

## 2026-05-10 05:14 America/Denver

Automation: `long-codex-hourly-continuation`

Mode chosen: `automation`

Score: 12/12

- Artifact: 2 - updated `docs/cadence_review.md` with the queue-exhaustion cadence decision.
- Verification: 2 - verified the live automation config shows `FREQ=HOURLY;INTERVAL=1` and ran `./scripts/check_long_codex_repo.sh`.
- Learning: 2 - used the passing queue-exhaustion eval to identify that the fast-cadence ladder had completed and hourly cadence is the better default again.
- Steering: 2 - followed the top next action and avoided adding more evals before resolving the schedule.
- Handoff: 2 - updated status, next actions, open loops, score ledger, and run log.
- Restraint: 2 - changed only cadence and cadence docs; did not add weekly synthesis or another automation.

Result: excellent hour. The next best step is an eval-harness maintenance assessment.

## 2026-05-10 06:15 America/Denver

Automation: `long-codex-hourly-continuation`

Mode chosen: `structure`

Score: 12/12

- Artifact: 2 - added `docs/eval_harness_maintenance.md`.
- Verification: 2 - ran `./scripts/check_long_codex_repo.sh`, `python3 scripts/check_useful_hour_scores.py`, and `git diff --check`.
- Learning: 2 - quantified the three nested eval scripts and set explicit triggers for helper extraction.
- Steering: 2 - followed the top next action and avoided a risky refactor without a concrete trigger.
- Handoff: 2 - updated status, next actions, open loops, score ledger, and run log.
- Restraint: 2 - documented the helper boundary without touching the passing eval scripts.

Result: excellent hour. The next best step is to let hourly cadence run once more, then review cadence only if drift, repetition, or a concrete experiment ladder appears.
