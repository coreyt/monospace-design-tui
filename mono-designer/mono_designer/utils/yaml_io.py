import yaml
from pathlib import Path
from typing import Any, Dict

def load_yaml(path: Path) -> Dict[str, Any]:
    """Loads a YAML file into a dictionary."""
    with open(path, "r") as f:
        return yaml.safe_load(f)

def save_yaml(data: Dict[str, Any], path: Path):
    """Saves a dictionary to a YAML file."""
    with open(path, "w") as f:
        yaml.safe_dump(data, f, sort_keys=False)

def load_artifact_data(content: str) -> Dict[str, Any]:
    """Loads YAML data from a string."""
    return yaml.safe_load(content)
