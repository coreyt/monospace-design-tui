# Monospace Design TUI Standard

```
┏┳┓┏━┓┏┓┓┏━┓┏━┓┏━┓┏━┓┏━┓┏━┓  ┏┳┓┳ ┳┳
┃┃┃┃ ┃┃┃┃┃ ┃┗━┓┣━┛┣━┫┃  ┣┫    ┃ ┃ ┃┃
┻ ┻┗━┛┛┗┛┗━┛┗━┛┻  ┻ ┻┗━┛┗━┛   ┻ ┗━┛┻
```

**Version 1.0** — Prescriptive rules for Monospace Design TUI applications.

**Package:** `mono-tui`

This document defines the authoritative design rules for Monospace TUI-compliant terminal applications. It distills the research in [mono-tui.md](mono-tui.md) into falsifiable, auditable requirements. A companion [Rendering Reference](mono-tui-rendering-reference.md) provides exact character codes, SGR sequences, and measurements. A [Textual Appendix](mono-tui-textual-appendix.md) maps these rules to the Textual framework.

## Conventions

The key words "MUST", "MUST NOT", "SHOULD", "SHOULD NOT", and "MAY" are to be interpreted as described in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

**Falsifiability:** Every rule in this document is written so that a reviewer can declare a specific implementation "compliant" or "in violation." If a rule cannot be tested, it is not a rule.

**Traceability:** Rules cite their research basis in parentheses — e.g., (CUA §1.3) refers to mono-tui.md §1 "IBM Common User Access," (M3 §3.2) to §3 "Material Design 3," etc.

---

## §1 Grid & Layout

### §1.1 Atomic Unit

The atomic unit of all Monospace TUI measurement is **1 character cell** (1 column × 1 row). All spacing, sizing, and positioning values in this standard are expressed in character cells unless stated otherwise. (CUA §2, M3 §3 cross-cutting synthesis)

### §1.2 Spacing Scale

Applications MUST use the following spacing scale for all padding, margins, and gaps:

```
0  1  2  3  4  6  8
```

Values are in character cells. Intermediate values (5, 7) MUST NOT be used. (M3 §3 spacing tokens → character-cell mapping)

### §1.3 Three-Region Layout

Every screen MUST divide its content area into up to three regions:

| Region | Position | Width | Behavior |
|--------|----------|-------|----------|
| A — Navigation | LEFT | 8–20 cols | Collapsible |
| B — Content | CENTER | Flex (fills remaining) | Always visible |
| C — Context | RIGHT or BOTTOM | Fixed or collapsible | Optional |

- Region B MUST always be present and MUST fill all space not occupied by Regions A and C.
- Region A MAY be omitted if the archetype has no sidebar navigation.
- Region C MAY be omitted if the archetype has no contextual detail pane.

(CUA §1 panel layout, M3 §3 canonical layouts, tui-architect Cockpit Design Standard)

### §1.4 Footer Key Strip

Every screen MUST display a footer key strip occupying the bottom 1–2 rows of the terminal. The footer MUST:

- Show all keys available in the current context.
- Update when context changes (e.g., different panel focused).
- Remain visible at all times — it MUST NOT be scrolled off-screen or hidden.

Format: `F1 Help  F5 Refresh  / Filter  q Quit` — key name followed by action label, separated by 2+ spaces. (CUA §1 function key area, Norton Commander F-key bar)

### §1.5 Minimum Dimensions

| Tier | Columns × Rows | Status |
|------|---------------|--------|
| Minimum viable | 80 × 24 | MUST support — application MUST remain functional |
| Standard | 120 × 40 | SHOULD target — primary design canvas |

Applications MUST NOT crash or produce garbled output at 80×24. Applications SHOULD present their full layout at 120×40. (Terminal §6 VT100 legacy, OS/2 §2)

### §1.6 Responsive Breakpoints

Applications MUST adapt layout at these column-width breakpoints:

| Breakpoint | Column Range | Layout Rule |
|------------|-------------|-------------|
| Compact | 40–79 | Region A collapses; Region C hidden or stacked below B; footer reduces to single row |
| Standard | 80–119 | Region A visible (narrow, 8–12 cols); Region C optional; full footer |
| Expanded | 120–159 | Full three-region layout; Region A at 12–16 cols |
| Wide | 160+ | Region A at full width (up to 20 cols); Region C expanded; extra whitespace in B |

Applications MUST handle terminal resize (SIGWINCH) and re-render within 100ms. Applications MUST NOT require a restart after resize. (Terminal §6 SIGWINCH, M3 §3 window size classes)

---

## §2 Keyboard Interaction

### §2.1 Primary Model

CUA is the primary keyboard model for all Monospace TUI applications. Every interactive element MUST be reachable and operable using only the keyboard. Mouse support is OPTIONAL and MUST NOT be required for any workflow. (CUA §1, KLM §5 keyboard efficiency advantage)

### §2.2 Standard Key Assignments

Every action in this standard has both a **CUA key** (F-key tradition) and a **common key** (non-F-key alternative). Both MUST be bound. Applications MUST NOT require F-keys for any workflow — the common key MUST always work as an equivalent path. This ensures usability on modern laptops where F-keys may require an Fn modifier.

