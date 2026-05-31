# CLAUDE.md — contexts/

## Purpose
Reusable context presets that bias an agent toward a working mode. Each file is a curated
bundle of priorities/conventions for a phase of work.

## Key Files
| File | Mode |
|---|---|
| `dev.md` | Development context (build/iterate) |
| `research.md` | Research/discovery context |
| `review.md` | Review/QA context |

## Internal Architecture
Markdown documents loaded as context to shape agent behavior for a session phase. They layer
on top of rules/skills, not replace them.

## Public Interface
Referenced by commands/workflows that switch context; installed per-harness where supported.

## Dependencies
Data only.

## Dependents
Commands/workflows that set a working mode; localized copies under `docs/<locale>/contexts/`.

## Conventions
- Keep each context focused on one mode; avoid duplicating rule content — reference it.
- lowercase-with-hyphens filenames.

## Gotchas
- Contexts are additive; conflicting contexts loaded together produce mixed signals.
- Keep in sync with localized versions under `docs/*/contexts/`.

## Testing
Covered indirectly by docs/consistency tests. Pure content; no runtime behavior.
