# Mono Designer Schema Models

This document defines the Python-ready schemas (intended for Pydantic) for Mono Designer artifacts in `0.3.0`.

## Base Artifact Metadata

All artifacts inherit from a common base to ensure consistency across the system.

```python
from datetime import datetime
from typing import List, Optional, Literal, Union, Dict
from pydantic import BaseModel, Field

class ArtifactSource(BaseModel):
    kind: Literal["generated", "manual", "imported"]
    inputs: List[str] = []

class BaseArtifact(BaseModel):
    version: str = "0.3.0"
    artifact_type: str
    id: str
    title: str
    purpose: str
    source: ArtifactSource
    status: Literal["draft", "reviewed", "approved"] = "draft"
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    notes: List[str] = []
```

## 1. Navigation Models

```python
class Workspace(BaseModel):
    id: str
    label: str
    purpose: Optional[str] = None

class Route(BaseModel):
    id: Optional[str] = None
    from_workspace: str = Field(alias="from")
    to_workspace: str = Field(alias="to")
    kind: Literal["push", "pop", "modal", "jump", "switch"]
    trigger: Optional[str] = None
    notes: Optional[str] = None

class NavigationSpec(BaseArtifact):
    artifact_type: Literal["navigation"] = "navigation"
    workspaces: List[Workspace]
    routes: List[Route]
    rules: List[str] = []
```

## 2. Workflow Models

```python
class WorkflowStage(BaseModel):
    id: str
    label: str
    purpose: str
    screen_ids: List[str] = []

class WorkflowTransition(BaseModel):
    id: Optional[str] = None
    from_stage: str = Field(alias="from")
    to_stage: str = Field(alias="to")
    trigger: str
    kind: Literal["advance", "return", "modal", "jump"]

class Checkpoint(BaseModel):
    id: str
    label: str
    type: Literal["approve", "revise", "continue", "cancel", "collect_more", "publish"]
    stage_id: str

class WorkflowSpec(BaseArtifact):
    artifact_type: Literal["workflow"] = "workflow"
    entry_conditions: List[str] = []
    exit_conditions: List[str] = []
    stages: List[WorkflowStage]
    transitions: List[WorkflowTransition]
    checkpoints: List[Checkpoint]
    assumptions: List[str] = []
    linked_screens: List[str] = []
```

## 3. Screen Models

```python
class Region(BaseModel):
    id: str
    type: Literal["header", "region_a", "region_b", "region_c", "footer", "modal", "inspector"]
    role: str
    contents: Optional[str] = None

class Component(BaseModel):
    id: str
    type: Literal["menu", "list", "table", "form", "summary", "detail", "status", "actions", "progress", "text", "input", "footer_keys"]
    region: str
    purpose: str
    items: Optional[List[str]] = None
    fields: Optional[List[str]] = None

class Action(BaseModel):
    id: str
    label: str
    target: str
    kind: Literal["global", "selection_local", "workflow", "review"]

class FocusModel(BaseModel):
    default_target: str
    focus_order: List[str]

class FooterKey(BaseModel):
    key: str
    label: str
    scope: Literal["screen", "region", "global"]

class ScreenSpec(BaseArtifact):
    artifact_type: Literal["screen"] = "screen"
    workflow_id: Optional[str] = None
    archetype: Literal["dashboard", "admin", "file-manager", "editor", "fuzzy-finder", "hybrid"]
    patterns: List[str] = []
    entry_conditions: List[str] = []
    regions: List[Region]
    components: List[Component]
    actions: List[Action] = []
    focus: FocusModel
    transitions: List[dict] = [] # Shared transition logic
    footer_keys: List[FooterKey] = []
```

## Implementation Notes

- **Naming**: Use Python-standard `snake_case` for class attributes. Pydantic `Field(alias="...")` should be used to map back to the YAML `from` keyword (which is reserved in Python).
- **Validation**: Enforce `artifact_type` literals to prevent loading the wrong YAML file into a model.
- **Flexibility**: Use `Optional` and default factories where it makes sense to allow rapid wireframe drafting by agents without requiring every single field up front.