**Case-insensitivity rule:** All single-letter key bindings MUST be case-insensitive — `r` and `R` trigger the same action, `d` and `D` trigger the same action, etc. Applications MUST bind both cases but MUST display only the lowercase form in the footer key strip. Displaying both cases is unnecessary clutter. The sole exception is the `g` / `G` scrolling pair (see Tier 1 Scrolling below), where case carries distinct meaning from vim convention.

**Tier 1 — Global keys** (MANDATORY, always active):

| Action | CUA Key | Common Key | Context |
|--------|---------|------------|---------|
| Help | F1 | `?` | Context-sensitive help for focused element |
| Back / Cancel | F3 | Esc | Return to previous screen or cancel dialog |
| Refresh | F5 | `r` (when no text input focused) | Reload current data |
| Scroll backward | F7 | Page Up | Scrollable content areas |
| Scroll forward | F8 | Page Down | Scrollable content areas |
| Activate menu bar | F10 | Alt | Toggle focus to action bar |
| Next field | — | Tab | Left-to-right, top-to-bottom order |
| Previous field | — | Shift+Tab | Reverse of Tab order |
| Confirm / activate | — | Enter | Submit form, press focused button |
| Toggle / select | — | Space | Toggles, checkboxes, radio buttons |
| Navigate within control | — | Arrow keys | Within a single control only |
| Quit application | — | `q` | When no text input focused; SHOULD confirm if unsaved state |
| Search / filter | — | `/` | Open search or filter input |

**Tier 1 — Text entry keys** (MANDATORY, active when a text input field is focused):

| Action | Key | Notes |
|--------|-----|-------|
| Cut | Ctrl+X | |
| Copy | Ctrl+C | MUST NOT conflict with SIGINT; use Ctrl+Ins as fallback |
| Paste | Ctrl+V | |
| Undo | Ctrl+Z | |

Applications MUST NOT reassign Tier 1 keys to different actions **unless an archetype explicitly overrides specific keys** (see §2.7). (CUA §1, lazygit/k9s/ranger/yazi/btop conventions)

**Tier 1 — Scrolling keys** (MANDATORY in scrollable content when no text input focused):

| Action | Key | Notes |
|--------|-----|-------|
| Top of list | `g` twice, or Home | Vim `gg` convention |
| Bottom of list | `G` (Shift+g), or End | Vim convention (**exception to case-insensitivity rule** — `g` and `G` are distinct) |
| Half-page down | Ctrl+D | |
| Half-page up | Ctrl+U | |
| Next search result | `n` | After `/` search; wraps from last to first result |

**Tier 2 — Common keys** (SHOULD be used when the action exists):

These keys are not mandatory for every application, but when an application provides the listed action, it MUST use the specified key. This prevents every app from inventing its own binding for the same concept.

| Action | Key | Notes |
|--------|-----|-------|
| Delete / remove | `d` | Contextual; MUST confirm destructive actions |
| Edit / modify | `e` | Open item for editing |
| Add / create | `a` | Create new item |
| Yank / copy value | `y` | Copy focused item's value to clipboard |
| Sort | `s` | Cycle or select sort column/order |
| Command mode | `:` | Open command input (colon-command pattern) |
| Suspend to background | Ctrl+Z | Standard Unix SIGTSTP |

All Tier 2 letter keys are case-insensitive per the global rule.

**Tier 3 — Screen mnemonic keys** (application-defined):

Applications with multiple top-level screens SHOULD assign single-letter mnemonics based on the screen name's first letter. These provide instant navigation without traversing menus.

Rules for Tier 3 keys:

- MUST NOT conflict with any Tier 1 or Tier 2 key.
- MUST be case-insensitive per the global rule (bind both cases, show only lowercase in footer).
- SHOULD prefer the first letter of the screen name.
- If a conflict exists with Tier 1/2, use the second letter or a distinctive letter.
- MUST be shown in the footer key strip.

Common mnemonic patterns (for reference, not prescriptive):

| Mnemonic | Screen | Rationale |
|----------|--------|-----------|
| `1`–`9` | Numbered screens | Best when >4 screens; lazygit/airlock pattern |
| `[` / `]` | Prev / next tab | Tab cycling; lazygit/yazi pattern |
| `d` | Dashboard | — |
| `w` | Wizard / setup | — |
| `i` | Init / initialize | — |
| `s` | Settings | Conflicts with Tier 2 `s` (sort) — see resolution below |
| `c` | Config | — |
| `l` | Logs | — |
| `m` | Models / monitor | — |

**Tier conflict resolution:** When a Tier 3 mnemonic would shadow a Tier 2 key, the application MUST either:

1. Use an alternative letter (e.g., `t` for Se**t**tings instead of `s`), or
2. Use Ctrl+letter (e.g., Ctrl+S for Settings, leaving `s` for sort), or
3. Use number keys (`1`–`9`) for all screen navigation, avoiding letter conflicts entirely.

