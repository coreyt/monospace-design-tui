---
title: "Foundational Research"
subtitle: "A synthesis of legacy TUI and modern HCI research"
description: "Seven decades of interaction design — IBM CUA, OS/2, Material Design 3, Apple HIG, KLM, terminal capabilities, and historical TUI applications"
---

## 1. IBM Common User Access: the original text interface grammar

IBM's CUA standard, published between 1987 and 1992, defined three interface tiers that remain the most thorough specification of text-mode interaction ever produced.

### Three interface models

CUA specifies an **Entry Model** (full-screen panels with function-key navigation, no action bars), a **Text Subset of the Graphical Model** (adds action bars, pull-down menus, and pop-up windows to text mode), and the full **Graphical Model** (OS/2 Presentation Manager, mouse-driven). The Entry Model targets non-programmable 3270-type terminals; the Text Subset targets higher-function character-mode displays with cursor addressing; the Graphical Model targets windowed GUI environments. The critical distinction: **the Text Subset adds action bars and pull-downs to the Entry Model**, while sharing all other components (entry fields, check boxes, radio buttons, lists).

### Standard menu hierarchy

CUA defines a **three-level menu hierarchy**: Action Bar → Pull-Down Menu → Cascaded Menu. The standard action bar order is `File  Edit  View  Selected  Options  Windows  Help`, limited to **6 choices** separated by two or more spaces. Pull-down menus appear directly below their action bar item, limited to **10 choices**, with separator lines grouping related items. Cascaded menus extend to the right, indicated by `▸`. An ellipsis suffix (`...`) signals that selection will open a dialog requiring further input. Unavailable items remain visible but dimmed — never hidden.

### Keyboard navigation standard

The CUA keyboard map became the template for all subsequent text interfaces:

| Key | Function |
|-----|----------|
| **F1** | Context-sensitive help |
| **F3** | Exit current level |
| **F4** | Prompt (show alternatives for entry field) |
| **F5** | Refresh |
| **F7 / Page Up** | Scroll backward |
| **F8 / Page Down** | Scroll forward |
| **F10 / Alt** | Activate action bar |
| **F12 / Esc** | Cancel (return to previous panel) |
| **Tab / Shift+Tab** | Next / previous field (left-to-right, top-to-bottom) |
| **Enter** | Process / confirm |
| **Ctrl+X / Shift+Del** | Cut |
| **Ctrl+C / Ctrl+Ins** | Copy |
| **Ctrl+V / Shift+Ins** | Paste |
| **Ctrl+Z** | Undo |
| **Alt+F4** | Close window |

Navigation order follows **left-to-right, top-to-bottom** for Western languages, wrapping from last to first field. Arrow keys move *within* a control (e.g., between radio buttons in a group or characters in an entry field). **F10** toggles focus between panel body and action bar.

### Mnemonic assignment rules

Mnemonics (underlined characters enabling single-keystroke selection) must be **unique within their menu level**, cannot be blanks, and should prefer the **first letter** of the item text. In resource files, a tilde (`~`) or ampersand (`&`) prefix marks the mnemonic character. Typing the mnemonic character while a menu is active selects that item immediately.

### Component specifications (text mode)

| Component | Visual Representation | Behavior |
|-----------|----------------------|----------|
| **Action bar** | Reverse-video text labels on row 1 | F10/Alt activates; mnemonic letters highlighted |
| **Pull-down menu** | Single-line bordered vertical list | Arrow keys navigate; Enter selects; Esc closes |
| **Entry field** | `Name: ____________` (underscores/dots fill space) | Arrow keys move within; Tab moves to next field |
| **Push button** | `< OK >` or `< Cancel >` | Enter/Space activates; one default button per dialog |
| **Check box** | `[X] Option` / `[ ] Option` | Space toggles; non-mutually-exclusive |
| **Radio button** | `(*) Option A` / `( ) Option B` | Arrow keys cycle; mutually exclusive within group |
| **List box** | Bordered scrollable list with highlight bar | Arrow keys move selection; Page Up/Down scroll |
| **Spin button** | Sequential ring of choices with ±controls | Max 20 choices recommended |

### State indicators

**Active** windows display at normal intensity with cursor positioned inside. **Inactive** windows appear dimmed. **Focus** is indicated by cursor placement (blinking block or underline). **Disabled** items render in low-intensity/dim text but remain visible. **Selected** items use reverse video or fill marks (`[X]`, `(*)`). Pop-up windows use distinct color schemes by severity: **notification** (white/neutral), **warning** (yellow), **critical** (red), with alternating colors for stacked pop-ups.

### CUA text-mode panel layout

```
┌─────────────────────────────────────────────────┐
│ Action Bar (File  Edit  View  Help)              │ ← Line 1
│─────────────────────────────────────────────────│ ← Separator
│ Panel Title / Panel ID                           │
│                                                  │
│ Panel Body (scrollable content area)             │
│   Entry fields, selection lists, controls        │
│                                                  │
│ Command ===>                                     │ ← Command line
│ Message line                                     │
│ F1=Help  F3=Exit  F7=Bkwd  F8=Fwd  F10=Actions │ ← Function key area
└─────────────────────────────────────────────────┘
```

