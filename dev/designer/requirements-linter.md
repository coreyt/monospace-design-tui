# Mono Designer DSL Linter Requirements

## Purpose

This document defines the requirements for a Mono Designer DSL Linter. The linter ensures that canonical YAML artifacts are not only structurally valid but also semantically consistent and aligned with the Monospace Design TUI standard.

## 1. Structural Validation (Level 1)

The linter must verify that the YAML file adheres to the Pydantic schemas defined in the `mono-designer` package.

- **Required Fields**: Ensure all mandatory fields (id, title, purpose, source, status) are present.
- **Type Safety**: Ensure field types match (e.g., `stages` is a list, `version` is a string).
- **Literal Constraints**: Validate that field values fall within allowed sets (e.g., `archetype` must be one of the supported 0.3.0 archetypes).

## 2. Cross-Artifact Consistency (Level 2)

The linter must verify relationships between different files in the designer package.

- **Workflow-Screen Mapping**: If a `ScreenSpec` references a `workflow_id`, verify that the corresponding `workflow.<id>.yaml` exists.
- **Stage-Screen Mapping**: If a `WorkflowSpec` stage lists `screen_ids`, verify those screens exist and are correctly typed.
- **Navigation Integrity**: Verify that `workspaces` referenced in `routes` are defined in the `workspaces` list.

## 3. Design Standard Compliance (Level 3)

The linter must enforce Monospace-specific design rules.

- **Region Naming**: Flag non-standard region IDs (e.g., prefer `region_a`, `region_b` over `left_box`).
- **Footer Discoverability**: Warning if a screen has actions but no `footer_keys` defined for them.
- **Focus Order**: Verify that all interactive components (inputs, lists, menus) are included in the `focus_order`.
- **Archetype Alignment**: Ensure that regions and components match the chosen archetype (e.g., an `editor` archetype should likely have a `region_b` or `region_c` role of "editor").

## 4. CLI Interface

The linter should be accessible via the `mono-designer` CLI.

- **Command**: `mono-designer lint <path_to_file_or_dir>`
- **Output**: 
  - Standard error format: `[FILE]:[LINE]:[COL] [LEVEL] [CODE] [MESSAGE]`
  - Exit code `0` on success, non-zero on Level 1/2 errors.
- **Fix Support**: Optionally provide suggestions for common standard violations.

## 5. Success Criteria

- The linter catches missing mandatory fields.
- The linter identifies broken links between screens and workflows.
- The linter warns when a screen violates Mono design patterns.
