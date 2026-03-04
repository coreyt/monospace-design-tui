---
title: "§R1 Box-Drawing Characters"
description: "Unicode codepoints for single-line, double-line, heavy, rounded, dashed, block, and indicator characters"
weight: 1
---

## §R1.1 Single-Line (Light)

Used for: Level 1 panels, Level 2 menus, inactive windows (Standard [§6.1](/standard/borders/#61-elevation-levels), [§6.2](/standard/borders/#62-activeinactive-window-borders)).

| Glyph | Name | Unicode | Description |
|-------|------|---------|-------------|
| `─` | BOX DRAWINGS LIGHT HORIZONTAL | U+2500 | Horizontal line |
| `│` | BOX DRAWINGS LIGHT VERTICAL | U+2502 | Vertical line |
| `┌` | BOX DRAWINGS LIGHT DOWN AND RIGHT | U+250C | Top-left corner |
| `┐` | BOX DRAWINGS LIGHT DOWN AND LEFT | U+2510 | Top-right corner |
| `└` | BOX DRAWINGS LIGHT UP AND RIGHT | U+2514 | Bottom-left corner |
| `┘` | BOX DRAWINGS LIGHT UP AND LEFT | U+2518 | Bottom-right corner |
| `├` | BOX DRAWINGS LIGHT VERTICAL AND RIGHT | U+251C | Left T-junction |
| `┤` | BOX DRAWINGS LIGHT VERTICAL AND LEFT | U+2524 | Right T-junction |
| `┬` | BOX DRAWINGS LIGHT DOWN AND HORIZONTAL | U+252C | Top T-junction |
| `┴` | BOX DRAWINGS LIGHT UP AND HORIZONTAL | U+2534 | Bottom T-junction |
| `┼` | BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL | U+253C | Cross junction |

## §R1.2 Heavy (Thick)

Used for: optional emphasis borders, header separators.

| Glyph | Name | Unicode |
|-------|------|---------|
| `━` | BOX DRAWINGS HEAVY HORIZONTAL | U+2501 |
| `┃` | BOX DRAWINGS HEAVY VERTICAL | U+2503 |
| `┏` | BOX DRAWINGS HEAVY DOWN AND RIGHT | U+250F |
| `┓` | BOX DRAWINGS HEAVY DOWN AND LEFT | U+2513 |
| `┗` | BOX DRAWINGS HEAVY UP AND RIGHT | U+2517 |
| `┛` | BOX DRAWINGS HEAVY UP AND LEFT | U+251B |
| `┣` | BOX DRAWINGS HEAVY VERTICAL AND RIGHT | U+2523 |
| `┫` | BOX DRAWINGS HEAVY VERTICAL AND LEFT | U+252B |
| `┳` | BOX DRAWINGS HEAVY DOWN AND HORIZONTAL | U+2533 |
| `┻` | BOX DRAWINGS HEAVY UP AND HORIZONTAL | U+253B |
| `╋` | BOX DRAWINGS HEAVY VERTICAL AND HORIZONTAL | U+254B |

## §R1.3 Double-Line

Used for: Level 3 dialogs, Level 4 modals, active windows (Standard [§6.1](/standard/borders/#61-elevation-levels), [§6.2](/standard/borders/#62-activeinactive-window-borders)).

| Glyph | Name | Unicode |
|-------|------|---------|
| `═` | BOX DRAWINGS DOUBLE HORIZONTAL | U+2550 |
| `║` | BOX DRAWINGS DOUBLE VERTICAL | U+2551 |
| `╔` | BOX DRAWINGS DOUBLE DOWN AND RIGHT | U+2554 |
| `╗` | BOX DRAWINGS DOUBLE DOWN AND LEFT | U+2557 |
| `╚` | BOX DRAWINGS DOUBLE UP AND RIGHT | U+255A |
| `╝` | BOX DRAWINGS DOUBLE UP AND LEFT | U+255D |
| `╠` | BOX DRAWINGS DOUBLE VERTICAL AND RIGHT | U+2560 |
| `╣` | BOX DRAWINGS DOUBLE VERTICAL AND LEFT | U+2563 |
| `╦` | BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL | U+2566 |
| `╩` | BOX DRAWINGS DOUBLE UP AND HORIZONTAL | U+2569 |
| `╬` | BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL | U+256C |

## §R1.4 Rounded Corners

Used for: cosmetic non-interactive containers only (Standard [§6.6](/standard/borders/#66-rounded-corners)).

| Glyph | Name | Unicode |
|-------|------|---------|
| `╭` | BOX DRAWINGS LIGHT ARC DOWN AND RIGHT | U+256D |
| `╮` | BOX DRAWINGS LIGHT ARC DOWN AND LEFT | U+256E |
| `╰` | BOX DRAWINGS LIGHT ARC UP AND RIGHT | U+256F |
| `╯` | BOX DRAWINGS LIGHT ARC UP AND LEFT | U+2570 |

## §R1.5 Dashed Lines

Used for: optional separators, visual grouping within panels.

| Glyph | Name | Unicode |
|-------|------|---------|
| `┄` | BOX DRAWINGS LIGHT TRIPLE DASH HORIZONTAL | U+2504 |
| `┆` | BOX DRAWINGS LIGHT TRIPLE DASH VERTICAL | U+2506 |
| `┈` | BOX DRAWINGS LIGHT QUADRUPLE DASH HORIZONTAL | U+2508 |
| `┊` | BOX DRAWINGS LIGHT QUADRUPLE DASH VERTICAL | U+250A |
| `╌` | BOX DRAWINGS HEAVY TRIPLE DASH HORIZONTAL | U+254C |
| `╎` | BOX DRAWINGS HEAVY TRIPLE DASH VERTICAL | U+254E |

## §R1.6 Block and Shade Characters

Used for: progress bars, sparklines, scroll indicators, shadows.

| Glyph | Name | Unicode | Coverage |
|-------|------|---------|----------|
| `░` | LIGHT SHADE | U+2591 | 25% fill |
| `▒` | MEDIUM SHADE | U+2592 | 50% fill |
| `▓` | DARK SHADE | U+2593 | 75% fill |
| `█` | FULL BLOCK | U+2588 | 100% fill |
| `▄` | LOWER HALF BLOCK | U+2584 | Bottom half |
| `▀` | UPPER HALF BLOCK | U+2580 | Top half |
| `▌` | LEFT HALF BLOCK | U+258C | Left half |
| `▐` | RIGHT HALF BLOCK | U+2590 | Right half |
| `▏` | LEFT ONE EIGHTH BLOCK | U+258F | 1/8 left |
| `▎` | LEFT ONE QUARTER BLOCK | U+258E | 1/4 left |
| `▍` | LEFT THREE EIGHTHS BLOCK | U+258D | 3/8 left |
| `▋` | LEFT FIVE EIGHTHS BLOCK | U+258B | 5/8 left |
| `▊` | LEFT THREE QUARTERS BLOCK | U+258A | 3/4 left |
| `▉` | LEFT SEVEN EIGHTHS BLOCK | U+2589 | 7/8 left |

## §R1.7 Status and Indicator Symbols

Used for: status displays, selection marks, navigation indicators.

| Glyph | Name | Unicode | Use |
|-------|------|---------|-----|
| `◉` | FISHEYE | U+25C9 | Active/healthy status |
| `○` | WHITE CIRCLE | U+25CB | Inactive status |
| `●` | BLACK CIRCLE | U+25CF | Filled indicator |
| `▸` | BLACK RIGHT-POINTING SMALL TRIANGLE | U+25B8 | Focus/selection indicator |
| `▴` | BLACK UP-POINTING SMALL TRIANGLE | U+25B4 | Sort ascending |
| `▾` | BLACK DOWN-POINTING SMALL TRIANGLE | U+25BE | Sort descending |
| `⚠` | WARNING SIGN | U+26A0 | Warning status |
| `✓` | CHECK MARK | U+2713 | Success/confirmed |
| `✗` | BALLOT X | U+2717 | Error/failed |
| `⋯` | MIDLINE HORIZONTAL ELLIPSIS | U+22EF | Truncation indicator |
| `↑` | UPWARDS ARROW | U+2191 | Scroll up indicator |
| `↓` | DOWNWARDS ARROW | U+2193 | Scroll down indicator |

## §R1.8 Focus Bracket Markers

Used for: alternative focus indication when reverse video is insufficient (Standard [§7.2](/standard/typography/#72-focus-and-selection-indication), [§8.1](/standard/state/#81-required-states)).

```
[▸ focused item ◂]
```

| Glyph | Name | Unicode | Position |
|-------|------|---------|----------|
| `[` | LEFT SQUARE BRACKET | U+005B | Before indicator |
| `▸` | BLACK RIGHT-POINTING SMALL TRIANGLE | U+25B8 | After opening bracket + space |
| `◂` | BLACK LEFT-POINTING SMALL TRIANGLE | U+25C2 | Before closing bracket + space |
| `]` | RIGHT SQUARE BRACKET | U+005D | After indicator |

Total width overhead: 6 characters (3 prefix `[▸ ` + 3 suffix ` ◂]`).

## §R1.9 Mnemonic Rendering

Mnemonics (Standard [§2.4](/standard/keyboard/#24-mnemonic-rules)) are underlined letters enabling single-keystroke selection in menus. Source notation uses tilde (`~F~ile`) or ampersand (`&File`).

**Visual rendering:** The mnemonic character MUST be rendered with underline (SGR 4). If the terminal does not support underline, use a contrasting foreground color (bright white when surrounding text is dimmer).

```
Example — "File" with F as mnemonic:
  Source:  ~F~ile
  Render:  ESC[4mFESC[24mile
           ─────         ────
           underlined F   normal "ile"
```
