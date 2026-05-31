# CLAUDE.md — ecc2/src/tui/

## Purpose
The `ratatui`/`crossterm` terminal UI: the dashboard, app event loop, and reusable widgets that visualize sessions and risk.

## Key Files
`mod.rs` (module wiring), `app.rs` (event loop + state), `dashboard.rs` (layout), `widgets.rs` (reusable UI)

## Internal Architecture
`app.rs` runs the input/render loop, dispatching key events (mapped via `config` keybindings) and rendering `dashboard.rs`, which composes `widgets.rs`. Reads session + risk data from other modules.

## Public Interface
`app` is `pub`; `dashboard`/`widgets` are crate-private.

## Dependencies
`ratatui`, `crossterm`, `crate::session`, `crate::observability`, `crate::config`.

## Dependents
`main.rs` boots the TUI.

## Conventions
- Rust 2021; `anyhow::Result` for fallible app code, `thiserror` for typed errors.
- serde enums use `#[serde(rename_all = "snake_case")]`; provide `Default` where sensible.
- Share cross-module types via `crate::` paths rather than duplicating.

## Gotchas
- Keybindings come from `config`; do not hardcode keys. Rendering must stay non-blocking — long work belongs in `session`/daemon, not the render loop.
- Alpha crate: APIs here are unstable and may change between commits.

## Testing
`cd ecc2 && cargo test`. Module tests live inline under `#[cfg(test)]`. Tests that touch
the working directory must use `crate::test_support::CurrentDirGuard`.
