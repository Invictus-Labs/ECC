# CLAUDE.md — ecc2/

## Purpose
The Rust-based **ECC 2.0 control plane** (`ecc-tui`, alpha). It is the layer *above*
individual harness installs: manage many agent sessions from one surface, track session
state/output/risk, and provide worktree-aware orchestration. See ADR-005 — it is an
isolated crate, NOT part of the npm package.

## Key Files
| Path | Role |
|---|---|
| `Cargo.toml` | Crate manifest (`ecc-tui`, edition 2021) |
| `src/main.rs` | Entrypoint; module wiring; test-support current-dir guard |
| `src/tui/` | `ratatui` terminal UI (app, dashboard, widgets) |
| `src/session/` | Session manager, daemon, store (SQLite), runtime, output |
| `src/worktree/` | Git worktree creation + merge-readiness checks (`git2`) |
| `src/observability/` | Tool-call events + risk scoring |
| `src/comms/` | Task/notification messaging primitives (priority queue) |
| `src/config/` | Config model (layouts, risk thresholds, keybindings) |
| `src/notifications.rs` | Desktop/webhook/completion-summary notifications |

## Internal Architecture
`tokio` async runtime drives a `ratatui` TUI. Sessions are created/tracked by `session/`,
persisted in SQLite via `session/store.rs`, and can detach as a background `daemon.rs`.
`observability/` scores each tool call against `config` risk thresholds and surfaces it in
the dashboard. `worktree/` integrates `git2` for per-session worktrees and merge readiness.

## Public Interface
A CLI/TUI binary (`cargo run` → `ecc-tui`). Internally, modules expose Rust APIs
(`StateStore`, `SessionManager`, `RiskAssessment`, `MergeReadiness`, `Config`).

## Dependencies
`ratatui`, `crossterm`, `tokio`, `rusqlite` (bundled), `git2` (vendored OpenSSL), `serde`,
`clap`, `tracing`, `anyhow`/`thiserror`, `chrono`, `cron`, `uuid`, `dirs`.

## Dependents
Standalone. The npm installer and `src/llm/` do not depend on it.

## Conventions
- `#[serde(rename_all = "snake_case")]` on enums; `Default` impls for config types.
- Errors via `anyhow::Result` in app code, `thiserror` for typed errors.
- Tests serialize current-dir mutation through `test_support::CurrentDirGuard` (a process
  Mutex) — never `set_current_dir` in a test without the guard.

## Gotchas
- Alpha quality + unstable API; do not wire into the stable installer.
- `default = ["vendored-openssl"]` — a C toolchain is required to build `git2`.
- SQLite is bundled via `rusqlite` feature; no system sqlite needed.

## Testing
`cd ecc2 && cargo test`. Build a release binary with `cargo build --release`
(→ `target/release/ecc-tui`). Set `RUST_LOG=ecc_tui=debug` for verbose tracing.
