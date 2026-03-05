"""Monospace Design TUI — MCP Server.

Exposes the Monospace TUI design system (palettes, tokens, components,
keyboard bindings, archetypes, and full standard/reference sections)
so that AI agents in other projects can query design rules when building
terminal user interfaces.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Optional

from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
STANDARD_DIR = PROJECT_ROOT / "website" / "content" / "standard"
REFERENCE_DIR = PROJECT_ROOT / "website" / "content" / "reference"
TEXTUAL_DIR = PROJECT_ROOT / "website" / "content" / "textual"

CORE_DOCS = {
    "design-standard": PROJECT_ROOT / "mono-tui-design-standard.md",
    "rendering-reference": PROJECT_ROOT / "mono-tui-rendering-reference.md",
    "textual-appendix": PROJECT_ROOT / "mono-tui-textual-appendix.md",
    "research": PROJECT_ROOT / "mono-tui.md",
    "template": PROJECT_ROOT / "TUI-DESIGN.template.md",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _strip_frontmatter(text: str) -> str:
    """Remove Hugo YAML frontmatter (--- ... ---) from markdown."""
    return re.sub(r"\A---\n.*?---\n+", "", text, count=1, flags=re.DOTALL)


def _read_section_file(directory: Path, name: str) -> str | None:
    """Read a markdown file from a content directory, stripping frontmatter."""
    candidates = [
        directory / f"{name}.md",
        directory / f"_{name}.md",
        directory / "_index.md" if name == "index" else None,
    ]
    for path in candidates:
        if path and path.is_file():
            return _strip_frontmatter(path.read_text())
    return None


def _list_sections(directory: Path) -> list[str]:
    """List available section names in a content directory."""
    return sorted(
        p.stem for p in directory.glob("*.md") if p.stem != "_index"
    )


# ---------------------------------------------------------------------------
# MCP Server
# ---------------------------------------------------------------------------

mcp = FastMCP(
    "mono-tui",
    instructions="""\
Monospace Design TUI — a complete design system for terminal user interfaces.

Use this server when building, designing, or auditing a TUI application.
The tools are organized around a recommended workflow, but you can jump to
any tool at any point.

## Recommended workflow

1. **Pick an archetype** — Start here. Call `list_archetypes()` to see the
   five defined application patterns (dashboard, admin, file-manager, editor,
   fuzzy-finder), then `get_archetype(name)` to get the layout, component
   list, and keyboard bindings for your pattern. If none fit, skip to step 2.

2. **Get layout rules** — Call `get_standard_section("layout")` for the
   three-region layout model, responsive breakpoints, and footer requirements.
   Call `get_design_tokens()` for the spacing scale, elevation levels, timing
   tiers, and minimum dimensions as structured data.

3. **Choose components** — Call `get_widget_recommendation(data_type)` to get
   the correct widget for your data (boolean → toggle, exclusive 2-5 → radio,
   exclusive 6-25 → list box, etc.). Then call `get_component_spec(name)` for
   exact measurements, formats, and interaction rules.

4. **Apply a color palette** — Call `list_palettes()` to browse the eight
   named palettes, then `get_palette(name)` for the full semantic-role color
   mapping with 256-color indices and hex values.

5. **Wire keyboard bindings** — Call `get_keyboard_bindings()` for all three
   tiers, or filter by tier. Tier 1 (global) keys are mandatory. Tier 2
   (common actions) should be bound when the action exists. Tier 3 (screen
   mnemonics) are application-defined.

6. **Render correctly** — Call `get_box_drawing(style)` for border characters
   with Unicode codepoints. Call `get_state_model()` for the 7-state rendering
   model (enabled, focused, hovered, pressed, selected, disabled, error) with
   SGR codes. Call `get_reference_section(name)` for shadows, SGR codes,
   sparklines, escape sequences, or color detection.

7. **Implement in Textual** — Call `get_textual_guide()` for the full mapping
   of standard rules to Python Textual widgets, TCSS patterns, async/worker
   rules, and the `ci()` case-insensitive binding helper.

8. **Document overrides** — Call `get_project_template()` to get the
   TUI-DESIGN.template.md file for recording project-specific WAIVE, OVERRIDE,
   or TIGHTEN decisions against the standard.

## Quick reference

- Standard sections (markdown): layout, keyboard, navigation, components,
  color, borders, typography, state, accessibility, motion, archetypes
- Reference sections (markdown): box-drawing, sgr-codes, color-palette,
  measurements, shadows, escape-sequences, color-detection, mixed-borders,
  sparklines
- Palettes: default, monochrome, commander, os2, turbo, amber, green, airlock
- Components: push-button, entry-field, toggle, radio-group, list-box,
  data-table, metric-card, dialog, menu, spin-button, footer
- Archetypes: dashboard, admin, file-manager, editor, fuzzy-finder
- Widget data types: boolean, exclusive, free_text, numeric, action, spin_value
- Keyboard tiers: tier1_global, tier1_scrolling, tier1_text_entry,
  tier2_common, tier3_mnemonics
- Box-drawing styles: single, heavy, double, rounded, dashed, blocks,
  indicators
