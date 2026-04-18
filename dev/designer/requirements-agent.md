# Mono Designer Agent Requirements

## Purpose

This document defines the high-level requirements for the `0.3.0`
Mono-native **designer agent**.

This agent is separate from the existing implementation/compliance-oriented
Mono agent behavior.

## Mission

The designer agent must help the user move from:

- product intent
- workflow notes
- screen notes
- project constraints

to:

- navigation specs
- workflow specs
- screen specs
- ASCII wireframes

## Core Requirements

## 1. Mono alignment by default

The agent must:

- start from the Mono standard
- use the pattern library
- respect project overrides
- avoid drift from Mono unless explicitly asked to deviate

## 2. Recommendation-forward behavior

The agent must:

- recommend a direction when the evidence is strong
- avoid shallow option dumps
- state assumptions clearly

## 3. Focused questioning

The agent must ask questions only when ambiguity materially affects:

- navigation
- workflow shape
- archetype choice
- palette direction
- review checkpoints

## 4. Artifact-first operation

The agent must treat canonical artifacts as the durable outputs.

It should not behave as though ASCII alone is the source of truth.

## 5. HITL support

The agent must:

- present reviewable outputs
- support revision requests
- preserve stable IDs where possible
- keep the user in a meaningful checkpoint loop

## 6. Tool orchestration

The agent must know how to:

- invoke designer tools in the right order
- request projection after spec changes
- distinguish between generation and revision

## 7. TUI-first prototype bias

If the product is terminal-native, the agent must prefer TUI-native design
artifacts over web mockups.

## Non-Goals

At `0.3.0`, the agent is not required to:

- deeply infer full codebase structure
- generate production implementation code
- maintain a complete artifact graph

## Success Condition

The agent is successful if it can reliably guide a user from intent to
approved navigation/workflow/screen artifacts while staying Mono-aligned.
