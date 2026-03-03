---
title: "Rendering Reference"
subtitle: "v0.1 — Exact characters, SGR codes, and measurements for implementers"
description: "Unicode codepoints, SGR escape sequences, component measurements, and color palettes"
toc: true
---

## §R1 Box-Drawing Characters

### §R1.1 Single-Line (Light)

Used for: Level 1 panels, Level 2 menus, inactive windows (Standard §6.1, §6.2).

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

### §R1.2 Heavy (Thick)

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

### §R1.3 Double-Line

Used for: Level 3 dialogs, Level 4 modals, active windows (Standard §6.1, §6.2).

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

### §R1.4 Rounded Corners

Used for: cosmetic non-interactive containers only (Standard §6.6).

| Glyph | Name | Unicode |
|-------|------|---------|
| `╭` | BOX DRAWINGS LIGHT ARC DOWN AND RIGHT | U+256D |
| `╮` | BOX DRAWINGS LIGHT ARC DOWN AND LEFT | U+256E |
| `╰` | BOX DRAWINGS LIGHT ARC UP AND RIGHT | U+256F |
| `╯` | BOX DRAWINGS LIGHT ARC UP AND LEFT | U+2570 |

### §R1.5 Dashed Lines

Used for: optional separators, visual grouping within panels.

| Glyph | Name | Unicode |
|-------|------|---------|
| `┄` | BOX DRAWINGS LIGHT TRIPLE DASH HORIZONTAL | U+2504 |
| `┆` | BOX DRAWINGS LIGHT TRIPLE DASH VERTICAL | U+2506 |
| `┈` | BOX DRAWINGS LIGHT QUADRUPLE DASH HORIZONTAL | U+2508 |
| `┊` | BOX DRAWINGS LIGHT QUADRUPLE DASH VERTICAL | U+250A |
| `╌` | BOX DRAWINGS HEAVY TRIPLE DASH HORIZONTAL | U+254C |
| `╎` | BOX DRAWINGS HEAVY TRIPLE DASH VERTICAL | U+254E |

### §R1.6 Block and Shade Characters

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

### §R1.7 Status and Indicator Symbols

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

### §R1.8 Focus Bracket Markers

Used for: alternative focus indication when reverse video is insufficient (Standard §7.2, §8.1).

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

### §R1.9 Mnemonic Rendering

Mnemonics (Standard §2.4) are underlined letters enabling single-keystroke selection in menus. Source notation uses tilde (`~F~ile`) or ampersand (`&File`).

**Visual rendering:** The mnemonic character MUST be rendered with underline (SGR 4). If the terminal does not support underline, use a contrasting foreground color (bright white when surrounding text is dimmer).

```
Example — "File" with F as mnemonic:
  Source:  ~F~ile
  Render:  ESC[4mFESC[24mile
           ─────         ────
           underlined F   normal "ile"
```

---

## §R2 SGR (Select Graphic Rendition) Codes

### §R2.1 Attribute Codes

All styling uses CSI sequences: `ESC[{params}m` (where ESC = `\x1b` or `\033`).

| Code | Attribute | Reset Code | Use in Monospace TUI |
|------|-----------|-----------|-------------|
| 0 | Reset all | — | Clear all attributes |
| 1 | Bold | 22 | Display and Title typography (Standard §7.1) |
| 2 | Dim (faint) | 22 | Label typography, Disabled state (Standard §7.1, §8.1) |
| 3 | Italic | 23 | Sparingly — not in standard typography roles |
| 4 | Underline | 24 | Hovered state, mnemonics (Standard §8.1) |
| 7 | Reverse video | 27 | Focused and Selected states (Standard §8.1) |
| 9 | Strikethrough | 29 | Deprecated items only |

### §R2.2 Typography Role → SGR Mapping

| Typography Role | SGR Sequence | Example |
|----------------|-------------|---------|
| Display | `ESC[1m` (+ uppercase in source) | `ESC[1mDASHBOARDESC[22m` |
| Title | `ESC[1m` | `ESC[1mSection HeaderESC[22m` |
| Body | (no attributes) | `Normal content text` |
| Label | `ESC[2m` | `ESC[2mLast updated: 12:34ESC[22m` |

### §R2.3 State → SGR Mapping

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

### §R2.4 Standard Foreground Colors

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

### §R2.5 Extended Color Sequences

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

---

## §R3 256-Color Palette

### §R3.1 Palette Structure

| Index Range | Content |
|------------|---------|
| 0–7 | Standard ANSI colors (black, red, green, yellow, blue, magenta, cyan, white) |
| 8–15 | Bright ANSI colors |
| 16–231 | 6×6×6 color cube: `index = 16 + 36r + 6g + b` (r, g, b = 0–5) |
| 232–255 | 24-step grayscale ramp (232 = darkest, 255 = lightest) |

### §R3.2 Semantic Role → 256-Color Mapping

#### Dark Theme (default)

| Semantic Role | Foreground (index) | Background (index) | Hex Approximation |
|--------------|-------------------|-------------------|-------------------|
| Primary | 75 (light blue) | 17 (dark blue) | fg #5fafff, bg #00005f |
| Secondary | 109 (muted blue) | 236 (dark gray) | fg #87afaf, bg #303030 |
| Tertiary | 79 (teal) | 236 (dark gray) | fg #5fd7af, bg #303030 |
| Error | 196 (bright red) | 52 (dark red) | fg #ff0000, bg #5f0000 |
| Neutral fg | 252 (light gray) | — | fg #d0d0d0 |
| Neutral bg | — | 235 (near-black) | bg #262626 |
| Surface | 252 | 234 (charcoal) | bg #1c1c1c |

#### Light Theme

