# CLAUDE.md — legacy-command-shims/

## Purpose
Backward-compatibility shims for commands that were renamed/moved, so old invocations keep
working after `commands/` reorganizations.

## Key Files
| Path | Role |
|---|---|
| `commands/` | Shim command files (e.g. `agent-sort.md`, `claw.md`, `context-budget.md`, `devfleet.md`, `docs.md`) |
| `README.md` | Why shims exist + the deprecation policy |

## Internal Architecture
Each shim is a thin command file that points users at the current command name, preserving the
old entrypoint during a deprecation window.

## Public Interface
Old slash-command names; they resolve/redirect to the current commands in `commands/`.

## Dependencies
The current `commands/` they alias.

## Dependents
Users with muscle-memory/scripts on old command names; the command registry.

## Conventions
- A shim names its replacement clearly.
- Remove shims only after the deprecation window; track in the legacy-artifact inventory.

## Gotchas
- Shims still pass command validation — keep their frontmatter valid.
- `tests/docs/legacy-artifact-inventory.test.js` tracks what's deprecated.

## Testing
`scripts/ci/validate-commands.js`; `tests/docs/legacy-artifact-inventory.test.js`.
