---
title: "Prototyping Guide"
weight: 30
---

# Interactive TUI Prototyping

Terminal User Interfaces are highly sensitive to information density and keyboard ergonomics. Because TUIs lack pointers or trackpads, designs that look clean in a static wireframe often fail when users actually try to navigate them.

Therefore, Monospace explicitly mandates **TUI-First Prototyping**.

**Never build web-based UI mockups (e.g., React, HTML/CSS, or Figma prototypes) to test a terminal application.** It guarantees that you will design interactions that cannot be effectively mapped to the terminal grid.

Instead, we progress through four levels of prototyping directly in the terminal.

## Level 0: Static ASCII Wireframes

Level 0 is the immediate output of the Monospace Designer. 

A user generates a conceptual YAML `ScreenSpec`, and the `mono-designer project` tool returns a static ASCII projection. This confirms structural placement, footer key existence, and overall focus logic.

You should spend the vast majority of your early design phase entirely in Level 0, iterating on workflow shapes via YAML.

## Level 1: Navigable Shell

Level 1 takes the YAML specifications and translates them into actual rendering code (e.g., Python/Textual or Go/Bubbletea).

- **Purpose:** To test the "Navigation Topology" (§3). Does the `Esc` key reliably pop the screen stack? Do modal overlays work?
- **Fidelity:** Very low. The components are empty placeholder boxes labeled with their `id` and `purpose`.
- **State:** "Fake". There is no local state or data. Hardcoded hotkeys simply `push()` or `pop()` views.

```python
# Level 1 Textual Shell Example
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Vertical

class Placeholder(Static):
    """A generic box for Level 1 prototyping."""

class MainScreen(Screen):
    BINDINGS = [
        ("enter", "inspect_service", "Inspect"),
        ("q", "quit", "Quit")
    ]
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(Placeholder("metric-cards: key metrics"))
        yield Vertical(Placeholder("service-table: service status list"))
        yield Footer()

    def action_inspect_service(self):
        self.app.push_screen(DetailScreen())
```

## Level 2: Interactive Data-Entry

Level 2 replaces the placeholder boxes with real framework widgets (e.g., a true `DataTable` or `Input`).

- **Purpose:** To test the "Keyboard Interaction" (§2). Can the user navigate between inputs? Are single-letter bindings suppressed correctly when text fields are focused?
- **Fidelity:** Medium. The screens look like the final application.
- **State:** Local Mock State. The tables contain hardcoded sample rows. Forms validate input locally but don't save anywhere.

## Level 3: Workflow Simulation

Level 3 links the Level 2 screens together and simulates the asynchronous backend.

- **Purpose:** To test the "State Model" (§8) and "Motion & Feedback" (§10). How does the TUI respond when a simulated API call takes 3 seconds? How do loaders and disabling work?
- **Fidelity:** High.
- **State:** Simulated Backend. Clicking 'Refresh' triggers a Python `@work` thread that `time.sleep(2)` and then posts a message updating the UI with new mock data.

*When you have completed a Level 3 prototype, you are ready to hand off to the engineering team for true backend implementation.*