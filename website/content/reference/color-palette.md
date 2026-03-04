---
title: "§R3 256-Color Palette"
description: "Palette structure, semantic role mappings, status colors, and eight named palettes with examples"
weight: 3
---

## §R3.1 Palette Structure

| Index Range | Content |
|------------|---------|
| 0–7 | Standard ANSI colors (black, red, green, yellow, blue, magenta, cyan, white) |
| 8–15 | Bright ANSI colors |
| 16–231 | 6×6×6 color cube: `index = 16 + 36r + 6g + b` (r, g, b = 0–5) |
| 232–255 | 24-step grayscale ramp (232 = darkest, 255 = lightest) |

## §R3.2 Semantic Role → 256-Color Mapping

### Dark Theme (default)

| Semantic Role | Foreground (index) | Background (index) | Hex Approximation |
|--------------|-------------------|-------------------|-------------------|
| Primary | 75 (light blue) | 17 (dark blue) | fg #5fafff, bg #00005f |
| Secondary | 109 (muted blue) | 236 (dark gray) | fg #87afaf, bg #303030 |
| Tertiary | 79 (teal) | 236 (dark gray) | fg #5fd7af, bg #303030 |
| Error | 196 (bright red) | 52 (dark red) | fg #ff0000, bg #5f0000 |
| Neutral fg | 252 (light gray) | — | fg #d0d0d0 |
| Neutral fg bright | 231 (white) | — | fg #ffffff |
| Neutral bg | — | 235 (near-black) | bg #262626 |
| Surface | 252 | 234 (charcoal) | bg #1c1c1c |

**Neutral fg bright** is for text on colored backgrounds (headers, selected tabs, active indicators) where standard neutral fg lacks sufficient contrast.

### Light Theme

| Semantic Role | Foreground (index) | Background (index) | Hex Approximation |
|--------------|-------------------|-------------------|-------------------|
| Primary | 25 (dark blue) | 189 (light blue) | fg #005faf, bg #d7d7ff |
| Secondary | 66 (muted blue) | 254 (near-white) | fg #5f8787, bg #e4e4e4 |
| Tertiary | 30 (dark teal) | 254 (near-white) | fg #008787, bg #e4e4e4 |
| Error | 124 (dark red) | 224 (light pink) | fg #af0000, bg #ffd7d7 |
| Neutral fg | 235 (dark gray) | — | fg #262626 |
| Neutral bg | — | 255 (white) | bg #eeeeee |
| Surface | 235 | 231 (pure white) | bg #ffffff |

## §R3.3 Status Color Mapping

| Status | Dark Theme (FG index) | Light Theme (FG index) | Paired Symbol |
|--------|----------------------|----------------------|---------------|
| Healthy / Success | 40 (green) | 28 (dark green) | `◉` or `✓` |
| Error / Critical | 196 (bright red) | 124 (dark red) | `✗` or `●` |
| Warning / Caution | 220 (yellow) | 172 (orange) | `⚠` or `▲` |
| Inactive / Disabled | 240 (gray) | 247 (gray) | `○` or `—` |

## §R3.4 Named Palettes

