import asyncio

from mcp.client import Client

async def main() -> None:
  async with Client=("http://localhost:8080/mcp") as client:
        result = await client.call_tool("sum_numbers", {"a": 2, "b": 5})
        print (result.structured_content)
  