---

## 2. OS/2 text-mode design: character-cell engineering

### Grid fundamentals

OS/2 text mode operated on a VGA character-cell grid. **80×25** (9×16 pixel cells, 720×400 resolution) was the universal baseline. **80×43** (8×8 cells via EGA) and **80×50** (8×8 cells via VGA) provided denser modes. Each cell occupied 2 bytes in video memory: one character byte plus one attribute byte encoding **4-bit foreground + 4-bit background = 16 colors**.

The VIO (Video I/O) subsystem replaced DOS BIOS calls with protected-mode APIs: `VioGetBuf` (obtain logical buffer), `VioShowBuf` (flush to screen), `VioSetMode` (switch resolution), `VioWrtCellStr` (write character-attribute pairs). Advanced VIO (AVIO) allowed text-mode applications to run inside Presentation Manager windows, with PM handling rendering via monospaced fonts.

### Box-drawing character standards

OS/2 used IBM Code Page 437 (CP437) box-drawing characters (Unicode block U+2500–U+257F equivalents):

**Single-line set:** `─` (0xC4) `│` (0xB3) `┌` (0xDA) `┐` (0xBF) `└` (0xC0) `┘` (0xD9) `├` (0xC3) `┤` (0xB4) `┬` (0xC2) `┴` (0xC1) `┼` (0xC5)

**Double-line set:** `═` (0xCD) `║` (0xBA) `╔` (0xC9) `╗` (0xBB) `╚` (0xC8) `╝` (0xBC) `╠` (0xCC) `╣` (0xB9) `╦` (0xCB) `╩` (0xCA) `╬` (0xCE)

**Shade/block characters:** `░` (0xB0, 25%) `▒` (0xB1, 50%) `▓` (0xB2, 75%) `█` (0xDB, full) `▄` (0xDC, lower half) `▀` (0xDF, upper half) `▌` (0xDD, left half) `▐` (0xDE, right half)

### Window decoration conventions

**Active/primary windows** used **double-line** borders (`╔═╗║╚═╝`) with brighter color attributes. **Inactive windows** used **single-line** borders (`┌─┐│└─┘`) with dimmer attributes. Pop-up menus used single-line frames. Window titles were centered in the top border: `╔══ Title ══════════╗`. Close button rendered as `[■]` at top-left; zoom as `[↕]` at top-right. **Shadows** simulated depth via a **2-column × 1-row offset** beneath windows, changing underlying characters to attribute **0x08** (dark gray on black) while preserving their character codes.

### Responsive adaptation

Applications queried dimensions via `VioGetMode` (returning `VIOMODEINFO` with `row`, `col`, `hres`, `vres`, `color` fields). The standard strategy: **design for 80×25 as baseline**, then expand content areas for 80×43 and 80×50 modes. Centering formula: `start = (available_space - content_size) / 2` for both axes. Action bar always occupied row 1; function key area always occupied the bottom row(s). In windowed AVIO mode, PM handled scrolling if the window was smaller than the logical buffer.

### Mnemonic marking

Mnemonics were indicated in source files via **tilde** (`~F~ile`) or **ampersand** (`&File`) prefixes, rendered as underlined or highlighted-color characters. The mnemonic letter was displayed in a contrasting color (e.g., bright white when surrounding text was cyan). The standard color convention: **white on blue** (0x1F) for normal text, **black on white/cyan** for action bars, **reverse video** for selections, **red background** for errors, and **distinct color schemes** for help windows versus main panels.

---

## 3. Material Design 3: modern design tokens for text translation

### Layout grid and spacing system

M3 uses a **4dp base grid** (8dp for general layout) with window size classes that map naturally to terminal widths:

| Window Size Class | Width Range | Grid Columns | Margins | Gutters |
|---|---|---|---|---|
| **Compact** | < 600dp | 4 | 16dp | 8dp |
| **Medium** | 600–839dp | 8–12 | 24dp | 16–24dp |
| **Expanded** | 840–1199dp | 12 | 24dp | 24dp |
| **Large** | 1200–1599dp | 12 | 24dp | 24dp |
| **Extra-large** | ≥ 1600dp | 12 | 24dp | 24dp |

**Spacing tokens** follow a progressive scale: **0, 4, 8, 12, 16, 24, 32, 48, 64dp**. M3's four **canonical layouts** — List-Detail, Supporting Pane, Feed, and Hero/Detail — provide adaptive templates that map to TUI archetypes (dual-pane, sidebar, grid, and master-detail).

### Navigation pattern specifications

**Navigation bar** (bottom, for compact): **80dp tall**, 24dp icons, pill-shaped active indicator (64×32dp) using secondary-container color, **3–5 destinations**. **Navigation rail** (side, for medium): **80dp wide**, 56×32dp active indicator, **3–7 destinations**, optional FAB at top. **Navigation drawer** (persistent, for expanded): **256–360dp wide**, 56dp item height, full-width rounded rectangle active indicator. The selection rule: compact → bottom bar, medium → rail, expanded → drawer.

### Component dimensions

