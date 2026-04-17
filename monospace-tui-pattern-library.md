# Monospace TUI Pattern Library

This document abstracts recurring interface patterns from modern high-functioning TUIs into reusable patterns for Monospace Design TUI.

Monospace TUI is intentionally compatible with **aesthetic-first CUI design**: interfaces that use the terminal as an expressive visual canvas, not just as a neutral control surface.[^cui-aesthetic] The patterns below assume that visual richness is welcome when it preserves semantic clarity, accessibility, and keyboard fluency.

Primary reference set:

- Lazygit
- k9s
- btop
- bottom
- Helix

The library complements the existing standard. It does not replace archetypes. Instead, it gives shared names to proven interaction patterns that can appear across multiple archetypes.

## Scope

This library focuses on screen-level and interaction-level patterns. It is meant to support:

- screen design
- archetype selection
- design review
- implementation audits

The archetypes referenced below are the screen archetypes in the Monospace TUI standard:

- Dashboard
- Admin / Config
- File Manager
- Editor
- Fuzzy Finder

## Named Pattern Appendix

### Footer Command Bar

Definition:

A persistent footer that exposes the currently available commands for the focused surface. It is the primary discoverability layer for keyboard-first interaction.

Why it exists:

- Makes keyboard grammar visible
- Reduces memory burden
- Keeps dense interfaces self-teaching
- Favors recognition over recall in high-density workflows.[^recognition-recall]

Observed in:

- Lazygit
- k9s
- btop

Mono fit:

- Directly extends the standard footer key strip
- Best treated as mandatory on every interactive screen

Audit checklist:

- The footer is always visible.
- The footer changes when focus or mode changes.
- The footer shows only actions valid in the current context.
- No task-critical command is hidden if the footer is the only discoverability surface.
- Labels are action-oriented rather than internal jargon.

### Focused Surface

Definition:

Exactly one pane, widget, list, editor, or control cluster owns primary interaction at any moment. Keyboard behavior is derived from that ownership.

Why it exists:

- Prevents ambiguity in dense layouts
- Keeps commands predictable
- Supports multi-pane interfaces without modal confusion
- Preserves spatial orientation when screens remain visually stable.[^spatial-memory]

Observed in:

- Lazygit
- k9s
- bottom
- Helix

Mono fit:

- Extends the standard's focus requirements into a named pane-level pattern
- Especially important for split views, dashboards, and browser screens

Audit checklist:

- Exactly one interactive surface is focused at a time.
- Focus indication is visible without relying only on color.
- Moving focus changes the footer/help/action scope.
- Removing a focused surface transfers focus predictably.
- Users can tell whether a row is selected, a pane is focused, or both.

### Master-Detail

Definition:

A browse surface controls a secondary detail or preview surface without requiring full navigation to another screen.

Why it exists:

- Preserves orientation
- Keeps overview and inspection together
- Reduces navigation churn
- Supports progressive disclosure without abandoning the current frame.[^progressive-disclosure]

Observed in:

- Lazygit
- k9s
- bottom

Mono fit:

- Natural use of Region B for browsing and Region C for detail
- Useful wherever selected objects have meaningful metadata or preview content

Audit checklist:

- Selection updates the detail area immediately.
- The detail area adds context rather than duplicating the list.
- The user can still act on the selected object without leaving the screen.
- Detail collapse or hide behavior is defined at compact widths.
- Returning from a full detail view restores the originating selection.

### Expand-to-Focus

Definition:

A dense panel or widget can temporarily expand into the primary content area while preserving its identity, state, and command model.

Why it exists:

- Resolves small-terminal density
- Avoids fragmenting one screen into many separate variants
- Supports progressive disclosure without changing mental models

Observed in:

- bottom
- k9s, by implication in detail views

Mono fit:

- Best for Dashboard and monitoring-heavy screens
- Useful for responsive breakpoints and compact layouts

Audit checklist:

- Expanded mode preserves the same object, commands, and data model.
- Collapse returns the user to the prior layout and focus position.
- Expansion meaning is clear from the UI.
- Expanded mode is not required to complete ordinary tasks.
- Compact layouts have a defined path to expansion for dense widgets.

