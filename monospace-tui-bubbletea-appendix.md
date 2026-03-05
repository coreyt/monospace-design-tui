# Monospace Design TUI Bubble Tea Appendix

**Version: ALPHA** — Section structure and mapping notes. Not yet a complete appendix.

**Package:** `mono-tui`

This document maps the [Monospace Design TUI Standard](monospace-tui-design-standard.md) to [Bubble Tea](https://github.com/charmbracelet/bubbletea) (Go), including the companion libraries [Bubbles](https://github.com/charmbracelet/bubbles) (components), [Lip Gloss](https://github.com/charmbracelet/lipgloss) (styling), [Huh?](https://github.com/charmbracelet/huh) (forms), and [Gum](https://github.com/charmbracelet/gum) (shell scripts). It assumes familiarity with the standard and the [Rendering Reference](monospace-tui-rendering-reference.md).

**Architecture:** Bubble Tea follows **The Elm Architecture (TEA)** — `Init`, `Update`, `View`. State is immutable; `Update` returns a new model. `View` returns a string. There is no widget tree, no CSS, and no built-in layout engine. All rendering is manual string composition via Lip Gloss.

---

## §TB1 Component Mapping

### §TB1.1 Bubbles Component Table

| Monospace TUI Component (Standard §4) | Charm Component | Package | Notes |
|----------------------------------------|-----------------|---------|-------|
| Entry field | `textinput.Model` | `bubbles/textinput` | Placeholder, validation, character limit |
| Multi-line entry | `textarea.Model` | `bubbles/textarea` | Line numbers, word wrap |
| List box | `list.Model` | `bubbles/list` | Built-in fuzzy filtering, pagination, status bar |
| Data table | `table.Model` | `bubbles/table` | Column widths, row selection, header |
| Progress bar | `progress.Model` | `bubbles/progress` | Percentage, gradient colors |
| Spinner | `spinner.Model` | `bubbles/spinner` | Multiple spinner styles |
| Footer key strip | `help.Model` | `bubbles/help` | Renders `key.Binding` slices as help bar |
| Scrollable content | `viewport.Model` | `bubbles/viewport` | Content paging, scroll indicators |
| File picker | `filepicker.Model` | `bubbles/filepicker` | Directory browsing, filtering |
| Timer / stopwatch | `timer.Model`, `stopwatch.Model` | `bubbles/timer`, `bubbles/stopwatch` | Countdown and elapsed |

### §TB1.2 Huh? Form Components

| Monospace TUI Component | Huh? Field | Notes |
|--------------------------|-----------|-------|
| Entry field | `huh.Input` | Validation, placeholder, char limit |
| Multi-line entry | `huh.Text` | Editor mode |
| Radio group | `huh.Select` | Single selection from options |
| Checkbox group | `huh.MultiSelect` | Multiple selection |
| Toggle / confirm | `huh.Confirm` | Yes/No boolean |
| File picker | `huh.FilePicker` | Directory navigation |
| Read-only text | `huh.Note` | Instructions, summaries |

### §TB1.3 Missing Components

TODO: Implementation guidance for components not provided by Bubbles or Huh?.

| Monospace TUI Component | Implementation Strategy |
|--------------------------|------------------------|
| Push button | Custom model: styled text block, Enter to activate |
| Toggle / Switch | Custom model: `[X]`/`[ ]` rendering, Space to toggle |
| Radio group (non-form) | Custom model or embed `huh.Select` |
| Metric card | Lip Gloss styled block with border |
| Sparkline | Custom model using Braille characters (§R6) |
| Tabs | Custom model: styled tab bar, `[`/`]` to switch |
| Action bar / menus | Custom model: horizontal items, Alt to activate |
| Tree view | Custom model: indented list with expand/collapse |

### §TB1.4 Gum Shell Components

| Monospace TUI Component | Gum Command | Usage |
|--------------------------|-------------|-------|
| Entry field | `gum input` | `result=$(gum input --placeholder "Name")` |
| Multi-line entry | `gum write` | `result=$(gum write --header "Description")` |
| Select (exclusive) | `gum choose` | `result=$(gum choose "opt1" "opt2" "opt3")` |
| Multi-select | `gum choose --limit N` | `result=$(gum choose --no-limit "a" "b" "c")` |
| Confirm | `gum confirm` | `gum confirm "Continue?" && echo yes` |
| Fuzzy finder | `gum filter` | `result=$(cat items.txt \| gum filter)` |
| File picker | `gum file` | `result=$(gum file /path)` |
| Data table | `gum table` | `gum table < data.csv` |
| Scrollable viewer | `gum pager` | `cat long.txt \| gum pager` |
| Spinner / progress | `gum spin` | `gum spin --title "Working" -- command` |

---

## §TB2 Layout System

### §TB2.1 Three-Region Layout via Lip Gloss

TODO: Map Standard §1.3 to Lip Gloss `JoinHorizontal` and `JoinVertical`.

```go
func (m model) View() string {
    width, height := m.width, m.height

    // Region A — Navigation sidebar
    navWidth := 16
    nav := lipgloss.NewStyle().
        Width(navWidth).
        Height(height - 2).  // minus header and footer
        Border(lipgloss.NormalBorder(), false, true, false, false).
        Render(m.navView())

    // Region C — Context panel
    ctxWidth := 30
    ctx := lipgloss.NewStyle().
        Width(ctxWidth).
        Height(height - 2).
        Render(m.contextView())

    // Region B — Content (fills remaining)
    contentWidth := width - navWidth - ctxWidth
    content := lipgloss.NewStyle().
        Width(contentWidth).
        Height(height - 2).
        Render(m.contentView())

    body := lipgloss.JoinHorizontal(lipgloss.Top, nav, content, ctx)
    footer := m.footerView()

    return lipgloss.JoinVertical(lipgloss.Left, body, footer)
}
```

### §TB2.2 Responsive Breakpoints

TODO: Handle `tea.WindowSizeMsg` and branch layout in `View()`.

```go
func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
    switch msg := msg.(type) {
    case tea.WindowSizeMsg:
        m.width = msg.Width
        m.height = msg.Height
    }
    // ...
}

func (m model) View() string {
    switch {
    case m.width < 80:   // Compact: B only
    case m.width < 120:  // Standard: A + B
    case m.width < 160:  // Expanded: A + B + C
    default:             // Wide: full layout
    }
}
```

---

## §TB3 Keyboard Handling

### §TB3.1 Key Binding Declarations

TODO: Map Standard §2.2 three-tier system to Bubble Tea `key.Binding`.

```go
import "github.com/charmbracelet/bubbles/key"

type keyMap struct {
    // Tier 1 — Global
    Help key.Binding
    Quit key.Binding
    Back key.Binding
    Filter key.Binding
    Refresh key.Binding

    // Tier 1 — Scrolling
    Up   key.Binding
    Down key.Binding
    Top  key.Binding
    Bottom key.Binding

    // Tier 2 — Common actions
    Sort   key.Binding
    Delete key.Binding
    Edit   key.Binding
    Add    key.Binding
    Yank   key.Binding
}

func defaultKeyMap() keyMap {
    return keyMap{
        Help:    key.NewBinding(key.WithKeys("?", "f1"), key.WithHelp("?", "help")),
        Quit:    key.NewBinding(key.WithKeys("q", "Q"), key.WithHelp("q", "quit")),
        Back:    key.NewBinding(key.WithKeys("esc", "f3"), key.WithHelp("esc", "back")),
        Filter:  key.NewBinding(key.WithKeys("/"), key.WithHelp("/", "filter")),
        Refresh: key.NewBinding(key.WithKeys("r", "R", "f5"), key.WithHelp("r", "refresh")),
        Sort:    key.NewBinding(key.WithKeys("s", "S"), key.WithHelp("s", "sort")),
        // ... etc
    }
}
```

### §TB3.2 Key Routing by Focus

TODO: Manual key routing in `Update()` based on which panel has focus.

### §TB3.3 Footer Key Strip via Help Bubble

TODO: Map Standard §1.4 to `help.Model` rendering active key bindings.

### §TB3.4 Case Insensitivity

TODO: Standard §2.2 requires case-insensitive keys. Bubble Tea's `key.WithKeys()` accepts both cases.

---

## §TB4 Styling and Color

### §TB4.1 Semantic Color Theme

TODO: Map Standard §5.1 to a Lip Gloss theme struct.

```go
type Theme struct {
    Primary    lipgloss.AdaptiveColor
    Secondary  lipgloss.AdaptiveColor
    Tertiary   lipgloss.AdaptiveColor
    Error      lipgloss.AdaptiveColor
    Success    lipgloss.AdaptiveColor
    Warning    lipgloss.AdaptiveColor
    Surface    lipgloss.AdaptiveColor
    Text       lipgloss.AdaptiveColor
    Disabled   lipgloss.AdaptiveColor
}

var DefaultTheme = Theme{
    Primary:   lipgloss.AdaptiveColor{Light: "63", Dark: "75"},
    Secondary: lipgloss.AdaptiveColor{Light: "245", Dark: "109"},
    // ...
}
```

### §TB4.2 Elevation via Lip Gloss Borders

TODO: Map Standard §6.1 to Lip Gloss border styles.

| Elevation | Lip Gloss Border | Shadow |
|-----------|-----------------|--------|
| Level 0 | None | None |
| Level 1 | `lipgloss.NormalBorder()` | None |
| Level 2 | `lipgloss.NormalBorder()` | TODO: custom shadow rendering |
| Level 3 | `lipgloss.DoubleBorder()` | TODO: custom shadow rendering |
| Level 4 | `lipgloss.DoubleBorder()` | TODO: custom shadow + scrim |

### §TB4.3 State Rendering

TODO: Map Standard §8.1 states to Lip Gloss style variants.

| State | Lip Gloss Style |
|-------|----------------|
| Enabled | Normal foreground |
| Focused | `Reverse(true)` or bracket markers |
| Selected | `Reverse(true)` + marker |
| Disabled | `Faint(true)` |
| Error | `Foreground(theme.Error)` |

---

## §TB5 Screen and Navigation Management

### §TB5.1 Screen State Pattern

TODO: Map Standard §3.1 and §12 workflow archetypes to Bubble Tea state management.

```go
type screenState int

const (
    screenList screenState = iota
    screenDetail
    screenEdit
    screenConfirm
)

type model struct {
    state       screenState
    listModel   listModel
    detailModel detailModel
    editModel   editModel
    // ...
}

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
    switch m.state {
    case screenList:
        return m.updateList(msg)
    case screenDetail:
        return m.updateDetail(msg)
    // ...
    }
}

func (m model) View() string {
    switch m.state {
    case screenList:
        return m.listModel.View()
    case screenDetail:
        return m.detailModel.View()
    // ...
    }
}
```

### §TB5.2 Workflow Archetype Patterns

TODO: Mapping for each workflow archetype (§12).

| Workflow (§12) | Bubble Tea Pattern |
|----------------|-------------------|
| Wizard (§12.1) | State enum per step; Huh? `Form` with groups for form steps |
| CRUD (§12.2) | State enum: list/detail/edit; list state preserved on return |
| Monitor-Respond (§12.3) | `tea.Tick` cmd for auto-refresh; state enum for detail/action |
| Search-Act (§12.4) | `list.Model` with filtering; state for preview/action |
| Drill-Down (§12.5) | Stack of level states; push/pop on Enter/Esc |
| Pipeline (§12.6) | State enum per stage; loop between preview and config states |
| Review-Approve (§12.7) | Queue index in model; advance index on decision |
| Configuration (§12.8) | Huh? `Form` with multiple groups; or custom tab model |

---

## §TB6 Async Operations

### §TB6.1 Commands for Background Work

TODO: Map Standard §10.2 to Bubble Tea `tea.Cmd`.

```go
func fetchData() tea.Msg {
    // Runs in a goroutine
    result, err := api.GetData()
    if err != nil {
        return errMsg{err}
    }
    return dataMsg{result}
}

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
    switch msg := msg.(type) {
    case dataMsg:
        m.data = msg.data
    case errMsg:
        m.err = msg.err
    }
    return m, nil
}
```

### §TB6.2 Tick for Auto-Refresh

TODO: Map Monitor-Respond (§12.3) auto-refresh to `tea.Tick`.

---

## §TB7 Huh? for Admin/Config Screens

### §TB7.1 Form to Admin Archetype

TODO: Map Standard §11.2 and §12.8 to Huh? forms.

```go
form := huh.NewForm(
    huh.NewGroup(
        huh.NewInput().Title("Application Name").Value(&name),
        huh.NewSelect[string]().
            Title("Log Level").
            Options(
                huh.NewOption("Info", "info"),
                huh.NewOption("Debug", "debug"),
                huh.NewOption("Error", "error"),
            ).Value(&logLevel),
        huh.NewConfirm().Title("Enable Caching").Value(&caching),
    ).Title("General"),

    huh.NewGroup(
        huh.NewInput().Title("API Host").Value(&apiHost),
        huh.NewInput().Title("API Port").Value(&apiPort),
    ).Title("Network"),
)
```

### §TB7.2 Wizard via Huh? Groups

TODO: Map Wizard workflow (§12.1) to Huh? sequential groups with `LayoutDefault`.

### §TB7.3 Accessible Mode

TODO: Huh? supports `form.WithAccessible(true)` for screen reader compatibility — aligns with Standard §9.1.

---

## §TB8 Gum for Shell Script Workflows

### §TB8.1 Wizard Workflow in Shell

TODO: Map Wizard (§12.1) to sequential Gum commands.

```bash
#!/bin/bash
# Wizard workflow (§12.1) via Gum

# Step 1 — Project name
name=$(gum input --placeholder "Project name")

# Step 2 — Select archetype
archetype=$(gum choose "Dashboard" "Admin" "File Manager" "Editor" "Fuzzy Finder")

# Step 3 — Select palette
palette=$(gum choose "Default" "Monochrome" "Commander" "OS/2" "Turbo Pascal")

# Step 4 — Confirm
gum confirm "Create project '$name' with $archetype archetype and $palette palette?" || exit 1

echo "Creating project..."
gum spin --title "Setting up..." -- setup_command "$name" "$archetype" "$palette"
```

### §TB8.2 Limitations

Gum cannot build persistent full-screen TUI applications. It provides individual interaction components for shell scripts. Not suitable for screen archetypes, three-region layouts, or continuous keyboard interaction.

---

## §TB9 Compliance Gap Summary

| Standard Rule | Bubble Tea | Huh? | Gum |
|---------------|-----------|------|-----|
| §1.3 Three-region layout | Manual (Lip Gloss) | N/A | N/A |
| §1.4 Footer key strip | Help Bubble | Inline | N/A |
| §2.2 Key assignments | Manual routing | Built-in per-field | Per-command |
| §5.1 Semantic colors | Manual theme struct | Lip Gloss themes | CLI flags |
| §6.1 Elevation | Lip Gloss borders | N/A | `--border` |
| §6.4 Shadow rendering | Custom implementation needed | N/A | N/A |
| §6.5 Scrim | Custom implementation needed | N/A | N/A |
| §8.1 State model | Manual style switching | Focused/blurred | N/A |
| §8.2 Focus invariant | Manual focus tracking | Built-in | N/A |
| §9.1 Accessible mode | Not built-in | `WithAccessible(true)` | N/A |
| §11 Screen archetypes | Manual composition | Form-only | N/A |
| §12 Workflow archetypes | State enum pattern | Groups (wizard/config) | Sequential shell |