**Buttons:** All types are **40dp tall** with **20dp full-round corner radius** and **24dp left/right padding**. Label uses label-large typography (**14sp, 500 weight, 0.1sp tracking**). Minimum touch target: **48×48dp**. Disabled state: container at **12% on-surface**, content at **38% on-surface**.

**Text fields:** **56dp tall**, 16dp horizontal padding, body-large input text (16sp), body-small label (12sp when focused). Filled variant: 4dp top corners, 1dp bottom indicator. Outlined: 1dp border (2dp on focus).

**Cards:** **12dp corner radius**, 16dp content padding. Elevated type at Level 1 (1dp). Outlined type has 1dp border at Level 0.

**Dialogs:** **280dp min / 560dp max width**, **28dp corner radius**, 24dp padding all sides, Level 3 elevation (6dp). Title: headline-small (24sp). Body: body-medium (14sp). 16dp gap between title and body.

**Chips:** **32dp tall**, **8dp corner radius**, 16dp padding, label-large typography (14sp). 1dp outline when unselected; filled when selected.

**Menus:** **48dp item height**, 112dp min / 280dp max width, Level 2 elevation (3dp), 4dp corner radius, 8dp vertical padding.

**Data tables:** **52dp default row height** (36dp dense), 56dp header row, 16dp cell horizontal padding, 56dp checkbox column width.

### State layer system

M3's state system uses a **single translucent overlay** at the content color with defined opacity:

| State | Opacity | Notes |
|---|---|---|
| **Enabled** | 0% | No overlay |
| **Hovered** | 8% | Low emphasis |
| **Focused** | 10% | + focus ring |
| **Pressed** | 10% | Ripple feedback |
| **Dragged** | 16% | Highest active overlay |
| **Disabled container** | 12% on-surface | |
| **Disabled content** | 38% on-surface | |

The state layer color matches the content's "on-" color (e.g., a filled button with `primary` container uses `on-primary` at the relevant opacity). Only **one state layer** is rendered at a time.

### Motion and duration tokens

M3 defines **16 duration tokens** in a linear progression from **50ms (Short 1) to 1000ms (Extra Long 4)**, incrementing by 50ms. Standard easing: `cubic-bezier(0.2, 0, 0, 1)`. Emphasized decelerate: `cubic-bezier(0.05, 0.7, 0.1, 1)`. Emphasized accelerate: `cubic-bezier(0.3, 0, 0.8, 0.15)`. Desktop animations should run **~30% faster** than mobile. Standard component transitions: **250–300ms**.

### Typography scale (15 tokens)

| Role | Size (sp) | Line Height | Weight | Tracking |
|---|---|---|---|---|
| Display Large | 57 | 64 | 400 | -0.25 |
| Display Medium | 45 | 52 | 400 | 0 |
| Display Small | 36 | 44 | 400 | 0 |
| Headline Large | 32 | 40 | 400 | 0 |
| Headline Medium | 28 | 36 | 400 | 0 |
| Headline Small | 24 | 32 | 400 | 0 |
| Title Large | 22 | 28 | 400 | 0 |
| Title Medium | 16 | 24 | 500 | 0.15 |
| Title Small | 14 | 20 | 500 | 0.1 |
| Body Large | 16 | 24 | 400 | 0.5 |
| Body Medium | 14 | 20 | 400 | 0.25 |
| Body Small | 12 | 16 | 400 | 0.4 |
| Label Large | 14 | 20 | 500 | 0.1 |
| Label Medium | 12 | 16 | 500 | 0.5 |
| Label Small | 11 | 16 | 500 | 0.5 |

### Color system and elevation

M3 generates **five key color tonal palettes** (Primary, Secondary, Tertiary, Error, Neutral) using the **HCT color space**, each with **13 tones** (0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 99, 100). Light theme uses Tone-40 for primary, Tone-80 for dark theme. Surface containers form a 5-level hierarchy: `surface-container-lowest` through `surface-container-highest`.

**Elevation levels** map to tonal surface tint rather than shadows: Level 0 (0dp, 0% tint), Level 1 (1dp, 5%), Level 2 (3dp, 8%), Level 3 (6dp, 11%), Level 4 (8dp, 12%), Level 5 (12dp, 14%). **Shape tokens** range from `corner-none` (0dp) through `corner-extra-small` (4dp), `corner-small` (8dp), `corner-medium` (12dp), `corner-large` (16dp), `corner-extra-large` (28dp), to `corner-full` (50%).

---

## 4. Apple HIG: accessibility-first interaction principles

### Layout and spatial model

Apple uses an **8-point grid** with resolution-independent points (1pt = 1px @1x, 2px @2x Retina). Layout margins: **16pt compact / 20pt regular width**. Size classes divide devices into compact width (iPhone portrait), regular width (iPad, iPhone landscape), compact height (iPhone landscape), and regular height. The **readable content guide** constrains text width for legibility on wide displays.

### Navigation architecture

