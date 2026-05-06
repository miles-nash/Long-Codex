# Long Codex Workbench

This repo is a durability layer for making Codex sessions run longer and produce more value.

The core idea is simple: do not ask future sessions to remember the project from chat. Put the goal, plan, current status, evidence, and operating loop in files that Codex can reread every time it wakes up.

## Start Here

1. Read [AGENTS.md](AGENTS.md).
2. Read [docs/spec.md](docs/spec.md).
3. Read [docs/operating_loop.md](docs/operating_loop.md).
4. Read [state/status.md](state/status.md) and [state/next_actions.md](state/next_actions.md).
5. Read the latest file in [logs/](logs).
6. Pick one bounded cycle, do it, verify it, and update the durable state.

## Current Shape

- `docs/spec.md`: mission, constraints, non-goals, definition of done.
- `docs/operating_loop.md`: the repeatable cycle each long-running session should follow.
- `docs/research/`: distilled research and source notes.
- `state/status.md`: current project state and decisions.
- `state/next_actions.md`: prioritized queue for the next automation.
- `logs/`: timestamped run notes.
- `.agents/skills/long-codex-cycle/SKILL.md`: repo-scoped skill for future Codex runs.
- `scripts/check_long_codex_repo.sh`: lightweight structure check.

## First Principle

Long-horizon agent work is less like a heroic single thought and more like a lab notebook with hands. Keep the notebook excellent.
