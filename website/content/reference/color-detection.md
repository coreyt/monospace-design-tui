---
title: "§R7 Color Capability Detection"
description: "Detection algorithm and graceful degradation table for terminal color capabilities"
weight: 7
---

## §R7.1 Detection Algorithm

Applications MUST detect color capability at startup using this priority order:

```
1. If COLORTERM == "truecolor" or COLORTERM == "24bit":
     → Truecolor (24-bit, 16.7M colors)
2. Else if TERM contains "256color":
     → 256-color mode
3. Else if TERM == "dumb":
     → Monochrome (attributes only: bold, dim, underline, reverse)
4. Else:
     → 16-color ANSI (standard + bright)
```

## §R7.2 Graceful Degradation

| Feature | Truecolor | 256-color | 16-color | Monochrome |
|---------|----------|-----------|----------|------------|
| Semantic roles ([§R3.2](/reference/color-palette/#r32-semantic-role--256-color-mapping)) | Exact hex | Nearest 256 index | Nearest ANSI | N/A |
| Status colors ([§R3.3](/reference/color-palette/#r33-status-color-mapping)) | Exact hex | Nearest 256 index | Standard red/green/yellow | Bold/dim/reverse |
| Elevation shadows | Dim + color | Dim + index 240 | Dim (SGR 2) | Reverse video strip |
| Scrim (Level 4) | Semi-transparent dim | Dim all bg cells | Dim all bg cells | Reverse video border |
| Typography | Full SGR | Full SGR | Full SGR | Bold, dim, reverse only |