### Object-Local Actions

Definition:

Commands apply to the current selection or focused object by default rather than through detached global workflows.

Why it exists:

- Makes command targets obvious
- Shortens task flow
- Improves confidence for destructive or high-cost actions

Observed in:

- Lazygit
- k9s
- Helix

Mono fit:

- Strong fit for lists, trees, queues, records, and file/resource browsers
- Works best when selection state is explicit

Audit checklist:

- The current target object is visually explicit.
- Primary actions operate on the selected object without extra targeting steps.
- Confirmation dialogs name the affected object.
- Global actions are limited to truly global scope.
- Empty-selection behavior is handled explicitly.

### Command Jump

Definition:

Users can navigate directly to screens, views, resources, or commands through an addressable command input rather than only through stepwise navigation.

Why it exists:

- Compresses navigation distance
- Rewards expertise without removing visible paths
- Scales well in multi-view products

Observed in:

- k9s
- Helix

Mono fit:

- Best as an optional expert layer
- Strong fit for large operational tools and multi-screen applications

Audit checklist:

- Command input is optional, not mandatory.
- Every important destination also has a visible non-command path.
- Command results are predictable and scoped.
- Unknown commands fail clearly and recoverably.
- The command surface does not conflict with ordinary text entry modes.

### Selection Grammar

Definition:

The primary interaction model is “select target, then act” or “select range, then transform.” Selection is a visible part of the grammar, not a side effect.

Why it exists:

- Clarifies user intent
- Reduces hidden state
- Enables composable actions
- Improves visual confirmation before commitment in editing and review tasks.[^direct-manipulation]

Observed in:

- Helix
- Lazygit
- k9s

Mono fit:

- Useful for editors, queues, browsers, inspectors, and multi-select flows
- Especially important where destructive or batch actions exist

Audit checklist:

- Selection state is persistent enough to trust.
- Selection and focus are visually distinguishable if both exist.
- Actions describe whether they apply to the current item, current selection, or whole view.
- Batch actions behave consistently with single-item actions.
- Selection survives short navigation flows where continuity matters.

### Live Drill-Down

Definition:

A screen presents real-time overview data and allows immediate drill-down into anomalies, items, or alerts without leaving the operational context.

Why it exists:

- Supports monitoring and intervention in one shell
- Preserves situational awareness
- Reduces the cost of switching between overview and investigation

Observed in:

- k9s
- btop
- bottom

Mono fit:

- Strong fit for Dashboard and Monitor-Respond flows
- Can also support Review-Approve and CRUD hubs where live state matters

Audit checklist:

- The overview remains legible during live updates.
- The user can drill into a live item directly from the overview.
- Auto-refresh does not destroy scroll position or selection.
- Returning from drill-down restores the prior overview state.
- Health, anomaly, or status changes are visible without opening detail first.

## Companion Practices

These are not primary cross-archetype patterns on the same level as the appendix above, but they are recurring interaction practices worth preserving in Mono implementations.

### Filtered Help

Help should usually be filtered to the focused pane, active layer, or current object scope rather than presented as a global command dump. This works especially well in context-panel, modal, and prefix-driven interfaces.[^recognition-recall]

### Command Transparency

Applications that wrap an underlying CLI or external toolchain MAY expose the raw command, request, or operation log in a secondary status region. This improves trust, teaches the underlying system, and reduces the sense that the interface is doing hidden magic.

### Discoverable Prefix Continuations

When a prefix or leader key opens a temporary command layer, applications SHOULD expose available continuations in a lightweight popup or status hint rather than relying entirely on memory.[^progressive-disclosure]

### Provenance and Lineage Views

Operational tools SHOULD consider a lineage view that explains why an object exists, what owns it, or what it is connected to. This is especially useful in hierarchical systems where object provenance is otherwise opaque.

## Key Set Appendix

Key sets are coherent clusters of bindings that should be used together across related screens. They complement the standard's keyboard rules by making screen families feel internally consistent.

Consistency rules:

