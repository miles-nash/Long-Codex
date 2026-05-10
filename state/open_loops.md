# Open Loops

Last updated: 2026-05-10

## Purpose

Separate active blockers, active follow-ups, parked ideas, and retired ideas so future sessions do not confuse "not now" with "blocked" or "never again."

## Active Blockers

- None currently. The repo check passes, the eval summaries are passing, and the active heartbeat automation is still useful.

## Active Follow-Ups

| Item | Why It Matters | Evidence | Next Action |
| --- | --- | --- | --- |
| Source-ledger freshness | New research notes can land without a corresponding source-ledger date check. | `docs/source_ledger.md`, `docs/research/2026-05-08-agent-artifact-handoffs.md`, `scripts/check_long_codex_repo.sh` | Add a lightweight freshness check for source-ledger date versus latest research note date. |
| Cadence watchpoints | The faster cadence is still active and useful, but should slow down if value drops. | `docs/cadence_review.md`, `state/useful_hour_scores.md`, `logs/2026-05-08T2248Z-current-practices-harvest.md`, `logs/2026-05-10T0638Z-subagent-handoff-rule.md` | Revisit only if a watchpoint triggers or after two more heartbeat runs. |

## Parked Ideas

- Global user skill: wait until the repo-scoped skill proves stable across more cycles.
- Shared eval harness module: wait until a third eval creates real duplication.
- Expanded useful-hour scorecard: keep the current scorecard until runs reveal missing dimensions.
- Eval summary usage policy revisit: the current decision is to keep compact `usage` fields; reopen only if summaries become noisy or expensive.
- Useful-hour behavior eval: wait until the score ledger shape is checked or manual scoring proves insufficient.
- Useful-hour score ledger check exceptions: revisit only if a real blocked run scores below 7 and needs explicit syntax.
- Weekly synthesis automation: wait until logs become repetitive or hard to scan.
- Parallel subagent cycles: wait until a cycle has genuinely independent branches and can use artifact handoffs.
- Subagent handoff drift check: add only if the operating loop and repo skill diverge later.

## Retired Ideas

- Bigger heartbeat prompt as the default solution: retired for now because source ledgers, checks, and skills carry state more cleanly.
- Filename sort for latest log: retired because modification time is the repo rule.
- Summary-only memory: retired because source-backed claims should point to durable local evidence.
- Duplicate automation for faster cadence: retired because updating the existing heartbeat preserves continuity.
- Eval summary usage decision: resolved in `docs/eval_summary_policy.md`.
- Post-open-loop heartbeat trend synthesis: resolved in `docs/heartbeat_synthesis.md`; keep the heartbeat as-is and defer weekly synthesis automation.
- Useful-hour score ledger consistency: resolved in `scripts/check_useful_hour_scores.py`.
- Faster-cadence review: resolved in `docs/cadence_review.md`; keep 30-minute heartbeat active while watchpoints stay clear.
- Current-practices harvest: resolved in `docs/research/2026-05-08-agent-artifact-handoffs.md` and `docs/source_ledger.md`.
- Subagent artifact handoff rule: resolved in `docs/operating_loop.md` and `.agents/skills/long-codex-cycle/SKILL.md`.
- Post-review cadence check: resolved in `docs/cadence_review.md`; keep 30-minute heartbeat active while watchpoints stay clear.
