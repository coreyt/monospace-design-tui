---
title: "§6 Border & Elevation"
description: "Five elevation levels, active/inactive borders, window titles, shadow rendering, scrim"
weight: 6
---

## §6.1 Elevation Levels

Applications MUST use exactly 5 elevation levels:

| Level | Use | Border Style | Shadow |
|-------|-----|-------------|--------|
| 0 | Inline content, flat text | None | None |
| 1 | Panels, content regions | Single-line (`─│┌┐└┘`) | None |
| 2 | Menus, dropdowns | Single-line (`─│┌┐└┘`) | 2-col × 1-row offset |
| 3 | Dialogs, secondary windows | Double-line (`═║╔╗╚╝`) | 2-col × 1-row offset |
| 4 | Modal overlays | Double-line (`═║╔╗╚╝`) | 2-col × 1-row + background scrim (dim) |

Applications MUST NOT use double-line borders for Level 0–2 elements. Applications MUST NOT use single-line borders for Level 3–4 elements. (OS/2 §2 window decoration, M3 §3 elevation levels, monospace-design-tui-research.md cross-cutting synthesis)

## §6.2 Active/Inactive Window Borders

- Active (focused) windows: MUST use double-line borders (`═║╔╗╚╝`).
- Inactive (unfocused) windows: MUST use single-line borders (`─│┌┐└┘`).

This rule applies to **overlapping windows** (Level 3–4) that can independently gain or lose focus. The following are exempt and retain their elevation-defined border style regardless of focus:

- **Panels within a non-overlapping layout** ([§1.3](/standard/layout/#13-three-region-layout)) — SHOULD use single-line borders (Level 1).
- **Menus and dropdowns** (Level 2) — MUST use single-line borders; focus is indicated by the highlight bar on the selected item, not by border change.

(OS/2 §2, CUA §1)

## §6.3 Window Titles

Window and panel titles MUST be centered in the top border row:

```
╔══ Dialog Title ══════════════╗
┌── Panel Title ───────────────┐
```

The title text MUST be padded with at least one space on each side within the border. (OS/2 §2)

## §6.4 Shadow Rendering

Shadows at Levels 2–4 MUST be rendered as a 2-column × 1-row offset below and to the right of the bordered element. Shadow cells MUST:

- Preserve the underlying character codes.
- Apply attribute 0x08 (dim) to the underlying characters.

(OS/2 §2 shadow specification, Turbo Vision §7)

## §6.5 Scrim

Level 4 (modal overlay) MUST dim all background content behind the modal. The scrim MUST apply the dim attribute (SGR 2) to all non-modal cells while preserving their character content. (M3 §3 elevation)

## §6.6 Rounded Corners

Rounded corner characters (`╭╮╰╯`) MAY be used for cosmetic, non-interactive containers (e.g., decorative cards, informational callouts). Rounded corners MUST NOT be used for interactive windows, dialogs, or panels that participate in the elevation system. (Terminal §6 Unicode box drawing)