**Key scope rules:** Single-letter keys (`q`, `r`, `/`, `d`, `e`, `a`, `s`, `g`, `n`, `y`, and Tier 3 mnemonics) MUST be suppressed when a text input widget has focus — in that context, keystrokes are literal character input. Only modified keys (Ctrl+, Alt+, F-keys) and Esc remain active during text entry. (CUA §1, vim conventions, lazygit/k9s/ranger/yazi/btop cross-application consensus, ~/projects/ codebase conventions)

### §2.3 Footer Key Discoverability

All available keys for the current context MUST be displayed in the footer key strip (§1.4). A key that is not shown in the footer MUST NOT be required to complete a task — though it MAY exist as an accelerator for expert users if the same action is available through a visible path. (CUA §1, Norton Commander §7)

### §2.4 Mnemonic Rules

Menu items and labeled controls SHOULD have mnemonic accelerators (underlined letters). Mnemonics:

- MUST be unique within their menu level or control group.
- SHOULD prefer the first letter of the label text.
- MUST NOT be a space character.
- MUST be marked in source with tilde (`~F~ile`) or ampersand (`&File`) prefix notation.

Typing the mnemonic character while its menu is active MUST select that item immediately. (CUA §1 mnemonic assignment rules, OS/2 §2)

### §2.5 Navigation Order

Tab order MUST follow left-to-right, top-to-bottom visual order for LTR locales, wrapping from last field to first. Arrow keys MUST move only within a single control (e.g., between radio buttons in a group, or characters in a text field) — arrow keys MUST NOT cross control boundaries. (CUA §1)

### §2.6 Composable Keyboard Layers

Archetypes MAY add additional keyboard layers beyond the CUA base, provided:

| Layer Type | Activation | Deactivation | Example |
|------------|-----------|--------------|---------|
| Modal | Explicit key (e.g., `i` for insert mode) | Explicit key (e.g., `Esc`) | Editor archetype |
| Prefix | Leader key (e.g., `Ctrl+B`) | Timeout or next key | Multiplexer pattern |
| Fuzzy | Typing in filter field | Esc or Enter | Fuzzy finder archetype |
| Context-panel | Focus moves to a different panel (Tab or click) | Focus leaves panel | File manager, lazygit-style apps |

- The current layer MUST be indicated in the status area or footer.
- Esc MUST always return to the base CUA layer.
- Layer-specific keys MUST NOT shadow CUA base keys unless the layer is explicitly activated.

(mono-tui.md §7 six keyboard interaction models)

### §2.7 Archetype Key Overrides

An archetype (§11) MAY override keys from the Tier 1 or Tier 2 tables when the archetype's domain conventions are universally established and would cause user confusion if replaced. When an archetype overrides a standard key:

- The override MUST be documented in the archetype's "Keyboard additions" table with the annotation "(overrides §2.2)".
- The overridden key's original action MUST remain accessible through an alternative key binding.
- The footer key strip MUST display the overridden binding, not the standard one.

Example: The File Manager archetype (§11.3) overrides F3 (normally Back/Cancel) with "View file" and F5/`r` (normally Refresh) with "Copy." In this archetype, Esc serves as Back/Cancel and Ctrl+R serves as Refresh. The `r` key is freed for reuse within the archetype since Refresh has moved to Ctrl+R.

(CUA §1, Norton Commander §7 — domain conventions)

---

## §3 Navigation Topology

### §3.1 Navigation Pattern Decision Tree

Choose the navigation pattern based on the relationship between views:

| Relationship | Pattern | Implementation |
|-------------|---------|---------------|
| Parallel contexts (peer-level views) | Tabs or sidebar items | Region A list or tab bar |
| Hierarchical drill-down | Screens (push/pop) | New screen replaces content |
| Transient confirmation or input | Modal dialog | Overlay with scrim |
| Contextual detail for selected item | Panel (split or overlay) | Region C or overlay pane |

Applications MUST NOT mix patterns for the same relationship type within a single workflow. (CUA §1, M3 §3 navigation patterns, tui-architect navigation topology)

### §3.2 Menu Hierarchy

Menus MUST follow a maximum three-level hierarchy:

1. **Action Bar** — top row, ≤6 items.
2. **Pull-Down Menu** — vertical list below action bar item, ≤10 items per menu.
3. **Cascaded Menu** — extends to the right, indicated by `▸` suffix, ≤1 level of cascading.

Applications MUST NOT cascade menus more than one level deep. (CUA §1 standard menu hierarchy)

### §3.3 Action Bar Order

When an action bar is present, items MUST appear in this standard order (omitting inapplicable items):

```
File  Edit  View  [Domain-specific]  Options  Help
```

- `File` and `Help` MUST be present if the application has an action bar.
- Domain-specific items (e.g., `Models`, `Guardrails`) appear between `View` and `Options`.
- Maximum 6 top-level items.

(CUA §1)

### §3.4 Unavailable Items

Menu items and controls that are currently unavailable MUST remain visible but rendered in the Disabled state (dim text, SGR 2). Unavailable items MUST NOT be hidden. This ensures users can discover features and understand why they are currently inaccessible. (CUA §1, Apple HIG §4)

### §3.5 Ellipsis Convention

A menu item that will open a dialog requiring further user input before executing MUST display an ellipsis suffix (`...`). A menu item that executes immediately MUST NOT display an ellipsis. (CUA §1)

