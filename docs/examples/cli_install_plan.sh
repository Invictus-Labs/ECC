#!/usr/bin/env bash
# Inspect and plan an ECC install without writing anything, then read install state.
# Run from the repo root. Requires: npm install (Node >= 18).
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

echo "== Available install profiles & component IDs =="
node scripts/catalog.js --text

echo
echo "== Resolved install plan (dry inspect; nothing is written) =="
node scripts/install-plan.js

echo
echo "== Recommend components from a natural-language query =="
node scripts/consult.js "python backend with tdd and code review" || true

echo
echo "== Current install state for this context =="
node scripts/list-installed.js || echo "(no install state yet — run 'npx ecc <profile>' to install)"
node scripts/status.js || true
