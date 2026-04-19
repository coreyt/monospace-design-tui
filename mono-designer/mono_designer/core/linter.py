import os
import re
from pathlib import Path
from typing import List, Dict, Any, Optional
import yaml
import json
import jsonschema

class LintResult:
    def __init__(self, file_path: Path, code: str, message: str, level: str):
        self.file_path = file_path
        self.code = code
        self.message = message
        self.level = level

    def __repr__(self):
        return f"[{self.level}] {self.code}: {self.message} ({self.file_path})"

class WorkspaceContext:
    def __init__(self, directory: Path):
        self.directory = Path(directory)
        self.artifacts: Dict[Path, Dict[str, Any]] = {}
        self.workflows: Dict[str, Path] = {}
        self.screens: Dict[str, Path] = {}
        self.project_suppressions = set()
        self._load_workspace()
        self._load_project_overrides()

    def _load_project_overrides(self):
        tui_design_path = self.directory / "TUI-DESIGN.md"
        if tui_design_path.exists():
            try:
                text = tui_design_path.read_text(encoding="utf-8")
                # Look for patterns like [WAIVE] H001
                matches = re.findall(r'\[WAIVE\]\s+([A-Z][0-9]{3})', text)
                for match in matches:
                    self.project_suppressions.add(match)
            except Exception:
                pass

    def _load_workspace(self):
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.endswith(('.yaml', '.yml')):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = yaml.safe_load(f)
                            if content and isinstance(content, dict):
                                self.artifacts[file_path] = content
                                artifact_id = content.get('id')
                                kind = content.get('kind') or content.get('artifact_type')
                                
                                if artifact_id:
                                    if kind == 'workflow':
                                        self.workflows[artifact_id] = file_path
                                    elif kind == 'screen':
                                        self.screens[artifact_id] = file_path
                    except Exception as e:
                        pass # Ignore parsing errors for now, or handle appropriately


class Linter:
    def __init__(self, schema_path: Optional[Path] = None):
        self.schema = None
        if schema_path and schema_path.exists():
            try:
                with open(schema_path, 'r', encoding='utf-8') as f:
                    self.schema = json.load(f)
            except Exception:
                pass

    def _is_suppressed(self, artifact: Dict[str, Any], code: str, context: WorkspaceContext = None) -> bool:
        if context and code in context.project_suppressions:
            return True
        notes = artifact.get("notes", "")
        if isinstance(notes, str) and f"mono-lint-disable: {code}" in notes:
            return True
        if isinstance(notes, list):
            for note in notes:
                if isinstance(note, str) and f"mono-lint-disable: {code}" in note:
                    return True
        return False

    def lint_workspace(self, context: WorkspaceContext) -> List[LintResult]:
        results: List[LintResult] = []

        for file_path, artifact in context.artifacts.items():
            # Level 1: Schema Validation
            if self.schema:
                try:
                    jsonschema.validate(instance=artifact, schema=self.schema)
                except jsonschema.exceptions.ValidationError as e:
                    if not self._is_suppressed(artifact, "E001", context):
                        results.append(LintResult(
                            file_path=file_path,
                            code="E001",
                            message=f"Schema validation error: {e.message}",
                            level="error"
                        ))

            kind = artifact.get('kind') or artifact.get('artifact_type')

            if kind == 'screen':
                # W001: CheckWorkflowExists
                workflow_id = artifact.get('workflow_id')
                if workflow_id and workflow_id not in context.workflows:
                    if not self._is_suppressed(artifact, "W001", context):
                        results.append(LintResult(
                            file_path=file_path,
                            code="W001",
                            message=f"Workflow '{workflow_id}' not found in workspace",
                            level="warning"
                        ))

                # H001: RequireFooterKeys
                actions = artifact.get('actions', [])
                footer_keys = artifact.get('footer_keys')
                if actions and not footer_keys:
                    if not self._is_suppressed(artifact, "H001", context):
                        results.append(LintResult(
                            file_path=file_path,
                            code="H001",
                            message="Screen has actions but missing footer_keys",
                            level="warning"
                        ))

                # H002: InteractiveFocus
                components = artifact.get('components', [])
                focus = artifact.get('focus', {})
                focus_order = focus.get('focus_order', []) if isinstance(focus, dict) else []
                
                interactive_types = {'input', 'list', 'menu', 'form'}
                for comp in components:
                    if isinstance(comp, dict) and comp.get('type') in interactive_types:
                        comp_id = comp.get('id')
                        if not focus_order and not self._is_suppressed(artifact, "H002", context):
                             results.append(LintResult(
                                file_path=file_path,
                                code="H002",
                                message=f"Interactive component '{comp_id}' found but no focus_order defined",
                                level="warning"
                            ))
                        elif comp_id not in focus_order and not self._is_suppressed(artifact, "H002", context):
                             results.append(LintResult(
                                file_path=file_path,
                                code="H002",
                                message=f"Interactive component '{comp_id}' must be in focus_order",
                                level="warning"
                            ))

            elif kind == 'workflow':
                # W002: CheckScreenInWorkflow
                stages = artifact.get('stages', [])
                for stage in stages:
                    if isinstance(stage, dict):
                        screen_ids = stage.get('screen_ids', [])
                        for s_id in screen_ids:
                            if s_id not in context.screens:
                                if not self._is_suppressed(artifact, "W002", context):
                                    results.append(LintResult(
                                        file_path=file_path,
                                        code="W002",
                                        message=f"Screen '{s_id}' not found in workspace",
                                        level="warning"
                                    ))

        return results
