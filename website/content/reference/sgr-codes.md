---
title: "§R2 SGR Codes"
description: "Select Graphic Rendition codes for text styling, typography roles, and state rendering"
weight: 2
---

## §R2.1 Attribute Codes

All styling uses CSI sequences: `ESC[{params}m` (where ESC = `\x1b` or `\033`).

| Code | Attribute | Reset Code | Use in Monospace TUI |
|------|-----------|-----------|-------------|
| 0 | Reset all | — | Clear all attributes |
| 1 | Bold | 22 | Display and Title typography (Standard [§7.1](/standard/typography/#71-text-treatments)) |
| 2 | Dim (faint) | 22 | Label typography, Disabled state (Standard [§7.1](/standard/typography/#71-text-treatments), [§8.1](/standard/state/#81-required-states)) |
| 3 | Italic | 23 | Sparingly — not in standard typography roles |
| 4 | Underline | 24 | Hovered state, mnemonics (Standard [§8.1](/standard/state/#81-required-states)) |
| 7 | Reverse video | 27 | Focused and Selected states (Standard [§8.1](/standard/state/#81-required-states)) |
| 9 | Strikethrough | 29 | Deprecated items only |

## §R2.2 Typography Role → SGR Mapping

| Typography Role | SGR Sequence | Example |
|----------------|-------------|---------|
| Display | `ESC[1m` (+ uppercase in source) | `ESC[1mDASHBOARDESC[22m` |
| Title | `ESC[1m` | `ESC[1mSection HeaderESC[22m` |
| Body | (no attributes) | `Normal content text` |
| Label | `ESC[2m` | `ESC[2mLast updated: 12:34ESC[22m` |

## §R2.3 State → SGR Mapping

| State | SGR Sequence | Notes |
|-------|-------------|-------|
| Enabled | (no attributes) | Default rendering |
| Focused | `ESC[7m` | Reverse video |
| Hovered | `ESC[4m` | Underline (mouse contexts) |
| Pressed | `ESC[7m` → `ESC[27m` (within ≤100ms) | Brief reverse flash |
| Selected | `ESC[7m` + fill mark character | Reverse video with `[X]` or `(*)` |
| Disabled | `ESC[2m` | Dim/faint |
| Error | `ESC[31m` or `ESC[91m` | Red foreground (standard or bright) |
| Error (severe) | `ESC[41m` | Red background |

## §R2.4 Standard Foreground Colors

| Color | Standard FG | Bright FG | Standard BG | Bright BG |
|-------|------------|-----------|------------|-----------|
| Black | 30 | 90 | 40 | 100 |
| Red | 31 | 91 | 41 | 101 |
| Green | 32 | 92 | 42 | 102 |
| Yellow | 33 | 93 | 43 | 103 |
| Blue | 34 | 94 | 44 | 104 |
| Magenta | 35 | 95 | 45 | 105 |
| Cyan | 36 | 96 | 46 | 106 |
| White | 37 | 97 | 47 | 107 |
| Default | 39 | — | 49 | — |

## §R2.5 Extended Color Sequences

**256-color mode:**

```
Foreground: ESC[38;5;{n}m    (n = 0–255)
Background: ESC[48;5;{n}m    (n = 0–255)
```

**Truecolor (24-bit):**

```
Foreground: ESC[38;2;{r};{g};{b}m    (r, g, b = 0–255)
Background: ESC[48;2;{r};{g};{b}m    (r, g, b = 0–255)
```
