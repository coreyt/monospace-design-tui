# Mono Designer Tool Requirements

## Purpose

This document defines the high-level requirements for the `0.3.0`
Mono-authored **designer tools**.

These tools are the artifact-producing backend for the designer system.

## Mission

The tools must create and revise canonical artifacts for:

- navigation
- workflows
- screens

and support projection into ASCII.

## Tool Set

Expected `0.3.0` tools:

- navigation generator
- workflow generator
- screen generator
- revision tool
- ASCII projectors
- YAML validation/read/write helpers

## Core Requirements

## 1. Predictable contracts

Each tool must have:

- explicit inputs
- explicit outputs
- stable behavior

## 2. YAML-first outputs

Generation tools must write canonical YAML artifacts.

They must not treat ASCII as the primary output format.

## 3. Projection separation

Projection tools must:

- consume canonical artifacts
- emit ASCII outputs

Generation and projection should remain separate concerns.

## 4. Stable IDs

Tools must preserve stable IDs across revisions where possible.

## 5. Validation

Tools must validate inputs before generating or revising outputs.

## 6. Revision support

The revision tool must accept structured revision requests and update canonical
artifacts accordingly.

## 7. Mono alignment

All tools must encode Mono assumptions by default:

- archetypes
- patterns
- keyboard conventions
- footer discoverability
- visible focus

## 8. Python-first implementation

For `0.3.0`, tools should be implemented in Python.

Why:

- fast iteration
- simple schema handling
- strong MCP compatibility
- easy integration with agent orchestration

## Suggested Responsibilities by Tool

### Navigation Generator

- create navigation spec YAML

### Workflow Generator

- create workflow spec YAML

### Screen Generator

- create screen spec YAML

### Revision Tool

- revise any canonical artifact YAML

### Projectors

- create ASCII outputs from canonical artifacts

### YAML Helpers

- validate
- normalize
- load
- save

## Success Condition

The tools are successful if they make the design-generation flow reliable,
repeatable, and artifact-driven for `0.3.0`.
