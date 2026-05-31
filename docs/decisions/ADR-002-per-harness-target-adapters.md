# ADR-002: Per-harness target adapters + manifest/schema layer

## Status
Accepted

## Context
Each supported harness expects content in a different place and shape (`~/.claude/skills/`,
`.cursor/rules/`, Codex TOML config, OpenCode plugin format, etc.). Hardcoding harness
knowledge into the installer core would make the core grow and break every time a harness
was added. We also needed a declarative way to say *what* gets installed for a given profile.

## Decision
Separate **what** from **where**:
- *What* is declared as data in `manifests/` (`install-profiles.json` →
  `install-modules.json` → `install-components.json`) and validated against
  `schemas/install-*.schema.json` with `ajv`.
- *Where* is implemented by one adapter per harness under
  `scripts/lib/install-targets/<harness>.js`, registered in `registry.js`.

Adding a harness = adding one adapter module + a registry entry. Adding content = editing
a manifest, not the installer.

## Consequences
- Open/closed: the installer core is extended by adding adapters, not edited.
- New harness support (e.g. `claude-project`, `codebuddy-project`) lands as a small,
  testable adapter PR (see git history for `claude-project` adapter, PR #7004662-era).
- Manifests are fail-closed: a manifest that violates its schema blocks the install.
- The manifest/schema indirection adds a layer to learn, documented in `manifests/CLAUDE.md`
  and `schemas/CLAUDE.md`.
