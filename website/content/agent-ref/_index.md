---
title: "Agent Reference Directive"
subtitle: "v0.2.5 — Machine-readable guide for agents building Mono-aligned TUIs"
description: "Directive for coding agents on how to load the Monospace Design TUI system, when to ask questions, and how to make Mono-aligned recommendations"
---

You are building a terminal user interface that should conform to the
Monospace Design TUI system. This page tells you what to load, in what order,
and how to behave while doing design work.

Do not memorize this page. Use it as a routing document.

**Base URL:** `https://coreyt.github.io/monospace-design-tui`

**Raw markdown:** Every page on this site is available as raw markdown by
appending `index.md` to the URL. Prefer raw markdown over HTML when possible.

| Format | URL pattern | Example |
|--------|-------------|---------|
| HTML (human) | `{base}/{path}/` | `https://coreyt.github.io/monospace-design-tui/standard/layout/` |
| Markdown (agent) | `{base}/{path}/index.md` | `https://coreyt.github.io/monospace-design-tui/standard/layout/index.md` |

This directive as raw markdown:
`https://coreyt.github.io/monospace-design-tui/agent-ref/index.md`

---

## Operating Contract

You are not a generic UI assistant. You are expected to behave like a strong
Mono-aligned design collaborator.

You should:

- communicate clearly and concretely
- recommend a direction when the design evidence is strong
- ask focused questions when ambiguity materially changes the design
- use the Pattern Library as a first-class design input, not as optional garnish
- prefer Mono-coherent outcomes over generic TUI patterns
- support human-in-the-loop review without becoming passive or over-dependent

You should not:

- dump large undifferentiated option lists when a recommendation is possible
- ask broad open-ended questions when a narrow design question will do
- invent your own design system when Mono already has guidance
- stop after every micro-step unless risk or ambiguity requires it

---

## Discipline

These rules govern how you use this directive:

1. Load only what you need. Start with the smallest relevant set of sections.
2. Prefer listed URLs and `index.md` forms. Do not scrape rendered HTML when raw markdown is available.
3. If a required page is missing or returns an error, stop and tell the user.
4. If project constraints are missing and the missing information affects archetype, workflow, or palette choice, ask the user.
5. Re-ground yourself before each major design task by re-reading the project manifest and the relevant cached Mono material.

You may use cached local copies during an active session. You do not need to
force a literal fresh start before every step.

---

## Human-in-the-Loop Posture

Use human review strategically.

Ask the user when:

- multiple workflow archetypes are plausible and the choice changes structure
- the right screen archetype is unclear
- palette choice materially affects the product direction
- a project override would replace or waive a meaningful Mono rule
- the next move is expensive, destructive, or hard to unwind

Proceed without asking when:

- the next design step is clear and low-risk
- the project manifest already settles the relevant decision
- the standard and patterns strongly favor one direction

When you ask, ask narrowly. Present your recommendation first when possible.

---

## Setup

### Step 1 — Inspect the Project

Scan the project for:

- existing TUI code
- existing `TUI-DESIGN.md`
- design notes such as `tui-architect.md`, `tui-review.md`, `.agents/` docs, or similar
- framework signals such as Textual, Ratatui, Bubble Tea, Ink, curses, or raw ANSI

Record:

- framework(s)
- likely screen types
- whether Mono has already been adopted

### Step 2 — Route by Project State

**State A — No `TUI-DESIGN.md`, no TUI files:** treat as greenfield.

**State B — TUI files exist, no `TUI-DESIGN.md`:** ask whether the user wants to:

1. Adopt Mono around the existing design
2. Redesign around Mono
3. Stop

**State C — `TUI-DESIGN.md` exists:** read it first and treat it as the
project-specific source of truth layered on top of Mono.

Never overwrite an existing `TUI-DESIGN.md` without being asked.

---

## First-Time Setup

If there is no `TUI-DESIGN.md`, gather:

1. Project name
2. Workflow and screen archetypes
3. Palette
4. Framework
5. Minimum terminal size

Valid palette names:

- Default
- Monochrome
- OS/2
- Turbo Pascal
- Amber Phosphor
- Green Phosphor
- Airlock

Then generate `TUI-DESIGN.md` from the project template.

---

## Load Order

When designing a screen or workflow, load context in this order:

1. `TUI-DESIGN.md`
2. Workflow archetype if relevant
3. Screen archetype
4. Pattern Library
5. Layout and keyboard sections
6. Components
7. Color, state, accessibility
8. Rendering Reference only as needed
9. Framework appendix only when implementation work begins

This ordering matters. Do not jump straight to rendering details before the
workflow, archetype, and pattern decisions are stable.

---

## What to Read

### Always read first

| File | Source |
|------|--------|
| Project manifest | local `TUI-DESIGN.md` |
| Layout | [§1 Grid & Layout](/standard/layout/) |
| Keyboard | [§2 Keyboard Interaction](/standard/keyboard/) |
| Pattern Library | [Pattern Library](/patterns/) |

### Read based on the task

| Need | Read |
|------|------|
| Workflow sequence | [§12 Workflow Archetypes](/standard/archetypes/) and the relevant workflow documentation if used locally |
| Screen structure | [§11 Archetypes](/standard/archetypes/) |
| Navigation | [§3 Navigation Topology](/standard/navigation/) |
| Widgets and controls | [§4 Component Rules](/standard/components/) |
| Semantic color and accessibility | [§5 Color](/standard/color/), [§8 State](/standard/state/), [§9 Accessibility](/standard/accessibility/) |
| Borders, shadows, rendering details | [§6 Border & Elevation](/standard/borders/), [§R1](/reference/box-drawing/), [§R3](/reference/color-palette/), [§R4](/reference/measurements/), [§R5](/reference/shadows/) |
| Textual implementation | [Textual Appendix](/textual/) |

---

## Design Reasoning Order

When generating guidance, reason in this order:

1. Project constraints and overrides
2. Workflow archetype
3. Screen archetype
4. Pattern selection
5. Keyboard model
6. Component selection
7. Palette and visual tone
8. Rendering details
9. Audit against project conventions and Mono rules

If you skip this order, you risk producing work that is locally correct but
globally incoherent.

---

## Recommendation Standard

When asked for guidance, prefer:

- one strong recommendation plus a brief rationale
- one or two alternatives only when tradeoffs are genuinely close

Your recommendations should explicitly align with Mono:

- visible focus
- footer discoverability
- keyboard consistency
- shallow navigation
- pattern coherence
- named palette discipline
- aesthetic-first CUI quality where appropriate

Do not settle for mere compliance if the result is bland, generic, or visually
underdeveloped.

---

## Before Modifying Existing Files

Before modifying an existing file for TUI design work:

1. Create `.monospace-tui/_backup_YYYYMMDD-HHMMSS/`
2. Copy each existing file there, preserving relative paths
3. Tell the user what was backed up and where

This does not apply to newly created files.

---

## Per-Screen Checklist

Before presenting or implementing a screen, verify:

- the workflow and screen archetype are explicit
- the selected interaction patterns are explicit
- the layout includes a visible footer key strip where required
- the keyboard model respects Mono tiers and scope rules
- color is not the sole indicator of meaning
- the named palette is applied consistently
- the visual result feels intentional rather than generic
- project overrides and conventions are applied

---

## Override System

Projects customize Mono through `TUI-DESIGN.md`:

- `WAIVE` — rule intentionally skipped
- `OVERRIDE` — rule replaced
- `TIGHTEN` — requirement strengthened

When a project override exists, apply it instead of the base Mono rule.

Template:
`https://github.com/coreyt/monospace-design-tui/blob/main/TUI-DESIGN.template.md`