| Semantic Role | Foreground (index) | Background (index) | Hex Approximation |
|--------------|-------------------|-------------------|-------------------|
| Primary | 25 (dark blue) | 189 (light blue) | fg #005faf, bg #d7d7ff |
| Secondary | 66 (muted blue) | 254 (near-white) | fg #5f8787, bg #e4e4e4 |
| Tertiary | 30 (dark teal) | 254 (near-white) | fg #008787, bg #e4e4e4 |
| Error | 124 (dark red) | 224 (light pink) | fg #af0000, bg #ffd7d7 |
| Neutral fg | 235 (dark gray) | — | fg #262626 |
| Neutral bg | — | 255 (white) | bg #eeeeee |
| Surface | 235 | 231 (pure white) | bg #ffffff |

### §R3.3 Status Color Mapping

| Status | Dark Theme (FG index) | Light Theme (FG index) | Paired Symbol |
|--------|----------------------|----------------------|---------------|
| Healthy / Success | 40 (green) | 28 (dark green) | `◉` or `✓` |
| Error / Critical | 196 (bright red) | 124 (dark red) | `✗` or `●` |
| Warning / Caution | 220 (yellow) | 172 (orange) | `⚠` or `▲` |
| Inactive / Disabled | 240 (gray) | 247 (gray) | `○` or `—` |

### §R3.4 Named Palettes

The Dark Theme and Light Theme mappings above (§R3.2) define the default palettes. Applications MAY offer additional named palettes. Seven named palettes are defined here, drawn from the historical research that informs the standard. All palettes map to the same five semantic roles (§5.1); they differ only in color assignment.

#### Default

Source: Textual framework default dark theme. This is the standard modern dark palette — the recommended starting point for new applications. It uses the same 256-color mappings defined in §R3.2 Dark Theme.

| Semantic Role | Foreground (index) | Background (index) | Hex Approximation |
|--------------|-------------------|-------------------|-------------------|
| Primary | 75 (light blue) | 17 (dark blue) | fg #5fafff, bg #00005f |
| Secondary | 109 (muted blue) | 236 (dark gray) | fg #87afaf, bg #303030 |
| Tertiary | 79 (teal) | 236 (dark gray) | fg #5fd7af, bg #303030 |
| Error | 196 (bright red) | 52 (dark red) | fg #ff0000, bg #5f0000 |
| Neutral fg | 252 (light gray) | — | fg #d0d0d0 |
| Neutral bg | — | 235 (near-black) | bg #262626 |
| Surface | 252 | 234 (charcoal) | bg #1c1c1c |

Status colors:

| Status | Foreground (index) | Paired Symbol |
|--------|-------------------|---------------|
| Healthy / Success | 40 (green) | `◉` or `✓` |
| Error / Critical | 196 (bright red) | `✗` or `●` |
| Warning / Caution | 220 (yellow) | `⚠` or `▲` |
| Inactive / Disabled | 240 (gray) | `○` or `—` |

Example — Dashboard rendered in Default:

<pre class="palette-example palette-default"><span style="color:#585858">┌──</span> <span style="font-weight:bold;color:#5fafff">Service Monitor</span> <span style="color:#585858">────────────────────────────────────────────────────────────┐
│</span> <span style="color:#87afaf">File  View  Help</span>                                                              <span style="color:#585858">│
├───────────────────────────────────────────────────────────────────────────────┤</span>
<span style="color:#585858">│</span>                                                                               <span style="color:#585858">│</span>
<span style="color:#585858">│</span>  CPU: 34%          Services: 12/12          Alerts: 3          Mem: 61%       <span style="color:#585858">│</span>
<span style="color:#585858">│</span>                                                                               <span style="color:#585858">│
├───────────────────────────────────────────────────────────────────────────────┤</span>
<span style="color:#585858">│</span> Service              │ Status   │ Uptime       │ CPU     │ Memory             <span style="color:#585858">│</span>
<span style="color:#585858">│</span>──────────────────────│──────────│──────────────│─────────│────────────────────<span style="color:#585858">│</span>
<span style="color:#585858">│</span> <span style="background:#00005f;color:#5fafff">> api-gateway        │ </span><span style="background:#00005f;color:#00d700"> OK</span><span style="background:#00005f;color:#5fafff">      │ 14d  3h 22m  │   2.1%  │  340MB            </span> <span style="color:#585858">│</span>
<span style="color:#585858">│</span>   auth-service       │ <span style="color:#00d700"> OK</span>      │ 14d  3h 22m  │   0.8%  │  128MB             <span style="color:#585858">│</span>
<span style="color:#585858">│</span>   worker-pool        │ <span style="color:#ffd700"> WARN</span>    │  0d  1h 45m  │  78.3%  │  1.2GB             <span style="color:#585858">│</span>
<span style="color:#585858">│</span>   notification-svc   │ <span style="color:#ff0000"> DOWN</span>    │  0d  0h 00m  │   0.0%  │    0MB             <span style="color:#585858">│</span>
<span style="color:#585858">│</span>   metrics-collector  │ <span style="color:#00d700"> OK</span>      │ 14d  3h 22m  │   1.4%  │  256MB             <span style="color:#585858">│</span>
<span style="color:#585858">│</span>                                                                               <span style="color:#585858">│
├───────────────────────────────────────────────────────────────────────────────┤</span>
<span style="color:#585858">│</span><span style="color:#87afaf"> ? Help  r Refresh  / Filter  q Quit                             5 services    </span><span style="color:#585858">│</span>
<span style="color:#585858">└───────────────────────────────────────────────────────────────────────────────┘</span></pre>

#### Monochrome

Source: CUA `cpAppMonochrome` system palette, Turbo Vision `cpAppBlackWhite` palette, and the capability-detection degradation path (§5.6).

No color indices are used. All semantic differentiation is achieved through SGR text attributes on a black background.

