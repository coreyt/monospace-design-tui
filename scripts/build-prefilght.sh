#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WEBSITE_DIR="$ROOT_DIR/website"
WORKFLOW_FILE="$ROOT_DIR/.github/workflows/hugo.yml"
EXPECTED_HUGO_VERSION="${EXPECTED_HUGO_VERSION:-0.147.0}"
BUILD_BASE_URL="${BUILD_BASE_URL:-https://example.invalid/monospace-design-tui/}"

cd "$ROOT_DIR"

echo "==> Preflight: environment"
command -v hugo >/dev/null
command -v rg >/dev/null
command -v git >/dev/null
command -v python3 >/dev/null

HUGO_VERSION_OUTPUT="$(hugo version)"
echo "$HUGO_VERSION_OUTPUT"
case "$HUGO_VERSION_OUTPUT" in
  *"v${EXPECTED_HUGO_VERSION}"*"+extended"*) ;;
  *)
    echo "Expected Hugo Extended ${EXPECTED_HUGO_VERSION}, got: $HUGO_VERSION_OUTPUT" >&2
    exit 1
    ;;
esac

echo "==> Preflight: workflow version check"
rg -n "HUGO_VERSION: \"${EXPECTED_HUGO_VERSION}\"" "$WORKFLOW_FILE" >/dev/null

echo "==> Preflight: shell syntax"
if [ -d "$ROOT_DIR/scripts" ]; then
  while IFS= read -r script; do
    bash -n "$script"
  done < <(find "$ROOT_DIR/scripts" -type f -name '*.sh' | sort)
fi

echo "==> Preflight: trailing whitespace"
if rg -n "[[:blank:]]$" \
  "$ROOT_DIR/.github" \
  "$ROOT_DIR/website" \
  "$ROOT_DIR/README.md" \
  "$ROOT_DIR"/*.md \
  "$ROOT_DIR"/scripts/*.sh \
  >/tmp/mono-tui-preflight-trailing-whitespace.txt 2>/dev/null; then
  cat /tmp/mono-tui-preflight-trailing-whitespace.txt
  echo "Trailing whitespace found." >&2
  exit 1
fi

echo "==> Preflight: required docs exist"
test -f "$ROOT_DIR/monospace-tui-design-standard.md"
test -f "$ROOT_DIR/monospace-tui-pattern-library.md"
test -f "$WEBSITE_DIR/content/patterns/_index.md"

echo "==> Preflight: markdown footnotes resolve"
python3 - <<'PY'
from pathlib import Path
import re
import sys

paths = [
    Path("monospace-tui-design-standard.md"),
    Path("monospace-tui-pattern-library.md"),
    Path("website/content/standard/_index.md"),
    Path("website/content/standard/keyboard.md"),
    Path("website/content/standard/navigation.md"),
    Path("website/content/patterns/_index.md"),
]

ref_re = re.compile(r"\[\^([^\]]+)\]")
def_re = re.compile(r"^\[\^([^\]]+)\]:", re.MULTILINE)

errors = []
for path in paths:
    text = path.read_text()
    refs = set(ref_re.findall(text))
    defs = set(def_re.findall(text))
    missing = sorted(refs - defs)
    if missing:
      errors.append(f"{path}: missing footnote definitions for {', '.join(missing)}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
PY

echo "==> Preflight: Git whitespace check"
git diff --check -- . ':(exclude)website/public'

echo "==> Preflight: Hugo build"
rm -rf "$WEBSITE_DIR/public"
HUGO_ENVIRONMENT="${HUGO_ENVIRONMENT:-production}" TZ="${TZ:-America/Chicago}" hugo --minify --source "$WEBSITE_DIR" --baseURL "$BUILD_BASE_URL"
test -f "$WEBSITE_DIR/public/index.html"
test -f "$WEBSITE_DIR/public/patterns/index.html"

echo "Preflight passed."
