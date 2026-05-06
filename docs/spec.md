# Spec: Long Codex Persistence

Date: 2026-05-06

## Mission

Make Codex sessions persist longer and provide more value across hour-scale and multi-day work.

This repo should help future sessions:

- start quickly
- stay coherent
- choose valuable work
- verify progress
- remember what happened
- recover from context loss or automation wakeups

## User Goal

The user wants a Codex system that can use hourly automations to keep working productively, learn from each run, and improve its own structure over time.

## Hard Constraints

- Durable state must live in files, not only in chat.
- Each cycle must produce a concrete artifact or a clear negative result.
- Future sessions should be able to resume by reading a small, named set of files.
- Automations should avoid vague prompts. They need the task, state files, stop conditions, and reporting expectations.
- New complexity must earn its keep.

## Non-Goals

- Do not build a giant orchestration framework before the file-based loop is proven.
- Do not depend on hidden chain-of-thought or unrecoverable context.
- Do not create unattended workflows that can spend money, contact people, publish, trade, or access secrets without explicit approval.
- Do not optimize for "agent stays busy" over "agent leaves useful evidence."

## Working Hypothesis

Long Codex improves through four layers:

1. External memory: specs, plans, logs, decisions, and next actions.
2. Cadence: heartbeat automations that wake the same thread for continuity.
3. Reusable procedure: repo skill plus AGENTS guidance.
4. Evaluation: lightweight checks that measure whether the process improved.

## Definition Of Done

The system is better when a fresh Codex session can:

- identify the mission and current state in under five minutes
- select a next action without asking the user
- spend a bounded cycle on useful work
- verify at least one thing
- update the durable state
- leave the next session with less ambiguity than it inherited