---

## §4 Component Rules

### §4.1 Widget Selection

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

Applications SHOULD NOT deviate from this table. If an application uses a widget not listed here, it MUST document the rationale and ensure the widget follows the state model (§8) and keyboard rules (§2). (CUA §1 component specifications, tui-architect widget selection heuristics)

### §4.2 Default Button

Every dialog MUST have exactly one default button, visually distinguished from other buttons (e.g., bold label, bracket style `» OK «`). Pressing Enter when no other control captures it MUST activate the default button. (CUA §1)

### §4.3 Tab Order

Tab order MUST follow field layout: top-to-bottom, then left-to-right within each row. Tab order MUST be predictable — a user who presses Tab repeatedly MUST visit every interactive element in visual order and return to the first element. (CUA §1, §2.5)

### §4.4 Entry Field Conventions

- Empty entry fields MUST display fill characters (underscores `_` or dots `·`) to indicate their width.
- Entry fields MUST show a visible cursor at the current edit position.
- Entry fields with constrained input (numeric, date, etc.) MUST validate on field exit (Tab or Enter) and display an error state (§8) with explanatory text if validation fails.

(CUA §1 entry field specification)

---

## §5 Color System

### §5.1 Semantic Color Roles

Applications MUST define colors for these 5 semantic roles:

| Role | Purpose | Example Use |
|------|---------|-------------|
| Primary | Brand identity, key actions | Action bar, active tab indicator |
| Secondary | Supporting UI elements | Panel borders, secondary buttons |
| Tertiary | Accent, highlight | Links, selected items |
| Error | Error states, destructive actions | Error messages, delete buttons |
| Neutral | Backgrounds, body text, borders | Content area, panel backgrounds |

Colors MUST be assigned by semantic role, not by literal color name. Applications MUST NOT hardcode ANSI color indices directly in layout code — use a theme or token layer. (M3 §3 color system)

### §5.2 Status Colors

Applications MUST use these 4 semantic status colors consistently:

| Status | Color | Use |
|--------|-------|-----|
| Healthy / Success | Green | Passing checks, active services, confirmations |
| Error / Critical | Red | Failures, blocked states, destructive confirmations |
| Warning / Caution | Yellow | Degraded performance, approaching limits |
| Inactive / Disabled | Dim gray | Placeholder text, disabled controls, secondary info |

(tui-architect common violations — status color palette)

### §5.3 Color Independence

Color MUST NOT be the sole indicator of any state or meaning. Every use of color MUST be paired with at least one of:

- Text label (e.g., "Error:", "OK")
- Typographic attribute (bold, dim, underline)
- Symbol or marker (e.g., `✓`, `✗`, `⚠`, `◉`)

This rule is non-negotiable for accessibility. (Apple HIG §4 color independence, mono-tui.md cross-cutting synthesis)

### §5.4 Dialog Severity Colors

Dialogs MUST use background color to indicate severity:

| Severity | Background | Required Non-Color Indicator |
|----------|-----------|------------------------------|
| Notification / Info | Neutral background | Title or icon (e.g., `ℹ`) |
| Warning | Yellow-tinted background | `⚠` symbol and/or "Warning:" label |
| Critical / Error | Red-tinted background | `✗` symbol and/or "Error:" label |

Per §5.3, severity background color MUST be paired with a text label or symbol. A dialog with a red background and no textual severity indicator is a violation. (CUA §1 state indicators — pop-up severity colors)

### §5.5 Active/Inactive Window Distinction

Active windows MUST render with brighter color attributes than inactive windows. The distinction MUST be visible without relying on color alone — active windows MUST also use double-line borders (§6) and/or bold title text. (CUA §1, OS/2 §2)

### §5.6 Color Capability Detection

Applications MUST detect the terminal's color capability and degrade gracefully:

1. **Truecolor** (24-bit) — `COLORTERM=truecolor` or `COLORTERM=24bit`
2. **256-color** — `TERM` contains `256color`
3. **16-color** — Standard ANSI colors
4. **Monochrome** — Bold, dim, underline, reverse video only

Applications MUST NOT emit color codes unsupported by the detected capability level. Applications MUST remain fully functional in monochrome mode. (Terminal §6 color detection)

---

## §6 Border & Elevation

### §6.1 Elevation Levels

Applications MUST use exactly 5 elevation levels:

| Level | Use | Border Style | Shadow |
|-------|-----|-------------|--------|
| 0 | Inline content, flat text | None | None |
| 1 | Panels, content regions | Single-line (`─│┌┐└┘`) | None |
| 2 | Menus, dropdowns | Single-line (`─│┌┐└┘`) | 2-col × 1-row offset |
| 3 | Dialogs, secondary windows | Double-line (`═║╔╗╚╝`) | 2-col × 1-row offset |
| 4 | Modal overlays | Double-line (`═║╔╗╚╝`) | 2-col × 1-row + background scrim (dim) |

Applications MUST NOT use double-line borders for Level 0–2 elements. Applications MUST NOT use single-line borders for Level 3–4 elements. (OS/2 §2 window decoration, M3 §3 elevation levels, mono-tui.md cross-cutting synthesis)