| Semantic Role | Foreground | Background | SGR Attributes |
|--------------|-----------|-----------|----------------|
| Primary | White | Black | **Bold** (SGR 1) |
| Secondary | White | Black | Normal |
| Tertiary | White | Black | Underline (SGR 4) |
| Error | White | Black | **Bold** + Reverse (SGR 1;7) |
| Neutral fg | White | Black | Dim (SGR 2) |
| Neutral bg | — | Black | — |
| Surface | White | Black | — |
| Focus indicator | Black | White | Reverse (SGR 7) |
| Selected item | Black | White | Reverse (SGR 7) |
| Disabled | White | Black | Dim (SGR 2) |

Status mapping under Monochrome:

| Status | Rendering | Paired Symbol |
|--------|----------|---------------|
| Healthy / Success | Normal | `◉` or `✓` |
| Error / Critical | Bold + Reverse | `✗` or `●` |
| Warning / Caution | Bold | `⚠` or `▲` |
| Inactive / Disabled | Dim | `○` or `—` |

Example — Dashboard rendered in Monochrome:

<pre class="palette-example palette-mono"><span style="font-weight:bold;color:#fff">┌── Service Monitor ────────────────────────────────────────────────────────────┐
│</span> <span style="font-weight:bold;color:#fff">File  View  Help</span>                                                              <span style="font-weight:bold;color:#fff">│
├───────────────────────────────────────────────────────────────────────────────┤</span>
│                                                                               │
│  CPU: 34%          Services: 12/12          Alerts: 3          Mem: 61%       │
│                                                                               │
├───────────────────────────────────────────────────────────────────────────────┤
│ Service              │ Status   │ Uptime       │ CPU     │ Memory             │
│──────────────────────│──────────│──────────────│─────────│────────────────────│
│ <span style="background:#ccc;color:#000">> api-gateway        │  OK      │ 14d  3h 22m  │   2.1%  │  340MB            </span> │
│   auth-service       │  OK      │ 14d  3h 22m  │   0.8%  │  128MB             │
│   worker-pool        │ <span style="font-weight:bold;color:#fff"> WARN</span>    │  0d  1h 45m  │  78.3%  │  1.2GB             │
│   notification-svc   │ <span style="font-weight:bold;background:#fff;color:#000">DOWN</span>     │  0d  0h 00m  │   0.0%  │    0MB             │
│   metrics-collector  │  OK      │ 14d  3h 22m  │   1.4%  │  256MB             │
│                                                                               │
├───────────────────────────────────────────────────────────────────────────────┤
│ <span style="color:#666">? Help  r Refresh  / Filter  q Quit                           5 services     </span> │
└───────────────────────────────────────────────────────────────────────────────┘</pre>

#### Commander

Source: OS/2 Presentation Manager text-mode conventions (attribute byte 0x1F = white on blue), Norton Commander's blue-panel aesthetic (0x1_ attribute range), and Turbo Vision's window frame palette entry (0x17 = white on blue). This is the canonical look of IBM PC and OS/2 text-mode applications from 1987–1995.

| Semantic Role | Foreground (index) | Background (index) | Hex Approximation |
|--------------|-------------------|-------------------|-------------------|
| Primary | 15 (bright white) | 19 (dark blue) | fg #ffffff, bg #0000af |
| Secondary | 14 (bright cyan) | 237 (gray) | fg #00ffff, bg #3a3a3a |
| Tertiary | 11 (bright yellow) | 19 (dark blue) | fg #ffff00, bg #0000af |
| Error | 196 (bright red) | 52 (dark red) | fg #ff0000, bg #5f0000 |
| Neutral fg | 15 (bright white) | — | fg #ffffff |
| Neutral bg | — | 19 (dark blue) | bg #0000af |
| Surface | 15 | 17 (navy) | bg #00005f |

Key conventions from the source systems:

- **Panels and windows**: White or cyan text on blue background — the definitive CUA/OS/2 look.
- **Active selection**: Yellow (bright) on blue, or reverse video — Norton Commander convention for selected files.
- **Dialogs**: Black on light gray (Turbo Vision 0x70) — dialogs use a visually distinct, lighter surface to establish elevation.
- **Action bar / menus**: Black on cyan (CUA convention) or white on dark gray.
- **Input fields**: White on blue (Turbo Vision 0x1F) — matching the standard window background.

Dialog surface override for Commander palette:

| Element | Foreground (index) | Background (index) | Hex Approximation |
|---------|-------------------|-------------------|-------------------|
| Dialog surface | 232 (black) | 250 (light gray) | fg #080808, bg #bcbcbc |
| Dialog border | 232 (black) | 250 (light gray) | fg #080808, bg #bcbcbc |
| Dialog button | 232 (black) | 78 (green) | fg #080808, bg #5fd787 |

Example — Dashboard rendered in Commander:

<pre class="palette-example palette-commander">┌── Service Monitor ────────────────────────────────────────────────────────────┐
│ <span style="background:#00cdcd;color:#000"> File  View  Help </span>                                                            │
├───────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  CPU: 34%          Services: 12/12          Alerts: 3          Mem: 61%       │
│                                                                               │
├───────────────────────────────────────────────────────────────────────────────┤
│ Service              │ Status   │ Uptime       │ CPU     │ Memory             │
│──────────────────────│──────────│──────────────│─────────│────────────────────│
│ <span style="color:#ffff00">> api-gateway        │ </span><span style="color:#00ffff"> OK</span><span style="color:#ffff00">      │ 14d  3h 22m  │   2.1%  │  340MB            </span> │
│   auth-service       │ <span style="color:#00ffff"> OK</span>      │ 14d  3h 22m  │   0.8%  │  128MB             │
│   worker-pool        │ <span style="color:#ffff00"> WARN</span>    │  0d  1h 45m  │  78.3%  │  1.2GB             │
│   notification-svc   │ <span style="color:#ff0000"> DOWN</span>    │  0d  0h 00m  │   0.0%  │    0MB             │
│   metrics-collector  │ <span style="color:#00ffff"> OK</span>      │ 14d  3h 22m  │   1.4%  │  256MB             │
│                                                                               │
├───────────────────────────────────────────────────────────────────────────────┤
│ <span style="color:#00ffff">? Help  r Refresh  / Filter  q Quit                           5 services     </span> │
└───────────────────────────────────────────────────────────────────────────────┘</pre>

