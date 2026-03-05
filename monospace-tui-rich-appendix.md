# Monospace Design TUI Rich Appendix

**Version: ALPHA** — Section structure and mapping notes. Not yet a complete appendix.

**Package:** `mono-tui`

This document maps the [Monospace Design TUI Standard](monospace-tui-design-standard.md) to Python [Rich](https://rich.readthedocs.io/) for CLI output formatting. Rich is a **rendering library**, not a full TUI framework — it provides styled terminal output but no interactive event loop, focus management, or keyboard handling. Use this appendix for non-interactive or semi-interactive output (reports, dashboards, progress displays). For interactive applications, use the [Textual Appendix](monospace-tui-textual-appendix.md) instead.

**When to use Rich alone:**
- CLI tools that print formatted output (tables, trees, panels)
- Non-interactive dashboards using `Live` display
- Progress bars for long-running operations
- Log output with structured formatting
- Rendering layer inside a custom event loop (curses, blessed)

**When Rich is insufficient:**
- Any application requiring keyboard interaction beyond `Prompt.ask()`
- Focus management, modal dialogs, screen navigation
- Footer key strips, keyboard tiers, state model
- Full screen archetypes (Dashboard, Admin, File Manager, Editor, Fuzzy Finder)

---

## §TR1 Renderable Mapping

### §TR1.1 Component to Renderable Table

| Monospace TUI Component (Standard §4) | Rich Renderable | Import | Notes |
|----------------------------------------|-----------------|--------|-------|
| Data table | `Table` | `rich.table` | Sortable columns, row styles, box characters |
| Metric card | `Panel` + `Text` | `rich.panel`, `rich.text` | Panel with title for bordered display |
| Tree / hierarchy | `Tree` | `rich.tree` | Collapsible, styled branches |
| Progress bar | `Progress` | `rich.progress` | Multiple concurrent tasks, custom columns |
| Spinner | `Spinner` | `rich.spinner` | Inline or status context |
| Log viewer | `Console` with `log()` | `rich.console` | Timestamped structured output |
| Sparkline | Custom renderable | — | TODO: `__rich_console__` protocol implementation using Braille (§R6) |
| Status indicator | `Text` with markup | `rich.text` | `[green]OK[/]`, `[red]FAIL[/]` with symbol pairing |
| Syntax highlighting | `Syntax` | `rich.syntax` | Language-aware code rendering |
| Markdown | `Markdown` | `rich.markdown` | Rendered markdown content |

### §TR1.2 Missing Capabilities

| Monospace TUI Component | Status | Notes |
|--------------------------|--------|-------|
| Push button | N/A | No interactivity |
| Entry field | Limited | `Prompt.ask()` blocks for single-line input |
| Toggle / Checkbox | N/A | No interactivity |
| Radio group | N/A | No interactivity |
| List box (interactive) | N/A | No selection, no focus |
| Spin button | N/A | No interactivity |
| Footer key strip | N/A | No key binding system |
| Action bar / menus | N/A | No menu system |

---

## §TR2 Layout Mapping

### §TR2.1 Three-Region Layout via Rich Layout

TODO: Map Standard §1.3 to `rich.layout.Layout` with `split_row()` and `split_column()`.

```python
from rich.layout import Layout
from rich.panel import Panel

layout = Layout()
layout.split_row(
    Layout(name="nav", minimum_size=8, ratio=1),      # Region A
    Layout(name="content", ratio=4),                    # Region B
    Layout(name="context", minimum_size=12, ratio=1),  # Region C
)
```

### §TR2.2 Responsive Adaptation

TODO: Manual terminal size detection and layout rebuilding.

```python
from rich.console import Console

console = Console()
width = console.width

if width < 80:
    # Compact: Region B only
    ...
elif width < 120:
    # Standard: A + B
    ...
else:
    # Expanded: A + B + C
    ...
```

---

## §TR3 Color and Styling

### §TR3.1 Semantic Color Theme

TODO: Map Standard §5.1 semantic roles to Rich `Theme`.

```python
from rich.theme import Theme
from rich.console import Console

mono_tui_theme = Theme({
    "primary": "bold #5fafff",
    "secondary": "#87afaf",
    "tertiary": "#5fd7af",
    "error": "bold red",
    "success": "green",
    "warning": "yellow",
    "disabled": "dim",
    "focused": "reverse",
})

console = Console(theme=mono_tui_theme)
```

### §TR3.2 Color Capability Detection

TODO: Rich auto-detects color capability via `COLORTERM` and `TERM` — aligns with Standard §5.6 and Rendering Reference §R7.

### §TR3.3 Status Colors

TODO: Map Standard §5.2 status colors with color independence (pair color with symbol).

---

## §TR4 Elevation via Panel Borders

TODO: Map Standard §6.1 elevation levels to Rich `Panel` box styles.

| Elevation | Rich Box Style | Import |
|-----------|---------------|--------|
| Level 0 | No panel | — |
| Level 1 | `box.SIMPLE` or `box.ROUNDED` | `rich.box` |
| Level 2 | `box.SQUARE` + shadow (custom) | `rich.box` |
| Level 3 | `box.DOUBLE` | `rich.box` |
| Level 4 | `box.DOUBLE` + scrim (not supported) | `rich.box` |

---

## §TR5 Typography Mapping

TODO: Map Standard §7.1 to Rich markup/styles.

| Treatment | Rich Style |
|-----------|-----------|
| Display | `bold` + uppercase in source |
| Title | `bold` |
| Body | (default) |
| Label | `dim` |

---

## §TR6 Live Display for Dashboards

TODO: Map Monitor-Respond workflow (§12.3) to `rich.live.Live`.

```python
from rich.live import Live
from rich.table import Table
import time

def generate_table() -> Table:
    # Build fresh table with current data
    ...

with Live(generate_table(), refresh_per_second=4) as live:
    while True:
        time.sleep(0.25)
        live.update(generate_table())
```

### §TR6.1 Progress Bars

TODO: Map Pipeline workflow (§12.6) execution stage to `rich.progress.Progress`.

---

## §TR7 Compliance Limitations

Rich alone cannot satisfy the following Standard requirements:

| Standard Rule | Status | Reason |
|---------------|--------|--------|
| §1.4 Footer key strip | Cannot comply | No key binding system |
| §2.1 Keyboard-first interaction | Cannot comply | No interactive event loop |
| §2.2 Standard key assignments | Cannot comply | No key handling |
| §8.1 Required states (focus, hover, pressed) | Cannot comply | No state model |
| §8.2 Focus invariant | Cannot comply | No focus system |
| §9.1 Dual-rendering architecture | Partial | Rich renders text-mode output, but no screen reader integration |
| §10.2 Long-operation feedback | Can comply | `Progress` and `Spinner` |
| §11 Screen archetypes | Cannot comply | No interactive screens |
| §12 Workflow archetypes | Cannot comply | No screen navigation |

**Recommendation:** Use Rich for rendering within a framework (Textual, curses) or for non-interactive CLI output. Do not attempt to build a compliant interactive TUI with Rich alone.
