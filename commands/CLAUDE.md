# CLAUDE.md — commands/

## Purpose
Slash-command definitions (79 files) invoked by users (`/tdd`, `/plan`, `/e2e`,
`/code-review`, `/build-fix`, `/learn`, …). Markdown with `description` frontmatter and a
command body describing the workflow.

## Key Files
| File (examples) | Command |
|---|---|
| `code-review.md` | `/code-review` |
| `build-fix.md` | `/build-fix` |
| `checkpoint.md`, `aside.md` | session control |
| `cost-report.md` | cost reporting |
| `cpp-build.md` / `cpp-review.md` / `cpp-test.md` | language-specific |
| `ecc-guide.md` | onboarding/help |

## Internal Architecture
Each file declares a command via frontmatter (at minimum `description`) and a body that
instructs the agent. Commands are indexed into a generated command registry
(`scripts/ci/generate-command-registry.js`).

## Public Interface
One slash command per file. Installed into the harness's command location by the target
adapter.

## Dependencies
May reference `agents/`, `skills/`, and `rules/`. Validated by
`scripts/ci/validate-commands.js`.

## Dependents
Users; the command registry; `tests/commands/`.

## Conventions
- lowercase-with-hyphens filenames; one command per file.
- Keep frontmatter valid; regenerate the registry after adding/removing commands
  (`npm run command-registry:write`).

## Gotchas
- Adding a command without regenerating the registry fails `command-registry:check` in CI.
- `legacy-command-shims/` provides backward-compatible aliases for renamed commands.

## Testing
`scripts/ci/validate-commands.js`, `tests/commands/command-frontmatter.test.js`,
`tests/ci/command-registry.test.js`.