**Tab bars** (bottom, 3–5 tabs on iPhone, 49pt standard height) provide flat top-level navigation. **Navigation bars** (44pt height excluding status bar) enable hierarchical drill-down with back button, centered title, and right-aligned actions. **Large titles** display at 34pt font size and collapse to inline on scroll. **Sidebars** serve as persistent vertical navigation on iPadOS/macOS. Modal presentations require clear Done/Cancel buttons and support swipe-to-dismiss.

**Progressive disclosure** is a core principle: show only essential information initially, reveal detail on demand via disclosure triangles, expandable sections, and context-dependent formatting toolbars.

### Accessibility specifications

Apple's accessibility requirements directly inform keyboard-first TUI design:

- **Minimum touch target: 44×44pt** on iOS/iPadOS (exceeding WCAG AAA requirements of 24×24px)
- **Color contrast: 4.5:1 minimum** for normal text, 3:1 for large text (18pt+ regular or 14pt+ bold)
- **Color independence**: Never use color as the sole information carrier — pair with text, icons, or patterns
- **Dynamic Type scale**: Large Title (34pt), Title 1 (28pt), Title 2 (22pt), Headline (17pt semibold), Body (17pt), Subheadline (15pt), Footnote (13pt), Caption 1 (12pt), Caption 2 (11pt minimum)
- **Reduced motion**: Replace animations with crossfades when system setting is active
- Every interactive element requires a **meaningful accessibility label** describing purpose (not appearance)
- **Focus management**: Tab/Shift-Tab between focus groups, arrow keys within groups, Escape dismisses transient UI

### Keyboard shortcut conventions

Apple's modifier hierarchy: **⌘ Command** (primary, most shortcuts), **⌥ Option** (alternative behavior), **⌃ Control** (system-level), **⇧ Shift** (extend/reverse). Ergonomic preference: keys nearest modifiers reachable with index/middle fingers (Q, W, E, A, S, D, O, P). The full standard shortcut table (⌘+C/V/X/Z/S/N/O/P/W/Q/F/A, ⌘+Shift+Z for Redo, ⌘+, for Settings) established conventions now universal across platforms.

### State and feedback

Button states: **Default** (standard tint), **Highlighted/Pressed** (dimmed/darkened, slight scale), **Disabled** (~30–40% opacity), **Selected** (accent color fill), **Focused** (blue halo ring ~3–4px). The **focus ring** follows the element's shape, uses `keyboardFocusIndicatorColor` (system blue #0A84FF by default). **Haptic feedback types**: Impact (light/medium/heavy), Selection (subtle tick), Notification (success/warning/error).

---

## 5. Keystroke-Level Model: quantifying keyboard-first efficiency

### Operator time values

Card, Moran, and Newell's KLM (1980/1983) provides the foundational efficiency model for comparing interaction paths:

| Operator | Description | Time |
|---|---|---|
| **K** (Best typist, 135 wpm) | Keystroke | **0.08 sec** |
| **K** (Expert, 90 wpm) | Keystroke | **0.12 sec** |
| **K** (Average skilled, 55 wpm) | Keystroke | **0.20 sec** |
| **K** (Average non-secretarial, 40 wpm) | Keystroke | **0.28 sec** (default) |
| **K** (Worst, hunt-and-peck) | Keystroke | **1.20 sec** |
| **P** | Point to target (mouse) | **1.10 sec** (0.8–1.5 range) |
| **H** | Home hand between keyboard/mouse | **0.40 sec** |
| **M** | Mental preparation | **1.35 sec** (σ ≈ 1.1) |
| **B** | Mouse button press/release | **0.10 sec** (BB click = 0.20) |
| **R/W** | System response wait | Variable |

The prediction formula: **T_execute = ΣK + ΣP + ΣH + ΣM + ΣB + ΣR**. M operators are placed via heuristic rules: insert M before all non-argument K's and command-selecting P's (Rule 0), then delete M's that are fully anticipated (Rule 1), part of cognitive units like command names (Rule 2), redundant terminators (Rule 3), or constant-string terminators (Rule 4).

### The keyboard efficiency advantage

KLM analysis reveals a **58% speed advantage** for keyboard shortcuts over mouse-driven menu navigation on common tasks:

| Task | Keyboard Path | Mouse Path | Savings |
|---|---|---|---|
| Save file (Ctrl+S) | M+2K = **1.91 sec** | M+H+P+B+P+B+H = **4.55 sec** | **2.64 sec (58%)** |
| Copy (Ctrl+C) | M+2K = **1.91 sec** | M+H+P+B+P+B+H = **4.55 sec** | **2.64 sec (58%)** |
| Bold (Ctrl+B) | M+2K = **1.91 sec** | M+H+P+BB+H = **3.45 sec** | **1.54 sec (45%)** |

Keyboard-first interfaces eliminate H operators entirely (hands never leave keyboard), replace P operators with faster K operators (0.12–0.28 sec vs. 1.10 sec), and support **chunking** where expert users execute entire command sequences as single cognitive units (one M for an entire command string).

### Fitts's Law does not apply to keyboard navigation

