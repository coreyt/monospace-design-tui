---
title: "Agent Reference Directive"
subtitle: "Machine-readable guide for AI agents building TUI applications"
description: "Concise directive page telling AI agents what to fetch and when from the Monospace Design TUI standard"
---

You are building a terminal user interface that conforms to the Monospace Design TUI standard. This page tells you what to fetch and when. **Do not memorize this page** — fetch specific sections as needed.

**Base URL:** `https://coreyt.github.io/monospace-design-tui`

**If your fetch tool summarizes or truncates this page**, fetch the raw markdown instead: `https://raw.githubusercontent.com/coreyt/monospace-design-tui/main/website/content/agent-ref/_index.md`

---

## Discipline

**These rules govern everything on this page.**

1. **Fresh start.** Every time you fetch this directive, treat it as a fresh start. Do not reuse answers, context, or state from previous runs — even within the same session. Always re-scan and re-ask.
2. **Listed URLs only.** Every URL you need is on this page. Do not fetch URLs not listed here. On 404 or error, stop and tell the user.
3. **No exploring.** Do not scan the website, follow links from fetched pages, or fetch monolithic source files from the repository. If you catch yourself doing this, stop and return to this directive.
4. **Stop on uncertainty.** If unsure which archetype, section, or rule applies, ask the user.
5. **One step at a time.** After each discrete step, tell the user what you did. Do not chain steps without their go-ahead.

---

## Safety: Backup Before Modifying

Before modifying any existing file as part of TUI design work:

1. Create `.monospace-tui/_backup_YYYYMMDD-HHMMSS/` (current timestamp). Reuse within a session.
2. Copy each file into that directory, preserving its relative path.
3. Tell the user what was backed up and where.

Applies to all modifications (code, stylesheets, config, `TUI-DESIGN.md`). Does NOT apply to newly created files.

---

## Setup

### Step 1 — Scan for existing TUI work

Scan the project for TUI-related files across all frameworks:

| Framework | Look for |
|-----------|----------|
| Textual (Python) | Imports of `textual`, `curses`, `blessed`; `.tcss` files; `DEFAULT_CSS` / `CSS` class variables |
| Ratatui (Rust) | `Cargo.toml` with `ratatui`, `tui`, or `crossterm`; `ratatui::` imports |
| Bubble Tea (Go) | `go.mod` with `charmbracelet/bubbletea` or `lipgloss`; Go imports |
| tview (Go) | `go.mod` with `rivo/tview` or `gdamore/tcell`; Go imports |
| Ink (Node.js/TS) | `package.json` with `ink`, `blessed`, or `neo-blessed`; JS/TS imports |

Also check for: design documents (`tui-architect.md`, `tui-review.md`, or similar in `.agents/`, `docs/`, project root) and existing `TUI-DESIGN.md`.

Note what you find — framework(s), file count, design docs. You need this in Step 2.

### Step 2 — Route based on project state

