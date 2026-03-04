---
title: "§R6 Braille Sparkline Encoding"
description: "Braille pattern block, dot-to-bit mapping, sparkline construction, progress bar encoding"
weight: 6
---

## §R6.1 Braille Pattern Block

Unicode Braille Patterns occupy U+2800–U+28FF (256 characters). Each character represents a 2×4 dot matrix within one character cell, providing **2× horizontal and 4× vertical sub-cell resolution**.

## §R6.2 Dot Position → Bit Mapping

Each Braille character's codepoint is `U+2800 + bitmask`, where bits map to dot positions:

```
Position:    Bit:
┌───┬───┐
│ 1 │ 4 │   bit 0 = dot 1 (top-left)
│ 2 │ 5 │   bit 1 = dot 2 (mid-left)
│ 3 │ 6 │   bit 2 = dot 3 (lower-left)
│ 7 │ 8 │   bit 3 = dot 7 (bottom-left)
└───┴───┘   bit 4 = dot 4 (top-right)
            bit 5 = dot 5 (mid-right)
            bit 6 = dot 6 (lower-right)
            bit 7 = dot 8 (bottom-right)
```

## §R6.3 Sparkline Construction Algorithm

To render a sparkline from a sequence of values:

1. **Normalize** values to a 0–3 range (for single-column sparklines) or 0–7 range (for two-column sparklines using both dot columns).
2. **For each character cell** in the sparkline, determine which vertical dots to fill based on the normalized value. A value of 0 = no dots; a value of 3 = dots at positions 7, 3, 2 (bottom three on left column).
3. **Compute the bitmask** by OR-ing the bits for each active dot position.
4. **Emit** `U+2800 + bitmask`.

**Example — single-column bar chart (left column only):**

| Value (0–4) | Active dots | Bitmask | Character |
|-------------|------------|---------|-----------|
| 0 | none | 0x00 | `⠀` (blank) |
| 1 | 7 | 0x40 | `⡀` |
| 2 | 3, 7 | 0x44 | `⡄` |
| 3 | 2, 3, 7 | 0x46 | `⡆` |
| 4 | 1, 2, 3, 7 | 0x47 | `⡇` |

## §R6.4 Progress Bar Using Eighth Blocks

For linear progress bars, use eighth-block characters for smooth fill:

| Progress | Character Sequence |
|----------|-------------------|
| 0/8 | ` ` (space) |
| 1/8 | `▏` (U+258F) |
| 2/8 | `▎` (U+258E) |
| 3/8 | `▍` (U+258D) |
| 4/8 | `▌` (U+258C) |
| 5/8 | `▋` (U+258B) |
| 6/8 | `▊` (U+258A) |
| 7/8 | `▉` (U+2589) |
| 8/8 | `█` (U+2588) |

A progress bar of width W cols at P% completion:

```
filled_cells = floor(W * P / 100)
partial = ((W * P / 100) - filled_cells) * 8   → index into eighth-block table
output = "█" × filled_cells + eighth_block[partial] + " " × remaining
```
