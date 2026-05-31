# CLAUDE.md — ecc2/src/config/

## Purpose
The configuration model: pane layouts, risk thresholds, keybindings, and notification settings for the control plane.

## Key Files
`mod.rs` (PaneLayout, RiskThresholds, ResolvedAgentProfile, keybinding parsing)

## Internal Architecture
Defines serde-(de)serializable config types with defaults. Parses keybindings into `crossterm` `KeyEvent`s (via `regex`). `RiskThresholds` (review/confirm) feed `observability`.

## Public Interface
`Config`, `RiskThresholds`, `PaneLayout`, `ResolvedAgentProfile` (aliased as `SessionAgentProfile`).

## Dependencies
`serde`, `crossterm` (KeyEvent), `regex`, `crate::notifications`.

## Dependents
Nearly every module: `session`, `tui`, `observability`, `worktree`.

## Conventions
- Rust 2021; `anyhow::Result` for fallible app code, `thiserror` for typed errors.
- serde enums use `#[serde(rename_all = "snake_case")]`; provide `Default` where sensible.
- Share cross-module types via `crate::` paths rather than duplicating.

## Gotchas
- Foundational module — changing a config type ripples widely. `#[serde(default)]` is used so partial configs load; keep defaults sane.
- Alpha crate: APIs here are unstable and may change between commits.

## Testing
`cd ecc2 && cargo test`. Module tests live inline under `#[cfg(test)]`. Tests that touch
the working directory must use `crate::test_support::CurrentDirGuard`.
