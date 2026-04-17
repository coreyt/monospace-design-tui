# TUI Application UX Survey

Date: 2026-04-17

This document surveys UI and UX design patterns in five text-based applications:

- Lazygit
- k9s
- btop
- bottom
- Helix

The goal is not to rank the tools. It is to extract reusable interface patterns that appear repeatedly in high-functioning terminal applications, especially patterns relevant to Monospace Design TUI.

## Method

For each project, the survey used:

- The project repository and README/docs as the primary source of interface intent
- Example screens, screenshots, and official demos where available
- Focused UI or UX commentary when available

This is an interaction-design survey, not a feature comparison.

## Lazygit

Primary sources:

- https://github.com/jesseduffield/lazygit
- https://www.bwplotka.dev/2025/lazygit/
- https://graphite.com/guides/lazygit

Observed patterns:

- Persistent multi-pane workspace. Multiple Git objects remain visible at once: files, commits, branches, stash, diff, and action context.
- Master-detail coordination. Moving focus in one list updates an adjacent detail pane rather than forcing navigation to a new screen.
- Footer-based discoverability. Commands are exposed in-context, which reduces the need to memorize keys before becoming productive.
- Context-panel keyboard model. Available actions change based on the focused pane. This is one of lazygit's strongest contributions to modern TUI interaction design.
- Object-local actions. Git operations act on the selected file, commit, branch, or stash entry directly.
- Shallow flows for complex tasks. Rebase, stash, conflict handling, and branch operations are surfaced through short guided sequences instead of deeply nested menus.
- Stable pane semantics. Each pane keeps a consistent role, which keeps the high density legible.

UX read:

- Lazygit is optimized for operational fluency rather than visual novelty.
- Its strongest trait is discoverable consistency: the user is taught the product by the footer, pane titles, and focus changes.
- The interface stays dense but rarely becomes disorienting because selection, focus, and target object remain explicit.

## k9s

Primary sources:

- https://github.com/derailed/k9s
- https://k9scli.io/
- https://palark.com/blog/k9s-the-powerful-terminal-ui-for-kubernetes/

Observed patterns:

- Resource-view navigation. The product is organized around Kubernetes resource types and operational views rather than around generic pages.
- Command-jump model. Colon commands such as `:pods`, `:deploy`, `:pulse`, and `:xray` let expert users navigate directly to a destination.
- Real-time operational cockpit. The interface is designed for continuously changing state rather than static inspection.
- Drill-down from overview to intervention. Users move from cluster/resource overview to logs, shell access, edit, describe, port-forward, or scale without leaving the operational shell.
- Focused tables with contextual actions. The selected resource defines the action surface.
- Breadcrumb/history support. Navigational state is treated as something worth preserving and showing, which matters in large clusters.
- Presentation controls. Users can toggle visual chrome and adjust density without changing the underlying interaction model.

UX read:

- k9s strongly favors expert speed under operational pressure.
- Discoverability exists, but the product leans more toward command efficiency than beginner onboarding.
- Its best pattern contribution is addressable navigation inside a live multi-resource environment.

## btop

Primary sources:

- https://github.com/aristocratos/btop
- https://www.howtogeek.com/heres-why-btop-became-my-favorite-linux-terminal-resource-monitor/
- https://terminaltrove.com/btop/

Observed patterns:

- Dashboard-in-a-box layout. CPU, memory, network, disks, and process list are visually chunked into bordered modules.
- Graph-first monitoring. Trends are legible at a glance through time-series displays rather than requiring number parsing first.
- Embedded onboarding. Keyboard hints and menu affordances are visible inside the main interface.
- Fast view customization. Users can reconfigure what is shown without losing orientation.
- Hybrid input model. Mouse support exists, but keyboard use remains first-class.
- Decorative utility. Color, graph fidelity, and framed modules improve visual appeal while also clarifying grouping and hierarchy.

UX read:

- btop is unusually approachable for a dense monitor because it invests in visual chunking and in-band guidance.
- It treats aesthetic polish as a usability lever rather than a cosmetic layer.
- Compared with bottom, btop is more ornamental and more immediately inviting.

