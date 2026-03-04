---
title: "§4 Component Rules"
description: "Widget selection table, default button, tab order, entry field conventions"
weight: 4
---

## §4.1 Widget Selection

Applications MUST select widgets according to this decision table:

| Data Type | Count / Range | Required Widget | Primary Key |
|-----------|--------------|----------------|-------------|
| Boolean | 2 states | Toggle/Switch `[X]` / `[ ]` | Space |
| Exclusive choice | 2–5 options | Radio group `(*)` / `( )` | Arrow keys within group |
| Exclusive choice | 6–25 options | List box with highlight bar | Arrow keys + Enter |
| Free text | N/A | Entry field (underscore fill) | Arrow keys within, Tab to leave |
| Numeric | N/A | Entry field with validation | Arrow keys within, Tab to leave |
| Action | N/A | Push button `< OK >` | Enter or Space |
| Spin value | ≤20 values | Spin button with ± controls | Arrow Up/Down |

Applications SHOULD NOT deviate from this table. If an application uses a widget not listed here, it MUST document the rationale and ensure the widget follows the state model ([§8](/standard/state/)) and keyboard rules ([§2](/standard/keyboard/)). (CUA §1 component specifications, tui-architect widget selection heuristics)

## §4.2 Default Button

Every dialog MUST have exactly one default button, visually distinguished from other buttons (e.g., bold label, bracket style `» OK «`). Pressing Enter when no other control captures it MUST activate the default button. (CUA §1)

## §4.3 Tab Order

Tab order MUST follow field layout: top-to-bottom, then left-to-right within each row. Tab order MUST be predictable — a user who presses Tab repeatedly MUST visit every interactive element in visual order and return to the first element. (CUA §1, [§2.5](/standard/keyboard/#25-navigation-order))

## §4.4 Entry Field Conventions

- Empty entry fields MUST display fill characters (underscores `_` or dots `·`) to indicate their width.
- Entry fields MUST show a visible cursor at the current edit position.
- Entry fields with constrained input (numeric, date, etc.) MUST validate on field exit (Tab or Enter) and display an error state ([§8](/standard/state/)) with explanatory text if validation fails.

(CUA §1 entry field specification)
