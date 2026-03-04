---
title: "§1 Grid & Layout"
description: "Atomic unit, spacing scale, three-region layout, footer key strip, breakpoints"
weight: 1
---

## §1.1 Atomic Unit

The atomic unit of all Monospace TUI measurement is **1 character cell** (1 column × 1 row). All spacing, sizing, and positioning values in this standard are expressed in character cells unless stated otherwise. (CUA §2, M3 §3 cross-cutting synthesis)

## §1.2 Spacing Scale

Applications MUST use the following spacing scale for all padding, margins, and gaps:

```
0  1  2  3  4  6  8
```

Values are in character cells. Intermediate values (5, 7) MUST NOT be used. (M3 §3 spacing tokens → character-cell mapping)

## §1.3 Three-Region Layout

Every screen MUST divide its content area into up to three regions:

| Region | Position | Width | Behavior |
|--------|----------|-------|----------|
| A — Navigation | LEFT | 8–20 cols | Collapsible |
| B — Content | CENTER | Flex (fills remaining) | Always visible |
| C — Context | RIGHT or BOTTOM | Fixed or collapsible | Optional |

- Region B MUST always be present and MUST fill all space not occupied by Regions A and C.
- Region A MAY be omitted if the archetype has no sidebar navigation.
- Region C MAY be omitted if the archetype has no contextual detail pane.

(CUA §1 panel layout, M3 §3 canonical layouts, tui-architect Cockpit Design Standard)

## §1.4 Footer Key Strip

Every screen MUST display a footer key strip occupying the bottom 1–2 rows of the terminal. The footer MUST:

- Show all keys available in the current context.
- Update when context changes (e.g., different panel focused).
- Remain visible at all times — it MUST NOT be scrolled off-screen or hidden.

Format: `F1 Help  F5 Refresh  / Filter  q Quit` — key name followed by action label, separated by 2+ spaces. (CUA §1 function key area, Norton Commander F-key bar)

## §1.5 Minimum Dimensions

| Tier | Columns × Rows | Status |
|------|---------------|--------|
| Minimum viable | 80 × 24 | MUST support — application MUST remain functional |
| Standard | 120 × 40 | SHOULD target — primary design canvas |

Applications MUST NOT crash or produce garbled output at 80×24. Applications SHOULD present their full layout at 120×40. (Terminal §6 VT100 legacy, OS/2 §2)

## §1.6 Responsive Breakpoints

Applications MUST adapt layout at these column-width breakpoints:

| Breakpoint | Column Range | Layout Rule |
|------------|-------------|-------------|
| Compact | 40–79 | Region A collapses; Region C hidden or stacked below B; footer reduces to single row |
| Standard | 80–119 | Region A visible (narrow, 8–12 cols); Region C optional; full footer |
| Expanded | 120–159 | Full three-region layout; Region A at 12–16 cols |
| Wide | 160+ | Region A at full width (up to 20 cols); Region C expanded; extra whitespace in B |

Applications MUST handle terminal resize (SIGWINCH) and re-render within 100ms. Applications MUST NOT require a restart after resize. (Terminal §6 SIGWINCH, M3 §3 window size classes)