### §6.2 Active/Inactive Window Borders

- Active (focused) windows: MUST use double-line borders (`═║╔╗╚╝`).
- Inactive (unfocused) windows: MUST use single-line borders (`─│┌┐└┘`).

This rule applies to **overlapping windows** (Level 3–4) that can independently gain or lose focus. The following are exempt and retain their elevation-defined border style regardless of focus:

- **Panels within a non-overlapping layout** (§1.3 regions) — SHOULD use single-line borders (Level 1).
- **Menus and dropdowns** (Level 2) — MUST use single-line borders; focus is indicated by the highlight bar on the selected item, not by border change.

(OS/2 §2, CUA §1)

### §6.3 Window Titles

Window and panel titles MUST be centered in the top border row:

```
╔══ Dialog Title ══════════════╗
┌── Panel Title ───────────────┐
```

The title text MUST be padded with at least one space on each side within the border. (OS/2 §2)

### §6.4 Shadow Rendering

Shadows at Levels 2–4 MUST be rendered as a 2-column × 1-row offset below and to the right of the bordered element. Shadow cells MUST:

- Preserve the underlying character codes.
- Apply attribute 0x08 (dim) to the underlying characters.

(OS/2 §2 shadow specification, Turbo Vision §7)

### §6.5 Scrim

Level 4 (modal overlay) MUST dim all background content behind the modal. The scrim MUST apply the dim attribute (SGR 2) to all non-modal cells while preserving their character content. (M3 §3 elevation)

### §6.6 Rounded Corners

Rounded corner characters (`╭╮╰╯`) MAY be used for cosmetic, non-interactive containers (e.g., decorative cards, informational callouts). Rounded corners MUST NOT be used for interactive windows, dialogs, or panels that participate in the elevation system. (Terminal §6 Unicode box drawing)

---

## §7 Typography

### §7.1 Text Treatments

Applications MUST use exactly 4 typographic treatments:

| Role | SGR Attributes | Use |
|------|---------------|-----|
| Display | Bold (SGR 1) + optional UPPERCASE | Screen titles, hero metrics |
| Title | Bold (SGR 1) | Section headers, panel titles, column headers |
| Body | Normal (no attributes) | Content text, field values, menu items |
| Label | Dim (SGR 2) | Secondary info, placeholders, help text, timestamps |

Applications MUST NOT combine more than 2 SGR attributes on a single text span (e.g., Bold + Underline is acceptable; Bold + Dim + Italic is not). (mono-tui.md cross-cutting synthesis — 4 text treatments)

### §7.2 Focus and Selection Indication

- Focused text MUST use reverse video (SGR 7).
- If reverse video is insufficient for the context (e.g., list items that are already highlighted), bracket markers `[▸ item ◂]` MAY be used as an alternative.

(mono-tui.md unified state model)

### §7.3 Error Text

Error text MUST use red foreground (SGR 31 or bright red SGR 91). For critical errors, a red background (SGR 41) MAY be used. Error text MUST be accompanied by an explanatory message — a red-colored field with no text explanation violates this rule. (CUA §1, §5.3 color independence)

---

## §8 State Model

### §8.1 Required States

Every interactive element MUST support and render these 6 mandatory states plus 1 conditional state:

| State | Rendering | Rule |
|-------|-----------|------|
| Enabled | Normal attributes (Body typography) | Default state for all interactive elements |
| Focused | Reverse video (SGR 7) or bracket markers `[▸ item ◂]` | Exactly one element MUST be focused at all times |
| Hovered | Underline (SGR 4) or highlight bar | Mouse-optional; render only if mouse tracking is active |
| Pressed | Brief reverse flash (≤100ms) | Visual feedback for activation; revert to Focused after |
| Selected | Reverse video + fill mark (`[X]` or `(*)`) | For multi-select contexts and radio/checkbox groups |
| Disabled | Dim (SGR 2) | Visible but non-interactive; MUST NOT be hidden (§3.4) |
| Error | Red foreground (SGR 31) or red background (SGR 41) | MUST include text explanation (§7.3) |

### §8.2 Focus Invariant

Exactly one interactive element MUST hold focus at all times. There MUST NOT be a state where no element is focused. When a focused element is removed from the screen (e.g., dialog closes), focus MUST transfer to the most recently focused element on the underlying screen. (CUA §1, Apple HIG §4 focus management)

### §8.3 Disabled Visibility

Disabled elements MUST remain visible in their normal position. Applications MUST NOT hide, remove, or reposition disabled elements. This ensures users can discover features and understand the complete interface surface. (CUA §1, §3.4)

---

## §9 Accessibility

### §9.1 Dual-Rendering Architecture

Applications SHOULD implement a dual-rendering architecture:

1. **Visual renderer** — ANSI escape sequences for sighted users (standard rendering).
2. **Linear semantic renderer** — Sequential text output without cursor jumping, suitable for screen readers.

The linear renderer SHOULD output content in reading order (top-to-bottom, left-to-right) with clear section labels. (Terminal §6 screen reader accessibility)

### §9.2 Scrolling Regions

