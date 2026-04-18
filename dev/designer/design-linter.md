# Mono Designer DSL Linter Design

## Overview

The DSL Linter is a static analysis tool that validates Mono Designer artifacts. It operates as a pipeline of rules, progressing from basic structural integrity to high-level design system compliance.

## Architecture

The linter will be integrated into the `mono_designer` package under `mono_designer/core/linter.py`.

### Components

1.  **Registry**: A collection of named rules categorized by Level (1, 2, or 3).
2.  **Runner**: Orchestrates the execution of rules against a set of artifacts.
3.  **Reporter**: Formats and outputs violations.

## Implementation Strategy

### 1. Level 1: Schema Validation (JSON Schema)
Uses the canonical `dev/designer/mono-dsl.schema.json` file. This schema is programmatically generated from the Pydantic models in `mono_designer/models/`.
- **Approach**: The linter validates incoming YAML against the JSON Schema before attempting any model instantiation or higher-level heuristic checks.
- **Outcome**: Catch missing fields, invalid types, and literal violations with standardized error messages natively supported by IDEs.

### 2. Level 2: Consistency Engine
Validates relationships between multiple artifacts.
- **Approach**: Uses a `WorkspaceContext` object that loads all `.yaml` files in the target directory (and subdirectories) into a shared graph.
- **Path Resolution**: The linter recursively scans the execution root for `*.yaml` files with valid `artifact_type` keys, building an index of `id -> filepath`.
- **Example Rules**:
    - `CheckWorkflowExists`: Ensures a screen's `workflow_id` resolves to an ID in the `WorkspaceContext`.
    - `CheckScreenInWorkflow`: Ensures all `screen_ids` in a workflow stage exist in the `WorkspaceContext`.

### 3. Level 3: Design Standards (Heuristics)
Validates adherence to the Monospace TUI Standard.
- **Approach**: Pattern-matching against the validated models.
- **Project Overrides**: The `WorkspaceContext` looks for a `.monospace-tui.yaml` or `TUI-DESIGN.md` in the workspace root. If found, specific rules can be downgraded from "Error" to "Warning" or ignored entirely based on project-level decisions.
- **Example Rules**:
    - `RequireFooterKeys`: If `actions` exist, verify `footer_keys` contain matching keybindings.
    - `StrictRegionNaming`: Enforce the use of `region_a`, `region_b`, `region_c`.
    - `InteractiveFocus`: Verify all `input`, `list`, and `menu` components are present in `focus_order`.

## Opt-Out Mechanism (Inline Suppression)

Designers must be able to bypass heuristics during early drafting.
- YAML nodes can include a `notes` array.
- If a note contains `mono-lint-disable: <RULE_CODE>`, the linter suppresses that violation for that specific artifact.
- Example: `notes: ["mono-lint-disable: M302 (Strict Region Naming)"]`

## Rule Definition API

Rules should be defined as discrete functions or classes.

```python
class LintRule:
    code: str  # e.g., "M101"
    level: int # 1, 2, or 3
    message: str

    def check(self, artifact: BaseArtifact, context: WorkspaceContext) -> List[LintViolation]:
        pass
```

## CLI Integration

```bash
mono-designer lint ./designer-artifacts/
```

- If a directory is provided, the linter performs Level 2 cross-references.
- If a single file is provided, Level 2 checks are skipped or limited.
