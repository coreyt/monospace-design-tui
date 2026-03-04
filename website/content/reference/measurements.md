---
title: "§R4 Component Measurements"
description: "Exact character-cell dimensions for buttons, entry fields, toggles, radio groups, lists, tables, dialogs, menus"
weight: 4
---

All measurements are in character cells (cols × rows).

## §R4.1 Push Button

```
< Label >     (standard)
» Label «     (default button)
```

| Property | Value |
|----------|-------|
| Height | 1 row |
| Min width | Label length + 4 (2 padding chars each side) |
| Padding | 1 space each side inside delimiters |
| Delimiter (standard) | `<` and `>` |
| Delimiter (default) | `»` and `«` |
| Gap between buttons | 2 cols |

## §R4.2 Entry Field

```
Label: [input text here____]
```

| Property | Value |
|----------|-------|
| Height | 1 row |
| Min width | 10 cols (including brackets) |
| Max width | 60 cols |
| Fill character | `_` (underscore) or `·` (middle dot) |
| Bracket delimiters | `[` and `]` |
| Label gap | 1 space between label and field |

## §R4.3 Toggle / Checkbox

```
[X] Enabled option
[ ] Disabled option
```

| Property | Value |
|----------|-------|
| Height | 1 row per option |
| Indicator width | 3 cols (`[X]` or `[ ]`) |
| Gap to label | 1 space |
| Vertical gap between options | 0 rows (consecutive lines) |

## §R4.4 Radio Group

```
(*) Selected option
( ) Unselected option A
( ) Unselected option B
```

| Property | Value |
|----------|-------|
| Height | 1 row per option |
| Indicator width | 3 cols (`(*)` or `( )`) |
| Gap to label | 1 space |
| Vertical gap between options | 0 rows |
| Group label | 1 row above group, Title typography |

## §R4.5 List Box

```
┌── Select Model ──────────┐
│ ▸ claude-3-opus           │
│   claude-3-sonnet         │
│   gpt-4-turbo             │
│   gpt-4o                  │
│   gemini-1.5-pro      ↓   │
└──────────────────────────┘
```

| Property | Value |
|----------|-------|
| Min height | 3 rows (content) + 2 (border) = 5 rows |
| Max height | 15 rows (content) + 2 (border) = 17 rows |
| Min width | 20 cols (including border) |
| Highlight bar | Reverse video on focused row |
| Selection indicator | `▸` (1 col) before focused item |
| Scroll indicator | `↑` / `↓` in right border when content overflows |
| Border | Level 1 (single-line) |

## §R4.6 Data Table

```
│ Name         │ Status │ Latency │ Errors │
│──────────────│────────│─────────│────────│
│ claude-3     │ ◉ OK   │  120ms  │ 0      │
│ gpt-4        │ ⚠ SLOW │  890ms  │ 2      │
```

| Property | Value |
|----------|-------|
| Header row | 1 row, Title typography (bold) |
| Separator | 1 row of `─` characters below header |
| Data row height | 1 row |
| Cell horizontal padding | 1 space each side |
| Column separator | `│` (single vertical line) |
| Min column width | Longest header or data value + 2 (padding) |
| Sort indicator | `▴` (ascending) or `▾` (descending) after header text |

## §R4.7 Metric Card

```
▲ Requests: 1,234
```

| Property | Value |
|----------|-------|
| Height | 1 row (compact) or 2–3 rows (expanded) |
| Icon/symbol | 1–2 cols |
| Gap icon → label | 1 space |
| Gap label → value | 1 space (or `: `) |
| Separator between cards | `│` with 1 space padding each side |

## §R4.8 Dialog

```
╔══ Confirm Delete ══════════════════╗
║                                    ║
║  Are you sure you want to delete   ║
║  "report.pdf"?                     ║
║                                    ║
║         < Delete >  < Cancel >     ║
║                                    ║
╚════════════════════════════════════╝
```

| Property | Value |
|----------|-------|
| Min width | 30 cols |
| Max width | 72 cols |
| Min height | 5 rows (content) + 2 (border) = 7 rows |
| Padding | 2 cols horizontal, 1 row vertical (inside border) |
| Border | Level 3 (double-line) |
| Shadow | 2-col × 1-row offset |
| Title | Centered in top border |
| Button area | Bottom of content, right-aligned or centered |
| Button gap | 2 cols between buttons |

## §R4.9 Menu (Pull-Down)

```
┌──────────────────┐
│ New           ^N  │
│ Open...       ^O  │
│ Save          ^S  │
│───────────────────│
│ Close         ^W  │
└──────────────────┘
```

| Property | Value |
|----------|-------|
| Item height | 1 row |
| Max items | 10 |
| Min width | Longest item text + shortcut + 4 (padding) |
| Max width | 40 cols |
| Horizontal padding | 1 space each side |
| Separator | Full-width `─` line |
| Shortcut alignment | Right-aligned, 2 spaces before right border |
| Border | Level 2 (single-line) |
| Shadow | 2-col × 1-row offset |
| Cascade indicator | `▸` suffix (right-aligned) |
| Disabled items | Dim (SGR 2), no shortcut highlight |

## §R4.10 Spin Button

```
Model Count: < 5 >
```

| Property | Value |
|----------|-------|
| Height | 1 row |
| Decrease indicator | `<` |
| Increase indicator | `>` |
| Value padding | 1 space each side of value |
| Max recommended values | 20 |

## §R4.11 Footer Key Strip

```
F1 Help  F5 Refresh  / Filter  q Quit
```

| Property | Value |
|----------|-------|
| Height | 1–2 rows |
| Key label | Key name in bold or contrasting color |
| Action label | Body typography |
| Gap key → action | 1 space |
| Gap between pairs | 2+ spaces |
| Position | Absolute bottom of terminal |
