import pytest
import json
from pathlib import Path
from mono_designer.core.revision import apply_revision
from mono_designer.utils.yaml_io import save_yaml, load_yaml
from mono_designer.core.normalization import normalize_artifact
import pydantic

@pytest.fixture
def sample_yaml(tmp_path):
    file_path = tmp_path / "sample.yaml"
    data = {
        "artifact_type": "screen",
        "id": "test_screen_id",
        "title": "Test Screen",
        "name": "test_screen",
        "description": "A test screen",
        "archetype": "dashboard",
        "footer_keys": [
            {"key": "q", "label": "Quit", "action": "quit", "scope": "global"}
        ]
    }
    save_yaml(data, file_path)
    return file_path

def test_apply_revision_valid_update(sample_yaml):
    updates = {
        "title": "Updated Screen",
        "archetype": "admin"
    }
    
    result = apply_revision(sample_yaml, updates)
    
    # Assert return value is a valid artifact (ScreenSpec in this case)
    assert result.title == "Updated Screen"
    assert result.archetype == "admin"
    
    # Assert file is updated
    loaded_data = load_yaml(sample_yaml)
    assert loaded_data["title"] == "Updated Screen"
    assert loaded_data["archetype"] == "admin"

def test_apply_revision_invalid_update(sample_yaml):
    updates = {
        "title": "Updated Screen",
        "archetype": "invalid_archetype" # This will fail validation
    }
    
    with pytest.raises(Exception):
        apply_revision(sample_yaml, updates)
        
    # Assert file is NOT updated
    loaded_data = load_yaml(sample_yaml)
    assert loaded_data["title"] == "Test Screen"
    assert loaded_data["archetype"] == "dashboard"

def test_apply_revision_returns_base_artifact(sample_yaml):
    from mono_designer.models.base import BaseArtifact
    updates = {"title": "Updated"}
    result = apply_revision(sample_yaml, updates)
    assert isinstance(result, BaseArtifact)

from typer.testing import CliRunner
from mono_designer.cli.main import app

runner = CliRunner()

def test_cli_revise_valid(sample_yaml):
    patch = {"title": "CLI Updated Screen", "archetype": "admin"}
    patch_json = json.dumps(patch)
    
    result = runner.invoke(app, ["revise", str(sample_yaml), patch_json])
    
    assert result.exit_code == 0
    assert "Successfully revised screen" in result.stdout
    
    loaded_data = load_yaml(sample_yaml)
    assert loaded_data["title"] == "CLI Updated Screen"
    assert loaded_data["archetype"] == "admin"

def test_cli_revise_invalid_json(sample_yaml):
    result = runner.invoke(app, ["revise", str(sample_yaml), "{invalid_json}"])
    
    assert result.exit_code == 1
    assert "Error parsing patch_json" in result.stdout

def test_cli_revise_invalid_patch(sample_yaml):
    patch = {"archetype": "invalid_archetype"}
    patch_json = json.dumps(patch)
    
    result = runner.invoke(app, ["revise", str(sample_yaml), patch_json])
    
    assert result.exit_code == 1
    assert "Error applying revision" in result.stdout
    
    loaded_data = load_yaml(sample_yaml)
    assert loaded_data["archetype"] == "dashboard" # Unchanged
