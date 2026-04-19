# Distributing the Monospace MCP Server for Claude Code

This guide outlines the process for publishing and distributing the `mono-mcp-server` so that it can be easily installed and used by Anthropic's Claude Code and other generic MCP clients.

## Ecosystem Overview

The Model Context Protocol (MCP) ecosystem supports multiple ways to distribute servers. Because `mono-mcp-server` is written in Python, the primary distribution mechanism should be **PyPI (Python Package Index)**. 

While there are MCP registries and marketplaces, they primarily act as discovery layers (directories) that point back to standard package managers (npm, PyPI) or GitHub repositories.

### Recommended Distribution Channels

1.  **PyPI (Primary):** Publishing to PyPI allows users to run the server on-demand using `uvx`, without needing manual installation steps.
2.  **Smithery.ai (Discovery/Hosting):** A popular third-party marketplace that acts as the "Vercel for MCP". Connecting the GitHub repository allows users to discover the server and even use hosted versions.
3.  **Official MCP Registry (Metadata):** Managed by Anthropic (`registry.modelcontextprotocol.io`), this is the upstream source of truth. Registering here ensures official namespace verification (e.g., `io.github.yourusername/mono-mcp-server`).

## 1. Preparing the Python Package

Before publishing, ensure `mcp-server/pyproject.toml` defines a console script entry point so that `uvx` knows what command to execute.

```toml
# mcp-server/pyproject.toml
[project]
name = "mono-mcp-server"
version = "0.3.0"
# ...

[project.scripts]
mono-mcp-server = "server:main" # Update with actual module and function path
```

## 2. Publishing to PyPI

You can use standard Python packaging tools or `uv` to build and publish the package.

```bash
cd mcp-server

# If using uv (recommended):
uv build
uv publish

# Or using standard tools:
python -m build
twine upload dist/*
```

## 3. Registering for Discovery (Optional but Recommended)

*   **Smithery.ai:** Add a `smithery.yaml` and `smithery.json` to your repository root and link the repo on the Smithery website.
*   **Official Registry:** Use the MCP Publisher CLI to create a `server.json` manifest and run the `publish` command to claim your namespace.

---

## Installing in Claude Code

Once published to PyPI, users do not need to `pip install` the server manually. They can use `uvx` (which creates an isolated, ephemeral environment) directly from within Claude Code.

### Installation Command

Instruct users to run the following command in their terminal (where Claude Code is installed):

```bash
claude mcp add mono-mcp-server uvx mono-mcp-server
```

**Breakdown of the command:**
*   `claude mcp add`: The Claude Code CLI command to register a new server.
*   `mono-mcp-server`: The local alias the user is assigning to this server.
*   `uvx`: The command runner that Claude Code will execute.
*   `mono-mcp-server`: The name of the package on PyPI to be executed by `uvx`.

### Managing the Server in Claude Code

Users can view and manage their installed MCP servers using:

*   **List servers:** `claude mcp list`
*   **Remove server:** `claude mcp remove mono-mcp-server`
*   **Interactive UI:** Running `/mcp` inside an active Claude Code session.
