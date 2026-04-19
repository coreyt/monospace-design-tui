from typing import List, Literal, Optional, Dict, Any, Union
from .base import BaseArtifact, BaseModel


class Region(BaseModel):
    id: str
    type: Literal[
        "header", "region_a", "region_b", "region_c", "footer", "modal", "inspector"
    ]
    role: str
    contents: Optional[Union[str, List[str]]] = None


class Component(BaseModel):
    id: str
    type: Literal[
        "menu",
        "list",
        "table",
        "form",
        "summary",
        "detail",
        "status",
        "actions",
        "progress",
        "text",
        "input",
        "footer_keys",
    ]
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
    scope: (
        str  # Kept broad (e.g., 'screen', 'form', 'list', 'finder') as seen in examples
    )


class ScreenSpec(BaseArtifact):
    artifact_type: Literal["screen"] = "screen"
    purpose: Optional[str] = None
    workflow_id: Optional[str] = None
    archetype: Literal[
        "dashboard", "admin", "file-manager", "editor", "fuzzy-finder", "hybrid"
    ]
    patterns: List[str] = []
    entry_conditions: List[str] = []
    regions: List[Region] = []
    components: List[Component] = []
    actions: List[Action] = []
    focus: Optional[FocusModel] = None  # Some examples omit focus block
    transitions: List[Dict[str, Any]] = []  # Generic transitions for screens
    footer_keys: List[FooterKey] = []