Fitts's Law (**MT = a + b × log₂(D/W + 1)**) models continuous pointing movements with a logarithmic speed-accuracy tradeoff. Keyboard navigation is **discrete and linear**: T = n × K, where n = number of keypresses to reach target. There is no "keyboard Fitts's Law" in mainstream HCI literature. However, Fitts's Law does inform the P operator's 1.10-second average. For known commands, **keyboard beats pointing** (2K ≈ 0.56 sec vs. H+P+B ≈ 1.60 sec). For spatial selection among unknown targets, pointing wins. The crossover: keyboard becomes faster than mouse after moderate practice (days, not weeks), but most users "satisfice" and never invest in learning shortcuts.

---

## 6. Terminal technical capabilities: the modern rendering substrate

### ANSI/SGR escape sequences

All terminal styling uses CSI sequences (`ESC[{params}m`). The complete attribute set:

**Styling:** Bold (1), Dim (2), Italic (3), Underline (4), Slow Blink (5), Rapid Blink (6), Reverse (7), Hidden (8), Strikethrough (9), Double Underline (21), Overline (53). Each has a corresponding reset code (22, 23, 24, 25, 27, 28, 29, 54, 55).

**Standard colors (foreground/background):** Black (30/40), Red (31/41), Green (32/42), Yellow (33/43), Blue (34/44), Magenta (35/45), Cyan (36/46), White (37/47). **Bright variants:** 90–97 foreground, 100–107 background. Default reset: 39/49.

**256-color mode:** `ESC[38;5;{n}m` (fg) / `ESC[48;5;{n}m` (bg). Palette structure: indices **0–7** = standard colors, **8–15** = bright colors, **16–231** = 6×6×6 color cube (index = 16 + 36r + 6g + b, where 0 ≤ r,g,b ≤ 5), **232–255** = 24-step grayscale ramp.

**True color (24-bit):** `ESC[38;2;{r};{g};{b}m` (fg) / `ESC[48;2;{r};{g};{b}m` (bg). Supported by xterm (252+), iTerm2, kitty, Alacritty, WezTerm, Windows Terminal, all libvte terminals. **Not** supported by macOS Terminal.app. Detection: check `COLORTERM=truecolor` or `COLORTERM=24bit`, then `TERM` containing `256color`, then fallback to 8 colors.

### Unicode box-drawing for modern TUI chrome

The Unicode Box Drawing block (U+2500–U+257F) provides **128 characters** across light, heavy, double, and mixed styles plus **rounded corners** (╭╮╰╯ at U+256D–U+2570). Block Elements (U+2580–U+259F) include half-blocks, quarter-blocks, and shade characters. **Braille patterns** (U+2800–U+28FF, 256 characters) enable **2×4 sub-cell pixel rendering** — each character encodes 8 dots at positions mapped to bits, achieving 2× horizontal and 4× vertical resolution over character cells. This powers sparklines, mini-charts, and smooth progress indicators in modern TUI frameworks.

### Terminal responsive design

**SIGWINCH** (signal 28) fires when the terminal resizes. Applications install a handler via `sigaction()` and query new dimensions with `ioctl(STDOUT_FILENO, TIOCGWINSZ, &ws)` returning `ws_row` and `ws_col`. Alternative methods: `tput cols`/`tput lines`, `$COLUMNS`/`$LINES` environment variables, or CSI query `ESC[18t`. The new POSIX 2024 standard adds `tcgetwinsize()`. Recommended breakpoints: **full layout ≥ 120 cols, standard ≥ 80 cols, compact ≥ 40 cols**, with a minimum convention of **80×24** (VT100 legacy) or **60×20** for complex TUIs.

### Mouse protocol

**SGR extended encoding (mode 1006)** is the recommended modern protocol: enable with `ESC[?1006h`, events reported as `CSI < Cb;Cx;Cy M` (press) or `m` (release). Button values: 0=left, 1=middle, 2=right, 64=scroll-up, 65=scroll-down. Modifier bits in Cb: 4=Shift, 8=Meta, 16=Control. No coordinate limit. Enable basic tracking with `ESC[?1000h`, drag tracking with `ESC[?1002h`, all-motion with `ESC[?1003h`.

### Screen reader accessibility: the critical gap

**TUI accessibility is fundamentally broken.** Screen readers (Speakup on Linux, NVDA/JAWS on Windows, VoiceOver on macOS) track cursor position to announce text changes. When TUI frameworks aggressively redraw — moving the cursor to update spinners, status bars, and reactive widgets — screen readers produce unintelligible noise. There is **no terminal equivalent of ARIA** for semantic markup. Best practices: prefer linear/stream output over grid rendering, minimize cursor movement, use VT100 scrolling regions (`ESC[{top};{bottom}r`) instead of full redraws, offer HTML export alternatives for complex content, and batch visual updates. Modern reactive frameworks (Ink, Bubbletea) are often *worse* than simple CLIs for accessibility because their canvas-style rendering creates cursor chaos.

### Modern framework architectures

Four dominant patterns have emerged:

**Textual (Python):** DOM-like widget tree with **CSS-like styling (TCSS)** — selectors, `fr`/`%`/`vw`/`vh` units, docking, grid layout. Reactive attributes auto-trigger CSS updates. Event bubbling through widget tree. Best-in-class accessibility with screen reader integration and command palette.

