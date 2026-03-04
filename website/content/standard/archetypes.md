---
title: "§11 Archetypes"
description: "Dashboard, Admin, File Manager, Editor, Fuzzy Finder archetypes plus appendices"
weight: 11
---

An archetype defines a reusable screen pattern with a specific layout, keyboard layer, and component set. Applications MUST select one archetype per screen and adhere to its rules. Applications MAY combine archetypes across screens (e.g., a Dashboard screen and an Admin screen in the same application).

All archetypes inherit the CUA base keyboard ([§2.2](/standard/keyboard/#22-standard-key-assignments)), three-region layout ([§1.3](/standard/layout/#13-three-region-layout)), and footer key strip ([§1.4](/standard/layout/#14-footer-key-strip)).

## §11.1 Dashboard

**Purpose:** Real-time monitoring and status overview (htop, btop, system dashboards).

**Layout:**

```
╔══ Dashboard Title ══════════════════════════════╗
║ ▲ Metric A: 1,234  │ ◉ Status B  │ ⚠ Warns: 3  ║
╠═════════════════════════════════════════════════╣
║ Column 1    │ Column 2 │ Column 3 │ Column 4    ║
║ row data    │ ◉ OK     │  120ms   │ 0           ║
║ row data    │ ⚠ SLOW   │  890ms   │ 2           ║
║ row data    │ ◉ OK     │   45ms   │ 0           ║
╠═════════════════════════════════════════════════╣
║ ?Help  r Refresh  /Filter  s Sort  q Quit       ║
╚═════════════════════════════════════════════════╝
```

**Structure:**

| Area | Rows | Content |
|------|------|---------|
| Header metrics | 1–3 | Metric cards with status indicators |
| Data area | Flex | Scrollable data table or panel grid |
| Footer | 1–2 | Key strip |

**Keyboard (inherits all Tier 1; uses Tier 2 `s`, `/` from standard):**

| Key | Action | Tier |
|-----|--------|------|
| `?` | Help | Tier 1 (common key for F1) |
| `r` | Refresh | Tier 1 (common key for F5) |
| `/` | Activate filter input | Tier 1 |
| `s` | Cycle sort order (asc/desc) | Tier 2 |
| `q` | Quit | Tier 1 |
| Number keys (1–9) | Sort by column N | Archetype-specific |

**Key components:** Metric cards, data table, sparklines, status indicators.

**Example workflow — filter and sort a dashboard table:**

| Step | Key | Action | KLM |
|------|-----|--------|-----|
| 1 | `/` | Open filter | K = 0.28s |
| 2 | Type query | Filter text | M + nK |
| 3 | Enter | Apply filter | K = 0.28s |
| 4 | `s` | Sort focused column | K = 0.28s |
| Total | | 4 keystrokes + query | ~2.2s + typing |

## §11.2 Admin / Config

**Purpose:** Application configuration and settings management (setup wizards, settings panels).

**Layout:**

```
┌─ Categories ─┬── General Settings ──────────────┐
│               │                                  │
│ ▸ General     │  Application Name                │
│   Network     │  [ My App_____________ ]         │
│   Security    │                                  │
│   Advanced    │  Log Level                       │
│               │  (*) Info                        │
│               │  ( ) Debug                       │
│               │  ( ) Error                       │
│               │                                  │
│               │  Enable Caching                  │
│               │  [X] Enabled                     │
│               │                                  │
│               │  < Save >   < Cancel >           │
├───────────────┴──────────────────────────────────┤
│ F1 Help  Tab Next  Esc Cancel  Enter Save        │
└──────────────────────────────────────────────────┘
```

**Structure:**

| Area | Position | Content |
|------|----------|---------|
| Region A — Sidebar | Left, 8–16 cols | Category list |
| Region B — Form | Center, flex | Tabbed or sectioned form fields |
| Footer | Bottom, 1–2 rows | Key strip |

**Keyboard (inherits all Tier 1):**

| Key | Action | Tier |
|-----|--------|------|
| `?` | Help | Tier 1 |
| Esc | Back / cancel edit | Tier 1 |
| Ctrl+S | Save | Archetype |
| Number keys (1–9) | Jump to sidebar item N | Archetype |
| `[` / `]` | Previous / next settings tab | Archetype |

Note: Single-letter Tier 2 keys (`d`, `e`, `a`) are suppressed in the Admin archetype because form fields dominate the screen. Use Ctrl+ modified keys or buttons instead.

**Key components:** Entry fields, toggles/switches, radio groups, push buttons, tabbed content.

## §11.3 File Manager

**Purpose:** File system navigation and operations (Norton Commander, ranger, Midnight Commander).

**Layout (dual-pane):**

```
┌── /home/user ────────────┬── /home/user/docs ───────┐
│ ..                       │ ..                        │
│ ▸ documents/             │   report.pdf         12K  │
│   downloads/             │   notes.txt           2K  │
│   projects/              │   slides.pptx        45K  │
│   .bashrc            1K  │                           │
│   .gitconfig         2K  │                           │
├──────────────────────────┴───────────────────────────┤
│ user@host:~$                                         │
├──────────────────────────────────────────────────────┤
│ F3 View  F4 Edit  F5 Copy  F6 Move  F7 Mkdir  F8 Del│
└──────────────────────────────────────────────────────┘
```

**Structure:**

| Area | Position | Content |
|------|----------|---------|
| Left panel | Left, 50% | Directory listing with highlight bar |
| Right panel | Right, 50% | Directory listing or preview |
| Command line | 1 row above footer | Shell command input |
| Footer | Bottom, 1–2 rows | F-key operations |

**Keyboard (inherits Tier 1 with overrides per [§2.7](/standard/keyboard/#27-archetype-key-overrides); uses context-panel layer [§2.6](/standard/keyboard/#26-composable-keyboard-layers)):**

| Key | Action | Tier |
|-----|--------|------|
| Tab | Switch active panel | Archetype (context-panel layer [§2.6](/standard/keyboard/#26-composable-keyboard-layers)) |
| Space or Insert | Select/deselect file | Tier 1 toggle + Norton convention |
| `/` | Filter file list | Tier 1 |
| `y` | Copy (yank) selected to other panel | Tier 2 |
| `d` | Delete selected (MUST confirm) | Tier 2 |
| `a` | Create directory | Tier 2 |
| `e` | Edit file | Tier 2 |
| `g` `g` / `G` | Top / bottom of list | Tier 1 scrolling |
| F3 | View file | Archetype (overrides §2.2) |
| F4 | Edit file (alias for `e`) | Archetype (Norton convention) |
| F5 | Copy to other panel (alias for `y`) | Archetype (overrides §2.2) |
| F6 | Move/rename selected | Archetype (Norton convention) |
| F7 | Create directory (alias for `a`) | Archetype (Norton convention) |
| F8 | Delete selected (alias for `d`) | Archetype (Norton convention) |
| Esc | Back / Cancel | Tier 1 (replaces F3) |
| Ctrl+R | Refresh | Archetype (replaces F5/`r`) |

**Key components:** File list with columns (name, size, date), path breadcrumb, selection markers.

(Norton Commander §7, OFM paradigm, [§2.7](/standard/keyboard/#27-archetype-key-overrides) archetype key overrides)

## §11.4 Editor

**Purpose:** Text editing and document manipulation (Vim, Turbo Vision editor, nano).

**Layout:**

```
┌── filename.py ───────────────────── ln 42, col 8 ─┐
│  1 │ def calculate(x, y):                          │
│  2 │     result = x + y                            │
│  3 │     return result                             │
│  4 │                                               │
│  5 │ # TODO: add error handling                    │
│    │                                               │
├────┴───────────────────────────────────────────────┤
│ -- INSERT --                  UTF-8  LF  Python    │
├────────────────────────────────────────────────────┤
│ F1 Help  F2 Save  F3 Close  ^G Goto  ^F Find      │
└────────────────────────────────────────────────────┘
```

**Structure:**

| Area | Position | Content |
|------|----------|---------|
| Document area | Flex | Text buffer with optional line numbers |
| Status line | 1 row | Filename, cursor position, encoding, mode |
| Footer | 1–2 rows | Key strip |

**Keyboard (text input dominates — single-letter Tier 1/2 keys are suppressed by default):**

| Key | Action | Tier |
|-----|--------|------|
| Ctrl+S or F2 | Save | Archetype |
| Ctrl+F or `/` | Find (`/` only in normal mode) | Tier 1 (`/`) + Archetype (Ctrl+F) |
| Ctrl+G | Go to line | Archetype |
| `?` or F1 | Help (`?` only in normal mode) | Tier 1 |

The Editor archetype MAY add a modal keyboard layer ([§2.6](/standard/keyboard/#26-composable-keyboard-layers)) for vi-style normal/insert/command modes. When a modal layer is active, Tier 1/2 single-letter keys (`q`, `r`, `d`, `e`, `a`, `s`, `g`, `n`, `y`) MAY be rebound within the normal-mode layer. If modal layers are used:

- The current mode MUST be displayed in the status line.
- Esc MUST return to normal/command mode.

**Key components:** Text buffer, line numbers, status bar, optional syntax highlighting.

## §11.5 Fuzzy Finder

**Purpose:** Rapid search and selection from large item sets (fzf, telescope, command palettes).

**Layout:**

```
┌── Find File ─────────────────────────────────────┐
│ > search query█                                  │
├──────────────────────────────────────────────────┤
│ ▸ src/utils/helpers.py              [92% match]  │
│   src/utils/http.py                 [87% match]  │
│   src/core/handler.py               [71% match]  │
│   tests/test_helpers.py             [65% match]  │
│                                                  │
│                                     4 / 128      │
├──────────────────────────────────────────────────┤
│ Enter Select  Esc Cancel  ↑↓ Navigate            │
└──────────────────────────────────────────────────┘
```

**Structure:**

| Area | Position | Content |
|------|----------|---------|
| Filter input | Top, 1 row | Text entry with type-to-filter |
| Results | Flex | Ranked result list with match scores |
| Preview | Optional, right split | Preview of focused result |
| Footer | 1 row | Key strip |

**Keyboard (fuzzy layer [§2.6](/standard/keyboard/#26-composable-keyboard-layers) — all printable input goes to filter):**

| Key | Action | Tier |
|-----|--------|------|
| Any printable character | Appends to filter | Fuzzy layer ([§2.6](/standard/keyboard/#26-composable-keyboard-layers)) |
| Ctrl+N or Arrow Down | Next result | Archetype |
| Ctrl+P or Arrow Up | Previous result | Archetype |
| Enter | Select focused result and close | Tier 1 |
| Esc | Cancel and close | Tier 1 |
| Ctrl+D / Ctrl+U | Half-page down / up in results | Tier 1 scrolling |

Tier 1/2 single-letter keys (`q`, `r`, `/`, `d`, etc.) are captured by the filter input. Only Esc, Enter, and Ctrl+ modified keys remain functional. CUA navigation keys (Tab, F-keys) are suspended while the fuzzy layer is active.

**Key components:** Search input, scored result list, match highlighting, optional preview pane.

---

## Appendix A: Rule Index

For auditing convenience, every section's prescriptive rules are summarized:

| Section | Rule Count | Key MUST Rules |
|---------|-----------|---------------|
| [§1 Grid & Layout](/standard/layout/) | 6 | Three-region layout, footer always visible, 80×24 minimum, SIGWINCH handling |
| [§2 Keyboard](/standard/keyboard/) | 7 | CUA primary, 3-tier key system (F-key + common key duals), case-insensitivity, footer discoverability, key scope rules, composable layers, archetype overrides |
| [§3 Navigation](/standard/navigation/) | 5 | Decision tree, 3-level menu max, unavailable items visible, ellipsis convention |
| [§4 Components](/standard/components/) | 4 | Widget selection table, one default button, tab order, entry field fill characters |
| [§5 Color](/standard/color/) | 6 | 5 semantic roles, 4 status colors, color independence, capability detection |
| [§6 Borders](/standard/borders/) | 6 | 5 elevation levels, active/inactive distinction, shadow rendering, scrim for modals |
| [§7 Typography](/standard/typography/) | 3 | 4 treatments only, reverse video for focus, error text requirements |
| [§8 State Model](/standard/state/) | 3 | 6 mandatory + 1 conditional state, focus invariant, disabled visibility |
| [§9 Accessibility](/standard/accessibility/) | 6 | Dual rendering, scrolling regions, text labels, contrast ratios, focus visibility |
| [§10 Motion](/standard/motion/) | 3 | 4 timing tiers, long-operation feedback, capability degradation |
| §11 Archetypes | 5 | Dashboard, Admin, File Manager, Editor, Fuzzy Finder |

---

## Appendix B: Glossary

| Term | Definition |
|------|-----------|
| Character cell | The atomic rendering unit: 1 column × 1 row in a monospace terminal grid |
| CUA | IBM Common User Access — the base keyboard and interaction standard |
| Elevation | Visual layering depth, expressed as Level 0–4 |
| Footer key strip | The bottom 1–2 rows showing available keyboard actions |
| Mnemonic | An underlined letter in a menu or label enabling single-keystroke selection |
| Region | One of three layout areas (A=Navigation, B=Content, C=Context) |
| Scrim | A dim overlay applied to background content behind a modal |
| SGR | Select Graphic Rendition — ANSI escape codes for text styling |
| Monospace TUI | Monospace Design TUI — the design system defined by this standard (package: `mono-tui`) |
