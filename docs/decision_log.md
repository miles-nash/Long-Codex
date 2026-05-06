# Decision Log

## 2026-05-06: File-Based Memory First

Decision: Use checked-in markdown files as the source of truth for mission, state, research, and handoff.

Reason: Official Codex guidance favors `AGENTS.md`, skills, and durable project context. Research on memory systems points toward layered, inspectable state rather than a single opaque context.

## 2026-05-06: Thread Heartbeat For Continuity

Decision: Use a heartbeat automation attached to this thread for hourly continuation.

Reason: The work benefits from preserving the conversation and making repeated improvements in the same context.

## 2026-05-06: Repo Skill Defines Method

Decision: Put the repeated long-run procedure in `.agents/skills/long-codex-cycle/SKILL.md`.

Reason: Skills define reusable method; automations define schedule.

## 2026-05-06: Add Steering Before More Machinery

Decision: Add `docs/automation_steering.md` and a useful-hour scorecard before building heavier orchestration.

Reason: The next bottleneck is not storage capacity. It is choosing useful work and proving the hour mattered.

## 2026-05-06: Run Codex Evals In Temporary Copies

Decision: `scripts/eval_long_codex_cycle.py` runs nested `codex exec --json` smoke tests in a temporary copy of the repo with `workspace-write` sandboxing and `approval_policy="never"`.

Reason: The eval should measure whether the long-codex cycle can update durable state without risking the live project, changing automations, committing, or pushing.