#### OS/2

Source: OS/2 Presentation Manager text-mode conventions as seen in OS/2 terminal emulators like Softerm. Yellow-green text on CGA blue, with light gray action bars and status lines. The window title bar uses yellow on dark blue. Selections use reverse video. Active windows use double-line borders with brighter attributes; inactive windows use single-line borders with dimmer attributes (§5.5).

| Semantic Role | Foreground (index) | Background (index) | Hex Approximation |
|--------------|-------------------|-------------------|-------------------|
| Primary | 14 (yellow) | 1 (blue) | fg #FFFF55, bg #0000AA |
| Secondary | 7 (light gray) | 1 (blue) | fg #AAAAAA, bg #0000AA |
| Tertiary | 0 (black) | 7 (light gray) | fg #000000, bg #AAAAAA |
| Error | 12 (light red) | 1 (blue) | fg #FF5555, bg #0000AA |
| Neutral fg | 0 (black) | — | fg #000000 |
| Neutral bg | — | 7 (light gray) | bg #AAAAAA |
| Surface | 14 (yellow) | 1 (blue) | bg #0000AA |

Key conventions:

- **Action bar**: Black on light gray — the CUA standard. Distinguished from the blue panel area.
- **Title bar**: Yellow on dark blue. Window name displayed in the title frame.
- **Panels**: Yellow or light gray text on blue. Terminal text area uses yellow on blue.
- **Status line**: Black on light gray, with status indicators (Online, Half Duplex, etc.).
- **Active/inactive windows**: Bright borders (active) vs. dim borders (inactive), with double-line vs. single-line distinction (§6.1).

Example — Dashboard rendered in OS/2:

<pre class="palette-example palette-os2"><span style="color:#FFFF55">┌──</span> <span style="font-weight:bold;color:#FFFF55">Service Monitor</span> <span style="color:#FFFF55">────────────────────────────────────────────────────────────┐</span>
<span style="color:#FFFF55">│</span> <span style="background:#AAAAAA;color:#000"> File  View  Help </span>                                                            <span style="color:#FFFF55">│</span>
<span style="color:#FFFF55">├───────────────────────────────────────────────────────────────────────────────┤</span>
│                                                                               │
│  CPU: 34%          Services: 12/12          Alerts: 3          Mem: 61%       │
│                                                                               │
<span style="color:#FFFF55">├───────────────────────────────────────────────────────────────────────────────┤</span>
│ Service              │ Status   │ Uptime       │ CPU     │ Memory             │
│──────────────────────│──────────│──────────────│─────────│────────────────────│
<span style="color:#FFFF55">│</span> <span style="background:#AAAAAA;color:#0000AA">> api-gateway        │  OK      │ 14d  3h 22m  │   2.1%  │  340MB            </span> <span style="color:#FFFF55">│</span>
│   auth-service       │ <span style="color:#55FF55"> OK</span>      │ 14d  3h 22m  │   0.8%  │  128MB             │
│   worker-pool        │ <span style="color:#fff"> WARN</span>    │  0d  1h 45m  │  78.3%  │  1.2GB             │
│   notification-svc   │ <span style="color:#FF5555"> DOWN</span>    │  0d  0h 00m  │   0.0%  │    0MB             │
│   metrics-collector  │ <span style="color:#55FF55"> OK</span>      │ 14d  3h 22m  │   1.4%  │  256MB             │
│                                                                               │
<span style="color:#FFFF55">├───────────────────────────────────────────────────────────────────────────────┤</span>
│<span style="background:#AAAAAA;color:#000"> ? Help  r Refresh  / Filter  q Quit                           5 services     </span> │
<span style="color:#FFFF55">└───────────────────────────────────────────────────────────────────────────────┘</span></pre>

#### Turbo Pascal

Source: Borland Turbo Vision palette system (1990) as seen in the Turbo Pascal 7.0 and Turbo C++ IDEs. The desktop uses a `░` dither pattern in light gray on blue. Editor windows show white text on blue. Menu bar and status line use black on light gray. Window frames are white on blue; active windows use double-line borders, inactive use single-line. Dialog boxes use black on light gray, visually distinct from the blue editor surface. Buttons use black on green.

| Semantic Role | Foreground (index) | Background (index) | Hex Approximation |
|--------------|-------------------|-------------------|-------------------|
| Primary | 15 (white) | 1 (blue) | fg #FFFFFF, bg #0000AA |
| Secondary | 7 (light gray) | 1 (blue) | fg #AAAAAA, bg #0000AA |
| Tertiary | 0 (black) | 2 (green) | fg #000000, bg #00AA00 |
| Error | 12 (light red) | 1 (blue) | fg #FF5555, bg #0000AA |
| Neutral fg | 0 (black) | — | fg #000000 |
| Neutral bg | — | 7 (light gray) | bg #AAAAAA |
| Surface | 15 (white) | 1 (blue) | bg #0000AA |

Key conventions from the Borland IDE:

- **Desktop**: `░` dither pattern — light gray (7) on blue (1). Visible behind all windows.
- **Editor area**: White (15) on blue (1). Comments and secondary text in light gray (7).
- **Window frames**: White (15) on blue (1). Double-line for active, single-line for inactive.
- **Menu bar and status line**: Black (0) on light gray (7). Hotkey letters highlighted in red or yellow.
- **Dialog boxes**: Black on light gray. A visually distinct surface from the blue editor area.
- **Buttons**: Black on green (`[ OK ]`). Default button uses highlighted delimiters.