- A key's meaning should stay stable across screens that share a key set.
- Applications should not reuse the same single-letter key for different domain actions on sibling screens in the same key set.
- If a screen changes key sets, the footer or status area should make that obvious immediately.
- Arrow keys remain within one control. Pane, widget, or view switching should use Tab/Shift+Tab, numbered views, or other non-arrow bindings.

### Browse/Inspect Set

Use together on list, table, and resource browser screens:

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

Use together on live dashboards and operational consoles:

- `r` = refresh
- `/` = filter stream or item list
- Enter = inspect current anomaly or row
- `a` = acknowledge or act
- `s` = sort current table
- `1`–`9` = switch views or dashboards
- Tab / Shift+Tab = switch focused panel

### Search/Select Set

Use together on fuzzy finders, pickers, and command palettes:

- printable input = append to filter
- Ctrl+N / Ctrl+P or Up / Down = move through results
- Enter = select
- Esc = cancel
- Tab = toggle preview or advance preview focus

### Edit/Transform Set

Use together on editors and structured review surfaces:

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

## Pattern Guidance by Archetype

### Dashboard

Best pattern set:

- Footer Command Bar
- Focused Surface
- Object-Local Actions
- Live Drill-Down

Optional additions:

- Expand-to-Focus
- Master-Detail
- Selection Grammar
- Command Jump

### Admin / Config

Best pattern set:

- Footer Command Bar

Optional additions:

- Focused Surface for multi-pane settings screens
- Master-Detail for category list plus form detail
- Object-Local Actions for editable records or setting groups

Patterns usually avoided:

- Live Drill-Down
- Expand-to-Focus
- Command Jump unless the product is unusually large

### File Manager

Best pattern set:

- Footer Command Bar
- Focused Surface
- Master-Detail
- Object-Local Actions

Optional additions:

- Selection Grammar
- Expand-to-Focus
- Live Drill-Down in preview-heavy or live-refresh variants

### Editor

Best pattern set:

- Footer Command Bar
- Focused Surface
- Selection Grammar

Optional additions:

- Object-Local Actions
- Command Jump

Patterns usually avoided:

- Expand-to-Focus
- Live Drill-Down
- classic Master-Detail except in picker or sidecar views

### Fuzzy Finder

Best pattern set:

- Footer Command Bar
- Focused Surface
- Selection Grammar

Optional additions:

- Master-Detail through an optional preview pane
- Object-Local Actions when result actions vary

Patterns usually avoided:

- Expand-to-Focus
- Command Jump inside the finder itself
- Live Drill-Down

## Review Use

This pattern library is meant to support design and implementation review. A reviewer can use it in three passes:

1. Identify the screen archetype.
2. Check which patterns are required or optional for that archetype.
3. Run the corresponding pattern audit checklists against the implementation.

## Relationship to the Standard

This library is intentionally aligned with existing Monospace TUI rules:

- Footer Command Bar extends the footer key strip.
- Focused Surface extends explicit focus-state requirements.
- Master-Detail extends the three-region layout and contextual pane model.
- Expand-to-Focus complements responsive layout behavior.
- Object-Local Actions complements Tier 2 contextual actions.
- Command Jump complements composable keyboard layers and command-mode patterns.
- Selection Grammar complements editor, finder, and review-oriented interaction models.
- Live Drill-Down complements Dashboard and Monitor-Respond workflows.

The pattern names make these behaviors easier to discuss, apply, and audit consistently across applications.

[^cui-aesthetic]: Historical terminal systems and modern TUIs both show that strong visual identity and atmospheric rendering can improve orientation, brand, and perceived quality when semantic state remains legible.
[^recognition-recall]: Recognition over recall is a long-standing usability principle; filtering actions and help to the current surface reduces memory burden in dense interfaces.
[^spatial-memory]: Stable panel locations and visible anchors support spatial memory in multi-pane environments.
[^progressive-disclosure]: Progressive disclosure reduces cognitive load by revealing detail when a user signals intent instead of front-loading all complexity.
[^direct-manipulation]: Visual confirmation before commit is a core strength of direct-manipulation systems and maps well to selection-first editing models.
