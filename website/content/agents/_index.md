---
title: "Working with AI Agents"
subtitle: "v0.2.5 — A modern adoption model for Mono-aligned coding agents"
description: "How AI coding agents can use the Monospace Design TUI standard with instruction files, project manifests, MCP, and agent-native accelerators"
---

Monospace Design TUI assumes that developers increasingly build with coding
agents. The goal is not merely to make the standard readable by machines. The
goal is to help agents behave like strong design collaborators: clear,
pattern-aware, recommendation-capable, and comfortable working with humans in
the loop.

The tiers below describe the current adoption model.

---

## What a Mono Agent Should Be

A Mono-aligned agent should not act like a generic code generator with a style
guide stapled on afterward.

It should:

- ground itself in the Standard, Rendering Reference, Pattern Library, and project overrides
- recommend strong directions when the design evidence is clear
- ask focused questions when archetype, workflow, or visual direction is materially ambiguous
- explain tradeoffs cleanly without becoming verbose or indecisive
- work comfortably with human review at the right checkpoints
- steer toward aesthetic-first, keyboard-first, pattern-coherent TUIs rather than generic dashboards

The intended reasoning order is:

1. Project constraints and overrides
2. Workflow archetype
3. Screen archetype
4. Pattern selection
5. Keyboard model
6. Component selection
7. Palette and visual tone
8. Rendering details
9. Audit against the standard and project conventions

---

## Tier 1: Instruction Pointer

The lightest integration is a short project instruction file:

- `AGENTS.md`
- `CLAUDE.md`
- another tool-specific instruction or memory file

Recommended snippet:

```md
When building TUI screens, follow the Monospace Design TUI standard.
Read the agent directive at:
  https://coreyt.github.io/monospace-design-tui/agent-ref/index.md
Use the project's `TUI-DESIGN.md` if present.
Default to the "Default" palette unless the project specifies another named palette.
```

This is enough to tell an agent Mono exists and where to begin.

**Valid palette names:** Default, Monochrome, OS/2, Turbo Pascal, Amber Phosphor, Green Phosphor, Airlock

---

## Tier 2: Project Manifest

For projects that need explicit control, create a `TUI-DESIGN.md` in the
project root using the [template](https://github.com/coreyt/monospace-design-tui/blob/main/TUI-DESIGN.template.md).

The manifest declares:

- which archetypes the project uses
- which palette applies
- any rule overrides (`WAIVE`, `OVERRIDE`, `TIGHTEN`)
- project-specific conventions beyond the base standard

This is how Mono becomes project-specific rather than generic.

---

## Tier 3: MCP Integration

This is now the preferred serious integration path.

The MCP server gives any compatible coding agent structured access to the
design system from any project, without cloning the repository into that
project.

### Why MCP comes before agent-native extensions

- it is cross-agent rather than vendor-specific
- it exposes structured data instead of relying on long prompt memory
- it supports direct retrieval of rules, palettes, components, archetypes, and patterns
- it is the best portable foundation for modern agent workflows

### What it provides

18 tools organized around:

- design consultation
- workflow archetypes
- UI archetypes
- standard and reference sections
- color palettes
- components and widget recommendations
- keyboard bindings

The MCP server is the portable backbone of Mono’s agent story.

---

## Tier 4: Agent-Native Accelerators

Once MCP and `TUI-DESIGN.md` are in place, agent-native features can improve
ergonomics and local workflow.

Examples:

- Claude slash commands, skills, hooks, and subagents
- Codex skills, app workflows, and automations
- Cursor or Windsurf equivalents

These are not the foundation. They are accelerators on top of the portable
system.

### Current Mono-native accelerators

The repository currently includes two agent-facing skills:

#### `mono-tui-design`

Use for:

- layout planning
- widget selection
- pattern selection
- wireframe creation
- implementation guidance

Expected behavior:

- load `TUI-DESIGN.md` first
- load relevant Standard sections
- load Rendering Reference only as needed
- load the Pattern Library as a first-class design input
- recommend an archetype and pattern set, not just raw rules
- propose ASCII wireframes before implementation

#### `mono-tui-audit`

Use for:

- compliance review after a screen is built or changed
- auditing rule conformance and project overrides
- identifying stale overrides and manual-review gaps

Expected behavior:

- merge the base ruleset with project overrides
- check code-level violations
- flag visual/manual checks separately
- produce high-signal findings and concrete fixes

---

## Recommended Workflow

For most projects:

1. Add a Tier 1 instruction pointer.
2. Create `TUI-DESIGN.md` when palette, archetype, or override decisions matter.
3. Connect the MCP server for structured retrieval and design consultation.
4. Add agent-native accelerators if your platform supports them.

In practice:

- Tier 1 tells the agent Mono exists
- Tier 2 tells the agent how this project specializes Mono
- Tier 3 gives the agent reliable structured access to Mono
- Tier 4 makes the workflow faster and more ergonomic

---

## Human in the Loop

Mono expects agents to work well with human review rather than avoiding it.

The right posture is:

- ask when workflow, archetype, or palette direction is materially ambiguous
- proceed when the next step is clear and low-risk
- surface tradeoffs before expensive or irreversible design decisions
- return with recommendations, not vague uncertainty

This is not a one-micro-step-per-approval model, and it is not blind autonomy.
It is disciplined, recommendation-forward collaboration.

---

## The Contract

The standard is the source of truth. The [agent directive](/agent-ref/) tells
agents how to load it. `TUI-DESIGN.md` tells agents how a specific project
customizes it. MCP makes the system portable. Agent-native accelerators make
the workflow better.

The end goal is simple: an agent that gives excellent, Mono-aligned guidance
and helps build TUIs that are coherent, legible, keyboard-consistent, and
visually intentional.