The Dark Theme and Light Theme mappings above (§R3.2) define the default palettes. Applications MAY offer additional named palettes. Eight named palettes are defined here, drawn from the historical research that informs the standard. All palettes map to the same five semantic roles ([§5.1](/standard/color/#51-semantic-color-roles)); they differ only in color assignment.

### Default

Source: Textual framework default dark theme. This is the standard modern dark palette — the recommended starting point for new applications. It uses the same 256-color mappings defined in §R3.2 Dark Theme.

| Semantic Role | Foreground (index) | Background (index) | Hex Approximation |
|--------------|-------------------|-------------------|-------------------|
| Primary | 75 (light blue) | 17 (dark blue) | fg #5fafff, bg #00005f |
| Secondary | 109 (muted blue) | 236 (dark gray) | fg #87afaf, bg #303030 |
| Tertiary | 79 (teal) | 236 (dark gray) | fg #5fd7af, bg #303030 |
| Error | 196 (bright red) | 52 (dark red) | fg #ff0000, bg #5f0000 |
| Neutral fg | 252 (light gray) | — | fg #d0d0d0 |
| Neutral fg bright | 231 (white) | — | fg #ffffff |
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

### Monochrome

Source: CUA `cpAppMonochrome` system palette, Turbo Vision `cpAppBlackWhite` palette, and the capability-detection degradation path ([§5.6](/standard/color/#56-color-capability-detection)).

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

### Commander

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

### OS/2

Source: OS/2 Presentation Manager text-mode conventions as seen in OS/2 terminal emulators like Softerm. Yellow-green text on CGA blue, with light gray action bars and status lines. The window title bar uses yellow on dark blue. Selections use reverse video. Active windows use double-line borders with brighter attributes; inactive windows use single-line borders with dimmer attributes ([§5.5](/standard/color/#55-activeinactive-window-distinction)).

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
- **Active/inactive windows**: Bright borders (active) vs. dim borders (inactive), with double-line vs. single-line distinction ([§6.1](/standard/borders/#61-elevation-levels)).

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

### Turbo Pascal

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

### Amber Phosphor

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

### Green Phosphor

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

### Airlock

Source: The Airlock AI-agent security proxy — a guardrail enforcement layer that inspects, scores, and controls LLM tool-call traffic in real time. The palette uses Material Design–derived signal colors (`#4caf50` healthy, `#f44336` error, `#ff9800` warning) mapped to 256-color indices, paired with a cool neutral surface. The aesthetic communicates operational security: a calm, dark control-room backdrop with high-contrast status signals that demand attention only when something changes state.

| Semantic Role | Foreground (index) | Background (index) | Hex Approximation |
|--------------|-------------------|-------------------|-------------------|
| Primary | 71 (green) | 236 (dark gray) | fg #5faf5f, bg #303030 |
| Secondary | 109 (muted blue) | 236 (dark gray) | fg #87afaf, bg #303030 |
| Tertiary | 214 (orange) | 236 (dark gray) | fg #ffaf00, bg #303030 |
| Error | 167 (red) | 52 (dark red) | fg #d75f5f, bg #5f0000 |
| Neutral fg | 252 (light gray) | — | fg #d0d0d0 |
| Neutral fg bright | 231 (white) | — | fg #ffffff |
| Neutral bg | — | 235 (near-black) | bg #262626 |
| Surface | 252 | 234 (charcoal) | bg #1c1c1c |

Status colors:

| Status | Foreground (index) | Paired Symbol |
|--------|-------------------|---------------|
| Healthy / Live | 77 (green) | `◉` or `✓` |
| Error / Blocked | 167 (red) | `⊘` or `✗` |
| Warning / Paused | 214 (orange) | `⚠` or `⏸` |
| Inactive / Shadow | 245 (gray) | `○` or `—` |

Key conventions: Primary is green rather than blue — the healthy state is the dominant visual signal in a security proxy, reinforcing that traffic is flowing and guardrails are active. Tertiary is orange (the warning hue) because the "half-open" and "elevated score" states are the most operationally interesting. The status symbols include `⊘` (block) and `⏸` (paused) to match Airlock's enforcement vocabulary.

Example — Dashboard rendered in Airlock:

<pre class="palette-example palette-airlock"><span style="color:#585858">┌──</span> <span style="font-weight:bold;color:#5faf5f">Service Monitor</span> <span style="color:#585858">────────────────────────────────────────────────────────────┐
│</span> <span style="color:#87afaf">File  View  Help</span>                                                              <span style="color:#585858">│
├───────────────────────────────────────────────────────────────────────────────┤</span>
<span style="color:#585858">│</span>                                                                               <span style="color:#585858">│</span>
<span style="color:#585858">│</span>  CPU: 34%          Services: 12/12          Alerts: 3          Mem: 61%       <span style="color:#585858">│</span>
<span style="color:#585858">│</span>                                                                               <span style="color:#585858">│
├───────────────────────────────────────────────────────────────────────────────┤</span>
<span style="color:#585858">│</span> Service              │ Status   │ Uptime       │ CPU     │ Memory             <span style="color:#585858">│</span>
<span style="color:#585858">│</span>──────────────────────│──────────│──────────────│─────────│────────────────────<span style="color:#585858">│</span>
<span style="color:#585858">│</span> <span style="background:#303030;color:#5faf5f">> api-gateway        │ </span><span style="background:#303030;color:#5fd75f"> OK</span><span style="background:#303030;color:#5faf5f">      │ 14d  3h 22m  │   2.1%  │  340MB            </span> <span style="color:#585858">│</span>
<span style="color:#585858">│</span>   auth-service       │ <span style="color:#5fd75f"> OK</span>      │ 14d  3h 22m  │   0.8%  │  128MB             <span style="color:#585858">│</span>
<span style="color:#585858">│</span>   worker-pool        │ <span style="color:#ffaf00"> WARN</span>    │  0d  1h 45m  │  78.3%  │  1.2GB             <span style="color:#585858">│</span>
<span style="color:#585858">│</span>   notification-svc   │ <span style="color:#d75f5f"> DOWN</span>    │  0d  0h 00m  │   0.0%  │    0MB             <span style="color:#585858">│</span>
<span style="color:#585858">│</span>   metrics-collector  │ <span style="color:#5fd75f"> OK</span>      │ 14d  3h 22m  │   1.4%  │  256MB             <span style="color:#585858">│</span>
<span style="color:#585858">│</span>                                                                               <span style="color:#585858">│
├───────────────────────────────────────────────────────────────────────────────┤</span>
<span style="color:#585858">│</span><span style="color:#87afaf"> ? Help  r Refresh  / Filter  q Quit                             5 services    </span><span style="color:#585858">│</span>
<span style="color:#585858">└───────────────────────────────────────────────────────────────────────────────┘</span></pre>
