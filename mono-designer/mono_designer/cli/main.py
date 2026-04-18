import typer
from pathlib import Path
from ..utils.yaml_io import load_yaml
from ..core.normalization import normalize_artifact
from ..core.linter import Linter, WorkspaceContext
from ..projectors.ascii_screen import project_screen_ascii
from ..models.screen import ScreenSpec

app = typer.Typer(help="Mono Designer Toolset (0.3.0)")

@app.command()
def project(path: Path):
    """
    Project a design artifact into ASCII.
    """
    if not path.exists():
        typer.echo(f"Error: File not found: {path}", err=True)
        raise typer.Exit(1)
        
    data = load_yaml(path)
    artifact = normalize_artifact(data)
    
    if isinstance(artifact, ScreenSpec):
        output = project_screen_ascii(artifact)
        typer.echo(output)
    else:
        typer.echo(f"Projection for {artifact.artifact_type} not yet implemented.", err=True)

@app.command()
def lint(
    path: Path = typer.Argument(..., help="Path to the directory containing design artifacts"),
    schema_path: Path = typer.Option(None, help="Path to the JSON schema file for level 1 validation")
):
    """
    Lint design artifacts in a given directory.
    """
    if not path.exists() or not path.is_dir():
        typer.echo(f"Error: Directory not found: {path}", err=True)
        raise typer.Exit(1)
        
    if not schema_path:
        # Default fallback relative to repo root assuming running from source
        root_dir = Path(__file__).parent.parent.parent.parent
        schema_path = root_dir / "dev" / "designer" / "mono-dsl.schema.json"
        
    if not schema_path.exists():
        typer.echo(f"Warning: JSON schema not found at {schema_path}. Level 1 validation will be skipped.", err=True)

    ctx = WorkspaceContext(path)
    linter = Linter(schema_path=schema_path)
    
    results = linter.lint_workspace(ctx)
    
    if not results:
        typer.secho("Success: No linting issues found.", fg=typer.colors.GREEN)
        return
        
    error_count = 0
    warning_count = 0
    for r in results:
        if r.level == 'error':
            error_count += 1
            typer.secho(f"[ERROR] {r.code}: {r.message} ({r.file_path})", fg=typer.colors.RED)
        else:
            warning_count += 1
            typer.secho(f"[WARNING] {r.code}: {r.message} ({r.file_path})", fg=typer.colors.YELLOW)
            
    typer.echo(f"\nFound {error_count} error(s) and {warning_count} warning(s).")
    if error_count > 0:
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
