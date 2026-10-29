#!/usr/bin/env bash
# Run from the repository root after installing requirements and starting the API.
# Captures real cURL responses from the local service; it does not fabricate output.
set -euo pipefail
BASE_URL="${BASE_URL:-http://127.0.0.1:5000}"
OUT_DIR="${OUT_DIR:-submission-evidence}"
mkdir -p "$OUT_DIR"

capture() {
  local name="$1"; shift
  {
    printf '$'
    printf ' %q' "$@"
    printf '\n\n'
    "$@"
    printf '\n'
  } | tee "$OUT_DIR/$name"
}

capture rest-create-done.txt curl -sS -i -X POST "$BASE_URL/accounts" \
  -H 'Content-Type: application/json' \
  -d '{"name":"Evidence User","email":"evidence-user@example.com","address":"123 Example Road","phone_number":"555-0100"}'
capture rest-list-done.txt curl -sS -i "$BASE_URL/accounts"
capture rest-read-done.txt curl -sS -i "$BASE_URL/accounts/1"
capture rest-update-done.txt curl -sS -i -X PUT "$BASE_URL/accounts/1" \
  -H 'Content-Type: application/json' \
  -d '{"name":"Evidence User","email":"evidence-user@example.com","address":"123 Example Road","phone_number":"555-0101"}'
capture rest-delete-done.txt curl -sS -i -X DELETE "$BASE_URL/accounts/1"
echo "Captured live cURL responses in $OUT_DIR. Check the account ID and HTTP statuses before submission."
