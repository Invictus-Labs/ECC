# CLAUDE.md — src/llm/cli/

## Purpose
Interactive command-line provider/model selector. Backs the `llm-select` console script and
`python -m llm` GUI launcher.

## Key Files
| File | Role |
|---|---|
| `selector.py` | `interactive_select()` + `main()` entrypoint |
| `__init__.py` | Package surface |

## Internal Architecture
`selector.main()` drives an interactive prompt that lets a user pick a `ProviderType` and a
model, persisting the choice (e.g. to `.llm.env`) so subsequent `get_provider()` calls pick
it up via the resolver order.

## Public Interface
- `interactive_select(...)` — programmatic selection helper (re-exported from `llm`).
- `main()` — console entrypoint, wired as `llm-select` in `pyproject.toml [project.scripts]`.

## Dependencies
`core/types.ProviderType`, `providers/resolver` for available providers/models. Standard lib
for terminal interaction.

## Dependents
`llm-select` console script; `llm.gui()` in the package `__init__`.

## Conventions
- Selection persists to the same `.llm.env` the resolver reads, so CLI and library agree.
- Keep prompts non-interactive-safe (degrade gracefully when stdin is not a TTY).

## Gotchas
- Writing `.llm.env` changes resolver behavior process-wide for later runs in that directory.
- The module starts minimal (`from __future__ import annotations`); confirm current contents
  before assuming richer helpers exist.

## Testing
Covered indirectly via resolver tests; selector logic should be exercised with stdin mocking
when adding interactive behavior. No persistent server/daemon here.
