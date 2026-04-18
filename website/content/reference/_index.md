---
title: "Rendering Reference"
subtitle: "v0.2.5 — Exact characters, SGR codes, and measurements for implementers"
description: "Unicode codepoints, SGR escape sequences, component measurements, and color palettes"
---
This companion document to the [Design Standard]({{< relref "/standard/_index.md" >}}) provides the exact character codes, escape sequences, color mappings, and component measurements needed to implement compliant Monospace TUI applications. Where the standard says *what* to do, this reference says *how* — down to the Unicode codepoint and SGR parameter.

## Start Here

If you are choosing the visual system for a Mono TUI implementation, start with these reference plates:

- [§R3 256-Color Palette]({{< relref "/reference/color-palette.md" >}}) — semantic roles, named palettes, and rendered palette examples
- [§R4 Component Measurements]({{< relref "/reference/measurements.md" >}}) — exact character-cell sizing rules
- [§R1 Box-Drawing Characters]({{< relref "/reference/box-drawing.md" >}}) — borders, indicators, and shading glyphs
- [§R5 Shadow Rendering]({{< relref "/reference/shadows.md" >}}) — shadow algorithm and scrim treatment for dialogs and modals
