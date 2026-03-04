---
title: "§10 Motion & Feedback"
description: "Four timing tiers, long-running operation feedback, terminal capability degradation"
weight: 10
---

## §10.1 Timing Tiers

Applications MUST categorize all visual transitions into these 4 tiers:

| Tier | Duration | Use |
|------|----------|-----|
| Instant | 0ms | State toggles, key echo, character insertion |
| Fast | 50–100ms | Button press feedback, cursor movement animations |
| Standard | 150–300ms | Panel transitions, menu open/close, tab switch |
| Slow | 300–500ms | Screen transitions, progressive disclosure reveal |

Durations exceeding 500ms MUST NOT be used for UI transitions. (M3 §3 motion tokens, mono-tui.md cross-cutting synthesis)

## §10.2 Long-Running Operation Feedback

Any operation taking longer than 100ms MUST display immediate feedback:

- Operations <2s: spinner or progress indicator.
- Operations 2–10s: progress bar with percentage or step count.
- Operations >10s: progress bar with estimated time remaining.

Applications MUST NOT leave the terminal without visual feedback during any operation. A "hanging" terminal with no indication of progress is a violation. (tui-architect state transparency rule)

## §10.3 Terminal Capability Degradation

Applications MUST degrade motion gracefully based on terminal capabilities:

- Dumb terminals (`TERM=dumb`): All transitions MUST be Instant (0ms swap).
- Standard terminals: Full timing tiers apply.
- When `NO_MOTION=1` or `REDUCE_MOTION=1` environment variable is set: All transitions MUST be Instant.

(Apple HIG §4 reduced motion, Terminal §6)
