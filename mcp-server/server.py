import os
import json
import subprocess
from pathlib import Path
from pydantic import BaseModel, Field
from mcp.server.fastmcp import FastMCP

# Initialize the MCP Server
mcp = FastMCP("mono-designer")

# The workspace root is the directory where the user runs the server.
WORKSPACE_ROOT = Path.cwd()

def _run_cli(command: list[str]) -> tuple[bool, str]:
    """Helper to run the mono-designer CLI."""
    try:
        # Assuming mono-designer is installed in the environment
        result = subprocess.run(
            ["python3", "-m", "mono_designer.cli.main"] + command,
            capture_output=True,
            text=True,
            check=True
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr or e.stdout

# --- 1. design_generate ---

class GenerateInput(BaseModel):
    file_path: str = Field(..., description="Relative path (e.g., 'dev/designer/screens/scr-01.yaml') to save the artifact.")
    yaml_content: str = Field(..., description="The raw YAML content of the Navigation, Workflow, or Screen spec.")

@mcp.tool()
def design_generate(input: GenerateInput) -> str:
    """
    Creates or overwrites a Mono Designer YAML artifact.
    It immediately lints the file (Level 1 Schema check) and projects it into ASCII.
    Returns the ASCII wireframe and any lint warnings for HITL review.
    """
    full_path = WORKSPACE_ROOT / input.file_path
    
    # Ensure directory exists
    full_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write the YAML
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(input.yaml_content)
        
    # Project it to ASCII
    success, output = _run_cli(["project", str(full_path)])
    
    if not success:
        return f"❌ Validation Failed. Please fix your YAML:\n\n{output}"
        
    # The output is the valid ASCII projection
    return f"✅ Artifact saved successfully.\n\nASCII Projection:\n```text\n{output}\n```"

# --- 2. design_revise ---

class ReviseInput(BaseModel):
    file_path: str = Field(..., description="Relative path of the existing artifact to revise.")
    json_patch: str = Field(..., description="A JSON string representing the dictionary updates to deep-merge into the YAML.")

@mcp.tool()
def design_revise(input: ReviseInput) -> str:
    """
    Safely updates an existing Mono Designer artifact using a JSON deep-merge patch.
    Validates the merged result against the strict schema before saving.
    Returns the updated ASCII projection.
    """
    full_path = WORKSPACE_ROOT / input.file_path
    
    if not full_path.exists():
        return f"❌ Error: File not found at {input.file_path}"
        
    # Ensure the patch is valid JSON
    try:
        json.loads(input.json_patch)
    except json.JSONDecodeError as e:
         return f"❌ Error: json_patch is not valid JSON string: {e}"

    # Run the revise CLI command
    success, output = _run_cli(["revise", str(full_path), input.json_patch])
    
    if not success:
         return f"❌ Revision Failed. The patch resulted in an invalid schema:\n\n{output}"
         
    # If revision succeeds, project the updated file
    proj_success, proj_output = _run_cli(["project", str(full_path)])
    
    return f"✅ Artifact revised successfully.\n\nUpdated ASCII Projection:\n```text\n{proj_output}\n```"

# --- 3. design_lint ---

class LintInput(BaseModel):
    directory: str = Field(..., description="Relative directory path to lint (e.g., 'dev/designer/').")

@mcp.tool()
def design_lint(input: LintInput) -> str:
    """
    Runs the Level 2 (Relational) and Level 3 (Heuristic) Mono Linter against a directory.
    Use this to verify cross-artifact integrity (e.g., workflow_id links, screen_ids arrays).
    """
    full_path = WORKSPACE_ROOT / input.directory
    
    if not full_path.exists() or not full_path.is_dir():
         return f"❌ Error: Directory not found at {input.directory}"
         
    success, output = _run_cli(["lint", str(full_path)])
    
    if success:
        return f"✅ Linting Passed:\n\n{output}"
    else:
        return f"⚠️ Linting Issues Found:\n\n{output}"

if __name__ == "__main__":
    # Start the standard stdio server for MCP
    mcp.run()
