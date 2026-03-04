---
title: "Agent Reference Directive"
subtitle: "Machine-readable guide for AI agents building TUI applications"
description: "Concise directive page telling AI agents what to fetch and when from the Monospace Design TUI standard"
---

You are building a terminal user interface that conforms to the Monospace Design TUI standard. This page tells you what to fetch and when. **Do not memorize this page** — fetch specific sections as needed.

**Base URL:** `https://coreyt.github.io/monospace-design-tui`

**Raw content:** If your fetch tool summarizes or truncates content, use raw markdown URLs instead of HTML pages. This directive as raw markdown: `https://raw.githubusercontent.com/coreyt/monospace-design-tui/main/website/content/agent-ref/_index.md`

For any section link on this page, construct the raw URL with this pattern:

| Page link | Raw URL |
|-----------|---------|
| `/standard/{page}/` | `https://raw.githubusercontent.com/coreyt/monospace-design-tui/main/website/content/standard/{page}.md` |
| `/reference/{page}/` | `https://raw.githubusercontent.com/coreyt/monospace-design-tui/main/website/content/reference/{page}.md` |
| `/textual/` | `https://raw.githubusercontent.com/coreyt/monospace-design-tui/main/website/content/textual/_index.md` |

Example: `/standard/layout/` → `https://raw.githubusercontent.com/coreyt/monospace-design-tui/main/website/content/standard/layout.md`

---

## Discipline

**These rules govern everything on this page.**

1. **Fresh start.** Every time you fetch this directive, treat it as a fresh start. Do not reuse answers, context, or state from previous runs — even within the same session. Always re-scan and re-ask. If `.monospace-tui/cache/` exists from a previous run, delete it before proceeding.
2. **Listed URLs only.** Every URL you need is on this page or constructable from the raw URL pattern above. Do not fetch other URLs. On 404 or error, stop and tell the user.
3. **No exploring.** Do not scan the website, follow links from fetched pages, or fetch monolithic source files from the repository. Do not use `curl`, shell commands, or HTML scraping to work around fetch limitations — use the raw URL pattern instead. If you catch yourself doing any of this, stop and return to this directive.
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

- **Adopt**: Run wizard with pre-filled answers from scan. Generate `TUI-DESIGN.md`. [Build cache](#build-local-cache). Stop.
- **Redesign**: Back up all TUI files (Safety rule). Run wizard with pre-filled answers. Generate `TUI-DESIGN.md`. [Build cache](#build-local-cache). Proceed to [Design Workflow](#design-workflow).
- **Cancel**: Stop.

**State C — `TUI-DESIGN.md` exists:** Read it. Note palette, archetypes, overrides (WAIVE/OVERRIDE/TIGHTEN). [Build cache](#build-local-cache) if `.monospace-tui/cache/` does not exist. Proceed to [Design Workflow](#design-workflow).

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

**After generating:** Tell the user the file was created and summarize choices. For **Redesign**, proceed to Build Local Cache then Design Workflow. For **Greenfield/Adopt**, build cache then stop unless the user asks to design a screen.

---

## Build Local Cache

After setup completes (or on State C entry when no cache exists), fetch and save the sections the project needs to `.monospace-tui/cache/`. This eliminates repeated network fetches, avoids content summarization, and survives context compaction.

**Always cache:**

| File | Source |
|------|--------|
| `directive.md` | This page (raw URL) |
| `layout.md` | [§1 Grid & Layout](/standard/layout/) |
| `keyboard.md` | [§2 Keyboard Interaction](/standard/keyboard/) |

**Cache based on `TUI-DESIGN.md` selections:**

| If project uses... | File | Source |
|---------------------|------|--------|
| Dashboard archetype | `archetype-dashboard.md` | [§11 Archetypes](/standard/archetypes/) — extract §11.1 only |
| Admin archetype | `archetype-admin.md` | [§11 Archetypes](/standard/archetypes/) — extract §11.2 only |
| File Manager archetype | `archetype-filemanager.md` | [§11 Archetypes](/standard/archetypes/) — extract §11.3 only |
| Editor archetype | `archetype-editor.md` | [§11 Archetypes](/standard/archetypes/) — extract §11.4 only |
| Fuzzy Finder archetype | `archetype-fuzzyfinder.md` | [§11 Archetypes](/standard/archetypes/) — extract §11.5 only |
| Default palette | `palette.md` | [§R3 Color Palette](/reference/color-palette/) — extract Default section only |
| Monochrome palette | `palette.md` | Same source — extract Monochrome section only |
| Commander palette | `palette.md` | Same source — extract Commander section only |
| *(same pattern for OS/2, Turbo Pascal, Amber Phosphor, Green Phosphor, Airlock)* | | |
| Textual framework | `textual.md` | [Textual Appendix](/textual/) |

Fetch the full source page once, extract only the relevant section, and save that to the cache file. This keeps each cached file small and focused.

**After caching:** Tell the user what was cached and where. The cache is at `.monospace-tui/cache/`.

---

## Design Workflow

**Before each screen:** Re-read `.monospace-tui/cache/directive.md` and `TUI-DESIGN.md`. This resets your grounding and prevents drift across multiple screens. Do not re-fetch from the network — use the cache.

For each screen you build:

**Read from cache (steps 1–3):**

1. **Pick archetype** — Read the cached archetype file (e.g., `.monospace-tui/cache/archetype-dashboard.md`).
2. **Architect layout** — Read `.monospace-tui/cache/layout.md`.
3. **Apply color** — Read `.monospace-tui/cache/palette.md`.

**Fetch as needed (steps 4–6) — check cache first, fetch and cache if missing:**

4. **Assign keys** — Read `.monospace-tui/cache/keyboard.md`.
5. **Select widgets** — Fetch [§4 Component Rules](/standard/components/) + [§R4 Measurements](/reference/measurements/) if not cached. Save to cache.
6. **Check rules** — Fetch as relevant: [§5 Color](/standard/color/), [§8 State](/standard/state/), [§9 Accessibility](/standard/accessibility/). Save to cache.

**Generate code.** Textual: read `.monospace-tui/cache/textual.md`. Other frameworks: apply rules using framework idioms.

### Per-Screen Checklist

Verify after generating code. Tell the user the result. Fix failures before the next screen.

- [ ] **Archetype** — follows selected archetype's layout and regions
- [ ] **Layout** — header, body, footer present; footer key strip visible
- [ ] **Palette** — only named palette colors; no hardcoded values
- [ ] **Keyboard** — Tier 1 keys bound; archetype keys assigned; no conflicts
- [ ] **Color independence** — info conveyed by color also conveyed by text/shape/position
- [ ] **Overrides** — WAIVE/OVERRIDE/TIGHTEN from `TUI-DESIGN.md` applied

---

## Cleanup

When the design session is complete (all screens built, or user says to stop), delete `.monospace-tui/cache/`. The cache is ephemeral — it exists only to support the current session. Tell the user the cache was removed.

The `.monospace-tui/_backup_*/` directories are **not** deleted — those are the user's safety net.

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

Each override targets a rule ID (e.g., `§2.2`, `§R3.2`). When reading a cached section, apply overrides from `TUI-DESIGN.md` instead of the original rule.

Template: [TUI-DESIGN.md](https://raw.githubusercontent.com/coreyt/monospace-design-tui/main/TUI-DESIGN.template.md)