**Bubbletea (Go):** The **Elm Architecture** (Model-Update-View). `Init() Cmd`, `Update(Msg) (Model, Cmd)`, `View() string`. Immutable state, side effects via commands, framerate-based rendering. Lip Gloss for styling. Layout is manual string concatenation.

**Ratatui (Rust):** **Immediate-mode rendering** with Cassowary constraint solver for layout. `Layout::vertical()`/`horizontal()` with constraints: `Length(n)`, `Min(n)`, `Max(n)`, `Percentage(n)`, `Fill(weight)`. Buffer diffing for efficient updates. Most performant.

**Blessed (Node.js):** Traditional **widget/event pattern** with absolute positioning. Largely unmaintained but established the widget vocabulary (Box, List, Table, Form, Input, etc.) used by successors.

---

## 7. Historical TUI applications: proven interaction archetypes

### Norton Commander and the Orthodox File Manager paradigm

Norton Commander established the **dual-pane file manager** archetype in the late 1980s. Layout: **Row 1** = menu bar (Left, Files, Disk, Commands, Right), **Rows 2–22** = two equal-width file panels with title bars and status lines, **Row 23** = DOS command line, **Rows 24–25** = function key bar. The F-key assignments became a de facto standard:

**F1**=Help, **F2**=User Menu, **F3**=View, **F4**=Edit, **F5**=Copy, **F6**=Rename/Move, **F7**=Mkdir, **F8**=Delete, **F9**=Pull-down menus, **F10**=Quit. **Tab** switches the active panel. **Insert** selects/deselects files (shown in yellow). **Ctrl+O** toggles panels to reveal full command line.

The **Orthodox File Manager (OFM)** paradigm, codified by Dr. Nikolai Bezroukov, defines: dual symmetric panels, three logical frames (left panel, right panel, command line), command line integration, F-key operations, keyboard-first interaction, built-in viewer/editor, virtual filesystem (archives as directories), and user-customizable menus.

Color conventions: **blue background** (0x1_ attribute), white/cyan filenames, **yellow** for selected files, **cyan** for pull-down menus, **gray** for dialog boxes, **red** for errors. This blue-panel aesthetic became the canonical DOS TUI look.

### Borland Turbo Vision: the definitive TUI component framework

Turbo Vision (1990) created a complete **object-oriented widget toolkit** for text mode with a CUA-influenced interaction model. The hierarchy: `TObject → TView → TGroup → TWindow → TDialog`, with specialized controls: `TButton`, `TInputLine`, `TCheckBoxes`, `TRadioButtons`, `TListBox`, `TScrollBar`, `TMenuBar`, `TStatusLine`, `TLabel`, `THistory`, `TEditor`.

**Coordinate model:** `TRect(ax, ay, bx, by)` with origin (0,0) at top-left of owning view. All coordinates relative to owner. **Event architecture:** Three-phase processing — PreProcess (flagged views), Focused (selected subview), PostProcess (flagged views). Event types: mouse (`evMouseDown/Up/Move/Auto`), keyboard (`evKeyDown`), command (`evCommand`), broadcast (`evBroadcast`).

**Hierarchical palette system:** Each view has its own palette indices that chain through owners to the application's master 63-entry palette of BIOS color attributes. Three system palettes auto-detected: `cpAppColor`, `cpAppBlackWhite`, `cpAppMonochrome`. Key colors: desktop 0x71 (blue on light gray), window frame 0x17 (white on blue), dialog frame 0x70 (black on light gray), button normal 0x20 (black on green), input passive 0x1F (white on blue).

**Component visuals:** `TButton` renders as `[ OK ]` with shadow, default button marked with `» OK «`. `TWindow` uses double-line borders with `[■]` close and `[↕]` zoom buttons. Shadows: **2 columns × 1 row offset**, attribute 0x08 (dark gray on black). `TMenuBar` uses `~` to mark hotkeys: `~F~ile`. `TStatusLine` shows `~F1~ Help  ~Alt+X~ Exit`.

### Modern TUI exemplars and their patterns

**Midnight Commander** preserves Norton Commander's layout and all F-key bindings while adding VFS (archives, FTP/SFTP), subshell integration, and full mouse support. **htop/btop** pioneered the dashboard archetype: configurable header meters (bar/text/graph/LED), sortable process table, F-key footer. btop extended this with Braille-character graphs, rounded corners, and truecolor support. **Vim/Neovim** demonstrated that **modal interfaces** with composable commands (`[count][operator][motion]`) achieve the highest keystroke efficiency for text manipulation. **tmux** introduced the **prefix-key model** (Ctrl+B → command) for multiplexed pane/window/session management. **lazygit** pioneered **context-sensitive panels** where available keys change per focused view. **ranger** brought **Miller columns** (parent | current | preview) to the terminal. **fzf** established the **fuzzy finder pattern** — type-to-filter with ranked results, composable via Unix pipes.

### Six keyboard interaction models across history

