# Monospace Design TUI — MCP Server

MCP server that exposes the Monospace TUI design system so AI agents in other
projects can query design rules, color palettes, component specs, keyboard
bindings, and archetypes when building terminal user interfaces.

## Requirements

- Python 3.10+
- `mcp` SDK (`pip install mcp`)

## Configuration

Add to your Claude Code MCP settings (`~/.claude/settings.json` or project
`.mcp.json`):

```json
{
  "mcpServers": {
    "mono-tui": {
      "command": "python3",
      "args": ["/home/coreyt/projects/monospace-design-tui/mcp-server/server.py"]
    }
  }
}
```

## Available Tools (18)

### Design Consultation (sampling)

| Tool | Description |
|------|-------------|
| `design_consultation(message, session_id?)` | Start or continue a multi-turn design consultation. Describe your project and get proposals for workflows, screens, components, keyboard maps, and palettes. Uses MCP sampling to reason with full design system context. Pass `session_id` from a previous response to continue the conversation. |

### Workflow Archetypes

| Tool | Description |
|------|-------------|
| `list_workflow_archetypes()` | List all 7 workflow archetypes (task-flow patterns) |
| `get_workflow_archetype(name)` | Get workflow details: screen sequence, navigation model, keyboard map, layout guidance, state management (wizard, crud, monitor-respond, search-act, drill-down, pipeline, review-approve) |

### UI Archetypes

| Tool | Description |
|------|-------------|
| `list_archetypes()` | List all 5 UI screen archetypes |
| `get_archetype(name)` | Get screen archetype details (dashboard, admin, file-manager, editor, fuzzy-finder) |

### Standard & Reference Sections

| Tool | Description |
|------|-------------|
| `get_standard_section(section)` | Read a section of the design standard (layout, keyboard, navigation, components, color, borders, typography, state, accessibility, motion, archetypes) |
| `get_reference_section(section)` | Read a rendering reference section (box-drawing, sgr-codes, color-palette, measurements, shadows, escape-sequences, color-detection, mixed-borders, sparklines) |
| `get_textual_guide()` | Get the full Textual framework mapping guide |
| `get_project_template()` | Get the TUI-DESIGN.template.md for project overrides |

### Structured Data

| Tool | Description |
|------|-------------|
| `get_design_tokens()` | Spacing scale, elevation levels, timing tiers, breakpoints, typography |
| `get_state_model()` | 7-state rendering model with SGR codes |

### Color Palettes

| Tool | Description |
|------|-------------|
| `list_palettes()` | List all 8 available palettes |
| `get_palette(name)` | Get palette colors (default, monochrome, commander, os2, turbo, amber, green, airlock) |

### Components

| Tool | Description |
|------|-------------|
| `list_components()` | List all 11 component specs |
| `get_component_spec(component)` | Get measurements for a component (push-button, entry-field, toggle, etc.) |
| `get_widget_recommendation(data_type?)` | Widget selection by data type (boolean, exclusive, free_text, numeric, action, spin_value) |

### Keyboard & Characters

| Tool | Description |
|------|-------------|
| `get_keyboard_bindings(tier?)` | Get bindings by tier (tier1_global, tier1_scrolling, tier1_text_entry, tier2_common, tier3_mnemonics) |
| `get_box_drawing(style?)` | Box-drawing characters (single, heavy, double, rounded, dashed, blocks, indicators) |

## How it works

### Direct queries

An agent building a TUI calls individual tools to get specific design data:
archetype → layout rules → components → palette → keyboard → rendering.

### Design consultation (agent-to-agent)

An agent describes its project and has a multi-turn conversation with the
design system. The `design_consultation` tool uses **MCP sampling** — the
server requests an LLM completion from the client with the full Monospace TUI
standard as context. The calling agent provides the reasoning capability; the
server provides the design knowledge.

```
Project agent                    mono-tui MCP server
    │                                    │
    ├─ design_consultation(desc) ──────> │
    │                                    ├─ loads standard context
    │                                    ├─ builds system prompt with
    │                                    │  workflow archetypes, UI archetypes,
    │                                    │  tokens, palettes, keyboard tiers
    │           sampling request <────── ├─ requests LLM completion
    ├─ LLM reasoning ──────────────────> │
    │           proposal <────────────── ├─ returns proposal + session_id
    │                                    │
    ├─ design_consultation(follow_up,    │
    │    session_id=...) ──────────────> │  (continues with full history)
    │              ...                   │
```
