from mono_designer.models.screen import ScreenSpec, FocusModel, Region, Component, FooterKey
from mono_designer.models.base import ArtifactSource

def test_screen_spec_instantiation():
    data = {
        "id": "dashboard-system-monitor",
        "title": "System Monitor",
        "purpose": "Monitor key service and resource status",
        "artifact_type": "screen",
        "source": {
            "kind": "generated",
            "inputs": []
        },
        "status": "draft",
        "archetype": "dashboard",
        "regions": [
            {"id": "header", "type": "header", "role": "metrics"},
            {"id": "region_b", "type": "region_b", "role": "primary-data"},
            {"id": "footer", "type": "footer", "role": "commands"}
        ],
        "components": [
            {"id": "metric-cards", "type": "summary", "region": "header", "purpose": "key metrics"},
            {"id": "service-table", "type": "table", "region": "region_b", "purpose": "service status list"}
        ],
        "focus": {
            "default_target": "service-table",
            "focus_order": ["service-table"]
        },
        "footer_keys": [
            {"key": "?", "label": "Help", "scope": "screen"},
            {"key": "q", "label": "Quit", "scope": "screen"}
        ]
    }
    
    try:
        spec = ScreenSpec(**data)
        print(f"Successfully instantiated ScreenSpec: {spec.id}")
        print(f"Title: {spec.title}")
        print(f"Regions count: {len(spec.regions)}")
    except Exception as e:
        print(f"Failed to instantiate ScreenSpec: {e}")
        exit(1)

if __name__ == "__main__":
    test_screen_spec_instantiation()
