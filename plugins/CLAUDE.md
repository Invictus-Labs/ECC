# CLAUDE.md — plugins/

## Purpose
Plugin-distribution surface for ECC (the repo ships as a Claude Code / harness plugin via
`.claude-plugin/`, `.codex-plugin/`, etc.). This directory currently holds plugin
documentation.

## Key Files
| File | Role |
|---|---|
| `README.md` | Plugin overview / pointer to the plugin manifests |

## Internal Architecture
The actual plugin manifests live in the dotfile plugin dirs (`.claude-plugin/`,
`.codex-plugin/`) and are validated against `schemas/plugin.schema.json`. This directory
documents the plugin story.

## Public Interface
Documentation only here; the installable plugin is defined by the `.‹harness›-plugin/`
manifests and `package.json` `files`.

## Dependencies
`schemas/plugin.schema.json` (validates the real manifests).

## Dependents
Marketplace/plugin install flows; `tests/plugin-manifest.test.js`.

## Conventions
- Keep plugin docs in sync with the actual `.*-plugin/` manifests.
- Plugin root resolution is handled by the hook bootstrap (see `hooks/CLAUDE.md`).

## Gotchas
- Don't confuse this docs dir with the dotfile plugin manifest dirs that actually define the
  installable plugin.

## Testing
`tests/plugin-manifest.test.js` validates the plugin manifest surface.
