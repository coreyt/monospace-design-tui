---
title: "Workflow Generation"
weight: 10
---

# Workflow Generation

Before drawing a single terminal UI box, the Monospace Designer forces you to map the **task flow** into a screen flow. This is the **Workflow Generation** phase.

A Workflow is a canonical `yaml` document defining the stages, transitions, and checkpoints of a user task.

## The Workflow Specification

A complete `WorkflowSpec` dictates exactly *why* a user enters a process and *how* they leave it. The `id` is crucial for linking screens back to the workflow.

```yaml
kind: workflow
id: wf-alert-triage
title: Alert Triage
purpose: Monitor active alerts and respond to anomalies
entry_conditions: [dashboard active]
exit_conditions: [alert acknowledged or remediated]
```

### Stages

A workflow is divided into logical **stages**. A stage maps roughly to a major task phase and is almost always fulfilled by a single `ScreenSpec`.

```yaml
stages:
  - id: dashboard
    label: Live Dashboard
  - id: detail
    label: Alert Detail
  - id: action
    label: Action Dialog
```

### Transitions

Transitions define how a user navigates between the stages. The vocabulary is explicitly TUI-native:

- **`push`**: Drill-down navigation. A new screen is stacked over the current context. Requires an `Esc` binding to pop the stack.
- **`pop`**: Returning to the previous context.
- **`modal`**: Transient overlay. Used for critical interruptions or confirmations (Level 4 Elevation).
- **`jump`**: Context-switching navigation (e.g., from an editor to a search results pane).

```yaml
transitions:
  - id: tr-01
    type: push
    trigger: inspect
    target: detail
  - id: tr-02
    type: modal
    trigger: act
    target: action
```

### Human-In-The-Loop (HITL) Checkpoints

For complex agent-assisted workflows, explicit checkpoints are necessary. Checkpoints define moments where the system halts and waits for explicit user intervention.

```yaml
checkpoints:
  - id: cp-01
    label: approve remediation
    stage_id: action
```

Valid checkpoint types include: `approve`, `revise`, `continue`, `cancel`, `collect_more`, and `publish`.

## ASCII Projection

The Mono Designer tools will automatically project your `WorkflowSpec` into an ASCII outline for review. This prevents you from getting bogged down in pixels while evaluating the logic of the application.

```text
Workflow: Alert Triage

- Live Dashboard
- Alert Detail
- Action Dialog

Checkpoints: approve remediation (Stage: action)
```

## Next Steps

Once the workflow logic is approved, every `stage_id` must be mapped to a corresponding `ScreenSpec`. See the [Wireframe Guide](../wireframe-guide) for details on generating screens.