---
name: mono-tui-audit
description: Audit TUI code for compliance with the Monospace Design TUI standard. Produces a structured pass/fail report respecting project overrides in TUI-DESIGN.md. Use after building or modifying TUI screens.
---

# Mono-TUI Audit

Audit terminal user interface code for compliance with the
[Monospace Design TUI Standard](../../monospace-tui-design-standard.md), respecting
project-specific overrides in `TUI-DESIGN.md`.

## Invocation

```
/tui-audit                      # Audit all TUI code in current project
/tui-audit src/tui/             # Audit specific directory
/tui-audit src/tui/dashboard.py # Audit specific file
```

When invoked without a path, scan for TUI-related files (`.py` files importing
`textual`, `curses`, or containing ANSI escape sequences).

## Audit Algorithm

### Phase 1: Load Ruleset

1. **Read the Design Standard** (`monospace-tui-design-standard.md`).
   Extract every rule that uses RFC 2119 language (MUST, MUST NOT, SHOULD,
   SHOULD NOT, MAY). Each rule has:
   - **ID**: Section number (e.g., `§1.3`, `§2.2`, `§5.3`)
   - **Level**: MUST or SHOULD (MAY rules are informational, not audited)
   - **Text**: The falsifiable requirement

2. **Read the Rendering Reference** (`monospace-tui-rendering-reference.md`).
   Extract `§R`-prefixed rules using the same criteria.

3. **Read TUI-DESIGN.md** from the project root (or nearest ancestor).
   Parse the `## Overrides` section. For each H3 heading matching:
   ```
   ### [ACTION] §X.Y ...
   ```
   Extract:
   - **Rule ID**: `§X.Y` or `§RX.Y`
   - **Action**: `WAIVE`, `OVERRIDE`, or `TIGHTEN`
   - **Original**: The `**Original:**` field text
   - **Replacement**: The `**Replacement:**` field text (OVERRIDE/TIGHTEN only)
   - **Scope**: The `**Scope:**` field text (for scoped overrides)

4. **Read TUI-DESIGN.md Project Conventions** (`## Project Conventions`).
   For each H3 heading matching `### [P#] ...`, extract:
   - **ID**: `P1`, `P2`, etc.
   - **Level**: From the `**Level:**` field
   - **Text**: The convention's requirement text

### Phase 2: Merge Ruleset

Build the effective ruleset by merging standard rules with overrides:

```
For each standard rule §X.Y:
    If TUI-DESIGN.md has [WAIVE] §X.Y:
        → Mark as WAIVED
        → Check staleness: compare Original field against current standard text
    Elif TUI-DESIGN.md has [OVERRIDE] §X.Y:
        → Replace rule text with Replacement field
        → Check staleness: compare Original field against current standard text
    Elif TUI-DESIGN.md has [TIGHTEN] §X.Y:
        → Upgrade SHOULD → MUST (or MAY → SHOULD)
        → Replace rule text with Replacement field
        → Check staleness
    Else:
        → Use standard rule as-is

Append all [P#] conventions as additional rules.
```

### Phase 3: Scan Code

For each target file, check the effective ruleset. Rules are grouped by
what can be detected through code analysis:

**Statically checkable** (grep/AST analysis):

| Rule | What to Check |
|------|---------------|
| §1.4 Footer | `Footer()` in compose/layout; BINDINGS declared |
| §2.2 Key bindings | BINDINGS list contains required Tier 1 keys; `ci()` used for letter keys |
| §2.2 Case-insensitivity | No letter binding without its case counterpart (except g/G) |
| §2.2 F-key duals | Every F-key binding has a common key equivalent |
| §4.1 Widget selection | Widget choices match data types (boolean → Switch, 2-5 options → RadioSet, etc.) |
| §5.3 Color independence | Status/state indicators have text labels or symbols alongside color |
| §6.1 Elevation borders | CSS border styles match elevation levels |
| §7.1 Typography | Text styles limited to 4 roles; no >2 SGR attributes combined |
| §8.1 States | Focus, disabled, error states handled |
| §10.2 Long operations | I/O uses @work decorator; no time.sleep() on main thread |
| §T3.1 Async (Textual) | All I/O in @work-decorated methods |
| §T3.2 Worker rules (Textual) | Worker.cancelled and Worker.error handled; no time.sleep() on main thread |

**Structurally checkable** (layout/architecture review):

| Rule | What to Check |
|------|---------------|
| §1.3 Three-region layout | Screen has navigation, content, (optional) context regions |
| §1.6 Responsive | Resize handler exists; breakpoint classes applied |
| §3.1 Navigation topology | Push/pop for drill-down, tabs for parallel, modals for transient |
| §3.2 Menu hierarchy | No more than 3 levels of menus |
| §3.4 Unavailable items | Disabled items visible, not hidden |
| §11 Archetype | Screen follows declared archetype's layout and keyboard |

**Manually verifiable** (require runtime or visual inspection):

| Rule | Report as |
|------|-----------|
| §5.5 Active/inactive distinction | MANUAL — verify active windows use brighter attributes |
| §6.4 Shadow rendering | MANUAL — verify shadows render at correct offset |
| §8.2 Focus invariant | MANUAL — verify exactly one element always focused |
| §9.5 Minimum contrast | MANUAL — verify 4.5:1 contrast ratio |
| §10.1 Timing tiers | MANUAL — verify transition durations match tiers |

### Phase 4: Produce Report

Generate a structured compliance report in this exact format:

