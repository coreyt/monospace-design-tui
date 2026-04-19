from ..models.workflow import WorkflowSpec


def project_workflow_ascii(spec: WorkflowSpec) -> str:
    lines = []
    lines.append(f"Workflow: {spec.title}")
    lines.append("")

    for stage in spec.stages:
        lines.append(f"- {stage.label}")

    lines.append("")

    cp_strs = []
    for cp in spec.checkpoints:
        cp_strs.append(f"{cp.label} (Stage: {cp.stage_id})")

    if cp_strs:
        lines.append(f"Checkpoints: {' | '.join(cp_strs)}")

    if spec.assumptions:
        lines.append(f"Assumptions: {' | '.join(spec.assumptions)}")

    return "\n".join(lines)
