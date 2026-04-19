#!/usr/bin/env bash
# build-preflight.sh - Verifies that the Monospace Designer repository is healthy before distribution.

set -e # Exit immediately if a command exits with a non-zero status.

echo "🚀 Running Monospace Designer Pre-flight Checks..."

# 1. Check Python Linter (Ruff)
echo "🐍 Running Python Linters (Ruff)..."
if command -v ruff >/dev/null 2>&1; then
    ruff check mono-designer/ mcp-server/
    ruff format --check mono-designer/ mcp-server/
else
    echo "⚠️  Ruff not found. Skipping Python linting. (Install with: pip install ruff)"
fi

# 2. Run Python Tests (Pytest)
echo "🧪 Running Python Unit Tests..."
export PYTHONPATH=$(pwd)/mono-designer
pytest mono-designer/tests/

# 3. Check Go Linter
echo "🐹 Running Go Linters (golangci-lint)..."
if command -v golangci-lint >/dev/null 2>&1; then
    (cd mono-designer-verify && golangci-lint run)
else
    echo "⚠️  golangci-lint not found. Skipping Go linting. (Install with: go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest)"
fi

# 4. Run Go Tests
echo "🧪 Running Go Unit Tests..."
(cd mono-designer-verify && go test -v ./...)

# 5. E2E Output Verification
echo "🔍 Validating all 0.3.0 YAML Examples..."
export PYTHONPATH=$(pwd)/mono-designer
python3 -m mono_designer.cli.main lint dev/designer/examples/

echo "✅ All pre-flight checks passed! The 0.3.0 release is healthy."