Example — Dashboard rendered in Turbo Pascal:

<pre class="palette-example palette-turbo"><span style="color:#fff">┌──</span> <span style="font-weight:bold;color:#fff">Service Monitor</span> <span style="color:#fff">────────────────────────────────────────────────────────────┐</span>
<span style="color:#fff">│</span> <span style="background:#AAAAAA;color:#000"> File  View  Help </span>                                                            <span style="color:#fff">│</span>
<span style="color:#fff">├───────────────────────────────────────────────────────────────────────────────┤</span>
│                                                                               │
│  CPU: 34%          Services: 12/12          Alerts: 3          Mem: 61%       │
│                                                                               │
<span style="color:#fff">├───────────────────────────────────────────────────────────────────────────────┤</span>
│ Service              │ Status   │ Uptime       │ CPU     │ Memory             │
│──────────────────────│──────────│──────────────│─────────│────────────────────│
<span style="color:#fff">│</span> <span style="background:#00AAAA;color:#fff">> api-gateway        │  OK      │ 14d  3h 22m  │   2.1%  │  340MB            </span> <span style="color:#fff">│</span>
│   auth-service       │ <span style="color:#55FF55"> OK</span>      │ 14d  3h 22m  │   0.8%  │  128MB             │
│   worker-pool        │ <span style="color:#FFFF55"> WARN</span>    │  0d  1h 45m  │  78.3%  │  1.2GB             │
│   notification-svc   │ <span style="color:#FF5555"> DOWN</span>    │  0d  0h 00m  │   0.0%  │    0MB             │
│   metrics-collector  │ <span style="color:#55FF55"> OK</span>      │ 14d  3h 22m  │   1.4%  │  256MB             │
│                                                                               │
<span style="color:#fff">├───────────────────────────────────────────────────────────────────────────────┤</span>
│<span style="background:#AAAAAA;color:#000"> ? Help  r Refresh  / Filter  q Quit                           5 services     </span> │
<span style="color:#fff">└───────────────────────────────────────────────────────────────────────────────┘</span></pre>

#### Amber Phosphor

Source: DEC VT220 and VT320 amber phosphor (P3) displays, widely deployed in business and institutional computing through the 1980s. Control Data Corporation PLATO terminals also used amber-orange plasma displays. The single-hue-on-black aesthetic predates color terminals entirely.

All UI elements are rendered in shades of amber (`#FFB000` at full brightness) on a black background. Semantic roles are distinguished by brightness level within the single hue.

| Semantic Role | Foreground (index) | Background (index) | Hex Approximation |
|--------------|-------------------|-------------------|-------------------|
| Primary | 214 (bright amber) | 0 (black) | fg #ffaf00, bg #000000 |
| Secondary | 172 (medium amber) | 0 (black) | fg #d78700, bg #000000 |
| Tertiary | 214 (bright amber) | 0 (black) | fg #ffaf00, bg #000000 (underline) |
| Error | 214 (bright amber) | 0 (black) | fg #ffaf00, bg #000000 (reverse) |
| Neutral fg | 136 (dim amber) | — | fg #af8700 |
| Neutral bg | — | 0 (black) | bg #000000 |
| Surface | 136 | 0 (black) | bg #000000 |

Because amber is a single-hue palette, SGR attributes provide essential differentiation:

| Element | Color | Additional SGR |
|---------|-------|---------------|
| Focused / active | Bright amber (214) | Bold (SGR 1) |
| Body text | Medium amber (172) | Normal |
| Secondary / labels | Dim amber (136) | Dim (SGR 2) |
| Selected item | Black on amber | Reverse (SGR 7) |
| Error state | Black on amber | Reverse + Bold |
| Disabled | Dim amber (136) | Dim (SGR 2) |
| Links / interactive | Bright amber (214) | Underline (SGR 4) |

Example — Dashboard rendered in Amber Phosphor:

<pre class="palette-example palette-amber"><span style="color:#af8700">┌──</span> <span style="font-weight:bold;color:#ffaf00">Service Monitor</span> <span style="color:#af8700">────────────────────────────────────────────────────────────┐
│</span> <span style="font-weight:bold;color:#ffaf00">File  View  Help</span>                                                              <span style="color:#af8700">│
├───────────────────────────────────────────────────────────────────────────────┤</span>
<span style="color:#af8700">│</span>                                                                               <span style="color:#af8700">│</span>
<span style="color:#af8700">│</span>  CPU: 34%          Services: 12/12          Alerts: 3          Mem: 61%       <span style="color:#af8700">│</span>
<span style="color:#af8700">│</span>                                                                               <span style="color:#af8700">│
├───────────────────────────────────────────────────────────────────────────────┤</span>
<span style="color:#af8700">│</span> Service              │ Status   │ Uptime       │ CPU     │ Memory             <span style="color:#af8700">│</span>
<span style="color:#af8700">│</span>──────────────────────│──────────│──────────────│─────────│────────────────────<span style="color:#af8700">│</span>
<span style="color:#af8700">│</span> <span style="background:#ffaf00;color:#000">> api-gateway        │  OK      │ 14d  3h 22m  │   2.1%  │  340MB            </span> <span style="color:#af8700">│</span>
<span style="color:#af8700">│</span>   auth-service       │  OK      │ 14d  3h 22m  │   0.8%  │  128MB             <span style="color:#af8700">│</span>
<span style="color:#af8700">│</span>   worker-pool        │ <span style="font-weight:bold;color:#ffaf00"> WARN</span>    │  0d  1h 45m  │  78.3%  │  1.2GB             <span style="color:#af8700">│</span>
<span style="color:#af8700">│</span>   notification-svc   │ <span style="font-weight:bold;background:#ffaf00;color:#000"> DOWN</span>    │  0d  0h 00m  │   0.0%  │    0MB             <span style="color:#af8700">│</span>
<span style="color:#af8700">│</span>   metrics-collector  │  OK      │ 14d  3h 22m  │   1.4%  │  256MB             <span style="color:#af8700">│</span>
<span style="color:#af8700">│</span>                                                                               <span style="color:#af8700">│
├───────────────────────────────────────────────────────────────────────────────┤</span>
<span style="color:#af8700">│ ? Help  r Refresh  / Filter  q Quit                           5 services      │
└───────────────────────────────────────────────────────────────────────────────┘</span></pre>

