from mcp.server import MCPServer


mcp = MCPServer("Max_MCP")

# Internal implementation
def execute_ms(code: str) -> str:
    listener = ""
    return listener
    
@mcp.tool(
        name="execute scripts"
        description="Executes MaxScripts (.ms) code in active 3ds max"
)
def execute_script(code: str) -> str:
    return execute_ms(code)


if __name__ == "__main__":
    mcp.run()
