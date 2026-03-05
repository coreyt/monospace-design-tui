---
title: "Examples"
subtitle: "The design standard in action"
description: "ASCII screenshots showing Monospace Design TUI archetypes applied to real interface patterns"
---

These examples demonstrate how the Monospace Design TUI standard looks when applied. Each screenshot follows the standard's rules for layout (§1), keyboard (§2), navigation (§3), components (§4), color roles (§5), borders (§6), typography (§7), and state (§8).

All examples are shown at the Standard breakpoint (120 columns).

---

## Dashboard — System Monitor

Archetype §11.1. Header metrics with status indicators, sortable data table, footer key strip. Note the three-region layout (§1.3) with Region B filling all space, and semantic status colors paired with symbols (§5.3).

```
┌── System Monitor ─────────────────────────────────────────────────────────────────────────────────┐
│ File  View  Options  Help                                                                         │
├───────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                   │
│  ▲ CPU: 34%          ◉ Services: 12/12 healthy          ⚠ Alerts: 3          ▲ Memory: 61%       │
│                                                                                                   │
├───────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Service              │ Status     │ Uptime       │ CPU     │ Memory  │ Requests/s  │ Errors (24h) │
│──────────────────────│────────────│──────────────│─────────│─────────│─────────────│──────────────│
│ ▸ api-gateway        │ ◉ OK       │ 14d  3h 22m  │   2.1%  │  340MB  │       1,234 │            0 │
│   auth-service       │ ◉ OK       │ 14d  3h 22m  │   0.8%  │  128MB  │         892 │            0 │
│   worker-pool        │ ⚠ DEGRADED │  0d  1h 45m  │  78.3%  │  1.2GB  │         456 │           12 │
│   cache-redis        │ ◉ OK       │ 14d  3h 22m  │   0.3%  │  2.1GB  │      14,562 │            0 │
│   db-primary         │ ◉ OK       │ 30d  8h 11m  │   5.6%  │  4.8GB  │       3,421 │            0 │
│   db-replica-01      │ ◉ OK       │ 30d  8h 11m  │   3.2%  │  4.1GB  │       2,198 │            0 │
│   scheduler          │ ◉ OK       │  7d 12h 05m  │   0.1%  │   64MB  │          18 │            0 │
│   notification-svc   │ ✗ DOWN     │  0d  0h 00m  │   0.0%  │    0MB  │           0 │          847 │
│   metrics-collector  │ ◉ OK       │ 14d  3h 22m  │   1.4%  │  256MB  │       8,921 │            0 │
│   log-aggregator     │ ⚠ SLOW     │ 14d  3h 22m  │  12.7%  │  890MB  │       5,678 │            3 │
│   cdn-origin         │ ◉ OK       │ 60d  2h 19m  │   0.9%  │  512MB  │      22,456 │            0 │
│   backup-agent       │ ◉ OK       │  3d  6h 40m  │   0.2%  │   96MB  │           1 │            0 │
│                                                                                                   │
├───────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ?Help  r Refresh  /Filter  s Sort  d Details  q Quit                             12 services ↓   │
└───────────────────────────────────────────────────────────────────────────────────────────────────┘
```

**Standards applied:** Three-region layout (§1.3) — Region B only, no sidebar needed. Footer key strip (§1.4) with Tier 1 keys (`?`, `r`, `/`, `q`) and Tier 2 keys (`s`, `d`). Metric cards in header (§R4.7). Data table with sort indicators (§R4.6). Color independence (§5.3) — every status has a symbol (`◉`, `⚠`, `✗`) and text label. Focus indicator `▸` on current row (§8.1).

---

## Admin — Application Settings

Archetype §11.2. Sidebar category navigation (Region A), form fields in Region B, footer key strip. Demonstrates the widget selection table (§4.1): radio groups for exclusive choice, toggles for booleans, entry fields for free text.

```
┌── Settings ───────────────────────────────────────────────────────────────────────────────────────┐
│ File  Edit  Options  Help                                                                         │
├─ Categories ──┬── Network Settings ───────────────────────────────────────────────────────────────┤
│               │                                                                                   │
│ ▸ General     │  API Endpoint                                                                     │
│   Network     │  [ https://api.example.com__________ ]                                            │
│   Security    │                                                                                   │
│   Logging     │  Connection Timeout (seconds)                                                     │
│   Advanced    │  [ 30______ ]                                                                     │
│               │                                                                                   │
│               │  Retry Strategy                                                                   │
│               │  (*) Exponential backoff                                                          │
│               │  ( ) Linear retry                                                                 │
│               │  ( ) No retry                                                                     │
│               │                                                                                   │
│               │  Max Retries                                                                      │
│               │  < 3 >                                                                            │
│               │                                                                                   │
│               │  TLS Verification                                                                 │
│               │  [X] Verify server certificates                                                   │
│               │  [X] Send client certificate                                                      │
│               │                                                                                   │
│               │                                                                                   │
│               │         < Save >   < Cancel >                                                     │
│               │                                                                                   │
├───────────────┴───────────────────────────────────────────────────────────────────────────────────┤
│ F1 Help  Tab Next field  Esc Cancel  Enter Save  [ / ] Prev/Next category                        │
└───────────────────────────────────────────────────────────────────────────────────────────────────┘
```

