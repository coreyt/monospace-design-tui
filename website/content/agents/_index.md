---
title: "Working with AI Agents"
subtitle: "Using Claude Code skills to design and audit TUI applications"
description: "How AI coding agents can use the Monospace Design TUI standard through Claude Code skills"
---

A design standard is only useful if it's applied. Monospace Design TUI was built with the expectation that developers would use AI coding agents as collaborators — and that those agents need structured, machine-readable standards to follow.

The Monospace Design TUI project includes two [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skills that give AI agents direct access to the standard. When a developer asks an agent to build a TUI screen, the agent doesn't improvise — it loads the relevant sections of the standard, applies project-specific overrides, and produces compliant designs and code.

---

## mono-tui-design

The design skill handles the creative work: planning layouts, selecting widgets, assigning keyboard bindings, and generating implementation code.

**When it activates:** Layout planning, widget selection, wireframe creation, or writing Textual code for terminal interfaces.

**What it does:**

1. **Loads context** — Reads the project's `TUI-DESIGN.md` for overrides and conventions, then loads relevant sections of the design standard.
2. **Analyzes intent** — Determines which archetype (Dashboard, Admin, File Manager, Editor, Fuzzy Finder) matches the user's goal.
3. **Architects** — Proposes a design with ASCII wireframes, region layout, widget selection rationale, keyboard bindings across all three tiers, and color/state assignments.
4. **Self-critiques** — Checks the design against common violations: frozen UI, mouse traps, navigation mazes, invisible focus, missing footer keys, case-sensitivity errors, F-key dependencies.
5. **Generates code** — Produces framework-specific implementation (Textual TCSS, Python widgets, key bindings with the `ci()` helper).

**Invoke with:** `/mono-tui-design`

---

## mono-tui-audit

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

1. Create a `TUI-DESIGN.md` in your project root (use the [template](https://github.com/monospace-tui/monospace-design-tui/blob/main/TUI-DESIGN.template.md)) to declare your archetypes, framework, and any overrides.
2. Ask the agent to design a screen — it uses `mono-tui-design` to produce a compliant wireframe and code.
3. Build and iterate.
4. Run `mono-tui-audit` to verify compliance. Fix violations. Repeat.

The standard is the source of truth. The skills are how the agent reads and applies it. The `TUI-DESIGN.md` is how your project customizes it.

---

## Getting the Skills

The skills are included in the [Monospace Design TUI repository](https://github.com/monospace-tui/monospace-design-tui) under `skills/`. To use them with Claude Code, clone the repository and the skills will be available when working within the project directory.

```
skills/
├── mono-tui-design/
│   └── SKILL.md
└── mono-tui-audit/
    └── SKILL.md
```