#### Green Phosphor

Source: DEC VT100 and VT101 green phosphor (P1) displays — the original "green screen" terminal that defined the early Unix and VAX/VMS experience. Also used in IBM 3278 display terminals and countless institutional systems through the 1970s–1980s.

Structurally identical to Amber Phosphor but in green. All UI elements rendered in shades of green (`#33FF00` at full brightness) on black.

| Semantic Role | Foreground (index) | Background (index) | Hex Approximation |
|--------------|-------------------|-------------------|-------------------|
| Primary | 82 (bright green) | 0 (black) | fg #5fff00, bg #000000 |
| Secondary | 34 (medium green) | 0 (black) | fg #00af00, bg #000000 |
| Tertiary | 82 (bright green) | 0 (black) | fg #5fff00, bg #000000 (underline) |
| Error | 82 (bright green) | 0 (black) | fg #5fff00, bg #000000 (reverse) |
| Neutral fg | 28 (dim green) | — | fg #008700 |
| Neutral bg | — | 0 (black) | bg #000000 |
| Surface | 28 | 0 (black) | bg #000000 |

SGR attribute usage follows the same pattern as Amber Phosphor:

| Element | Color | Additional SGR |
|---------|-------|---------------|
| Focused / active | Bright green (82) | Bold (SGR 1) |
| Body text | Medium green (34) | Normal |
| Secondary / labels | Dim green (28) | Dim (SGR 2) |
| Selected item | Black on green | Reverse (SGR 7) |
| Error state | Black on green | Reverse + Bold |
| Disabled | Dim green (28) | Dim (SGR 2) |
| Links / interactive | Bright green (82) | Underline (SGR 4) |

Example — Dashboard rendered in Green Phosphor:

<pre class="palette-example palette-green"><span style="color:#008700">┌──</span> <span style="font-weight:bold;color:#5fff00">Service Monitor</span> <span style="color:#008700">────────────────────────────────────────────────────────────┐
│</span> <span style="font-weight:bold;color:#5fff00">File  View  Help</span>                                                              <span style="color:#008700">│
├───────────────────────────────────────────────────────────────────────────────┤</span>
<span style="color:#008700">│</span>                                                                               <span style="color:#008700">│</span>
<span style="color:#008700">│</span>  CPU: 34%          Services: 12/12          Alerts: 3          Mem: 61%       <span style="color:#008700">│</span>
<span style="color:#008700">│</span>                                                                               <span style="color:#008700">│
├───────────────────────────────────────────────────────────────────────────────┤</span>
<span style="color:#008700">│</span> Service              │ Status   │ Uptime       │ CPU     │ Memory             <span style="color:#008700">│</span>
<span style="color:#008700">│</span>──────────────────────│──────────│──────────────│─────────│────────────────────<span style="color:#008700">│</span>
<span style="color:#008700">│</span> <span style="background:#5fff00;color:#000">> api-gateway        │  OK      │ 14d  3h 22m  │   2.1%  │  340MB            </span> <span style="color:#008700">│</span>
<span style="color:#008700">│</span>   auth-service       │  OK      │ 14d  3h 22m  │   0.8%  │  128MB             <span style="color:#008700">│</span>
<span style="color:#008700">│</span>   worker-pool        │ <span style="font-weight:bold;color:#5fff00"> WARN</span>    │  0d  1h 45m  │  78.3%  │  1.2GB             <span style="color:#008700">│</span>
<span style="color:#008700">│</span>   notification-svc   │ <span style="font-weight:bold;background:#5fff00;color:#000"> DOWN</span>    │  0d  0h 00m  │   0.0%  │    0MB             <span style="color:#008700">│</span>
<span style="color:#008700">│</span>   metrics-collector  │  OK      │ 14d  3h 22m  │   1.4%  │  256MB             <span style="color:#008700">│</span>
<span style="color:#008700">│</span>                                                                               <span style="color:#008700">│
├───────────────────────────────────────────────────────────────────────────────┤</span>
<span style="color:#008700">│ ? Help  r Refresh  / Filter  q Quit                           5 services      │
└───────────────────────────────────────────────────────────────────────────────┘</span></pre>

---

## §R4 Component Measurements

All measurements are in character cells (cols × rows).

### §R4.1 Push Button

```
< Label >     (standard)
» Label «     (default button)
```

| Property | Value |
|----------|-------|
| Height | 1 row |
| Min width | Label length + 4 (2 padding chars each side) |
| Padding | 1 space each side inside delimiters |
| Delimiter (standard) | `<` and `>` |
| Delimiter (default) | `»` and `«` |
| Gap between buttons | 2 cols |

### §R4.2 Entry Field

```
Label: [input text here____]
```

| Property | Value |
|----------|-------|
| Height | 1 row |
| Min width | 10 cols (including brackets) |
| Max width | 60 cols |
| Fill character | `_` (underscore) or `·` (middle dot) |
| Bracket delimiters | `[` and `]` |
| Label gap | 1 space between label and field |

### §R4.3 Toggle / Checkbox

```
[X] Enabled option
[ ] Disabled option
```

| Property | Value |
|----------|-------|
| Height | 1 row per option |
| Indicator width | 3 cols (`[X]` or `[ ]`) |
| Gap to label | 1 space |
| Vertical gap between options | 0 rows (consecutive lines) |

### §R4.4 Radio Group

