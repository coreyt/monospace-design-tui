import re

with open('/home/coreyt/projects/monospace-design-tui/mono-designer/mono_designer/cli/main.py', 'r') as f:
    content = f.read()

import_statement = "import json\nfrom ..core.revision import apply_revision\n"
content = import_statement + content

cmd = """
@app.command()
def revise(path: Path, patch_json: str):
    \"\"\"
    Applies a JSON patch to a YAML artifact, validates it, and saves it.
    \"\"\"
    if not path.exists():
        typer.echo(f"Error: File not found: {path}", err=True)
        raise typer.Exit(1)
        
    try:
        updates = json.loads(patch_json)
    except json.JSONDecodeError as e:
        typer.echo(f"Error parsing patch_json: {e}", err=True)
        raise typer.Exit(1)
        
    try:
        artifact = apply_revision(path, updates)
        typer.echo(f"Successfully revised {artifact.artifact_type} '{artifact.id}' at {path}")
    except Exception as e:
        typer.echo(f"Error applying revision: {e}", err=True)
        raise typer.Exit(1)

"""

content += cmd

with open('/home/coreyt/projects/monospace-design-tui/mono-designer/mono_designer/cli/main.py', 'w') as f:
    f.write(content)
