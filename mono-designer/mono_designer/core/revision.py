import jsonpatch
from pathlib import Path
from typing import Any, Dict, List
from ..utils.yaml_io import load_yaml, save_yaml
from .normalization import normalize_artifact
from ..models.base import BaseArtifact

def apply_revision(file_path: Path, patch: List[Dict[str, Any]]) -> BaseArtifact:
    """
    Applies a JSON Patch (RFC 6902) array to a YAML file, validates it, and saves it.
    """
    data = load_yaml(file_path)
    if not data:
        raise ValueError(f"Could not load data from {file_path}")
        
    try:
        new_data = jsonpatch.apply_patch(data, patch)
    except jsonpatch.JsonPatchException as e:
        raise ValueError(f"Failed to apply JSON patch: {e}")
        
    # Validate against schemas via normalize
    artifact = normalize_artifact(new_data)
    
    # Save if valid
    save_yaml(new_data, file_path)
    
    return artifact
