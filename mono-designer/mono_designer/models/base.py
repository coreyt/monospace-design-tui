from datetime import datetime
from typing import List, Literal, Optional
from pydantic import BaseModel, Field, model_validator


class ArtifactSource(BaseModel):
    kind: Literal["generated", "manual", "imported"] = "manual"
    inputs: List[str] = []


class BaseArtifact(BaseModel):
    version: str = "0.3.0"
    artifact_type: str = Field(alias="kind")
    id: str
    title: str
    purpose: Optional[str] = None
    source: ArtifactSource = Field(default_factory=ArtifactSource)
    status: Literal["draft", "reviewed", "approved"] = "draft"
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    notes: List[str] = []

    @model_validator(mode="before")
    @classmethod
    def handle_kind_alias(cls, data: dict) -> dict:
        if "kind" in data and "artifact_type" not in data:
            data["artifact_type"] = data.pop("kind")
        return data

    class Config:
        populate_by_name = True
