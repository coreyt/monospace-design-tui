---
title: "Agent Reference Directive"
subtitle: "Machine-readable guide for AI agents building TUI applications"
description: "Concise directive page telling AI agents what to fetch and when from the Monospace Design TUI standard"
---

You are building a terminal user interface that conforms to the Monospace Design TUI standard. This page tells you what to fetch and when. **Do not memorize this page** — fetch the specific sections you need during each design task.

**Base URL:** `https://monospace-tui.dev`

## Setup

Check if `TUI-DESIGN.md` exists in the project root.

- **If it exists:** Read it. Note the palette name, archetypes, and any overrides (WAIVE, OVERRIDE, TIGHTEN). Note which rule IDs are affected — you will skip or modify those rules when you encounter them in fetched sections. **Do not overwrite or regenerate this file.** Proceed to [Design Workflow](#design-workflow).
- **If it does NOT exist:** Run the [First-Time Setup](#first-time-setup) wizard below to generate it.

## First-Time Setup

> **Guard:** Only run this section if `TUI-DESIGN.md` does NOT exist. If it exists, skip entirely — the user's configuration is authoritative.

Walk the user through these questions to generate their `TUI-DESIGN.md`. Ask each question interactively and wait for the user's answer before proceeding to the next.

**Step 1 — Project name:** Ask the user for the name of their project.

**Step 2 — Archetypes:** Ask which screen archetypes their project will use. Allow multiple selections.

- Dashboard — real-time monitoring, status overview
- Admin / Config — settings panels, setup wizards
- File Manager — file navigation, dual-pane operations
- Editor — text editing, document manipulation
- Fuzzy Finder — rapid search and selection from large sets

**Step 3 — Palette:** Ask which named color palette to use.

- Default — modern dark theme (recommended)
- Monochrome — no color, SGR attributes only
- Commander — white on blue (Norton Commander / OS/2 aesthetic)
- OS/2 — yellow on blue (Presentation Manager aesthetic)
- Turbo Pascal — Borland IDE aesthetic (blue editor, gray dialogs)
- Amber Phosphor — single-hue amber on black (DEC VT220)
- Green Phosphor — single-hue green on black (DEC VT100)
- Airlock — green primary with orange warning signals

**Step 4 — Framework:** Ask which TUI framework they are using.

- Textual (Python)
- curses / ncurses
- Raw ANSI escape sequences
- Other (let user specify)

**Step 5 — Minimum terminal size:** Ask for the minimum terminal size they need to support.

- 80×24 (VT100 standard — widest compatibility)
- 120×40 (recommended — full layout canvas)

**After collecting answers:** Generate `TUI-DESIGN.md` in the project root using the [template structure](https://github.com/coreyt/monospace-design-tui/blob/main/TUI-DESIGN.template.md). Fill in the Meta table with the user's answers. Set `Created` and `Last reviewed` to today's date. Leave the Overrides, Project Conventions, and Decision Log sections with their placeholder text (`_No overrides yet._`, etc.) — the user will populate these as the project evolves.

Map archetype selections to section references in the Meta table: Dashboard → `§11.1 Dashboard`, Admin/Config → `§11.2 Admin`, File Manager → `§11.3 File Manager`, Editor → `§11.4 Editor`, Fuzzy Finder → `§11.5 Fuzzy Finder`.

## Safety: Backup Before Modifying

Before modifying any existing file as part of TUI design work, back it up:

1. Create the backup directory: `.monospace-tui/_backup_YYYYMMDD-HHMMSS/` (using the current timestamp).
2. Copy each file you are about to modify into that directory, preserving its relative path from the project root.
3. Tell the user what was backed up and where.

This applies to all modifications — screen code, stylesheets, widget files, configuration. It does NOT apply to newly created files (no prior state to protect) or to the initial `TUI-DESIGN.md` generation (first-time setup creates a new file).

## Design Workflow

For each screen you build:

**Always fetch (steps 1–3):**

1. **Pick archetype** — Fetch [§11 Archetypes](/standard/archetypes/) and select Dashboard, Admin, File Manager, Editor, or Fuzzy Finder based on the user's intent.
2. **Architect layout** — Fetch [§1 Grid & Layout](/standard/layout/) for regions, footer key strip, and breakpoints.
3. **Apply color** — Fetch your palette directly: [Default](/reference/color-palette/#default), [Monochrome](/reference/color-palette/#monochrome), [Commander](/reference/color-palette/#commander), [OS/2](/reference/color-palette/#os2), [Turbo Pascal](/reference/color-palette/#turbo-pascal), [Amber Phosphor](/reference/color-palette/#amber-phosphor), [Green Phosphor](/reference/color-palette/#green-phosphor), or [Airlock](/reference/color-palette/#airlock).

**Fetch as needed (steps 4–6):**

4. **Assign keys** — Fetch [§2 Keyboard Interaction](/standard/keyboard/) when assigning key bindings. The archetype page (step 1) defines archetype-specific keys; §2 defines the base three-tier system.
5. **Select widgets** — Fetch [§4 Component Rules](/standard/components/) for the widget selection table, and [§R4 Measurements](/reference/measurements/) for exact character-cell dimensions.
6. **Check rules** — Fetch as relevant: [§5 Color](/standard/color/) (color independence), [§8 State](/standard/state/) (focus, disabled, error states), [§9 Accessibility](/standard/accessibility/) (contrast, labels).

**Then generate code.** If using Textual, see the [Textual Appendix](/textual/) for framework-specific patterns. Otherwise, apply the rules from the fetched sections directly.

## All Sections

Use these tables to find any section not covered in the workflow above.

**Standard** (design rules):

| When you need to... | Fetch |
|---------------------|-------|
| Navigation patterns, menus, action bar | [§3 Navigation Topology](/standard/navigation/) |
| Border styles, elevation levels, shadows | [§6 Border & Elevation](/standard/borders/) |
| Text treatments (bold, dim, reverse) | [§7 Typography](/standard/typography/) |
| Transition timing, progress feedback | [§10 Motion & Feedback](/standard/motion/) |

**Reference** (implementation details):

| When you need... | Fetch |
|-----------------|-------|
| Box-drawing Unicode codepoints | [§R1 Box-Drawing Characters](/reference/box-drawing/) |
| SGR escape codes for styling | [§R2 SGR Codes](/reference/sgr-codes/) |
| Full palette structure and status colors | [§R3 256-Color Palette](/reference/color-palette/) |
| Shadow and scrim rendering algorithm | [§R5 Shadow Rendering](/reference/shadows/) |
| Sparkline / progress bar encoding | [§R6 Braille Sparkline Encoding](/reference/sparklines/) |
| Terminal color detection logic | [§R7 Color Capability Detection](/reference/color-detection/) |
| Cursor, scrolling, mouse sequences | [§R8 Escape Sequences](/reference/escape-sequences/) |
| Mixed single/double border junctions | [§R9 Mixed Border Junctions](/reference/mixed-borders/) |

## Override System

Projects customize the standard through `TUI-DESIGN.md` using three actions:

- **WAIVE** — Rule acknowledged, intentionally not followed. Skip this rule during design.
- **OVERRIDE** — Rule replaced with project-specific version. Use the replacement text instead.
- **TIGHTEN** — SHOULD/MAY elevated to MUST. Treat the rule as mandatory.

Each override targets a rule ID (e.g., `§2.2`, `§R3.2`). When you fetch a section and encounter an overridden rule, apply the override from `TUI-DESIGN.md` instead.

Use the [TUI-DESIGN.md template](https://github.com/coreyt/monospace-design-tui/blob/main/TUI-DESIGN.template.md) to create a new project override file manually.
