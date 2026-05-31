# CLAUDE.md — integrations/

## Purpose
Optional, opt-in integrations with external systems. Currently the **AURA** trust-check
adapter (a read-only counterparty-reputation gate). Integrations are self-contained and
disabled until explicitly wired in.

## Key Files
| Path | Role |
|---|---|
| `aura/` | AURA trust-check adapter (Python, zero-dependency) |

## Internal Architecture
Each integration is a self-contained module a host project can vendor. AURA exposes a
read-only `GET /check?did=...` gate with fail-closed defaults; see `aura/CLAUDE.md`.

## Public Interface
Per-integration. AURA: `aura_verdict(did)`, `before_settle(did, allow=...)`,
`require_trust` (alias).

## Dependencies
Integration-specific. AURA is pure stdlib (no third-party imports).

## Dependents
Host agent projects that opt in; nothing in ECC depends on these by default.

## Conventions
- Integrations are opt-in and isolated; no global hooks or background calls.
- Document the trust boundary and failure mode (fail-open vs fail-closed) explicitly.

## Gotchas
- AURA is fail-closed by default (`unknown` verdict rejects); flipping to `fail_open=True`
  inverts that — a meaningful security decision.

## Testing
`integrations/aura/tests/` (pytest). See `aura/THREAT_MODEL.md` for the security boundary.
