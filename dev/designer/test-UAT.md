# Monospace Designer 0.3.0 - User Acceptance Testing (UAT) Guide

This guide explains how to test the entire `0.3.0` Designer ecosystem on your local machine. By following these steps, you will connect an AI agent (like Claude Code or Gemini CLI) to the local Monospace Designer MCP server, load the specialized `mono-tui-design` skill, and generate canonical TUI design artifacts.

## 1. Running the MCP Server Locally

The `mcp-server` provides the agent with access to the Monospace design rules, patterns, and the generation tools (e.g., `design_generate`, `design_revise`). 

To prepare the local environment:

1. Ensure you have Python 3.10+ installed.
2. Open your terminal and navigate to the project root.
3. Install the required dependencies and the local `mono-designer` package in editable mode:
   ```bash
   pip install mcp pydantic
   pip install -e ./mono-designer
   ```
4. You do not need to leave the server running in a separate terminal. Your AI agent will spawn the server process (via `stdio`) using the configuration in the next step.

## 2. Configuring Your Agent

You need to tell your AI agent how to start and communicate with this local MCP server.

### For Claude Code
Add the server configuration to your global settings (`~/.claude/settings.json`) or your project-level config (`.mcp.json`):

```json
{
  "mcpServers": {
    "mono-tui": {
      "command": "python3",
      "args": ["/home/coreyt/projects/monospace-design-tui/mcp-server/server.py"]
    }
  }
}
```
*(Ensure the absolute path matches your local machine's directory structure if you move the project).*

### For Gemini CLI
Gemini CLI also supports MCP servers. You can add the MCP server to your workspace configuration by running:
```bash
gemini mcp add mono-tui python3 /home/coreyt/projects/monospace-design-tui/mcp-server/server.py
```

## 3. Installing the `mono-tui-design` Skill Locally

The `mono-tui-design` skill provides the agent with the precise system prompt, rules, and workflows (the "Senior Product Architect" persona) required to design Monospace TUIs correctly.

**To install this skill locally for Gemini CLI:**

1. Run the installation command pointing to the local skill directory:
   ```bash
   gemini skills install ./skills/mono-tui-design --scope workspace
   ```
   *(Alternatively, if you have packaged it into a `.skill` file, you can point to the `.skill` file instead).*
2. Start an interactive Gemini CLI session (or go to your open one).
3. Reload your skills to ensure it's picked up:
   ```
   /skills reload
   ```
4. Verify the skill is loaded by running `/skills list`.

## 4. Sample UAT Scenario

Once your agent is connected to the MCP server and has the skill loaded, paste the following prompt into your agent (Claude Code or Gemini CLI) to begin the UAT process:

> **Prompt:**
> "Activate the `mono-tui-design` skill. I want to design a simple TUI for viewing local Docker containers. The user should be able to see a list of running containers, select one to view its logs in a detail pane, and have a footer action to stop or restart the selected container. Please guide me through the design generation workflow starting with the workflow definition and then the screen design."

## 5. Reviewing the Generated Output

As the agent executes the workflow, it will automatically call the MCP server tools (`design_generate`, `design_revise`, etc.). Follow these steps to evaluate the outputs:

1. **ASCII Projection (Visual Review):** 
   The agent will present an ASCII structural wireframe in the chat returned by the server. Review this visual representation to ensure the regions (`region_a`, `region_b`, `footer`), focus orders, and layout match your expectations for the Docker container monitor.
2. **YAML Artifacts (Source of Truth):** 
   Check the `dev/designer/workflows/` and `dev/designer/screens/` directories in your workspace. You should see new canonical YAML files. Verify that the schema constraints (e.g., regions, focus arrays, footer keys) are strictly followed.
3. **Revisions (Patching):** 
   Ask the agent to make a change (e.g., "Change the 'Stop' action to 'Pause'"). It MUST use the `design_revise` tool to surgically patch the YAML via JSON deep-merge. Verify the YAML updates correctly without losing surrounding context or breaking indentation.
4. **Linting (Integrity Check):** 
   Finally, ask the agent to run the `design_lint` tool against the `dev/designer/` directory to ensure your new TUI designs have no broken relational links (e.g., missing workflows) or heuristics violations.