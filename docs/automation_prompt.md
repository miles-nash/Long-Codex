# Canonical Hourly Heartbeat Prompt

Use this prompt for a thread heartbeat that keeps this work moving:

```text
Continue the Long Codex persistence project in /Users/milesnash/Documents/New project 6.

Use the $long-codex-cycle skill if it is available. First read AGENTS.md, docs/spec.md, docs/operating_loop.md, state/status.md, state/next_actions.md, the latest logs/*.md, and git status --short --branch.

Choose exactly one bounded cycle: research, structure, skill, automation, eval, or synthesis. Spend the cycle producing one durable artifact or one clearly logged negative result. Prefer the next action with the highest learning per minute. Use official OpenAI docs for OpenAI/Codex facts and use current web research when claims may have changed.

Before finishing, run ./scripts/check_long_codex_repo.sh, update state/status.md, update state/next_actions.md, add or update a logs/YYYY-MM-DD-*.md run note, and report changed files, verification result, and the next smallest useful step. Ask Miles only for concrete blockers.
```

## Stop Conditions

The heartbeat should stop and ask for help only if:

- a required credential or account permission is missing
- an automation or config change needs explicit user consent
- work risks spending money, publishing, contacting people, or deleting user data
- the repo state is contradictory enough that guessing would likely cause damage
