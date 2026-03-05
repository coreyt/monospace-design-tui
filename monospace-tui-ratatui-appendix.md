# Monospace Design TUI Ratatui Appendix

**Version: ALPHA** — Section structure and mapping notes. Not yet a complete appendix.

**Package:** `mono-tui`

This document maps the [Monospace Design TUI Standard](monospace-tui-design-standard.md) to [Ratatui](https://ratatui.rs/) (Rust) with the [crossterm](https://docs.rs/crossterm/) backend. It assumes familiarity with the standard and the [Rendering Reference](monospace-tui-rendering-reference.md).

**Architecture:** Ratatui is an **immediate-mode rendering** library. There is no retained widget tree, no built-in event loop, and no application framework. On every frame the application reads events, updates state, and renders the entire UI via `terminal.draw(|frame| { ... })`. Ratatui diffs against the previous frame and writes only changed cells. The developer owns the event loop, state management, and all interaction logic.

**Key implication:** Ratatui provides the most precise control over character-cell rendering of any framework — every cell is individually addressable. This makes exact Monospace TUI compliance achievable (including shadows, scrim, mixed borders) but requires building all abstractions from scratch.

---

## §TRa1 Widget Mapping

### §TRa1.1 Component to Widget Table

| Monospace TUI Component (Standard §4) | Ratatui Widget | Module | Notes |
|----------------------------------------|---------------|--------|-------|
| Data table | `Table` | `ratatui::widgets` | Row selection via `TableState`, header, column widths |
| List box | `List` | `ratatui::widgets` | Selection via `ListState`, highlight style |
| Progress bar | `Gauge` / `LineGauge` | `ratatui::widgets` | Percentage, label, ratio |
| Sparkline | `Sparkline` | `ratatui::widgets` | Bar-style (not Braille — see §TRa1.2) |
| Tree / hierarchy | `Tree` | `tui-tree-widget` (third-party) | Or custom implementation |
| Tabs | `Tabs` | `ratatui::widgets` | Tab bar with selection index |
| Scrollable content | `Paragraph` with scroll | `ratatui::widgets` | `scroll` offset, `Wrap` policy |
| Chart / graph | `Chart` | `ratatui::widgets` | Axes, datasets, line/scatter |
| Bar chart | `BarChart` | `ratatui::widgets` | Grouped bars, labels |
| Calendar | `Monthly` | `ratatui::widgets` | Date display |
| Bordered container | `Block` | `ratatui::widgets` | Borders, titles, padding |

### §TRa1.2 Missing Components

| Monospace TUI Component | Implementation Strategy |
|--------------------------|------------------------|
| Entry field / text input | `tui-textarea` or `tui-input` crate (third-party) |
| Push button | Custom widget: styled `Paragraph` in a `Block`, Enter to activate |
| Toggle / Checkbox | Custom widget: `[X]`/`[ ]` rendering, Space to toggle |
| Radio group | Custom widget: `(*)`/`( )` rendering, arrow keys to cycle |
| Spin button | Custom widget: value display with up/down handlers |
| Metric card | `Block` with title + centered `Paragraph` |
| Footer key strip | Custom widget: `Paragraph` with key-action pairs (see §TRa3.3) |
| Action bar / menus | Custom widget: horizontal `Paragraph` items |
| Sparkline (Braille) | Custom widget using Braille encoding (§R6) |

---

## §TRa2 Layout System

### §TRa2.1 Three-Region Layout via Constraints

TODO: Map Standard §1.3 to Ratatui's constraint-based `Layout`.

```rust
use ratatui::layout::{Constraint, Direction, Layout};

fn render(frame: &mut Frame, area: Rect) {
    // Vertical split: body + footer
    let vertical = Layout::default()
        .direction(Direction::Vertical)
        .constraints([
            Constraint::Fill(1),      // Body
            Constraint::Length(1),     // Footer key strip
        ])
        .split(area);

    let body = vertical[0];
    let footer = vertical[1];

    // Horizontal split: Region A | Region B | Region C
    let horizontal = Layout::default()
        .direction(Direction::Horizontal)
        .constraints([
            Constraint::Length(16),    // Region A — Navigation
            Constraint::Fill(1),       // Region B — Content
            Constraint::Length(30),    // Region C — Context
        ])
        .split(body);

    let nav = horizontal[0];
    let content = horizontal[1];
    let context = horizontal[2];

    // Render widgets into each Rect...
}
```

### §TRa2.2 Responsive Breakpoints

TODO: Branch on `frame.area().width` to select different constraint sets.

```rust
fn layout_constraints(width: u16) -> Vec<Constraint> {
    match width {
        0..80   => vec![Constraint::Fill(1)],                          // Compact: B only
        80..120 => vec![Constraint::Length(12), Constraint::Fill(1)],   // Standard: A + B
        120..160 => vec![                                               // Expanded: A + B + C
            Constraint::Length(16),
            Constraint::Fill(1),
            Constraint::Length(30),
        ],
        _ => vec![                                                      // Wide
            Constraint::Length(20),
            Constraint::Fill(1),
            Constraint::Length(40),
        ],
    }
}
```

---

## §TRa3 Keyboard Handling

### §TRa3.1 Event Loop with crossterm

TODO: Map Standard §2.1 to crossterm event polling.

```rust
use crossterm::event::{self, Event, KeyCode, KeyModifiers};

fn handle_key(key: event::KeyEvent, app: &mut App) {
    // Normalize case — Standard §2.2 case insensitivity
    let code = match key.code {
        KeyCode::Char(c) => KeyCode::Char(c.to_ascii_lowercase()),
        other => other,
    };

    // Tier 1 — Global (always active)
    match (code, key.modifiers) {
        (KeyCode::Char('q'), _) | (KeyCode::Char('Q'), _) => app.quit(),
        (KeyCode::Esc, _) | (KeyCode::F(3), _) => app.back(),
        (KeyCode::Char('?'), _) | (KeyCode::F(1), _) => app.help(),
        (KeyCode::Char('r'), _) | (KeyCode::F(5), _) => app.refresh(),
        (KeyCode::Char('/'), _) => app.filter(),

        // Tier 2 — Context-dependent
        _ => match app.focus {
            Focus::List => handle_list_keys(code, key.modifiers, app),
            Focus::Detail => handle_detail_keys(code, key.modifiers, app),
            // ...
        },
    }
}
```

### §TRa3.2 Key Binding Registry

TODO: Structured key binding system for dynamic footer rendering.

```rust
struct KeyBinding {
    keys: Vec<KeyCode>,
    modifiers: KeyModifiers,
    action: &'static str,
    description: &'static str,
    tier: KeyTier,
    active: bool,
}

enum KeyTier { Tier1Global, Tier1Scrolling, Tier2Common, Tier3Mnemonic, Archetype }
```

### §TRa3.3 Footer Key Strip Widget

TODO: Custom widget rendering active key bindings as Standard §1.4.

```rust
fn render_footer(frame: &mut Frame, area: Rect, bindings: &[KeyBinding]) {
    let text: Vec<Span> = bindings.iter()
        .filter(|b| b.active)
        .flat_map(|b| vec![
            Span::styled(b.description_key(), Style::default().bold()),
            Span::raw(" "),
            Span::raw(b.description),
            Span::raw("  "),
        ])
        .collect();

    frame.render_widget(Paragraph::new(Line::from(text)), area);
}
```

---

## §TRa4 Styling and Color

### §TRa4.1 Semantic Color Theme

TODO: Map Standard §5.1 to a theme struct.

```rust
use ratatui::style::{Color, Modifier, Style};

struct Theme {
    primary: Color,
    primary_bg: Color,
    secondary: Color,
    tertiary: Color,
    error: Color,
    success: Color,
    warning: Color,
    surface: Color,
    text: Color,
    disabled: Color,
}

impl Default for Theme {
    fn default() -> Self {
        Self {
            primary: Color::Indexed(75),      // #5fafff
            primary_bg: Color::Indexed(17),   // #00005f
            secondary: Color::Indexed(109),   // #87afaf
            tertiary: Color::Indexed(79),     // #5fd7af
            error: Color::Indexed(196),       // #ff0000
            success: Color::Indexed(40),      // #00d700
            warning: Color::Indexed(220),     // #ffd700
            surface: Color::Indexed(234),     // #1c1c1c
            text: Color::Indexed(252),        // #d0d0d0
            disabled: Color::Indexed(240),    // #585858
        }
    }
}
```

### §TRa4.2 State to Style Mapping

TODO: Map Standard §8.1 to Ratatui `Style` + `Modifier`.

| State | Style |
|-------|-------|
| Enabled | `Style::default().fg(theme.text)` |
| Focused | `Style::default().add_modifier(Modifier::REVERSED)` |
| Selected | `Style::default().add_modifier(Modifier::REVERSED).fg(theme.primary)` |
| Disabled | `Style::default().fg(theme.disabled).add_modifier(Modifier::DIM)` |
| Error | `Style::default().fg(theme.error)` |
| Hovered | `Style::default().add_modifier(Modifier::UNDERLINED)` |

### §TRa4.3 Elevation via Block Borders

TODO: Map Standard §6.1.

| Elevation | Border Type | Shadow |
|-----------|------------|--------|
| Level 0 | `Borders::NONE` | None |
| Level 1 | `BorderType::Plain` (single-line) | None |
| Level 2 | `BorderType::Plain` + shadow (§TRa4.4) | 2x1 offset |
| Level 3 | `BorderType::Double` + shadow | 2x1 offset |
| Level 4 | `BorderType::Double` + shadow + scrim | 2x1 offset + dim background |

### §TRa4.4 Shadow Rendering

TODO: Ratatui's immediate-mode rendering allows direct cell manipulation for shadows.

```rust
fn render_shadow(frame: &mut Frame, widget_area: Rect) {
    // Shadow: 2 cols right, 1 row below (Rendering Reference §R5.1)
    let shadow_style = Style::default()
        .fg(Color::Indexed(240))
        .add_modifier(Modifier::DIM);

    // Right shadow (2 cols wide, widget height)
    for y in (widget_area.y + 1)..=(widget_area.y + widget_area.height) {
        for x in 0..2 {
            let col = widget_area.x + widget_area.width + x;
            if let Some(cell) = frame.buffer_mut().cell_mut((col, y)) {
                cell.set_style(shadow_style);
            }
        }
    }
    // Bottom shadow (widget width + 2, 1 row)
    let y = widget_area.y + widget_area.height;
    for x in (widget_area.x + 2)..=(widget_area.x + widget_area.width + 1) {
        if let Some(cell) = frame.buffer_mut().cell_mut((x, y)) {
            cell.set_style(shadow_style);
        }
    }
}
```

### §TRa4.5 Scrim Rendering

TODO: Dim all cells outside the modal area for Level 4 elevation.

```rust
fn render_scrim(frame: &mut Frame, modal_area: Rect) {
    let scrim_style = Style::default().add_modifier(Modifier::DIM);
    let buf = frame.buffer_mut();
    for y in 0..buf.area.height {
        for x in 0..buf.area.width {
            if !modal_area.contains((x, y).into()) {
                if let Some(cell) = buf.cell_mut((x, y)) {
                    cell.set_style(scrim_style);
                }
            }
        }
    }
}
```

---

## §TRa5 Screen and Navigation Management

### §TRa5.1 Screen State Pattern

TODO: Map Standard §12 workflow archetypes to Rust state management.

```rust
enum Screen {
    List(ListScreen),
    Detail(DetailScreen),
    Edit(EditScreen),
}

struct App {
    screen: Screen,
    screen_stack: Vec<Screen>,  // For drill-down (§12.5)
}

impl App {
    fn push_screen(&mut self, screen: Screen) {
        let current = std::mem::replace(&mut self.screen, screen);
        self.screen_stack.push(current);
    }

    fn pop_screen(&mut self) {
        if let Some(prev) = self.screen_stack.pop() {
            self.screen = prev;
        }
    }
}
```

### §TRa5.2 Workflow Archetype Patterns

TODO: Mapping for each workflow archetype.

| Workflow (§12) | Ratatui Pattern |
|----------------|----------------|
| Wizard (§12.1) | Step enum; per-step render function; step data in struct |
| CRUD (§12.2) | Screen enum: List/Detail/Edit; `ListState` preserved |
| Monitor-Respond (§12.3) | Tick-based refresh via crossterm poll timeout |
| Search-Act (§12.4) | Filter input + `List` with dynamic filtering |
| Drill-Down (§12.5) | Screen stack with per-level state structs |
| Pipeline (§12.6) | Stage enum; `Gauge` for execution progress |
| Review-Approve (§12.7) | Queue index; advance on decision |
| Configuration (§12.8) | `Tabs` widget + per-tab form state |

---

## §TRa6 Async Operations

### §TRa6.1 Tokio Event Loop

TODO: Map Standard §10.2 to async Ratatui with tokio.

```rust
use crossterm::event::EventStream;
use tokio_stream::StreamExt;

#[tokio::main]
async fn main() {
    let mut events = EventStream::new();
    let mut interval = tokio::time::interval(Duration::from_secs(5));

    loop {
        tokio::select! {
            Some(Ok(event)) = events.next() => {
                handle_event(event, &mut app);
            }
            _ = interval.tick() => {
                app.refresh_data().await;
            }
        }
        terminal.draw(|frame| app.render(frame))?;
        if app.should_quit { break; }
    }
}
```

---

## §TRa7 Color Capability Detection

TODO: Ratatui does not auto-detect color capability. Implement Standard §5.6 / §R7 manually.

```rust
fn detect_color_capability() -> ColorCapability {
    if let Ok(ct) = std::env::var("COLORTERM") {
        if ct == "truecolor" || ct == "24bit" {
            return ColorCapability::TrueColor;
        }
    }
    if let Ok(term) = std::env::var("TERM") {
        if term.contains("256color") {
            return ColorCapability::Color256;
        }
        if term == "dumb" {
            return ColorCapability::Monochrome;
        }
    }
    ColorCapability::Color16
}
```

---

## §TRa8 Compliance Gap Summary

| Standard Rule | Status | Notes |
|---------------|--------|-------|
| §1.3 Three-region layout | Full support | Constraint-based layout maps directly |
| §1.4 Footer key strip | Custom widget needed | No built-in — render as `Paragraph` |
| §2.2 Key assignments | Manual implementation | No key binding abstraction |
| §4.1 Widget selection | Partial | No text input, buttons, checkboxes in core |
| §5.6 Color detection | Manual implementation | Not built-in |
| §6.4 Shadow rendering | Full support | Direct buffer cell manipulation |
| §6.5 Scrim | Full support | Direct buffer cell manipulation |
| §8.1 State model | Manual style switching | No built-in state system |
| §8.2 Focus invariant | Manual tracking | No focus system |
| §9.1 Accessible mode | Not supported | No screen reader integration |
| §10.2 Long-operation feedback | `Gauge` / `LineGauge` | Built-in progress widgets |
| §R9 Mixed border junctions | Full support | Direct Unicode character rendering |

**Strengths:** Ratatui's immediate-mode rendering and direct buffer access make it the best framework for pixel-perfect Monospace TUI compliance — shadows, scrim, mixed borders, and custom box-drawing are all natively achievable. The constraint-based layout maps cleanly to the three-region model.

**Weaknesses:** Everything above the rendering layer (focus, key routing, screen stack, state model, interactive widgets) must be built by the developer.
