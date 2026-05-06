# Status

Last updated: 2026-05-06

## Current State

The repo now has an initial long-horizon Codex scaffold:

- mission and constraints in `docs/spec.md`
- repeatable operating loop in `docs/operating_loop.md`
- first research distillation in `docs/research/2026-05-06-long-horizon-codex.md`
- canonical hourly automation prompt in `docs/automation_prompt.md`
- repo-scoped skill in `.agents/skills/long-codex-cycle/SKILL.md`
- lightweight structural check in `scripts/check_long_codex_repo.sh`
- active thread heartbeat automation `long-codex-hourly-continuation`
- GitHub remote `origin` set to `https://github.com/miles-nash/Long-Codex.git`
- initial scaffold commit `4a8ad38`; latest pushed handoff commit `aa4fec7`

## Decisions

- Use markdown files as the source of truth, with Codex memories as a secondary recall layer.
- Use a thread heartbeat for continuity when the same conversation should keep waking up.
- Keep cycles bounded by artifact, verification, and handoff rather than by ambition.
- Treat evals as part of the system, starting with cheap deterministic structure checks.
- Enable Codex memories in `~/.codex/config.toml`, but keep required guidance in repo files.

## Known Gaps

- No empirical `codex exec --json` eval suite exists yet.
- The repo has not yet accumulated multiple hourly run logs, so the synthesis layer is thin.
- The automation needs to be observed after its first wakeup and adjusted if the prompt is too vague or too heavy.

## Recovery Instructions

If a future session is disoriented, do this:

1. Read `README.md` and `AGENTS.md`.
2. Run `./scripts/check_long_codex_repo.sh`.
3. Read this file and `state/next_actions.md`.
4. Pick the first not-done next action that is still relevant.
5. Leave a log before stopping.
