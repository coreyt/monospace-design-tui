---
title: "Monospace Design TUI Standard"
subtitle: "v0.2.5 — Prescriptive rules for Monospace Design TUI applications"
description: "The authoritative design specification for Monospace TUI-compliant terminal applications"
---
**Package:** `mono-tui`

This document defines the authoritative design rules for Monospace TUI-compliant terminal applications. It distills the research in the [Foundational Research](/research/) into falsifiable, auditable requirements. A companion [Rendering Reference](/reference/) provides exact character codes, SGR sequences, and measurements. A [Textual Appendix](/textual/) maps these rules to the Textual framework.

Monospace TUI explicitly supports **aesthetic-first terminal applications** — character user interfaces (CUIs) that treat the terminal as a high-fidelity visual medium rather than as a purely utilitarian text transport.[^cui-aesthetic]

For reusable interaction strategies that cut across multiple archetypes, see the companion [Pattern Library](/patterns/).

## Conventions

The key words "MUST", "MUST NOT", "SHOULD", "SHOULD NOT", and "MAY" are to be interpreted as described in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

**Falsifiability:** Every rule in this document is written so that a reviewer can declare a specific implementation "compliant" or "in violation." If a rule cannot be tested, it is not a rule.

**Traceability:** Rules cite their research basis in parentheses — e.g., (CUA §1.3) refers to monospace-design-tui-research.md §1 "IBM Common User Access," (M3 §3.2) to §3 "Material Design 3," etc.

[^cui-aesthetic]: Historical terminal systems and modern TUIs both show that strong visual identity and atmospheric rendering can improve orientation and perceived quality when semantic state remains legible. See the color-systems and historical-application synthesis in the research.