1. **Function key model** (Norton Commander): F1–F10 as primary operations, Ctrl/Alt/Shift modifiers extend
2. **CUA model** (Turbo Vision): Alt activates menus, Tab navigates, standardized shortcuts
3. **Modal model** (Vim): Mode-dependent key interpretation, composable grammar
4. **Prefix model** (tmux/screen): Leader key followed by command key
5. **Fuzzy/incremental** (fzf): Type-to-filter with ranked results
6. **Context-panel model** (lazygit): Available keys change per focused panel

---

## Cross-cutting synthesis: design tokens for Monospace TUI

### Mapping M3 concepts to character cells

The translation from pixel-based design tokens to character-cell equivalents follows a natural mapping. M3's 4dp base grid becomes **1 character cell** as the Monospace TUI atomic unit. M3's compact layout margins (16dp) translate to **2 character columns**. M3's navigation rail (80dp wide) maps to **~10 columns**. M3's button height (40dp) maps to **1 row with padding characters**. The 15-level typography scale collapses to approximately 4 text treatments in a terminal: **bold** (headings), **normal** (body), **dim** (secondary/disabled), and **reverse** (selected/focused).

M3's elevation system translates directly to TUI layering: Level 0 = inline content, Level 1 = raised panels (single-line borders), Level 2 = menus (single-line borders with shadows), Level 3 = dialogs (double-line borders with shadows), Level 4 = modal overlays. M3's tonal surface-tint approach can be approximated through background color variation across the 256-color or truecolor palette.

### Unified state model

Combining CUA, M3, and Apple HIG state definitions yields a comprehensive state model for Monospace TUI:

| State | CUA Indicator | M3 Opacity | Apple Visual | Monospace TUI Rendering |
|---|---|---|---|---|
| **Enabled** | Normal intensity | 0% | Standard tint | Normal text + color |
| **Focused** | Cursor position + blink | 10% | Blue halo ring | Reverse video or bracket markers |
| **Hovered** | (N/A in text) | 8% | (Mouse only) | Highlight bar / underline |
| **Pressed** | (N/A in text) | 10% | Dimmed/scaled | Brief reverse flash |
| **Selected** | Reverse video / fill mark | Accent fill | Accent background | Reverse video or `[X]`/`(*)` marks |
| **Disabled** | Low intensity / dim | 12%+38% | 30–40% opacity | Dim attribute (SGR 2) |
| **Error** | Red background | Error color | Red text + shake | Red foreground or background |

### Color systems across the research vectors

Each research vector contributed a distinct approach to color in text-mode interfaces. Synthesizing them reveals both a shared structure and a clear evolution from hardware-constrained palettes to semantic color systems.

**The 16-color era: attribute bytes and fixed palettes.** OS/2 and DOS applications encoded color as a single attribute byte per character cell — 4 bits foreground, 4 bits background, yielding 16 possible colors drawn from the IBM CGA/EGA/VGA palette. This was not a limitation designers worked around; it was the design medium itself. The CUA standard established conventions within these 16 colors: **white on blue** (attribute 0x1F) for normal text, **black on white or cyan** for action bars, **reverse video** for selections, **red backgrounds** for error states, and **distinct color schemes** to differentiate help windows from main panels. These conventions were not arbitrary — they maximized readability on CRT displays where blue backgrounds reduced flicker perception and white-on-blue provided strong contrast without the harshness of white-on-black.

**Norton Commander and the blue-panel canonical aesthetic.** Norton Commander codified what became the definitive DOS TUI look: a **blue background** (attribute 0x1_) as the universal surface color, **white and cyan** for filenames, **yellow** for selected files, **cyan** for pull-down menus, **gray** for dialog boxes, and **red** for errors. This palette was not just one application's choice — it became the expected appearance of professional DOS software. Midnight Commander, FAR Manager, and dozens of other tools adopted it wholesale. The blue-panel aesthetic persists in modern terminal applications as a deliberate retro reference.

**Turbo Vision's hierarchical palette system.** Borland's Turbo Vision (1990) introduced the most sophisticated color architecture of the text-mode era: a **63-entry master palette** of BIOS color attributes, with each widget type maintaining its own palette indices that chain through the ownership hierarchy to resolve against the application's master palette. Three system palettes were auto-detected based on display capability: `cpAppColor` (16-color), `cpAppBlackWhite` (monochrome with intensity), and `cpAppMonochrome` (monochrome without intensity). Key entries in the color palette: desktop 0x71 (blue on light gray), window frame 0x17 (white on blue), dialog frame 0x70 (black on light gray), button normal 0x20 (black on green), input field 0x1F (white on blue). The critical insight: **Turbo Vision separated color assignment from widget logic**, allowing the entire application's appearance to change by swapping the master palette — the same architecture that modern theming systems rediscovered decades later.

**Phosphor displays: single-hue terminals.** Before color terminals existed, DEC VT100 and VT101 terminals used **green phosphor (P1)** displays — bright green characters on a black background. DEC VT220 and VT320 terminals offered **amber phosphor (P3)** as an alternative, preferred in business environments for reduced eye strain during extended use. Control Data Corporation's PLATO terminals used amber-orange plasma displays. IBM 3278 terminals used green phosphor. On these monochrome displays, all visual hierarchy was achieved through **brightness variation** (normal, bold, dim) and **SGR attributes** (reverse video, underline, blink). This constraint produced an important design principle: **a well-designed TUI must be fully usable without color**, relying on typography and spatial organization rather than chromatic differentiation.

