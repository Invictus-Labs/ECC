# CLAUDE.md — scripts/lib/state-store/

## Purpose
The SQLite-backed install-state store (via `sql.js`). Records what ECC installed, where, and
with what provenance, enabling `doctor`/`repair`/`status`/`uninstall` and drift detection
(ADR-003).

## Key Files
| File | Role |
|---|---|
| `schema.js` | Table/column definitions |
| `migrations.js` | Forward migrations preserving existing rows |
| `queries.js` | Read/write query helpers |
| `index.js` | Store facade (open/init/query) |

## Internal Architecture
`index.js` opens the SQLite DB (`sql.js`), runs `migrations.js` to bring the schema current
(`schema.js`), then exposes `queries.js` helpers. Provenance/hashes (per
`schemas/provenance.schema.json` and `install-state.schema.json`) let `doctor` compare
on-disk content to recorded state.

## Public Interface
`StateStore`-style facade: open, record install, query installed components, detect drift.
Consumed by `status.js`, `list-installed.js`, `doctor.js`, `repair.js`, `uninstall.js`,
`sessions-cli.js`.

## Dependencies
`sql.js`. Node `fs`/`path`.

## Dependents
All operator/read commands and the install apply path.

## Conventions
- Every schema change ships a migration; never mutate existing rows destructively.
- Store provenance/hash so drift detection stays accurate.

## Gotchas
- `sql.js` is an in-memory WASM SQLite; the DB is serialized to disk — ensure flushes on write.
- Losing the store degrades drift detection but not the ability to re-install.

## Testing
`tests/lib/*` cover store init/query/migration behavior.
