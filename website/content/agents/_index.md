---
title: "Working with AI Agents"
subtitle: "Three tiers of adoption for AI-assisted TUI development"
description: "How AI coding agents can use the Monospace Design TUI standard — from a one-line snippet to full Claude Code skills"
---

A design standard is only useful if it's applied. Monospace Design TUI was built with the expectation that developers would use AI coding agents as collaborators — and that those agents need structured, machine-readable standards to follow.

There are three tiers of adoption, from lightweight to full integration.

---

## Tier 1: CLAUDE.md Snippet

The simplest adoption path. Add two lines to your project's `CLAUDE.md` (or equivalent agent instructions file):

```
When building TUI screens, follow the Monospace Design TUI standard.
Fetch the agent directive (raw markdown) at:
  https://raw.githubusercontent.com/coreyt/monospace-design-tui/main/website/content/agent-ref/_index.md
Use the "Default" palette (or substitute your chosen palette name).
```

This gives any AI agent enough context to fetch the [Agent Reference Directive](/agent-ref/), which links to every section of the standard. The agent fetches only the sections it needs for the current task.

**Valid palette names:** Default, Monochrome, Commander, OS/2, Turbo Pascal, Amber Phosphor, Green Phosphor, Airlock

---

## Tier 2: TUI-DESIGN.md

For projects that need palette customization and rule overrides, create a `TUI-DESIGN.md` in your project root using the [template](https://github.com/coreyt/monospace-design-tui/blob/main/TUI-DESIGN.template.md).

The file declares:
- Which archetypes your project uses
- Which palette to apply
- Any rule overrides (WAIVE, OVERRIDE, TIGHTEN)
- Project-specific conventions beyond the standard

AI agents read this file before designing screens, applying your project's customizations on top of the base standard. The audit skill checks compliance against both the standard and your overrides.

---

## Tier 3: Claude Code Skills

The deepest integration. The Monospace Design TUI project includes two [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skills that give AI agents direct access to the standard.

### mono-tui-design

The design skill handles the creative work: planning layouts, selecting widgets, assigning keyboard bindings, and generating implementation code.

**When it activates:** Layout planning, widget selection, wireframe creation, or writing Textual code for terminal interfaces.

**What it does:**

1. **Loads context** — Reads the project's `TUI-DESIGN.md` for overrides and conventions, then loads relevant sections of the design standard.
2. **Analyzes intent** — Determines which archetype (Dashboard, Admin, File Manager, Editor, Fuzzy Finder) matches the user's goal.
3. **Architects** — Proposes a design with ASCII wireframes, region layout, widget selection rationale, keyboard bindings across all three tiers, and color/state assignments.
4. **Self-critiques** — Checks the design against common violations: frozen UI, mouse traps, navigation mazes, invisible focus, missing footer keys, case-sensitivity errors, F-key dependencies.
5. **Generates code** — Produces framework-specific implementation (Textual TCSS, Python widgets, key bindings with the `ci()` helper).

**Invoke with:** `/mono-tui-design`

### mono-tui-audit

The audit skill handles compliance checking. It reads your TUI code and produces a structured pass/fail report against the full standard.

**When it activates:** After building or modifying TUI screens, when you want to verify compliance.

**What it does:**

1. **Builds the effective ruleset** — Merges the standard's rules with your project's `TUI-DESIGN.md` overrides (WAIVE, OVERRIDE, TIGHTEN).
2. **Scans code** — Checks statically verifiable rules (key bindings, widget choices, footer presence, color independence, async patterns) and flags rules that require manual verification (contrast ratios, focus visibility, transition timing).
3. **Detects staleness** — Compares override text against the current standard. If the standard has changed since an override was written, it flags the override for review without invalidating it.
4. **Produces a structured report** — Every rule gets a status: PASS, FAIL, WAIVED, OVERRIDDEN, TIGHTENED, STALE, MANUAL, or N/A. Violations include the rule text, finding, file location, and a specific fix recommendation.

**Invoke with:** `/mono-tui-audit`

---

## How It Fits Together

The typical workflow:

1. **Tier 1:** Add the snippet to your `CLAUDE.md` — agents can immediately start designing compliant TUIs.
2. **Tier 2:** Create a `TUI-DESIGN.md` when you need to lock in a palette, declare archetypes, or override rules.
3. **Tier 3:** Clone the repository to get the Claude Code skills for full design/audit integration.

The standard is the source of truth. The [agent directive](/agent-ref/) is how agents discover it. The `TUI-DESIGN.md` is how your project customizes it. The skills are the deepest integration for Claude Code users.

---

## Getting the Skills

The skills are included in the [Monospace Design TUI repository](https://github.com/coreyt/monospace-design-tui) under `skills/`. To use them with Claude Code, clone the repository and the skills will be available when working within the project directory.

```
skills/
├── mono-tui-design/
│   └── SKILL.md
└── mono-tui-audit/
    └── SKILL.md
```
