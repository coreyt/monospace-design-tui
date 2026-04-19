---
title: "Designer (alpha)"
weight: 60
---

# Monospace Designer (alpha)

The **Monospace Designer** is a suite of tools, schemas, and AI agent skills designed to help you move from vague product intent to structured terminal user interfaces *before* you write a single line of rendering code.

It bridges the gap between the static rules of the Monospace Design TUI Standard and the active implementation of a Textual or Bubbletea application.

## The Designer Philosophy

When building a TUI, it is tempting to start immediately with layout code or, worse, to draw web-based UI mockups that don't translate to the terminal grid.

The Designer forces a **TUI-First, Artifact-Driven** approach:

1. **Workflow over Screens:** You do not start by drawing boxes. You start by defining the task flow, entry conditions, and human-in-the-loop checkpoints.
2. **Structural YAML over Pixels:** The source of truth for a design is a canonical YAML specification (`dsl.yaml`), not a Figma file or a Python script.
3. **ASCII Projection:** The Designer tools automatically project your structural YAML into reviewable ASCII wireframes. You iterate on the YAML, and the wireframes update deterministically.
4. **Agent Collaboration:** The `mono-tui-design` skill allows AI agents to act as your Senior Product Architect, generating these YAML artifacts and discussing the ASCII projections with you.

## Sections

- **[Workflow Generation](../designer/workflow-generation)**: How to define applications as a series of task stages and transitions.
- **[Wireframes](../designer/wireframe-guide)**: How to read and write the canonical YAML screen specifications and their ASCII projections.
- **[Prototyping](../designer/prototyping-guide)**: How to move from ASCII wireframes to interactive, navigable terminal prototypes.