""",
)

# ---- Standard sections ----------------------------------------------------

@mcp.tool()
def get_standard_section(
    section: str,
) -> str:
    """Get a section of the Monospace TUI Design Standard.

    Available sections: layout, keyboard, navigation, components, color,
    borders, typography, state, accessibility, motion, archetypes.
    """
    content = _read_section_file(STANDARD_DIR, section)
    if content is None:
        available = _list_sections(STANDARD_DIR)
        return f"Section '{section}' not found. Available: {', '.join(available)}"
    return content


# ---- Reference sections ---------------------------------------------------

@mcp.tool()
def get_reference_section(
    section: str,
) -> str:
    """Get a section of the Monospace TUI Rendering Reference.

    Available sections: box-drawing, sgr-codes, color-palette, measurements,
    shadows, escape-sequences, color-detection, mixed-borders, sparklines.
    """
    content = _read_section_file(REFERENCE_DIR, section)
    if content is None:
        available = _list_sections(REFERENCE_DIR)
        return f"Section '{section}' not found. Available: {', '.join(available)}"
    return content


# ---- Textual appendix -----------------------------------------------------

@mcp.tool()
def get_textual_guide() -> str:
    """Get the Textual framework mapping guide.

    Returns widget mappings, TCSS patterns, async rules, and binding helpers
    for implementing Monospace TUI with Python Textual.
    """
    path = CORE_DOCS["textual-appendix"]
    if path.is_file():
        return path.read_text()
    # Fall back to website version
    content = _read_section_file(TEXTUAL_DIR, "_index")
    if content:
        return content
    return "Textual appendix not found."


# ---- Design tokens --------------------------------------------------------

@mcp.tool()
def get_design_tokens() -> dict:
    """Get core design tokens: spacing scale, elevation levels, timing tiers,
    responsive breakpoints, and typography treatments.

    Returns structured data that can be directly used in implementations.
    """
    return {
        "spacing_scale": {
            "values": [0, 1, 2, 3, 4, 6, 8],
            "unit": "character cells",
            "rule": "Intermediate values (5, 7) MUST NOT be used.",
        },
        "elevation_levels": [
            {
                "level": 0,
                "use": "Inline content",
                "border": "none",
                "shadow": False,
                "scrim": False,
            },
            {
                "level": 1,
                "use": "Panels, content regions",
                "border": "single-line",
                "border_chars": "─│┌┐└┘├┤┬┴┼",
                "shadow": False,
                "scrim": False,
            },
            {
                "level": 2,
                "use": "Menus, dropdowns",
                "border": "single-line",
                "border_chars": "─│┌┐└┘├┤┬┴┼",
                "shadow": {"offset_cols": 2, "offset_rows": 1, "sgr": "dim (SGR 2)"},
                "scrim": False,
            },
            {
                "level": 3,
                "use": "Dialogs, secondary windows",
                "border": "double-line",
                "border_chars": "═║╔╗╚╝╠╣╦╩╬",
                "shadow": {"offset_cols": 2, "offset_rows": 1, "sgr": "dim (SGR 2)"},
                "scrim": False,
            },
            {
                "level": 4,
                "use": "Modal overlays",
                "border": "double-line",
                "border_chars": "═║╔╗╚╝╠╣╦╩╬",
                "shadow": {"offset_cols": 2, "offset_rows": 1, "sgr": "dim (SGR 2)"},
                "scrim": True,
            },
        ],
        "timing_tiers": {
            "instant": {"ms": 0, "use": "State toggles, key echo"},
            "fast": {"ms": "50-100", "use": "Button press feedback, cursor movement"},
            "standard": {"ms": "150-300", "use": "Panel transitions, menu open/close"},
            "slow": {"ms": "300-500", "use": "Screen transitions, progressive disclosure"},
            "max": "500ms for any UI transition",
        },
        "breakpoints": {
            "compact": {"cols": "40-79", "layout": "Region A collapses; C hidden/stacked; footer 1 row"},
            "standard": {"cols": "80-119", "layout": "Region A visible (8-12 cols); C optional; full footer"},
            "expanded": {"cols": "120-159", "layout": "Full three-region; A at 12-16 cols"},
            "wide": {"cols": "160+", "layout": "A at full width (up to 20); C expanded"},
        },
        "min_dimensions": {
            "minimum_viable": {"cols": 80, "rows": 24, "requirement": "MUST support"},
            "standard": {"cols": 120, "rows": 40, "requirement": "SHOULD target"},
        },
        "typography": {
            "display": {"sgr": "1 (bold)", "transform": "uppercase"},
            "title": {"sgr": "1 (bold)", "transform": "none"},
            "body": {"sgr": "none", "transform": "none"},
            "label": {"sgr": "2 (dim)", "transform": "none"},
        },
    }


# ---- Color palettes -------------------------------------------------------

PALETTES = {
    "default": {
        "name": "Default (Textual Dark)",
        "description": "Standard dark theme based on Textual defaults",
        "theme": "dark",
        "roles": {
            "primary": {"fg": {"index": 75, "hex": "#5fafff"}, "bg": {"index": 17, "hex": "#00005f"}},
            "secondary": {"fg": {"index": 109, "hex": "#87afaf"}, "bg": {"index": 236, "hex": "#303030"}},
            "tertiary": {"fg": {"index": 79, "hex": "#5fd7af"}, "bg": {"index": 236, "hex": "#303030"}},
            "error": {"fg": {"index": 196, "hex": "#ff0000"}, "bg": {"index": 52, "hex": "#5f0000"}},
            "neutral": {"fg": {"index": 252, "hex": "#d0d0d0"}, "fg_bright": {"index": 231, "hex": "#ffffff"}, "bg": {"index": 235, "hex": "#262626"}},
        },
        "status": {
            "healthy": {"index": 40, "hex": "#00d700"},
            "error": {"index": 196, "hex": "#ff0000"},
            "warning": {"index": 220, "hex": "#ffd700"},
            "inactive": {"index": 240, "hex": "#585858"},
        },
    },
    "monochrome": {
        "name": "Monochrome (CUA)",
        "description": "Single-color theme using SGR attributes only",
        "theme": "dark",
        "roles": {
            "primary": {"sgr": "1 (bold)", "note": "Bold white on black"},
            "secondary": {"sgr": "none", "note": "Normal white on black"},
            "tertiary": {"sgr": "4 (underline)", "note": "Underlined white on black"},
            "error": {"sgr": "1;7 (bold+reverse)", "note": "Bold reverse white on black"},
            "neutral": {"sgr": "2 (dim)", "note": "Dim white on black"},
        },
        "status": {
            "healthy": {"sgr": "none"},
            "warning": {"sgr": "1 (bold)"},
            "error": {"sgr": "1;7 (bold+reverse)"},
            "inactive": {"sgr": "2 (dim)"},
        },
    },
    "commander": {
        "name": "Commander (Norton/OS2 PM)",
        "description": "Classic blue-background file manager theme",
        "theme": "dark",
        "roles": {
            "primary": {"fg": {"index": 15, "hex": "#ffffff"}, "bg": {"index": 19, "hex": "#0000af"}},
            "secondary": {"fg": {"index": 14, "hex": "#00ffff"}, "bg": {"index": 237, "hex": "#3a3a3a"}},
            "tertiary": {"fg": {"index": 11, "hex": "#ffff00"}, "bg": {"index": 19, "hex": "#0000af"}},
            "error": {"fg": {"index": 196, "hex": "#ff0000"}, "bg": {"index": 52, "hex": "#5f0000"}},
            "neutral": {"fg": {"index": 15, "hex": "#ffffff"}, "bg": {"index": 19, "hex": "#0000af"}},
        },
        "special": {
            "dialog": {"fg": {"index": 232, "hex": "#080808"}, "bg": {"index": 250, "hex": "#bcbcbc"}},
            "button": {"fg": {"index": 232, "hex": "#080808"}, "bg": {"index": 78, "hex": "#5fd787"}},
        },
    },
    "os2": {
        "name": "OS/2 (Presentation Manager)",
        "description": "IBM OS/2 Warp yellow-on-blue theme",
        "theme": "dark",
        "roles": {
            "primary": {"fg": {"index": 14, "hex": "#ffff00"}, "bg": {"index": 1, "hex": "#0000aa"}},
            "secondary": {"fg": {"index": 7, "hex": "#c0c0c0"}, "bg": {"index": 1, "hex": "#0000aa"}},
            "tertiary": {"fg": {"index": 0, "hex": "#000000"}, "bg": {"index": 7, "hex": "#c0c0c0"}},
            "error": {"fg": {"index": 12, "hex": "#ff5555"}, "bg": {"index": 1, "hex": "#0000aa"}},
            "neutral": {"fg": {"index": 0, "hex": "#000000"}, "bg": {"index": 7, "hex": "#aaaaaa"}},
        },
    },
    "turbo": {
        "name": "Turbo Pascal (Borland IDE)",
        "description": "Classic Borland IDE white-on-blue theme",
        "theme": "dark",
        "roles": {
            "primary": {"fg": {"index": 15, "hex": "#ffffff"}, "bg": {"index": 1, "hex": "#0000aa"}},
            "secondary": {"fg": {"index": 7, "hex": "#c0c0c0"}, "bg": {"index": 1, "hex": "#0000aa"}},
            "tertiary": {"fg": {"index": 0, "hex": "#000000"}, "bg": {"index": 2, "hex": "#00aa00"}},
            "error": {"fg": {"index": 12, "hex": "#ff5555"}, "bg": {"index": 1, "hex": "#0000aa"}},
            "neutral": {"fg": {"index": 0, "hex": "#000000"}, "bg": {"index": 7, "hex": "#aaaaaa"}},
        },
        "special": {
            "desktop_pattern": "░ (U+2591) in light gray on blue",
        },
    },
    "amber": {
        "name": "Amber Phosphor (DEC VT220)",
        "description": "Single-hue amber CRT theme",
        "theme": "dark",
        "roles": {
            "primary": {"fg": {"index": 214, "hex": "#ffaf00"}, "bg": {"index": 0, "hex": "#000000"}},
            "secondary": {"fg": {"index": 172, "hex": "#d78700"}, "bg": {"index": 0, "hex": "#000000"}},
            "tertiary": {"fg": {"index": 214, "hex": "#ffaf00"}, "bg": {"index": 0, "hex": "#000000"}, "sgr": "4 (underline)"},
            "error": {"fg": {"index": 214, "hex": "#ffaf00"}, "bg": {"index": 0, "hex": "#000000"}, "sgr": "1;7 (bold+reverse)"},
            "neutral": {"fg": {"index": 136, "hex": "#af8700"}, "bg": {"index": 0, "hex": "#000000"}},
        },
    },
    "green": {
        "name": "Green Phosphor (DEC VT100)",
        "description": "Single-hue green CRT theme",
        "theme": "dark",
        "roles": {
            "primary": {"fg": {"index": 82, "hex": "#5fff00"}, "bg": {"index": 0, "hex": "#000000"}},
            "secondary": {"fg": {"index": 34, "hex": "#00af00"}, "bg": {"index": 0, "hex": "#000000"}},
            "tertiary": {"fg": {"index": 82, "hex": "#5fff00"}, "bg": {"index": 0, "hex": "#000000"}, "sgr": "4 (underline)"},
            "error": {"fg": {"index": 82, "hex": "#5fff00"}, "bg": {"index": 0, "hex": "#000000"}, "sgr": "1;7 (bold+reverse)"},
            "neutral": {"fg": {"index": 28, "hex": "#008700"}, "bg": {"index": 0, "hex": "#000000"}},
        },
    },
    "airlock": {
        "name": "Airlock (AI-Agent Security)",
        "description": "Muted dark theme for security/agent proxy interfaces",
        "theme": "dark",
        "roles": {
            "primary": {"fg": {"index": 71, "hex": "#5faf5f"}, "bg": {"index": 236, "hex": "#303030"}},
            "secondary": {"fg": {"index": 109, "hex": "#87afaf"}, "bg": {"index": 236, "hex": "#303030"}},
            "tertiary": {"fg": {"index": 214, "hex": "#ffaf00"}, "bg": {"index": 236, "hex": "#303030"}},
            "error": {"fg": {"index": 167, "hex": "#d75f5f"}, "bg": {"index": 52, "hex": "#5f0000"}},
            "neutral": {"fg": {"index": 252, "hex": "#d0d0d0"}, "bg": {"index": 235, "hex": "#262626"}},
        },
        "status": {
            "healthy": {"index": 77, "hex": "#5fd75f"},
            "error": {"index": 167, "hex": "#d75f5f"},
            "warning": {"index": 214, "hex": "#ffaf00"},
            "inactive": {"index": 245, "hex": "#8a8a8a"},
        },
    },
}


@mcp.tool()
def list_palettes() -> list[dict]:
    """List all available Monospace TUI color palettes.

    Returns name, description, and theme type for each palette.
    """
    return [
        {"id": pid, "name": p["name"], "description": p["description"], "theme": p.get("theme", "dark")}
        for pid, p in PALETTES.items()
    ]


@mcp.tool()
def get_palette(name: str) -> dict | str:
    """Get a specific color palette with all semantic role mappings.

    Args:
        name: Palette identifier. One of: default, monochrome, commander,
              os2, turbo, amber, green, airlock.

    Returns full palette with foreground/background colors per semantic role,
    status colors, and any special mappings.
    """
    palette = PALETTES.get(name)
    if palette is None:
        return f"Palette '{name}' not found. Available: {', '.join(PALETTES.keys())}"
    return palette


# ---- Component specs -------------------------------------------------------

COMPONENTS = {
    "push-button": {
        "name": "Push Button",
        "height": 1,
        "width": "label + 4",
        "padding": "1 cell each side",
        "standard_format": "< label >",
        "default_format": "» label «",
        "activation": "Enter or Space",
        "rule": "Exactly one default button per dialog (§4.3)",
    },
    "entry-field": {
        "name": "Entry Field",
        "height": 1,
        "width": "10-60 cols",
        "padding": "1 space between label and field",
        "format": "[input____] (fill with underscore)",
        "navigation": "Arrow keys within, Tab to next field",
    },
    "toggle": {
        "name": "Toggle / Checkbox",
        "height": "1 per item",
        "indicator_width": 3,
        "gap": "1 space",
        "format_checked": "[X]",
        "format_unchecked": "[ ]",
        "activation": "Space",
        "use": "Non-mutually-exclusive boolean options",
    },
    "radio-group": {
        "name": "Radio Group",
        "height": "1 per option",
        "indicator_width": 3,
        "gap": "1 space",
        "format_selected": "(*)",
        "format_unselected": "( )",
        "navigation": "Arrow keys within group",
        "use": "Mutually exclusive, 2-5 options",
    },
    "list-box": {
        "name": "List Box",
        "height": "5-17 rows",
        "width": "20+ cols",
        "padding": "1 cell each side",
        "border": "Level 1 (single-line)",
        "focus_indicator": "▸",
        "scroll_indicators": "↑ ↓",
        "use": "Selection from 6-25 items",
    },
    "data-table": {
        "name": "Data Table",
        "height": "1 header + 1 separator + N data rows",
        "cell_padding": "1 cell each side",
        "sort_ascending": "▴",
        "sort_descending": "▾",
        "separator": "─ (full width)",
    },
    "metric-card": {
        "name": "Metric Card",
        "height": "1-3 rows",
        "layout": "icon (1-2) + gap (1) + label + gap (1) + value",
    },
    "dialog": {
        "name": "Dialog",
        "height": "7-40 rows",
        "width": "30-72 cols",
        "padding": "2 horizontal, 1 vertical",
        "border": "Level 3 (double-line ═║╔╗╚╝)",
        "shadow": "2 cols right, 1 row down",
        "title": "Centered in top border",
    },
    "menu": {
        "name": "Menu",
        "height": "1 per item + separator rows",
        "max_width": 40,
        "padding": "1 cell each side",
        "border": "Level 2 (single-line + shadow)",
        "separator": "Full-width horizontal line",
        "shortcut_alignment": "Right-aligned",
        "max_items": 10,
    },
    "spin-button": {
        "name": "Spin Button",
        "height": 1,
        "width": "value + 4",
        "padding": "1 around value",
        "format": "< value >",
        "navigation": "Arrow Up/Down to cycle",
        "max_choices": 20,
    },
    "footer": {
        "name": "Footer Key Strip",
        "height": "1-2 rows",
        "format": "F1 Help  F5 Refresh  / Filter  q Quit",
        "separator": "2+ spaces between key-action pairs",
        "rule": "MUST always be visible, MUST update with context",
    },
}


@mcp.tool()
def list_components() -> list[dict]:
    """List all component specifications available in the design system."""
    return [
        {"id": cid, "name": c["name"]}
        for cid, c in COMPONENTS.items()
    ]


@mcp.tool()
def get_component_spec(component: str) -> dict | str:
    """Get the measurement and behavior spec for a specific component.

    Args:
        component: Component identifier. One of: push-button, entry-field,
                   toggle, radio-group, list-box, data-table, metric-card,
                   dialog, menu, spin-button, footer.
    """
    spec = COMPONENTS.get(component)
    if spec is None:
        return f"Component '{component}' not found. Available: {', '.join(COMPONENTS.keys())}"
    return spec


# ---- Keyboard bindings ----------------------------------------------------

KEYBOARD_BINDINGS = {
    "tier1_global": {
        "description": "Mandatory global keys — MUST be bound in every application",
        "bindings": [
            {"action": "Help", "cua_key": "F1", "common_key": "?", "context": "Context-sensitive"},
            {"action": "Back/Cancel", "cua_key": "F3", "common_key": "Esc", "context": "Return to previous screen"},
            {"action": "Refresh", "cua_key": "F5", "common_key": "r", "context": "When no text input focused"},
            {"action": "Scroll backward", "cua_key": "F7", "common_key": "PageUp", "context": "Scrollable areas"},
            {"action": "Scroll forward", "cua_key": "F8", "common_key": "PageDown", "context": "Scrollable areas"},
            {"action": "Activate menu", "cua_key": "F10", "common_key": "Alt", "context": "Toggle action bar focus"},
            {"action": "Next field", "cua_key": None, "common_key": "Tab", "context": "LTR top-to-bottom order"},
            {"action": "Previous field", "cua_key": None, "common_key": "Shift+Tab", "context": "Reverse tab order"},
            {"action": "Confirm/activate", "cua_key": None, "common_key": "Enter", "context": "Submit form, press button"},
            {"action": "Toggle/select", "cua_key": None, "common_key": "Space", "context": "Toggles, checkboxes, radio"},
            {"action": "Navigate within control", "cua_key": None, "common_key": "Arrow keys", "context": "Within single control"},
            {"action": "Quit application", "cua_key": None, "common_key": "q", "context": "When no text input focused"},
            {"action": "Search/filter", "cua_key": None, "common_key": "/", "context": "Open filter input"},
        ],
    },
    "tier1_scrolling": {
        "description": "Scrolling keys — active in scrollable content when no text input focused",
        "bindings": [
            {"action": "Top of list", "key": "gg or Home"},
            {"action": "Bottom of list", "key": "G (Shift+G) or End"},
            {"action": "Half-page down", "key": "Ctrl+D"},
            {"action": "Half-page up", "key": "Ctrl+U"},
            {"action": "Next search result", "key": "n (after /)"},
        ],
    },
    "tier1_text_entry": {
        "description": "Text entry keys — active when text input field is focused",
        "bindings": [
            {"action": "Cut", "key": "Ctrl+X"},
            {"action": "Copy", "key": "Ctrl+C or Ctrl+Ins"},
            {"action": "Paste", "key": "Ctrl+V"},
            {"action": "Undo", "key": "Ctrl+Z"},
        ],
    },
    "tier2_common": {
        "description": "Common action keys — SHOULD bind when action exists",
        "bindings": [
            {"action": "Delete/remove", "key": "d", "case_insensitive": True},
            {"action": "Edit/modify", "key": "e", "case_insensitive": True},
            {"action": "Add/create", "key": "a", "case_insensitive": True},
            {"action": "Yank/copy value", "key": "y", "case_insensitive": True},
            {"action": "Sort", "key": "s", "case_insensitive": True},
            {"action": "Command mode", "key": ":"},
            {"action": "Suspend to background", "key": "Ctrl+Z"},
        ],
    },
    "tier3_mnemonics": {
        "description": "Screen mnemonics — application-defined, must not conflict with Tier 1/2",
        "common_patterns": [
            "1-9 for numbered screens",
            "d Dashboard, w Wizard, c Config, l Logs, m Models",
        ],
        "rules": [
            "Must not conflict with Tier 1 or Tier 2 bindings",
            "Case-insensitive (bind both cases, show lowercase in footer)",
            "Shown in footer key strip",
        ],
    },
    "key_scope_rule": (
        "Single-letter keys (q, r, /, d, e, a, s, g, n, y, Tier 3) are "
        "suppressed when text input widget is focused. Only Ctrl+, Alt+, "
        "F-keys, and Esc remain active during text entry."
    ),
}


@mcp.tool()
def get_keyboard_bindings(
    tier: Optional[str] = None,
) -> dict | str:
    """Get keyboard binding specifications.

    Args:
        tier: Optional filter. One of: tier1_global, tier1_scrolling,
              tier1_text_entry, tier2_common, tier3_mnemonics.
              If omitted, returns all tiers.
    """
    if tier is None:
        return KEYBOARD_BINDINGS
    bindings = KEYBOARD_BINDINGS.get(tier)
    if bindings is None:
        available = [k for k in KEYBOARD_BINDINGS.keys() if k != "key_scope_rule"]
        return f"Tier '{tier}' not found. Available: {', '.join(available)}"
    return bindings


# ---- Archetypes -----------------------------------------------------------

ARCHETYPES = {
    "dashboard": {
        "name": "Dashboard",
        "section": "§11.1",
        "description": "Real-time monitoring (htop, btop, system dashboards)",
        "layout": "Metric header + data table + footer",
        "components": ["Metric cards", "Data table", "Sparklines", "Status indicators"],
        "keyboard": {
            "?": "Help", "r": "Refresh", "/": "Filter", "s": "Sort",
            "q": "Quit", "1-9": "Column sort",
        },
    },
    "admin": {
        "name": "Admin / Config",
        "section": "§11.2",
        "description": "Settings and configuration panels",
        "layout": "Category sidebar + form body + footer",
        "components": ["Entry fields", "Toggles", "Radio groups", "Buttons"],
        "keyboard": {
            "Tab/Shift+Tab": "Field navigation", "Esc": "Cancel",
            "Ctrl+S": "Save", "1-9": "Jump to sidebar item",
            "[ ]": "Tab cycling",
        },
    },
    "file-manager": {
        "name": "File Manager",
        "section": "§11.3",
        "description": "File system navigation (Norton Commander, ranger)",
        "layout": "Dual-pane file lists + command line + footer",
        "components": ["File list with columns", "Path breadcrumb", "Selection markers"],
        "keyboard": {
            "Tab": "Switch panel", "Space": "Select file", "/": "Filter",
            "y": "Yank", "d": "Delete", "a": "Mkdir", "e": "Edit",
            "g": "Top", "G": "Bottom",
        },
        "fkey_overrides": {
            "F3": "View", "F4": "Edit", "F5": "Copy",
            "F6": "Move", "F7": "Mkdir", "F8": "Delete",
        },
    },
    "editor": {
        "name": "Editor",
        "section": "§11.4",
        "description": "Text editing and document manipulation",
        "layout": "Document area + status line + footer",
        "components": ["Text buffer", "Line numbers", "Status bar", "Syntax highlighting"],
        "keyboard": {
            "Ctrl+S/F2": "Save", "Ctrl+F or /": "Find",
            "Ctrl+G": "Goto line", "?/F1": "Help",
        },
        "note": "May add modal layers (vi-style normal/insert/command modes)",
    },
    "fuzzy-finder": {
        "name": "Fuzzy Finder",
        "section": "§11.5",
        "description": "Rapid search and selection (fzf, telescope, command palettes)",
        "layout": "Filter input + results list + optional preview + footer",
        "components": ["Search input", "Scored result list", "Match highlighting", "Preview pane"],
        "keyboard": {
            "type": "Type-to-filter", "Ctrl+N/↓": "Next result",
            "Ctrl+P/↑": "Prev result", "Enter": "Select",
            "Esc": "Cancel", "Ctrl+D/U": "Half-page scroll",
        },
    },
}


@mcp.tool()
def list_archetypes() -> list[dict]:
    """List all defined TUI application archetypes."""
    return [
        {"id": aid, "name": a["name"], "description": a["description"]}
        for aid, a in ARCHETYPES.items()
    ]


@mcp.tool()
def get_archetype(name: str) -> dict | str:
    """Get a specific archetype pattern with layout, components, and keyboard specs.

    Args:
        name: Archetype identifier. One of: dashboard, admin, file-manager,
              editor, fuzzy-finder.
    """
    archetype = ARCHETYPES.get(name)
    if archetype is None:
        return f"Archetype '{name}' not found. Available: {', '.join(ARCHETYPES.keys())}"
    return archetype


# ---- Widget recommendation ------------------------------------------------

WIDGET_TABLE = [
    {"data_type": "boolean", "count": "2 states", "widget": "Toggle [X]/[ ]", "key": "Space"},
    {"data_type": "exclusive", "count": "2-5 options", "widget": "Radio group (*)/( )", "key": "Arrow keys"},
    {"data_type": "exclusive", "count": "6-25 options", "widget": "List box", "key": "Arrow+Enter"},
    {"data_type": "free_text", "count": "N/A", "widget": "Entry field", "key": "Arrow/Tab"},
    {"data_type": "numeric", "count": "N/A", "widget": "Entry field + validation", "key": "Arrow/Tab"},
    {"data_type": "action", "count": "N/A", "widget": "Push button", "key": "Enter/Space"},
    {"data_type": "spin_value", "count": "<=20 choices", "widget": "Spin button", "key": "Arrow Up/Down"},
]


@mcp.tool()
def get_widget_recommendation(
    data_type: Optional[str] = None,
) -> list[dict] | str:
    """Get widget selection recommendations based on data type.

    Args:
        data_type: Optional filter. One of: boolean, exclusive, free_text,
                   numeric, action, spin_value. If omitted, returns full table.
    """
    if data_type is None:
        return WIDGET_TABLE
    matches = [w for w in WIDGET_TABLE if w["data_type"] == data_type]
    if not matches:
        types = sorted(set(w["data_type"] for w in WIDGET_TABLE))
        return f"Data type '{data_type}' not found. Available: {', '.join(types)}"
    return matches


# ---- State model -----------------------------------------------------------

@mcp.tool()
def get_state_model() -> dict:
    """Get the 7-state rendering model with SGR codes and rules."""
    return {
        "states": [
            {"state": "Enabled", "sgr": "none (Body typography)", "rule": "Default state"},
            {"state": "Focused", "sgr": "7 (reverse video) OR bracket markers [▸ item ◂]", "rule": "Exactly one element MUST hold focus at all times"},
            {"state": "Hovered", "sgr": "4 (underline) or highlight bar", "rule": "Mouse-optional"},
            {"state": "Pressed", "sgr": "Brief reverse flash (<=100ms)", "rule": "Visual feedback; revert to Focused"},
            {"state": "Selected", "sgr": "7 (reverse) + fill mark ([X] or (*))", "rule": "Multi-select and radio/checkbox"},
            {"state": "Disabled", "sgr": "2 (dim)", "rule": "Visible but non-interactive; MUST NOT be hidden"},
            {"state": "Error", "sgr": "31 (red fg) or 41 (red bg)", "rule": "MUST include explanatory text"},
        ],
        "focus_invariant": "Exactly one interactive element MUST hold focus at all times.",
        "color_independence": "Color MUST NOT be the sole indicator of any state.",
    }


# ---- Box-drawing characters ------------------------------------------------

@mcp.tool()
def get_box_drawing(
    style: Optional[str] = None,
) -> dict | str:
    """Get box-drawing character sets with Unicode codepoints.

    Args:
        style: Optional filter. One of: single, heavy, double, rounded,
               dashed, blocks, indicators. If omitted, returns all sets.
    """
    sets = {
        "single": {
            "name": "Single-Line (Light)",
            "use": "Level 1 panels, Level 2 menus, inactive windows",
            "chars": {
                "horizontal": {"glyph": "─", "unicode": "U+2500"},
                "vertical": {"glyph": "│", "unicode": "U+2502"},
                "top_left": {"glyph": "┌", "unicode": "U+250C"},
                "top_right": {"glyph": "┐", "unicode": "U+2510"},
                "bottom_left": {"glyph": "└", "unicode": "U+2514"},
                "bottom_right": {"glyph": "┘", "unicode": "U+2518"},
                "left_t": {"glyph": "├", "unicode": "U+251C"},
                "right_t": {"glyph": "┤", "unicode": "U+2524"},
                "top_t": {"glyph": "┬", "unicode": "U+252C"},
                "bottom_t": {"glyph": "┴", "unicode": "U+2534"},
                "cross": {"glyph": "┼", "unicode": "U+253C"},
            },
        },
        "heavy": {
            "name": "Heavy (Thick)",
            "use": "Optional emphasis borders, header separators",
            "chars": {
                "horizontal": {"glyph": "━", "unicode": "U+2501"},
                "vertical": {"glyph": "┃", "unicode": "U+2503"},
                "top_left": {"glyph": "┏", "unicode": "U+250F"},
                "top_right": {"glyph": "┓", "unicode": "U+2513"},
                "bottom_left": {"glyph": "┗", "unicode": "U+2517"},
                "bottom_right": {"glyph": "┛", "unicode": "U+251B"},
                "left_t": {"glyph": "┣", "unicode": "U+2523"},
                "right_t": {"glyph": "┫", "unicode": "U+252B"},
                "top_t": {"glyph": "┳", "unicode": "U+2533"},
                "bottom_t": {"glyph": "┻", "unicode": "U+253B"},
                "cross": {"glyph": "╋", "unicode": "U+254B"},
            },
        },
        "double": {
            "name": "Double-Line",
            "use": "Level 3 dialogs, Level 4 modals, active windows",
            "chars": {
                "horizontal": {"glyph": "═", "unicode": "U+2550"},
                "vertical": {"glyph": "║", "unicode": "U+2551"},
                "top_left": {"glyph": "╔", "unicode": "U+2554"},
                "top_right": {"glyph": "╗", "unicode": "U+2557"},
                "bottom_left": {"glyph": "╚", "unicode": "U+255A"},
                "bottom_right": {"glyph": "╝", "unicode": "U+255D"},
                "left_t": {"glyph": "╠", "unicode": "U+2560"},
                "right_t": {"glyph": "╣", "unicode": "U+2563"},
                "top_t": {"glyph": "╦", "unicode": "U+2566"},
                "bottom_t": {"glyph": "╩", "unicode": "U+2569"},
                "cross": {"glyph": "╬", "unicode": "U+256C"},
            },
        },
        "rounded": {
            "name": "Rounded Corners",
            "use": "Cosmetic non-interactive containers only",
            "chars": {
                "top_left": {"glyph": "╭", "unicode": "U+256D"},
                "top_right": {"glyph": "╮", "unicode": "U+256E"},
                "bottom_left": {"glyph": "╰", "unicode": "U+256F"},
                "bottom_right": {"glyph": "╯", "unicode": "U+2570"},
            },
        },
        "dashed": {
            "name": "Dashed Lines",
            "use": "Optional separators, visual grouping",
            "chars": {
                "light_triple_h": {"glyph": "┄", "unicode": "U+2504"},
                "light_triple_v": {"glyph": "┆", "unicode": "U+2506"},
                "light_quad_h": {"glyph": "┈", "unicode": "U+2508"},
                "light_quad_v": {"glyph": "┊", "unicode": "U+250A"},
                "heavy_triple_h": {"glyph": "╌", "unicode": "U+254C"},
                "heavy_triple_v": {"glyph": "╎", "unicode": "U+254E"},
            },
        },
        "blocks": {
            "name": "Block & Shade Characters",
            "use": "Progress bars, sparklines, scroll indicators, shadows",
            "chars": {
                "light_shade": {"glyph": "░", "unicode": "U+2591", "coverage": "25%"},
                "medium_shade": {"glyph": "▒", "unicode": "U+2592", "coverage": "50%"},
                "dark_shade": {"glyph": "▓", "unicode": "U+2593", "coverage": "75%"},
                "full_block": {"glyph": "█", "unicode": "U+2588", "coverage": "100%"},
                "lower_half": {"glyph": "▄", "unicode": "U+2584"},
                "upper_half": {"glyph": "▀", "unicode": "U+2580"},
                "left_half": {"glyph": "▌", "unicode": "U+258C"},
                "right_half": {"glyph": "▐", "unicode": "U+2590"},
            },
        },
        "indicators": {
            "name": "Status & Indicator Symbols",
            "use": "Status indicators, sort markers, navigation cues",
            "chars": {
                "active": {"glyph": "◉", "unicode": "U+25C9"},
                "inactive": {"glyph": "○", "unicode": "U+25CB"},
                "filled": {"glyph": "●", "unicode": "U+25CF"},
                "focus_right": {"glyph": "▸", "unicode": "U+25B8"},
                "focus_left": {"glyph": "◂", "unicode": "U+25C2"},
                "sort_asc": {"glyph": "▴", "unicode": "U+25B4"},
                "sort_desc": {"glyph": "▾", "unicode": "U+25BE"},
                "warning": {"glyph": "⚠", "unicode": "U+26A0"},
                "success": {"glyph": "✓", "unicode": "U+2713"},
                "error": {"glyph": "✗", "unicode": "U+2717"},
                "truncation": {"glyph": "⋯", "unicode": "U+22EF"},
                "scroll_up": {"glyph": "↑", "unicode": "U+2191"},
                "scroll_down": {"glyph": "↓", "unicode": "U+2193"},
            },
        },
    }

    if style is None:
        return sets
    charset = sets.get(style)
    if charset is None:
        return f"Style '{style}' not found. Available: {', '.join(sets.keys())}"
    return charset


# ---- Project template ------------------------------------------------------

@mcp.tool()
def get_project_template() -> str:
    """Get the TUI-DESIGN.template.md file for creating project-specific overrides.

    Returns the template that teams use to WAIVE, OVERRIDE, or TIGHTEN
    standard rules for their specific project.
    """
    path = CORE_DOCS["template"]
    if path.is_file():
        return path.read_text()
    return "Template file not found."


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run()
