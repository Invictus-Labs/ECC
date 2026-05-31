# ADR-005: ecc2/ control plane as an isolated alpha crate

## Status
Accepted

## Context
ECC 2.0 aims to be the layer *above* individual harness installs: manage many agent
sessions from one surface, track session state/output/risk, and add orchestration and
worktree management. This is GA-track but actively churning. Wiring it into the stable npm
package would let alpha instability break the production installer.

## Decision
Implement the control plane as a **separate Rust crate** in `ecc2/` (`ecc-tui`), using
`ratatui`/`crossterm` for the TUI, `tokio` for async, `rusqlite` for the session store, and
`git2` for worktree integration. It is **not** included in the npm `files` list and is not
installed by `npx ecc`. It is built and tested independently with `cargo`.

## Consequences
- The stable installer never depends on `ecc2/` build health.
- `ecc2/` can iterate at alpha speed; it is explicitly labelled alpha in `ecc2/README.md`.
- Contributors must have a Rust toolchain only if they touch `ecc2/`.
- Two languages of "operator tooling" coexist (Node CLI for installs, Rust for sessions)
  until ECC 2.0 GA consolidates them.
