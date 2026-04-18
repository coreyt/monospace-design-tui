# Mono Designer E2E Test Harness Requirements

## Purpose

The E2E Test Harness verifies the fidelity of the ASCII projection engine. It ensures that the human-readable output (ASCII) accurately reflects the canonical machine-readable input (YAML) and that no semantic information is lost or misplaced during projection.

## 1. Input Specifications

The harness must accept:
- **Canonical YAML**: Navigation, Workflow, or Screen specs.
- **Generated ASCII**: The output produced by the `mono-designer project` command.

## 2. ASCII Parsing & Identification

The harness must be able to "read" the ASCII output and extract its semantic structure:

- **Component Identification**: Locate components (e.g., tables, lists, summary cards) within the ASCII based on labels, bullets, or region markers.
- **Region Detection**: Identify the boundaries and roles of regions (Header, Region A/B/C, Footer) by parsing box-drawing characters and region labels.
- **Annotation/Note Extraction**: Identify and parse metadata included in the ASCII (e.g., "ACTIONS: ...", "[?] Help").
- **State/Focus Markers**: Detect markers like `[focused]` or `> selected` if present in the projection.

## 3. Verification Logic

The harness must compare the parsed ASCII structure against the source YAML DSL:

- **Existence Check**: Verify that every component defined in the YAML appears in the ASCII within its designated region.
- **Label Accuracy**: Verify that labels, IDs, and purposes in the ASCII match the YAML spec.
- **Positional Consistency**: Ensure regions appear in the correct order (Header at top, Footer at bottom).
- **Metadata Coverage**: Verify that all actions and footer keys defined in the YAML are visible in the ASCII output.

## 4. Test Reporting

- **Match Report**: A summary of which elements matched perfectly.
- **Mismatch Log**: Explicit details on what failed (e.g., "Component 'service-table' was expected in REGION_B but found in REGION_A").
- **Completeness Score**: A metric indicating what percentage of the YAML semantics were successfully projected to ASCII.

## 5. Usage Scenarios

- **Regression Testing**: Automatically run against the `dev/designer/examples/` to ensure projector updates don't break existing wireframe styles.
- **Validation of Manual Edits**: (Future) Verify if a manually tweaked ASCII file still aligns with its source spec.

## 6. Success Criteria

- The harness can identify a missing action in an ASCII footer.
- The harness correctly maps ASCII text back to specific YAML `Component` IDs.
- The harness fails if a region label in the ASCII doesn't match the YAML `role`.
