---
title: "§R5 Shadow Rendering"
description: "Shadow algorithm, shadow cell attributes, and scrim rendering for modal overlays"
weight: 5
---

## §R5.1 Algorithm

Shadows create depth illusion for Level 2–4 elements (Standard [§6.4](/standard/borders/#64-shadow-rendering)).

**Offset:** 2 columns right, 1 row down from the bordered element's edges.

**Rendering steps:**

1. Record the character content in cells that will be covered by shadow.
2. Apply dim attribute (SGR 2) to those cells, preserving character codes.
3. Shadow cells form an L-shape: the right edge (2 cols wide, full height of element) and the bottom edge (full width of element, 1 row tall), excluding the overlap with the element itself.

**Visual diagram:**

```
┌──────────┐
│ Content  │░░
│          │░░
└──────────┘░░
  ░░░░░░░░░░░░
```

Where `░` represents shadow cells (underlying characters rendered dim).

## §R5.2 Shadow Cell Attribute

In 16-color mode, shadow cells use attribute byte `0x08` (dark gray foreground on black background), preserving the original character code. In 256-color or truecolor mode, shadow cells apply SGR 2 (dim) to whatever attributes the underlying cell had.

## §R5.3 Scrim Rendering

Scrims create a dimmed backdrop behind Level 4 modal overlays (Standard [§6.5](/standard/borders/#65-scrim)).

**Rendering steps:**

1. Determine the bounding rectangle of the modal overlay (including its border and shadow).
2. For every cell **outside** the modal's bounding rectangle, apply SGR 2 (dim) while preserving the cell's existing character code and foreground color.
3. The modal itself renders normally (no dim) at its elevation level.
4. When the modal is dismissed, restore all cells to their original attributes.

**Capability degradation:**

| Color Mode | Scrim Rendering |
|-----------|----------------|
| Truecolor | SGR 2 (dim) on all background cells |
| 256-color | SGR 2 (dim) on all background cells |
| 16-color | SGR 2 (dim) on all background cells |
| Monochrome | No scrim — modal distinguished by double-line border only |