**State A — No `TUI-DESIGN.md`, no TUI files:** Greenfield. Run [First-Time Setup](#first-time-setup).

**State B — No `TUI-DESIGN.md`, TUI files found:** Tell the user what you found (framework, file count, design docs). Ask:

> This project already has TUI code. Do you want to:
> 1. **Adopt** — Generate a TUI-DESIGN.md reflecting the existing project (I'll pre-fill from what I found)
> 2. **Redesign** — Back up existing files, generate a fresh TUI-DESIGN.md, then build new screens
> 3. **Cancel** — Stop

- **Adopt**: Run wizard with pre-filled answers from scan. Generate `TUI-DESIGN.md`. Stop.
- **Redesign**: Back up all TUI files (Safety rule). Run wizard with pre-filled answers. Generate `TUI-DESIGN.md`. Then proceed to [Design Workflow](#design-workflow) to build replacement screens.
- **Cancel**: Stop.

**State C — `TUI-DESIGN.md` exists:** Read it. Note palette, archetypes, overrides (WAIVE/OVERRIDE/TIGHTEN). Proceed to [Design Workflow](#design-workflow).

To redo setup: user must explicitly ask. Back up existing `TUI-DESIGN.md` first. Never overwrite without being asked.

---

## First-Time Setup

Ask each question interactively — wait for the answer before proceeding. If existing TUI work was detected (State B), pre-fill from scan results and let the user confirm or change.

**Step 1 — Project name.**

**Step 2 — Archetypes.** Multiple selections allowed. If scan found screens, pre-select matching archetypes and show which screens mapped to each. Mention any screens that don't map cleanly and ask how to classify them.

- Dashboard — real-time monitoring, status overview
- Admin / Config — settings panels, setup wizards
- File Manager — file navigation, dual-pane operations
- Editor — text editing, document manipulation
- Fuzzy Finder — rapid search and selection from large sets

**Step 3 — Palette.** Can be changed later by editing `TUI-DESIGN.md`.

- Default (recommended), Monochrome, Commander, OS/2, Turbo Pascal, Amber Phosphor, Green Phosphor, Airlock

**Step 4 — Framework.** Pre-fill from scan if detected.

- Textual (Python), Ratatui (Rust), Bubble Tea (Go), tview (Go), Ink (Node.js/TS), curses/ncurses, raw ANSI, other

The design standard applies to all frameworks. Automated implementation support (code generation, the [Textual Appendix](/textual/)) is currently **Textual-only**. For other frameworks, `TUI-DESIGN.md` and design rules still apply — code generation uses the framework's own idioms.

**Step 5 — Minimum terminal size.** Determines layout breakpoints and three-region availability.

- 80×24 (VT100 standard) or 120×40 (recommended)

**Generate `TUI-DESIGN.md`:** Fetch the [template](https://raw.githubusercontent.com/coreyt/monospace-design-tui/main/TUI-DESIGN.template.md). Fill in Meta table. Set dates to today. Leave Overrides/Conventions/Decision Log as placeholders.

Archetype mapping: Dashboard → `§11.1`, Admin/Config → `§11.2`, File Manager → `§11.3`, Editor → `§11.4`, Fuzzy Finder → `§11.5`.

**After generating:** Tell the user the file was created and summarize choices. For **Redesign**, proceed to Design Workflow. For **Greenfield/Adopt**, stop unless the user asks to design a screen.

---

## Design Workflow

**Before each screen:** Re-fetch this directive page. Re-read `TUI-DESIGN.md`. This prevents drift across multiple screens.

**Always fetch (steps 1–3):**

1. **Pick archetype** — Fetch [§11 Archetypes](/standard/archetypes/).
2. **Architect layout** — Fetch [§1 Grid & Layout](/standard/layout/).
3. **Apply color** — Fetch your palette: [Default](/reference/color-palette/#default), [Monochrome](/reference/color-palette/#monochrome), [Commander](/reference/color-palette/#commander), [OS/2](/reference/color-palette/#os2), [Turbo Pascal](/reference/color-palette/#turbo-pascal), [Amber Phosphor](/reference/color-palette/#amber-phosphor), [Green Phosphor](/reference/color-palette/#green-phosphor), [Airlock](/reference/color-palette/#airlock).

**Fetch as needed (steps 4–6):**

4. **Assign keys** — [§2 Keyboard Interaction](/standard/keyboard/) for the base three-tier system. Archetype page (step 1) has archetype-specific keys.
5. **Select widgets** — [§4 Component Rules](/standard/components/) + [§R4 Measurements](/reference/measurements/).
6. **Check rules** — [§5 Color](/standard/color/) (independence), [§8 State](/standard/state/) (focus/disabled/error), [§9 Accessibility](/standard/accessibility/) (contrast/labels).

**Generate code.** Textual: see [Textual Appendix](/textual/). Other frameworks: apply rules using framework idioms.

### Per-Screen Checklist

Verify after generating code. Tell the user the result. Fix failures before the next screen.

- [ ] **Archetype** — follows selected archetype's layout and regions
- [ ] **Layout** — header, body, footer present; footer key strip visible
- [ ] **Palette** — only named palette colors; no hardcoded values
- [ ] **Keyboard** — Tier 1 keys bound; archetype keys assigned; no conflicts
- [ ] **Color independence** — info conveyed by color also conveyed by text/shape/position
- [ ] **Overrides** — WAIVE/OVERRIDE/TIGHTEN from `TUI-DESIGN.md` applied

---

## All Sections

**Standard** (design rules):

| When you need... | Fetch |
|------------------|-------|
| Navigation, menus, action bar | [§3 Navigation Topology](/standard/navigation/) |
| Borders, elevation, shadows | [§6 Border & Elevation](/standard/borders/) |
| Text treatments (bold, dim, reverse) | [§7 Typography](/standard/typography/) |
| Transitions, progress feedback | [§10 Motion & Feedback](/standard/motion/) |

**Reference** (implementation details):

| When you need... | Fetch |
|------------------|-------|
| Box-drawing Unicode codepoints | [§R1 Box-Drawing Characters](/reference/box-drawing/) |
| SGR escape codes | [§R2 SGR Codes](/reference/sgr-codes/) |
| Full palette + status colors | [§R3 256-Color Palette](/reference/color-palette/) |
| Shadow/scrim rendering | [§R5 Shadow Rendering](/reference/shadows/) |
| Sparkline/progress encoding | [§R6 Braille Sparkline Encoding](/reference/sparklines/) |
| Color detection logic | [§R7 Color Capability Detection](/reference/color-detection/) |
| Cursor, scrolling, mouse | [§R8 Escape Sequences](/reference/escape-sequences/) |
| Mixed border junctions | [§R9 Mixed Border Junctions](/reference/mixed-borders/) |

---

## Override System

Projects customize the standard through `TUI-DESIGN.md`:

- **WAIVE** — Rule skipped intentionally. Do not enforce during design.
- **OVERRIDE** — Rule replaced. Use the replacement text.
- **TIGHTEN** — SHOULD/MAY elevated to MUST. Treat as mandatory.

Each override targets a rule ID (e.g., `§2.2`, `§R3.2`). When fetching a section, apply overrides from `TUI-DESIGN.md` instead of the original rule.

Template: [TUI-DESIGN.md](https://raw.githubusercontent.com/coreyt/monospace-design-tui/main/TUI-DESIGN.template.md)
