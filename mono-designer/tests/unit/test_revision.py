import json
from pathlib import Path
from mono_designer.core.revision import apply_revision
from mono_designer.utils.yaml_io import save_yaml, load_yaml

def test_apply_revision(tmp_path):
    # Setup initial valid YAML
    yaml_path = tmp_path / "test_artifact.yaml"
    initial_data = {
        "version": "0.3.0",
        "artifact_type": "screen",
        "id": "scr-test",
        "title": "Test Screen",
        "archetype": "dashboard",
        "source": {"kind": "manual", "inputs": []},
        "regions": [],
        "components": [{"id": "c1", "type": "text", "region": "region_a", "purpose": "none"}],
        "focus": {"default_target": "none", "focus_order": []},
        "actions": []
    }
    save_yaml(initial_data, yaml_path)
    
    # Define a JSON patch array (RFC 6902)
    patch = [
        {"op": "replace", "path": "/title", "value": "Updated Title"},
        {"op": "remove", "path": "/components/0"}
    ]
    
    artifact = apply_revision(yaml_path, patch)
    assert artifact.title == "Updated Title"
    
    loaded_data = load_yaml(yaml_path)
    assert loaded_data["title"] == "Updated Title"
    assert len(loaded_data["components"]) == 0

def test_apply_revision_invalid_schema(tmp_path):
    yaml_path = tmp_path / "test_artifact.yaml"
    initial_data = {
        "version": "0.3.0",
        "artifact_type": "screen",
        "id": "scr-test",
        "title": "Test Screen",
        "archetype": "dashboard",
        "source": {"kind": "manual", "inputs": []},
        "regions": [],
        "components": [],
        "focus": {"default_target": "none", "focus_order": []},
        "actions": []
    }
    save_yaml(initial_data, yaml_path)
    
    # Try to set an invalid archetype
    patch = [
        {"op": "replace", "path": "/archetype", "value": "invalid-archetype"}
    ]
    
    import pytest
    with pytest.raises(Exception):
        apply_revision(yaml_path, patch)