**Material Design 3: semantic color as a system.** M3's contribution is architectural rather than aesthetic. Its **HCT color space** generates five tonal palettes (Primary, Secondary, Tertiary, Error, Neutral), each with 13 tonal steps from 0 (black) to 100 (white). Colors are assigned by **semantic role**, never by specific hue — a primary button is "primary" whether that resolves to blue, purple, or green. Light and dark themes are achieved by selecting different tonal steps from the same palettes (Tone-40 for light, Tone-80 for dark). This approach translates directly to terminal color systems: define semantic roles, then map them to different concrete palettes (16-color, 256-color, truecolor) depending on terminal capability.

**Apple HIG: color independence as accessibility requirement.** Apple's Human Interface Guidelines contributed the non-negotiable rule that **color must never be the sole indicator of state or meaning**. Every use of color must be paired with at least one non-chromatic indicator: a text label, a typographic attribute (bold, dim, underline), or a symbol (`✓`, `✗`, `⚠`). This rule intersects with the phosphor-display principle — if the interface works on a monochrome terminal, it satisfies color independence by construction.

**Synthesis for Monospace TUI.** The named palettes in the Rendering Reference (§R3.4) — Default, Monochrome, OS/2, Turbo Pascal, Amber Phosphor, Green Phosphor, and Airlock — are not arbitrary inventions. They are direct encodings or modern reinterpretations of historical terminal and text-mode color systems within the standard's semantic role framework. The Monochrome palette implements Turbo Vision's `cpAppMonochrome` strategy. The OS/2 and Turbo Pascal palettes preserve IBM and Borland blue-panel traditions. The phosphor palettes preserve the DEC terminal single-hue aesthetic. Airlock is a modern operator palette built using the same semantic-role logic rather than a historical literal. The Default Dark and Light themes apply M3's semantic-role architecture to the 256-color palette. All palettes enforce Apple HIG's color independence rule. The historical progression from 2-color to 16-color to 256-color to truecolor is not treated as obsolescence — it is the graceful degradation path (§5.6) that every compliant application must support.

### Efficiency implications from KLM analysis

Monospace TUI should prioritize **keyboard-first design** based on the KLM evidence: keyboard shortcuts are **58% faster** than mouse menu navigation for practiced users, keyboard-only interfaces eliminate the **0.40-second homing penalty** per hand transition, and expert chunking reduces mental preparation overhead. The framework should support all six historical keyboard models (function-key, CUA, modal, prefix, fuzzy, context-panel) as composable layers rather than forcing a single paradigm.

### Accessibility as architectural constraint

Terminal accessibility research reveals that **reactive grid-based TUI rendering is fundamentally hostile to screen readers**. Monospace TUI should adopt a dual-rendering architecture: a visual renderer using ANSI escape sequences for sighted users, and a linear semantic renderer for screen readers that outputs structured, sequential text without cursor jumping. VT100 scrolling regions should replace full-screen redraws where possible. All interactive elements require text labels independent of visual position. Color must never be the sole information carrier — pair with bold/dim/underline attributes and text markers.

### The Monospace TUI design token vocabulary

Drawing from all seven research vectors, the core Monospace TUI token set emerges:

- **Grid:** 1 character = 1 unit; minimum 80×24, standard 120×40, responsive breakpoints at 40/80/120/160 columns
- **Spacing:** 0, 1, 2, 3, 4, 6, 8 character units (mapping M3's 0/4/8/12/16/24/32dp)
- **Borders:** Light single (─│┌┐└┘), heavy single (━┃┏┓┗┛), double (═║╔╗╚╝), rounded (╭╮╰╯), dashed (┄┈)
- **Elevation:** Level 0 (no border), Level 1 (single-line border), Level 2 (single + 2×1 shadow), Level 3 (double-line + shadow), Level 4 (double-line + shadow + scrim)
- **Color:** 5 semantic roles (primary, secondary, tertiary, error, neutral) × 13 tonal steps, mapped to 256-color with truecolor enhancement
- **Typography:** 4 levels — Display (bold + uppercase or double-width), Title (bold), Body (normal), Label (dim or small)
- **States:** Enabled (normal), Focused (reverse or bracket), Selected (reverse + marker), Disabled (dim), Error (red attribute)
- **Navigation keys:** F1=Help, F3/Esc=Exit/Cancel, F10/Alt=Menu, Tab/Shift+Tab=Next/Prev field, arrow keys=within-control, Enter=Confirm, Space=Toggle
- **Motion:** State transitions via immediate swap (0ms), fast feedback (50–100ms delayed redraw), standard transition (150–300ms progressive reveal), slow reveal (300–500ms panel slide)

This token vocabulary provides Monospace TUI with a principled foundation that honors the precision of CUA and Turbo Vision, adopts the systematic design thinking of Material Design 3 and Apple HIG, and leverages the full capability of modern terminal emulators — while keeping keyboard efficiency and accessibility as non-negotiable architectural constraints.
