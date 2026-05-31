# Architecture Decision Records (ADRs)

This directory captures significant architectural decisions for ECC (`ecc-universal`).
Each ADR follows the format: **Context → Decision → Consequences**. ADRs are immutable once
accepted; supersede rather than edit.

| ADR | Title | Status |
|---|---|---|
| [ADR-001](ADR-001-content-as-data-installer-as-code.md) | Content-as-data, installer-as-code | Accepted |
| [ADR-002](ADR-002-per-harness-target-adapters.md) | Per-harness target adapters + manifest/schema layer | Accepted |
| [ADR-003](ADR-003-sqlite-install-state-store.md) | SQLite install-state store for drift & uninstall | Accepted |
| [ADR-004](ADR-004-provider-agnostic-llm-interface.md) | Provider-agnostic LLM interface with resolver | Accepted |
| [ADR-005](ADR-005-ecc2-isolated-alpha-crate.md) | `ecc2/` control plane as an isolated alpha crate | Accepted |
| [ADR-006](ADR-006-validation-as-the-gate.md) | CI validation, not runtime, is the content gate | Accepted |

These ADRs were reconstructed from the codebase structure and `git log` (PRs adding
harness adapters, the release approval gate, the `ecc-2.0` lane, and content validators).
