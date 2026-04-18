# Mono Designer Examples

This directory contains example artifacts for the `0.3.0` designer system.

Each example follows the same shape:

- `spec.yaml` — canonical YAML artifact
- `dsl.yaml` — normalized minimal semantic DSL form
- `ascii.txt` — projected review output

## Monospace Reference Screens

These are the canonical example screens already present in Monospace Design TUI
and should be treated as the first visual references for the designer layer.

1. `Dashboard — System Monitor`
   A dashboard archetype example with header metrics, a live data table, and a
   footer command strip.
2. `Admin — Application Settings`
   An admin/config archetype example with category navigation, forms, and save
   actions.
3. `File Manager — Dual Pane`
   A file-manager archetype example using the orthodox dual-pane layout.
4. `Editor — Code Editing`
   An editor archetype example with a text buffer, status line, and footer.
5. `Fuzzy Finder — Command Palette`
   A fuzzy-finder archetype example with filter input, ranked results, preview,
   and fuzzy-layer footer keys.
6. `Dialog — Confirm Delete`
   A modal dialog example showing Level 4 elevation and destructive-action
   confirmation.

The designer examples below extend those references into a broader `0.3.0`
artifact set for navigation, workflows, and screen generation.

## Screen Archetypes

These come directly from Monospace Design TUI `§11`.

### 1. Dashboard

Definition:

- a screen for operational awareness, monitoring, queue state, or system status
- optimized for fast scanning and quick drill-down into anomalies

Typical structure:

- header metrics or summary cards
- primary table, list, or stream in Region B
- optional inspector/detail pane
- footer command strip

Reference examples:

- `Dashboard — System Monitor`
- `dashboard-system-monitor`
- `dashboard-run-activity`
- `dashboard-collection-review`

### 2. Admin / Config

Definition:

- a screen for setup, settings, forms, approval checkpoints, or structured
  editing of a single object
- optimized for field entry, review, and save/continue actions

Typical structure:

- category list, summary pane, or step indicator
- form or structured review pane
- clear primary action row
- footer command strip

Reference examples:

- `Admin — Application Settings`
- `admin-request-form`
- `admin-scope-refinement`
- `admin-settings`

### 3. File Manager

Definition:

- a screen for navigating collections, hierarchies, directories, or evidence
  sets
- optimized for browse, select, compare, and object-local actions

Typical structure:

- dual panes, Miller-style columns, or browse/detail split
- stable current path or breadcrumb
- object actions localized to the focused pane
- footer command strip

Reference examples:

- `File Manager — Dual Pane`
- `file-manager-topic-browser`
- `file-manager-source-explorer`
- `file-manager-source-select`

### 4. Editor

Definition:

- a screen for drafting, annotating, refining, or reviewing text-heavy content
- optimized for focused editing or side-by-side inspection

Typical structure:

- main document or workspace area
- optional inspector or companion document pane
- status line
- footer command strip

Reference examples:

- `Editor — Code Editing`
- `editor-analysis-workspace`
- `editor-report-draft`
- `editor-item-review`

### 5. Fuzzy Finder

Definition:

- a screen or overlay for rapid type-to-filter search and selection
- optimized for narrowing a large set to one next action

Typical structure:

- query input at the top
- ranked results list
- optional preview pane
- minimal footer with fuzzy-layer keys

Reference examples:

- `Fuzzy Finder — Command Palette`
- `fuzzy-command-palette`
- `fuzzy-topic-search`
- `fuzzy-source-jump`

## Workflow Archetypes

These come directly from Monospace Design TUI `§12`.

### 1. Wizard

Definition:

- a linear, step-by-step flow for infrequent or guided setup tasks

Navigation model:

- sequential / linear

Use when:

- the user should move through a fixed set of steps in order
- validation gates each transition forward

### 2. CRUD

Definition:

- a list to detail to edit cycle for managing records

Navigation model:

- hub-and-spoke

Use when:

- the list is the operational home
- the user repeatedly opens, edits, creates, or deletes records

### 3. Monitor-Respond

Definition:

- a live operational loop where the user observes state, inspects an issue, and
  optionally acts

Navigation model:

- hub-and-spoke with a live dashboard hub

Use when:

- the dashboard must remain the stable point of return
- action dialogs and detail views are short-lived spokes

### 4. Search-Act

Definition:

- a funnel flow where the user searches, narrows, previews, and then acts

Navigation model:

- funnel

Use when:

- the dominant interaction is finding one thing in a large set
- direct browsing would be too slow

### 5. Drill-Down

Definition:

- a hierarchical flow from overview to category to item to detail

Navigation model:

- hierarchical / tree

Use when:

- content is naturally nested
- the user benefits from breadcrumbs and a preserved back path

### 6. Pipeline

Definition:

- a staged transformation flow with preview before execution

Navigation model:

- sequential with preview loop

Use when:

- the user configures a multi-stage process and needs to inspect intermediate
  results before running it

### 7. Review-Approve

Definition:

- a queue-based decision flow where items are opened, decided, and then
  advanced automatically

Navigation model:

- queue

Use when:

- the user repeatedly approves, rejects, comments on, or defers queued items

### 8. Configuration

Definition:

- a non-linear settings flow where users move freely across categories or tabs

Navigation model:

- flat / lateral

Use when:

- there is no required order
- unsaved changes must survive category switches

## Navigation Patterns

These are defined here for the designer layer using Mono’s navigation topology
and workflow model.

### 1. Hub-and-Spoke

Definition:

- one stable home screen or root workspace
- secondary screens return to the hub instead of chaining deeper

Use when:

- the app has a clear home dashboard, queue, or main menu
- most tasks begin and end from the same screen

### 2. Hierarchical Drill-Down

Definition:

- users move from broad overview to narrower levels
- each step preserves a visible back path and local state

Use when:

- topics, files, directories, categories, or entities are nested

### 3. Lateral Workspace Switching

Definition:

- top-level sections are peers at the same hierarchy level
- users switch directly among them

Use when:

- the app has distinct workspaces such as Research, Analysis, Reports, and
  Settings

### 4. Contextual Panel Navigation

Definition:

- the overall frame stays stable while focus and detail move between panes
- detail deepens in place instead of replacing the whole screen

Use when:

- master-detail or inspector layouts are the dominant interaction pattern

## Example Sets

The current `0.3.0` example set includes:

- `2` navigation examples
- `3` workflow examples
- `15` screen examples

### Navigation Examples

1. `research-ops-hub`
2. `file-workbench`

### Workflow Examples

1. `wizard-onboarding`
2. `monitor-respond-alert-triage`
3. `drill-down-topic-explorer`

### Screen Examples

1. `dashboard-system-monitor`
2. `dashboard-run-activity`
3. `dashboard-collection-review`
4. `admin-request-form`
5. `admin-scope-refinement`
6. `admin-settings`
7. `file-manager-topic-browser`
8. `file-manager-source-explorer`
9. `file-manager-source-select`
10. `editor-analysis-workspace`
11. `editor-report-draft`
12. `editor-item-review`
13. `fuzzy-command-palette`
14. `fuzzy-topic-search`
15. `fuzzy-source-jump`
