---
title: "Monospace Design TUI Standard"
subtitle: "v0.1 — Prescriptive rules for Monospace Design TUI applications"
description: "The authoritative design specification for Monospace TUI-compliant terminal applications"
---
**Package:** `mono-tui`

This document defines the authoritative design rules for Monospace TUI-compliant terminal applications. It distills the research in the [Foundational Research](/research/) into falsifiable, auditable requirements. A companion [Rendering Reference](/reference/) provides exact character codes, SGR sequences, and measurements. A [Textual Appendix](/textual/) maps these rules to the Textual framework.

## Conventions

The key words "MUST", "MUST NOT", "SHOULD", "SHOULD NOT", and "MAY" are to be interpreted as described in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

**Falsifiability:** Every rule in this document is written so that a reviewer can declare a specific implementation "compliant" or "in violation." If a rule cannot be tested, it is not a rule.

**Traceability:** Rules cite their research basis in parentheses — e.g., (CUA §1.3) refers to monospace-design-tui-research.md §1 "IBM Common User Access," (M3 §3.2) to §3 "Material Design 3," etc.
