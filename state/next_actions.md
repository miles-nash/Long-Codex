# Next Actions

Last updated: 2026-05-06

## Priority Queue

1. Observe the first `long-codex-hourly-continuation` wakeup and check whether it resumes from durable files without asking unnecessary questions.
2. Add a tiny `codex exec --json` eval that verifies `$long-codex-cycle` produces a log and updates `state/status.md`.
3. Improve `scripts/check_long_codex_repo.sh` to detect stale status files and missing source links.
4. Distill the next research layer: compare MUSE, H2R, MemoryAgentBench, and OpenAI Codex practices into a concrete memory architecture.
5. Add a `docs/decision_log.md` once there are at least five meaningful decisions.
6. After the first automation wakeup, review the run log and tighten the heartbeat prompt if it wandered or repeated work.

## Parking Lot

- Explore whether a global user skill is useful after the repo skill proves itself.
- Consider a weekly synthesis automation that compresses logs into principles.
- Build a scorecard for "useful hour" quality: artifact, verification, novelty, handoff clarity, and token efficiency.
