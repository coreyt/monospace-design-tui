# Mono Designer YAML Specification

## Purpose

This document specifies the canonical YAML artifacts for `0.3.0`.

These YAML files are the source of truth for the designer system.

Primary artifact types:

- navigation spec
- workflow spec
- screen spec

## Shared Rules

All YAML artifacts should:

- use stable IDs
- include `version`
- include `artifact_type`
- include `created_at`
- include `updated_at`
- include `source`
- include `status`

Supported `status` values for `0.3.0`:

- `draft`
- `reviewed`
- `approved`

## 1. Navigation Spec

Suggested filename:

- `nav.<id>.yaml`

Required fields:

```yaml
version: "0.3.0"
artifact_type: navigation
id: nav-main
title: Main Navigation
purpose: Stable root navigation for the application
source:
  kind: generated
  inputs: []
status: draft
workspaces: []
routes: []
rules: []
```

### `workspaces`

Each workspace includes:

- `id`
- `label`
- `purpose`

### `routes`

Each route includes:

- `from`
- `to`
- `kind`
- `notes`

### `rules`

Short navigation rules such as:

- root invariants
- cross-workspace movement rules
- back behavior

## 2. Workflow Spec

Suggested filename:

- `workflow.<id>.yaml`

Required fields:

```yaml
version: "0.3.0"
artifact_type: workflow
id: rq-collection
title: Research Collection
purpose: Collect and review evidence for a topic
source:
  kind: generated
  inputs: []
status: draft
entry_conditions: []
exit_conditions: []
stages: []
transitions: []
checkpoints: []
assumptions: []
linked_screens: []
```

### `stages`

Each stage includes:

- `id`
- `label`
- `purpose`
- `screen_ids`

### `transitions`

Each transition includes:

- `from`
- `to`
- `trigger`
- `kind`

### `checkpoints`

Each checkpoint includes:

- `id`
- `label`
- `type`
- `stage_id`

Supported `type` values:

- `approve`
- `revise`
- `continue`
- `cancel`
- `collect_more`
- `publish`

## 3. Screen Spec

Suggested filename:

- `screen.<id>.yaml`

Required fields:

```yaml
version: "0.3.0"
artifact_type: screen
id: rq-02
title: Scope Refinement Review
purpose: Review and adjust proposed dimensions before collection
source:
  kind: generated
  inputs: []
status: draft
workflow_id: rq-collection
archetype: admin
patterns: []
entry_conditions: []
regions: []
components: []
actions: []
focus:
  default_target: ""
  focus_order: []
transitions: []
footer_keys: []
notes: []
```

### `archetype`

Supported `0.3.0` archetype values:

- `dashboard`
- `admin`
- `file-manager`
- `editor`
- `fuzzy-finder`
- `hybrid`

### `patterns`

Named Mono patterns, such as:

- `focused-surface`
- `master-detail`
- `object-local-actions`
- `command-jump`
- `live-drill-down`

### `regions`

Each region includes:

- `id`
- `type`
- `role`
- `contents`

### `components`

Each component includes:

- `id`
- `type`
- `region`
- `purpose`

### `actions`

Each action includes:

- `id`
- `label`
- `target`
- `kind`

### `footer_keys`

Each key includes:

- `key`
- `label`
- `scope`

## YAML Directory Layout

Suggested `0.3.0` storage layout:

```text
.monospace-tui/designer/
  nav/
    nav-main.yaml
  workflows/
    workflow.rq-collection.yaml
  screens/
    screen.nav-01.yaml
    screen.rq-01.yaml
    screen.rq-02.yaml
```

## Canonical Rule

At `0.3.0`:

- YAML is canonical
- ASCII is projected
- direct manual editing of ASCII should not be treated as authoritative
