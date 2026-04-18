# Mono Designer Skill Requirements

## Purpose

This document defines the high-level requirements for the `0.3.0`
Mono-native **designer skill** track.

This skill track is distinct from the existing Mono implementation/audit
skills.

## Mission

The designer skill should package the workflow for:

- navigation design
- workflow design
- screen generation
- ASCII wireframe generation
- design artifact revision

## Core Requirements

## 1. Separate concern from implementation skills

The designer skill must be clearly separate from:

- implementation guidance
- compliance audit

It is a design-generation skill, not a coding skill.

## 2. Load the correct context

The skill must load:

- `TUI-DESIGN.md`
- relevant Mono standard sections
- pattern library
- rendering guidance only as needed
- existing design artifacts if present

## 3. Operate on canonical artifacts

The skill must:

- generate YAML artifacts
- revise YAML artifacts
- request ASCII projection from those artifacts

## 4. Preserve Mono-native structure

The skill must ensure generated outputs include:

- archetype mapping
- pattern selection
- keyboard/focus thinking
- region/component structure
- workflow and screen IDs

## 5. Support HITL revision

The skill must help with:

- screen revisions
- workflow revisions
- navigation revisions

without collapsing into freeform redesign every time.

## 6. Keep outputs lightweight

The skill should favor:

- ASCII wireframes
- YAML specs
- concise review artifacts

over verbose prose dumps.

## Success Condition

The skill is successful if it helps an agent repeatedly generate and revise
Mono-aligned design artifacts for real TUI projects.
