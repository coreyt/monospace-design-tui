---
title: "§2 Keyboard Interaction"
description: "CUA keyboard model, three-tier key system, composable layers, archetype overrides"
weight: 2
---

## §2.1 Primary Model

CUA is the primary keyboard model for all Monospace TUI applications. Every interactive element MUST be reachable and operable using only the keyboard. Mouse support is OPTIONAL and MUST NOT be required for any workflow. (CUA §1, KLM §5 keyboard efficiency advantage)

## §2.2 Standard Key Assignments

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

Applications MUST NOT reassign Tier 1 keys to different actions **unless an archetype explicitly overrides specific keys** (see [§2.7](#27-archetype-key-overrides)). (CUA §1, lazygit/k9s/ranger/yazi/btop conventions)

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

## §2.3 Footer Key Discoverability

All available keys for the current context MUST be displayed in the footer key strip ([§1.4](/standard/layout/#14-footer-key-strip)). A key that is not shown in the footer MUST NOT be required to complete a task — though it MAY exist as an accelerator for expert users if the same action is available through a visible path. (CUA §1, Norton Commander §7)

## §2.4 Mnemonic Rules

Menu items and labeled controls SHOULD have mnemonic accelerators (underlined letters). Mnemonics:

- MUST be unique within their menu level or control group.
- SHOULD prefer the first letter of the label text.
- MUST NOT be a space character.
- MUST be marked in source with tilde (`~F~ile`) or ampersand (`&File`) prefix notation.

Typing the mnemonic character while its menu is active MUST select that item immediately. (CUA §1 mnemonic assignment rules, OS/2 §2)

## §2.5 Navigation Order

Tab order MUST follow left-to-right, top-to-bottom visual order for LTR locales, wrapping from last field to first. Arrow keys MUST move only within a single control (e.g., between radio buttons in a group, or characters in a text field) — arrow keys MUST NOT cross control boundaries. (CUA §1)

## §2.6 Composable Keyboard Layers

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

## §2.7 Archetype Key Overrides

An archetype ([§11](/standard/archetypes/)) MAY override keys from the Tier 1 or Tier 2 tables when the archetype's domain conventions are universally established and would cause user confusion if replaced. When an archetype overrides a standard key:

- The override MUST be documented in the archetype's "Keyboard additions" table with the annotation "(overrides §2.2)".
- The overridden key's original action MUST remain accessible through an alternative key binding.
- The footer key strip MUST display the overridden binding, not the standard one.

Example: The File Manager archetype ([§11.3](/standard/archetypes/#113-file-manager)) overrides F3 (normally Back/Cancel) with "View file" and F5/`r` (normally Refresh) with "Copy." In this archetype, Esc serves as Back/Cancel and Ctrl+R serves as Refresh. The `r` key is freed for reuse within the archetype since Refresh has moved to Ctrl+R.

(CUA §1, Norton Commander §7 — domain conventions)
