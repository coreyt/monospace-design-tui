```
┏┳┓┏━┓┏┓┓┏━┓┏━┓┏━┓┏━┓┏━┓┏━┓  ┏┳┓┳ ┳┳
┃┃┃┃ ┃┃┃┃┃ ┃┗━┓┣━┛┣━┫┃  ┣┫    ┃ ┃ ┃┃
┻ ┻┗━┛┛┗┛┗━┛┗━┛┻  ┻ ┻┗━┛┗━┛   ┻ ┗━┛┻
```

**A design language for terminal user interfaces** — v0.2.5

Website: [coreyt.github.io/monospace-design-tui](https://coreyt.github.io/monospace-design-tui/)

---

Monospace Design TUI is a design standard for terminal applications: dashboards,
file managers, editors, admin panels, fuzzy finders, and other keyboard-first
interfaces that run in a text terminal.

Text-based interfaces are making a comeback because they are fast, simple,
portable, scriptable, and well-suited to modern developer workflows. But while
GUI and web teams have long had design systems and style guides, terminal
applications largely did not. Every project invented its own conventions.
Keyboard shortcuts varied from app to app. Layouts followed no shared logic.
Color meant different things in different tools. The experience of using one
TUI taught you nothing about using the next.

This seemed wrong. Graphical interfaces had solved this decades ago. Apple
published the Human Interface Guidelines. Google developed Material Design.
These standards meant that a user who learned one application could sit down in
front of another and already know how it worked. But for terminal interfaces:
no shared vocabulary, no common rules, no design system. So I created one.

The raw material already existed. The history of text-mode computing is rich
with thoughtful design: IBM's CUA keyboard model from 1987, the window
management conventions of OS/2, Norton Commander's dual-pane paradigm,
Borland's Turbo Vision component framework, plus lessons from modern tools such
as Lazygit, k9s, btop, bottom, and Helix.

Monospace Design TUI collects those ideas and turns them into a single
prescriptive system. Not loose inspiration. Not vague guidelines. Falsifiable,
auditable rules that a reviewer can check against an implementation and declare
it compliant or in violation.

The result is Monospace Design TUI: a v0.2.5 design standard for terminal applications that want to look and behave like they belong to the same family.

## Why Use It

Monospace TUI gives terminal applications the same kinds of benefits that GUI
and web design systems provide:

- shared keyboard conventions across applications
- clearer layout and navigation patterns
- stronger focus, state, and feedback rules
- reusable interaction patterns instead of one-off design choices
- named palettes and rendering guidance for consistent visual tone
- a basis for design review, implementation audit, and AI-agent guidance

The goal is not uniformity for its own sake. The goal is making TUIs easier to
learn, easier to build, easier to review, and better to use.

## Quick Start

If you want to adopt Mono quickly:

1. Read the [Design Standard](monospace-tui-design-standard.md).
2. Pick a [named palette](monospace-tui-rendering-reference.md) and the
   relevant [archetype](monospace-tui-design-standard.md).
3. Create a `TUI-DESIGN.md` from [TUI-DESIGN.template.md](TUI-DESIGN.template.md)
   if your project needs explicit archetypes, overrides, or conventions.

If you are implementing in Textual, also read the
[Textual Appendix](monospace-tui-textual-appendix.md).

If you are designing with AI agents, start with
[Working with AI Agents](website/content/agents/_index.md) and the
[Agent Reference Directive](website/content/agent-ref/_index.md).

## The Documents

**[Design Standard](monospace-tui-design-standard.md)** — The authoritative specification. Grid and layout, keyboard interaction, navigation topology, components, color, borders, typography, state, accessibility, motion, and archetypes.

**[Pattern Library](monospace-tui-pattern-library.md)** — Reusable interaction patterns distilled from modern TUIs. Footer command bars, focused surfaces, master-detail layouts, expand-to-focus behavior, object-local actions, command jumps, selection grammar, and live drill-down.

**[Rendering Reference](monospace-tui-rendering-reference.md)** — The concrete companion. Exact Unicode codepoints, SGR escape sequences, component measurements, 256-color palettes, and shadow rendering algorithms.

**[Textual Appendix](monospace-tui-textual-appendix.md)** — Mapping the standard to the Python Textual framework. Widget selection, TCSS patterns, async rules, responsive breakpoints, and a working dashboard example.

**Framework Appendices (outlines):**

- **[Rich](monospace-tui-rich-appendix.md)** — Python Rich rendering library (non-interactive output, `Live` displays, progress bars)
- **[Bubble Tea](monospace-tui-bubbletea-appendix.md)** — Go Elm-architecture TUI (includes Bubbles, Lip Gloss, Huh?, and Gum)
- **[Ratatui](monospace-tui-ratatui-appendix.md)** — Rust immediate-mode rendering (crossterm backend, constraint layout)
- **[Ink](monospace-tui-ink-appendix.md)** — Node.js/TypeScript React-based TUI (Flexbox layout, `@inkjs/ui` components)

**[Foundational Research](monospace-design-tui-research.md)** — The seven research vectors behind the standard. The full synthesis of legacy TUI and modern HCI research that informed every rule.

**[Examples](website/content/examples/_index.md)** — ASCII screenshots showing the design standard in action across all five archetypes.

**[Working with AI Agents](website/content/agents/_index.md)** — A modern adoption model for Mono-aligned coding agents, from simple instruction pointers to MCP-backed structured design workflows.

**[MCP Server](mcp-server/)** — Connect AI agents in any project to the design system via MCP. Query design rules, palettes, components, keyboard bindings, and archetypes — 18 tools including interactive design consultation.

## License

This work is licensed under [CC BY-SA 4.0](LICENSE).
