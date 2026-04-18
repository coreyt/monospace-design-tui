# Mono Designer Component Designs

## Purpose

This document defines the concrete `0.3.0` designer components in one place.

For each component, it specifies:

- component name
- purpose
- input
- output
- work to do
- pseudocode
- tests to consider

This document stays scoped to `0.3.0`.

## 1. Input Collector

### Purpose

Collect and normalize the design inputs needed to start a design-generation
session.

### Input

Comes in from:

- user prompt
- project notes
- optional codebase hints
- optional `TUI-DESIGN.md`

Interface:

- function call
- agent tool invocation

Suggested interface:

```python
collect_inputs(
    user_request: str,
    project_paths: list[str] | None = None,
    tui_design_path: str | None = None,
) -> DesignerInputSet
```

### Output

Produces:

- normalized `DesignerInputSet`

To:

- Designer Agent
- Navigation Generator
- Workflow Generator

### Work To Do

- read user request
- load `TUI-DESIGN.md` if present
- gather referenced notes/files
- classify input kinds
- normalize into a structured input bundle

### Pseudocode

```python
def collect_inputs(user_request, project_paths=None, tui_design_path=None):
    inputs = DesignerInputSet()
    inputs.user_request = user_request
    if tui_design_path:
        inputs.project_overrides = load_tui_design(tui_design_path)
    for path in project_paths or []:
        inputs.documents.append(read_text(path))
    return normalize_inputs(inputs)
```

### Tests To Consider

- no `TUI-DESIGN.md` present
- valid `TUI-DESIGN.md` present
- multiple notes present
- invalid input path
- empty user request

## 2. Override Loader

### Purpose

Load and expose project-specific Mono overrides and conventions.

### Input

Comes in from:

- path to `TUI-DESIGN.md`

Suggested interface:

```python
load_tui_design(path: str) -> ProjectOverrides
```

### Output

Produces:

- `ProjectOverrides`

To:

- Designer Agent
- Generators
- Revision Tool

### Work To Do

- parse `TUI-DESIGN.md`
- extract palette
- extract archetypes
- extract overrides
- extract project conventions

### Pseudocode

```python
def load_tui_design(path):
    text = read_text(path)
    doc = parse_markdown_sections(text)
    return ProjectOverrides(
        palette=parse_palette(doc),
        archetypes=parse_archetypes(doc),
        overrides=parse_overrides(doc),
        conventions=parse_conventions(doc),
    )
```

### Tests To Consider

- missing file
- malformed override heading
- valid palette
- unknown palette
- scoped overrides

## 3. Navigation Generator

### Purpose

Generate the canonical navigation spec YAML.

### Input

Comes in from:

- `DesignerInputSet`
- `ProjectOverrides`

Suggested interface:

```python
generate_navigation(
    inputs: DesignerInputSet,
    overrides: ProjectOverrides | None,
) -> NavigationSpec
```

### Output

Produces:

- `NavigationSpec`

To:

- artifact store
- workflow generator
- navigation projector

### Work To Do

- determine top-level workspaces
- identify navigation rules
- define major routes
- produce stable navigation IDs

### Pseudocode

```python
def generate_navigation(inputs, overrides=None):
    workspaces = infer_workspaces(inputs)
    rules = infer_navigation_rules(inputs, overrides)
    routes = infer_routes(workspaces, rules)
    return NavigationSpec(
        id="nav-main",
        title="Main Navigation",
        workspaces=workspaces,
        routes=routes,
        rules=rules,
    )
```

### Tests To Consider

- single-workflow app
- multi-workspace app
- conflicting navigation intent
- explicit project navigation constraint

## 4. Workflow Generator

### Purpose

Generate canonical workflow spec YAML.

### Input

Comes in from:

- `DesignerInputSet`
- `ProjectOverrides`
- optional `NavigationSpec`

Suggested interface:

```python
generate_workflows(
    inputs: DesignerInputSet,
    navigation: NavigationSpec | None,
    overrides: ProjectOverrides | None,
) -> list[WorkflowSpec]
```

### Output

Produces:

- one or more `WorkflowSpec`

To:

- artifact store
- screen generator
- workflow projector

### Work To Do

- identify workflows
- define stages
- define transitions
- define HITL checkpoints
- assign stable workflow IDs

### Pseudocode

```python
def generate_workflows(inputs, navigation=None, overrides=None):
    workflow_intents = infer_workflow_intents(inputs)
    workflows = []
    for intent in workflow_intents:
        workflows.append(
            WorkflowSpec(
                id=make_workflow_id(intent),
                title=intent.title,
                purpose=intent.purpose,
                entry_conditions=infer_entry_conditions(intent),
                exit_conditions=infer_exit_conditions(intent),
                stages=infer_stages(intent),
                transitions=infer_transitions(intent),
                checkpoints=infer_checkpoints(intent),
                assumptions=infer_assumptions(intent),
            )
        )
    return workflows
```

