---
title: "Wireframes"
weight: 20
---

# TUI-First Wireframes

In Monospace Designer, wireframes are strictly structured, low-fidelity representations of a screen.

They are generated deterministically from a machine-readable `ScreenSpec` YAML file. You do not "draw" a wireframe; you define its structure, and the Designer projects it into an ASCII wireframe.

## The YAML Screen Specification

A `ScreenSpec` defines the *semantics* of a terminal UI, not its exact layout logic or styling. The Designer relies on the Monospace Standard's [Archetypes](../../standard/archetypes) and [Patterns](../../patterns/) to govern the exact placement of elements.

### Metadata

Every screen requires metadata linking it to the workflow and defining its primary archetype. The `archetype` dictates the layout boundaries (e.g., a `dashboard` implies strong multi-panel structures, while a `fuzzy-finder` implies an overlaid popup).

```yaml
kind: screen
id: dashboard-system-monitor
title: System Monitor
purpose: Monitor key service and resource status
workflow_id: wf-alert-triage
archetype: dashboard
patterns: [focused-surface, live-drill-down]
entry_conditions: [system active]
```

### Regions & Components

Instead of X/Y coordinates, a TUI screen is divided into named, semantic `regions`. Components are then placed inside those regions.

```yaml
regions:
  - { id: header, type: header, role: metrics }
  - { id: region_b, type: region_b, role: primary-data }
  - { id: footer, type: footer, role: commands }

components:
  - { id: metric-cards, type: summary, region: header, purpose: key metrics }
  - { id: service-table, type: table, region: region_b, purpose: service status list }
```

### Interactions & Discoverability

A TUI must be fully navigable via the keyboard. The `ScreenSpec` enforces this by making focus and footer keys explicit requirements of the design process.

```yaml
actions:
  - { id: refresh, label: Refresh, target: service-table, kind: global }

focus: 
  default_target: service-table
  focus_order: [service-table]

footer_keys:
  - { key: "?", label: Help, scope: screen }
  - { key: "r", label: Refresh, scope: screen }
  - { key: "/", label: Filter, scope: screen }
  - { key: "q", label: Quit, scope: screen }
```

*Note: The `mono-designer` linter will flag an error if a screen contains interactive components (like lists or inputs) that are missing from the `focus_order`, or if `actions` lack corresponding `footer_keys`.*

## ASCII Projection

The `mono-designer project` tool converts the `ScreenSpec` into a standard ASCII wireframe. This is the artifact you review during the design phase.

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│                   System Monitor (dashboard-system-monitor)                  │
├──────────────────────────────────────────────────────────────────────────────┤
│ [HEADER] metrics                                                             │
│   • metric-cards (summary): key metrics                                      │
│                                                                              │
│ [REGION_B] primary-data                                                      │
│   • service-table (table): service status list                               │
│                                                                              │
├──────────────────────────────────────────────────────────────────────────────┤
│ ACTIONS: Refresh                                                             │
├──────────────────────────────────────────────────────────────────────────────┤
│ [?] Help [r] Refresh [/] Filter [q] Quit                                     │
└──────────────────────────────────────────────────────────────────────────────┘
```

The wireframe forces designers and AI agents to confront the realities of terminal real estate:
1. Is there too much dense text?
2. Are the interaction targets clearly defined?
3. Are the hotkeys discoverable?

If the ASCII layout feels cluttered, the design must be revised and broken down into further workflow stages.

## Validating Projections

The Designer tools include an end-to-end verification harness. When an AI agent generates this ASCII, the system automatically runs a reverse-projection check. It parses the ASCII regions, extracts the components and keys, and strictly verifies that *100% of the semantic meaning* from the `dsl.yaml` survived the projection.