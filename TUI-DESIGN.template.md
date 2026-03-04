# TUI-DESIGN.md — Project Override Template

**Version 1.0** — Template for project-specific overrides to the
[Monospace Design TUI Standard](https://coreyt.github.io/monospace-design-tui/standard/) and
[Rendering Reference](https://coreyt.github.io/monospace-design-tui/reference/).

Copy this file to your project root as `TUI-DESIGN.md` and fill in each section.

---

## Meta

| Key              | Value                                         |
|------------------|-----------------------------------------------|
| Project          | _project name_                                |
| Standard URL     | https://coreyt.github.io/monospace-design-tui/ |
| Standard version | 1.0                                           |
| Palette          | _Default / Monochrome / Commander / OS/2 / Turbo Pascal / Amber Phosphor / Green Phosphor / Airlock_ |
| Archetypes       | _§11.1 Dashboard, §11.2 Admin, etc._         |
| Framework        | _Textual / curses / raw ANSI / etc._          |
| Minimum terminal | _80×24 / 120×40 / etc._                       |
| Created          | _YYYY-MM-DD_                                  |
| Last reviewed    | _YYYY-MM-DD_                                  |

---

## Overrides

<!--
  GRAMMAR — each override is an H3 heading with this exact format:

    ### [ACTION] §X.Y Summary phrase

  Rule IDs come from two sources:
    §X.Y   — Design Standard rules  (e.g., §2.2, §5.1, §11.3)
    §RX.Y  — Rendering Reference rules (e.g., §R1.4, §R3.2, §R5.3)

  ACTION is one of:
    WAIVE    — Rule acknowledged, intentionally not followed.
    OVERRIDE — Rule replaced with a project-specific version.
    TIGHTEN  — SHOULD/MAY elevated to MUST for this project.

  The heading is the machine-parseable key. Everything below it is
  structured metadata for the auditor, then optional prose for humans.

  REGEX to find all overrides:
    grep -E '^### \[(WAIVE|OVERRIDE|TIGHTEN)\] §R?' TUI-DESIGN.md

  REGEX to find overrides for a specific rule:
    grep -E '^### \[.*\] §2\.2' TUI-DESIGN.md
    grep -E '^### \[.*\] §R3\.2' TUI-DESIGN.md
-->

<!-- EXAMPLE — delete or replace with real overrides:

### [WAIVE] §2.2 Footer key strip in editor mode

- **Rule:** §2.2
- **Original:** Footer key strip MUST occupy the bottom 1–2 rows and MUST be visible at all times.
- **Action:** WAIVE
- **Scope:** Editor archetype screens only
- **Rationale:** Editor needs maximum vertical space; keys shown on demand via `?`.
- **Decided:** 2026-03-01

### [OVERRIDE] §5.1 Semantic color count

- **Rule:** §5.1
- **Original:** Applications MUST define exactly 5 semantic color roles: primary, secondary, tertiary, error, neutral.
- **Replacement:** Applications MUST define 6 semantic color roles: primary, secondary, tertiary, error, neutral, accent.
- **Action:** OVERRIDE
- **Scope:** All screens
- **Rationale:** Brand guidelines require an accent color for call-to-action elements.
- **Decided:** 2026-03-01

### [TIGHTEN] §9.3 Minimum contrast

- **Rule:** §9.3
- **Original:** Applications SHOULD maintain 4.5:1 contrast for body text.
- **Replacement:** Applications MUST maintain 4.5:1 contrast for body text.
- **Action:** TIGHTEN
- **Scope:** All text rendering
- **Rationale:** WCAG AA compliance is a hard requirement for this deployment.
- **Decided:** 2026-03-02

### [OVERRIDE] §R3.2 Dark theme status colors

- **Rule:** §R3.2
- **Original:** Healthy: index 34 (green). Warning: index 214 (orange). Error: index 196 (red).
- **Replacement:** Healthy: index 42 (bright green). Warning: index 220 (bright yellow). Error: index 160 (dark red).
- **Action:** OVERRIDE
- **Scope:** All status indicators
- **Rationale:** Default palette has insufficient contrast on our target terminal (Alacritty dark theme).
- **Decided:** 2026-03-02

-->

_No overrides yet._

---

## Project Conventions

<!--
  Project-specific rules that go BEYOND the standard. These are
  auditable — the auditor checks them alongside standard rules.

  GRAMMAR — each convention is an H3 heading:

    ### [P#] Convention name

  Where # is a sequential integer. The auditor treats [P#] rules
  the same as §X.Y rules — checking compliance based on the Level.

  REGEX to find all project conventions:
    grep -E '^### \[P[0-9]+\]' TUI-DESIGN.md
-->

<!-- EXAMPLE — delete or replace with real conventions:

### [P1] Screen class naming

All screen classes MUST be suffixed with `Screen` (e.g., `DashboardScreen`, `SetupScreen`).

- **Level:** MUST
- **Applies to:** All screen classes
- **Decided:** 2026-03-01

### [P2] Health status ordering

Status indicators MUST use top-to-bottom severity ordering: healthy (top) → warning → error (bottom).

- **Level:** MUST
- **Applies to:** All status lists and dashboards
- **Decided:** 2026-03-02

### [P3] Modal confirmation for destructive actions

Any action that deletes or resets data SHOULD show a confirmation modal before execution.

- **Level:** SHOULD
- **Applies to:** Delete, reset, clear operations
- **Decided:** 2026-03-02

-->

_No project conventions yet._

---

## Decision Log

<!--
  Chronological record of design decisions. Not machine-audited,
  but cross-references overrides and conventions by ID.

  This section answers "why did we make these choices?" for future
  readers. Each entry is an H3 with a date and topic.
-->

<!-- EXAMPLE — delete or replace with real decisions:

### 2026-03-01 — Initial TUI architecture

**Participants:** @coreyt, @designer

**Decisions:**
- Selected Dashboard (§11.1) + Admin (§11.2) archetypes
- Waived footer in editor mode → [WAIVE] §2.2
- Added accent color → [OVERRIDE] §5.1
- Established screen naming convention → [P1]

**Context:**
The application manages long-running processes. Operators spend 80% of time
on the dashboard, 20% in config. The editor mode is for inline YAML editing
and needs every row.

### 2026-03-02 — Accessibility review

**Participants:** @coreyt

**Decisions:**
- Tightened contrast requirement → [TIGHTEN] §9.3
- Added severity ordering convention → [P2]
- Added destructive action confirmation → [P3]

**Context:**
Deployment target includes terminals with poor contrast. WCAG AA is a
contractual requirement.

-->

_No decisions logged yet._
