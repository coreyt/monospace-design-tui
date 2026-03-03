```
┏┳┓┏━┓┏┓┓┏━┓┏━┓┏━┓┏━┓┏━┓┏━┓  ┏┳┓┳ ┳┳
┃┃┃┃ ┃┃┃┃┃ ┃┗━┓┣━┛┣━┫┃  ┣┫    ┃ ┃ ┃┃
┻ ┻┗━┛┛┗┛┗━┛┗━┛┻  ┻ ┻┗━┛┗━┛   ┻ ┗━┛┻
```

**A design language for terminal user interfaces** — v0.1

Website: [monospace-tui.dev](https://monospace-tui.dev/)

---

As terminal user interfaces grew beyond simple scripts into full applications — dashboards, file managers, configuration wizards — a problem became clear. Every project invented its own conventions. Keyboard shortcuts varied from app to app. Layouts followed no shared logic. Color meant different things in different tools. The experience of using one TUI taught you nothing about using the next.

This seemed wrong. Graphical interfaces had solved this decades ago. Apple published the Human Interface Guidelines. Google developed Material Design. These standards meant that a user who learned one application could sit down in front of another and already know how it worked. But for terminal interfaces — nothing. No shared vocabulary, no common rules, no design system.

We suspected the raw material already existed. The history of text-mode computing is rich with thoughtful design: IBM's CUA keyboard model from 1987, the window management conventions of OS/2, Norton Commander's dual-pane paradigm, Borland's Turbo Vision component framework. These weren't ad hoc — they were carefully engineered systems that millions of people used daily. The knowledge was there, scattered across manuals, technical references, and the muscle memory of experienced developers.

So we collected it. We studied seven research vectors — CUA, OS/2, Material Design 3, Apple HIG, the Keystroke-Level Model, modern terminal capabilities, and historical TUI applications — and synthesized them into a single, prescriptive design language. Not guidelines. Not suggestions. Falsifiable, auditable rules that a reviewer can check against an implementation and declare it compliant or in violation.

The result is Monospace Design TUI: a v0.1 design standard for terminal applications that want to look and behave like they belong to the same family.

## The Documents

**[Design Standard](mono-tui-design-standard.md)** — The authoritative specification. Grid and layout, keyboard interaction, navigation topology, components, color, borders, typography, state, accessibility, motion, and archetypes.

**[Rendering Reference](mono-tui-rendering-reference.md)** — The concrete companion. Exact Unicode codepoints, SGR escape sequences, component measurements, 256-color palettes, and shadow rendering algorithms.

**[Textual Appendix](mono-tui-textual-appendix.md)** — Mapping the standard to the Python Textual framework. Widget selection, TCSS patterns, async rules, responsive breakpoints, and a working dashboard example.

**[Foundational Research](mono-tui.md)** — The seven research vectors behind the standard. The full synthesis of legacy TUI and modern HCI research that informed every rule.

**[Examples](website/content/examples/_index.md)** — ASCII screenshots showing the design standard in action across all five archetypes.

**[Working with AI Agents](website/content/agents/_index.md)** — Claude Code skills for designing and auditing TUI applications against the standard.

## License

This work is licensed under [CC BY-SA 4.0](LICENSE).
