# CLAUDE.md — ecc2/src/worktree/

## Purpose
Git worktree management for per-session isolation, plus merge-readiness detection so the operator knows if a session's branch is mergeable.

## Key Files
`mod.rs` (MergeReadiness, worktree create/inspect via git2)

## Internal Architecture
Uses `git2` (and shelling out via `std::process::Command` where needed) to create worktrees, hash content (`sha2`), and compute `MergeReadiness` (Ready vs Conflicted with a conflict list).

## Public Interface
`MergeReadiness`, `MergeReadinessStatus`, worktree creation/inspection fns; `WorktreeInfo` from `session`.

## Dependencies
`git2` (vendored-openssl), `sha2`, `crate::config`, `crate::session::WorktreeInfo`.

## Dependents
`session`/`tui` for per-session worktrees and merge status.

## Conventions
- Rust 2021; `anyhow::Result` for fallible app code, `thiserror` for typed errors.
- serde enums use `#[serde(rename_all = "snake_case")]`; provide `Default` where sensible.
- Share cross-module types via `crate::` paths rather than duplicating.

## Gotchas
- `git2` builds vendored OpenSSL — needs a C toolchain. Merge-readiness is advisory; it does not perform the merge.
- Alpha crate: APIs here are unstable and may change between commits.

## Testing
`cd ecc2 && cargo test`. Module tests live inline under `#[cfg(test)]`. Tests that touch
the working directory must use `crate::test_support::CurrentDirGuard`.
