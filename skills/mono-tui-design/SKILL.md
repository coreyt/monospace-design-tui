---
name: mono-tui-design
description: Design and implement TUI screens following the Monospace Design TUI standard. Use when planning layouts, selecting widgets, creating wireframes, or writing Textual code for terminal interfaces.
---

# Mono-TUI Design

Design and implement terminal user interfaces following the
[Monospace Design TUI Standard](../../mono-tui-design-standard.md).

## Context Loading

Before any design work, load context in this order:

1. **Project overrides** — Read `TUI-DESIGN.md` in the project root (or nearest
   ancestor). If it exists, parse:
   - `## Meta` → archetypes, framework, minimum terminal size
   - `## Overrides` → `[WAIVE]`, `[OVERRIDE]`, `[TIGHTEN]` rules that modify
     the standard for this project
   - `## Project Conventions` → `[P#]` rules to follow alongside the standard

2. **Design Standard** — Read the Monospace Design TUI Standard for the rules
   governing the current task. You do not need to read all 11 sections — load
   what is relevant:
   - Layout questions → §1 Grid & Layout
   - Keyboard design → §2 Keyboard Interaction
   - Screen flow → §3 Navigation Topology
   - Widget selection → §4 Component Rules
   - Color/theme → §5 Color System
   - Borders/elevation → §6 Border & Elevation
   - Text styling → §7 Typography
   - Interactive states → §8 State Model
   - Accessibility → §9 Accessibility
   - Animation/feedback → §10 Motion & Feedback
   - Full-screen patterns → §11 Archetypes

3. **Rendering Reference** — Read when you need exact character codes, SGR
   sequences, measurements, or color indices for implementation.

4. **Textual Appendix** — Read when the framework is Textual. Contains widget
   mappings, TCSS patterns, and the `ci()` binding helper.

**Override precedence:** When TUI-DESIGN.md contains an override for a rule,
the override takes priority. Use the override's `Replacement:` text (for
OVERRIDE), skip the rule (for WAIVE), or tighten the level (for TIGHTEN).
Never recommend something that contradicts an active project override.

## Workflow

### 1. Analyze Intent

Determine what the user is building:
- What is the user's goal? (e.g., "add a settings screen", "build a dashboard")
- Which archetype (§11) matches? Dashboard, Admin/Config, File Manager, Editor,
  Fuzzy Finder, or a hybrid?
- Are there active overrides that affect this design?

### 2. Architect

Propose the design with reasoning:

**Layout** — Apply the three-region rule (§1.3). Show an ASCII wireframe using
the archetype's layout pattern. Specify region widths and what goes in each.

**Navigation** — Apply the decision tree (§3.1). How does this screen relate
to others? Tabs (parallel), push/pop (drill-down), modal (transient), or
panel (contextual detail)?

**Widget Selection** — Apply the widget decision table (§4.1). For each data
element, choose the correct widget based on data type and option count.
Justify deviations.

**Keyboard** — Apply the three-tier key system (§2.2):
- Tier 1: Verify all mandatory keys are bound (q, ?, /, r, Esc, etc.)
- Tier 2: Bind standard keys for actions that exist (d, e, a, s, y, `:`, Ctrl+Z)
- Tier 3: Assign screen mnemonics if applicable
- Check for conflicts between tiers

**Color & State** — Apply semantic roles (§5.1) and the state model (§8.1).
Ensure color independence (§5.3) — every color has a paired text/symbol.

### 3. Critique

Before presenting the design, self-audit against common violations:

| Violation | Check |
|-----------|-------|
| Frozen UI | Is any I/O on the main thread? |
| Mouse trap | Can every action be done by keyboard? |
| Angry fruit salad | More than 4 colors visible at once? |
| Navigation maze | More than 2 levels of drill-down? |
| Invisible focus | Is focus always visible? |
| Hardcoded layout | Any fixed pixel/col values that should be flex? |
| Missing footer | Are all keys shown in the footer? |
| Case-sensitivity | Any letter bindings that aren't case-insensitive? |
| F-key dependency | Can every action be done without F-keys? |

### 4. Code

Generate implementation code following:

- The standard's rules (with overrides applied)
- The Textual Appendix patterns (if framework is Textual):
  - Use `ci()` helper for case-insensitive bindings (§T4.3)
  - Use `@work` for all I/O; handle Worker.cancelled and Worker.error (§T3.1, §T3.2)
  - Use `Footer()` for key strip (§T1.1)
  - Use elevation TCSS classes (§T2.1)
  - Use responsive breakpoint handler (§T6)
- The Rendering Reference (for exact characters, SGR codes, measurements)

## Wireframe Format

When proposing layouts, use this ASCII wireframe format:

```
┌── Region A ───┬── Region B (flex) ───────────────┐
│               │                                   │
│  Navigation   │  Content area                     │
│  items here   │                                   │
│               │                                   │
├───────────────┴───────────────────────────────────┤
│ ?Help  r Refresh  /Filter  q Quit                 │
└───────────────────────────────────────────────────┘
```

Use single-line borders for panels (Level 1), double-line for dialogs (Level 3).
Include the footer key strip. Mark flex areas.

## TUI-DESIGN.md Bootstrap

If the project has no `TUI-DESIGN.md` and the user is starting fresh, offer to
create one from the template. Ask:

1. What archetypes will the project use?
2. What framework (Textual, curses, raw ANSI)?
3. What is the minimum terminal size?
4. Are there any known standard rules to override?

Then generate a `TUI-DESIGN.md` with the Meta section filled in and empty
Override/Convention/Decision sections.

## Rules

- **Always** check for TUI-DESIGN.md before recommending standard rules.
- **Always** show an ASCII wireframe before writing code.
- **Always** include footer key strip in wireframes.
- **Always** use `ci()` for letter bindings in Textual code.
- **Always** use `@work` for I/O in Textual code.
- **Never** recommend a pattern that contradicts an active WAIVE or OVERRIDE.
- **Never** bind only F-keys — every F-key must have a common key equivalent.
- **Never** use color as the sole indicator of any state.
- **Never** hide disabled controls — dim them instead.

## Related Documents

| Document | Path | When to Read |
|----------|------|-------------|
| Design Standard | `mono-tui-design-standard.md` | Always — authoritative rules |
| Rendering Reference | `mono-tui-rendering-reference.md` | Implementation — exact chars, SGR, measurements |
| Textual Appendix | `mono-tui-textual-appendix.md` | When framework is Textual |
| TUI-DESIGN.md | Project root | Always — project overrides and conventions |
| TUI-DESIGN.template.md | `TUI-DESIGN.template.md` | When bootstrapping a new project |
