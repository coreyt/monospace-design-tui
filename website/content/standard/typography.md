---
title: "§7 Typography"
description: "Four text treatments, focus and selection indication, error text requirements"
weight: 7
---

## §7.1 Text Treatments

Applications MUST use exactly 4 typographic treatments:

| Role | SGR Attributes | Use |
|------|---------------|-----|
| Display | Bold (SGR 1) + optional UPPERCASE | Screen titles, hero metrics |
| Title | Bold (SGR 1) | Section headers, panel titles, column headers |
| Body | Normal (no attributes) | Content text, field values, menu items |
| Label | Dim (SGR 2) | Secondary info, placeholders, help text, timestamps |

Applications MUST NOT combine more than 2 SGR attributes on a single text span (e.g., Bold + Underline is acceptable; Bold + Dim + Italic is not). (mono-tui.md cross-cutting synthesis — 4 text treatments)

## §7.2 Focus and Selection Indication

- Focused text MUST use reverse video (SGR 7).
- If reverse video is insufficient for the context (e.g., list items that are already highlighted), bracket markers `[▸ item ◂]` MAY be used as an alternative.

(mono-tui.md unified state model)

## §7.3 Error Text

Error text MUST use red foreground (SGR 31 or bright red SGR 91). For critical errors, a red background (SGR 41) MAY be used. Error text MUST be accompanied by an explanatory message — a red-colored field with no text explanation violates this rule. (CUA §1, [§5.3](/standard/color/#53-color-independence) color independence)
