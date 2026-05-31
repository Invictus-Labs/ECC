# CLAUDE.md — rules/

## Purpose
Always-follow guideline sets, organized by language/domain (21 groups). Rules encode coding
style, security, and testing requirements that agents should treat as standing constraints.

## Key Files
| Subdir | Scope |
|---|---|
| `common/` | Cross-language rules |
| `python/`, `golang/`, `java/`, `kotlin/`, `rust/`, `csharp/`, `typescript/`, `react/`, `web/` | Language/framework rules |
| `cpp/`, `dart/`, `swift/`, `php/`, `ruby/`, `perl/`, `angular/`, `fsharp/`, `arkts/` | More languages |
| `zh/` | Localized rules |

## Internal Architecture
Each subdirectory holds Markdown rule files. Rules are concise, imperative, and meant to be
injected as standing context for the relevant language/domain.

## Public Interface
Referenced by `commands/`, `agents/`, and the installer's profiles (a language profile
installs that language's rules + skills).

## Dependencies
Data only. Validated by `scripts/ci/validate-rules.js`.

## Dependents
Install profiles (`manifests/`), `agents/`, `commands/`; `tests/ci/validators.test.js`.

## Conventions
- One concern per rule; keep them short and testable.
- Group by language/domain directory; lowercase-with-hyphens filenames.

## Gotchas
- Rules are standing constraints — overly broad rules cause unwanted agent behavior.
- Localized rule sets (`zh/`) must stay consistent with their source.

## Testing
`scripts/ci/validate-rules.js`; consistency via the catalog/registry checks.
