#!/usr/bin/env bash
# SOCVault — Automated QA runner for STAGING
# Usage:
#   ./tests/qa/run-staging-qa.sh              # full suite
#   ./tests/qa/run-staging-qa.sh --pre-deploy # health only (before terraform apply)
#   ./tests/qa/run-staging-qa.sh --story US-005
#   ./tests/qa/run-staging-qa.sh --bruno      # also run Bruno collection if CLI installed
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

# Load config
if [[ -f tests/qa/config/staging.env ]]; then
  # shellcheck source=/dev/null
  source tests/qa/config/staging.env
fi

export STAGING_API_URL="${STAGING_API_URL:-https://api-staging.socvault.io/api/v1}"
export QA_LOG_DIR="${QA_LOG_DIR:-/tmp/socvault-qa}"
mkdir -p "$QA_LOG_DIR"

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'
FAILED=0

log() { echo "[qa] $*"; }
pass() { echo -e "${GREEN}[PASS]${NC} $*"; }
fail() { echo -e "${RED}[FAIL]${NC} $*"; FAILED=1; }

run_health() {
  log "Health check → ${STAGING_API_URL}/health"
  local code body
  body="$(curl -sf -w "\n%{http_code}" "${STAGING_API_URL}/health" 2>/dev/null || echo -e "\n000")"
  code="$(echo "$body" | tail -n1)"
  body="$(echo "$body" | sed '$d')"
  if [[ "$code" == "200" ]] && echo "$body" | grep -q '"status"'; then
    pass "T-PLAT-001 health ($code)"
  else
    fail "T-PLAT-001 health (HTTP $code)"
  fi
}

run_pytest() {
  local extra_args=()
  if [[ -n "${STORY_FILTER:-}" ]]; then
    extra_args=(-k "$STORY_FILTER")
  fi
  if command -v pytest >/dev/null 2>&1; then
    log "pytest tests/qa/api ${extra_args[*]:-}"
    if pytest tests/qa/api -v --tb=short "${extra_args[@]}" 2>&1 | tee "$QA_LOG_DIR/pytest.log"; then
      pass "pytest api suite"
    else
      fail "pytest api suite"
    fi
  else
    log "pytest not installed — skipping Python QA (pip install -r tests/qa/requirements.txt)"
  fi
}

run_bruno() {
  if [[ "${RUN_BRUNO:-0}" != "1" ]]; then
    return 0
  fi
  local bru_cmd=""
  if command -v bru >/dev/null 2>&1; then
    bru_cmd="bru"
  elif command -v npx >/dev/null 2>&1; then
    bru_cmd="npx @usebruno/cli"
  fi
  if [[ -z "$bru_cmd" ]]; then
    log "Bruno CLI not found — skip (--bruno ignored)"
    return 0
  fi
  log "Bruno collection → staging"
  if $bru_cmd run collections/bruno/SOCVault-MVP --env staging 2>&1 | tee "$QA_LOG_DIR/bruno.log"; then
    pass "Bruno staging collection"
  else
    fail "Bruno staging collection"
  fi
}

story_to_filter() {
  case "$1" in
    US-001|US-002) STORY_FILTER="freemail or signup" ;;
    US-003|US-004|US-005) STORY_FILTER="signup or otp or verify" ;;
    US-006|US-007) STORY_FILTER="auth or me or refresh" ;;
    US-008|US-009|US-010) STORY_FILTER="scan" ;;
    *) STORY_FILTER="" ;;
  esac
}

MODE="full"
STORY=""
RUN_BRUNO=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --pre-deploy) MODE="pre" ;;
    --story) STORY="$2"; shift ;;
    --bruno) RUN_BRUNO=1 ;;
    -h|--help)
      sed -n '2,8p' "$0" | tail -n +2
      exit 0
      ;;
    *) fail "Unknown arg: $1"; exit 1 ;;
  esac
  shift
done

log "SOCVault staging QA — mode=$MODE api=$STAGING_API_URL"
[[ -n "$STORY" ]] && story_to_filter "$STORY" && log "Story filter: $STORY → pytest -k '$STORY_FILTER'"

run_health

if [[ "$MODE" == "pre" ]]; then
  [[ $FAILED -eq 0 ]] && pass "Pre-deploy QA complete" || fail "Pre-deploy QA failed"
  exit $FAILED
fi

run_pytest
run_bruno

if [[ $FAILED -eq 0 ]]; then
  pass "Staging QA complete"
else
  fail "Staging QA failed — see $QA_LOG_DIR"
fi
exit $FAILED
