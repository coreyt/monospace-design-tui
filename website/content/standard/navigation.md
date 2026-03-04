---
title: "§3 Navigation Topology"
description: "Navigation patterns, menu hierarchy, action bar order, unavailable items"
weight: 3
---

## §3.1 Navigation Pattern Decision Tree

Choose the navigation pattern based on the relationship between views:

| Relationship | Pattern | Implementation |
|-------------|---------|---------------|
| Parallel contexts (peer-level views) | Tabs or sidebar items | Region A list or tab bar |
| Hierarchical drill-down | Screens (push/pop) | New screen replaces content |
| Transient confirmation or input | Modal dialog | Overlay with scrim |
| Contextual detail for selected item | Panel (split or overlay) | Region C or overlay pane |

Applications MUST NOT mix patterns for the same relationship type within a single workflow. (CUA §1, M3 §3 navigation patterns, tui-architect navigation topology)

## §3.2 Menu Hierarchy

Menus MUST follow a maximum three-level hierarchy:

1. **Action Bar** — top row, ≤6 items.
2. **Pull-Down Menu** — vertical list below action bar item, ≤10 items per menu.
3. **Cascaded Menu** — extends to the right, indicated by `▸` suffix, ≤1 level of cascading.

Applications MUST NOT cascade menus more than one level deep. (CUA §1 standard menu hierarchy)

## §3.3 Action Bar Order

When an action bar is present, items MUST appear in this standard order (omitting inapplicable items):

```
File  Edit  View  [Domain-specific]  Options  Help
```

- `File` and `Help` MUST be present if the application has an action bar.
- Domain-specific items (e.g., `Models`, `Guardrails`) appear between `View` and `Options`.
- Maximum 6 top-level items.

(CUA §1)

## §3.4 Unavailable Items

Menu items and controls that are currently unavailable MUST remain visible but rendered in the Disabled state (dim text, SGR 2). Unavailable items MUST NOT be hidden. This ensures users can discover features and understand why they are currently inaccessible. (CUA §1, Apple HIG §4)

## §3.5 Ellipsis Convention

A menu item that will open a dialog requiring further user input before executing MUST display an ellipsis suffix (`...`). A menu item that executes immediately MUST NOT display an ellipsis. (CUA §1)
