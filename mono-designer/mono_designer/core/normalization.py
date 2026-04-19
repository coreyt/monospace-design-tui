from typing import Any, Dict, Union
from ..models.navigation import NavigationSpec
from ..models.workflow import WorkflowSpec
from ..models.screen import ScreenSpec

ArtifactType = Union[NavigationSpec, WorkflowSpec, ScreenSpec]


def normalize_artifact(data: Dict[str, Any]) -> ArtifactType:
    """
    Normalizes raw dictionary data into a validated Mono Designer model.
    Dispatches based on 'artifact_type' or 'kind'.
    """
    artifact_type = data.get("artifact_type") or data.get("kind")

    # Inject default metadata if missing for 0.3.0 examples
    if "source" not in data:
        data["source"] = {"kind": "manual", "inputs": []}
    if "status" not in data:
        data["status"] = "draft"
    if "version" not in data:
        data["version"] = "0.3.0"

    if artifact_type == "navigation":
        return NavigationSpec(**data)
    elif artifact_type == "workflow":
        return WorkflowSpec(**data)
    elif artifact_type == "screen":
        # Handle footer_keys mapping if it's in the old 'bindings' format
        if (
            "footer_keys" in data
            and isinstance(data["footer_keys"], dict)
            and "bindings" in data["footer_keys"]
        ):
            data["footer_keys"] = data["footer_keys"]["bindings"]

        if "archetype" not in data:
            data["archetype"] = "hybrid"

        return ScreenSpec(**data)
    else:
        raise ValueError(f"Unknown or missing artifact_type/kind: {artifact_type}")
