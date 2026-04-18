# Monospace Design TUI Textual Appendix

**Version 0.2.5** — Mapping Monospace Design TUI Standard rules to Python Textual framework.

**Package:** `mono-tui`

### Changelog

| Version | Date | Changes |
|---------|------|---------|
| 0.2.5 | 2026-04-18 | Synced appendix framing and agent-facing expectations with the v0.2.5 Mono documentation set. |
| 0.1.2 | 2026-04-17 | Synced appendix expectations with standard v0.1.2 keyboard/help/navigation guidance. |
| 0.1.1 | 2026-03-05 | Added §T8 Workflow Archetype Patterns (wizard, CRUD, monitor-respond, drill-down, configuration, review-approve). Renumbered §T8 Command Palette to §T9. |
| 0.1.0 | — | Initial release |

This document maps the framework-agnostic [Monospace Design TUI Standard](monospace-tui-design-standard.md) to concrete [Textual](https://textual.textualize.io/) widgets, TCSS patterns, and code conventions. It assumes familiarity with the standard and the [Rendering Reference](monospace-tui-rendering-reference.md).

---

## §T1 Widget Mapping

### §T1.1 Component → Widget Table

| Monospace TUI Component (Standard §4) | Textual Widget | Import Path | Notes |
|------------------------------|---------------|-------------|-------|
| Toggle / Switch `[X]`/`[ ]` | `Switch` | `textual.widgets.Switch` | Space to toggle; `value` property |
| Checkbox `[X]`/`[ ]` | `Checkbox` | `textual.widgets.Checkbox` | Use for multi-select; `value` property |
| Radio group `(*)`/`( )` | `RadioSet` + `RadioButton` | `textual.widgets.RadioSet` | Arrow keys within group |
| Entry field | `Input` | `textual.widgets.Input` | `placeholder`, `password`, `validators` |
| Push button `< OK >` | `Button` | `textual.widgets.Button` | `variant` for default: `"primary"` |
| List box | `ListView` + `ListItem` | `textual.widgets.ListView` | For 6–25 items |
| Select (dropdown) | `Select` | `textual.widgets.Select` | Alternative to ListView |
| Data table | `DataTable` | `textual.widgets.DataTable` | Sortable columns, cursor modes |
| Spin button | `Input` with validators | `textual.widgets.Input` | Custom up/down key bindings |
| Action bar | `Header` | `textual.widgets.Header` | Application header with title |
| Footer key strip | `Footer` | `textual.widgets.Footer` | Auto-populates from `BINDINGS` |
| Metric card | `Static` or `Label` | `textual.widgets.Static` | Custom widget recommended |
| Sparkline | `Sparkline` | `textual.widgets.Sparkline` | Built-in Braille rendering |
| Log viewer | `RichLog` | `textual.widgets.RichLog` | Streaming text output |
| Tabs | `TabbedContent` + `TabPane` | `textual.widgets.TabbedContent` | Parallel context switching |
| Progress bar | `ProgressBar` | `textual.widgets.ProgressBar` | With label |
| Tree navigation | `Tree` | `textual.widgets.Tree` | Hierarchical sidebar |

### §T1.2 Missing Widgets

These Monospace TUI components have no direct Textual equivalent and require custom widgets:

| Monospace TUI Component | Custom Implementation Strategy |
|---------------|-------------------------------|
| Spin button | Subclass `Input`; override `key_up`/`key_down` to cycle values |
| Dialog severity backgrounds | Use `ModalScreen` with TCSS class for severity level |
| Status indicator (`◉`/`○`) | `Static` widget with reactive `status` attribute |
| Menu bar with pull-downs | Use Textual's `Header` + command palette, or custom `MenuBar` widget |

---

## §T2 TCSS Patterns

### §T2.1 Elevation System

Maps Standard §6.1 elevation levels to Textual CSS:

```css
/* Level 0 — Inline content */
.elevation-0 {
    border: none;
}

/* Level 1 — Panels, content regions */
.elevation-1 {
    border: solid $secondary;
}

/* Level 2 — Menus, dropdowns (single-line border + shadow not native;
   approximate with Textual's border + offset) */
.elevation-2 {
    border: solid $secondary;
    /* Textual does not support character-cell shadows natively.
       Use a custom render or overlay technique. */
}

/* Level 3 — Dialogs (double-line border) */
.elevation-3 {
    border: double $primary;
}

/* Level 4 — Modal overlays (double-line + scrim) */
.elevation-4 {
    border: double $primary;
    /* Scrim handled by ModalScreen's built-in overlay */
}
```

### §T2.2 Color System

Maps Standard §5.1 semantic roles to Textual design variables:

```css
/* Define in your app's CSS or a shared stylesheet */
$primary: #5fafff;          /* 256-color: index 75 */
$primary-bg: #00005f;       /* 256-color: index 17 */
$secondary: #87afaf;        /* 256-color: index 109 */
$secondary-bg: #303030;     /* 256-color: index 236 */
$tertiary: #5fd7af;         /* 256-color: index 79 */
$error: #ff0000;            /* 256-color: index 196 */
$error-bg: #5f0000;         /* 256-color: index 52 */

$success: #00d700;          /* 256-color: index 40 */
$warning: #ffd700;          /* 256-color: index 220 */
$inactive: #585858;         /* 256-color: index 240 */

$surface: #1c1c1c;          /* 256-color: index 234 */
$surface-light: #262626;    /* 256-color: index 235 */
$text: #d0d0d0;             /* 256-color: index 252 */
```

### §T2.3 Typography

Maps Standard §7.1 to TCSS text styling:

```css
/* Display — screen titles, hero metrics */
.typography-display {
    text-style: bold;
    /* Apply UPPERCASE in Python source, not CSS */
}

/* Title — section headers, panel titles */
.typography-title {
    text-style: bold;
}

/* Body — content text (default, no special CSS needed) */
.typography-body {
    text-style: none;
}

/* Label — secondary info, placeholders (Standard §7.1: SGR 2 dim) */
.typography-label {
    text-style: dim;
}
```

### §T2.4 State Rendering

Maps Standard §8.1 to Textual focus/hover/disabled patterns:

```css
/* Focused state — reverse video */
*:focus {
    text-style: reverse;
}

/* Focused within a container (e.g., focused panel) */
*:focus-within {
    border: double $primary;
}

/* Disabled state */
*:disabled {
    opacity: 50%;
    /* Textual uses opacity; maps to dim appearance */
}

/* Hover state (mouse) */
*:hover {
    text-style: underline;
}
```

### §T2.5 Three-Region Layout

Maps Standard §1.3 to TCSS grid:

```css
/* Standard layout: Navigation | Content | Context */
Screen {
    layout: grid;
    grid-size: 3 1;
    grid-columns: auto 1fr auto;
    grid-rows: 1fr;
}

/* Region A — Navigation sidebar */
.region-nav {
    width: 16;
    min-width: 8;
    max-width: 20;
    dock: left;
}

/* Region B — Content (flex, fills remaining) */
.region-content {
    /* Inherits 1fr from grid */
}

/* Region C — Context panel */
.region-context {
    width: 30;
    dock: right;
}

/* Compact breakpoint: collapse sidebar */
Screen.-compact .region-nav {
    display: none;
}

Screen.-compact .region-context {
    display: none;
}
```

### §T2.6 Dialog Severity

Maps Standard §5.4:

```css
/* Notification dialog (neutral) */
.dialog-info {
    border: double $secondary;
    background: $surface;
}

/* Warning dialog */
.dialog-warning {
    border: double $warning;
    background: #3a3000;
}

/* Critical dialog */
.dialog-critical {
    border: double $error;
    background: $error-bg;
}
```

### §T2.7 Active / Inactive Window Distinction

Maps Standard §5.5 and §6.2:

```css
/* Active panel — bright border */
.panel:focus-within {
    border: double $primary;
}

/* Inactive panel — dim border */
.panel {
    border: solid $secondary;
}
```

---

## §T3 Async Rules

### §T3.1 Worker Decorator

All I/O operations MUST use the `@work` decorator or `run_worker()` to avoid blocking the main thread. This maps to Standard §10.2 (long-running operation feedback).

```python
from textual.worker import work

class MyScreen(Screen):

    @work(thread=True)
    async def check_health(self) -> None:
        """Never block the main thread with I/O."""
        self.query_one("#status", Static).update("Checking...")
        result = await some_api_call()
        self.query_one("#status", Static).update(f"Status: {result}")
```

### §T3.2 Rules

| Rule | Rationale (Standard reference) |
|------|-------------------------------|
| Use `@work(thread=True)` for blocking I/O (file, network) | §10.2 — never leave terminal hanging |
| Use `@work` (async) for non-blocking async operations | §10.2 — immediate feedback |
| Show spinner before starting worker | §10.2 — operations >100ms need feedback |
| Handle `Worker.cancelled` and `Worker.error` | §8.1 — Error state must show explanation |
| Never call `time.sleep()` on main thread | §10.2 — frozen UI violation |

---

## §T4 Navigation Mapping

### §T4.1 Pattern → Textual Implementation

Maps Standard §3.1 navigation topology:

| Monospace TUI Pattern | Textual Implementation | Method |
|-------------|----------------------|--------|
| Parallel contexts (tabs) | `TabbedContent` + `TabPane` | Static or dynamic tabs |
| Hierarchical drill-down (screens) | `Screen` subclass | `app.push_screen()` / `app.pop_screen()` |
| Transient confirmation (modal) | `ModalScreen` subclass | `app.push_screen(modal, callback)` |
| Contextual detail (panel) | Container widget (show/hide) | `widget.display = True/False` or CSS class toggle |

### §T4.2 Screen Stack

Textual's screen stack maps directly to Standard §3.1 hierarchical drill-down:

```python
# Push a new screen (drill-down)
self.app.push_screen(DetailScreen(item_id))

# Pop back (F3 / Esc)
self.app.pop_screen()

# Modal with callback (transient confirmation)
def on_confirm(result: bool) -> None:
    if result:
        self.delete_item()

self.app.push_screen(ConfirmDialog("Delete?"), on_confirm)
```

### §T4.3 Binding Declarations

Maps Standard §2.2 key assignments to Textual's `BINDINGS`:

```python
from textual.app import App
from textual.binding import Binding

class MonoTuiApp(App):
    BINDINGS = [
        # Tier 1 Global — CUA keys + common key duals (Standard §2.2)
        # F-key and common key both bound; footer shows the common key.
        Binding("f1", "help", "Help", show=False),
        Binding("question_mark", "help", "?Help"),             # ? shown in footer
        Binding("f3", "back", "Back", show=False),
        Binding("escape", "back", "Back"),                     # Esc shown in footer
        Binding("f5", "refresh", "Refresh", show=False),
        *ci("r", "refresh", "Refresh"),                        # r shown in footer
        Binding("f10", "toggle_menu", "Menu"),
        *ci("q", "quit", "Quit"),
        Binding("slash", "filter", "Filter"),                  # / search
        # Tab/Shift+Tab, Enter, Space, Arrow keys handled natively by Textual.
        # Ctrl+C/V/X/Z handled natively by Input widgets.

        # Tier 1 Scrolling
        # NOT using ci() — g/G is the sole case-sensitive exception (Standard §2.2)
        Binding("g", "scroll_top", "Top", show=False),         # gg (see key handler)
        Binding("G", "scroll_bottom", "Bottom", show=False),   # Shift+G = bottom
        Binding("n", "next_search_result", show=False),         # after / search
        Binding("N", "next_search_result", show=False),         # case-insensitive
        Binding("ctrl+d", "page_down", show=False),
        Binding("ctrl+u", "page_up", show=False),
    ]

    def action_back(self) -> None:
        """F3/Esc/? — always go back (Standard §2.2)."""
        if len(self.screen_stack) > 1:
            self.pop_screen()

    def action_help(self) -> None:
        """F1/? — context-sensitive help (Standard §2.2)."""
        self.push_screen(HelpScreen(context=self.focused))
```

**Case-insensitive binding helper** — Standard §2.2 requires all single-letter keys
to be case-insensitive (bind both cases, show only lowercase). Use a helper to
reduce boilerplate:

```python
def ci(key: str, action: str, description: str) -> list[Binding]:
    """Case-insensitive binding pair (Standard §2.2 case rule)."""
    return [
        Binding(key.lower(), action, description),
        Binding(key.upper(), action, description, show=False),
    ]
```

**Tier 3 screen mnemonics:**

```python
class MyApp(MonoTuiApp):
    BINDINGS = [
        *MonoTuiApp.BINDINGS,
        # Tier 3 — screen mnemonics (Standard §2.2)
        *ci("d", "switch_screen('dashboard')", "Dashboard"),
        *ci("c", "switch_screen('config')", "Config"),
        *ci("l", "switch_screen('logs')", "Logs"),
    ]
```

---

## §T5 Example: Dashboard Archetype

A minimal Textual application implementing Standard §11.1 (Dashboard).

```python
"""Monospace TUI-compliant Dashboard — Standard §11.1."""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import (
    DataTable,
    Footer,
    Header,
    Input,
    Static,
)
from textual.worker import work


class MetricCard(Static):
    """A single metric display (Rendering Reference §R4.7)."""

    DEFAULT_CSS = """
    MetricCard {
        width: 1fr;
        height: 3;
        content-align: center middle;
        text-style: bold;
        border: solid $secondary;
    }
    """


class DashboardApp(App):
    """Dashboard archetype (Standard §11.1).

    Layout:
        Header metrics (1-3 rows)
        Scrollable data table (flex)
        Footer key strip (1-2 rows)
    """

    CSS = """
    Screen {
        layout: vertical;
    }

    #metrics {
        height: 3;
        layout: horizontal;
    }

    #data-area {
        height: 1fr;
    }

    #filter-bar {
        height: 3;
        display: none;
    }

    #filter-bar.visible {
        display: block;
    }

    DataTable {
        height: 1fr;
    }
    """

    # Tier 1 global + common keys (Standard §2.2)
    BINDINGS = [
        # CUA key + common key duals
        Binding("f1", "help", "Help", show=False),
        Binding("question_mark", "help", "?Help"),
        Binding("escape", "back", "Back"),
        Binding("f5", "refresh", "Refresh", show=False),
        *ci("r", "refresh", "Refresh"),
        # Tier 1 global
        *ci("q", "quit", "Quit"),
        Binding("slash", "toggle_filter", "Filter", key_display="/"),
        # Tier 2
        *ci("s", "sort", "Sort"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()

        # Header metrics (Standard §11.1: 1-3 rows)
        with Horizontal(id="metrics"):
            yield MetricCard("▲ Requests: 1,234", id="metric-requests")
            yield MetricCard("◉ Healthy", id="metric-health")
            yield MetricCard("⚠ Warnings: 3", id="metric-warnings")

        # Filter bar (hidden by default)
        yield Input(placeholder="Type to filter...", id="filter-bar")

        # Data area (Standard §11.1: scrollable data table, flex)
        yield DataTable(id="data-area")

        # Footer key strip (Standard §1.4: always visible)
        yield Footer()

    def on_mount(self) -> None:
        """Populate table on mount."""
        table = self.query_one(DataTable)
        table.add_columns("Model", "Status", "Latency", "Errors")
        table.add_rows([
            ("claude-3-opus", "◉ OK", "120ms", "0"),
            ("claude-3-sonnet", "◉ OK", "85ms", "0"),
            ("gpt-4-turbo", "⚠ SLOW", "890ms", "2"),
            ("gpt-4o", "◉ OK", "45ms", "0"),
        ])
        # Start live refresh
        self.refresh_data()

    @work(thread=True, exclusive=True)
    async def refresh_data(self) -> None:
        """Refresh dashboard data (Standard §10.2: never leave hanging).

        Uses @work to avoid blocking main thread (§T3.1).
        """
        # In a real app, fetch from API/database here
        pass

    def action_back(self) -> None:
        """Esc — close filter or go back (Standard §2.2)."""
        filter_bar = self.query_one("#filter-bar")
        if filter_bar.has_class("visible"):
            filter_bar.remove_class("visible")
            self.query_one(DataTable).focus()
        elif len(self.screen_stack) > 1:
            self.pop_screen()

    def action_toggle_filter(self) -> None:
        """/ — toggle filter input (Standard §11.1)."""
        filter_bar = self.query_one("#filter-bar")
        if filter_bar.has_class("visible"):
            filter_bar.remove_class("visible")
            self.query_one(DataTable).focus()
        else:
            filter_bar.add_class("visible")
            filter_bar.focus()

    def action_refresh(self) -> None:
        """F5 — refresh data (Standard §2.2)."""
        self.query_one("#metric-requests", MetricCard).update(
            "▲ Refreshing..."
        )
        self.refresh_data()

    def action_help(self) -> None:
        """F1 — context-sensitive help (Standard §2.2)."""
        self.notify("Help: Use / to filter, F5 to refresh, q to quit.")


if __name__ == "__main__":
    app = DashboardApp()
    app.run()
```

### §T5.1 Compliance Checklist

| Standard Rule | Implementation |
|---------------|---------------|
| §1.4 Footer always visible | `Footer()` in `compose()` — Textual auto-docks to bottom |
| §2.2 Tier 1 keys | `BINDINGS` includes F1/?/Esc/F5/r/q// — CUA + common key duals |
| §2.3 Footer discoverability | Textual `Footer` auto-renders from `BINDINGS` |
| §4.1 Data table for list data | `DataTable` widget |
| §5.3 Color independence | Status uses `◉`/`⚠` symbols paired with text labels |
| §8.2 Focus invariant | Textual maintains exactly one focused widget |
| §10.2 Long-operation feedback | `refresh_data()` uses `@work`; shows "Refreshing..." |
| §11.1 Dashboard layout | Header metrics → DataTable → Footer |

---

## §T6 Responsive Breakpoints in Textual

Maps Standard §1.6 to Textual CSS breakpoints:

```css
/* Standard layout (80-119 cols) — default */
.region-nav {
    width: 12;
}

/* Compact (40-79 cols) — collapse navigation */
Screen {
    /* Textual doesn't have native media queries by terminal width.
       Use on_resize to toggle CSS classes. */
}
```

Responsive adaptation requires a resize handler:

```python
from textual.events import Resize

class MonoTuiApp(App):

    def on_resize(self, event: Resize) -> None:
        """Apply responsive breakpoints (Standard §1.6)."""
        width = event.size.width
        screen = self.screen

        # Remove all breakpoint classes
        screen.remove_class("-compact", "-standard", "-expanded", "-wide")

        if width < 80:
            screen.add_class("-compact")
        elif width < 120:
            screen.add_class("-standard")
        elif width < 160:
            screen.add_class("-expanded")
        else:
            screen.add_class("-wide")
```

Then style with breakpoint classes:

```css
Screen.-compact .region-nav {
    display: none;
}

Screen.-compact .region-context {
    display: none;
}

Screen.-expanded .region-nav {
    width: 16;
}

Screen.-wide .region-nav {
    width: 20;
}

Screen.-wide .region-context {
    width: 40;
}
```

---

## §T7 Modal Dialogs in Textual

Maps Standard §6.1 Level 3–4 and §3.1 modal pattern:

```python
from textual.screen import ModalScreen
from textual.widgets import Button, Label
from textual.containers import Vertical, Horizontal


class ConfirmDialog(ModalScreen[bool]):
    """Monospace TUI-compliant confirmation dialog (Standard §6.1 Level 4).

    Uses ModalScreen for scrim (Level 4) and double-line border (Level 3).
    """

    CSS = """
    ConfirmDialog {
        align: center middle;
    }

    #dialog-container {
        width: 50;
        max-width: 72;
        min-width: 30;
        height: auto;
        max-height: 20;
        border: double $primary;
        padding: 1 2;
        background: $surface;
    }

    #dialog-buttons {
        height: 3;
        align: center middle;
    }

    Button {
        margin: 0 1;
    }
    """

    BINDINGS = [
        ("escape", "cancel", "Cancel"),
        ("enter", "confirm", "Confirm"),
    ]

    def __init__(self, message: str) -> None:
        super().__init__()
        self._message = message

    def compose(self):
        with Vertical(id="dialog-container"):
            yield Label(self._message)
            with Horizontal(id="dialog-buttons"):
                yield Button("Confirm", variant="primary", id="confirm")
                yield Button("Cancel", variant="default", id="cancel")

    def action_confirm(self) -> None:
        self.dismiss(True)

    def action_cancel(self) -> None:
        self.dismiss(False)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.id == "confirm")
```

---

## §T8 Workflow Archetype Patterns

Maps Standard §12 workflow archetypes to Textual screen management, navigation, and state patterns.

### §T8.1 Workflow → Textual Navigation Table

| Workflow Archetype (§12) | Navigation Model | Textual Implementation |
|--------------------------|-----------------|----------------------|
| Wizard (§12.1) | Sequential/linear | `Screen` subclasses, `push_screen()` / `pop_screen()` per step |
| CRUD (§12.2) | Hub-and-spoke | List `Screen` as hub, `push_screen()` to detail/edit, `pop_screen()` to return |
| Monitor-Respond (§12.3) | Hub-and-spoke + real-time | Single `Screen` with `set_interval()` or `@work` for auto-refresh |
| Search-Act (§12.4) | Funnel | `ModalScreen` overlay or inline container with `Input` + `ListView` |
| Drill-Down (§12.5) | Hierarchical/tree | `push_screen()` per level, maintain stack state in app |
| Pipeline (§12.6) | Sequential + preview loop | Same as Wizard but with `pop_screen()` loop between preview and config |
| Review-Approve (§12.7) | Queue with auto-advance | Single `Screen` that swaps content; `call_after_refresh()` for auto-advance |
| Configuration (§12.8) | Flat/lateral | `TabbedContent` + `TabPane` per category |

### §T8.2 Wizard Flow

Implements §12.1 with a base `WizardScreen` and per-step subclasses.

```python
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Footer, Label, Static
from textual.containers import Horizontal, Vertical


class WizardStep(Screen):
    """Base for wizard steps (Standard §12.1)."""

    step_number: int = 0
    total_steps: int = 1
    step_title: str = ""

    def compose(self) -> ComposeResult:
        yield Static(
            f"Step {self.step_number} of {self.total_steps} ── {self.step_title}",
            classes="typography-title",
        )
        yield from self.compose_step()
        with Horizontal(id="wizard-buttons"):
            if self.step_number > 1:
                yield Button("Back", id="back")
            yield Button("Next", variant="primary", id="next")
            yield Button("Cancel", id="cancel")
        yield Footer()

    def compose_step(self) -> ComposeResult:
        """Override in subclasses to provide step content."""
        yield Label("Step content goes here")

    BINDINGS = [
        ("escape", "back_step", "Back"),
        ("enter", "next_step", "Next"),
    ]

    def action_next_step(self) -> None:
        # Subclasses override to validate before advancing
        self.dismiss(True)

    def action_back_step(self) -> None:
        self.dismiss(False)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "next":
            self.action_next_step()
        elif event.button.id == "back":
            self.action_back_step()
        elif event.button.id == "cancel":
            self.app.pop_screen()  # Exit wizard entirely
```

Step data is preserved by storing it on the `App` instance or a shared state object, so navigating backward does not lose input (§12.1 state rules).

### §T8.3 CRUD Hub-and-Spoke

Implements §12.2 with a list screen as the hub.

```python
class ItemListScreen(Screen):
    """CRUD list view — the hub (Standard §12.2)."""

    BINDINGS = [
        *ci("a", "add_item", "Add"),
        *ci("e", "edit_item", "Edit"),
        *ci("d", "delete_item", "Delete"),
        ("enter", "view_item", "View"),
        ("escape", "back", "Back"),
        ("slash", "filter", "/Filter"),
    ]

    def action_view_item(self) -> None:
        """Enter — push detail screen (spoke)."""
        row_key = self._get_selected_row_key()
        if row_key:
            self.app.push_screen(ItemDetailScreen(row_key))

    def action_edit_item(self) -> None:
        """e — push edit form (spoke)."""
        row_key = self._get_selected_row_key()
        if row_key:
            self.app.push_screen(ItemEditScreen(row_key))

    def action_delete_item(self) -> None:
        """d — confirm then delete (Standard §12.2: MUST confirm)."""
        def on_confirm(result: bool) -> None:
            if result:
                self._delete_selected()

        self.app.push_screen(ConfirmDialog("Delete this item?"), on_confirm)
```

List scroll position is preserved automatically — Textual maintains widget state when screens are pushed/popped (§12.2 state rules).

### §T8.4 Monitor-Respond with Auto-Refresh

Implements §12.3 with `set_interval()` for continuous updates.

```python
from textual.worker import work


class MonitorScreen(Screen):
    """Live dashboard with auto-refresh (Standard §12.3)."""

    BINDINGS = [
        *ci("r", "force_refresh", "Refresh"),
        ("enter", "open_detail", "Detail"),
        *ci("a", "acknowledge", "Ack"),
    ]

    def on_mount(self) -> None:
        """Start auto-refresh on mount."""
        self.set_interval(5.0, self.refresh_data)

    @work(thread=True, exclusive=True)
    async def refresh_data(self) -> None:
        """Background refresh — never blocks UI (§10.2, §12.3)."""
        data = await fetch_metrics()
        # Textual's call_from_thread ensures safe UI update
        self.app.call_from_thread(self._update_display, data)

    def _update_display(self, data) -> None:
        """Update widgets while preserving scroll position (§12.3 state rules)."""
        table = self.query_one(DataTable)
        cursor_row = table.cursor_row
        table.clear()
        table.add_rows(data)
        table.move_cursor(row=cursor_row)

    def action_open_detail(self) -> None:
        """Enter — drill into alert. Dashboard continues refreshing."""
        self.app.push_screen(AlertDetailScreen(self._selected_alert_id()))
```

### §T8.5 Drill-Down with State Stack

Implements §12.5 with a navigation stack preserving per-level state.

```python
from dataclasses import dataclass


@dataclass
class DrillDownState:
    """Preserved state per hierarchy level (Standard §12.5)."""
    level_id: str
    scroll_offset: int = 0
    filter_text: str = ""
    selected_index: int = 0


class DrillDownScreen(Screen):
    """Hierarchical drill-down (Standard §12.5)."""

    BINDINGS = [
        ("enter", "drill_in", "Open"),
        ("escape", "drill_out", "Back"),
        ("slash", "filter", "/Filter"),
        *ci("g", "jump_root", "Root"),
    ]

    def __init__(self, level_id: str) -> None:
        super().__init__()
        self.level_id = level_id

    def compose(self) -> ComposeResult:
        # Breadcrumb trail (Rendering Reference §R10.2)
        yield Static(self._build_breadcrumb(), id="breadcrumb")
        yield DataTable(id="items")
        yield Footer()

    def _build_breadcrumb(self) -> str:
        """Build breadcrumb from app's nav stack."""
        path = getattr(self.app, "_nav_path", [])
        parts = [s.level_id for s in path] + [self.level_id]
        return " \u203a ".join(parts)  # › separator

    def action_drill_in(self) -> None:
        """Enter — push deeper level, save current state."""
        state = DrillDownState(
            level_id=self.level_id,
            scroll_offset=self.query_one(DataTable).cursor_row,
        )
        if not hasattr(self.app, "_nav_path"):
            self.app._nav_path = []
        self.app._nav_path.append(state)
        child_id = self._get_selected_item_id()
        self.app.push_screen(DrillDownScreen(child_id))

    def action_drill_out(self) -> None:
        """Esc — pop stack, restore parent state (§12.5 state rules)."""
        if hasattr(self.app, "_nav_path") and self.app._nav_path:
            self.app._nav_path.pop()
        self.app.pop_screen()

    def action_jump_root(self) -> None:
        """g — return to overview (§12.5)."""
        if hasattr(self.app, "_nav_path"):
            self.app._nav_path.clear()
        while len(self.app.screen_stack) > 2:
            self.app.pop_screen()
```

### §T8.6 Configuration with TabbedContent

Implements §12.8 with Textual's `TabbedContent` for lateral navigation.

```python
from textual.widgets import TabbedContent, TabPane, Input, Switch


class ConfigScreen(Screen):
    """Non-linear settings (Standard §12.8)."""

    BINDINGS = [
        ("ctrl+s", "save_all", "Save"),
        ("escape", "exit_config", "Exit"),
        ("left_square_bracket", "previous_tab", "[Prev"),
        ("right_square_bracket", "next_tab", "]Next"),
    ]

    def compose(self) -> ComposeResult:
        with TabbedContent("General", "Network", "Security", "Advanced"):
            with TabPane("General", id="general"):
                yield Label("Application Name")
                yield Input(value="My App", id="app-name")
                yield Label("Enable Caching")
                yield Switch(value=True, id="caching")
            with TabPane("Network", id="network"):
                yield Label("API Host")
                yield Input(value="localhost", id="api-host")
            with TabPane("Security", id="security"):
                yield Label("Require Auth")
                yield Switch(value=True, id="require-auth")
            with TabPane("Advanced", id="advanced"):
                yield Label("Log Level")
                yield Input(value="INFO", id="log-level")
        yield Footer()

    # Track dirty state per tab (§12.8 state rules)
    _dirty_tabs: set[str] = set()

    def on_input_changed(self, event: Input.Changed) -> None:
        """Mark current tab as modified (§12.8: indicate modified categories)."""
        active_tab = self.query_one(TabbedContent).active
        self._dirty_tabs.add(active_tab)

    def on_switch_changed(self, event: Switch.Changed) -> None:
        active_tab = self.query_one(TabbedContent).active
        self._dirty_tabs.add(active_tab)

    def action_exit_config(self) -> None:
        """Esc — prompt if unsaved changes (§12.8 state rules)."""
        if self._dirty_tabs:
            def on_confirm(result: bool) -> None:
                if result:
                    self.app.pop_screen()

            self.app.push_screen(
                ConfirmDialog("Discard unsaved changes?"), on_confirm
            )
        else:
            self.app.pop_screen()
```

### §T8.7 Review-Approve with Auto-Advance

Implements §12.7 with inline decision keys and automatic progression.

```python
class ReviewScreen(Screen):
    """Queue-based review with auto-advance (Standard §12.7)."""

    BINDINGS = [
        *ci("a", "approve", "Approve"),
        *ci("x", "reject", "Reject"),
        *ci("d", "defer", "Defer"),
        *ci("c", "comment", "Comment"),
        *ci("n", "skip", "Skip"),
        ("ctrl+z", "undo_decision", "Undo"),
        ("escape", "back_to_queue", "Queue"),
    ]

    def __init__(self, queue: list, index: int = 0) -> None:
        super().__init__()
        self._queue = queue
        self._index = index
        self._last_decision: tuple | None = None

    def _show_current_item(self) -> None:
        """Render the current queue item with counter (§R10.3)."""
        remaining = sum(1 for i in self._queue if i["status"] == "pending")
        counter = f"{self._index + 1} of {len(self._queue)} ── {remaining} remaining"
        self.query_one("#queue-counter", Static).update(counter)
        self.query_one("#item-content", Static).update(
            self._queue[self._index]["content"]
        )

    def _advance(self) -> None:
        """Auto-advance to next undecided item (§12.7 state rules)."""
        for i in range(self._index + 1, len(self._queue)):
            if self._queue[i]["status"] == "pending":
                self._index = i
                self._show_current_item()
                return
        # No more items — return to queue
        self.app.pop_screen()

    def action_approve(self) -> None:
        """a — approve and auto-advance (§12.7)."""
        self._last_decision = (self._index, self._queue[self._index]["status"])
        self._queue[self._index]["status"] = "approved"
        self._advance()

    def action_undo_decision(self) -> None:
        """Ctrl+Z — undo last decision (§12.7 state rules)."""
        if self._last_decision:
            idx, prev_status = self._last_decision
            self._queue[idx]["status"] = prev_status
            self._index = idx
            self._show_current_item()
            self._last_decision = None
```

---

## §T9 Command Palette

Textual's built-in command palette maps to the Fuzzy Finder archetype (Standard §11.5) and the Search-Act workflow (Standard §12.4). It activates with `Ctrl+P` by default and provides type-to-filter over registered commands.

```python
from textual.command import Provider, Hit


class AppCommands(Provider):
    """Register commands for the palette (Standard §11.5 Fuzzy Finder)."""

    async def search(self, query: str):
        """Yield matching commands."""
        commands = {
            "Refresh Dashboard": self.app.action_refresh,
            "Toggle Filter": self.app.action_toggle_filter,
            "Show Help": self.app.action_help,
            "Quit": self.app.action_quit,
        }
        for name, action in commands.items():
            if query.lower() in name.lower():
                yield Hit(
                    score=1.0,
                    match_display=name,
                    command=action,
                )


class MonoTuiApp(App):
    COMMANDS = {AppCommands}
```

---

## Appendix TA: Textual Version Compatibility

This appendix targets **Textual >= 0.40**. Key features used:

| Feature | Minimum Version | Standard Reference |
|---------|----------------|-------------------|
| `ModalScreen` | 0.24 | §6.1 Level 4 |
| `DataTable` cursor modes | 0.30 | §4.1 data table |
| `TabbedContent` | 0.16 | §3.1 parallel contexts |
| `@work` decorator | 0.18 | §10.2 async operations |
| `Sparkline` widget | 0.36 | §R6 Braille sparklines |
| `Select` widget | 0.25 | §4.1 exclusive choice 6–25 |
| `command.Provider` | 0.32 | §11.5 Fuzzy Finder, §12.4 Search-Act |
| CSS variables (`$name`) | 0.24 | §5.1 semantic color roles |
| `Screen` stack (`push/pop`) | 0.11 | §12 Workflow archetypes (drill-down, wizard, CRUD) |
| `set_interval()` | 0.11 | §12.3 Monitor-Respond auto-refresh |
