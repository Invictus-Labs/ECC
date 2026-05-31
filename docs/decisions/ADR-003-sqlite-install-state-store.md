# ADR-003: SQLite install-state store for drift detection & uninstall

## Status
Accepted

## Context
Installs are stateful: ECC writes files into a user's harness directories. Users need to
know what ECC manages, detect when those files drift (manually edited or deleted), repair
them, and cleanly uninstall. Scanning the filesystem on every query is slow and ambiguous
(we cannot tell an ECC-managed file from a user file without provenance).

## Decision
Persist install state in a **SQLite state store** (`scripts/lib/state-store/`, accessed via
`sql.js`), recording installed components, target paths, and provenance/hashes
(`schemas/provenance.schema.json`, `schemas/install-state.schema.json`). Operator commands
`status`, `list-installed`, `doctor`, `repair`, and `uninstall` read/write this store.

## Consequences
- `doctor` can detect drift by comparing recorded hashes to on-disk content.
- `repair` and `uninstall` are reliable because ECC knows exactly what it wrote.
- The store is a durable cache; losing it degrades drift detection but not the ability to
  re-install.
- State store schema migrations live in `scripts/lib/state-store/migrations.js`.
