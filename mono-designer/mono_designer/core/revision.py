from pathlib import Path
from typing import Dict, Any
from copy import deepcopy

from mono_designer.utils.yaml_io import load_yaml, save_yaml
from mono_designer.core.normalization import normalize_artifact

def deep_merge(target: Dict[str, Any], source: Dict[str, Any]) -> Dict[str, Any]:
    """
    Deep merges source dict into target dict.
    If a key in source is a dict, merge it; if it's a list or scalar, overwrite it.
    Returns the merged dictionary.
    """
    result = deepcopy(target)
    for key, value in source.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = deepcopy(value)
    return result

def apply_revision(file_path: Path, updates: Dict[str, Any]):
    """
    Loads YAML from file_path, applies deep merge of updates, validates via normalize_artifact,
    saves the result to the file, and returns the normalized artifact.
    """
    # 1. Load the YAML from file_path
    data = load_yaml(file_path)
    
    # 2. Perform a deep merge
    merged_data = deep_merge(data, updates)
    
    # 3. Call normalize_artifact to validate against Pydantic schema
    # If it fails, an exception will be raised, so it won't be saved
    artifact = normalize_artifact(merged_data)
    
    # 4. If valid, save merged dict back to the YAML file
    save_yaml(merged_data, file_path)
    
    return artifact
