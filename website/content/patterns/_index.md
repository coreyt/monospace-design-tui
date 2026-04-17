---
title: "Monospace TUI Pattern Library"
subtitle: "Reusable interaction patterns distilled from modern text UIs"
description: "Named UX patterns for Monospace TUI applications, with archetype mapping and audit checklists"
weight: 4
---

This companion document to the [Design Standard](/standard/) names and formalizes recurring interaction patterns found in modern terminal applications such as Lazygit, k9s, btop, bottom, and Helix.

Monospace TUI is intentionally compatible with **aesthetic-first CUI design**: interfaces that use the terminal as an expressive visual canvas, not just as a neutral control surface.[^cui-aesthetic]

Where the standard defines **rules** and the archetypes define **screen structures**, the pattern library defines reusable **interaction strategies** that can appear across multiple archetypes.

## What This Adds

The pattern library gives Monospace TUI a shared vocabulary for discussing behaviors that already recur across the ecosystem:

- Footer Command Bar
- Focused Surface
- Master-Detail
- Expand-to-Focus
- Object-Local Actions
- Command Jump
- Selection Grammar
- Live Drill-Down

These patterns are intended to support:

- screen design
- archetype composition
- implementation review
- audit consistency

## Named Pattern Appendix

### Footer Command Bar

A persistent footer that exposes the currently available commands for the focused surface. This is the main discoverability layer for keyboard-first applications.

Use when:

- the screen has more than a few contextual actions
- the active commands vary by focus or mode
- the product expects users to learn by doing
- the design wants recognition over recall in dense workflows[^recognition-recall]

Audit checklist:

- The footer is always visible.
- The footer changes when focus or mode changes.
- The footer shows only actions valid in the current context.
- No task-critical command is hidden if the footer is the only discoverability surface.
- Labels describe user actions rather than internal implementation terms.

### Focused Surface

Exactly one pane, widget, editor, or control cluster owns primary interaction at a time. Keyboard behavior derives from that ownership.

Use when:

- the screen has multiple panes or widgets
- the interface is dense enough that input ownership could become ambiguous
- help, footer, or actions change by pane
- the product depends on spatial continuity across a stable frame[^spatial-memory]

Audit checklist:

- Exactly one interactive surface is focused at a time.
- Focus indication is visible without relying only on color.
- Moving focus changes the footer/help/action scope.
- Removing a focused surface transfers focus predictably.
- Users can distinguish selection from focus when both exist.

### Master-Detail

A browse surface controls a secondary detail or preview surface without requiring full navigation to another screen.

Use when:

- a selected object has meaningful metadata or preview content
- users need to compare overview and detail continuously
- screen transitions would disrupt orientation
- the product benefits from progressive disclosure inside a stable frame[^progressive-disclosure]

Audit checklist:

- Selection updates the detail area immediately.
- The detail area adds context rather than duplicating the list.
- The user can act on the selected object without leaving the screen.
- Detail collapse or hide behavior is defined at compact widths.
- Returning from a full detail view restores the originating selection.

### Expand-to-Focus

A dense panel or widget can temporarily expand into the primary content area while preserving its identity, state, and command model.

Use when:

- the screen is information-dense
- compact terminal sizes would otherwise force a separate screen
- a widget benefits from temporary extra space

Audit checklist:

- Expanded mode preserves the same object, commands, and data model.
- Collapse returns the user to the prior layout and focus position.
- Expansion meaning is clear from the UI.
- Expanded mode is not required to complete ordinary tasks.
- Compact layouts have a defined path to expansion for dense widgets.

### Object-Local Actions

Commands apply to the current selection or focused object by default rather than through detached global workflows.

Use when:

- the product revolves around operating on listed objects
- destructive or high-cost actions need strong target clarity
- users need a short path from selection to action

Audit checklist:

- The current target object is visually explicit.
- Primary actions operate on the selected object without extra targeting steps.
- Confirmation dialogs name the affected object.
- Global actions are limited to truly global scope.
- Empty-selection behavior is handled explicitly.

### Command Jump

Users can navigate directly to screens, resources, or commands through an addressable command input rather than only through stepwise navigation.

Use when:

- the application has many views or resources
- expert operators benefit from direct navigation
- the visible navigation model would otherwise become too broad

Audit checklist:

- Command input is optional, not mandatory.
- Every important destination also has a visible non-command path.
- Command results are predictable and scoped.
- Unknown commands fail clearly and recoverably.
- The command surface does not conflict with ordinary text entry modes.

### Selection Grammar

The primary interaction model is “select target, then act” or “select range, then transform.” Selection is part of the visible grammar, not a side effect.

Use when:

- batch actions or range operations matter
- editing, review, or object transformation is central
- the user needs confidence about what an action will affect
- the interface should favor visual confirmation before commitment[^direct-manipulation]

Audit checklist:

- Selection state is persistent enough to trust.
- Selection and focus are visually distinguishable if both exist.
- Actions describe whether they apply to the current item, current selection, or whole view.
- Batch actions behave consistently with single-item actions.
- Selection survives short navigation flows where continuity matters.

### Live Drill-Down

A screen presents real-time overview data and allows immediate drill-down into anomalies, items, or alerts without leaving the operational context.

Use when:

- the product includes live monitoring or live-refresh status
- users need to investigate anomalies without losing situational awareness
- overview and intervention belong in the same shell

Audit checklist:

- The overview remains legible during live updates.
- The user can drill into a live item directly from the overview.
- Auto-refresh does not destroy scroll position or selection.
- Returning from drill-down restores the prior overview state.
- Health, anomaly, or status changes are visible without opening detail first.

## Companion Practices

These are recurring interaction practices worth preserving even when they are not treated as primary cross-archetype patterns.

### Filtered Help

