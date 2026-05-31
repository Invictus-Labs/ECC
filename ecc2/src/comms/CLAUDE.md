# CLAUDE.md — ecc2/src/comms/

## Purpose
Messaging and task-priority primitives used to coordinate and notify across sessions.

## Key Files
`mod.rs` (TaskPriority and messaging types)

## Internal Architecture
Defines a `TaskPriority` ordering (Low<Normal<High<Critical) and message/task structures persisted via `session::store::StateStore`. Drives notification escalation.

## Public Interface
`TaskPriority` (Ord), message/task structs.

## Dependencies
`serde`, `crate::session::store::StateStore`.

## Dependents
`tui`, `notifications`, `observability` (escalation).

## Conventions
- Rust 2021; `anyhow::Result` for fallible app code, `thiserror` for typed errors.
- serde enums use `#[serde(rename_all = "snake_case")]`; provide `Default` where sensible.
- Share cross-module types via `crate::` paths rather than duplicating.

## Gotchas
- `TaskPriority` derives `Ord`; comparisons depend on the declared variant order — do not reorder the enum.
- Alpha crate: APIs here are unstable and may change between commits.

## Testing
`cd ecc2 && cargo test`. Module tests live inline under `#[cfg(test)]`. Tests that touch
the working directory must use `crate::test_support::CurrentDirGuard`.
