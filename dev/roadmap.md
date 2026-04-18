# Monospace Design TUI Roadmap

## Unplanned

These are important but challenging efforts that are not yet committed to a
specific release. They should remain visible because they materially affect how
valuable Mono can become as a design and prototyping system.

### Codebase understanding for design generation

To be genuinely valuable, Mono-based tools should be able to inspect an
existing codebase and understand:

- current routes / screens / flows
- current TUI framework structure
- current domain objects and actions
- existing keyboard model
- what is already implemented vs proposed

This is a hard problem because it requires more than file search. It likely
needs framework-aware analysis, project-structure inference, and an artifact
model that can distinguish:

- current state
- inferred state
- proposed target state

### Current-state inference and migration support

Mono will be much more useful if it can work on existing applications, not
just greenfield ones.

Challenging capabilities:

- infer the current application map from an existing codebase
- infer current workflows and screen relationships
- detect where the current implementation diverges from Mono
- propose an improved target design without losing what already exists
- support “adopt Mono” and “redesign with Mono” as separate modes

### Artifact graph and traceability

Mono will become significantly more valuable if it can maintain relationships
between:

- app navigation model
- workflow specs
- screen specs
- ASCII wireframes
- implementation notes
- codebase evidence

This implies an artifact graph with traceability such as:

- why a workflow exists
- why a screen exists
- which workflow step owns a screen
- which code files implement or partially implement a screen
- which Mono patterns and rules justify the current design

Mono will also become more trustworthy if every recommendation can explain
why it was made.

Future traceability should include:

- relevant Mono archetype
- relevant pattern(s)
- relevant codebase evidence
- relevant workflow assumptions

### Round-trip revision and diff

Generating wireframes once is useful. Revising them safely is much more
valuable.

Challenging capabilities:

- edit one screen without regenerating the full system
- modify a workflow and identify impacted screens
- diff prior and proposed ASCII wireframes
- diff workflow specs and screen specs
- support artifact-level approve / reject / revise loops

### Consistency checking across artifacts

If Mono starts generating:

- workflow specs
- screen specs
- wireframes
- prototypes

then it also needs to detect inconsistency across those artifacts.

Examples:

- workflow changed but screen inventory did not
- screen wireframe changed but keyboard model did not
- implementation drifted from the approved screen spec
- prototype behavior diverged from the workflow spec

### Implementation handoff quality

Wireframes and workflows are much more valuable if they can hand off cleanly to
implementation agents or human engineers.

This suggests future structured handoff artifacts including:

- keyboard bindings
- focus model
- region layout
- component selection
- transitions
- state variants
- implementation notes

### Prototype-state management

If Mono supports interactive TUI prototyping, it will eventually need a better
model for prototype state.

Challenging concerns:

- how much local fake state is enough
- how to simulate workflows without overbuilding
- how to distinguish prototype-only state from implementation-ready state
- how to represent pending / approved / draft / rejected design states

### HITL orchestration as a design primitive

Mono already leans toward HITL collaboration, but a stronger future capability
would be explicit design-review orchestration.

Examples:

- named approval checkpoints in workflows
- targeted design questions generated automatically
- review packages for navigation, workflow, or screen changes
- human decisions recorded as design constraints or artifact metadata

### Cross-framework structural inference

Mono is currently strongest in Textual-oriented implementation guidance.
Future tooling becomes harder and more valuable if it can reason structurally
across:

- Textual
- Ratatui
- Bubble Tea
- Ink
- curses / raw ANSI

without collapsing to the lowest common denominator.

### TUI-first prototype conversion

A recurring challenge is converting an existing web prototype or product brief
into a TUI-first prototype rather than simply reproducing web layout in a
terminal.

This requires Mono to reason about:

- what interaction structure is essential
- what should be removed
- what should become keyboard-first
- what should become multi-pane
- what should become workflow stages or drill-down

This is especially relevant for projects like Margie, where prototype intent
exists today, but the target form should be TUI rather than web.
