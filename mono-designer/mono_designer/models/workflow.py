from typing import List, Literal, Optional
from pydantic import Field, model_validator
from .base import BaseArtifact, BaseModel

class WorkflowStage(BaseModel):
    id: str
    label: str
    purpose: Optional[str] = None
    screen_ids: List[str] = []

class WorkflowTransition(BaseModel):
    id: Optional[str] = None
    from_stage: Optional[str] = Field(None, alias="from")
    to_stage: str = Field(alias="target") 
    trigger: str
    kind: Literal["advance", "return", "modal", "jump", "push", "pop"] = Field("push", alias="type") 

    @model_validator(mode='before')
    @classmethod
    def handle_to_target_alias(cls, data: dict) -> dict:
        # Support older 'to' field alongside newer 'target' field
        if "to" in data and "target" not in data:
            data["target"] = data.pop("to")
        return data

    class Config:
        populate_by_name = True

class Checkpoint(BaseModel):
    id: str
    label: str
    type: Optional[Literal["approve", "revise", "continue", "cancel", "collect_more", "publish"]] = None
    stage_id: str

class WorkflowSpec(BaseArtifact):
    artifact_type: Literal["workflow"] = "workflow"
    purpose: Optional[str] = None
    entry_conditions: List[str] = []
    exit_conditions: List[str] = []
    stages: List[WorkflowStage] = []
    transitions: List[WorkflowTransition] = []
    checkpoints: List[Checkpoint] = []
    assumptions: List[str] = []
    linked_screens: List[str] = []