Help should usually be filtered to the focused pane, active layer, or current object scope rather than shown as a global command dump.[^recognition-recall]

### Command Transparency

Applications that wrap an underlying CLI or external toolchain MAY expose the raw command, request, or operation log in a secondary status region. This improves trust, teaches the underlying system, and reduces the sense of hidden magic.

### Discoverable Prefix Continuations

When a prefix or leader key opens a temporary command layer, applications SHOULD expose available continuations in a lightweight popup or status hint rather than relying entirely on memory.[^progressive-disclosure]

### Provenance and Lineage Views

Operational tools SHOULD consider a lineage view that explains why an object exists, what owns it, or what it is connected to.

## Key Set Appendix

Key sets are coherent clusters of bindings that should be used together across related screens.

Consistency rules:

- A key's meaning should stay stable across screens that share a key set.
- Applications should not reuse the same single-letter key for different domain actions on sibling screens in the same key set.
- If a screen changes key sets, the footer or status area should make that obvious immediately.
- Arrow keys remain within one control. Pane, widget, or view switching should use Tab/Shift+Tab, numbered views, or other non-arrow bindings.

### Browse/Inspect Set

- Enter = inspect or open
- Esc = back
- `/` = filter
- `n` = next search result
- `g` / `G` = top / bottom
- `y` = copy value
- `e` = edit
- `d` = delete
- `s` = sort

### Monitor/Respond Set

- `r` = refresh
- `/` = filter stream or item list
- Enter = inspect current anomaly or row
- `a` = acknowledge or act
- `s` = sort current table
- `1`–`9` = switch views or dashboards
- Tab / Shift+Tab = switch focused panel

### Search/Select Set

- printable input = append to filter
- Ctrl+N / Ctrl+P or Up / Down = move through results
- Enter = select
- Esc = cancel
- Tab = toggle preview or advance preview focus

### Edit/Transform Set

- Ctrl+S = save
- Ctrl+F or `/` = find
- Ctrl+G = goto
- Esc = leave insert or prefix state
- selection commands stay consistent across editor screens

## Pattern to Archetype Mapping

`Primary` means the pattern is a strong natural fit for the archetype.
`Supported` means the pattern is useful but not central.
`Rare` means possible but atypical.

| Pattern | Dashboard | Admin / Config | File Manager | Editor | Fuzzy Finder |
|---------|-----------|----------------|--------------|--------|--------------|
| Footer Command Bar | Primary | Primary | Primary | Primary | Primary |
| Focused Surface | Primary | Supported | Primary | Primary | Primary |
| Master-Detail | Supported | Supported | Primary | Rare | Primary |
| Expand-to-Focus | Primary | Rare | Supported | Rare | Rare |
| Object-Local Actions | Primary | Supported | Primary | Supported | Supported |
| Command Jump | Supported | Rare | Rare | Supported | Rare |
| Selection Grammar | Supported | Rare | Supported | Primary | Primary |
| Live Drill-Down | Primary | Rare | Supported | Rare | Rare |

## Required vs Optional Matrix by Archetype

`Required` means the pattern should normally appear in a compliant implementation of the archetype.
`Optional` means it may appear when the product domain benefits from it.
`Not Typical` means the pattern is usually unnecessary for the archetype.

| Pattern | Dashboard | Admin / Config | File Manager | Editor | Fuzzy Finder |
|---------|-----------|----------------|--------------|--------|--------------|
| Footer Command Bar | Required | Required | Required | Required | Required |
| Focused Surface | Required | Optional | Required | Required | Required |
| Master-Detail | Optional | Optional | Required | Not Typical | Optional |
| Expand-to-Focus | Optional | Not Typical | Optional | Not Typical | Not Typical |
| Object-Local Actions | Required | Optional | Required | Optional | Optional |
| Command Jump | Optional | Not Typical | Not Typical | Optional | Not Typical |
| Selection Grammar | Optional | Not Typical | Optional | Required | Required |
| Live Drill-Down | Required for live operational dashboards | Not Typical | Optional | Not Typical | Not Typical |

## Relationship to the Standard

This pattern library is intentionally aligned with existing Monospace TUI rules:

- Footer Command Bar extends the footer key strip.
- Focused Surface extends explicit focus-state requirements.
- Master-Detail extends the three-region layout and contextual pane model.
- Expand-to-Focus complements responsive layout behavior.
- Object-Local Actions complements contextual Tier 2 actions.
- Command Jump complements composable keyboard layers and command-mode patterns.
- Selection Grammar complements editor, finder, and review-oriented interaction models.
- Live Drill-Down complements Dashboard and Monitor-Respond workflows.

## Source Survey

The full research write-up used to derive these patterns is available in the repository at:

- [`dev/TUI-application-UX-survey-2026-04-17.md`](https://github.com/coreyt/monospace-design-tui/blob/main/dev/TUI-application-UX-survey-2026-04-17.md)

The repo-root source for this page is:

- [`monospace-tui-pattern-library.md`](https://github.com/coreyt/monospace-design-tui/blob/main/monospace-tui-pattern-library.md)

[^cui-aesthetic]: Historical terminal systems and modern TUIs both show that strong visual identity and atmospheric rendering can improve orientation and perceived quality when semantic state remains legible.
[^recognition-recall]: Recognition over recall is a long-standing usability principle; filtering actions and help to the current surface reduces memory burden in dense interfaces.
[^spatial-memory]: Stable panel locations and visible anchors support spatial memory in multi-pane environments.
[^progressive-disclosure]: Progressive disclosure reduces cognitive load by revealing detail when a user signals intent instead of front-loading all complexity.
[^direct-manipulation]: Visual confirmation before commit is a core strength of direct-manipulation systems and maps well to selection-first editing models.
