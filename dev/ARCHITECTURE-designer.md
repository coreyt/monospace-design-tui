# Monospace Design TUI Designer Architecture

Date: 2026-04-18

## Purpose

This document defines the `0.3.0` architecture for the new Mono
**designer** capability.

Here, **designer** is a generic system term covering all components needed to
support:

- navigation design
- workflow design
- screen design
- ASCII wireframe generation
- workflow and screen spec generation
- HITL revision
- TUI-first prototyping direction

The term includes:

- tools
- projectors
- skills
- agent behavior
- artifact formats

This architecture is intentionally scoped to `0.3.0`. It does **not** assume
the future DSL or full projection/runtime platform from `0.4-0.8`.

The concrete `0.3.0` design package for this architecture lives under:

- `dev/designer/`

## Scope Boundary

This architecture is for:

- Python-first tooling
- YAML canonical artifacts
- ASCII as the primary human-facing output
- minimal semantic structure only where needed
- design-generation agents and skills

This architecture is **not** for:

- a full Mono DSL
- deep codebase inference
- multi-framework code generation
- artifact graph infrastructure
- full consistency-engine behavior

Those belong to later releases.

## Design Principles

- **Canonical spec first**: navigation, workflow, and screen specs are the
  source of truth.
- **ASCII first for review**: ASCII is the primary review artifact.
- **Projection, not duplication**: wireframes are derived from specs.
- **Agent as orchestrator**: the agent coordinates the flow, but the artifacts
  are the durable outputs.
- **HITL by design**: the system is built around human review checkpoints.
- **Mono alignment by default**: all components should start from the standard,
  pattern library, and project overrides unless the user explicitly asks
  otherwise.

## System Overview

At `0.3.0`, the designer system should be understood as six layers:

1. **Inputs**
2. **Canonical artifacts**
3. **Designer tools**
4. **Projection layer**
5. **Agent/skill layer**
6. **Review loop**

High-level flow:

1. user provides product intent, notes, or project context
2. agent invokes Mono design-generation logic
3. designer tools generate canonical YAML artifacts
4. projectors convert those artifacts into ASCII outputs
5. user reviews and revises through HITL checkpoints
6. approved artifacts become the basis for prototyping and implementation

## Components

## 1. Designer Input Set

### Definition

The set of materials the designer system can consume in order to produce a
navigation model, workflow specs, screen specs, and wireframes.

### Typical inputs

- product brief
- user task description
- workflow notes
- wireframe notes
- `TUI-DESIGN.md`
- existing Mono decisions
- limited project context from the codebase

### Responsibilities

- give the system enough context to propose a design direction
- establish constraints and intent
- define what the user is trying to build

### Non-responsibilities

- not a full project model
- not a full codebase inference system

## 2. Project Override Layer

### Definition

The project-specific constraints and preferences that modify the default Mono
guidance.

### Primary source

- `TUI-DESIGN.md`

### Responsibilities

- set palette
- set archetypes
- define overrides
- define project conventions
- constrain the generated design outputs

### Interactions

- read by the agent
- read by the designer tools
- applied before canonical artifacts are finalized

## 3. Canonical Artifact Store

### Definition

The set of YAML artifacts that serve as the designer system’s source of truth
at `0.3.0`.

### Artifact types

#### Navigation Spec

Represents:

- top-level workspaces or sections
- root navigation structure
- major routing rules
- cross-workspace paths

#### Workflow Spec

Represents:

- workflow purpose
- stages or steps
- transitions
- HITL checkpoints
- assumptions
- linked screens

#### Screen Spec

Represents:

- screen ID
- purpose
- regions
- components
- primary actions
- keyboard/focus model
- transitions
- linked workflow
- linked Mono patterns

### Responsibilities

- provide durable, structured outputs
- act as the source for ASCII projection
- support revision without losing structure

### Non-responsibilities

- not yet a full artifact graph
- not yet a full semantic DSL

## 4. Designer Tool Set

### Definition

The Mono-authored tools that create or revise canonical artifacts.

These are not generic coding tools. They are design-generation tools.

### Core tools for `0.3.0`

#### Navigation Generator

Produces a navigation spec from intent and project constraints.

#### Workflow Generator

Produces workflow specs from product intent, tasks, and chosen navigation
structure.

#### Screen Generator

Produces screen specs from workflow specs, archetypes, and selected patterns.

#### Revision Tool

Updates navigation/workflow/screen specs based on user feedback while trying to
preserve stable IDs and structure.

### Responsibilities

- create structured YAML outputs
- revise structured YAML outputs
- stay Mono-aligned
- expose predictable contracts for the agent layer

### Non-responsibilities

- not responsible for final runtime rendering
- not responsible for implementation code generation

## 5. Projection Layer

### Definition

The layer that converts canonical YAML artifacts into human-reviewable outputs.

At `0.3.0`, the primary projection target is ASCII.

### Core projectors

#### Navigation Projector

Projects the navigation spec into a compact ASCII navigation overview.

#### Workflow Projector

Projects a workflow spec into an ASCII workflow outline.

#### Screen Projector

Projects a screen spec into an ASCII wireframe.

### Responsibilities

- render artifacts in a clear, reviewable form
- preserve important structural information
- remain deterministic and consistent

### Non-responsibilities

- not the source of truth
- not yet a full interactive runtime generator

## 6. Minimal Semantic Layer / 0.3.0 DSL Normalization Layer

### Definition

The minimal semantic vocabulary embedded in canonical artifacts so that
projection is meaningful and future richer outputs remain possible.

At `0.3.0`, this is the practical Mono DSL layer. It is intentionally small
and primarily exists to normalize YAML artifacts into a consistent semantic
shape before projection.

### Semantic concepts in scope