**Standards applied:** Three-region layout (§1.3) — Region A (sidebar, 16 cols) + Region B (form, flex). Widget selection (§4.1) — entry fields for free text, radio group for exclusive choice with 3 options, spin button for bounded numeric, checkboxes for booleans. Entry field fill characters (§4.4) — underscores show available width. Default button (§4.2) — `< Save >` is the default. Tab order (§4.3) follows top-to-bottom within the form.

---

## File Manager — Dual Pane

Archetype §11.3. Norton Commander / Midnight Commander paradigm. Dual symmetric panels, command line, F-key footer. Demonstrates archetype key overrides (§2.7) where F3=View and F5=Copy instead of their standard CUA assignments.

```
┌── /home/user/projects ────────────────────┬── /home/user/projects/mono-tui ────────────────────┐
│ Name                          Size   Date  │ Name                          Size   Date          │
│────────────────────────────────────────────│─────────────────────────────────────────────────────│
│ ..                               ─   ─     │ ..                               ─   ─             │
│ ▸ mono-tui/                      ─   Mar 3 │   monospace-tui-design-standard.md   24K  Mar 3         │
│   airlock/                       ─   Feb 8 │   mono-tui-rendering-reference   19K  Mar 3        │
│   dotfiles/                      ─   Jan 2 │   monospace-tui-textual-appendix.md  21K  Mar 3         │
│   scripts/                       ─   Feb 1 │   monospace-design-tui-research.md                   11K  Mar 3         │
│   .bashrc                       2K   Jan 5 │   TUI-DESIGN.template.md         5K  Mar 3         │
│   .gitconfig                    1K   Jan 5 │   LICENSE                        1K  Mar 3         │
│   notes.txt                     4K   Feb 28│   logo.txt                       1K  Mar 3         │
│                                            │   skills/                        ─   Mar 3         │
│                                            │   website/                       ─   Mar 3         │
│                                            │                                                    │
│                                            │                                                    │
│                                            │                                                    │
│                                            │                                                    │
│                                            │                                                    │
│                                            │                                                    │
├────────────────────────────────────────────┴────────────────────────────────────────────────────┤
│ user@host:~/projects$                                                                           │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ F3 View  F4 Edit  F5 Copy  F6 Move  F7 Mkdir  F8 Delete  F9 Menu  F10 Quit                     │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

**Standards applied:** Dual-pane layout (§11.3) — two equal panels with Tab to switch. Archetype key overrides (§2.7) — F3=View and F5=Copy override standard CUA assignments; Esc serves as Back/Cancel, Ctrl+R as Refresh. Command line between panels and footer (Norton convention). F-key footer (§1.4). File listing with highlight bar `▸` for focus (§8.1). Directories shown with `/` suffix.

---

## Editor — Code Editing

Archetype §11.4. Text buffer with line numbers, status line showing mode and file info, minimal footer. Demonstrates the modal keyboard layer (§2.6) — the status line shows `-- INSERT --` to indicate the current mode.

```
┌── src/dashboard.py ──────────────────────────────────────────────── ln 24, col 17 ────────────────┐
│    1 │ """Monospace TUI-compliant Dashboard — Standard §11.1."""                                   │
│    2 │                                                                                             │
│    3 │ from textual.app import App, ComposeResult                                                  │
│    4 │ from textual.binding import Binding                                                         │
│    5 │ from textual.containers import Horizontal, Vertical                                         │
│    6 │ from textual.widgets import (                                                               │
│    7 │     DataTable,                                                                              │
│    8 │     Footer,                                                                                 │
│    9 │     Header,                                                                                 │
│   10 │     Input,                                                                                  │
│   11 │     Static,                                                                                 │
│   12 │ )                                                                                           │
│   13 │ from textual.worker import work                                                             │
│   14 │                                                                                             │
│   15 │                                                                                             │
│   16 │ class MetricCard(Static):                                                                   │
│   17 │     """A single metric display (Rendering Reference §R4.7)."""                              │
│   18 │                                                                                             │
│   19 │     DEFAULT_CSS = """                                                                       │
│   20 │     MetricCard {                                                                            │
│   21 │         width: 1fr;                                                                         │
│   22 │         height: 3;                                                                          │
│   23 │         content-align: center middle;                                                       │
│   24 │         text-style█ bold;                                                                   │
│   25 │         border: solid $secondary;                                                           │
│   26 │     }                                                                                       │
│   27 │     """                                                                                     │
│   28 │                                                                                             │
├──────┴─────────────────────────────────────────────────────────────────────────────────────────────┤
│ -- INSERT --                                              UTF-8  LF  Python  24/540               │
├────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ F1 Help  F2 Save  F3 Close  ^G Goto  ^F Find  Esc Normal mode                                    │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

