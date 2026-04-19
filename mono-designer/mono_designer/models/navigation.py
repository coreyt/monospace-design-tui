from typing import List, Literal, Optional
from pydantic import ConfigDict, Field
from .base import BaseArtifact, BaseModel


class Workspace(BaseModel):
    id: str
    label: str
    purpose: Optional[str] = None


class Route(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: Optional[str] = None
    from_workspace: str = Field(alias="from")
    to_workspace: str = Field(alias="to")
    kind: Literal["push", "pop", "modal", "jump", "switch"] = Field(alias="type")
    trigger: Optional[str] = None
    notes: Optional[str] = None


class NavigationSpec(BaseArtifact):
    artifact_type: Literal["navigation"] = "navigation"
    purpose: Optional[str] = None
    workspaces: List[Workspace] = []
    routes: List[Route] = []
    rules: List[str] = []