- regions
- components
- actions
- focus
- state

### Responsibilities

- preserve enough structure to make the artifacts useful
- support clean ASCII projection
- prepare the ground for future DSL work

### Non-responsibilities

- not a full user-authored language
- not a large syntax surface
- not the future `0.5+` mature Mono DSL

## 7. Designer Agent

### Definition

The Mono-native design-generation agent behavior that orchestrates the flow
between user intent, tools, artifacts, and review.

### Responsibilities

- interpret the user’s design request
- load Mono guidance and project overrides
- choose which designer tools to invoke
- present recommendations clearly
- ask focused clarification questions when required
- keep the user in a meaningful HITL loop

### Expected behavior

- recommendation-forward
- Mono-aligned by default
- explicit about assumptions
- careful about drift from Mono
- willing to deviate only when the user or project explicitly requires it

### Non-responsibilities

- not the artifact store
- not the projection engine
- not the final authority on durable design outputs

## 8. Designer Skill Set

### Definition

The separate design-generation skill/agent track introduced for `0.3.0`.

This is distinct from the existing implementation/compliance-oriented Mono
skills.

### Responsibilities

- workflow design
- screen generation
- wireframe generation
- spec generation
- revision support

### Key requirement

This skill set must succeed at its own design work while remaining grounded in:

- the Mono standard
- the pattern library
- the rendering reference where relevant
- project overrides

## 9. HITL Review Loop

### Definition

The explicit human review cycle through which the user accepts, rejects, or
revises generated artifacts.

### Expected review checkpoints

- approve navigation model
- approve workflow boundaries
- approve screen inventory
- approve workflow wireframes
- approve screen wireframes
- approve specs for downstream use

### Responsibilities

- make review clear and manageable
- avoid silent drift
- keep the artifacts aligned with human intent

## Component Interactions

## A. Input -> Override Layer

The user request and project context are read together with `TUI-DESIGN.md`.

Why:

- the request provides intent
- the override layer provides constraints

## B. Input + Override Layer -> Designer Agent

The agent forms an initial design interpretation based on:

- user intent
- project constraints
- Mono rules and patterns

The agent decides:

- whether to ask a clarifying question
- which design artifact to generate next

## C. Designer Agent -> Designer Tool Set

The agent invokes the appropriate tool:

- navigation generator
- workflow generator
- screen generator
- revision tool

The tool returns canonical YAML artifacts.

## D. Designer Tool Set -> Canonical Artifact Store

Generated artifacts are stored as:

- navigation spec
- workflow spec(s)
- screen spec(s)

These are the durable design outputs for `0.3.0`.

## E. Canonical Artifact Store -> Minimal Semantic Layer / 0.3.0 DSL

Canonical YAML artifacts are first normalized into the minimal semantic model.

Why:

- to unify structurally similar shapes
- to make projection deterministic
- to keep ASCII generation independent from raw YAML shape quirks

## F. Minimal Semantic Layer / 0.3.0 DSL -> Projection Layer

Projectors consume the normalized semantic form and produce:

- ASCII navigation output
- ASCII workflow output
- ASCII screen wireframes

This keeps projection logic semantic rather than ad hoc.

## G. Projection Layer -> HITL Review Loop

The projected outputs are what the human reviews.

The user can then:

- approve
- reject
- revise
- request alternatives

## H. HITL Review Loop -> Designer Agent

User feedback returns to the agent as structured revision intent.

The agent then decides whether to:

- ask a focused clarification question
- revise a workflow
- revise a screen
- regenerate a projection

## I. HITL Review Loop -> Revision Tool

When the user requests changes, the revision tool updates the canonical
artifacts rather than editing ASCII directly.

This is critical:

- ASCII is a projection
- YAML is the source of truth

## J. Canonical Artifact Store -> Downstream Consumers

Approved artifacts can later be used by:

- prototype guidance
- implementation planning
- future DSL migration
- future runtime projections

At `0.3.0`, downstream consumers are mostly conceptual and document-oriented,
not yet full code generators.

## Interaction Summary

In compact form:

`User Intent -> Agent -> Designer Tools -> YAML Artifacts -> 0.3.0 DSL Normalization -> ASCII Projectors -> HITL Review -> Revision -> Approved Artifacts`

## Required Contracts for 0.3.0

Each component should expose a clear contract.

### Navigation Generator Contract

Input:

- product intent
- project overrides

Output:

- navigation spec YAML

### Workflow Generator Contract

Input:

- workflow intent
- navigation context
- project overrides

Output:

- workflow spec YAML

### Screen Generator Contract

Input:

- workflow spec
- archetype choice
- pattern selection
- project overrides

Output:

- screen spec YAML

### Projection Contract

Input:

- canonical YAML artifact

Output:

- ASCII projection

### Revision Contract

Input:

- canonical YAML artifact
- user revision request

Output:

- revised canonical YAML artifact

## What Success Looks Like at 0.3.0

The designer architecture is successful if:

- agents can use Mono as the front door to design work
- Mono tools produce canonical YAML artifacts
- ASCII wireframes are always derived from canonical specs
- users can review and revise workflows and screens with HITL
- the design-generation skill track is distinct from implementation/audit work
- the architecture is simple enough to support future DSL and runtime work

## Forward Compatibility

This `0.3.0` architecture is intentionally shaped so that later releases can
extend it cleanly.

Future evolution should look like:

- canonical YAML artifacts become normalized semantic structures
- semantic structures mature into the Mono DSL
- projection layer expands beyond ASCII into runtime/prototype targets
- MCP exposes the tool contracts directly across agent harnesses

At `0.3.0`, however, the architecture should remain disciplined and modest:

- YAML as source of truth
- ASCII as primary projection
- Python as implementation
- HITL as review model
