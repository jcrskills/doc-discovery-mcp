from mcp.server import MCPServer

mcp=MCPServer(calculator)


@mcp.tool()
def sum_numbers(a: int, b: int) -> int:
  """
  Add user input numbers and return result
  """
  return a + b


@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
  """
  Greet someone by name
  """
  return f"Hello, {name}"
