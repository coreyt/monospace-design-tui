# Distributing the Mono TUI Design Skill and MCP Server

This guide explains how to package the `mono-tui-design` skill, publish it, and provides instructions for users to install both the skill and the `mono-mcp-server` into **Gemini CLI** and **Codex**.

## 1. Packaging the Skill

The `mono-tui-design` skill is built for Gemini CLI and compatible agentic tools. It must be packaged into a distributable `.skill` file using the Gemini CLI `skill-creator`.

1. Ensure the Gemini CLI `skill-creator` is available on your system.
2. Run the `package_skill.cjs` script against the skill directory:

```bash
node /home/coreyt/.nvm/versions/node/v24.15.0/lib/node_modules/@google/gemini-cli/bundle/builtin/skill-creator/scripts/package_skill.cjs ./skills/mono-tui-design ./dist
```

This process validates the `SKILL.md` frontmatter, checks for missing references, and produces a zipped `mono-tui-design.skill` file in the `dist/` directory.

## 2. Publishing

To distribute the skill and the MCP server:

- **Skill File:** Attach the generated `mono-tui-design.skill` file to your GitHub Releases or distribute it directly to users.
- **MCP Server:** Publish the `mcp-server` directory as a Python package to PyPI (e.g., `mono-mcp-server`), or instruct users to clone the repository and run it locally.

---

## 3. Installation Instructions for Users

### Gemini CLI

#### Installing the Skill
Users can install the packaged `.skill` file directly into their workspace or globally using the Gemini CLI:

```bash
# Install to the current workspace
gemini skills install path/to/mono-tui-design.skill --scope workspace

# Or install globally for the user
gemini skills install path/to/mono-tui-design.skill --scope user
```

*Note: After installation, users must start an interactive Gemini CLI session and run `/skills reload` to enable the new skill.*

#### Configuring the MCP Server
To give Gemini CLI access to the design system's tools, add the MCP server using the `gemini mcp add` command:

```bash
# Using a local Python script
gemini mcp add mono-tui python /path/to/monospace-design-tui/mcp-server/server.py

# Or if published via uvx/PyPI
gemini mcp add mono-tui uvx mono-mcp-server
```

### Codex

Codex is an agentic IDE/CLI tool that supports both standard skill directories and the Model Context Protocol (MCP).

#### Installing the Skill
Codex supports skills natively. To install the skill in Codex, users extract the skill folder and place it in the Codex skills directory:

1. Unzip the `mono-tui-design.skill` file to extract the skill folder (which contains `SKILL.md`).
2. Place the folder into your project's `.codex/skills/` directory (for workspace scope) or `~/.codex/skills/` (for global scope).

```bash
mkdir -p .codex/skills
cp -r path/to/extracted/mono-tui-design .codex/skills/
```

Alternatively, if running Codex interactively, users can type `$` to bring up the skill menu, select **Skill Installer**, and provide the path or URL to the skill.

#### Configuring the MCP Server
Codex uses TOML for its configuration. You can add the MCP server to Codex via the CLI or by manually editing the configuration file.

**Via CLI:**
```bash
# Add a local Python server
codex mcp add mono-tui -- python /path/to/monospace-design-tui/mcp-server/server.py
```

**Via Manual Configuration:**
Add the following configuration to `~/.codex/config.toml` (global) or `.codex/config.toml` (project-specific):

```toml
[mcp_servers.mono-tui]
command = "python"
args = ["/path/to/monospace-design-tui/mcp-server/server.py"]
```

Once configured, Codex will be able to utilize the `mono-tui` MCP tools alongside the instructions provided by the `mono-tui-design` skill.