### Tests To Consider

- workflow with no explicit checkpoints
- workflow with required approval gates
- workflow spanning multiple workspaces
- ambiguous workflow boundaries

## 5. Screen Generator

### Purpose

Generate canonical screen spec YAML from workflows and Mono patterns.

### Input

Comes in from:

- `WorkflowSpec`
- `ProjectOverrides`
- optional `NavigationSpec`

Suggested interface:

```python
generate_screens(
    workflows: list[WorkflowSpec],
    navigation: NavigationSpec | None,
    overrides: ProjectOverrides | None,
) -> list[ScreenSpec]
```

### Output

Produces:

- one or more `ScreenSpec`

To:

- artifact store
- screen projector

### Work To Do

- determine screen inventory
- assign screen IDs
- assign archetypes
- assign Mono patterns
- assign regions/components/actions/focus/transitions

### Pseudocode

```python
def generate_screens(workflows, navigation=None, overrides=None):
    screens = []
    for workflow in workflows:
        for stage in workflow.stages:
            screen = build_screen_from_stage(stage, workflow, overrides)
            screens.append(screen)
    return screens
```

### Tests To Consider

- one stage -> one screen
- one stage -> multiple screens
- hybrid archetype assignment
- missing pattern assignment
- missing footer keys

## 6. YAML Validator

### Purpose

Validate navigation, workflow, and screen YAML artifacts.

### Input

Comes in from:

- YAML text
- parsed YAML object

Suggested interface:

```python
validate_spec(spec: dict | object) -> ValidationResult
```

### Output

Produces:

- `ValidationResult`

To:

- loaders
- generators
- revision tool
- projectors

### Work To Do

- validate required fields
- validate field types
- validate references
- validate IDs

### Pseudocode

```python
def validate_spec(spec):
    errors = []
    check_required_fields(spec, errors)
    check_types(spec, errors)
    check_ids(spec, errors)
    return ValidationResult(ok=not errors, errors=errors)
```

### Tests To Consider

- missing `artifact_type`
- missing `id`
- bad region shape
- bad transition references
- invalid footer key entries

## 7. YAML Repository / Artifact Store

### Purpose

Persist canonical YAML artifacts and load them reliably.

### Input

Comes in from:

- generators
- revision tool
- agent requests

Suggested interface:

```python
save_spec(path: str, spec: object) -> None
load_spec(path: str) -> object
list_specs(base_dir: str, artifact_type: str | None = None) -> list[str]
```

### Output

Produces:

- canonical YAML files on disk
- loaded spec objects

To:

- projectors
- agent
- revision tool

### Work To Do

- save canonical field ordering
- preserve stable structure
- load by type
- support artifact directory layout

### Pseudocode

```python
def save_spec(path, spec):
    text = dump_yaml_canonical(spec)
    write_text(path, text)

def load_spec(path):
    text = read_text(path)
    data = parse_yaml(text)
    validate_spec(data)
    return normalize_spec(data)
```

### Tests To Consider

- save/load round trip
- field order stability
- preserving unknown fields
- duplicate IDs

## 8. DSL Normalizer

### Purpose

Normalize YAML artifacts into the minimal semantic `0.3.0` DSL shape used by
projectors.

### Input

Comes in from:

- `NavigationSpec`
- `WorkflowSpec`
- `ScreenSpec`

Suggested interface:

```python
normalize_to_dsl(spec: object) -> DSLNode
```

### Output

Produces:

- normalized DSL node

To:

- ASCII projectors

### Work To Do

- normalize region semantics
- normalize component semantics
- normalize inspector/detail representation
- normalize focus and state representation

### Pseudocode

```python
def normalize_to_dsl(spec):
    if spec.artifact_type == "screen":
        return normalize_screen_spec(spec)
    if spec.artifact_type == "workflow":
        return normalize_workflow_spec(spec)
    if spec.artifact_type == "navigation":
        return normalize_navigation_spec(spec)
    raise ValueError("unsupported artifact type")
```

### Tests To Consider

- inspector as region vs detail component
- action group normalization
- footer key normalization
- state alias normalization

## 9. Navigation ASCII Projector

### Purpose

Project a navigation artifact into ASCII.

### Input

Comes in from:

- normalized navigation DSL node

Suggested interface:

```python
project_navigation_ascii(node: DSLNode) -> str
```

### Output

Produces:

- ASCII navigation overview

To:

- agent response
- review loop
- design docs

### Work To Do

- render app title
- render workspaces
- render major routes
- keep layout compact and readable

### Pseudocode

```python
def project_navigation_ascii(node):
    lines = []
    lines.append(box_title(node.title))
    for workspace in node.workspaces:
        lines.append(f"│ [{workspace.label}]")
    lines.append(box_footer("navigation overview"))
    return "\n".join(lines)
```

