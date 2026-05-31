# CLAUDE.md — ecc2/src/

## Purpose
Source root of the `ecc-tui` crate. `main.rs` wires the modules and starts the TUI; each
subdirectory is a self-contained concern of the control plane.

## Key Files
| File/Dir | Role |
|---|---|
| `main.rs` | Module declarations, binary entrypoint, test current-dir guard |
| `notifications.rs` | Desktop / webhook / completion-summary notification configs |
| `tui/` | Terminal UI |
| `session/` | Session lifecycle + persistence |
| `worktree/` | Git worktree management |
| `observability/` | Risk scoring + tool-call events |
| `comms/` | Messaging / task priority |
| `config/` | Configuration model |

## Internal Architecture
`main.rs` declares `mod comms; mod config; mod notifications; mod observability; mod session;
mod tui; mod worktree;` and boots the async TUI. Cross-module types are shared via
`crate::` paths (e.g. `crate::session::store::StateStore`, `crate::config::Config`).

## Public Interface
The crate compiles to one binary. Modules expose `pub` items consumed across the crate.

## Dependencies
See `ecc2/Cargo.toml`. Inter-module: `config` is foundational; `session`, `observability`,
`worktree`, `comms` all reference it.

## Dependents
Only the `ecc-tui` binary.

## Conventions
- Keep one concern per module directory; share types through `crate::`.
- Public enums derive `Serialize`/`Deserialize` with snake_case rename for SQLite/JSON.

## Gotchas
- `main.rs` contains `#[cfg(test)] test_support` with a global `CURRENT_DIR_LOCK` Mutex;
  any test that changes the working directory MUST use `CurrentDirGuard::enter`.

## Testing
`cargo test` from `ecc2/`. Tests live alongside modules (`#[cfg(test)]`).