Applications SHOULD use VT100 scrolling regions (`ESC[{top};{bottom}r`) for content that updates independently of the rest of the screen (e.g., log tails, data feeds). This reduces full-screen redraws that disrupt screen readers. (Terminal §6)

### §9.3 Text Labels

All interactive elements MUST have text labels that convey their purpose independent of visual position. A button that says "OK" MUST be in a context where its purpose is unambiguous, or it MUST have an associated label (e.g., dialog title "Delete file?"). (Apple HIG §4)

### §9.4 Color Independence

Restated for emphasis: Color MUST NOT be the sole indicator of any state or meaning (§5.3). This is a hard accessibility requirement, not a suggestion.

### §9.5 Minimum Contrast

When using truecolor (24-bit color):

- Body text MUST have a contrast ratio of at least **4.5:1** against its background.
- Bold or Display text MUST have a contrast ratio of at least **3:1** against its background.

When using 16 or 256 indexed colors, applications SHOULD select color pairs known to meet these ratios on common terminal themes. (Apple HIG §4 contrast requirements, WCAG 2.1 AA)

### §9.6 Focus Visibility

The focus indicator MUST be visible at all times (§8.2). The focus indicator MUST NOT rely solely on color — it MUST use reverse video, bracket markers, or border change. (Apple HIG §4)

---

## §10 Motion & Feedback

### §10.1 Timing Tiers

Applications MUST categorize all visual transitions into these 4 tiers:

| Tier | Duration | Use |
|------|----------|-----|
| Instant | 0ms | State toggles, key echo, character insertion |
| Fast | 50–100ms | Button press feedback, cursor movement animations |
| Standard | 150–300ms | Panel transitions, menu open/close, tab switch |
| Slow | 300–500ms | Screen transitions, progressive disclosure reveal |

Durations exceeding 500ms MUST NOT be used for UI transitions. (M3 §3 motion tokens, mono-tui.md cross-cutting synthesis)

### §10.2 Long-Running Operation Feedback

Any operation taking longer than 100ms MUST display immediate feedback:

- Operations <2s: spinner or progress indicator.
- Operations 2–10s: progress bar with percentage or step count.
- Operations >10s: progress bar with estimated time remaining.

Applications MUST NOT leave the terminal without visual feedback during any operation. A "hanging" terminal with no indication of progress is a violation. (tui-architect state transparency rule)

### §10.3 Terminal Capability Degradation

Applications MUST degrade motion gracefully based on terminal capabilities:

- Dumb terminals (`TERM=dumb`): All transitions MUST be Instant (0ms swap).
- Standard terminals: Full timing tiers apply.
- When `NO_MOTION=1` or `REDUCE_MOTION=1` environment variable is set: All transitions MUST be Instant.

(Apple HIG §4 reduced motion, Terminal §6)

---

## §11 Archetypes

An archetype defines a reusable screen pattern with a specific layout, keyboard layer, and component set. Applications MUST select one archetype per screen and adhere to its rules. Applications MAY combine archetypes across screens (e.g., a Dashboard screen and an Admin screen in the same application).

All archetypes inherit the CUA base keyboard (§2.2), three-region layout (§1.3), and footer key strip (§1.4).

### §11.1 Dashboard

**Purpose:** Real-time monitoring and status overview (htop, btop, system dashboards).

**Layout:**

```
╔══ Dashboard Title ══════════════════════════════╗
║ ▲ Metric A: 1,234  │ ◉ Status B  │ ⚠ Warns: 3  ║
╠═════════════════════════════════════════════════╣
║ Column 1    │ Column 2 │ Column 3 │ Column 4    ║
║ row data    │ ◉ OK     │  120ms   │ 0           ║
║ row data    │ ⚠ SLOW   │  890ms   │ 2           ║
║ row data    │ ◉ OK     │   45ms   │ 0           ║
╠═════════════════════════════════════════════════╣
║ ?Help  r Refresh  /Filter  s Sort  q Quit       ║
╚═════════════════════════════════════════════════╝
```

**Structure:**

| Area | Rows | Content |
|------|------|---------|
| Header metrics | 1–3 | Metric cards with status indicators |
| Data area | Flex | Scrollable data table or panel grid |
| Footer | 1–2 | Key strip |

**Keyboard (inherits all Tier 1; uses Tier 2 `s`, `/` from standard):**

| Key | Action | Tier |
|-----|--------|------|
| `?` | Help | Tier 1 (common key for F1) |
| `r` | Refresh | Tier 1 (common key for F5) |
| `/` | Activate filter input | Tier 1 |
| `s` | Cycle sort order (asc/desc) | Tier 2 |
| `q` | Quit | Tier 1 |
| Number keys (1–9) | Sort by column N | Archetype-specific |

**Key components:** Metric cards, data table, sparklines, status indicators.

**Example workflow — filter and sort a dashboard table:**

| Step | Key | Action | KLM |
|------|-----|--------|-----|
| 1 | `/` | Open filter | K = 0.28s |
| 2 | Type query | Filter text | M + nK |
| 3 | Enter | Apply filter | K = 0.28s |
| 4 | `s` | Sort focused column | K = 0.28s |
| Total | | 4 keystrokes + query | ~2.2s + typing |

