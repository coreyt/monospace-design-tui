---
title: "§8 State Model"
description: "Six mandatory states plus error, focus invariant, disabled visibility"
weight: 8
---

## §8.1 Required States

Every interactive element MUST support and render these 6 mandatory states plus 1 conditional state:

| State | Rendering | Rule |
|-------|-----------|------|
| Enabled | Normal attributes (Body typography) | Default state for all interactive elements |
| Focused | Reverse video (SGR 7) or bracket markers `[▸ item ◂]` | Exactly one element MUST be focused at all times |
| Hovered | Underline (SGR 4) or highlight bar | Mouse-optional; render only if mouse tracking is active |
| Pressed | Brief reverse flash (≤100ms) | Visual feedback for activation; revert to Focused after |
| Selected | Reverse video + fill mark (`[X]` or `(*)`) | For multi-select contexts and radio/checkbox groups |
| Disabled | Dim (SGR 2) | Visible but non-interactive; MUST NOT be hidden ([§3.4](/standard/navigation/#34-unavailable-items)) |
| Error | Red foreground (SGR 31) or red background (SGR 41) | MUST include text explanation ([§7.3](/standard/typography/#73-error-text)) |

## §8.2 Focus Invariant

Exactly one interactive element MUST hold focus at all times. There MUST NOT be a state where no element is focused. When a focused element is removed from the screen (e.g., dialog closes), focus MUST transfer to the most recently focused element on the underlying screen. (CUA §1, Apple HIG §4 focus management)

## §8.3 Disabled Visibility

Disabled elements MUST remain visible in their normal position. Applications MUST NOT hide, remove, or reposition disabled elements. This ensures users can discover features and understand the complete interface surface. (CUA §1, [§3.4](/standard/navigation/#34-unavailable-items))
