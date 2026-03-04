---
title: "Agent Reference Directive"
subtitle: "Machine-readable guide for AI agents building TUI applications"
description: "Concise directive page telling AI agents what to fetch and when from the Monospace Design TUI standard"
---

You are building a terminal user interface that conforms to the Monospace Design TUI standard. This page tells you what to fetch and when. **Do not memorize this page** — fetch the specific sections you need during each design task.

**Base URL:** `https://coreyt.github.io/monospace-design-tui`

## Safety: Backup Before Modifying

**This rule applies to everything below.** Before modifying any existing file as part of TUI design work:

1. Create the backup directory: `.monospace-tui/_backup_YYYYMMDD-HHMMSS/` (using the current timestamp). Reuse the same backup directory within a single session.
2. Copy each file you are about to modify into that directory, preserving its relative path from the project root.
3. Tell the user what was backed up and where.

This applies to all modifications — screen code, stylesheets, widget files, configuration, and `TUI-DESIGN.md` itself. It does NOT apply to newly created files (no prior state to protect).

## Setup

Perform these checks in order:

### Step 1 — Scan for existing TUI work

Before checking `TUI-DESIGN.md`, scan the project for existing TUI-related files. Check for **all** of the following frameworks, not just the one the user intends to use:

**Textual (Python):**
- Python files importing `textual`, `curses`, `blessed`, or containing ANSI escape sequences
- `.tcss` files or inline `DEFAULT_CSS` / `CSS` class variables

**Ratatui (Rust):**
- `Cargo.toml` listing `ratatui`, `tui`, or `crossterm` as dependencies
- Rust files importing `ratatui::` or `tui::`

**Bubble Tea (Go):**
- `go.mod` listing `github.com/charmbracelet/bubbletea` or `github.com/charmbracelet/lipgloss`
- Go files importing `tea "github.com/charmbracelet/bubbletea"`

**tview (Go):**
- `go.mod` listing `github.com/rivo/tview` or `github.com/gdamore/tcell`
- Go files importing `"github.com/rivo/tview"`

**Ink (Node.js / TypeScript):**
- `package.json` listing `ink`, `blessed`, or `neo-blessed` as dependencies
- JS/TS files importing `ink` or `blessed`

**Also check for:**
- Design documents (e.g., `tui-architect.md`, `tui-review.md`, or similar in `.agents/`, `docs/`, or project root)
- Existing `TUI-DESIGN.md`

Note what you find — framework(s) detected, number of TUI-related files, any design documents. You will need this inventory in the next step.

### Step 2 — Route based on project state