**Standards applied:** Editor layout (§11.4) — document area with line numbers, status line, footer. Modal keyboard layer (§2.6) — `-- INSERT --` in status line indicates current mode; Esc returns to normal mode. Line numbers in Label typography (§7.1, dim). Cursor position shown in title bar. Status line shows encoding, line endings, language, and position. Footer shows modified key bindings (Ctrl+G, Ctrl+F) since single-letter keys go to the text buffer in insert mode.

---

## Fuzzy Finder — Command Palette

Archetype §11.5. Type-to-filter with ranked results, preview pane, minimal footer. Demonstrates the fuzzy keyboard layer (§2.6) where all printable input goes to the filter — only Esc, Enter, and Ctrl-modified keys remain functional.

```
╔══ Find File ══════════════════════════════════════════════════════════════════════════════════════╗
║ > dashboard█                                                                                     ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                              │                                   ║
║  ▸ src/tui/dashboard.py                     [94% match]      │   1 │ """Dashboard screen."""      ║
║    src/tui/dashboard_widgets.py             [87% match]      │   2 │                              ║
║    tests/test_dashboard.py                  [82% match]      │   3 │ from textual.app import App  ║
║    docs/dashboard-design.md                 [71% match]      │   4 │ from textual.widgets import  ║
║    src/models/dashboard_config.py           [68% match]      │   5 │     DataTable,               ║
║                                                              │   6 │     Footer,                  ║
║                                                              │   7 │     Header,                  ║
║                                                              │   8 │     Static,                  ║
║                                                              │   9 │                              ║
║                                                              │  10 │ class DashboardApp(App):     ║
║                                                              │  11 │     CSS = """                ║
║                                                              │  12 │     Screen {                 ║
║                                                              │                                   ║
║                                                       5/128  │                                   ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════╣
║ Enter Select  Esc Cancel  ↑↓ Navigate  ^P/^N Prev/Next  ^D Half-page down                       ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════╝
```

**Standards applied:** Fuzzy finder layout (§11.5) — filter input at top, ranked results, optional preview pane. Level 4 elevation (§6.1) — double-line borders for modal overlay. Fuzzy keyboard layer (§2.6) — all printable characters go to filter input. Results show match scores. Preview pane shows file contents for focused result. Counter `5/128` shows filtered vs. total results. Footer shows only keys active during fuzzy mode.

---

## Dialog — Confirm Delete

Elevation Level 4 modal (§6.1) with double-line borders, scrim behind, and severity-appropriate styling. Demonstrates dialog measurements (§R4.8), the default button convention (§4.2), and shadow rendering (§6.4).

```
┌── File Manager ─────────────────────────────────────────────────────────────────────┐
│                                                                                     │
│   documents/                                                                        │
│   downloads/                            ╔══ Confirm Delete ══════════════════╗       │
│   projects/                             ║                                    ║░░     │
│   .bashrc           1K                  ║  Are you sure you want to delete   ║░░     │
│   .gitconfig        2K                  ║  "old-backup.tar.gz" (2.4GB)?      ║░░     │
│                                         ║                                    ║░░     │
│                                         ║  ✗ This action cannot be undone.   ║░░     │
│                                         ║                                    ║░░     │
│                                         ║       » Delete «   < Cancel >      ║░░     │
│                                         ║                                    ║░░     │
│                                         ╚════════════════════════════════════╝░░     │
│                                           ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     │
│                                                                                     │
├─────────────────────────────────────────────────────────────────────────────────────┤
│ Enter Confirm  Esc Cancel                                                           │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

**Standards applied:** Level 4 modal overlay (§6.1) — double-line borders. Shadow rendering (§6.4) — 2-column × 1-row offset with `░` showing dimmed background. Scrim (§6.5) — background content behind modal is dimmed. Default button (§4.2) — `» Delete «` uses distinct delimiters. Dialog severity (§5.4) — destructive action with `✗` symbol and warning text, not relying on color alone (§5.3). Dialog measurements (§R4.8) — centered, padded, within 30–72 col width range.
