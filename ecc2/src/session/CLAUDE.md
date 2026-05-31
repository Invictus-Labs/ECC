# CLAUDE.md — ecc2/src/session/

## Purpose
Session lifecycle: create/start/stop/resume agent sessions, persist them in SQLite, and run a detachable background daemon.

## Key Files
`mod.rs` (HarnessKind, session types), `manager.rs` (lifecycle), `daemon.rs` (background mode), `store.rs` (SQLite StateStore), `runtime.rs`, `output.rs` (captured output)

## Internal Architecture
`manager.rs` owns lifecycle and writes through `store.rs` (SQLite). `daemon.rs` detaches a session to run in the background. `output.rs` captures and streams session stdout/stderr; `runtime.rs` holds run-time state. `HarnessKind` enumerates Claude/Codex/OpenCode/Gemini/Cursor/Unknown.

## Public Interface
`StateStore`, `SessionManager`, session/worktree info structs, `HarnessKind`.

## Dependencies
`rusqlite`, `tokio`, `serde`, `chrono`, `uuid`, `crate::config`.

## Dependents
`tui` (renders sessions), `observability` (reads store), `worktree` (WorktreeInfo).

## Conventions
- Rust 2021; `anyhow::Result` for fallible app code, `thiserror` for typed errors.
- serde enums use `#[serde(rename_all = "snake_case")]`; provide `Default` where sensible.
- Share cross-module types via `crate::` paths rather than duplicating.

## Gotchas
- SQLite schema lives here; migrations must preserve existing session rows. Daemon detachment uses `libc`; be careful with process lifetime on stop.
- Alpha crate: APIs here are unstable and may change between commits.

## Testing
`cd ecc2 && cargo test`. Module tests live inline under `#[cfg(test)]`. Tests that touch
the working directory must use `crate::test_support::CurrentDirGuard`.