```
(*) Selected option
( ) Unselected option A
( ) Unselected option B
```

| Property | Value |
|----------|-------|
| Height | 1 row per option |
| Indicator width | 3 cols (`(*)` or `( )`) |
| Gap to label | 1 space |
| Vertical gap between options | 0 rows |
| Group label | 1 row above group, Title typography |

### §R4.5 List Box

```
┌── Select Model ──────────┐
│ ▸ claude-3-opus           │
│   claude-3-sonnet         │
│   gpt-4-turbo             │
│   gpt-4o                  │
│   gemini-1.5-pro      ↓   │
└──────────────────────────┘
```

| Property | Value |
|----------|-------|
| Min height | 3 rows (content) + 2 (border) = 5 rows |
| Max height | 15 rows (content) + 2 (border) = 17 rows |
| Min width | 20 cols (including border) |
| Highlight bar | Reverse video on focused row |
| Selection indicator | `▸` (1 col) before focused item |
| Scroll indicator | `↑` / `↓` in right border when content overflows |
| Border | Level 1 (single-line) |

### §R4.6 Data Table

```
│ Name         │ Status │ Latency │ Errors │
│──────────────│────────│─────────│────────│
│ claude-3     │ ◉ OK   │  120ms  │ 0      │
│ gpt-4        │ ⚠ SLOW │  890ms  │ 2      │
```

| Property | Value |
|----------|-------|
| Header row | 1 row, Title typography (bold) |
| Separator | 1 row of `─` characters below header |
| Data row height | 1 row |
| Cell horizontal padding | 1 space each side |
| Column separator | `│` (single vertical line) |
| Min column width | Longest header or data value + 2 (padding) |
| Sort indicator | `▴` (ascending) or `▾` (descending) after header text |

### §R4.7 Metric Card

```
▲ Requests: 1,234
```

| Property | Value |
|----------|-------|
| Height | 1 row (compact) or 2–3 rows (expanded) |
| Icon/symbol | 1–2 cols |
| Gap icon → label | 1 space |
| Gap label → value | 1 space (or `: `) |
| Separator between cards | `│` with 1 space padding each side |

### §R4.8 Dialog

```
╔══ Confirm Delete ══════════════════╗
║                                    ║
║  Are you sure you want to delete   ║
║  "report.pdf"?                     ║
║                                    ║
║         < Delete >  < Cancel >     ║
║                                    ║
╚════════════════════════════════════╝
```

| Property | Value |
|----------|-------|
| Min width | 30 cols |
| Max width | 72 cols |
| Min height | 5 rows (content) + 2 (border) = 7 rows |
| Padding | 2 cols horizontal, 1 row vertical (inside border) |
| Border | Level 3 (double-line) |
| Shadow | 2-col × 1-row offset |
| Title | Centered in top border |
| Button area | Bottom of content, right-aligned or centered |
| Button gap | 2 cols between buttons |

### §R4.9 Menu (Pull-Down)

```
┌──────────────────┐
│ New           ^N  │
│ Open...       ^O  │
│ Save          ^S  │
│───────────────────│
│ Close         ^W  │
└──────────────────┘
```

| Property | Value |
|----------|-------|
| Item height | 1 row |
| Max items | 10 |
| Min width | Longest item text + shortcut + 4 (padding) |
| Max width | 40 cols |
| Horizontal padding | 1 space each side |
| Separator | Full-width `─` line |
| Shortcut alignment | Right-aligned, 2 spaces before right border |
| Border | Level 2 (single-line) |
| Shadow | 2-col × 1-row offset |
| Cascade indicator | `▸` suffix (right-aligned) |
| Disabled items | Dim (SGR 2), no shortcut highlight |

### §R4.10 Spin Button

```
Model Count: < 5 >
```

| Property | Value |
|----------|-------|
| Height | 1 row |
| Decrease indicator | `<` |
| Increase indicator | `>` |
| Value padding | 1 space each side of value |
| Max recommended values | 20 |

### §R4.11 Footer Key Strip

```
F1 Help  F5 Refresh  / Filter  q Quit
```

| Property | Value |
|----------|-------|
| Height | 1–2 rows |
| Key label | Key name in bold or contrasting color |
| Action label | Body typography |
| Gap key → action | 1 space |
| Gap between pairs | 2+ spaces |
| Position | Absolute bottom of terminal |

---

## §R5 Shadow Rendering

### §R5.1 Algorithm

Shadows create depth illusion for Level 2–4 elements (Standard §6.4).

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

### §R5.2 Shadow Cell Attribute

In 16-color mode, shadow cells use attribute byte `0x08` (dark gray foreground on black background), preserving the original character code. In 256-color or truecolor mode, shadow cells apply SGR 2 (dim) to whatever attributes the underlying cell had.

### §R5.3 Scrim Rendering

Scrims create a dimmed backdrop behind Level 4 modal overlays (Standard §6.5).

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

---

## §R6 Braille Sparkline Encoding

### §R6.1 Braille Pattern Block

Unicode Braille Patterns occupy U+2800–U+28FF (256 characters). Each character represents a 2×4 dot matrix within one character cell, providing **2× horizontal and 4× vertical sub-cell resolution**.

### §R6.2 Dot Position → Bit Mapping

Each Braille character's codepoint is `U+2800 + bitmask`, where bits map to dot positions:

```
Position:    Bit:
┌───┬───┐
│ 1 │ 4 │   bit 0 = dot 1 (top-left)
│ 2 │ 5 │   bit 1 = dot 2 (mid-left)
│ 3 │ 6 │   bit 2 = dot 3 (lower-left)
│ 7 │ 8 │   bit 3 = dot 7 (bottom-left)
└───┴───┘   bit 4 = dot 4 (top-right)
            bit 5 = dot 5 (mid-right)
            bit 6 = dot 6 (lower-right)
            bit 7 = dot 8 (bottom-right)
```

