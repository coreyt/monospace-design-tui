import pytest
from mono_designer.models.navigation import NavigationSpec, Workspace, Route
from mono_designer.models.workflow import WorkflowSpec, WorkflowStage, WorkflowTransition, Checkpoint
from mono_designer.projectors.ascii_nav import project_nav_ascii
from mono_designer.projectors.ascii_workflow import project_workflow_ascii

def test_project_nav_ascii():
    spec = NavigationSpec(
        id="nav1",
        title="Main Navigation",
        kind="navigation",
        workspaces=[
            Workspace(id="w1", label="Workspace1"),
            Workspace(id="w2", label="Workspace2")
        ],
        routes=[
            Route(id="r1", **{"from": "w1", "to": "w2", "type": "push", "trigger": "click_btn"})
        ],
        rules=["Rule 1", "Rule 2"]
    )
    output = project_nav_ascii(spec, width=80)
    lines = output.split("\n")
    
    # Check structure
    assert lines[0] == f"┌─ {spec.title} ".ljust(79, '─') + "┐"
    assert "│ [Workspace1]".ljust(79) + "│" in lines
    assert "│ [Workspace2]".ljust(79) + "│" in lines
    assert "├" + "─" * 78 + "┤" in lines
    assert "│ w1 -> click_btn -> w2".ljust(79) + "│" in lines
    assert "│ Rule 1 | Rule 2".ljust(79) + "│" in lines
    assert lines[-1] == "└" + "─" * 78 + "┘"
    for line in lines:
        assert len(line) == 80

def test_project_workflow_ascii():
    spec = WorkflowSpec(
        id="wf1",
        title="Main Workflow",
        kind="workflow",
        stages=[
            WorkflowStage(id="s1", label="Stage 1"),
            WorkflowStage(id="s2", label="Stage 2")
        ],
        transitions=[],
        checkpoints=[
            Checkpoint(id="cp1", label="CP 1", stage_id="s1")
        ],
        assumptions=[
            "Assumption A", "Assumption B"
        ]
    )
    output = project_workflow_ascii(spec)
    assert "Workflow: Main Workflow" in output
    assert "- Stage 1" in output
    assert "- Stage 2" in output
    assert "Checkpoints: CP 1 (Stage: s1)" in output
    assert "Assumptions: Assumption A | Assumption B" in output
