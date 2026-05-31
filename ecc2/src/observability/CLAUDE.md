# CLAUDE.md — ecc2/src/observability/

## Purpose
Risk scoring of agent tool calls and the event model that feeds the dashboard's risk view.

## Key Files
`mod.rs` (ToolCallEvent, RiskAssessment, SuggestedAction)

## Internal Architecture
Each `ToolCallEvent` (tool name, input/output summaries, duration, risk_score) is scored against `config::RiskThresholds` into a `RiskAssessment` (score + reasons + SuggestedAction). Persisted/queried via `session::store::StateStore`.

## Public Interface
`ToolCallEvent`, `RiskAssessment`, `SuggestedAction`, scoring fns.

## Dependencies
`serde`, `crate::config::RiskThresholds`, `crate::session::store::StateStore`.

## Dependents
`tui` renders risk; `comms` may escalate on high risk.

## Conventions
- Rust 2021; `anyhow::Result` for fallible app code, `thiserror` for typed errors.
- serde enums use `#[serde(rename_all = "snake_case")]`; provide `Default` where sensible.
- Share cross-module types via `crate::` paths rather than duplicating.

## Gotchas
- Risk thresholds (review/confirm) are config-driven; changing defaults changes operator gating behavior. Scores are f64 — compare with care.
- Alpha crate: APIs here are unstable and may change between commits.

## Testing
`cd ecc2 && cargo test`. Module tests live inline under `#[cfg(test)]`. Tests that touch
the working directory must use `crate::test_support::CurrentDirGuard`.
