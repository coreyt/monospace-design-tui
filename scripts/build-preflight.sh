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
    (cd mono-designer-verify && golangci-lint run main.go verify.go)
else
    echo "⚠️  golangci-lint not found. Skipping Go linting. (Install with: go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest)"
fi

# 4. Run Go Tests
echo "🧪 Running Go Unit Tests..."
(cd mono-designer-verify && go test -v ./...)

# 5. Check embedded verifier schema
echo "🔍 Checking embedded verifier schema..."
cmp dev/designer/mono-dsl.schema.json mono-designer-verify/schema/mono-dsl.schema.json

# 6. Lint examples
echo "🔍 Linting all 0.3.0 YAML examples..."
export PYTHONPATH=$(pwd)/mono-designer
python3 -m mono_designer.cli.main lint dev/designer/examples/

# 7. E2E Output Verification
echo "🔍 Verifying YAML examples against ASCII projections..."
while IFS= read -r dsl_file; do
    ascii_file="$(dirname "$dsl_file")/ascii.txt"
    if [ -f "$ascii_file" ]; then
        (cd mono-designer-verify && go run . verify "../$dsl_file" "../$ascii_file" >/dev/null)
    fi
done < <(find dev/designer/examples -name dsl.yaml | sort)

echo "✅ All pre-flight checks passed! The 0.3.0 release is healthy."
