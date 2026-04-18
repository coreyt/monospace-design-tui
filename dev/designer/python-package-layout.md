# Mono Designer Python Package Layout

This document defines the module structure for the `0.3.0` implementation of the Mono Designer toolset.

The implementation root is `/mono-designer/`.

## Package Philosophy

- **Modular**: Separate concern between the artifact models, the projection logic, and the CLI interface.
- **Python-First**: Standard modern Python structure using type hints and Pydantic for validation.
- **Stateless Projectors**: Projection functions should be pure, mapping models to strings without side effects.

## Directory Structure

```text
/mono-designer/
├── pyproject.toml             # Project metadata and dependencies
├── mono_designer/             # Main package
│   ├── __init__.py
│   ├── cli/                   # CLI implementation (using Typer or argparse)
│   │   ├── __init__.py
│   │   ├── main.py            # Entry point
│   │   ├── nav.py             # Navigation commands
│   │   ├── workflow.py        # Workflow commands
│   │   └── screen.py          # Screen commands
│   ├── models/                # Pydantic models (Canonical and DSL)
│   │   ├── __init__.py
│   │   ├── base.py            # Shared metadata and mixins
│   │   ├── navigation.py      # Navigation models
│   │   ├── workflow.py        # Workflow models
│   │   └── screen.py          # Screen models
│   ├── core/                  # Core logic and normalization
│   │   ├── __init__.py
│   │   ├── normalization.py   # Maps YAML models to DSL models
│   │   └── validation.py      # High-level consistency checks
│   ├── projectors/            # ASCII projection logic
│   │   ├── __init__.py
│   │   ├── ascii_nav.py       # Navigation -> ASCII
│   │   ├── ascii_workflow.py  # Workflow -> ASCII
│   │   └── ascii_screen.py    # Screen -> ASCII
│   └── utils/                 # Shared utilities
│       ├── __init__.py
│       └── yaml_io.py         # Standardized YAML read/write
└── tests/                     # Test suite
    ├── unit/
    └── integration/
```

## Module Responsibilities

### `models/`
Defines the structure of the canonical YAML artifacts. These models ensure that any artifact loaded into the system adheres to the `0.3.0` specification.

### `core/normalization.py`
Contains the logic to transform raw YAML-backed models into the "Minimal Mono DSL" objects. This allows the projectors to work against a stable semantic layer rather than varying YAML shapes.

### `projectors/`
The "renderer" of the designer system. These modules take DSL objects and produce the ASCII output required for HITL review.

### `cli/`
The primary interface for agents and humans.
Commands should include:
- `mono-designer nav generate`
- `mono-designer workflow generate`
- `mono-designer screen generate`
- `mono-designer project <file>`

## Dependencies (0.3.0)

- `pydantic`: For data modeling and validation.
- `ruamel.yaml`: For YAML round-tripping (preserving comments where possible).
- `typer`: For the CLI interface.
- `rich`: For enhanced CLI output (though canonical ASCII artifacts remain plain text).
