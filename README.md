# doc-discovery-mcp
Build an MCP server and client to search and return documents

### Main distinction to remember
 - MCP client: The protocol bridge in an AI host. It connects, discovers capabilities, makes calls, and returns results to the host/model.

 - MCP server: The controlled adapter around real systems. It exposes tools, resources, and prompts through a standard interface.

   - Tool: Something the model can request to be done.

   - Resource: Something the model can read as context.

   - Prompt: A reusable, user-selected workflow/template.

The best first MCP project for a web developer is usually a small read-only server for a real daily workflow—such as searching project documentation, inspecting a component catalog, or retrieving GitHub issue details—before exposing write access or deployment operations.
