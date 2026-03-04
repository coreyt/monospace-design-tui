---
title: "§9 Accessibility"
description: "Dual-rendering architecture, scrolling regions, text labels, contrast, focus visibility"
weight: 9
---

## §9.1 Dual-Rendering Architecture

Applications SHOULD implement a dual-rendering architecture:

1. **Visual renderer** — ANSI escape sequences for sighted users (standard rendering).
2. **Linear semantic renderer** — Sequential text output without cursor jumping, suitable for screen readers.

The linear renderer SHOULD output content in reading order (top-to-bottom, left-to-right) with clear section labels. (Terminal §6 screen reader accessibility)

## §9.2 Scrolling Regions

Applications SHOULD use VT100 scrolling regions (`ESC[{top};{bottom}r`) for content that updates independently of the rest of the screen (e.g., log tails, data feeds). This reduces full-screen redraws that disrupt screen readers. (Terminal §6)

## §9.3 Text Labels

All interactive elements MUST have text labels that convey their purpose independent of visual position. A button that says "OK" MUST be in a context where its purpose is unambiguous, or it MUST have an associated label (e.g., dialog title "Delete file?"). (Apple HIG §4)

## §9.4 Color Independence

Restated for emphasis: Color MUST NOT be the sole indicator of any state or meaning ([§5.3](/standard/color/#53-color-independence)). This is a hard accessibility requirement, not a suggestion.

## §9.5 Minimum Contrast

When using truecolor (24-bit color):

- Body text MUST have a contrast ratio of at least **4.5:1** against its background.
- Bold or Display text MUST have a contrast ratio of at least **3:1** against its background.

When using 16 or 256 indexed colors, applications SHOULD select color pairs known to meet these ratios on common terminal themes. (Apple HIG §4 contrast requirements, WCAG 2.1 AA)

## §9.6 Focus Visibility

The focus indicator MUST be visible at all times ([§8.2](/standard/state/#82-focus-invariant)). The focus indicator MUST NOT rely solely on color — it MUST use reverse video, bracket markers, or border change. (Apple HIG §4)
