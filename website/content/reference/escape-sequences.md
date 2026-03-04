---
title: "§R8 Escape Sequence Quick Reference"
description: "Cursor movement, scrolling regions, screen operations, and mouse tracking sequences"
weight: 8
---

## §R8.1 Cursor Movement

| Sequence | Action |
|----------|--------|
| `ESC[{n}A` | Cursor up n rows |
| `ESC[{n}B` | Cursor down n rows |
| `ESC[{n}C` | Cursor right n cols |
| `ESC[{n}D` | Cursor left n cols |
| `ESC[{row};{col}H` | Move cursor to row, col (1-based) |
| `ESC[s` | Save cursor position |
| `ESC[u` | Restore cursor position |
| `ESC[?25h` | Show cursor |
| `ESC[?25l` | Hide cursor |

## §R8.2 Scrolling Regions

| Sequence | Action |
|----------|--------|
| `ESC[{top};{bottom}r` | Set scrolling region (1-based row numbers) |
| `ESC[r` | Reset scrolling region to full screen |

## §R8.3 Screen Operations

| Sequence | Action |
|----------|--------|
| `ESC[2J` | Clear entire screen |
| `ESC[K` | Clear from cursor to end of line |
| `ESC[1K` | Clear from start of line to cursor |
| `ESC[2K` | Clear entire line |

## §R8.4 Mouse Tracking (SGR Extended)

| Sequence | Action |
|----------|--------|
| `ESC[?1000h` | Enable basic mouse tracking |
| `ESC[?1002h` | Enable button-event (drag) tracking |
| `ESC[?1003h` | Enable all-motion tracking |
| `ESC[?1006h` | Enable SGR extended encoding |
| `ESC[?1000l` | Disable mouse tracking |
| `ESC[?1006l` | Disable SGR encoding |

SGR mouse event format: `ESC[<{button};{col};{row}M` (press) or `m` (release).

Button values: 0=left, 1=middle, 2=right, 64=scroll-up, 65=scroll-down. Modifier bits: +4=Shift, +8=Meta, +16=Control.