**State A — No `TUI-DESIGN.md`, no existing TUI files:** Greenfield project. Run [First-Time Setup](#first-time-setup).

**State B — No `TUI-DESIGN.md`, but existing TUI files found:** Existing project adopting the standard. Tell the user what you found (number of screen files, widget files, CSS, design docs). Then ask:

> This project already has TUI code. Do you want to:
> 1. **Adopt** — Generate a TUI-DESIGN.md that reflects the existing project (I'll pre-fill archetypes and framework from what I found)
> 2. **Redesign** — Generate a fresh TUI-DESIGN.md and redesign screens to comply with the standard (existing files will be backed up before any changes)
> 3. **Cancel** — Stop and let you set things up manually

If **Adopt**: Run the wizard but pre-fill answers from the scan (detected framework, inferred archetypes from screen patterns). Let the user confirm or change each answer. Generate `TUI-DESIGN.md`.

If **Redesign**: Back up all existing TUI files first (see Safety rule above). Then run the wizard, pre-filling answers from the scan (detected framework, inferred archetypes) so the user can confirm or change each one. Generate `TUI-DESIGN.md`.

If **Cancel**: Stop. Do not generate any files.

**State C — `TUI-DESIGN.md` exists:** Read it. Note the palette name, archetypes, and any overrides (WAIVE, OVERRIDE, TIGHTEN). Note which rule IDs are affected — you will skip or modify those rules when you encounter them in fetched sections. Proceed to [Design Workflow](#design-workflow).

If the user explicitly asks to redo or reinitialize their TUI setup, back up the existing `TUI-DESIGN.md` (see Safety rule), then run the wizard. Otherwise, **never overwrite or regenerate `TUI-DESIGN.md` without being asked.**

## First-Time Setup

Walk the user through these questions to generate their `TUI-DESIGN.md`. Ask each question interactively and wait for the user's answer before proceeding to the next. If you detected existing TUI work (State B — Adopt or Redesign), pre-fill suggested answers from the scan (detected framework, inferred archetypes from screen patterns) and let the user confirm or change each one.

**Step 1 — Project name:** Ask the user for the name of their project.

**Step 2 — Archetypes:** Ask which screen archetypes their project will use. Allow multiple selections. If you scanned existing code, pre-select archetypes that match the screens you found and list which screens mapped to which archetype. If any existing screens don't map cleanly to an archetype, mention them and ask the user how to classify them.

- Dashboard — real-time monitoring, status overview
- Admin / Config — settings panels, setup wizards
- File Manager — file navigation, dual-pane operations
- Editor — text editing, document manipulation
- Fuzzy Finder — rapid search and selection from large sets

**Step 3 — Palette:** Ask which named color palette to use. Tell the user this can be changed later by editing the `Palette` field in `TUI-DESIGN.md`.

- Default — modern dark theme (recommended)
- Monochrome — no color, SGR attributes only
- Commander — white on blue (Norton Commander / OS/2 aesthetic)
- OS/2 — yellow on blue (Presentation Manager aesthetic)
- Turbo Pascal — Borland IDE aesthetic (blue editor, gray dialogs)
- Amber Phosphor — single-hue amber on black (DEC VT220)
- Green Phosphor — single-hue green on black (DEC VT100)
- Airlock — green primary with orange warning signals

**Step 4 — Framework:** Ask which TUI framework they are using. Pre-fill from the scan if a framework was detected.

- Textual (Python)
- Ratatui (Rust)
- Bubble Tea (Go)
- tview (Go)
- Ink (Node.js / TypeScript)
- curses / ncurses
- Raw ANSI escape sequences
- Other (let user specify)

**Important:** The design standard applies to all frameworks. However, automated implementation support (code generation, TCSS patterns, the [Textual Appendix](/textual/)) is currently only available for **Textual**. For other frameworks, you can still generate `TUI-DESIGN.md`, guide layout and keyboard decisions, and apply all design rules — but code generation must follow the framework's own idioms rather than Textual-specific patterns.

**Step 5 — Minimum terminal size:** Ask for the minimum terminal size they need to support. This determines layout breakpoints and whether the full three-region layout is available.

- 80×24 (VT100 standard — widest compatibility)
- 120×40 (recommended — full layout canvas)

**After collecting answers:** Fetch the [TUI-DESIGN.md template](https://raw.githubusercontent.com/coreyt/monospace-design-tui/main/TUI-DESIGN.template.md) and generate `TUI-DESIGN.md` in the project root. Fill in the Meta table with the user's answers. Set `Created` and `Last reviewed` to today's date. Leave the Overrides, Project Conventions, and Decision Log sections with their placeholder text (`_No overrides yet._`, etc.) — the user will populate these as the project evolves.

Map archetype selections to section references in the Meta table: Dashboard → `§11.1 Dashboard`, Admin/Config → `§11.2 Admin`, File Manager → `§11.3 File Manager`, Editor → `§11.4 Editor`, Fuzzy Finder → `§11.5 Fuzzy Finder`.

**After generating `TUI-DESIGN.md`:**

- **State A (greenfield) or State B — Adopt:** Stop. Tell the user the file was created and summarize the choices. Do not proceed to the Design Workflow unless the user asks you to design a screen.
- **State B — Redesign:** The existing TUI files have been backed up and the project needs new screens. Tell the user `TUI-DESIGN.md` was created, summarize the choices, then proceed to the [Design Workflow](#design-workflow) to build replacement screens for each archetype selected. Work through one screen at a time — show the user your design for each screen and get confirmation before generating code.

## Discipline: Follow This Directive Exactly

**This rule applies to everything on this page.**

1. **Only fetch URLs listed on this page.** Every URL you need is provided in this directive — the section tables, the palette links, the template link. If a URL is not on this page, do not fetch it. If a link returns a 404 or error, **stop and tell the user** — do not guess alternative URLs, do not try raw.githubusercontent.com variants, do not search for the content elsewhere.

2. **Do not explore or improvise.** If you find yourself scanning the website for pages, following links from fetched pages to other pages, or fetching the monolithic source files from the repository — stop. You are off-track. Return to this directive and find the correct section link.

3. **Stop on uncertainty.** If you are unsure which archetype applies, which section to fetch, or how to interpret a rule, stop and ask the user. Do not make assumptions and push forward.

4. **One step at a time.** After completing any discrete step (setup, backup, generating a file, designing a screen), tell the user what you did. Do not chain steps together without the user's go-ahead.

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

**Then generate code.** If using Textual, see the [Textual Appendix](/textual/) for TCSS patterns, widget mapping, async rules, and a working example. For Ratatui, Bubble Tea, tview, Ink, or other frameworks, apply the design rules from the fetched sections directly using your framework's idioms.

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