### Tests To Consider

- many workspaces
- no routes
- compact formatting
- deterministic output

## 10. Workflow ASCII Projector

### Purpose

Project a workflow artifact into ASCII.

### Input

Comes in from:

- normalized workflow DSL node

Suggested interface:

```python
project_workflow_ascii(node: DSLNode) -> str
```

### Output

Produces:

- ASCII workflow outline

To:

- agent response
- review loop

### Work To Do

- render stages in order
- render transitions
- render checkpoints
- render linked screens if useful

### Pseudocode

```python
def project_workflow_ascii(node):
    lines = [f"Workflow: {node.title}"]
    for stage in node.stages:
        lines.append(f"- {stage.label}")
    for checkpoint in node.checkpoints:
        lines.append(f"  * checkpoint: {checkpoint.label}")
    return "\n".join(lines)
```

### Tests To Consider

- no checkpoints
- multiple checkpoints per stage
- stage ordering
- deterministic formatting

## 11. Screen ASCII Projector

### Purpose

Project a screen artifact into an ASCII wireframe.

### Input

Comes in from:

- normalized screen DSL node

Suggested interface:

```python
project_screen_ascii(node: DSLNode) -> str
```

### Output

Produces:

- screen wireframe ASCII

To:

- agent response
- review loop
- design artifacts

### Work To Do

- render header
- render regions
- render semantic component placeholders
- render footer key strip
- preserve inspector placement and focused surface hints where relevant

### Pseudocode

```python
def project_screen_ascii(node):
    canvas = AsciiCanvas(width=78, height=24)
    draw_header(canvas, node.title)
    draw_regions(canvas, node.regions)
    draw_components(canvas, node.components)
    draw_footer_keys(canvas, node.footer_keys)
    return canvas.render()
```

### Tests To Consider

- standard three-region layout
- screen with inspector
- modal screen
- footer keys present
- long titles
- deterministic output

## 12. Revision Tool

### Purpose

Apply structured revision requests to canonical artifacts.

### Input

Comes in from:

- current spec
- revision request

Suggested interface:

```python
revise_spec(spec: object, request: RevisionRequest) -> object
```

### Output

Produces:

- revised canonical artifact

To:

- artifact store
- projectors
- agent

### Work To Do

- parse revision request
- apply only intended changes
- preserve stable IDs where possible
- return revised artifact for re-projection

### Pseudocode

```python
def revise_spec(spec, request):
    for op in request.operations:
        apply_operation(spec, op)
    validate_spec(spec)
    return spec
```

### Tests To Consider

- add region
- move component
- split stage
- preserve IDs
- invalid revision op

## 13. Designer Agent

### Purpose

Orchestrate the designer workflow between user, tools, artifacts, and review.

### Input

Comes in from:

- user prompt
- project inputs
- review feedback

Interface:

- conversational agent interface

### Output

Produces:

- recommendations
- tool invocations
- review packages
- revision prompts

To:

- user
- designer tools

### Work To Do

- decide next artifact to generate
- decide when to ask questions
- keep outputs Mono-aligned
- coordinate generation and revision

### Pseudocode

```python
def run_designer_turn(user_input, context):
    if needs_clarification(user_input, context):
        return ask_focused_question(user_input, context)
    plan = choose_next_design_step(user_input, context)
    return execute_plan(plan, context)
```

### Tests To Consider

- ambiguous workflow request
- clear single-screen request
- revision request
- project override conflict
- user-requested deviation from Mono

## 14. Designer Skill

### Purpose

Package the designer workflow for use by compatible agents.

### Input

Comes in from:

- agent invocation
- project context

### Output

Produces:

- a repeatable design-generation workflow

To:

- agent runtime

### Work To Do

- load proper Mono context
- sequence artifact generation
- keep design-generation separate from implementation/audit tracks

### Pseudocode

```python
def designer_skill(entry_request):
    context = load_designer_context(entry_request)
    return run_designer_flow(context)
```

### Tests To Consider

- correct context loading
- separate from implementation skill
- design-first output behavior

## 15. HITL Review Coordinator

### Purpose

Manage human review checkpoints across navigation, workflow, and screen
artifacts.

### Input

Comes in from:

- projected artifacts
- user review feedback

### Output

Produces:

- approval state updates
- revision requests
- checkpoint summaries

To:

- artifact store
- revision tool
- agent

### Work To Do

- track review stage
- capture approve/revise/reject decisions
- route revision intent back into the system

### Pseudocode

```python
def handle_review(artifact, user_feedback):
    if user_feedback.kind == "approve":
        artifact.status = "approved"
        return artifact
    if user_feedback.kind == "revise":
        return build_revision_request(user_feedback)
    return build_followup_question(user_feedback)
```

### Tests To Consider

- approve workflow
- revise screen
- reject navigation
- partial approval across multiple artifacts
