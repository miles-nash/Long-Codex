# Run Log: Initial Long Codex Scaffold

Date: 2026-05-06

## Goal

Research how to make Codex sessions run longer and provide more value, then modify the local system so future sessions can persist and improve.

## What Happened

- Inspected the workspace. It was an empty Git repo with no commits and no remote.
- Inspected Codex config and existing automations.
- Researched official OpenAI Codex docs, automations, memories, AGENTS.md, skills, non-interactive mode, compaction, and eval practices.
- Checked current long-horizon agent research and METR time-horizon framing.
- Created a file-based persistence scaffold in this repo.
- Prepared a repo-scoped skill and canonical hourly heartbeat prompt.
- Enabled Codex memories in `~/.codex/config.toml`.
- Created active thread heartbeat automation `long-codex-hourly-continuation`.
- Connected the empty GitHub repo `miles-nash/Long-Codex` as `origin`.
- Pushed the initial scaffold to `origin/main`.

## Key Takeaway

Longer Codex sessions need less mysticism and more bookkeeping. The useful pattern is an external memory loop: spec, plan, status, verification, log, repeat.

## Verification

Initial verification target:

```sh
./scripts/check_long_codex_repo.sh
```

## Next

Observe whether the first `long-codex-hourly-continuation` wakeup can follow the durable state without reorientation drag.
