# Mono Designer YAML Read/Write Specification

## Purpose

This document defines how the designer system should read and write canonical
YAML artifacts at `0.3.0`.

The goals are:

- predictable parsing
- stable output
- revision safety
- deterministic projection inputs

## Read Rules

## 1. Validate required fields

When reading a YAML artifact, the system must:

- confirm `version`
- confirm `artifact_type`
- confirm `id`
- confirm required artifact-specific fields

If validation fails:

- do not silently coerce invalid documents
- return a structured validation error

## 2. Preserve unknown fields

If a YAML file includes extra keys not used by the current tool:

- preserve them on write
- do not discard them silently

This is important for forward compatibility.

## 3. Normalize values

The read path may normalize:

- aliases
- shorthand values
- case differences where explicitly supported

But normalization must not erase meaning.

## 4. Keep IDs stable

On read, IDs should be treated as durable.

The system must not rename IDs unless:

- the user explicitly requested it, or
- the artifact is being created for the first time

## Write Rules

## 1. Write canonical ordering

Writers should emit YAML in a consistent field order.

Recommended order:

1. `version`
2. `artifact_type`
3. `id`
4. `title`
5. `purpose`
6. `source`
7. `status`
8. artifact-specific content
9. `notes`

## 2. Preserve stable structure

When revising an artifact:

- preserve stable IDs
- preserve unaffected sections
- update only the requested or derived parts

The system should avoid rewriting the full file unnecessarily.

## 3. Update timestamps

On write:

- keep `created_at` stable if present
- update `updated_at`

## 4. Record source intent

The writer should record enough source metadata to explain the artifact origin.

Suggested `source.kind` values:

- `generated`
- `revised`
- `imported`
- `manual`

## 5. Support review status transitions

Writers should allow updates to:

- `draft`
- `reviewed`
- `approved`

without forcing unrelated structure changes.

## Revision Semantics

The write path should support revision requests such as:

- add workspace
- remove workspace
- add workflow stage
- split workflow stage
- add screen
- revise screen purpose
- move component between regions
- add inspector pane
- revise footer keys

Revisions should be applied to YAML first, then reprojected to ASCII.

## Read/Write API Shape

Suggested Python module responsibilities:

- `load_navigation_spec(path) -> NavigationSpec`
- `load_workflow_spec(path) -> WorkflowSpec`
- `load_screen_spec(path) -> ScreenSpec`
- `save_navigation_spec(path, spec)`
- `save_workflow_spec(path, spec)`
- `save_screen_spec(path, spec)`
- `revise_spec(spec, revision_request) -> spec`

## Revision Request Shape

Suggested minimal structure:

```yaml
kind: revise-screen
target_id: rq-02
operations:
  - op: add-region
    type: inspector
  - op: move-component
    component_id: topic-summary
    to_region: region_c
```

## Canonical Flow

The correct `0.3.0` flow is:

1. read YAML
2. validate YAML
3. normalize semantic structure
4. apply revision if needed
5. write YAML
6. project YAML to ASCII

Never treat edited ASCII as the authoritative input path.
