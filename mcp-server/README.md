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

## Available Tools (15)

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

### Keyboard

| Tool | Description |
|------|-------------|
| `get_keyboard_bindings(tier?)` | Get bindings by tier (tier1_global, tier1_scrolling, tier1_text_entry, tier2_common, tier3_mnemonics) |

### Archetypes

| Tool | Description |
|------|-------------|
| `list_archetypes()` | List all 5 archetypes |
| `get_archetype(name)` | Get archetype details (dashboard, admin, file-manager, editor, fuzzy-finder) |

### Characters

| Tool | Description |
|------|-------------|
| `get_box_drawing(style?)` | Box-drawing characters (single, heavy, double, rounded, dashed, blocks, indicators) |