### §11.2 Admin / Config

**Purpose:** Application configuration and settings management (setup wizards, settings panels).

**Layout:**

```
┌─ Categories ─┬── General Settings ──────────────┐
│               │                                  │
│ ▸ General     │  Application Name                │
│   Network     │  [ My App_____________ ]         │
│   Security    │                                  │
│   Advanced    │  Log Level                       │
│               │  (*) Info                        │
│               │  ( ) Debug                       │
│               │  ( ) Error                       │
│               │                                  │
│               │  Enable Caching                  │
│               │  [X] Enabled                     │
│               │                                  │
│               │  < Save >   < Cancel >           │
├───────────────┴──────────────────────────────────┤
│ F1 Help  Tab Next  Esc Cancel  Enter Save        │
└──────────────────────────────────────────────────┘
```

**Structure:**

| Area | Position | Content |
|------|----------|---------|
| Region A — Sidebar | Left, 8–16 cols | Category list |
| Region B — Form | Center, flex | Tabbed or sectioned form fields |
| Footer | Bottom, 1–2 rows | Key strip |

**Keyboard (inherits all Tier 1):**

| Key | Action | Tier |
|-----|--------|------|
| `?` | Help | Tier 1 |
| Esc | Back / cancel edit | Tier 1 |
| Ctrl+S | Save | Archetype |
| Number keys (1–9) | Jump to sidebar item N | Archetype |
| `[` / `]` | Previous / next settings tab | Archetype |

Note: Single-letter Tier 2 keys (`d`, `e`, `a`) are suppressed in the Admin archetype because form fields dominate the screen. Use Ctrl+ modified keys or buttons instead.

**Key components:** Entry fields, toggles/switches, radio groups, push buttons, tabbed content.

### §11.3 File Manager

**Purpose:** File system navigation and operations (Norton Commander, ranger, Midnight Commander).

**Layout (dual-pane):**

```
┌── /home/user ────────────┬── /home/user/docs ───────┐
│ ..                       │ ..                        │
│ ▸ documents/             │   report.pdf         12K  │
│   downloads/             │   notes.txt           2K  │
│   projects/              │   slides.pptx        45K  │
│   .bashrc            1K  │                           │
│   .gitconfig         2K  │                           │
├──────────────────────────┴───────────────────────────┤
│ user@host:~$                                         │
├──────────────────────────────────────────────────────┤
│ F3 View  F4 Edit  F5 Copy  F6 Move  F7 Mkdir  F8 Del│
└──────────────────────────────────────────────────────┘
```

**Structure:**

| Area | Position | Content |
|------|----------|---------|
| Left panel | Left, 50% | Directory listing with highlight bar |
| Right panel | Right, 50% | Directory listing or preview |
| Command line | 1 row above footer | Shell command input |
| Footer | Bottom, 1–2 rows | F-key operations |

**Keyboard (inherits Tier 1 with overrides per §2.7; uses context-panel layer §2.6):**

| Key | Action | Tier |
|-----|--------|------|
| Tab | Switch active panel | Archetype (context-panel layer §2.6) |
| Space or Insert | Select/deselect file | Tier 1 toggle + Norton convention |
| `/` | Filter file list | Tier 1 |
| `y` | Copy (yank) selected to other panel | Tier 2 |
| `d` | Delete selected (MUST confirm) | Tier 2 |
| `a` | Create directory | Tier 2 |
| `e` | Edit file | Tier 2 |
| `g` `g` / `G` | Top / bottom of list | Tier 1 scrolling |
| F3 | View file | Archetype (overrides §2.2) |
| F4 | Edit file (alias for `e`) | Archetype (Norton convention) |
| F5 | Copy to other panel (alias for `y`) | Archetype (overrides §2.2) |
| F6 | Move/rename selected | Archetype (Norton convention) |
| F7 | Create directory (alias for `a`) | Archetype (Norton convention) |
| F8 | Delete selected (alias for `d`) | Archetype (Norton convention) |
| Esc | Back / Cancel | Tier 1 (replaces F3) |
| Ctrl+R | Refresh | Archetype (replaces F5/`r`) |

**Key components:** File list with columns (name, size, date), path breadcrumb, selection markers.

(Norton Commander §7, OFM paradigm, §2.7 archetype key overrides)

### §11.4 Editor

**Purpose:** Text editing and document manipulation (Vim, Turbo Vision editor, nano).

**Layout:**

```
┌── filename.py ───────────────────── ln 42, col 8 ─┐
│  1 │ def calculate(x, y):                          │
│  2 │     result = x + y                            │
│  3 │     return result                             │
│  4 │                                               │
│  5 │ # TODO: add error handling                    │
│    │                                               │
├────┴───────────────────────────────────────────────┤
│ -- INSERT --                  UTF-8  LF  Python    │
├────────────────────────────────────────────────────┤
│ F1 Help  F2 Save  F3 Close  ^G Goto  ^F Find      │
└────────────────────────────────────────────────────┘
```

**Structure:**

