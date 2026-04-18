import os
import json
import tempfile
import unittest
from pathlib import Path

from mono_designer.core.linter import Linter, WorkspaceContext

class TestLinter(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.workspace_path = Path(self.temp_dir.name)
        
        # We need a dummy schema for testing, or we can use the real one if it exists,
        # but let's provide a mock schema or just use the real one if we can point to it.
        # Actually, let's create a minimal schema in the temp dir
        self.schema_path = self.workspace_path / "mono-dsl.schema.json"
        minimal_schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "properties": {
                "kind": {"type": "string"},
                "id": {"type": "string"}
            },
            "required": ["kind", "id"]
        }
        with open(self.schema_path, "w") as f:
            json.dump(minimal_schema, f)

    def tearDown(self):
        self.temp_dir.cleanup()

    def create_yaml(self, name, content):
        path = self.workspace_path / name
        with open(path, "w") as f:
            f.write(content)
        return path

    def test_level1_schema_validation_success(self):
        self.create_yaml("valid.yaml", "kind: screen\nid: screen-1\n")
        
        linter = Linter(schema_path=self.schema_path)
        ctx = WorkspaceContext(self.workspace_path)
        
        results = linter.lint_workspace(ctx)
        self.assertEqual(len(results), 0, f"Expected 0 errors, got {results}")

    def test_level1_schema_validation_failure(self):
        self.create_yaml("invalid.yaml", "kind: screen\n") # missing 'id'
        
        linter = Linter(schema_path=self.schema_path)
        ctx = WorkspaceContext(self.workspace_path)
        
        results = linter.lint_workspace(ctx)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].code, "E001")
        self.assertIn("required property", results[0].message)

    def test_level2_w001_check_workflow_exists(self):
        # A screen specifies a workflow_id that doesn't exist
        self.create_yaml("screen1.yaml", "kind: screen\nid: screen-1\nworkflow_id: wf-missing\n")
        
        linter = Linter(schema_path=self.schema_path)
        ctx = WorkspaceContext(self.workspace_path)
        
        results = linter.lint_workspace(ctx)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].code, "W001")
        self.assertIn("Workflow 'wf-missing' not found", results[0].message)

        # Now add the workflow, error should go away
        self.create_yaml("wf1.yaml", "kind: workflow\nid: wf-missing\n")
        ctx = WorkspaceContext(self.workspace_path)
        results = linter.lint_workspace(ctx)
        self.assertEqual(len(results), 0)

    def test_level2_w002_check_screen_in_workflow(self):
        # A workflow lists screen_ids that don't exist
        self.create_yaml("wf1.yaml", """kind: workflow
id: wf-1
stages:
  - id: stage1
    screen_ids: [screen-missing]
""")
        linter = Linter(schema_path=self.schema_path)
        ctx = WorkspaceContext(self.workspace_path)
        
        results = linter.lint_workspace(ctx)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].code, "W002")
        self.assertIn("Screen 'screen-missing' not found", results[0].message)

        # Add the screen
        self.create_yaml("screen1.yaml", "kind: screen\nid: screen-missing\n")
        ctx = WorkspaceContext(self.workspace_path)
        results = linter.lint_workspace(ctx)
        self.assertEqual(len(results), 0)

    def test_level3_h001_require_footer_keys(self):
        self.create_yaml("screen1.yaml", """kind: screen
id: s1
actions:
  - id: act1
    label: action 1
    target: a
    kind: global
""") # missing footer_keys
        linter = Linter(schema_path=self.schema_path)
        ctx = WorkspaceContext(self.workspace_path)
        results = linter.lint_workspace(ctx)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].code, "H001")
        self.assertIn("has actions but missing footer_keys", results[0].message)

        # with footer keys it should be fine
        self.create_yaml("screen1.yaml", """kind: screen
id: s1
actions:
  - id: act1
    label: action 1
    target: a
    kind: global
footer_keys:
  bindings:
    - key: Enter
      label: submit
      scope: form
""")
        ctx = WorkspaceContext(self.workspace_path)
        results = linter.lint_workspace(ctx)
        self.assertEqual(len(results), 0)

    def test_level3_h002_interactive_focus(self):
        self.create_yaml("screen1.yaml", """kind: screen
id: s1
components:
  - id: comp1
    type: input
focus:
  focus_order: [comp2]
""") # comp1 is not in focus_order
        linter = Linter(schema_path=self.schema_path)
        ctx = WorkspaceContext(self.workspace_path)
        results = linter.lint_workspace(ctx)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].code, "H002")
        self.assertIn("Interactive component 'comp1' must be in focus_order", results[0].message)

        # No focus_order block at all
        self.create_yaml("screen1.yaml", """kind: screen
id: s1
components:
  - id: comp1
    type: form
""")
        ctx = WorkspaceContext(self.workspace_path)
        results = linter.lint_workspace(ctx)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].code, "H002")
        self.assertIn("Interactive component 'comp1' found but no focus_order defined", results[0].message)

    def test_suppression(self):
        # A file that would trigger H001, but is suppressed
        self.create_yaml("screen1.yaml", """kind: screen
id: s1
notes: "Something mono-lint-disable: H001"
actions:
  - id: act1
    label: action 1
    target: a
    kind: global
""")
        linter = Linter(schema_path=self.schema_path)
        ctx = WorkspaceContext(self.workspace_path)
        results = linter.lint_workspace(ctx)
        self.assertEqual(len(results), 0)

if __name__ == '__main__':
    unittest.main()
