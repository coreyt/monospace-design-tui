# Mono Designer DSL Specification

## Purpose

This document specifies the **minimal Mono DSL** for `0.3.0`.

At this stage, the DSL is not intended to be a large hand-authored language.
It is a small semantic layer used to preserve structure between:

- canonical YAML specs
- ASCII projections
- future prototype/runtime projections

## Design Constraints

The `0.3.0` DSL must:

- stay small
- be easy to validate in Python
- map cleanly from YAML artifacts
- preserve enough semantics for ASCII generation
- avoid framework-specific constructs

The `0.3.0` DSL must not:

- become a full rendering language
- encode Textual/Bubble Tea specifics
- try to solve future runtime behavior exhaustively

## Core Concepts

The DSL must be able to represent:

- regions
- components
- focus targets
- transitions
- footer keys
- inspector panes
- actions
- state

## Top-Level DSL Objects

## 1. `navigation`

Represents the application-level structure.

Required fields:

- `id`
- `title`
- `workspaces`
- `routes`
- `rules`

## 2. `workflow`

Represents a user flow or task sequence.

Required fields:

- `id`
- `title`
- `purpose`
- `entry_conditions`
- `exit_conditions`
- `stages`
- `transitions`
- `checkpoints`

## 3. `screen`

Represents a single TUI screen.

Required fields:

- `id`
- `title`
- `purpose`
- `regions`
- `components`
- `actions`
- `focus`
- `transitions`

## Screen DSL

## Regions

### Definition

A named structural area of a screen.

Supported region types for `0.3.0`:

- `header`
- `region_a`
- `region_b`
- `region_c`
- `footer`
- `modal`
- `inspector`

Required region fields:

- `id`
- `type`
- `role`
- `contents`

Optional region fields:

- `width`
- `height`
- `visible`

## Components

### Definition

A semantic UI element placed in a region.

Supported component types for `0.3.0`:

- `menu`
- `list`
- `table`
- `form`
- `summary`
- `detail`
- `status`
- `actions`
- `progress`
- `text`
- `input`
- `footer_keys`

Required component fields:

- `id`
- `type`
- `region`
- `purpose`

Optional component fields:

- `items`
- `fields`
- `columns`
- `status_kind`
- `notes`

## Focus Targets

### Definition

The semantic objects that can own input focus.

Required focus fields:

- `default_target`
- `focus_order`

Optional fields:

- `focus_rules`
- `suppressed_keys_when_input_focused`

## Transitions

### Definition

A semantic description of where the user can go next.

Supported transition types for `0.3.0`:

- `push`
- `pop`
- `switch`
- `modal`
- `advance`
- `return`
- `jump`

Required transition fields:

- `id`
- `type`
- `trigger`
- `target`

Optional fields:

- `condition`
- `notes`

## Footer Keys

### Definition

The visible current-context keyboard hints for the screen.

Required fields:

- `bindings`

Each binding includes:

- `key`
- `label`
- `scope`

## Inspector Panes

### Definition

A screen region or component that provides contextual detail without changing
the primary workflow location.

For `0.3.0`, an inspector pane is represented as:

- a `region` with type `inspector`, or
- a `component` of type `detail` within `region_c`

## Actions

### Definition

Operations available on the screen.

Required fields:

- `id`
- `label`
- `target`
- `kind`

Supported action kinds:

- `global`
- `selection_local`
- `workflow`
- `review`

## State

### Definition

The visible interaction or review state relevant to the screen.

Supported state concepts for `0.3.0`:

- `default`
- `focused`
- `selected`
- `disabled`
- `warning`
- `error`
- `review_required`
- `approved`

This is not yet a full runtime state machine.

## Normalization Rules

The DSL should normalize different YAML shapes into one semantic model.

Examples:

- `detail pane`, `inspector`, and `context pane` should normalize to either:
  - region type `inspector`, or
  - component type `detail`
- footer key strips should normalize to component type `footer_keys`
- screen-local action groups should normalize to component type `actions`

## Authoring Model

At `0.3.0`, the DSL is primarily:

- machine-generated
- machine-normalized
- machine-validated

Humans may inspect it, but it is not yet optimized as a primary authored
language.

## Output Expectations

The DSL must support projection into:

- navigation ASCII
- workflow ASCII
- screen wireframe ASCII

Later releases may add prototype/runtime projections from the same DSL.