### §R6.3 Sparkline Construction Algorithm

To render a sparkline from a sequence of values:

1. **Normalize** values to a 0–3 range (for single-column sparklines) or 0–7 range (for two-column sparklines using both dot columns).
2. **For each character cell** in the sparkline, determine which vertical dots to fill based on the normalized value. A value of 0 = no dots; a value of 3 = dots at positions 7, 3, 2 (bottom three on left column).
3. **Compute the bitmask** by OR-ing the bits for each active dot position.
4. **Emit** `U+2800 + bitmask`.

**Example — single-column bar chart (left column only):**

| Value (0–4) | Active dots | Bitmask | Character |
|-------------|------------|---------|-----------|
| 0 | none | 0x00 | `⠀` (blank) |
| 1 | 7 | 0x40 | `⡀` |
| 2 | 3, 7 | 0x44 | `⡄` |
| 3 | 2, 3, 7 | 0x46 | `⡆` |
| 4 | 1, 2, 3, 7 | 0x47 | `⡇` |

### §R6.4 Progress Bar Using Eighth Blocks

For linear progress bars, use eighth-block characters for smooth fill:

| Progress | Character Sequence |
|----------|-------------------|
| 0/8 | ` ` (space) |
| 1/8 | `▏` (U+258F) |
| 2/8 | `▎` (U+258E) |
| 3/8 | `▍` (U+258D) |
| 4/8 | `▌` (U+258C) |
| 5/8 | `▋` (U+258B) |
| 6/8 | `▊` (U+258A) |
| 7/8 | `▉` (U+2589) |
| 8/8 | `█` (U+2588) |

A progress bar of width W cols at P% completion:

```
filled_cells = floor(W * P / 100)
partial = ((W * P / 100) - filled_cells) * 8   → index into eighth-block table
output = "█" × filled_cells + eighth_block[partial] + " " × remaining
```

---

## §R7 Color Capability Detection

### §R7.1 Detection Algorithm

Applications MUST detect color capability at startup using this priority order:

```
1. If COLORTERM == "truecolor" or COLORTERM == "24bit":
     → Truecolor (24-bit, 16.7M colors)
2. Else if TERM contains "256color":
     → 256-color mode
3. Else if TERM == "dumb":
     → Monochrome (attributes only: bold, dim, underline, reverse)
4. Else:
     → 16-color ANSI (standard + bright)
```

### §R7.2 Graceful Degradation

| Feature | Truecolor | 256-color | 16-color | Monochrome |
|---------|----------|-----------|----------|------------|
| Semantic roles (§R3.2) | Exact hex | Nearest 256 index | Nearest ANSI | N/A |
| Status colors (§R3.3) | Exact hex | Nearest 256 index | Standard red/green/yellow | Bold/dim/reverse |
| Elevation shadows | Dim + color | Dim + index 240 | Dim (SGR 2) | Reverse video strip |
| Scrim (Level 4) | Semi-transparent dim | Dim all bg cells | Dim all bg cells | Reverse video border |
| Typography | Full SGR | Full SGR | Full SGR | Bold, dim, reverse only |

---

## §R8 Escape Sequence Quick Reference

### §R8.1 Cursor Movement

| Sequence | Action |
|----------|--------|
| `ESC[{n}A` | Cursor up n rows |
| `ESC[{n}B` | Cursor down n rows |
| `ESC[{n}C` | Cursor right n cols |
| `ESC[{n}D` | Cursor left n cols |
| `ESC[{row};{col}H` | Move cursor to row, col (1-based) |
| `ESC[s` | Save cursor position |
| `ESC[u` | Restore cursor position |
| `ESC[?25h` | Show cursor |
| `ESC[?25l` | Hide cursor |

### §R8.2 Scrolling Regions

| Sequence | Action |
|----------|--------|
| `ESC[{top};{bottom}r` | Set scrolling region (1-based row numbers) |
| `ESC[r` | Reset scrolling region to full screen |

### §R8.3 Screen Operations

| Sequence | Action |
|----------|--------|
| `ESC[2J` | Clear entire screen |
| `ESC[K` | Clear from cursor to end of line |
| `ESC[1K` | Clear from start of line to cursor |
| `ESC[2K` | Clear entire line |

### §R8.4 Mouse Tracking (SGR Extended)

| Sequence | Action |
|----------|--------|
| `ESC[?1000h` | Enable basic mouse tracking |
| `ESC[?1002h` | Enable button-event (drag) tracking |
| `ESC[?1003h` | Enable all-motion tracking |
| `ESC[?1006h` | Enable SGR extended encoding |
| `ESC[?1000l` | Disable mouse tracking |
| `ESC[?1006l` | Disable SGR encoding |

SGR mouse event format: `ESC[<{button};{col};{row}M` (press) or `m` (release).

Button values: 0=left, 1=middle, 2=right, 64=scroll-up, 65=scroll-down. Modifier bits: +4=Shift, +8=Meta, +16=Control.

---

## §R9 Mixed Border Junctions

When single-line and double-line borders meet (e.g., a Level 1 panel inside a Level 3 dialog), use mixed junction characters:

| Glyph | Unicode | Description |
|-------|---------|-------------|
| `╟` | U+255F | Double vertical, single right |
| `╢` | U+2562 | Double vertical, single left |
| `╤` | U+2564 | Single vertical, double horizontal (top) |
| `╧` | U+2567 | Single vertical, double horizontal (bottom) |
| `╫` | U+256B | Double vertical, single horizontal cross |
| `╪` | U+256A | Single vertical, double horizontal cross |
| `╓` | U+2553 | Double vertical, single horizontal (down-right) |
| `╖` | U+2556 | Double vertical, single horizontal (down-left) |
| `╙` | U+2559 | Double vertical, single horizontal (up-right) |
| `╜` | U+255C | Double vertical, single horizontal (up-left) |
