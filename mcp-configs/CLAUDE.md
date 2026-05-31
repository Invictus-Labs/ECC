# CLAUDE.md — mcp-configs/

## Purpose
Catalog of MCP (Model Context Protocol) server configurations users can install into a
harness — Jira, GitHub, and others. Reference configs with placeholder credentials.

## Key Files
| File | Role |
|---|---|
| `mcp-servers.json` | Map of server id → `{command, args, env, description}` |

## Internal Architecture
Each entry specifies how to launch an MCP server (`command` + `args`), required `env` (with
`YOUR_*_HERE` placeholders), and a human description. Merged into a harness's MCP config by
the installer (Codex via `scripts/codex/merge-mcp-config.js`).

## Public Interface
Consumed by the installer's MCP merge logic and `.mcp.json` tooling.

## Dependencies
The actual MCP server binaries (`uvx`, `npx` packages) at runtime — not bundled.

## Dependents
Install-target adapters that wire MCP; `tests/docs/mcp-management-docs.test.js`.

## Conventions
- NEVER commit real credentials — use `YOUR_*_HERE` placeholders.
- Include a `description` for every server.

## Gotchas
- Placeholders must be replaced by the user post-install; the installer does not inject secrets.
- A new server sharing an account/webhook must be source-guarded by its consumer (general
  ecosystem rule), not assumed isolated.

## Testing
`tests/docs/mcp-management-docs.test.js`; JSON shape validated where schema'd.
