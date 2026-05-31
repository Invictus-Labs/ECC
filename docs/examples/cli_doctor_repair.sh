#!/usr/bin/env bash
# Detect drift in ECC-managed files and repair it.
# Run from the repo root. Requires: npm install (Node >= 18).
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

echo "== Diagnose missing or drifted ECC-managed files =="
if node scripts/doctor.js; then
  echo "doctor: no drift detected."
else
  echo
  echo "doctor reported drift; attempting repair..."
  node scripts/repair.js
  echo
  echo "re-running doctor to confirm..."
  node scripts/doctor.js
fi