## bottom

Primary sources:

- https://github.com/ClementTsang/bottom
- https://bottom.pages.dev/stable/
- https://linuxblog.io/bottom-btm/
- https://www.linuxlinks.com/essential-system-utilities-bottom-graphical-process-system-monitor/3/

Observed patterns:

- Widget dashboard with explicit focus ownership. One widget is active at a time.
- Expand-to-focus. Any selected widget can take over the screen, which is a strong solution to terminal-space constraints.
- Directional widget navigation. Users move across the dashboard spatially rather than through abstract tabs.
- Two complexity tiers. Standard mode is information-dense; basic mode reduces complexity for smaller terminals or simpler use.
- Table-plus-graph composition. Historical signal and current-process inspection live in the same surface.
- Configurable layout as core architecture. Layout is not treated as fixed decoration; it is part of the product's interaction model.

UX read:

- bottom is highly structural. Its UX value comes from focus management and density control more than surface styling.
- The expand pattern is especially strong because it preserves continuity while resolving cramped layouts.
- Compared with btop, it feels more analytical and modular.

## Helix

Primary sources:

- https://github.com/helix-editor/helix
- https://docs.helix-editor.com/master/editor.html
- https://herecomesthemoon.net/2025/06/i-like-helix/
- https://tqwewe.com/blog/helix-vs-neovim/

Observed patterns:

- Selection-first interaction grammar. Users select ranges or multiple regions, then apply commands. This makes intent more visible than opaque verb-object editing models.
- Minimal but information-rich chrome. Statusline, gutters, diagnostics, pickers, and popups expose state without turning into a full IDE shell.
- In-context chord discovery. Possible key continuations and command outcomes are surfaced more clearly than in traditional modal editors.
- Multiple selections as a first-class feature. Parallel editing is not an advanced plugin pattern; it is part of the core interaction model.
- Command bar over detached dialogs. Commands remain composition-friendly instead of scattering interaction across many special-purpose flows.
- Mode visibility. Modal state is communicated through the statusline and cursor behavior, reducing hidden-state risk.
- Coherent built-ins. File picking, diagnostics, and language features are integrated into the core surface rather than feeling bolted on.

UX read:

- Helix is model-centric rather than dashboard-centric.
- Its biggest UX contribution is a clearer editing grammar: select, inspect, transform.
- It reduces memorization burden by making action possibilities more legible.

## Cross-Application Patterns

The five tools differ in domain, but their strongest UX choices repeatedly converge:

- Keep state visible. Focus, mode, target object, health state, and danger state should be inspectable without guesswork.
- Keep actions local. Most actions should operate on the selected object or focused pane.
- Keep navigation shallow. Prefer context panes, preview panes, expansion, and drill-down over large screen stacks.
- Teach in-context. Keyboard affordances should be visible inside the product, especially in the footer or status surfaces.
- Support expert acceleration without making it mandatory. Command jumps, modal layers, and dense shortcuts are valuable only if the basic path remains legible.
- Manage density explicitly. Rich multi-pane screens work when focus, grouping, and escape hatches are clear.

## Candidate Mono Pattern Names

These patterns appeared strongly enough to justify reusable names for Monospace Design TUI:

- Footer Command Bar
- Focused Surface
- Master-Detail
- Expand-to-Focus
- Object-Local Actions
- Command Jump
- Selection Grammar
- Live Drill-Down

## Notes for Mono

The current Monospace Design TUI standard already overlaps with much of this survey:

- `Footer Command Bar` aligns with the existing footer key strip rule.
- `Focused Surface` aligns with explicit focus requirements and context-sensitive panes.
- `Master-Detail` aligns with the three-region layout and contextual detail panes.
- `Command Jump`, `Selection Grammar`, and `Live Drill-Down` are not yet named as reusable patterns even though their ingredients already appear in the standard and archetypes.

The pattern-library companion document formalizes those patterns so they can be applied and audited consistently.