| Area | Position | Content |
|------|----------|---------|
| Document area | Flex | Text buffer with optional line numbers |
| Status line | 1 row | Filename, cursor position, encoding, mode |
| Footer | 1–2 rows | Key strip |

**Keyboard (text input dominates — single-letter Tier 1/2 keys are suppressed by default):**

| Key | Action | Tier |
|-----|--------|------|
| Ctrl+S or F2 | Save | Archetype |
| Ctrl+F or `/` | Find (`/` only in normal mode) | Tier 1 (`/`) + Archetype (Ctrl+F) |
| Ctrl+G | Go to line | Archetype |
| `?` or F1 | Help (`?` only in normal mode) | Tier 1 |

The Editor archetype MAY add a modal keyboard layer (§2.6) for vi-style normal/insert/command modes. When a modal layer is active, Tier 1/2 single-letter keys (`q`, `r`, `d`, `e`, `a`, `s`, `g`, `n`, `y`) MAY be rebound within the normal-mode layer. If modal layers are used:

- The current mode MUST be displayed in the status line.
- Esc MUST return to normal/command mode.

**Key components:** Text buffer, line numbers, status bar, optional syntax highlighting.

### §11.5 Fuzzy Finder

**Purpose:** Rapid search and selection from large item sets (fzf, telescope, command palettes).

**Layout:**

```
┌── Find File ─────────────────────────────────────┐
│ > search query█                                  │
├──────────────────────────────────────────────────┤
│ ▸ src/utils/helpers.py              [92% match]  │
│   src/utils/http.py                 [87% match]  │
│   src/core/handler.py               [71% match]  │
│   tests/test_helpers.py             [65% match]  │
│                                                  │
│                                     4 / 128      │
├──────────────────────────────────────────────────┤
│ Enter Select  Esc Cancel  ↑↓ Navigate            │
└──────────────────────────────────────────────────┘
```

**Structure:**

| Area | Position | Content |
|------|----------|---------|
| Filter input | Top, 1 row | Text entry with type-to-filter |
| Results | Flex | Ranked result list with match scores |
| Preview | Optional, right split | Preview of focused result |
| Footer | 1 row | Key strip |

**Keyboard (fuzzy layer §2.6 — all printable input goes to filter):**

| Key | Action | Tier |
|-----|--------|------|
| Any printable character | Appends to filter | Fuzzy layer (§2.6) |
| Ctrl+N or Arrow Down | Next result | Archetype |
| Ctrl+P or Arrow Up | Previous result | Archetype |
| Enter | Select focused result and close | Tier 1 |
| Esc | Cancel and close | Tier 1 |
| Ctrl+D / Ctrl+U | Half-page down / up in results | Tier 1 scrolling |

Tier 1/2 single-letter keys (`q`, `r`, `/`, `d`, etc.) are captured by the filter input. Only Esc, Enter, and Ctrl+ modified keys remain functional. CUA navigation keys (Tab, F-keys) are suspended while the fuzzy layer is active.

**Key components:** Search input, scored result list, match highlighting, optional preview pane.

---

## Appendix A: Rule Index

For auditing convenience, every section's prescriptive rules are summarized:

| Section | Rule Count | Key MUST Rules |
|---------|-----------|---------------|
| §1 Grid & Layout | 6 | Three-region layout, footer always visible, 80×24 minimum, SIGWINCH handling |
| §2 Keyboard | 7 | CUA primary, 3-tier key system (F-key + common key duals), case-insensitivity, footer discoverability, key scope rules, composable layers, archetype overrides |
| §3 Navigation | 5 | Decision tree, 3-level menu max, unavailable items visible, ellipsis convention |
| §4 Components | 4 | Widget selection table, one default button, tab order, entry field fill characters |
| §5 Color | 6 | 5 semantic roles, 4 status colors, color independence, capability detection |
| §6 Borders | 6 | 5 elevation levels, active/inactive distinction, shadow rendering, scrim for modals |
| §7 Typography | 3 | 4 treatments only, reverse video for focus, error text requirements |
| §8 State Model | 3 | 6 mandatory + 1 conditional state, focus invariant, disabled visibility |
| §9 Accessibility | 6 | Dual rendering, scrolling regions, text labels, contrast ratios, focus visibility |
| §10 Motion | 3 | 4 timing tiers, long-operation feedback, capability degradation |
| §11 Archetypes | 5 | Dashboard, Admin, File Manager, Editor, Fuzzy Finder |

---

## Appendix B: Glossary

| Term | Definition |
|------|-----------|
| Character cell | The atomic rendering unit: 1 column × 1 row in a monospace terminal grid |
| CUA | IBM Common User Access — the base keyboard and interaction standard |
| Elevation | Visual layering depth, expressed as Level 0–4 |
| Footer key strip | The bottom 1–2 rows showing available keyboard actions |
| Mnemonic | An underlined letter in a menu or label enabling single-keystroke selection |
| Region | One of three layout areas (A=Navigation, B=Content, C=Context) |
| Scrim | A dim overlay applied to background content behind a modal |
| SGR | Select Graphic Rendition — ANSI escape codes for text styling |
| Monospace TUI | Monospace Design TUI — the design system defined by this standard (package: `mono-tui`) |
