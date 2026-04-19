# Mono Designer E2E Test Harness Design

## Overview

The E2E Test Harness is a "Reversed Projection" validator. It reads a
projected ASCII wireframe and verifies that the semantic information extracted
from it matches the source YAML specification.

Crucially, this harness must act as a **cleanroom verification mechanism**. To
ensure true independence and prevent the accidental reuse of the main Python
`mono_designer` parsing logic or Pydantic models, the harness is written in a
different language ecosystem: **Go**.

## Architecture

The harness operates entirely independent of the main Python tooling.

### 1. Technology Stack

- **Language**: Go (Golang)
- **Dependencies**: `gopkg.in/yaml.v3` for loading source DSLs and
  `github.com/santhosh-tekuri/jsonschema/v5` for JSON Schema validation.
- **Execution**: Compiled to a single static binary or run via `go run main.go`.

### 2. Pipeline

1. **YAML Validation**: Loads the canonical schema and runs the incoming YAML
   against it to guarantee the input is structurally sound.
2. **YAML Loader**: Unmarshals the valid YAML into generic Go
   `map[string]interface{}` values. No redundant Go structs are needed because
   the schema already verified the data structure.
3. **ASCII State-Machine Parser**: Uses Go's `bufio.Scanner` to read the
   `.txt` ASCII file line-by-line, transitioning through states based on
   structural cues and extracting semantic properties via `regexp`.
4. **Comparator**: A strict or subset equality engine that asserts the Go data
   structures extracted from ASCII cover the data loaded from YAML.

## Detailed Design: Line-by-Line Regex State Machines

Because TUI widths and layouts can shift, the parser explicitly avoids
coordinate-based logic. Instead, it relies on line-by-line scanning governed by
a state machine that transitions on structural markers.

Below are the state machine and regex designs for each of the three core
artifact types, using the `dev/designer/examples/` as references.

---

### Artifact 1: Navigation Spec

**Example Pair:** `file-workbench/dsl.yaml` & `ascii.txt`

**ASCII Output Structure:**
```text
┌────────────────────────── File Workbench ────────────────────────┐
│ [Browser]                                                        │
│ [Editor]                                                         │
│ [Search]                                                         │
├──────────────────────────────────────────────────────────────────┤
│ Browser -> open file -> Editor                                   │
├──────────────────────────────────────────────────────────────────┤
│ browser hub | transient search | preserve editor context         │
└──────────────────────────────────────────────────────────────────┘
```

**Parser State Machine:**
*   **State: `START`**
    *   *Trigger*: Match `^┌─+(.+?)─+┐$`
    *   *Action*: Extract `title` from Group 1. Transition to `WORKSPACES`.
*   **State: `WORKSPACES`**
    *   *Trigger*: Match `^│\s*\[(.*?)\]\s*│$`
    *   *Action*: Extract `workspace.label` from Group 1.
    *   *Trigger*: Match `^├─+┤$` -> Transition to `ROUTES`.
*   **State: `ROUTES`**
    *   *Trigger*: Match `^│\s*(.+?)\s*->\s*(.+?)\s*->\s*(.+?)(?:\s*\(.*?\))?\s*│$`
    *   *Action*: Extract `route.from` (Grp 1), `route.trigger` (Grp 2), `route.to` (Grp 3).
    *   *Trigger*: Match `^├─+┤$` -> Transition to `RULES`.
*   **State: `RULES`**
    *   *Trigger*: Match `^│\s*(.*?)\s*│$`
    *   *Action*: Split Group 1 by `|` to extract the `rules` array.
    *   *Trigger*: Match `^└─+┘$` -> Transition to `DONE`.

---

### Artifact 2: Workflow Spec

**Example Pair:** `drill-down-topic-explorer/dsl.yaml` & `ascii.txt`

**ASCII Output Structure:**
```text
Workflow: Topic Explorer

- Overview
- Topic List
- Topic Detail
- Source Detail

Back path: breadcrumb / Esc
```

**Parser State Machine:**
*   **State: `START`**
    *   *Trigger*: Match `^Workflow:\s+(.+)$`
    *   *Action*: Extract `title`. Transition to `SEEKING_STAGES`.
*   **State: `SEEKING_STAGES`**
    *   *Trigger*: Blank line (Ignore).
    *   *Trigger*: Match `^-\s+(.+)$`
    *   *Action*: Extract `stage.label` from Group 1. Transition to `STAGES`.
*   **State: `STAGES`**
    *   *Trigger*: Match `^-\s+(.+)$` -> Extract `stage.label`.
    *   *Trigger*: Blank line -> Transition to `METADATA`.
*   **State: `METADATA`**
    *   *Trigger*: Match `^Back path:\s+(.+)$` -> Extract assumption/notes.
    *   *Trigger*: EOF -> Transition to `DONE`.

---

### Artifact 3: Screen Spec

**Example Pair:** `dashboard-system-monitor/dsl.yaml` & `ascii.txt`

**ASCII Output Structure:**
```text
┌────────────────────── System Monitor ──────────────────────┐
│ metric cards                                               │
├────────────────────────────────────────────────────────────┤
│ service status table                                       │
│ > current row                                              │
├────────────────────────────────────────────────────────────┤
│ ? Help  r Refresh  / Filter  q Quit                        │
└────────────────────────────────────────────────────────────┘
```

**Parser State Machine:**
*   **State: `START`**
    *   *Trigger*: Match `^┌─+(.+?)─+┐$` -> Extract `title`. Transition to `HEADER_REGION`.
*   **State: `HEADER_REGION`**
    *   *Trigger*: Match `^│\s*(.+?)\s*│$` -> Extract `component.purpose/label`.
    *   *Trigger*: Match `^├─+┤$` -> Transition to `BODY_REGION`.
*   **State: `BODY_REGION`**
    *   *Trigger*: Match `^│\s*>\s*(.+?)\s*│$` -> Extract focus state (`focus.default_target`).
    *   *Trigger*: Match `^│\s*(.+?)\s*│$` -> Extract `component.purpose/label`.
    *   *Trigger*: Match `^├─+┤$` -> Transition to `FOOTER_REGION`.
*   **State: `FOOTER_REGION`**
    *   *Trigger*: Match `^│\s*(.+?)\s*│$`
    *   *Action*: Execute global regex `([A-Za-z0-9\?\/])\s+([A-Za-z]+)` across Group 1 to extract an array of `footer_keys` (e.g., `key="?", label="Help"`).
    *   *Trigger*: Match `^└─+┘$` -> Transition to `DONE`.

## Comparison & Verification Strategy

After parsing the ASCII into Go data structures, the harness loads the canonical `dsl.yaml`.
The verification engine applies a **subset mapping** strategy (to allow visual fillers in ASCII):

1.  **Existence**: Assert `YAML.title` is substring of `ASCII.title`.
2.  **Navigation Match**: For each `YAML.workspaces`, assert `workspace.label` exists in `ASCII.workspaces`.
3.  **Workflow Match**: For each `YAML.stages`, assert `stage.label` exists in `ASCII.stages` in the exact same order.
4.  **Screen Match**: For each `YAML.components`, assert `component.purpose` or `id` was found in one of the regions. For each `YAML.footer_keys`, assert `key` and `label` match the extracted footer object.

## Failure Reporting

The harness will output explicit failures:
- `MISSING_WORKSPACE`: "Workspace label 'Browser' defined in YAML was not found in the ASCII."
- `ORDER_MISMATCH`: "Stage 'Topic Detail' appeared before 'Topic List' in the ASCII."
- `MISSING_FOOTER_KEY`: "Key '?' (Help) was defined in YAML but not detected in the ASCII footer region."
