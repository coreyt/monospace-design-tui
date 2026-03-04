---
title: "§5 Color System"
description: "Semantic color roles, status colors, color independence, capability detection"
weight: 5
---

## §5.1 Semantic Color Roles

Applications MUST define colors for these 5 semantic roles:

| Role | Purpose | Example Use |
|------|---------|-------------|
| Primary | Brand identity, key actions | Action bar, active tab indicator |
| Secondary | Supporting UI elements | Panel borders, secondary buttons |
| Tertiary | Accent, highlight | Links, selected items |
| Error | Error states, destructive actions | Error messages, delete buttons |
| Neutral | Backgrounds, body text, borders | Content area, panel backgrounds |

Colors MUST be assigned by semantic role, not by literal color name. Applications MUST NOT hardcode ANSI color indices directly in layout code — use a theme or token layer. (M3 §3 color system)

## §5.2 Status Colors

Applications MUST use these 4 semantic status colors consistently:

| Status | Color | Use |
|--------|-------|-----|
| Healthy / Success | Green | Passing checks, active services, confirmations |
| Error / Critical | Red | Failures, blocked states, destructive confirmations |
| Warning / Caution | Yellow | Degraded performance, approaching limits |
| Inactive / Disabled | Dim gray | Placeholder text, disabled controls, secondary info |

(tui-architect common violations — status color palette)

## §5.3 Color Independence

Color MUST NOT be the sole indicator of any state or meaning. Every use of color MUST be paired with at least one of:

- Text label (e.g., "Error:", "OK")
- Typographic attribute (bold, dim, underline)
- Symbol or marker (e.g., `✓`, `✗`, `⚠`, `◉`)

This rule is non-negotiable for accessibility. (Apple HIG §4 color independence, mono-tui.md cross-cutting synthesis)

## §5.4 Dialog Severity Colors

Dialogs MUST use background color to indicate severity:

| Severity | Background | Required Non-Color Indicator |
|----------|-----------|------------------------------|
| Notification / Info | Neutral background | Title or icon (e.g., `ℹ`) |
| Warning | Yellow-tinted background | `⚠` symbol and/or "Warning:" label |
| Critical / Error | Red-tinted background | `✗` symbol and/or "Error:" label |

Per §5.3, severity background color MUST be paired with a text label or symbol. A dialog with a red background and no textual severity indicator is a violation. (CUA §1 state indicators — pop-up severity colors)

## §5.5 Active/Inactive Window Distinction

Active windows MUST render with brighter color attributes than inactive windows. The distinction MUST be visible without relying on color alone — active windows MUST also use double-line borders ([§6](/standard/borders/)) and/or bold title text. (CUA §1, OS/2 §2)

## §5.6 Color Capability Detection

Applications MUST detect the terminal's color capability and degrade gracefully:

1. **Truecolor** (24-bit) — `COLORTERM=truecolor` or `COLORTERM=24bit`
2. **256-color** — `TERM` contains `256color`
3. **16-color** — Standard ANSI colors
4. **Monochrome** — Bold, dim, underline, reverse video only

Applications MUST NOT emit color codes unsupported by the detected capability level. Applications MUST remain fully functional in monochrome mode. (Terminal §6 color detection)