```markdown
# Mono-TUI Compliance Report

**Project:** {project name from TUI-DESIGN.md Meta, or directory name}
**Standard version:** 0.2.5
**Audited:** {date}
**Scope:** {files/directories audited}

## Summary

| Status | Count |
|--------|-------|
| PASS | {n} |
| FAIL | {n} |
| WAIVED | {n} |
| OVERRIDDEN | {n} |
| TIGHTENED | {n} |
| STALE | {n} |
| MANUAL | {n} |
| N/A | {n} |

{If any FAIL: "**Action required:** {count} violations found."}
{If any STALE: "**Review required:** {count} stale overrides — standard text has changed."}

## Violations

{Only if FAIL count > 0. List each violation with:}

### FAIL §X.Y — {rule summary}

- **Level:** MUST / SHOULD
- **Rule:** {rule text}
- **Finding:** {what was found or not found}
- **Location:** {file:line or general}
- **Fix:** {specific recommendation}

## Stale Overrides

{Only if STALE count > 0. List each:}

### STALE [ACTION] §X.Y — {override summary}

- **TUI-DESIGN.md says:** {Original field from override}
- **Standard now says:** {current rule text}
- **Action needed:** Review override and update Original field, or remove if no longer needed.

## Full Results

| Rule | Level | Status | Detail |
|------|-------|--------|--------|
| §1.1 | MUST | N/A | Atomic unit — structural |
| §1.3 | MUST | PASS | Three-region layout found |
| §1.4 | MUST | FAIL | No Footer widget in compose() |
| §2.2 | MUST | PASS | All Tier 1 keys bound |
| §2.2-ci | MUST | FAIL | `r` bound without `R` counterpart |
| §5.1 | MUST | OVERRIDDEN | 6 colors per [OVERRIDE] §5.1 — PASS |
| §5.3 | MUST | PASS | All status colors have paired symbols |
| §9.3 | SHOULD→MUST | TIGHTENED | 4.5:1 contrast per [TIGHTEN] §9.3 — PASS |
| §2.2-footer | MUST | WAIVED | Footer hidden in editor mode per [WAIVE] §2.2 |
| [P1] | MUST | PASS | All screen classes end with Screen |
| [P2] | MUST | FAIL | Health indicators not in severity order |
```

## Report Statuses

| Status | Meaning | Action |
|--------|---------|--------|
| **PASS** | Rule satisfied | None |
| **FAIL** | Rule violated | Fix required (MUST) or recommended (SHOULD) |
| **WAIVED** | Rule intentionally skipped per TUI-DESIGN.md | None — inform only |
| **OVERRIDDEN** | Rule replaced per TUI-DESIGN.md; check replacement | Check replacement rule |
| **TIGHTENED** | SHOULD elevated to MUST per TUI-DESIGN.md | Check tightened rule |
| **STALE** | Override's Original text doesn't match current standard | Review override |
| **MANUAL** | Cannot verify automatically; requires visual/runtime check | Human review |
| **N/A** | Rule is structural/conceptual, not code-checkable | None |

## Severity Mapping

- **MUST violation** → Blocker. Must be fixed before the TUI is compliant.
- **SHOULD violation** → Warning. Should be fixed unless there's a documented reason not to.
- **MAY violation** → Not audited. MAY rules are informational.
- **STALE override** → Review. The standard has changed since the override was written.
  The override may still be valid, but the `Original:` text needs updating.

## Staleness Detection

For each override in TUI-DESIGN.md, compare the `**Original:**` field against
the current standard text for that rule ID. If they differ:

1. Report as STALE with both texts shown
2. Do NOT treat the override as invalid — it may still be intentionally correct
3. Recommend the human review the override and update the `Original:` field

This catches cases where the standard was updated but project overrides
weren't reviewed against the new version.

## Edge Cases

**No TUI-DESIGN.md found:**
- Report all rules against the unmodified standard
- Add a note: "No TUI-DESIGN.md found. All standard rules applied without overrides."
- Suggest creating one if the project has intentional deviations

**Scoped overrides:**
- When an override has a `**Scope:**` field (e.g., "Editor archetype screens only"),
  only apply the override to files/screens matching that scope
- Report the original rule for files outside the scope

**Multiple archetypes:**
- When TUI-DESIGN.md declares multiple archetypes, verify each screen follows
  its declared archetype's rules
- A Dashboard screen is checked against §11.1; an Admin screen against §11.2

**Framework detection:**
- If Textual: also check §T-prefixed rules from the Textual Appendix
- If curses/raw ANSI: check §R-prefixed rendering rules
- Report framework-specific rules only when the framework is detected

## Rules

- **Always** check for TUI-DESIGN.md before auditing.
- **Always** produce the structured report format — never skip sections.
- **Always** show the full results table, even for passing rules.
- **Always** detect staleness for every override.
- **Never** report a WAIVED rule as FAIL.
- **Never** treat a STALE override as invalid — flag for review only.
- **Never** audit MAY rules — they are informational.
- **Never** skip Project Conventions ([P#] rules) — they are audited like standard rules.

## Related Documents

| Document | Path | Purpose |
|----------|------|---------|
| Design Standard | `monospace-tui-design-standard.md` | Source of all §-prefixed rules |
| Rendering Reference | `monospace-tui-rendering-reference.md` | Source of all §R-prefixed rules |
| Textual Appendix | `monospace-tui-textual-appendix.md` | Source of §T-prefixed rules (Textual only) |
| TUI-DESIGN.md | Project root | Overrides, conventions, and decisions |
| TUI-DESIGN.template.md | `TUI-DESIGN.template.md` | Template for new projects |
