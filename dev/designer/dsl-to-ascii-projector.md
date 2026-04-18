# Mono Designer DSL-to-ASCII Projector Specification

## Purpose

This document specifies the `0.3.0` ASCII projector.

The projector converts canonical YAML artifacts, via the normalized minimal
semantic layer, into reviewable ASCII outputs.

Primary outputs:

- navigation overview ASCII
- workflow ASCII
- screen wireframe ASCII

## Projector Goals

- deterministic output
- stable formatting
- readable in chats, docs, and diffs
- preserve enough structure for human review
- avoid premature visual polish

## Projector Inputs

The projector accepts:

- normalized navigation artifact
- normalized workflow artifact
- normalized screen artifact

The projector should not accept:

- raw user prose
- freeform edited ASCII as canonical input

## Projector Outputs

## 1. Navigation ASCII

Purpose:

- show overall workspace structure and major paths

Should include:

- application title
- workspace list
- major route summaries
- root navigation hints

## 2. Workflow ASCII

Purpose:

- show ordered stages and review checkpoints

Should include:

- workflow title
- stages in order
- transitions
- checkpoint markers
- linked screens where useful

## 3. Screen Wireframe ASCII

Purpose:

- show a structural TUI screen layout

Should include:

- title/header
- major regions
- component labels
- footer key strip
- obvious inspector/detail placement if present

## Rendering Rules

## 1. Borders

Use Mono-consistent box-drawing characters.

Default `0.3.0` wireframe style:

- single-line borders
- no decorative rendering
- no color in the canonical ASCII artifact

## 2. Region labeling

Regions should be labeled by role, not by implementation detail.

Examples:

- `Header`
- `Region A`
- `Region B`
- `Region C`
- `Inspector`
- `Footer Key Strip`

## 3. Component rendering

Components should be shown as semantic placeholders, not final content.

Examples:

- `topic list`
- `request summary`
- `coverage summary`
- `actions`
- `detail pane`

## 4. Focus hints

If focus matters materially, the wireframe may indicate:

- default focus target
- focused surface

But only at a low-fidelity level.

Examples:

- `> current row`
- `[focused]`

## 5. State hints

The projector may include low-fidelity state hints where necessary.

Examples:

- `approved`
- `review required`
- `warning`
- `in progress`

These are annotations, not runtime state displays.

## Layout Rules

## Navigation Overview

Prefer vertical workspace lists and short path summaries.

## Workflow Projection

Prefer top-to-bottom stage order.

Checkpoint locations should be clear.

## Screen Projection

Prefer the Mono shell structure when applicable:

- header
- main regions
- footer

If the screen is modal, focused, or hybrid, reflect that explicitly.

## Projection Determinism

For the same normalized artifact, the projector must produce the same ASCII.

This matters for:

- review
- diffing
- HITL revision

## Projector API Shape

Suggested Python API:

- `project_navigation_ascii(spec) -> str`
- `project_workflow_ascii(spec) -> str`
- `project_screen_ascii(spec) -> str`

## Error Handling

If the artifact is incomplete:

- fail with a clear validation error, or
- emit a clearly marked partial wireframe

The projector must not silently invent missing structure.

## Relationship to Future Work

At `0.3.0`, ASCII is the main projection target.

Later releases may project the same semantic layer into:

- interactive prototypes
- framework-target outputs
- richer runtime previews

This projector should therefore remain:

- semantic
- deterministic
- projection-oriented

not presentation-heavy.
