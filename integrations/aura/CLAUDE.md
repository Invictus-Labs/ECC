# CLAUDE.md — integrations/aura/

## Purpose
A zero-dependency, read-only AURA trust-check adapter: gate a sensitive action (settlement,
delegation, tool execution) behind a backward-looking trust verdict for a *counterparty*
agent. It makes one HTTP GET and returns a verdict. It does NOT sign, hold keys, move funds,
or touch wallets.

## Key Files
| File | Role |
|---|---|
| `adapter.py` | The adapter: `aura_verdict`, `before_settle`/`require_trust`, `AuraVerdict`, `AuraUntrusted` |
| `__init__.py` | Package surface |
| `README.md` | Usage + enable instructions |
| `THREAT_MODEL.md` | Security boundary and threat model |
| `tests/` | `test_adapter.py`, `fixtures.py` |

## Internal Architecture
`aura_verdict(did)` performs one `GET /check?did=...` via `urllib` (no auth) and returns an
`AuraVerdict`; it never raises on network failure (returns `unknown`). `before_settle` raises
`AuraUntrusted` when the verdict is not allowed. Fail-closed by default: `unknown` is rejected
unless `fail_open=True`.

## Public Interface
- `aura_verdict(did) -> AuraVerdict` — never raises on network errors.
- `before_settle(did, allow=...) -> AuraVerdict` — raises `AuraUntrusted` on distrust.
- `require_trust` — alias of `before_settle`.

## Dependencies
Python stdlib only (`urllib`, `json`, `dataclasses`). No `pip install` required — vendor the
folder.

## Dependents
Host projects that opt in at a trust boundary; AURA is not auto-wired anywhere in ECC.

## Conventions
- Read-only, no secrets, no coupling — preserve these invariants.
- Call the gate explicitly at the action you protect; no global hooks.

## Gotchas
- Fail-closed vs fail-open is a deliberate security choice; default rejects `unknown`.
- The endpoint is public/unauthenticated by design — do not add credentials.

## Testing
`pytest integrations/aura/tests/`. Tests use `fixtures.py` to mock the HTTP verdict;
`THREAT_MODEL.md` documents what is and isn't defended.
